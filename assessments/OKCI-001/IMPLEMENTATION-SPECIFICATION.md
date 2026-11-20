# STS-OKCI-001 — Operational Knowledge & Command Intelligence
# Implementation-Ready Specification

Status: Specification for human review; implementation is not authorized by this document.
Date: 2026-11-20
Repository: sts-controlled-ai-engineering

## 1. Executive summary

OKCI is a reusable knowledge layer for selecting and explaining commands safely. It is not an execution engine, approval authority, scheduler, or evidence store. It records command intent, syntax constraints, independent effects and risks, environment compatibility, prerequisites, limitations, and links to authoritative STS Control Desk records.

The design has three independent layers:

1. OKCI — reusable command knowledge and selection guidance.
2. Project operational profiles — repository-specific operating context.
3. STS Control Desk — authoritative approvals, milestones, risks, execution evidence, verification, freshness, invalidation, decisions, checkpoints, and history.

The principal control is provenance. OKCI may summarize verification, but VERIFIED is permitted only when a valid, current, appropriately scoped Control Desk verification record is referenced. Compatibility is a separate map, not a supported-environment list. Historical records remain historical. Missing, stale, conflicting, or invalid evidence lowers status or blocks selection.

This specification defines the vocabulary, schema, examples, selection protocol, layout, portability model, and separately gated implementation sequence. The examples are unexecuted documentation examples and are not permission to run commands.

## 2. Confirmed repository facts and evidence

### 2.1 Observed facts

- AGENTS.md requires preservation of existing work, use of METHOD.md as canonical methodology, evidence-backed claims, proportionate verification, and no commit, push, tag, publication, or deployment without a user request.
- METHOD.md defines the 13-stage lifecycle: Mission; Current State—Observe; Problem—Understand; Goal and Scope; Out of Scope; Risks; Acceptance Criteria; Human Approval; Execute in Small Steps; Verify with Evidence; Git Checkpoint; Lessons Learned; Next Milestone.
- CONTROL-DESK.md defines the milestone state machine, control gates, freshness and invalidation, and the rule that the desk is read-only and must not approve or execute work.
- control-desk/README.md states that Markdown records are authoritative and SQLite and HTML are derived, rebuildable projections.
- Stable record IDs use M-..., A-..., R-..., V-..., E-..., D-..., and C-...; filenames and front-matter IDs must match.
- .sts-project.json and control-desk/projects.json provide existing project-registration mechanisms. OKCI must not replace them.
- A central OKCI registry, environment-profile collection, project operational-profile template, and mandatory OKCI command-selection protocol do not currently exist as an implemented system.
- The current Git inspection for this specification found branch main, a working tree containing pre-existing untracked assessments/ content, and main...origin/main [ahead 2]. The repository state in AGENTS.md is a historical snapshot and must not be treated as current.

### 2.2 Evidence classification

- Fact: directly observed in the current repository, source, or Git state.
- Historical: preserved by an existing record but not re-executed for this specification.
- Inference: reasoned from observed source or structure.
- Recommendation: proposed future design.
- Example: illustrative, unexecuted documentation.
- Unresolved: not established by available evidence.

### 2.3 Relevant records inspected

- assessments/OKCI-001/INITIAL-ASSESSMENT.md
- assessments/OKCI-001/DESIGN-REFINEMENT.md
- METHOD.md
- CONTROL-DESK.md
- control-desk/README.md
- control-desk/schema.md
- control-desk/index_sqlite.py
- control-desk/sqlite-evaluation.md
- control-desk/evidence/E-2026-003.md
- representative control-desk/verifications/ and related milestone, approval, and evidence records

No proposed command, SQLite projection, dependency installation, external publication, or deployment was executed for this specification.

## 3. Proposed architecture

### 3.1 Layer 1 — OKCI

OKCI owns reusable operational knowledge:

- command definitions and constrained syntax;
- operation, effect, risk, approval-class, reversibility, target, secret, and service-impact metadata;
- prerequisites, limitations, expected results, failure conditions, and verification procedures;
- one authoritative environment-compatibility map per command record;
- concise verification-status summaries and references to Control Desk records;
- command-selection guidance for AI assistants;
- registry provenance, review, deprecation, and replacement information.

OKCI must not execute commands, approve actions, create evidence by assertion, change Control Desk state, or declare an action authorized.

### 3.2 Layer 2 — Project operational profiles

A project operational profile owns repository-specific context:

- repository identity, source boundary, and Control Desk location;
- directory structure and entry points;
- established operating systems, shells, runtimes, and tool versions;
- project-specific commands and validation procedures;
- generated and derived artifacts;
- safety restrictions, recovery expectations, and known project hazards;
- links to relevant OKCI and Control Desk records.

It does not replace METHOD.md, project-status records, approvals, or verification records. A profile is authoritative only for the project context and scope it explicitly declares, and it becomes stale when that context changes.

### 3.3 Layer 3 — STS Control Desk

The Control Desk remains authoritative for:

- human approvals and exact approval scope;
- milestones and lifecycle gates;
- risks and controls;
- execution evidence;
- verification records and acceptance-criterion results;
- freshness and invalidation;
- decisions, Git checkpoints, historical records, and recovery boundaries.

OKCI references these records by stable ID and stores no duplicate approval text or full verification record.

## 4. Authority and responsibility boundaries

