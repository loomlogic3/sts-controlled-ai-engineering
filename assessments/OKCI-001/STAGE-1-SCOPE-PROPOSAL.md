# STS-OKCI-001 — Stage 1 Scope Proposal

## 1. Mission and assessment scope

Mission: prepare an evidence-based, implementation-ready proposal for the smallest coherent Stage 1 implementation of Operational Knowledge & Command Intelligence (OKCI).

This assessment is read-only except for creating this report. It proposes documentation scope only; it does not implement OKCI, create architecture or vocabulary documentation, create registries or schemas, edit existing project documentation, create Control Desk records, execute project scripts or illustrative commands, install dependencies, or perform Git-mutating or external actions.

The authoritative design reference is `assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md`, which states that implementation is not authorized by the specification. The assessment distinguishes:

- **Fact:** directly observed in the repository or Git state.
- **Historical:** recorded by an existing document or record, not re-executed for this assessment.
- **Inference:** reasoned from observed facts.
- **Recommendation:** proposed future scope in this report.
- **Unresolved:** requiring a human decision or later evidence.

## 2. Repository state observed

Observed on 2026-11-20:

- Branch: `main`.
- HEAD: `6c9f7d5` (`Add usage help to Control Desk tools; record M-2026-028 and A-2026-025`).
- Remote relationship: `main...origin/main [ahead 2]`.
- Working tree before this report: `?? assessments/`; the assessment directory was already untracked and contains prior OKCI assessment material.
- The repository contains a repository-native Control Desk documentation and tooling area under `control-desk/`, in addition to the canonical method and templates.
- The snapshot in `AGENTS.md` is historical: its recorded HEAD and clean working-tree state do not match the current observed state.
- No application test suite was identified by the repository instructions; this task did not run project scripts, tests, or illustrative commands.

The assessment preserves the pre-existing untracked assessment material. The only file created for this task is this report.

## 3. Files inspected

Repository instructions and requested design references:

- `AGENTS.md`
- `assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md`
- `assessments/OKCI-001/FINAL-REVIEW-COPY.md`
- `assessments/OKCI-001/FINAL-REVIEW-CORRECTION-REPORT.md`
- `METHOD.md`
- `CONTROL-DESK.md`
- `README.md`

Relevant existing documentation and structure:

- `control-desk/README.md`
- `control-desk/schema.md`
- `control-desk/architecture.md`
- `control-desk/model-analysis-boundary.md`
- `control-desk/presentation.md`
- `control-desk/sqlite-evaluation.md`
- `.sts-project.json`
- `control-desk/projects.json`
- `templates/milestone.md`
- `templates/approval-record.md`
- `templates/verification-record.md`
- `templates/project-status.md`
- `templates/risk-register.md`
- `checklists/before-commit.md`
- `checklists/before-deployment.md`
- `checklists/high-risk-actions.md`
- `examples/sts-ai-lab/per-agent-tool-permissions.md`

The repository search found no additional nested `AGENTS.md` applicable to this repository.

## 4. Relevant existing documentation and findings

### Confirmed facts

- `METHOD.md` is the canonical controlled-engineering lifecycle and requires explicit scope, exclusions, risks, acceptance criteria, approval, evidence, verification, checkpoint, lessons, and next milestone.
- `CONTROL-DESK.md` defines the milestone state machine, control gates, freshness and invalidation rules, and the boundary that the desk is read-only and must not approve or execute work.
- `control-desk/README.md` and `control-desk/schema.md` establish Markdown records as authoritative, stable IDs and linked records as the traceability model, and SQLite/HTML as derived projections.
- Existing templates and records already provide approval, risk, evidence, verification, milestone, and project-status concepts.
- `.sts-project.json` and `control-desk/projects.json` already provide project-registration mechanisms.
- The implementation specification defines three independent layers: OKCI reusable command knowledge; project operational profiles; and the STS Control Desk as authority for approvals, milestones, risks, execution evidence, verification, freshness, invalidation, decisions, checkpoints, and history.
- The specification defines operation values `OBSERVE`, `INSPECT`, `ANALYZE`, `PREPARE`, `MODIFY`, and `EXECUTE`; effect values; risk flags; approval requirements; reversibility; target scope; secret handling; service impact; and explicit treatment of unknown behavior.

### Inferences

- Stage 1 needs a stable human-readable authority for architecture and vocabulary, but it does not need machine-readable structure yet.
- A single document is sufficient for Stage 1 because the objective is to approve the boundary and vocabulary, not to populate records or provide reusable templates.
- Creating multiple files now would increase cross-reference and authority-duplication risk without satisfying an additional Stage 1 acceptance criterion.

### Existing documentation to reference, not duplicate

