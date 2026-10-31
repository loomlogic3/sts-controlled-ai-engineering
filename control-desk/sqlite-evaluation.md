# SQLite Evaluation for the Cross-Project STS Control Desk

## Decision question

Can SQLite provide a trustworthy read-only index across all STS projects while preserving each repository's authority, auditability, and control boundaries?

## Recommendation

Yes. SQLite is justified as a local, rebuildable projection for cross-project discovery and dashboard queries.

It should not initially replace Markdown records inside project repositories. Each STS project remains authoritative for its own milestone, approval, risk, evidence, verification, and checkpoint records. The central SQLite database stores indexed copies with provenance and freshness metadata.

```text
STS project repositories
        ↓ read-only indexing
Central SQLite projection
        ↓ read-only queries
Future STS Control Desk dashboard
```

## Why file-only becomes insufficient

The file-based model remains the right source of truth, but a Control Desk covering all STS projects will need to:

- Search milestones across repositories.
- Filter by project, status, owner, risk, approval state, and freshness.
- Show cross-project blockers and overdue controls.
- Join milestones to approvals, risks, evidence, verification, and Git checkpoints.
- Detect duplicate IDs, stale records, schema drift, and unreachable repositories.
- Produce a consistent overview without opening every repository manually.

SQLite provides these query and relationship capabilities without requiring a database server.

## Proposed authority model

| Layer | Authority | Responsibility |
|---|---|---|
| Project Markdown | Authoritative | Human-readable milestone and control records. |
| Project Git history | Authoritative history | Reviewable changes and recovery checkpoints. |
| SQLite database | Derived projection | Cross-project indexing, search, joins, and freshness reporting. |
| Dashboard | Derived presentation | Read-only visibility into the projection. |

The database must be rebuildable from project repositories. A lost or corrupted database must not destroy project history.

## Project discovery

The index should read an explicit project registry rather than recursively scanning broad filesystem locations.

Each registered project should provide:

```yaml
project_id: sts-controlled-ai-engineering
display_name: STS Controlled AI Engineering
repository_path: /approved/path/to/repository
default_branch: main
enabled: true
visibility: private
```

The registry itself requires human review. A repository's presence does not imply permission to read sensitive data or index it.

## Provenance and freshness

Every indexed record should retain:

- `project_id`
- `record_id`
- `record_type`
- `source_path`
- `source_repository`
- `source_commit`
- `source_hash`
- `indexed_at`
- `source_updated_at`
- `parser_version`
- `schema_version`
- `read_status`

The dashboard must distinguish:

- Current index
- Stale index
- Failed indexing
- Repository unavailable
- Invalid source record
- Record deleted from source

An old indexed record must never appear current merely because it remains in SQLite.

## Initial logical schema

```text
projects
project_sources
records
milestones
approvals
risks
acceptance_criteria
verifications
evidence
decisions
checkpoints
record_links
index_runs
index_errors
```

The `records` table should preserve common metadata and raw Markdown. Type-specific tables may expose queryable fields. `record_links` should represent relationships without relying only on copied text.

Important constraints:

- `(project_id, record_id)` is unique.
- A record cannot be current without successful parsing.
- Source commit and source hash are required for indexed records.
- Foreign keys are enabled.
- Deletes and source disappearance are recorded as tombstones or explicit inactive states.
- Index runs are append-only audit records.

## Security and control boundaries

The first SQLite index must be:

- Read-only with respect to project repositories.
- Local-first and access-controlled.
- Explicitly limited to registered projects.
- Secret-aware and redacting.
- Unable to approve milestones or trigger execution.
- Unable to deploy, message external systems, or change source records.

The indexer should refuse to ingest files containing prohibited secret patterns where practical and should never copy credentials, private keys, tokens, or unredacted sensitive personal data into the database.

## Sync model

The first sync should be explicit and observable:

1. Load the approved project registry.
2. Confirm each repository path and branch.
3. Read only the defined `control-desk/` paths.
4. Record source commit before parsing.
5. Validate records.
6. Upsert valid records with provenance.
7. Record invalid records in `index_errors` without presenting them as current.
8. Mark records absent from a successful source scan as inactive.
9. Record the completed index run and summary.

Automatic scheduling should be a later milestone. The first implementation should be manually invoked and dry-run capable.

## SQLite decision gate

Proceed to implementation only when:

- The project registry format is approved.
- Source paths and visibility boundaries are explicit.
- The database schema and migrations are versioned.
- A full rebuild from repositories is possible.
- Stale, invalid, deleted, and unavailable source states are visible.
- Secret and sensitive-data handling is tested.
- The indexer is read-only and manually invoked.
- A sample of multiple STS projects passes validation.

## Not yet approved

This evaluation does not authorize:

- Building the dashboard UI.
- Automatic repository discovery.
- Background sync or scheduled jobs.
- Editing project records through SQLite.
- Replacing Markdown as the source of truth.
- Production deployment or external publication.

