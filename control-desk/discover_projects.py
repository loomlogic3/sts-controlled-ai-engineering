#!/usr/bin/env python3
"""Discover STS project candidates under explicitly approved roots.

Discovery is read-only. It reports candidates but never modifies projects.json.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


def candidate(root: Path, manifest_name: str, max_depth: int) -> list[dict[str, object]]:
    found: list[dict[str, object]] = []
    root = root.resolve()
    if not root.is_dir():
        return found
    for current, directories, files in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        depth = len(current_path.relative_to(root).parts)
        directories[:] = [directory for directory in directories if directory not in {".git", ".venv", "node_modules"}]
        if depth > max_depth:
            directories[:] = []
            continue
        if manifest_name not in files:
            continue
        manifest_path = current_path / manifest_name
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            project_id = manifest.get("project_id")
            display_name = manifest.get("display_name")
            control_desk = manifest.get("control_desk", "control-desk")
            valid = all(isinstance(value, str) and value for value in (project_id, display_name))
            control_desk_ready = isinstance(control_desk, str) and (current_path / control_desk).is_dir()
            manifest_status = manifest.get("control_desk_status", "ready" if control_desk_ready else "not_initialized")
            valid = valid and manifest_status in {"ready", "initialized", "not_initialized"}
            found.append({
                "project_id": project_id,
                "display_name": display_name,
                "repository_path": str(current_path),
                "manifest_path": str(manifest_path),
                "control_desk": control_desk,
                "valid": valid,
                "indexable": valid and control_desk_ready,
                "reason": ("valid manifest and Control Desk ready" if control_desk_ready else "valid manifest; Control Desk initialized with no records" if manifest_status == "initialized" else "valid manifest; Control Desk not initialized") if valid else "invalid manifest",
            })
        except (OSError, json.JSONDecodeError) as error:
            found.append({
                "repository_path": str(current_path),
                "manifest_path": str(manifest_path),
                "valid": False,
                "reason": f"cannot read manifest: {error}",
            })
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("discovery.json"))
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    candidates: list[dict[str, object]] = []
    for configured_root in config.get("approved_roots", []):
        root = (args.config.parent / configured_root).resolve()
        candidates.extend(candidate(root, config.get("manifest_name", ".sts-project.json"), int(config.get("max_depth", 0))))
    unique = {item.get("repository_path"): item for item in candidates}
    print(json.dumps({
        "discovery_status": "completed",
        "read_only": True,
        "approved_roots": [str((args.config.parent / root).resolve()) for root in config.get("approved_roots", [])],
        "candidates": list(unique.values()),
        "next_action": "Review candidates and explicitly approve eligible projects for projects.json.",
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

