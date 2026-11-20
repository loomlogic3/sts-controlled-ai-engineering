# STS-OKCI-001 — Design Refinement

## Document status

- Document type: Design proposal
- Project: STS Controlled AI Engineering
- Repository: `~/sts-repos/sts-controlled-ai-engineering`
- Date: 2026-11-20
- Primary input: `assessments/OKCI-001/INITIAL-ASSESSMENT.md`
- Implementation status: Not begun
- Example commands executed: No
- Dependencies installed: No
- Git commit, push, tag, publication, or deployment performed: No

## Evidence labels

- **Fact:** Directly observed in the current repository or Git state.
- **Historical:** Recorded by existing records but not re-executed during this refinement.
- **Inference:** Reasoned from observed facts.
- **Recommendation:** Proposed future design.
- **Example:** Illustrative documentation only; not authorization or execution evidence.
- **Unresolved:** Requires later investigation or human decision.

## 1. Assessment of the Initial Design

The initial assessment correctly identified that the repository already has the control foundation required for OKCI: `METHOD.md`, `CONTROL-DESK.md`, Control Desk records, templates, checklists, and project registration. It also correctly recommended that OKCI must not create a second approval system, evidence repository, project registry, or milestone state machine.

The design needs these corrections:

1. Command classification must use independent dimensions. An `ANALYZE` command may also write files, create processes, or access a network.
2. Verification status must be separate from environment compatibility.
3. Verification must be scoped evidence, not an unqualified boolean.
4. Control Desk records must remain authoritative for approvals, evidence, verification, freshness, and history.
5. Conflicts, stale versions, and deprecation require explicit handling.
6. Vocabulary and schema approval must precede registry creation.

## 2. Revised Architecture

### 2.1 Three-layer boundary

```text
OKCI
  Reusable command knowledge, classification, compatibility guidance,
  prerequisites, limitations, and links to evidence.

Project operational profile
  Repository-specific structure, entry points, workflows, environments,
  validation procedures, restrictions, and recovery expectations.

STS Control Desk
  Human approvals, milestone state, execution evidence, verification,
  freshness, invalidation, history, risks, and recovery checkpoints.
```

### 2.2 Authority rules

- OKCI is authoritative for reusable command metadata and documented constraints.
- A project profile is authoritative only for the project context and source/review boundary it declares.
- Control Desk Markdown remains authoritative for approvals, evidence, verification, milestones, risks, decisions, and checkpoints.
- OKCI may link to Control Desk records but must not copy their approval or verification decisions as a second authority.
- Indexes and future search products may summarize records but must retain provenance and must not strengthen their status.

### 2.3 Recommended future layout

This is a recommendation only; it is not being created in this phase.

```text
okci/
├── README.md
├── command-registry.yaml
├── classification.md
├── verification-status.md
├── ai-command-selection.md
├── environments/
│   ├── android-termux.yaml
│   ├── linux.yaml
│   ├── macos.yaml
│   └── windows.yaml
├── profiles/
│   └── project-operational-profile.md
├── templates/
│   ├── command-record.yaml
│   └── project-operational-profile.md
└── examples/
    └── command-selection-exercises.md
```

### 2.4 Overlap controls

| Potential overlap | Boundary control |
|---|---|
| OKCI records and verification records | OKCI stores metadata and references; Control Desk stores verification authority |
| Environment and project profiles | Environment profiles describe reusable platform facts; project profiles describe one repository's use |
| Project profiles and project-status records | Profiles describe operating procedures; status records describe a dated readiness checkpoint |
| OKCI approval fields and approvals | OKCI states the approval class required; Control Desk records whether a specific action was approved |
| OKCI freshness and Control Desk freshness | OKCI tracks knowledge review; Control Desk determines whether project evidence and approvals remain current |

## 3. Classification Model

### 3.1 Independent dimensions

#### Operation

- `OBSERVE` — Inspect environment, repository, or runtime state.
- `INSPECT` — Read source, configuration, records, logs, or output.
- `ANALYZE` — Validate, compare, parse, calculate, or diagnose.
- `PREPARE` — Stage, generate, preview, or plan a later operation.
- `MODIFY` — Create, edit, delete, or rewrite local files or data.
- `EXECUTE` — Run a program, script, service, test, or process.

