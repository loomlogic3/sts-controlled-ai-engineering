# STS Control Desk Specification

## Purpose

The STS Control Desk is the evidence-backed control surface for every project milestone.
It makes the state, authority, risks, evidence, recovery boundary, and next permitted action visible in one place.

The desk is not initially an execution console. The first version is read-only and must not approve work, change scope, run commands, deploy systems, or perform external actions.

## Governing rule

The desk may summarize a record, but it must not imply a stronger state than the underlying evidence supports.

Planned capability remains planned. A milestone is complete only when the completion requirements in `METHOD.md` are satisfied.

## Milestone state machine

### Normal path

```text
Proposed
  -> Observing
  -> Understanding
  -> Scoped
  -> Awaiting Approval
  -> Approved
  -> Executing
  -> Verifying
  -> Checkpoint Ready
  -> Complete
```

### Alternate states

- `Blocked` — progress cannot safely continue because a required condition is missing or failed.
- `Rejected` — the proposed milestone or approval was not accepted.
- `Paused` — work was deliberately paused by an authorised human decision.
- `Cancelled` — the milestone will not be completed.
- `Requires Rework` — evidence or implementation failed and correction is required.

Every transition records:

- Previous state
- New state
- Date and time
- Actor and role
- Reason
- Evidence or linked record

## Control gates

| Transition | Required condition |
|---|---|
| Proposed -> Observing | Mission and owner are recorded. |
| Observing -> Understanding | Current-state evidence is recorded. |
| Understanding -> Scoped | Confirmed facts, inferences, unknowns, and root problem are separated. |
| Scoped -> Awaiting Approval | Scope, exclusions, risks, and acceptance criteria are defined. |
| Awaiting Approval -> Approved | Required human approval is recorded for the exact scope. |
| Approved -> Executing | Approved scope is unchanged and preconditions are satisfied. |
| Executing -> Verifying | Execution steps have recorded results and no active stop condition. |
| Verifying -> Checkpoint Ready | Acceptance criteria are verified or limitations are explicitly accepted. |
| Checkpoint Ready -> Complete | Diff, checkpoint, lessons, and next milestone are recorded. |

No gate may be bypassed because implementation appears simple.

## Control Desk overview

The overview should answer:

- Which milestones are active?
- Which are awaiting approval?
- Which are blocked or have failed verification?
- Which approvals or evidence are stale or expired?
- Which high or critical risks remain open?
- Which milestones are eligible for the next transition?
- What is the single recommended next controlled action?

Minimum summary fields:

| Field | Meaning |
|---|---|
| Milestone ID | Stable identifier for traceability. |
| Title and mission | The intended outcome. |
| State and current stage | Where the milestone is in the lifecycle. |
| Owner and approver | Who is accountable and who authorises. |
| Risk level | Highest applicable risk classification. |
| Gate status | Ready, blocked, stale, or failed. |
| Evidence status | Complete, partial, missing, or stale. |
| Approval status | Not required, pending, valid, expired, or revoked. |
| Verification status | Pending, passed, failed, limited, or blocked. |
| Git checkpoint | Commit or other recovery boundary. |
| Next permitted action | One controlled action, not a general suggestion. |

## Milestone detail view

The detail view must expose the complete record without requiring the user to search unrelated files:

1. Mission and reason
2. Current-state observation and evidence
3. Problem understanding
4. Goal, scope, and exclusions
5. Risks and controls
6. Acceptance criteria
7. Approval and approval boundary
8. Execution steps and results
9. Verification records and evidence
10. Git checkpoint and repository state
11. Lessons learned
12. Next milestone
13. State-transition timeline
14. Linked decisions, risks, approvals, and artifacts

## Traceability model

Every related record has a stable ID and links to its milestone:

```text
M-2026-004
├── A-2026-004  approval
├── R-007       risk
├── AC-04       acceptance criterion
├── V-2026-004  verification
├── E-2026-031  evidence item
├── C-8c31f2a   Git checkpoint
└── M-2026-005  next milestone
```

Records should be linked rather than copied. A summary may be displayed in several views, but the detailed record has one source of truth.

## Freshness and invalidation

The desk must flag records that can no longer be trusted as current:

- Approval expired or revoked
- Evidence older than the defined review window
- Repository changed after approval
- Risk review overdue
- Verification performed against a different commit or environment
- Recovery checkpoint unavailable
- Scope changed after approval

When a material invalidation occurs, the milestone returns to the relevant earlier gate and cannot continue by default.

## Control health

Each milestone displays these independent checks:

- Scope: defined, changed, or unclear
- Approval: valid, pending, expired, or not required
- Risks: controlled, open, escalated, or blocked
- Acceptance criteria: defined, partial, or missing
- Evidence: complete, partial, missing, or stale
- Verification: passed, failed, limited, or pending
- Recovery: available or missing
- Git state: clean, changed, or unknown

The overall milestone state must not be green when a required control is unresolved.

## Initial delivery boundary

The first Control Desk milestone should deliver:

- The state machine and gate definitions
- A canonical milestone data model
- Stable IDs and linked-record conventions
- A read-only overview and detail specification
- Freshness and invalidation rules

It should not deliver:

- Automatic execution
- Automatic approval
- Automatic deployment
- Automatic scope expansion
- Unreviewed changes to project records

## Initial storage model

The first implementation uses Markdown records with YAML front matter under `control-desk/`.
The Markdown files are authoritative; any dashboard, validator, search index, or future
SQLite database is derived until a separately approved migration changes the source of truth.

The logical record fields are defined in [`control-desk/schema.md`](control-desk/schema.md),
and the repository layout and naming rules are defined in [`control-desk/README.md`](control-desk/README.md).

