# OKCI Architecture and Classification

## 1. Document status, authority, and scope

This is the Stage 1 foundational architecture and vocabulary document for
Operational Knowledge & Command Intelligence (OKCI). It implements the approved
architecture and classification boundary in
[`assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md`](../assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md),
whose final review copy was confirmed identical before implementation.

OKCI is defined here as a reusable knowledge layer for explaining commands and
guiding command selection. This document establishes architecture,
responsibility boundaries, and classification vocabulary only. It does not
authorize execution, publication, deployment, or any consequential action; a
classification or guidance entry is not permission.

The STS lifecycle, approval, evidence, verification, and completion
requirements remain canonical in [`METHOD.md`](../METHOD.md). The STS Control
Desk authority and lifecycle boundaries remain canonical in
[`CONTROL-DESK.md`](../CONTROL-DESK.md), with its record storage model in
[`control-desk/README.md`](../control-desk/README.md) and
[`control-desk/schema.md`](../control-desk/schema.md).

## 2. OKCI responsibility and boundaries

OKCI provides reusable command knowledge and command-selection guidance. Its
conceptual responsibilities include:

- command purpose and intent;
- syntax and constraints;
- prerequisites and operational context;
- effects and risk classifications;
- compatibility considerations;
- verification status and provenance references, as defined by later stages;
- limitations and known unknowns.

OKCI is not:

- a command execution engine;
- an approval authority;
- a substitute for human judgment;
- an evidence generator that can assert verification without evidence;
- a mechanism for changing Control Desk state; or
- authorization to execute commands merely because they exist in a registry.

## 3. Three-layer architecture

### Layer A — OKCI

OKCI owns reusable command knowledge, classifications, and guidance. It may
describe intended behavior and reference authoritative records, but it does not
execute commands, approve actions, create evidence by assertion, or declare an
action authorized.

### Layer B — Project operational profiles

Project operational profiles own project-specific context: repository paths,
entry points, environment, workflows, operational constraints, and
project-specific command applicability. A profile is authoritative only for
the project context and scope it explicitly declares. It does not replace
project status, approvals, verification records, or the STS method.

### Layer C — STS Control Desk

The STS Control Desk is authoritative for approvals, milestones, risks,
execution evidence, verification, freshness, invalidation, decisions,
checkpoints, and history. OKCI and project profiles reference that authority;
they do not reproduce, replace, advance, or weaken it.

The layers interact by reference and context: OKCI supplies reusable knowledge,
the project profile constrains its applicability, and the Control Desk governs
authorization and the evidence-backed lifecycle. None of these interactions
turns OKCI classification into permission.

## 4. Authority and responsibility matrix

| Information or responsibility | Authoritative layer | OKCI's permitted role | What OKCI must not do |
|---|---|---|---|
| Reusable command purpose, meaning, and constraints | OKCI | Maintain concise knowledge and limitations | Execute or authorize the command |
| Repository paths, entry points, workflows, and project applicability | Project operational profile | Use the declared context when available | Generalize beyond the declared project scope |
| Human approval and exact approval scope | STS Control Desk | Record or reference the required approval class | Approve, broaden, or imply approval |
| Execution output and evidence | STS Control Desk | Link to authoritative evidence | Invent output or assert evidence |
| Verification result and acceptance-criterion result | STS Control Desk | Summarize with scope and provenance references | Establish or replace verification |
| Milestone state, lifecycle gates, and risks | STS Control Desk | Reference current records | Change Control Desk state or risk acceptance |
| Freshness, invalidation, decisions, checkpoints, and history | STS Control Desk | Reflect referenced status and limitations | Override, conceal, or replace history |

## 5. Classification principles

Classifications are independent dimensions. Assess the actual command in its
actual execution context, including:

- exact command and arguments;
- shell interpretation, quoting, and escaping;
- redirection, pipelines, globbing, and command substitution;
- working directory and environment variables;
- permissions;
- runtime and tool versions;
- target identity and scope;
- authentication;
- reversibility; and
- recovery implications.

Executable names alone are insufficient to determine safety. One command may
have several effects and risk flags, and an operation classification does not
determine approval by itself.

## 6. Operation vocabulary

Use the exact approved values below; one or more may apply:

- `OBSERVE` — inspect environment, repository, or runtime state.
- `INSPECT` — read source, configuration, records, logs, or output.
- `ANALYZE` — validate, compare, parse, calculate, or diagnose.
- `PREPARE` — stage, generate, preview, or plan a later operation.
- `MODIFY` — create, edit, delete, or rewrite local files or data.
- `EXECUTE` — run a program, script, service, test, or process.

