#!/usr/bin/env python3
"""Validate the initial file-based STS Control Desk records."""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORD_DIRS = ("milestones", "approvals", "risks", "verifications", "evidence", "decisions", "checkpoints")
REQUIRED = {"id", "record_type", "project_id", "created_at", "updated_at"}
ALLOWED_TYPES = {"milestone", "approval", "risk", "verification", "evidence", "decision", "checkpoint"}
ALLOWED_STATUSES = {
    "proposed", "observing", "understanding", "scoped", "awaiting_approval",
    "approved", "executing", "verifying", "checkpoint_ready", "complete",
    "blocked", "rejected", "paused", "cancelled", "requires_rework",
    "pending", "approved_with_conditions", "deferred", "revoked", "expired",
    "open", "closed", "in_progress", "verified", "failed",
}
ALLOWED_RISK_LEVELS = {"low", "medium", "high", "critical"}
ALLOWED_STAGES = {
    "mission", "current_state", "problem", "scoped", "out_of_scope",
    "risks", "acceptance_criteria", "human_approval", "executing",
    "verifying", "git_checkpoint", "lessons_learned", "next_milestone",
    "approved", "checkpoint_ready", "complete",
}


def parse_front_matter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing YAML front matter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path}: unterminated YAML front matter"]

    values: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*)(.*)$", line)
        if not match:
            errors.append(f"{path}:{number}: unsupported front-matter line")
            continue
        key, value = match.groups()
        values[key] = value.strip()
    return values, errors


def validate_record(path: Path) -> list[str]:
    values, errors = parse_front_matter(path)
    missing = REQUIRED - values.keys()
    errors.extend(f"{path}: missing required field '{key}'" for key in sorted(missing))

    record_id = values.get("id", "")
    if record_id and path.stem != record_id:
        errors.append(f"{path}: filename ID '{path.stem}' does not match metadata ID '{record_id}'")
    record_type = values.get("record_type", "")
    if record_type and record_type not in ALLOWED_TYPES:
        errors.append(f"{path}: unsupported record_type '{record_type}'")
    status = values.get("status", "")
    if status and status not in ALLOWED_STATUSES:
        errors.append(f"{path}: unsupported status '{status}'")
    for field in ("created_at", "updated_at"):
        value = values.get(field, "")
        if not value:
            errors.append(f"{path}: field '{field}' must not be empty")
            continue

        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"{path}: field '{field}' is not an ISO 8601 timestamp")
    if record_type == "milestone":
        risk_level = values.get("risk_level", "")
        if risk_level not in ALLOWED_RISK_LEVELS:
            errors.append(f"{path}: unsupported or missing milestone risk_level '{risk_level}'")
        current_stage = values.get("current_stage", "")
        if current_stage not in ALLOWED_STAGES:
            errors.append(f"{path}: unsupported or missing milestone current_stage '{current_stage}'")
    if record_type == "milestone" and values.get("milestone_id") != record_id:
        errors.append(f"{path}: milestone_id must match id for milestone records")
    return errors


def validate_references(records: list[Path]) -> list[str]:
    known_ids = set()
    metadata_by_path: dict[Path, dict[str, str]] = {}
    errors: list[str] = []
    for path in records:
        values, parse_errors = parse_front_matter(path)
        errors.extend(parse_errors)
        metadata_by_path[path] = values
        if values.get("id"):
            if values["id"] in known_ids:
                errors.append(f"{path}: duplicate record ID '{values['id']}'")
            known_ids.add(values["id"])
    for path, values in metadata_by_path.items():
        for field in ("milestone_id", "approval_id", "verification_id", "next_milestone_id"):
            value = values.get(field, "")
            if value and value != "null" and value not in known_ids:
                errors.append(f"{path}: {field} references missing record '{value}'")
    return errors


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)", text):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path}: broken local link '{target}'")
    return errors


def main() -> int:
    errors: list[str] = []
    records = sorted(
        path
        for name in RECORD_DIRS
        if (ROOT / name).exists()
        for path in (ROOT / name).glob("*.md")
    )
    for path in records:
        errors.extend(validate_record(path))
        errors.extend(validate_links(path))
    errors.extend(validate_references(records))
    if errors:
        print("Control Desk validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Control Desk validation passed: {len(records)} record(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

