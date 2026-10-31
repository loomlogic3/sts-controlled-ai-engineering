# STS Control Desk Dual-Deployment Architecture

## Status

Architecture definition for M-2026-022. This document is a design boundary, not an implementation or hosting authorization.

## Product boundary

STS Control Desk has two supported deployment modes:

1. **Hosted SaaS** — a multi-tenant service operated by STS or an approved operator.
2. **Self-hosted/local** — an organization-operated deployment for sensitive, regulated, offline, or isolated work.

Both modes provide the same read-oriented control surface. Project repositories remain authoritative unless a later, separately approved migration changes that authority model.

## Trust and authority model

```text
Project repository
  Markdown records, Git history, source authority
          │ explicit read-only connector or local import
          ▼
Control Desk projection
  parsed records, provenance, freshness, audit events
          │ read-only queries
          ▼
Dashboard and reports
  derived presentation, filters, evidence links
```

The projection must visibly identify derived data and must not display a stronger state than the source evidence supports.

## Tenancy model

- An organization is the top-level tenant boundary.
- Projects belong to exactly one organization in a deployment.
- Users, roles, repository connections, records, evidence references, and audit events are tenant-scoped.
- Every query and background operation carries an organization and project scope.
- Cross-organization aggregation is disabled by default.
- Self-hosted mode may operate as a single-organization installation while retaining the same logical boundaries.

Required isolation controls include tenant-scoped authorization, database row or schema isolation, object-storage prefixes, connector scope checks, audit events for access, and isolation tests before production use.

## Deployment responsibilities

| Area | Hosted SaaS | Self-hosted/local |
|---|---|---|
| Runtime and upgrades | Service operator | Organization operator |
| Identity integration | Service identity and optional enterprise SSO | Local identity or organization SSO |
| Repository access | Explicit connector credentials or app installation | Local filesystem or organization-managed connector |
| Data residency | Operator-selected supported region | Organization-controlled |
| Backups and recovery | Service operator with export | Organization operator |
| Availability | Service SLA after separate approval | Organization-defined |
| Destruction/deletion | Tenant-requested and audited | Organization-controlled and audited |

## Connector and synchronization boundary

The first connector contract is read-only and explicit:

- A human registers a repository and approved `control-desk/` paths.
- The connector records repository identity, branch, commit, dirty state, source hash, parser version, and indexing time.
- A sync run is manual or separately approved; scheduling is not implied.
- Source disappearance, invalid records, stale evidence, and unavailable repositories remain visible as non-current states.
- Connectors cannot edit repositories, approve milestones, execute commands, deploy systems, or publish externally.
- Full source-code ingestion is not part of the default contract.

## Security and privacy requirements

- Organization and project authorization is enforced server-side.
- Secrets and private keys are never copied into the projection.
- Credentials use least privilege, rotation, revocation, and auditable access.
- Data is encrypted in transit and at rest where the deployment supports it.
- Audit history is append-oriented and records actor, tenant, action, target, time, and result.
- Retention, export, deletion, and legal-hold behavior are explicit before hosted launch.
- Self-hosted installations must be able to operate without sending source records to a hosted service.

## Freshness and recovery

Every displayed record must expose source commit, source hash, indexed time, source update time when available, and index status. The dashboard distinguishes current, stale, failed, unavailable, invalid, and inactive records.

The projection is rebuildable from approved repositories. A tenant can export its records and provenance. A hosted outage must not destroy source history or prevent a self-hosted rebuild.

## Migration path

1. Keep the current Markdown and local SQLite/HTML workflow as the reference implementation.
2. Define a versioned API and projection schema that preserve existing IDs and meanings.
3. Import a sample export into an isolated development environment.
4. Compare hosted/self-hosted projections against the local reference output.
5. Run tenant-isolation, freshness, deletion, export, backup, and recovery verification.
6. Obtain separate approval before any hosted pilot, external connector, or production deployment.

## Explicit non-goals

This architecture does not authorize public hosting, production deployment, automatic synchronization, repository writes, automatic approvals, execution, deployment, payments, or replacing Markdown as the source of truth.