`PREPARE` does not automatically mean safe; preparation can write files or
affect external state.

## 7. Effect vocabulary

Use all applicable approved values:

- `FILESYSTEM_READ` — reads files or filesystem state.
- `FILESYSTEM_WRITE` — writes filesystem state, including redirection,
  generated artifacts, databases, caches, and logs.
- `NETWORK_ACCESS` — communicates over a network.
- `PRIVILEGED_ACCESS` — requires or uses elevated or privileged permissions.
- `PROCESS_CREATION` — starts a program, script, service, test, or other
  process.
- `EXTERNAL_STATE_CHANGE` — changes state outside the local working context,
  including publication, remote mutation, or service control.

These effects are distinct and may coexist.

## 8. Risk-flag vocabulary

Use all applicable approved values, based on contextual behavior:

- `DESTRUCTIVE` — the operation can destroy or materially remove or replace
  data, state, or resources.
- `SECRET_EXPOSURE` — secrets or sensitive values may be disclosed or handled
  unsafely.
- `DATA_LOSS` — the target, behavior, recoverability, and consequences make
  loss of information plausible or irretrievable.
- `EXTERNAL_PUBLICATION` — information or changes may be made public or sent
  to an external audience.
- `SERVICE_DISRUPTION` — a service may be degraded, interrupted, or made
  unavailable.

Database writes are not automatically `DATA_LOSS`. That flag requires
assessment of actual behavior, target, recoverability, and consequences.

## 9. Approval requirements

Use the exact approved minimum-control values:

- `NONE` — no human approval is required for the exact operation under the
  stated constraints, while repository instructions still apply.
- `HUMAN_APPROVAL_REQUIRED` — valid approval for the exact operation and scope
  is required before execution.
- `EXPLICIT_HIGH_RISK_APPROVAL` — separate explicit approval, exact target
  confirmation, preflight, minimal scope, and independent post-action
  verification are required.

These classifications describe minimum controls. They do not constitute
approval, permission, or authorization. Actual authorization remains subject
to the applicable STS approval process and Control Desk authority.

## 10. Independent operational dimensions

These dimensions are independent of operation, effects, risks, and approval
requirements:

- `reversibility`: `REVERSIBLE`, `RECOVERABLE`, `PARTIALLY_REVERSIBLE`, or
  `IRREVERSIBLE`.
- `target_scope`: the explicit target kind, target constraints, exclusions,
  and recovery boundary.
- `secret_handling`: `NONE`, `INDIRECT_ONLY`, `SENSITIVE_OUTPUT_POSSIBLE`, or
  `PROHIBITED`.
- `service_impact`: `NONE`, `LOCAL_ONLY`, `DEGRADED`, or `OUTAGE_POSSIBLE`.

No additional enum values are established by Stage 1.

## 11. Unknown behavior and boundary-level stop conditions

Unknown behavior must be recorded rather than optimistically assumed. At the
architecture level, stop when:

- target identity or scope is unknown;
- material side effects are unknown;
- permission or recovery boundaries are unclear;
- authoritative sources conflict;
- required context is missing;
- classification is being treated as permission; or
- the requested action exceeds approved scope.

This document does not implement the complete Stage 6 command-selection
protocol. Later-stage status or selection treatment must preserve unknowns and
must not convert them into authorization.

## 12. Provenance and Control Desk relationship

OKCI may reference authoritative STS records by stable ID and may summarize
their applicable status with scope and limitations. It must not independently
establish or replace approvals, execution evidence, verification, milestone
state, risk acceptance, decisions, checkpoints, or history. Control Desk
Markdown records remain authoritative; derived projections remain derived, as
described in [`control-desk/README.md`](../control-desk/README.md).

## 13. Out-of-scope work and stage boundaries

The following are not implemented in Stage 1:

- command registry;
- command records;
- machine-readable schema;
- validation engine;
- environment profiles;
- project operational profiles;
- templates;
- AI command-selection protocol;
- examples;
- automation;
- execution capability;
- Control Desk integration;
- publication;
- deployment; and
- commercial infrastructure.

The staged roadmap and later gates are defined in the approved
[`IMPLEMENTATION-SPECIFICATION.md`](../assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md).

## 14. Change control and canonical references

Changes to this architecture or classification vocabulary require review
against the approved implementation specification and appropriate
authorization. This document links to canonical STS documentation rather than
copying its lifecycle, record, approval, or Control Desk contents. Future
stages must not silently add, remove, rename, or redefine approved enum values
or authority boundaries.