| Concern | Authority | OKCI behavior |
|---|---|---|
| Reusable command meaning and constraints | OKCI | Own concise metadata and limitations |
| Project paths, entry points, and workflows | Project profile | Reference the profile; do not generalize beyond it |
| Human approval | Control Desk approval record | Store required approval class only |
| Execution output | Control Desk evidence record | Link to it; do not invent output |
| Verification result | Control Desk verification record | Summarize with scope and reference |
| Milestone state and gates | Control Desk | Do not reproduce or advance state |
| Environment compatibility | Command record compatibility map, based on environment evidence | Never use a separate contradictory list |
| Historical status and invalidation | Control Desk history and current records | Reflect stale or invalidated state |
| Derived indexes | Derived tool output | Never treat as a source of truth |

## 5. Final classification vocabulary

Classification is contextual. Inspect exact arguments, shell interpretation, quoting, redirection, pipelines, globbing, command substitution, scripts, working directory, environment variables, permissions, runtime, actual targets, authentication, reversibility, and recovery before assigning values. Executable name alone is insufficient.

### 5.1 Operation

Use one or more values:

- OBSERVE — inspect environment, repository, or runtime state.
- INSPECT — read source, configuration, records, logs, or output.
- ANALYZE — validate, compare, parse, calculate, or diagnose.
- PREPARE — stage, generate, preview, or plan a later operation.
- MODIFY — create, edit, delete, or rewrite local files or data.
- EXECUTE — run a program, script, service, test, or process.

PREPARE does not mean safe by itself; preparation can write files or affect external state.

### 5.2 Effects

Use all applicable values:

- FILESYSTEM_READ
- FILESYSTEM_WRITE
- NETWORK_ACCESS
- PRIVILEGED_ACCESS
- PROCESS_CREATION
- EXTERNAL_STATE_CHANGE

FILESYSTEM_WRITE includes redirection, generated artifacts, databases, caches, and logs. EXTERNAL_STATE_CHANGE includes publication, remote mutation, service control, or any state change outside the local working context.

### 5.3 Risk flags

Use all applicable values:

- DESTRUCTIVE
- SECRET_EXPOSURE
- DATA_LOSS
- EXTERNAL_PUBLICATION
- SERVICE_DISRUPTION

Do not infer DATA_LOSS merely from writing a database. Apply it when the allowed operation can delete or irretrievably replace information, or when the target and recovery boundary make loss plausible. A rebuildable derived projection with authoritative Markdown preserved is not automatically data loss.

### 5.4 Approval requirement

- NONE — no human approval is required for the exact operation under the stated constraints, though repository instructions still apply.
- HUMAN_APPROVAL_REQUIRED — a valid approval for the exact operation and scope is required before execution.
- EXPLICIT_HIGH_RISK_APPROVAL — separate explicit approval, exact target confirmation, preflight, minimal scope, and independent post-action verification are required.

This field describes the minimum control. It is never an approval and never authorizes execution.

### 5.5 Additional dimensions

- reversibility: REVERSIBLE, RECOVERABLE, PARTIALLY_REVERSIBLE, or IRREVERSIBLE.
- target_scope: explicit kind, target constraints, exclusions, and recovery boundary.
- secret_handling: NONE, INDIRECT_ONLY, SENSITIVE_OUTPUT_POSSIBLE, or PROHIBITED.
- service_impact: NONE, LOCAL_ONLY, DEGRADED, or OUTAGE_POSSIBLE.
- Unknown behavior: record the unknown and use PROPOSED or BLOCKED; never fill a gap with an optimistic classification.

## 6. Verification authority and status rules

### 6.1 Four distinct concepts

1. Registry metadata describes intended command behavior, constraints, and known limitations. It is not execution evidence.
2. Verification status summary is a concise OKCI projection of current authoritative records. It is not authoritative evidence.
3. Authoritative verification evidence is the Control Desk V-... verification record and its linked E-... evidence, with exact scope, result, date, and limitations.
4. Environment-specific compatibility states where the command is supported, conditional, unsupported, or not assessed. It does not establish that a particular execution occurred.

### 6.2 Status values

- VERIFIED — a valid, successful, current Control Desk verification record exists and its scope matches the command variant, environment, working directory, target, relevant versions, and date requirements.
- PROJECT-DOCUMENTED — current project documentation supports the command, but an adequately scoped current verification is absent.
- HISTORICAL — prior evidence exists, but it is outside the current verification window, tied to an earlier version or context, or explicitly retained as history.
- PROPOSED — candidate knowledge lacks sufficient authoritative evidence.
- DEPRECATED — not recommended for new use; replacement, reason, date, and migration limitation are required.
- BLOCKED — known failure, prohibited behavior, missing critical prerequisite, unresolved safety conflict, invalid reference, or contradictory evidence prevents safe recommendation.

Environment-specificity belongs in environment_compatibility, not in a status value. A command may be VERIFIED for one environment and NOT_ASSESSED for another.

### 6.3 Status calculation and update rules

For each command record:

1. Resolve every V-..., E-..., A-..., M-..., and other referenced ID against the expected Control Desk path and front-matter ID. A plausible ID is not evidence.
2. Confirm the referenced verification record is record_type: verification, has a successful result for the relevant claim, and links or identifies sufficient evidence.
3. Compare verification scope with the command record: exact or constrained syntax, arguments, working directory, target, OS, shell, runtime/tool versions, repository/project/commit where relevant, and date.
4. Check Control Desk freshness, invalidation, approval scope, and any later conflicting record. A stale or invalidated record cannot establish VERIFIED.
5. Set VERIFIED only when all required comparisons pass. Set last_verified to the authoritative verification date, not the registry edit date.
6. If evidence exists but is historical or scope-mismatched, use HISTORICAL or PROJECT-DOCUMENTED as appropriate and explain the limitation.
   Historical evidence without an authoritative verification record does not populate last_verified; no V-... record may be inferred or invented.