#### Effects

- `FILESYSTEM_READ`
- `FILESYSTEM_WRITE`
- `NETWORK_ACCESS`
- `PRIVILEGED_ACCESS`
- `PROCESS_CREATION`
- `EXTERNAL_STATE_CHANGE`

These are sufficient for the initial model. `FILESYSTEM_WRITE` includes redirection, generated artifacts, databases, caches, and logs.

#### Risk flags

- `DESTRUCTIVE`
- `SECRET_EXPOSURE`
- `DATA_LOSS`
- `EXTERNAL_PUBLICATION`
- `SERVICE_DISRUPTION`

These are sufficient initially. Reversibility, target scope, sensitivity, and service impact should be fields rather than more flags:

- `reversibility`: `REVERSIBLE`, `RECOVERABLE`, `PARTIALLY_REVERSIBLE`, or `IRREVERSIBLE`
- `target_scope`: explicit path, repository, service, account, dataset, or endpoint
- `secret_handling`: `NONE`, `INDIRECT_ONLY`, `SENSITIVE_OUTPUT_POSSIBLE`, or `PROHIBITED`
- `service_impact`: `NONE`, `LOCAL_ONLY`, `DEGRADED`, or `OUTAGE_POSSIBLE`

#### Approval requirement

- `NONE`
- `HUMAN_APPROVAL_REQUIRED`
- `EXPLICIT_HIGH_RISK_APPROVAL`

This describes the minimum control; it is never itself an approval.

### 3.2 Sufficiency and classification procedure

The requested values are sufficient as an initial vocabulary when treated as orthogonal dimensions. Do not add `PUBLISH`, `NETWORK`, or `PRIVILEGED` as operation values; their meaning is already represented by effects, risk flags, target scope, and approval.

Classification must inspect exact arguments, working directory, targets, shell parsing, redirection, pipelines, globbing, command substitution, called scripts, environment variables, runtime, operating system, authentication, permissions, reversibility, and recovery. Unknown behavior must be `PROPOSED` or `BLOCKED`, not optimistically classified.

## 4. Verification Status and Environment Compatibility

### 4.1 Verification statuses

- `VERIFIED` — At least one successful, adequately scoped verification exists and is linked.
- `PROJECT-DOCUMENTED` — Current project documentation supports the command, but current registry execution evidence is absent.
- `HISTORICAL` — Earlier evidence exists but is not current verification.
- `PROPOSED` — Candidate command not yet supported by sufficient evidence.
- `DEPRECATED` — Previously documented but not recommended for new use.
- `BLOCKED` — Known failure, prohibited behavior, missing critical prerequisite, or unresolved safety conflict.

These statuses do not claim universal platform support.

### 4.2 Independent compatibility model

Each environment gets a separate compatibility result:

- `SUPPORTED` — Compatible under the stated constraints.
- `CONDITIONAL` — Compatible only with named shell, version, path, package, or configuration conditions.
- `UNSUPPORTED` — Known not to work or prohibited in the environment.
- `NOT_ASSESSED` — Insufficient environment-specific evidence.

Example:

```yaml
verification_status: VERIFIED
compatibility:
  android-termux:
    status: SUPPORTED
    shell: sh
  macos:
    status: NOT_ASSESSED
    shell: zsh
```

This means verified in at least one scoped context, not universally verified.

### 4.3 Conflict, expiration, and deprecation rules

- Retain conflicting evidence; never overwrite the earlier record.
- Add a newer verification or decision explaining whether the conflict is caused by platform, version, arguments, target, working directory, or project state.
- Narrow compatibility when the command works only in one context.
- Set `BLOCKED` when a safety-relevant conflict prevents reliable recommendation.
- Set `PROPOSED` or compatibility `NOT_ASSESSED` when evidence is insufficient.
- Treat verification as stale when tools, runtimes, scripts, repositories, environments, outputs, or review windows materially change.
- Preserve stale evidence as historical; do not silently promote it.
- A `DEPRECATED` record must identify its replacement, reason, date, and migration limitation.

Recommended freshness fields are `last_verified`, `review_due`, and `stale_reason`.

## 5. Proposed Command-Record Schema

This is a proposed YAML structure, not an implemented registry:

