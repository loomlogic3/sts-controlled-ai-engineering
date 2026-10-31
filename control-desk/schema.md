# Control Desk Record Schema

This is the initial logical schema for file-based records. It is storage-neutral so the same model can later be represented in SQLite.

## Common fields

Every record includes:

```yaml
id: M-2026-001
record_type: milestone
project_id: sts-controlled-ai-engineering
milestone_id: M-2026-001
created_at: 2026-10-31T00:00:00-04:00
updated_at: 2026-10-31T00:00:00-04:00
status: proposed
owner: human-owner
```

Required fields are `id`, `record_type`, `project_id`, `created_at`, and `updated_at`. Records linked to a milestone also require `milestone_id`.

## Milestone fields

```yaml
record_type: milestone
current_stage: mission
status: proposed
risk_level: low
accountable_human: human-owner
approval_id: null
verification_id: null
git_checkpoint: null
next_milestone_id: null
```

The milestone body contains the full 13-stage record from `templates/milestone.md`.

## Approval fields

```yaml
record_type: approval
milestone_id: M-2026-001
status: pending
decision_owner: human-owner
requested_at: 2026-10-31T00:00:00-04:00
expires_at: null
```

Approval status must distinguish `pending`, `approved`, `approved_with_conditions`, `rejected`, `deferred`, `revoked`, and `expired`.

## Risk fields

```yaml
record_type: risk
milestone_id: M-2026-001
status: open
category: technical
likelihood: possible
impact: moderate
priority: medium
risk_owner: human-owner
```

Risk records must include controls, required evidence, residual risk, review date, and closure conditions in the body.

## Verification fields

```yaml
record_type: verification
milestone_id: M-2026-001
status: in_progress
commit: null
environment: local
verified_by: null
```

Verification records must link each acceptance criterion to expected evidence and an actual result.

## Evidence fields

```yaml
record_type: evidence
milestone_id: M-2026-001
evidence_type: command_output
collected_at: 2026-10-31T00:00:00-04:00
collected_by: human-owner
redacted: true
```

Evidence must identify the claim, stage, or acceptance criterion it supports. Secrets and sensitive personal data are prohibited.

## Transition fields

State transitions remain in the milestone history and may later be indexed as separate events:

```yaml
from_status: proposed
to_status: observing
actor: human-owner
actor_role: accountable_human
transitioned_at: 2026-10-31T00:00:00-04:00
reason: Mission and owner recorded.
evidence_id: E-2026-001
```

## SQLite migration boundary

If the project later adopts SQLite, these logical entities should become tables or views without changing their IDs or meanings. The first migration should import and validate existing Markdown records before any application becomes authoritative.