- Link to `METHOD.md` for lifecycle, risk, approval, evidence, verification, and completion requirements.
- Link to `CONTROL-DESK.md` for milestone gates, authority, freshness, invalidation, and the read-only boundary.
- Link to `control-desk/README.md` and `control-desk/schema.md` for record storage, stable IDs, authoritative Markdown, and derived projections.
- Link to existing templates rather than restating approval, risk, milestone, verification, or evidence record formats.
- Link to `.sts-project.json` and `control-desk/projects.json` when describing project identity or registration; OKCI must not replace them.

## 5. Proposed Stage 1 file list

### Recommendation: one new file

| Exact path | State | Purpose | Stage 1 reason | Dependencies |
|---|---|---|---|---|
| `okci/architecture-and-classification.md` | New file; directory and file do not currently exist | Single human-readable authority for the approved OKCI three-layer boundary and independent classification vocabulary | Directly matches Stage 1's architecture-and-vocabulary objective while avoiding registry, schema, profile, and protocol work | `METHOD.md`, `CONTROL-DESK.md`, `control-desk/README.md`, `control-desk/schema.md`, and the approved implementation specification |

This path is a recommendation, not an assumption that the specification's illustrative `okci/` layout is already approved. The future approval must explicitly approve this path or substitute another exact path. No existing file should be updated for Stage 1.

### Why not split the document

The specification's proposed layout lists `okci/README.md`, `okci/classification.md`, and other later-stage files, but it also says not to create that layout in the current task. Stage 1's expected files are “approved architecture/classification documentation only.” A single `okci/architecture-and-classification.md` keeps the two inseparable decisions together, creates one reviewable authority, and avoids an early README/classification split whose relationship would itself need governance.

## 6. Proposed contents for `okci/architecture-and-classification.md`

The future implementation should contain the following headings and only the Stage 1 material needed under them:

1. **Document status, authority, and scope**
   - State that the document records the approved Stage 1 architecture and vocabulary.
   - State that it does not authorize execution, approval, publication, deployment, or registry use.
   - Link to the implementation specification, `METHOD.md`, and `CONTROL-DESK.md`.

2. **OKCI responsibility and boundaries**
   - Define OKCI as reusable command knowledge and selection guidance.
   - Include command intent, syntax constraints, independent effects and risks, prerequisites, limitations, compatibility guidance, and provenance references at the conceptual level.
   - Explicitly exclude execution, approval, evidence creation by assertion, Control Desk state changes, and authorization.

3. **Three-layer architecture**
   - Define the OKCI layer.
   - Define project operational profiles as repository-specific context.
   - Define the STS Control Desk as authority for approvals, milestones, risks, evidence, verification, freshness, invalidation, decisions, checkpoints, and history.

4. **Authority and responsibility matrix**
   - Map reusable command meaning to OKCI.
   - Map project paths, entry points, and workflows to the project profile.
   - Map human approval, execution evidence, verification, milestone state, and history to the Control Desk.
   - State that OKCI references Control Desk records and does not copy or replace their authority.

5. **Classification principles**
   - State that classification is contextual and requires inspection of exact arguments, shell interpretation, quoting, redirection, pipelines, globbing, command substitution, working directory, environment, permissions, runtime, targets, authentication, reversibility, and recovery.
   - State that executable names alone are insufficient.
   - State that dimensions are independent: an operation may have several effects and risk flags.

6. **Operation vocabulary**
   - Define exactly: `OBSERVE`, `INSPECT`, `ANALYZE`, `PREPARE`, `MODIFY`, `EXECUTE`.
   - Preserve the specification's definitions and the rule that `PREPARE` is not automatically safe.

7. **Effect vocabulary**
   - Define exactly: `FILESYSTEM_READ`, `FILESYSTEM_WRITE`, `NETWORK_ACCESS`, `PRIVILEGED_ACCESS`, `PROCESS_CREATION`, `EXTERNAL_STATE_CHANGE`.
   - Clarify that filesystem writes include generated artifacts, databases, caches, logs, and redirection.

8. **Risk-flag vocabulary**
   - Define exactly: `DESTRUCTIVE`, `SECRET_EXPOSURE`, `DATA_LOSS`, `EXTERNAL_PUBLICATION`, `SERVICE_DISRUPTION`.
   - Preserve the specification's caution that `DATA_LOSS` is contextual and is not inferred solely from writing a database.

9. **Approval requirement vocabulary**
   - Define `NONE`, `HUMAN_APPROVAL_REQUIRED`, and `EXPLICIT_HIGH_RISK_APPROVAL`.
   - State that this is a minimum-control classification, never an approval or authorization.