```yaml
schema_version: 1
command_id: CMD-0001
name: inspect-git-status
purpose: "Show the current branch and concise working-tree state."
syntax:
  kind: exact
  command: "git status --short --branch"
  argument_constraints: []
operation: [OBSERVE, INSPECT]
effects: [FILESYSTEM_READ]
risk_flags: []
approval_requirement: NONE
reversibility: REVERSIBLE
target_scope:
  kind: current-repository
  constraints: ["Run only from the intended repository."]
supported_environments: [android-termux, linux, macos, windows]
compatibility:
  android-termux:
    status: NOT_ASSESSED
    shell: sh
    executable: git
    version_constraints: "Not recorded"
    basis: "Not yet verified for the registry"
    last_assessed: null
prerequisites:
  - "Git is installed."
  - "The working directory is the intended repository."
working_directory:
  required: true
  rule: "Repository root or repository subdirectory."
expected_results:
  - "The active branch is identified."
  - "Changed paths, if any, are listed concisely."
verification_procedure:
  - "Confirm the intended repository and branch."
  - "Confirm no files are changed."
failure_conditions:
  - "The directory is not inside a Git repository."
limitations:
  - "Does not display the complete patch."
evidence_references:
  documentation: ["METHOD.md", "control-desk/milestones/M-2026-001.md"]
  control_desk_records: []
verification_status: PROJECT-DOCUMENTED
last_verified: null
review_due: null
source:
  kind: repository-documentation
  references: ["control-desk/milestones/M-2026-001.md"]
  source_commit: null
  provenance_note: "Documented usage; no registry execution performed."
```

### 5.1 Field requirements

| Field | Requirement | Notes |
|---|---|---|
| `schema_version`, `command_id`, `name`, `purpose` | Mandatory | Identity and intended outcome |
| `syntax`, `operation`, `effects`, `risk_flags` | Mandatory | Exact or constrained invocation and dimensions |
| `approval_requirement`, `supported_environments`, `compatibility` | Mandatory | Control and platform context |
| `prerequisites`, `working_directory`, `expected_results` | Mandatory | Preconditions and observable outcome |
| `verification_procedure`, `failure_conditions`, `limitations` | Mandatory | Safe verification and stop conditions |
| `evidence_references`, `verification_status`, `last_verified`, `source` | Mandatory | Provenance and confidence |
| `target_scope`, `reversibility` | Conditional | Required for broad, sensitive, modifying, external, or high-risk targets |
| `secret_handling`, `service_impact` | Conditional | Required when output or service behavior may be sensitive |
| `review_due`, `stale_reason` | Optional but recommended | Required when a review window is defined or verification is stale |

### 5.2 Illustrative records

These examples are proposed documentation only. They were not executed and do not authorize execution.

#### Read-only Git inspection

```yaml
command_id: CMD-GIT-STATUS-001
name: inspect-git-status
purpose: "Inspect the active branch and concise working-tree state."
syntax: {kind: exact, command: "git status --short --branch"}
operation: [OBSERVE, INSPECT]
effects: [FILESYSTEM_READ]
risk_flags: []
approval_requirement: NONE
reversibility: REVERSIBLE
target_scope: {kind: current-repository}
supported_environments: [android-termux, linux, macos, windows]
compatibility:
  android-termux: {status: NOT_ASSESSED, shell: sh, executable: git}
  linux: {status: NOT_ASSESSED, shell: sh, executable: git}
  macos: {status: NOT_ASSESSED, shell: zsh, executable: git}
  windows: {status: NOT_ASSESSED, shell: powershell, executable: git}
prerequisites: ["Git is installed", "The intended repository is current"]
working_directory: {required: true, rule: "Intended repository or subdirectory"}
expected_results: ["Branch and concise working-tree state are reported"]
verification_procedure: ["Confirm target repository and no mutation"]
failure_conditions: ["Not inside a Git repository"]
limitations: ["Does not show the complete diff"]
evidence_references:
  documentation: ["METHOD.md", "control-desk/milestones/M-2026-001.md"]
  control_desk_records: []
verification_status: PROJECT-DOCUMENTED
last_verified: null
source: {kind: repository-documentation}
```

#### Derived SQLite artifact