7. If a required reference is missing, malformed, unresolved, or contradictory, use BLOCKED for consequential selection; otherwise use PROPOSED with an unresolved-reference reason.
8. If a command is deprecated, DEPRECATED takes precedence for new selection even if old verification remains valid.
9. Recompute the summary whenever a linked verification, evidence, approval, project profile, environment profile, source commit, runtime/tool version, or review window materially changes.

A registry validator must reject VERIFIED with no valid Control Desk verification reference. It must also reject last_verified without a matching verification record and reject references that do not exist.

### 6.4 Verification scope minimum

An authoritative verification should record, where applicable: command ID; exact command after safe redaction; working directory; OS/platform; shell; runtime and tool versions; repository, branch, commit, or external target; date/time and timezone; exit code; observed result; evidence ID; limitations; and verifier. Termux verification does not establish macOS, Linux, or Windows verification.

## 7. Environment compatibility model

There is one authoritative environment_compatibility map per command record. Do not add a separate supported_environments list.

Allowed status values:

- SUPPORTED — evidence establishes compatibility under stated constraints.
- CONDITIONAL — compatibility depends on named shell, version, path, package, permissions, configuration, or other conditions.
- UNSUPPORTED — known incompatible or prohibited; explain why.
- NOT_ASSESSED — insufficient evidence.

Example:

~~~yaml
environment_compatibility:
  android-termux:
    profile_ref: env-android-termux
    status: NOT_ASSESSED
    shell: null
    executable: git
    version_constraints: null
    conditions: []
    evidence_references: []
  macos:
    profile_ref: env-macos
    status: NOT_ASSESSED
    shell: null
    executable: git
    version_constraints: null
    conditions: []
    evidence_references: []
~~~

Use stable environment-profile identifiers (env-android-termux, env-linux, env-macos, env-windows) for reusable platform facts. Embed the compatibility result in each command record so the record is self-contained and cannot silently inherit a contradictory list. The profile reference is descriptive; the command-level map and its evidence determine the result.

Rules:

- Never mark SUPPORTED without appropriate environment-scoped evidence.
- CONDITIONAL must name every material condition.
- UNSUPPORTED must explain incompatibility or prohibition.
- NOT_ASSESSED means insufficient evidence, not failure and not permission.
- Profiles must not claim unestablished executables, shells, packages, versions, or capabilities.
- Version changes, shell differences, platform updates, path changes, permission changes, and conflicting evidence trigger reassessment. Retain earlier records as historical; narrow status or set NOT_ASSESSED/BLOCKED until resolved.
- A project profile may further restrict a generally compatible environment. It may not broaden an environment claim without evidence.

## 8. Complete proposed YAML command-record schema

This specification distinguishes three separate deliverables:

1. Human-readable field contract — explains fields, allowed values, conditional rules, authority, and sensitivity.
2. Machine-readable validation schema — formal rules a validator can enforce.
3. Registry template — a starter YAML record for humans to populate.

The following illustrative YAML record is a registry template informed by the field contract. It is not, by itself, a complete machine-enforceable schema, and neither the schema nor a validator is created by this specification. All examples in this document are unexecuted.

~~~yaml
schema_version: 1
command_id: CMD-0001
name: example-command
purpose: "One-sentence operational purpose."
syntax:
  kind: exact                 # exact | constrained | template
  command: "example --approved-argument"
  argument_constraints: []
  shell_interpretation: "No unquoted expansion, substitution, pipeline, or redirection unless listed."
operation: [OBSERVE, INSPECT]
effects: [FILESYSTEM_READ]
risk_flags: []
approval_requirement: NONE
reversibility: REVERSIBLE
target_scope:
  kind: current-repository
  target: "Repository root"
  constraints: ["Run only from the intended repository."]
  exclusions: ["No external target"]
secret_handling: NONE
service_impact: NONE
environment_compatibility:
  android-termux:
    profile_ref: env-android-termux
    status: NOT_ASSESSED
    shell: null
    executable: example
    version_constraints: null
    conditions: []
    evidence_references: []
prerequisites:
  - "The intended repository is confirmed."
working_directory:
  required: true
  rule: "Repository root."
expected_results:
  - "The stated observation is reported."
verification_procedure:
  - "Compare output with the expected result and record safe evidence."
failure_conditions:
  - "The target or prerequisite cannot be confirmed."
limitations:
  - "This record does not authorize execution."
evidence_references:
  documentation: []
  control_desk_records: []
verification_status: PROPOSED
last_verified: null
review_due: null
stale_reason: null
source:
  kind: repository-documentation # repository-documentation | control-desk-record | observed | external
  references: []
  source_commit: null
  provenance_note: "Explain what is known and what is not."
provenance:
  recorded_by: human-owner
  recorded_at: 2026-11-20T00:00:00-06:00
  review_history: []
  replacement_command_id: null
~~~

### 8.1 Field contract