10. **Additional independent dimensions**
    - Define `reversibility`: `REVERSIBLE`, `RECOVERABLE`, `PARTIALLY_REVERSIBLE`, `IRREVERSIBLE`.
    - Define the required meaning of explicit `target_scope`.
    - Define `secret_handling`: `NONE`, `INDIRECT_ONLY`, `SENSITIVE_OUTPUT_POSSIBLE`, `PROHIBITED`.
    - Define `service_impact`: `NONE`, `LOCAL_ONLY`, `DEGRADED`, `OUTAGE_POSSIBLE`.

11. **Unknown behavior and stop conditions**
    - Record unknown behavior rather than filling gaps optimistically.
    - Require `PROPOSED` or `BLOCKED` treatment where the specification's status vocabulary is later applied.
    - State the Stage 1 boundary-level stops: unknown target, unknown side effect, unclear permission or recovery boundary, conflicting authority, and any attempt to treat classification as permission.
    - Do not reproduce the complete AI command-selection protocol here; link to its future Stage 6 deliverable in the implementation specification.

12. **Provenance and Control Desk relationship**
    - State that OKCI may summarize or reference authoritative records but does not create verification, approval, evidence, milestone, or risk authority.
    - State that registry status, compatibility, and verification rules are later-stage material unless needed as a short boundary clarification.

13. **Out-of-scope and next-stage boundary**
    - Identify schema, registry, profiles, templates, protocol, validation, examples, integration, automation, execution, publication, and deployment as later or excluded work.

14. **Change control and references**
    - Require review against the implementation specification and exact future approval before vocabulary changes.
    - Link to existing canonical documents rather than duplicating them.

## 7. Content that remains exclusively in the implementation specification

The following should remain detailed in `IMPLEMENTATION-SPECIFICATION.md` and should be referenced from the Stage 1 document rather than copied:

- The complete YAML command-record schema and field contract.
- Machine-readable validation-schema requirements and registry-template requirements.
- Illustrative command records and their detailed classifications.
- Detailed verification-status derivation, freshness, invalidation, and reference-resolution rules.
- The complete environment compatibility model and environment-profile identifiers.
- SQLite source-behavior assessment and the historical `E-2026-003` limitations.
- Detailed evidence-reference validation results.
- The full AI command-selection protocol and its consequential-action stop list.
- The proposed registry/profile directory layout and schema-evolution approach.
- Educational/commercial portability material.
- The eight-stage implementation roadmap, full specification acceptance criteria, and the specification's unresolved review decisions.

The Stage 1 document may summarize boundaries necessary to prevent misuse, but it must not become a second copy of these authorities.

## 8. Later-stage and out-of-scope content

### Later stages

- Stage 2: human-readable field contract, machine-readable validation schema, registry template, conditional rules, provenance, references, status, compatibility, and redaction.
- Stage 3: evidence-backed command registry and registry validation notes.
- Stage 4: environment profiles and compatibility evidence.
- Stage 5: this repository's project operational profile.
- Stage 6: mandatory AI command-selection protocol and detailed stop conditions.
- Stage 7: minimal cross-references into STS documentation, with separate approval for canonical-file changes.
- Stage 8: read-only validation and educational examples.

### Explicit exclusions from Stage 1

- No `command-registry.yaml` or command records.
- No machine-readable schema or validator.
- No environment files or project operational profile.
- No templates or examples.
- No edits to `METHOD.md`, `CONTROL-DESK.md`, `README.md`, templates, checklists, or existing Control Desk records.
- No Control Desk approval, milestone, evidence, verification, decision, or risk record.
- No command execution, automation, dependency installation, external action, commit, staging, push, tag, publication, or deployment.

## 9. Dependencies and risks

### Dependencies

- Human review and explicit approval of the exact Stage 1 file path and contents.
- `METHOD.md` for lifecycle and control requirements.
- `CONTROL-DESK.md` for authority, gates, freshness, invalidation, and the read-only boundary.
- Existing Control Desk documentation for authoritative-record and derived-data boundaries.
- The final implementation specification and final review copy as the design reference.

### Risks and controls

| Risk | Control for future implementation |
|---|---|
| Stage 1 accidentally creates a second authority | Keep one document; link to existing canonical documents; state authority boundaries explicitly |
| Vocabulary hides side effects | Keep operation, effects, risks, approval, reversibility, target, secrets, and service impact independent |
| Classification is treated as permission | State that approval requirement is descriptive and Control Desk approval remains authoritative |
| Unknown behavior receives an optimistic classification | Require explicit unknowns and `PROPOSED`/`BLOCKED` treatment at the boundary level |
| Future files are created prematurely | Restrict the approved implementation to the one exact file; defer registry/schema/profile files |
| Existing documents drift | Prohibit canonical-document edits in Stage 1 and require links instead of duplicate text |
| Proposed path is mistaken for approved layout | Record the path as a recommendation requiring explicit approval |
| Untracked assessment work is disturbed | Preserve all existing files under `assessments/OKCI-001/` and inspect final status |