```yaml
command_id: CMD-CONTROL-DESK-SQLITE-001
name: build-control-desk-sqlite-projection
purpose: "Build a rebuildable SQLite projection from registered Control Desk records."
syntax:
  kind: constrained
  command: "python3 control-desk/index_sqlite.py --database <database-path>"
operation: [ANALYZE, PREPARE, MODIFY, EXECUTE]
effects: [FILESYSTEM_READ, FILESYSTEM_WRITE, PROCESS_CREATION]
risk_flags: [DATA_LOSS]
approval_requirement: HUMAN_APPROVAL_REQUIRED
reversibility: RECOVERABLE
target_scope:
  kind: derived-local-artifact
  constraints: ["Markdown remains authoritative", "Database is disposable and rebuildable"]
supported_environments: [android-termux, linux, macos]
compatibility:
  android-termux: {status: NOT_ASSESSED, shell: sh, executable: python3}
  linux: {status: NOT_ASSESSED, shell: sh, executable: python3}
  macos: {status: NOT_ASSESSED, shell: zsh, executable: python3}
prerequisites: ["Registered paths are approved", "Target is confirmed as derived output"]
working_directory: {required: true, rule: "Repository root"}
expected_results: ["A derived projection is created or refreshed", "Errors and provenance are reported"]
verification_procedure: ["Confirm source files are unchanged", "Check counts, errors, provenance, and rebuildability"]
failure_conditions: ["Target is authoritative or ambiguous", "Invalid sources are silently hidden"]
limitations: ["Writing the database is a filesystem mutation", "Projection is not source of truth"]
evidence_references:
  documentation: ["control-desk/README.md", "control-desk/sqlite-evaluation.md"]
  control_desk_records: ["E-2026-003"]
verification_status: HISTORICAL
last_verified: null
source:
  kind: historical-documentation
  references: ["control-desk/evidence/E-2026-003.md"]
```

#### External publication

```yaml
command_id: CMD-GIT-PUSH-001
name: publish-git-branch
purpose: "Push an explicitly approved local branch to an explicitly approved remote."
syntax:
  kind: constrained
  command: "git push <approved-remote> <approved-branch>"
  argument_constraints: ["No wildcard, implicit target, command substitution, or automatic retry"]
operation: [EXECUTE]
effects: [FILESYSTEM_READ, NETWORK_ACCESS, PROCESS_CREATION, EXTERNAL_STATE_CHANGE]
risk_flags: [EXTERNAL_PUBLICATION]
approval_requirement: EXPLICIT_HIGH_RISK_APPROVAL
reversibility: PARTIALLY_REVERSIBLE
target_scope:
  kind: remote-repository
  constraints: ["Exact remote, branch, repository, and commit are approved"]
supported_environments: [android-termux, linux, macos, windows]
compatibility:
  android-termux: {status: NOT_ASSESSED, shell: sh, executable: git}
  linux: {status: NOT_ASSESSED, shell: sh, executable: git}
  macos: {status: NOT_ASSESSED, shell: zsh, executable: git}
  windows: {status: NOT_ASSESSED, shell: powershell, executable: git}
prerequisites: ["Exact publication approval exists", "Preflight and recovery controls pass"]
working_directory: {required: true, rule: "Intended repository and approved branch"}
expected_results: ["Only the approved branch is published"]
verification_procedure: ["Record actual remote, branch, commit, and result", "Independently inspect remote state"]
failure_conditions: ["Approval absent or expired", "Target ambiguous", "Preflight or independent verification fails"]
limitations: ["Publication may not be reversible after consumers act", "This is not authorization"]
evidence_references:
  documentation: ["METHOD.md", "checklists/before-commit.md"]
  control_desk_records: []
verification_status: PROPOSED
last_verified: null
source: {kind: method-and-checklist}
```

## 6. Verification Evidence Model

### 6.1 Verification event

An execution verification should capture, where applicable:

- Command ID
- Exact command and arguments after safe redaction
- Working directory
- Operating system and shell
- Runtime and tool versions
- Date and time with timezone
- Repository, branch, commit, or target identity
- Exit code
- Actual observed result
- Evidence reference
- Limitations
- Verification scope
- Reviewer or independent verifier when required

Example scope:

