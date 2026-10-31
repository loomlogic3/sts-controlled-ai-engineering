#!/usr/bin/env python3
"""Run a local-only, read-only tenant-scoped prototype over the SQLite projection."""

from __future__ import annotations

import argparse
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse


class PrototypeHandler(BaseHTTPRequestHandler):
    database: Path

    def _send_json(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read(self) -> sqlite3.Connection:
        uri = f"file:{self.database.resolve()}?mode=ro"
        return sqlite3.connect(uri, uri=True)

    def do_GET(self) -> None:  # noqa: N802
        path = [unquote(part) for part in urlparse(self.path).path.split("/") if part]
        try:
            if path == ["health"]:
                with self._read() as connection:
                    connection.execute("SELECT 1").fetchone()
                self._send_json(200, {"status": "ok", "read_only": True, "prototype": True})
                return
            if path == ["projects"]:
                with self._read() as connection:
                    rows = connection.execute(
                        "SELECT project_id, display_name, last_indexed_at, last_index_status "
                        "FROM projects WHERE enabled = 1 ORDER BY project_id"
                    ).fetchall()
                self._send_json(200, {"projects": [dict(zip(("project_id", "display_name", "last_indexed_at", "last_index_status"), row)) for row in rows]})
                return
            if len(path) == 3 and path[0] == "projects" and path[2] == "milestones":
                project_id = path[1]
                with self._read() as connection:
                    project = connection.execute(
                        "SELECT project_id, display_name FROM projects WHERE project_id = ? AND enabled = 1",
                        (project_id,),
                    ).fetchone()
                    if project is None:
                        self._send_json(404, {"error": "unknown project"})
                        return
                    rows = connection.execute(
                        "SELECT record_id, status, source_path, source_commit, source_hash, indexed_at "
                        "FROM records WHERE project_id = ? AND record_type = 'milestone' AND active = 1 "
                        "ORDER BY record_id",
                        (project_id,),
                    ).fetchall()
                fields = ("record_id", "status", "source_path", "source_commit", "source_hash", "indexed_at")
                self._send_json(200, {"project": dict(zip(("project_id", "display_name"), project)), "milestones": [dict(zip(fields, row)) for row in rows]})
                return
            self._send_json(404, {"error": "not found"})
        except (OSError, sqlite3.Error) as error:
            self._send_json(500, {"error": "prototype read failed", "detail": str(error)})

    def log_message(self, format: str, *args: object) -> None:
        return


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=Path(__file__).with_name("control-desk.sqlite3"))
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8766)
    args = parser.parse_args()
    if args.host not in {"127.0.0.1", "localhost", "::1"}:
        parser.error("prototype must bind to loopback")
    PrototypeHandler.database = args.database
    server = ThreadingHTTPServer((args.host, args.port), PrototypeHandler)
    print(f"Local-only prototype: http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
