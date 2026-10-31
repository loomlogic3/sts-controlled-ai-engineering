# File-Based Control Desk

This directory defines the initial repository-native storage model for the STS Control Desk.

Markdown is the authoritative human-readable record. Structured metadata is stored in YAML front matter so a future read-only desk, validator, or SQLite index can consume the records without changing their meaning.

## Proposed layout

```text
control-desk/
├── README.md
├── schema.md
├── milestones/
├── approvals/
├── risks/
├── verifications/
├── evidence/
├── decisions/
└── checkpoints/
```

Create a record only when it exists. Empty directories are not required to be committed.

## Record rules

- Every record has a stable ID.
- IDs are never reused.
- A record links to its project and milestone where applicable.
- The YAML front matter contains summary and indexing fields.
- The Markdown body contains the detailed human-readable record.
- Sensitive values, secrets, credentials, and private keys must never be stored here.
- Changes remain reviewable through Git diffs.
- A record may summarize another record, but must link to the source rather than silently duplicate authoritative content.
- Historical decisions and transitions are retained; they are not overwritten to hide prior state.

## Authoritative versus derived data

Authoritative records are the Markdown files committed to the repository. A dashboard, search index, or future SQLite database is derived from those records until an explicitly approved migration changes the source of truth.

Derived data must be rebuildable. Losing a generated index must not lose milestone history.

Run the initial read-only tools with:

```sh
python3 control-desk/validate.py
python3 control-desk/index.py
python3 control-desk/render.py > /tmp/sts-control-desk.html
```

Run the initial read-only validator with:

```sh
python3 control-desk/validate.py
```

## Initial record naming

Use lowercase record type and stable ID:

```text
milestones/M-2026-001.md
approvals/A-2026-001.md
risks/R-001.md
verifications/V-2026-001.md
evidence/E-2026-001.md
decisions/D-2026-001.md
checkpoints/C-2026-001.md
```

The filename ID and front-matter `id` must match.

## First implementation boundary

This storage model supports inspection, review, and future read-only indexing. It does not authorize automatic execution, approval, deployment, or scope changes.

For cross-project indexing, see [`sqlite-evaluation.md`](sqlite-evaluation.md). SQLite is treated as a rebuildable projection; project Markdown remains authoritative.

The explicit project registry is [`projects.json`](projects.json), and the manually invoked indexer is [`index_sqlite.py`](index_sqlite.py):

```sh
python3 control-desk/index_sqlite.py --database control-desk/control-desk.sqlite3
python3 control-desk/render.py --database control-desk/control-desk.sqlite3 > control-desk/dashboard.html
```

The SQLite database and generated HTML are rebuildable artifacts. They are not authoritative and should remain uncommitted unless a separate publication milestone explicitly requires an artifact snapshot.

Controlled discovery uses [`discovery.json`](discovery.json), project manifests named `.sts-project.json`, and the read-only [`discover_projects.py`](discover_projects.py). Discovery reports candidates; a human must approve onboarding into `projects.json`.

The manifest may declare `control_desk_status` as `ready`, `initialized`, or `not_initialized`. An `initialized` project has a Control Desk location but may have zero records; it is visible to the index as an empty project until real records are imported. A `not_initialized` project is discoverable but not indexable.