```yaml
verification_scope:
  platform: android-termux
  shell: sh
  runtime: "Python 3.x"
  tool_versions: {}
  repository_commit: null
  target: "safe-or-redacted-target"
result: PASS
limitations: []
```

### 6.2 Control Desk relationship

OKCI should reference existing records by stable ID:

- `E-2026-...` for evidence
- `V-2026-...` for verification
- `A-2026-...` for approval boundaries
- `M-2026-...` for milestone context
- `R-...` for relevant risks

OKCI should not duplicate full output or approval text. It stores references, concise provenance, and scope. Control Desk records remain authoritative.

### 6.3 Sensitive data

Never store passwords, tokens, private keys, seed phrases, credentials, or unredacted sensitive output. Redact arguments, environment values, URLs, identifiers, and output as needed. If redaction prevents reliable verification, mark the result limited or blocked rather than guessing.

## 7. Refined AI Command-Selection Protocol

1. Observe the environment.
2. Read repository instructions, including `AGENTS.md` and `METHOD.md`.
3. Inspect repository structure and Git state.
4. Understand the requested outcome.
5. Consult the project operational profile.
6. Consult OKCI for an exact or constrained command record.
7. Check platform, shell, versions, prerequisites, working directory, target, and permissions.
8. Analyze operation, effects, risk flags, reversibility, secrets, service impact, and approval.
9. Select the safest suitable command.
10. Explain material side effects and recovery implications.
11. Obtain the required human approval for the exact operation and scope.
12. Execute only the approved operation.
13. Capture safe evidence: command, environment, versions, time, exit code, result, and limitations.
14. Verify the outcome proportionately.
15. Record corrections, changed assumptions, risks, and lessons in the appropriate Control Desk record.

### Stop conditions

Stop for missing or conflicting instructions, stale or conflicting project profiles, absent command knowledge with unknown behavior, `BLOCKED` or `DEPRECATED` status for consequential work, `NOT_ASSESSED` compatibility, unknown prerequisites or targets, missing/expired/narrow approval, command drift from approval, secret exposure, unexpected side effects, contradictory results, or inadequate evidence.

The AI must not retry, broaden scope, substitute a different command, or interpret failure as permission to continue.

## 8. Relationship with the Existing Control Desk

- Milestones may identify OKCI command IDs used during execution.
- Evidence records may identify command ID, exact variant, environment, and result.
- Verification records assess acceptance criteria or command behavior.
- Approval records remain the authority for consequential actions.
- Risks may cover stale knowledge, unsafe selection, or compatibility.
- Any index of command references remains derived.

The first implementation must not alter the Control Desk state machine, project registry, or authoritative record model.

## 9. Educational and Commercial Portability

OKCI can teach the reasoning pattern:

```text
Goal → Context → Command → Effects → Approval → Evidence → Verification
```

Exercises should ask learners to identify the outcome, inspect context, compare variants, predict side effects, find prerequisites, choose approval, define expected results, and state what evidence would prove success. The material should teach judgment, not memorization.

Markdown, YAML, stable IDs, provenance, and provider-independent vocabulary support future downloadable templates, agent instruction packs, searchable knowledge bases, and educational products. No hosted service, paid dependency, monetization feature, or commercial infrastructure is part of this stage.

## 10. Staged Implementation Plan

Every stage requires its own scope, approval, evidence, verification, and Git checkpoint under the existing STS lifecycle.

### Stage 1 — Architecture and vocabulary approval

**Dependency:** None.  
**Scope:** Approve the three-layer boundary and independent dimensions.  
**Acceptance:** No duplicate authority; operation, effects, risks, approval, compatibility, and verification are separate.  
**Risk:** Vocabulary becomes ambiguous or over-complex.

### Stage 2 — Command-record schema approval

**Dependency:** Stage 1.  
**Scope:** Approve YAML fields, conditional requirements, provenance, and evidence references.  
**Acceptance:** Three illustrative command types are representable; compatibility is independent; redaction is explicit.  
**Risk:** Schema permits unsupported claims or creates excessive overhead.

### Stage 3 — Initial evidence-backed registry

**Dependency:** Stage 2 and separate write approval.  
**Scope:** Add a small set of documented commands.  
**Acceptance:** Every record has provenance and status; unsupported examples remain proposed or unassessed; no unscoped `VERIFIED` claims.  
**Risk:** Historical evidence is mistaken for current verification.

