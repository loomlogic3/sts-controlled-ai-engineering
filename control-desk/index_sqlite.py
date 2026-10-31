#!/usr/bin/env python3
"""Build a read-only, rebuildable SQLite projection of registered STS projects."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path


RECORD_DIRS = ("milestones", "approvals", "risks", "verifications", "evidence", "decisions", "checkpoints")


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip()
    return values


def git_value(repository: Path, *args: str) -> str:
    try:
        result = subprocess.run(["git", "-C", str(repository), *args], check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def schema(connection: sqlite3.Connection) -> None:
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS projects (
            project_id TEXT PRIMARY KEY,
            display_name TEXT NOT NULL,
            repository_path TEXT NOT NULL,
            default_branch TEXT,
            visibility TEXT NOT NULL,
            enabled INTEGER NOT NULL,
            last_indexed_at TEXT,
            last_index_status TEXT
        );
        CREATE TABLE IF NOT EXISTS records (
            project_id TEXT NOT NULL REFERENCES projects(project_id),
            record_id TEXT NOT NULL,
            record_type TEXT NOT NULL,
            milestone_id TEXT,
            status TEXT,
            source_path TEXT NOT NULL,
            source_commit TEXT,
            source_dirty INTEGER NOT NULL,
            source_hash TEXT NOT NULL,
            source_updated_at TEXT,
            indexed_at TEXT NOT NULL,
            parser_version TEXT NOT NULL,
            schema_version INTEGER NOT NULL,
            active INTEGER NOT NULL,
            raw_markdown TEXT NOT NULL,
            PRIMARY KEY (project_id, record_id)
        );
        CREATE TABLE IF NOT EXISTS record_links (
            project_id TEXT NOT NULL,
            from_record_id TEXT NOT NULL,
            to_record_id TEXT NOT NULL,
            relation TEXT NOT NULL,
            PRIMARY KEY (project_id, from_record_id, to_record_id, relation)
        );
        CREATE TABLE IF NOT EXISTS index_runs (
            run_id INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            project_count INTEGER NOT NULL,
            record_count INTEGER NOT NULL,
            error_count INTEGER NOT NULL,
            status TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS index_errors (
            run_id INTEGER NOT NULL REFERENCES index_runs(run_id),
            project_id TEXT,
            source_path TEXT,
            message TEXT NOT NULL
        );
        """
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=Path(__file__).with_name("projects.json"))
    parser.add_argument("--database", required=True, help="SQLite path, or :memory: for a non-persistent dry run")
    args = parser.parse_args()

    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    connection = sqlite3.connect(args.database)
    schema(connection)
    started = now()
    run = connection.execute(
        "INSERT INTO index_runs(started_at, project_count, record_count, error_count, status) VALUES (?, ?, 0, 0, 'running')",
        (started, len(registry.get("projects", []))),
    )
    run_id = run.lastrowid
    indexed = 0
    errors = 0
    try:
        for project in registry.get("projects", []):
            project_id = project["project_id"]
            if not project.get("enabled", False):
                continue
            repository = (args.registry.parent / project["repository_path"]).resolve()
            if not repository.is_dir():
                errors += 1
                connection.execute("INSERT INTO index_errors VALUES (?, ?, ?, ?)", (run_id, project_id, str(repository), "repository path is not a directory"))
                continue
            indexed_at = now()
            commit = git_value(repository, "rev-parse", "HEAD")
            dirty = 1 if git_value(repository, "status", "--porcelain") else 0
            connection.execute(
                "INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(project_id) DO UPDATE SET display_name=excluded.display_name, repository_path=excluded.repository_path, default_branch=excluded.default_branch, visibility=excluded.visibility, enabled=excluded.enabled, last_indexed_at=excluded.last_indexed_at, last_index_status=excluded.last_index_status",
                (project_id, project["display_name"], str(repository), project.get("default_branch"), project.get("visibility", "private"), 1, indexed_at, "running"),
            )
            seen: set[str] = set()
            for directory in RECORD_DIRS:
                folder = repository / "control-desk" / directory
                if not folder.exists():
                    continue
                for path in sorted(folder.glob("*.md")):
                    raw = path.read_text(encoding="utf-8")
                    values = metadata(path)
                    record_id = values.get("id")
                    if not record_id:
                        errors += 1
                        connection.execute("INSERT INTO index_errors VALUES (?, ?, ?, ?)", (run_id, project_id, str(path), "missing record ID"))
                        continue
                    seen.add(record_id)
                    connection.execute(
                        "INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(project_id, record_id) DO UPDATE SET record_type=excluded.record_type, milestone_id=excluded.milestone_id, status=excluded.status, source_path=excluded.source_path, source_commit=excluded.source_commit, source_dirty=excluded.source_dirty, source_hash=excluded.source_hash, source_updated_at=excluded.source_updated_at, indexed_at=excluded.indexed_at, parser_version=excluded.parser_version, schema_version=excluded.schema_version, active=1, raw_markdown=excluded.raw_markdown",
                        (project_id, record_id, values.get("record_type", "unknown"), values.get("milestone_id"), values.get("status"), str(path), commit, dirty, hashlib.sha256(raw.encode("utf-8")).hexdigest(), values.get("updated_at"), indexed_at, "1", 1, 1, raw),
                    )
                    indexed += 1
            existing = connection.execute("SELECT record_id FROM records WHERE project_id = ?", (project_id,)).fetchall()
            for (record_id,) in existing:
                if record_id not in seen:
                    connection.execute("UPDATE records SET active = 0, indexed_at = ? WHERE project_id = ? AND record_id = ?", (indexed_at, project_id, record_id))
            connection.execute("UPDATE projects SET last_index_status = 'success' WHERE project_id = ?", (project_id,))
        status = "success" if errors == 0 else "completed_with_errors"
        connection.execute("UPDATE index_runs SET finished_at = ?, record_count = ?, error_count = ?, status = ? WHERE run_id = ?", (now(), indexed, errors, status, run_id))
        connection.commit()
    except Exception as exc:
        connection.rollback()
        connection.execute("UPDATE index_runs SET finished_at = ?, record_count = ?, error_count = 1, status = 'failed' WHERE run_id = ?", (now(), indexed, run_id))
        connection.commit()
        raise
    finally:
        connection.close()

    print(f"SQLite index run {run_id}: {len(registry.get('projects', []))} project(s), {indexed} record(s), {errors} error(s), status={status}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

