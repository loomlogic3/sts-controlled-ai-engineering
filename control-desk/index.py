#!/usr/bin/env python3
"""Print a read-only summary of file-based Control Desk records."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RECORD_DIRS = ("milestones", "approvals", "risks", "verifications", "evidence", "decisions", "checkpoints")


def metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    result: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    return result


def main() -> int:
    records = []
    for directory in RECORD_DIRS:
        folder = ROOT / directory
        if folder.exists():
            records.extend(metadata(path) for path in sorted(folder.glob("*.md")))
    records = [record for record in records if record]

    milestones = [record for record in records if record.get("record_type") == "milestone"]
    print("STS Control Desk — read-only index")
    print(f"Records: {len(records)}")
    print(f"Milestones: {len(milestones)}")
    for milestone in milestones:
        milestone_id = milestone.get("id", "unknown")
        linked = [
            record["id"]
            for record in records
            if record.get("milestone_id") == milestone_id and record.get("id") != milestone_id
        ]
        print(f"- {milestone_id}: {milestone.get('status', 'unknown')} / {milestone.get('current_stage', 'unknown')}")
        print(f"  linked: {', '.join(sorted(linked)) or 'none'}")
    print("Source of truth: Markdown records under control-desk/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