| Field | Requirement and allowed values | Validation and authority | Sensitive-data rule |
|---|---|---|---|
| schema_version | Mandatory positive integer | Supported schema version; OKCI schema authority | No secrets |
| command_id | Mandatory stable CMD-... identifier | Unique; never reused; OKCI | No secrets |
| name | Mandatory non-empty stable name | Unique within registry; OKCI | No secrets |
| purpose | Mandatory plain-language outcome | Intent, not authorization; OKCI | No credentials |
| syntax | Mandatory exact, constrained, or template object | Command and argument constraints required; shell interpretation explicit; OKCI | Redact tokens and sensitive arguments |
| operation | Mandatory list | Only six operation values; at least one; OKCI | No secrets |
| effects | Mandatory list | Only six effect values; OKCI classification | No secrets |
| risk_flags | Mandatory list, possibly empty | Only five values; justified by context; OKCI classification | No secret contents |
| approval_requirement | Mandatory | Only three values; minimum control, not approval; OKCI classification | No approval text |
| reversibility | Mandatory | Only four values; match target/recovery analysis; OKCI classification | No recovery secrets |
| target_scope | Mandatory for every record | Kind, target, constraints, exclusions; exact target required for consequential actions | Redact sensitive identifiers |
| secret_handling | Mandatory when output/input can be sensitive; otherwise recommended | Only four values; PROHIBITED blocks selection | Never store secret values |
| service_impact | Mandatory when services may be affected; otherwise recommended | Only four values; actual target required | No credentials |
| environment_compatibility | Mandatory map; replaces supported-environment list | Every environment has one allowed status and required conditions/evidence | Avoid unnecessary host identifiers |
| prerequisites | Mandatory non-empty list | Checkable before execution; project-specific items may also be in profile | Never request secret disclosure |
| working_directory | Mandatory object | Required flag and rule; exact path or approved project rule for mutations | Redact sensitive paths |
| expected_results | Mandatory non-empty list | Observable outcomes, not proof of success | Redact sensitive output |
| verification_procedure | Mandatory non-empty list | Safe evidence and authoritative verification path; Control Desk owns result | No unredacted output |
| failure_conditions | Mandatory non-empty list | Includes unknown target, incompatible environment, approval mismatch, and safety stops | No secrets |
| limitations | Mandatory non-empty list | Preserve scope and historical limits; OKCI | No secrets |
| evidence_references | Mandatory object | Every reference resolves and supports exact claim; Control Desk authoritative | IDs only; no copied secret output |
| verification_status | Mandatory | Only six statuses; VERIFIED requires current valid V-... | No sensitive detail |
| last_verified | Mandatory nullable date/time | Required for VERIFIED; must trace to authoritative record | No secrets |
| review_due | Optional nullable date/time | Required if a review window exists; never creates verification | No secrets |
| stale_reason | Conditional | Required when stale, historical due to age, or invalidated | No secrets |
| source | Mandatory object | Source kind/references/commit/provenance; references resolve where applicable | Redact source content |
| provenance | Mandatory object | Recorder/date/review history/replacement; append, do not erase history | No credentials |

Conditional rules: target_scope must identify an exact approved target for any write, external action, privileged action, service impact, or high-risk action. secret_handling and service_impact must be explicit whenever relevant. evidence_references.control_desk_records is required for VERIFIED, and every ID must resolve to an authoritative record of the correct type.

## 9. Illustrative command records

These are unexecuted examples. They are not approvals, execution instructions, or evidence.

### 9.1 Read-only Git inspection

~~~yaml
schema_version: 1
command_id: CMD-GIT-STATUS-001
name: inspect-git-status
purpose: "Inspect the active branch and concise working-tree state."
syntax:
  kind: exact
  command: "git status --short --branch"
  argument_constraints: []
  shell_interpretation: "No pipeline, redirection, substitution, or extra arguments."
