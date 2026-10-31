#!/usr/bin/env python3
"""Collect deterministic, read-only Git observations for registered projects."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def observe_project(project: dict[str, object], registry_path: Path) -> dict[str, object]:
    repository = (registry_path.parent / str(project["repository_path"])).resolve()
    if not repository.is_dir():
        return {
            "project_id": project["project_id"],
            "display_name": project.get("display_name"),
            "repository_path": str(repository),
            "observation_status": "unavailable",
            "error": "repository path is not a directory",
        }
    try:
        branch = git(repository, "branch", "--show-current").strip()
        commit = git(repository, "rev-parse", "HEAD").strip()
        status_lines = [line for line in git(repository, "status", "--short").splitlines() if line]
        commits = []
        for line in git(repository, "log", "-20", "--format=%H%x09%aI%x09%s").splitlines():
            commit_id, authored_at, subject = line.split("\t", 2)
            commits.append({"commit": commit_id, "authored_at": authored_at, "subject": subject})
        observation = {
            "project_id": project["project_id"],
            "display_name": project.get("display_name"),
            "repository_path": str(repository),
            "observation_status": "success",
            "branch": branch,
            "head_commit": commit,
            "dirty": bool(status_lines),
            "changed_paths": [line[3:] if len(line) >= 3 else line for line in status_lines],
            "recent_commits": commits,
        }
        canonical = json.dumps(observation, sort_keys=True, separators=(",", ":"))
        observation["state_hash"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
        return observation
    except (OSError, subprocess.CalledProcessError, ValueError) as error:
        return {
            "project_id": project["project_id"],
            "display_name": project.get("display_name"),
            "repository_path": str(repository),
            "observation_status": "error",
            "error": str(error),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "projects.json")
    parser.add_argument("--output", type=Path, help="Write the observation bundle to this JSON path")
    parser.add_argument("--observed-at", help="Override observation time for reproducible fixtures")
    args = parser.parse_args()
    registry = json.loads(args.registry.read_text(encoding="utf-8"))
    bundle = {
        "schema_version": 1,
        "observation_type": "repository_state",
        "observed_at": args.observed_at or datetime.now(timezone.utc).isoformat(),
        "read_only": True,
        "source": "git",
        "projects": [
            observe_project(project, args.registry)
            for project in registry.get("projects", [])
            if project.get("enabled", True)
        ],
    }
    serialized = json.dumps(bundle, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