### Stage 4 — Environment profiles

**Dependency:** Stage 2 and observed environment facts.  
**Scope:** Add Termux, Linux, macOS, and relevant Windows profiles.  
**Acceptance:** Shells, executables, paths, packages, and limitations are evidence-backed; unknowns remain explicit.  
**Risk:** Platform generalization and version drift.

### Stage 5 — Project operational profile

**Dependency:** Stages 3–4.  
**Scope:** Document this repository's structure, entry points, validation, artifacts, restrictions, recovery, and evidence expectations.  
**Acceptance:** Facts are traceable and the profile does not duplicate canonical method authority.  
**Risk:** Profile drift or false test/runtime claims.

### Stage 6 — AI command-selection protocol

**Dependency:** Stages 1–5.  
**Scope:** Add decision sequence and stop conditions.  
**Acceptance:** Environment inspection, compatibility, approval, evidence, verification, and correction recording are mandatory.  
**Risk:** Checklist compliance without actual judgment.

### Stage 7 — Minimal STS integration

**Dependency:** Stages 1–6 and separate approval for canonical-document changes.  
**Scope:** Add only necessary cross-references and optional command/evidence fields.  
**Acceptance:** Existing lifecycle and authority remain unchanged; no duplicate system appears.  
**Risk:** Unintended methodology changes or documentation churn.

### Stage 8 — Validation and educational examples

**Dependency:** Stages 1–7.  
**Scope:** Validate consistency and add reasoning-focused exercises.  
**Acceptance:** Examples distinguish facts, history, proposals, and exercises; exercises teach effects and evidence.  
**Risk:** Examples are copied into production without context.

## 11. Risks and Unresolved Questions

### Risks

| Risk | Control |
|---|---|
| Flat categories hide side effects | Independent operation, effects, risk, and approval dimensions |
| Verification is interpreted as universal | Scope evidence by environment, version, target, commit, and date |
| Conflicting evidence is overwritten | Retain append-only Control Desk records and resolve explicitly |
| Registry duplicates Control Desk authority | Store references and provenance, not copied approvals or full evidence |
| Profiles become stale | Source commit, review date, compatibility status, and stale reason |
| Sensitive output is preserved | Redaction and blocked/limited status when verification becomes impossible |
| Educational examples imply authorization | Label examples and exercises explicitly |
| Schema becomes burdensome | Start small and make conditional fields proportional to risk |

### Unresolved questions

1. What review window should apply to different command classes?
2. Should the first registry use one YAML file or one file per command category?
3. What Windows facts can be documented without current Windows evidence?
4. Should command verification use references only to existing `E-` and `V-` records? Recommendation: yes unless a later need is demonstrated.
5. Which command fields, if any, should be indexed by the existing read-only projection?
6. What redaction standard is sufficient across different shells?
7. Which commands are frequent enough to justify ongoing registry maintenance?

## 12. Human Approval Request

Approve, revise, or reject the following refined design before implementation:

- A documentation-and-YAML OKCI layer with no execution engine.
- Independent operation, effects, risk flags, approval, compatibility, and verification dimensions.
- Scoped verification evidence linked to existing Control Desk records.
- A project profile distinct from reusable environment profiles.
- A mandatory AI selection protocol with explicit stop conditions.
- No duplicate approval, evidence, project registry, milestone, or state-machine system.
- No automatic approval, scheduling, retry, deployment, publication, or hosted product.

Explicitly excluded from the next design-to-implementation transition are execution of proposed examples, dependency installation, changes to `METHOD.md` or `AGENTS.md` unless separately approved, and any commit, push, tag, publication, or deployment.

The exact human decision required is approval of:

1. The three-layer architecture.
2. The independent classification model.
3. The verification and compatibility model.
4. The YAML command-record schema.
5. The staged implementation sequence.

No implementation should proceed until this decision is recorded through the existing STS approval process.

## Conclusion

The refined design makes OKCI a controlled knowledge layer rather than an execution authority. It separates what a command intends to do, what effects it can produce, what risks apply, what approval is required, where it is compatible, and what evidence verifies it. This preserves the STS principle: before adding command-selection power, add stronger control, provenance, and verification.