operation: [OBSERVE, INSPECT]
effects: [FILESYSTEM_READ]
risk_flags: []
approval_requirement: NONE
reversibility: REVERSIBLE
target_scope: {kind: current-repository, target: "Intended repository", constraints: [], exclusions: ["No other repository"]}
secret_handling: NONE
service_impact: NONE
environment_compatibility:
  android-termux: {profile_ref: env-android-termux, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  linux: {profile_ref: env-linux, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  macos: {profile_ref: env-macos, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  windows: {profile_ref: env-windows, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
prerequisites: ["Git is installed", "The intended repository is confirmed"]
working_directory: {required: true, rule: "Intended repository or subdirectory"}
expected_results: ["Branch and concise working-tree state are reported"]
verification_procedure: ["Confirm output refers to intended repository and no mutation occurred"]
failure_conditions: ["Not inside a Git repository", "Git unavailable", "Target unclear"]
limitations: ["Does not show the complete patch or prove project correctness"]
evidence_references: {documentation: ["METHOD.md", "control-desk/milestones/M-2026-001.md"], control_desk_records: []}
verification_status: PROJECT-DOCUMENTED
last_verified: null
review_due: null
stale_reason: null
source: {kind: repository-documentation, references: ["METHOD.md"], source_commit: null, provenance_note: "Documentation supports use; this example was not executed for OKCI."}
provenance: {recorded_by: human-owner, recorded_at: 2026-11-20T00:00:00-06:00, review_history: [], replacement_command_id: null}
~~~

### 9.2 Control Desk SQLite projection

~~~yaml
schema_version: 1
command_id: CMD-CONTROL-DESK-SQLITE-001
name: build-control-desk-sqlite-projection
purpose: "Build or refresh a rebuildable SQLite projection from explicitly registered Control Desk records."
syntax:
  kind: constrained
  command: "python3 control-desk/index_sqlite.py --database <approved-derived-database-path>"
  argument_constraints: ["Database target must be explicitly confirmed as derived output", "No unapproved registry or target substitution"]
  shell_interpretation: "No redirection, pipeline, substitution, or automatic retry."
operation: [ANALYZE, MODIFY, EXECUTE]
effects: [FILESYSTEM_READ, FILESYSTEM_WRITE, PROCESS_CREATION]
risk_flags: [SECRET_EXPOSURE]
approval_requirement: HUMAN_APPROVAL_REQUIRED
reversibility: RECOVERABLE
target_scope:
  kind: derived-local-artifact
  target: "Approved SQLite projection path only"
  constraints: ["Markdown remains authoritative", "Database is disposable and rebuildable", "Registered project paths are approved", "Target is explicitly established as eligible before backup or dry-run requirements are considered"]
  exclusions: ["Authoritative Markdown", "Unknown or important non-derived files"]
secret_handling: SENSITIVE_OUTPUT_POSSIBLE
service_impact: NONE
environment_compatibility:
  android-termux: {profile_ref: env-android-termux, status: NOT_ASSESSED, shell: null, executable: python3, version_constraints: null, conditions: [], evidence_references: []}
  linux: {profile_ref: env-linux, status: NOT_ASSESSED, shell: null, executable: python3, version_constraints: null, conditions: [], evidence_references: []}
  macos: {profile_ref: env-macos, status: NOT_ASSESSED, shell: null, executable: python3, version_constraints: null, conditions: [], evidence_references: []}
  windows: {profile_ref: env-windows, status: NOT_ASSESSED, shell: null, executable: python3, version_constraints: null, conditions: [], evidence_references: []}
prerequisites: ["Exact derived target is confirmed and eligible for this operation", "Explicit project registry is approved", "Source records are safe to index", "Required Python runtime is established"]
working_directory: {required: true, rule: "Repository root or exact documented invocation context"}
expected_results: ["Projection is created or refreshed", "Source Markdown is unchanged", "Run result, counts, and errors are observable"]
verification_procedure: ["Compare source hashes or diff before and after", "Inspect run status and error count", "Confirm target is rebuildable and non-authoritative"]
failure_conditions: ["Target is authoritative, unknown, ambiguous, or outside the approved boundary", "Source contains prohibited sensitive data", "Registry or repository path is not approved", "Unexpected side effect", "Transaction fails"]
limitations: ["The script stores raw Markdown in the projection and does not redact it", "A database write can alter an existing derived database", "Historical E-2026-003 is in-memory evidence only and is not current persistent-target verification"]
evidence_references:
  documentation: ["control-desk/README.md", "control-desk/sqlite-evaluation.md"]
  control_desk_records: ["E-2026-003"]
verification_status: HISTORICAL
last_verified: null
review_due: null
stale_reason: "E-2026-003 documents a historical in-memory run but does not establish an authoritative verification date, current persistent-target safety, or environment compatibility."
source: {kind: repository-documentation, references: ["control-desk/index_sqlite.py", "control-desk/README.md", "control-desk/sqlite-evaluation.md", "control-desk/evidence/E-2026-003.md"], source_commit: null, provenance_note: "Source code and documentation were inspected; E-2026-003 is retained as historical evidence; no execution performed for this specification."}
provenance: {recorded_by: human-owner, recorded_at: 2026-11-20T00:00:00-06:00, review_history: [], replacement_command_id: null}
~~~

For this example, an unknown, ambiguous, authoritative, or out-of-boundary SQLite target is BLOCKED. A backup does not make an otherwise unapproved target eligible. A different target, expanded scope, or changed operation requires a new assessment and applicable explicit approval. Backup or dry-run requirements apply only after the target has been established as eligible for this operation. No automatic retry or target substitution is permitted.

### 9.3 External Git publication

~~~yaml
schema_version: 1
command_id: CMD-GIT-PUSH-001
name: publish-git-branch
purpose: "Push an explicitly approved local branch to an explicitly approved remote."
syntax:
  kind: constrained
  command: "git push <approved-remote> <approved-branch>"
  argument_constraints: ["Exact remote, repository, branch, and commit must be approved", "No wildcard, implicit target, command substitution, or retry"]
  shell_interpretation: "No pipeline, redirection, or substituted target."
operation: [EXECUTE]
effects: [FILESYSTEM_READ, NETWORK_ACCESS, PROCESS_CREATION, EXTERNAL_STATE_CHANGE]
risk_flags: [EXTERNAL_PUBLICATION]
approval_requirement: EXPLICIT_HIGH_RISK_APPROVAL
reversibility: PARTIALLY_REVERSIBLE
target_scope: {kind: remote-repository, target: "Exact approved remote and branch", constraints: ["Repository, commit, branch, and recovery plan are explicit"], exclusions: ["No other remotes or branches"]}
secret_handling: SENSITIVE_OUTPUT_POSSIBLE
service_impact: NONE
environment_compatibility:
  android-termux: {profile_ref: env-android-termux, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  linux: {profile_ref: env-linux, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  macos: {profile_ref: env-macos, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
  windows: {profile_ref: env-windows, status: NOT_ASSESSED, shell: null, executable: git, version_constraints: null, conditions: [], evidence_references: []}
prerequisites: ["Exact publication approval exists", "Preflight and recovery controls pass", "Credentials are handled without exposing secrets"]
working_directory: {required: true, rule: "Intended repository and approved branch"}
expected_results: ["Only the approved commit is sent to the approved remote branch"]
verification_procedure: ["Record actual remote, branch, commit, result, and safe evidence", "Independently inspect remote state"]
failure_conditions: ["Approval absent, expired, or mismatched", "Target ambiguous", "Preflight fails", "Unexpected remote response or side effect"]
limitations: ["Publication can affect external consumers and may not be reversible after they act"]
evidence_references: {documentation: ["METHOD.md", "checklists/before-commit.md"], control_desk_records: []}
verification_status: PROPOSED
last_verified: null
review_due: null
stale_reason: null
source: {kind: repository-documentation, references: ["METHOD.md"], source_commit: null, provenance_note: "The record describes a controlled future action; it is not permission to publish."}
provenance: {recorded_by: human-owner, recorded_at: 2026-11-20T00:00:00-06:00, review_history: [], replacement_command_id: null}
~~~

## 10. SQLite source-behavior assessment

This assessment is based on source inspection and documentation only. The script was not executed for this specification.

| Question | Established behavior | Classification consequence |
|---|---|---|
| New or existing database? | sqlite3.connect(args.database) opens or creates the specified SQLite path. CREATE TABLE IF NOT EXISTS creates the schema when absent and preserves compatible existing tables. | FILESYSTEM_WRITE and MODIFY apply to the target; target identity is mandatory. |
| Can existing data be overwritten? | Existing projection rows are upserted by (project_id, record_id); project metadata is also upserted; absent source records are marked active = 0. | Existing derived data can change. Exact derived target and recoverability are required. |
| Can data be deleted? | The source shows no DELETE statements. It does not delete authoritative Markdown. It can make prior projection rows inactive and replace projected values. | Do not assign DATA_LOSS solely because the database is written. DATA_LOSS becomes conditional if the target is not confirmed disposable/rebuildable. |
| Transactions? | SQLite transaction behavior is used; schema and run writes are committed on success. On an exception, the current transaction is rolled back, then the script attempts to record failure. | Treat a failed run as not fully committed; confirm actual target state before any retry. |
| Failure behavior? | Missing repositories are recorded and contribute to completed_with_errors; an exception rolls back and re-raises. The failure-record update occurs after rollback and may not persist the failed run row. | A nonzero/exception result requires inspection; no automatic retry or success inference. |
| Rebuildable? | Documentation and schema show the projection is derived from registered Markdown records and has provenance fields. The source can rebuild from source records, subject to registry and parser compatibility. | RECOVERABLE for an approved derived target, not REVERSIBLE in the sense of preserving every prior projection state. |
| Authoritative Markdown unchanged? | The source reads Markdown and writes SQLite. It invokes Git read operations against source repositories. No source-record write is present. Historical E-2026-003 states source records remained unchanged for an in-memory run. | FILESYSTEM_READ plus target FILESYSTEM_WRITE; no authority transfer. Current unchanged status still requires execution evidence for the actual run. |
| Accidental important target? | --database accepts an arbitrary path. The source does not enforce that the path is derived, safe, or inside a designated output directory. | Exact target preflight is mandatory. Ambiguous or important targets are BLOCKED. |
| Backup/confirmation? | A backup is not automatically required for a disposable rebuildable database, but exact target confirmation and recovery evidence are required. Backup or a dry run is justified only after the target is established as eligible; it does not make an otherwise unapproved target eligible. An existing target that is important, not clearly disposable, or outside the documented derived boundary is BLOCKED or requires the applicable new assessment and approval. | HUMAN_APPROVAL_REQUIRED for the normal approved derived target; escalate to EXPLICIT_HIGH_RISK_APPROVAL or block for an important/unclear target. |

Final example classification uses ANALYZE, MODIFY, and EXECUTE; FILESYSTEM_READ, FILESYSTEM_WRITE, and PROCESS_CREATION; no blanket DATA_LOSS; RECOVERABLE; and a derived-target approval condition. SECRET_EXPOSURE is flagged as a conditional concern because the implementation stores raw Markdown and does not redact input. The command must be blocked if prohibited sensitive data or an authoritative target is involved.

Target eligibility is a precondition, not an outcome of recovery planning. An unknown, ambiguous, authoritative, or out-of-boundary target is BLOCKED. A backup does not make an otherwise unapproved target eligible. A different target, expanded scope, or changed operation requires a new assessment and applicable explicit approval. Backup or dry-run requirements apply only after the target has been established as eligible for the operation. No automatic retry or target substitution is permitted.

## 11. Evidence-reference validation results

control-desk/evidence/E-2026-003.md exists at the expected path and has matching front-matter ID E-2026-003, record_type: evidence, and a verified historical status. It records an in-memory invocation and reports a successful run with 20 records and zero errors. Its text supports these limited claims: the explicitly registered repository was indexed for that historical run, the database target was :memory:, and source records remained unchanged for that run.

It does not support these broader claims:

- current verification of the present source;
- persistent database-target safety;
- compatibility on Termux, Linux, macOS, or Windows;
- absence of all sensitive-data propagation;
- universal success or rebuildability under changed versions and targets.

The reference is valid for historical provenance but not sufficient for VERIFIED. The schema validator must resolve references by exact file and front-matter ID, check record type, and check that the body supports the exact claim. Missing, mismatched, malformed, stale, invalidated, or scope-mismatched references are unresolved and must never be treated as proof of success.

## 12. AI command-selection protocol

The following sequence is mandatory for consequential command selection:

1. Observe the actual environment.
2. Read repository instructions, including AGENTS.md, METHOD.md, and applicable project instructions.
3. Inspect repository structure and Git state.
4. Understand the requested outcome and success boundary.
5. Consult the project operational profile.
6. Consult OKCI for an exact or constrained command record.
7. Check prerequisites, environment compatibility, shell, runtime/tool versions, working directory, permissions, and target.
8. Analyze operation, effects, risks, approval, secrets, service impact, reversibility, and recovery.
9. Select the safest suitable command and smallest scope.
10. Explain material side effects and recovery implications.
11. Obtain the required human approval for the exact operation and target.
12. Execute only the approved operation.
13. Capture safe evidence: exact command after redaction, environment, versions, time, exit code, result, target, and limitations.
14. Verify the outcome proportionately using the Control Desk.
15. Record corrections, changed assumptions, risks, and lessons.

Stop immediately for:

- missing or conflicting repository instructions;
- missing, stale, or conflicting project profile;
- missing command record for a consequential action;
- command status PROPOSED, BLOCKED, or DEPRECATED when no renewed decision resolves it;
- NOT_ASSESSED compatibility for the actual environment;
- unknown command behavior, prerequisites, permissions, shell interpretation, or target;
- unknown, ambiguous, authoritative, or out-of-boundary SQLite target;
- backup offered for, or dry-run proposed against, a target that has not first been established as eligible;
- missing, expired, revoked, or scope-mismatched approval;
- target expansion or command drift from approval;
- unexpected side effects, secret exposure, service impact, or contradictory output;
- failed, stale, invalidated, or insufficient verification.

The AI must not automatically retry, broaden scope, substitute a different command or target, or reinterpret failure as permission. A backup does not make an otherwise unapproved SQLite target eligible. Any retry, command substitution, target change, or scope expansion requires a new assessment and applicable explicit approval. Backup or dry-run requirements apply only after the target has been established as eligible for the operation. A registry entry is never permission to publish, deploy, modify, delete, or execute.

## 13. Registry and project-profile layout recommendation

Use a small initial layout:

~~~text
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
~~~

Do not create this layout in the current task.

Recommendation: begin with one human-readable command-registry.yaml, grouped by stable command_id, rather than many category files. One file is easier to review on mobile devices and avoids cross-file category drift. Split only when review or merge size becomes a demonstrated problem; preserve stable IDs and schema versioning.

Use stable environment-profile IDs, but embed the authoritative per-command compatibility map. Use stable project IDs and profile references, while keeping repository-specific facts in the project profile. Use E-, V-, A-, M-, and R- references for Control Desk provenance; do not copy their authority.

Validation should check YAML shape, enums, unique IDs, required conditional fields, target constraints, exact reference existence, record type, status derivation, dates, stale reasons, environment-map completeness, and prohibited secrets. It should be read-only. Schema evolution requires an explicit schema_version, migration notes, compatibility rules, and preservation of old records. Stale records remain visible with stale reasons; they are not silently deleted or promoted. Deprecation requires a reason, date, replacement, and known migration limitation.

## 14. Educational and commercial portability

Each command record can become a beginner lesson or AI-selection exercise using this sequence:

Goal → Context → Command → Effects → Approval → Evidence → Verification

A learning resource should teach:

- what the command does;
- why it fits the outcome;
- what it can affect;
- what must be checked first;
- what approval is necessary;
- what evidence proves success;
- what limitations and recovery boundaries remain.

Stable IDs, Markdown, YAML, provenance, explicit uncertainty, and provider-independent vocabulary support reusable lessons, controlled-AI training, downloadable templates, and future STS educational products. No hosted service, paid dependency, commercial infrastructure, execution engine, or monetization feature is authorized by this specification.

## 15. Staged implementation roadmap

Each stage is a separate STS milestone with its own scope, evidence, verification, Git checkpoint, and human approval. No stage authorizes the next stage automatically.

### Stage 1 — Architecture and vocabulary

- Objective: Approve the three-layer boundary and independent dimensions.
- Scope: Responsibility boundaries; operation; effects; risk flags; approval; reversibility; target; secrets; service impact.
- Prerequisites: Human review of this specification and existing METHOD.md/CONTROL-DESK.md.
- Expected files: Approved architecture/classification documentation only.
- Acceptance criteria: No duplicate authority; all three layers and required enums are unambiguous.
- Risks: Vocabulary may hide side effects or become too complex.
- Verification evidence: Reviewed decision and approved terminology matrix.
- Required human approval: Explicit architecture and vocabulary approval.
- Out of scope: Registry files, execution, automation, Control Desk schema changes.

### Stage 2 — Command-record schema

- Objective: Approve and document the YAML record contract.
- Scope: Human-readable field contract; machine-readable validation schema; registry template; required fields, conditional rules, provenance, references, status, compatibility map, and redaction.
- Prerequisites: Stage 1 approval.
- Expected files: Human-readable field-contract documentation, machine-readable validation-schema definition, and registry-template documentation.
- Acceptance criteria: Three illustrative command types are representable; VERIFIED cannot lack a valid V- reference.
- Risks: Unsupported claims or excessive maintenance burden.
- Verification evidence: Review of all three deliverables, including schema validation review with negative cases for missing/invalid references.
- Required human approval: Review and approval of the human-readable field contract, machine-readable validation schema, and registry template.
- Out of scope: Populating a registry or executing examples.

### Stage 3 — Initial evidence-backed command registry

- Objective: Record a small set of commands with traceable provenance.
- Scope: Only commands supported by current documentation or authoritative records; unresolved commands remain proposed or blocked.
- Prerequisites: Stages 1–2 and separate write approval.
- Expected files: Initial registry and validation notes.
- Acceptance criteria: Unique IDs, exact references, no unscoped VERIFIED, no fabricated evidence, safe target constraints.
- Risks: Historical evidence may be mistaken for current verification.
- Verification evidence: Read-only validator output and human review of each reference.
- Required human approval: Registry-content approval.
- Out of scope: Execution engine, automatic status updates, approval automation.

### Stage 4 — Environment profiles

- Objective: Document reusable environment facts without overclaiming support.
- Scope: Termux, Linux, macOS, and relevant Windows profiles, only where facts are established.
- Prerequisites: Stage 2 and observed environment evidence.
- Expected files: Environment profile documents and compatibility references.
- Acceptance criteria: Shells, executables, versions, paths, packages, and limitations are evidence-backed; unknowns remain NOT_ASSESSED.
- Risks: Platform generalization and version drift.
- Verification evidence: Profile review and scoped compatibility records.
- Required human approval: Environment-profile approval.
- Out of scope: Claiming support based solely on platform names or running a compatibility matrix without authorization.

### Stage 5 — Project operational profile

- Objective: Describe this repository's actual operating context.
- Scope: Structure, entry points, runtime facts, project commands, validation, artifacts, restrictions, recovery, and linked records.
- Prerequisites: Stages 3–4.
- Expected files: Project profile and links; no changes to canonical method files unless separately approved.
- Acceptance criteria: Every material fact is traceable; profile does not duplicate authority or claim unestablished behavior.
- Risks: Profile drift and false runtime/test claims.
- Verification evidence: Repository observation record and profile review.
- Required human approval: Project-profile approval.
- Out of scope: Changing project behavior, Control Desk state, or existing schemas.

### Stage 6 — AI command-selection protocol

- Objective: Publish the mandatory sequence and stop conditions.
- Scope: Selection, compatibility, approval, evidence, verification, correction, retry, substitution, and scope rules.
- Prerequisites: Stages 1–5.
- Expected files: Protocol documentation and review examples.
- Acceptance criteria: Every consequential path checks context, target, approval, evidence, and verification; stop conditions are explicit.
- Risks: Checklist compliance without judgment.
- Verification evidence: Tabletop review using safe, modifying, and external examples.
- Required human approval: Protocol approval.
- Out of scope: Agent execution or automatic approval.

### Stage 7 — Minimal STS documentation integration

- Objective: Add only necessary cross-references to STS documentation.
- Scope: Optional command IDs and evidence links where they improve traceability.
- Prerequisites: Stages 1–6 and separate approval for canonical-document changes.
- Expected files: Minimal approved documentation edits.
- Acceptance criteria: Existing lifecycle, state machine, and authority remain unchanged; no duplicate system appears.
- Risks: Methodology drift and documentation churn.
- Verification evidence: Diff review, link/reference validation, and Control Desk verification.
- Required human approval: Explicit approval for each canonical-file change.
- Out of scope: Modifying METHOD.md, AGENTS.md, or Control Desk schemas without that separate approval.

### Stage 8 — Validation and educational examples

- Objective: Validate registry consistency and create reasoning-focused lessons.
- Scope: Read-only validation, examples, exercises, and portability guidance.
- Prerequisites: Stages 1–7.
- Expected files: Validator documentation, educational examples, and evidence-backed review records.
- Acceptance criteria: Examples distinguish fact, history, proposal, and exercise; lessons teach effects, approval, and evidence.
- Risks: Examples may be copied into production without context.
- Verification evidence: Validator results and human review of educational safety labels.
- Required human approval: Validation/example approval.
- Out of scope: Hosted products, paid services, automation, execution functionality, publication, or deployment.

## 16. Acceptance criteria for this specification

This specification is complete for human review when:

- all three independent layers and their boundaries are defined;
- final operation, effects, risk, and approval vocabularies are defined;
- registry metadata, status summary, authoritative verification, and compatibility are distinguished;
- VERIFIED rules require valid, scoped Control Desk verification;
- compatibility uses one map with the four allowed statuses and no independent supported list;
- the complete required YAML fields, conditional rules, validation rules, authority, and sensitivity are documented;
- three complete unexecuted examples are included;
- SQLite behavior is assessed from source without execution and its classification does not assume data loss;
- E-2026-003 and record conventions are validated and limitations are stated;
- the AI protocol and stop conditions prohibit unsafe retry, substitution, and scope expansion;
- the small registry/profile layout and schema evolution approach are specified;
- portability and the eight separately gated implementation stages are documented;
- implementation, automation, publication, and deployment remain explicitly out of scope.

## 17. Risks and unresolved decisions

### Risks and controls

| Risk | Control |
|---|---|
| Flat categories hide side effects | Independent operation, effects, risk, approval, target, secret, and service dimensions |
| Verification is interpreted as universal | Scope by environment, shell, versions, target, working directory, commit, and date |
| Historical evidence is promoted silently | Status derivation, stale reasons, and valid V- references only |
| Registry duplicates Control Desk authority | Store concise summaries and stable references, not copied approvals or full evidence |
| Environment claims drift | Stable profiles, command-level map, conditions, review dates, and conflict handling |
| SQLite target is important or ambiguous | Exact-target preflight, derived-boundary check, approval escalation, and no automatic retry |
| Raw Markdown propagates sensitive content | Secret-handling classification, input restrictions, redaction, and block on prohibited data |
| Profiles become stale | Source commit, review date, invalidation, and explicit stale reasons |
| Educational examples imply authorization | Label every example unexecuted and teach approval/evidence separately |

### Unresolved decisions for human review

1. What review window should apply to read-only, modifying, and external command classes?
2. Should the first registry remain one YAML file until review or merge size demonstrates a need to split?
3. What Windows environment evidence is available before any support claim is made?
4. Should every VERIFIED command require both a V- verification and at least one linked E- evidence record? Recommendation: yes.
5. Which OKCI fields, if any, should be exposed by the existing derived Control Desk index?
6. What common redaction standard should be adopted across shells and tools?
7. How should a later validator represent a failed SQLite run when the current source may not persist its failure row after rollback?

## 18. Human approval request

The exact next decision is human approval of this specification and authorization of Stage 1 only:

1. approve, revise, or reject the three-layer architecture;
2. approve, revise, or reject the independent classification model;
3. approve, revise, or reject the verification authority and environment-compatibility rules;
4. approve, revise, or reject the proposed YAML schema and validation rules;
5. approve, revise, or reject the eight-stage implementation sequence;
6. explicitly confirm that implementation files, registry creation, environment profiles, project profiles, execution functionality, automation, publication, and deployment remain out of scope until separately approved.

No implementation should begin until the decision is recorded through the existing STS Control Desk approval process. A future approval must name the exact stage, files, scope, risks, acceptance criteria, evidence plan, and exclusions. Approval of this specification is not approval to execute any example command or publish any external state.