## 10. Acceptance criteria

Stage 1 should be considered complete only if all of the following are observable in the approved future file and its review evidence:

1. The exact approved path is recorded and only the approved Stage 1 documentation file is added.
2. OKCI, project operational profiles, and the Control Desk are defined as separate layers with unambiguous responsibility boundaries.
3. The Control Desk remains authoritative for approvals, milestones, risks, evidence, verification, freshness, invalidation, decisions, checkpoints, and history.
4. The six operation values are present with the specification's meanings.
5. The six effect values are present with the specification's meanings.
6. The five risk flags are present with the specification's meanings and contextual `DATA_LOSS` rule.
7. The three approval requirements are present and explicitly described as minimum controls, not authorization.
8. Reversibility, target scope, secret handling, and service impact are defined independently.
9. Unknown behavior and boundary-level stop conditions are explicit, without silently expanding into the full Stage 6 protocol.
10. No registry, schema, template, profile, validator, execution capability, or Control Desk record is created or modified.
11. Existing canonical documents are linked and their authority is not duplicated or contradicted.
12. The final diff/status review confirms no unrelated file changes, secrets, or Git-mutating actions.

## 11. Verification and evidence plan

Verification for the future implementation should be read-only and documentation-focused:

- Inspect the exact final diff and confirm only the approved path changed.
- Check the document for all required headings and exact enum values.
- Compare the architecture and vocabulary against the implementation specification and final review copy for omissions or unauthorized changes.
- Review links to `METHOD.md`, `CONTROL-DESK.md`, and relevant Control Desk documentation.
- Search for duplicate or conflicting authority claims, especially claims that OKCI approves, executes, verifies, or changes Control Desk state.
- Confirm the document labels examples or future capabilities as planned, if any are included.
- Run proportionate documentation checks such as `git diff --check` only after the future implementation is approved; no project script or illustrative command is needed for Stage 1.
- Record the review result through the applicable approved STS process. This report does not create that record.

Expected evidence: the approved file diff, reviewer decision, an enum/heading review checklist or equivalent review note, link/reference review, and final Git status. A Control Desk verification record would be required only under a separately approved execution milestone; creating one is excluded from this task.

## 12. Exact implementation boundary requiring future approval

Future implementation may be authorized only for the following exact boundary:

- Add one new file at `okci/architecture-and-classification.md`, or use a different exact path only if the approving human explicitly substitutes it.
- Create the containing `okci/` directory only as required for that file.
- Add only the Stage 1 headings and contents described in Section 6.
- Reference, but do not modify, `METHOD.md`, `CONTROL-DESK.md`, `control-desk/README.md`, `control-desk/schema.md`, and the implementation specification.
- Do not create or modify any registry, schema, template, profile, example, validator, project documentation, or Control Desk record.
- Do not execute commands beyond approved read-only inspection and proportionate documentation verification.
- Do not commit, stage, push, tag, publish, deploy, install dependencies, or perform external actions unless separately authorized.

The approval must name the exact file path, mission, exclusions, risks, acceptance criteria, evidence plan, reviewer/approver, and any allowed verification commands. Approval of this report is not approval of the implementation itself unless the human explicitly states that this exact boundary is approved.

## 13. Unresolved decisions

1. Is `okci/architecture-and-classification.md` the preferred exact path, or should the future approved path be another single file such as `okci/README.md` or `okci/classification.md`?
2. Should architecture and vocabulary remain one document after Stage 1, or should a later approved milestone split them based on demonstrated review or maintenance needs?
3. Which boundary-level stop conditions belong in Stage 1, versus exclusively in the later AI command-selection protocol?
4. Should Stage 1 include a short verification-authority summary, or only the architecture/classification boundary and a link to the specification's detailed status rules?
5. What terminology, if any, should be added for operation context without changing the approved six operation values?
6. What review evidence format will the human approver require for the future documentation-only milestone?

## 14. Final Git status and confirmation of changes made

Final status observed after creating this report:

- Branch: `main`.
- HEAD remains `6c9f7d5`.
- Remote relationship remains `main...origin/main [ahead 2]`.
- Working tree remains represented as `?? assessments/`; the directory was pre-existing and untracked.
- This report is the only file created during this task.
- No existing file was modified by this task.
- No file was staged or committed.
- No push, tag, publication, deployment, dependency installation, project script, illustrative command, or external action was performed.

This report stops at scope preparation. Stage 1 implementation remains unauthorized pending explicit human approval of its exact file scope.
