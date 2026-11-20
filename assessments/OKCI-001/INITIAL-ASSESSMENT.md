# STS-OKCI-001 — Initial Assessment

## Assessment status

- Assessment type: Read-only initial assessment
- Project: STS Controlled AI Engineering
- Repository: `~/sts-repos/sts-controlled-ai-engineering`
- Assessment date: 2026-11-20
- Implementation status: Not begun
- Files modified during assessment: This assessment file only
- Commands from the requested example list executed: No
- Dependencies installed: No
- Git commit, push, tag, publication, or deployment performed: No

## Evidence classification

- **Confirmed fact:** Directly observed in the current repository or Git state.
- **Historical information:** Recorded by existing project records but not re-executed during this assessment.
- **Inference:** Reasoned from observed structure or documentation.
- **Recommendation:** Proposed future design, not implemented capability.

## A. Current State

### A.1 Confirmed repository state

- Branch: `main`
- Working tree: clean at inspection time
- Remote relationship: `main...origin/main [ahead 2]`
- HEAD: `6c9f7d5`
- Latest commit: `Add usage help to Control Desk tools; record M-2026-028 and A-2026-025`
- The supplied repository snapshot in `AGENTS.md` is stale: it describes an earlier HEAD and a documentation-only tree, while the current tree contains an expanded Control Desk system.

### A.2 Existing files and responsibilities

| Area | Existing responsibility |
|---|---|
| `METHOD.md` | Canonical 13-stage controlled engineering lifecycle, risk levels, approval boundaries, verification, Git checkpoint, and completion standard |
| `AGENTS.md` | Repository instructions for AI assistants and documentation scope |
| `CONTROL-DESK.md` | Control Desk state machine, gates, freshness, invalidation, authority, and read-only boundary |
| `README.md` | Project overview, method summary, toolkit contents, and release information |
| `templates/` | Reusable milestone, approval, project-status, risk, and verification formats |
| `checklists/` | Before-commit, before-deployment, and high-risk-action controls |
| `control-desk/README.md` | File-based Control Desk layout, record rules, authoritative/derived boundaries, and documented read-only tools |
| `control-desk/schema.md` | Logical record schema for milestones, approvals, risks, verifications, evidence, and transitions |
| `control-desk/projects.json` | Explicit cross-project registry |
| `.sts-project.json` | Minimal project manifest identifying this repository and its Control Desk directory |
| `control-desk/validate.py` | Read-only record validation tool |
| `control-desk/index.py` | Read-only record indexing tool |
| `control-desk/index_sqlite.py` | Derived SQLite projection builder |
| `control-desk/render.py` | Derived HTML presentation generator |
| `control-desk/discover_projects.py` | Controlled project discovery tool |
| `control-desk/milestones/` | Milestone records |
| `control-desk/approvals/` | Human approval records |
| `control-desk/risks/` | Risk records |
| `control-desk/verifications/` | Verification records |
| `control-desk/evidence/` | Evidence records, including historical command output summaries |
| `control-desk/reviews/` | Historical review packets and decision material |
| `examples/` | Historical worked examples, including project-specific testing and command references |

### A.3 Existing record conventions

The repository already provides conventions that OKCI should preserve:

1. Markdown records are authoritative.
2. YAML front matter supplies structured metadata.
3. Stable IDs are used for traceability.
4. Records link to one another instead of silently duplicating authority.
5. SQLite and HTML are derived, rebuildable projections.
6. Historical decisions and limitations remain visible.
7. Evidence records distinguish observed results from unsupported claims.
8. Approval applies only to the exact approved scope.
9. The Control Desk is read-only and does not itself execute, approve, deploy, or modify repositories.
10. Git history provides reviewable checkpoints and recovery boundaries.

### A.4 Existing OKCI capability

The proposed OKCI structure does not currently exist as a complete system. Parts of the required capability exist indirectly:

- Commands appear in `METHOD.md`, checklists, Control Desk documentation, milestone records, verification records, and historical examples.
- Project registration exists through `projects.json` and `.sts-project.json`.
- Project status contains runtime, operating-system, command, port, database, and deployment fields.
- Evidence and verification records can preserve actual command results.

There is no central command registry, command-record schema, environment-profile collection, project operational-profile template, or mandatory AI command-selection protocol.

## B. Gap Analysis

### B.1 Missing capability

- Reusable central command registry
- Standard command record format
- Explicit command safety taxonomy
- Explicit command verification-status taxonomy
- Platform and shell environment profiles
- Project-specific operational-profile template
- Mandatory AI command-selection protocol
- Command freshness, deprecation, and limitation fields
- Direct linkage between command records and execution evidence

### B.2 Incomplete capability

- Existing command references are distributed across documents.
- Existing commands do not consistently record prerequisites, side effects, platform compatibility, or exact verification procedures.
- Existing project manifests identify repositories but do not describe their operational workflows.
- Existing project-status records have useful runtime fields but are not specialized for command selection.
- Existing evidence records may preserve historical execution results, but there is no uniform command identifier or registry status.

### B.3 Reuse recommendation

OKCI should reuse the existing Control Desk for approvals, evidence, verification, freshness, invalidation, and history. It should not create a second approval system, evidence system, project registry, or milestone state machine.

The recommended boundary is:

```text
OKCI registry       Reusable command knowledge
Project profile     Repository-specific operating context
Control Desk        Approval, execution evidence, verification, and history
```

## C. Proposed Architecture

### C.1 Recommended structure

The following is a recommendation only. It was not created during this assessment.

```text
okci/
├── README.md
├── command-registry.yaml
├── safety-classification.md
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
    └── control-desk-commands.yaml
```

### C.2 Responsibilities

| Proposed document | Responsibility |
|---|---|
| `okci/README.md` | Explain purpose, authority, usage, portability, and relationship to Control Desk |
| `command-registry.yaml` | Store reusable command records |
| `safety-classification.md` | Define OBSERVE through PUBLISH categories and context-sensitive classification |
| `verification-status.md` | Define VERIFIED, PROJECT-DOCUMENTED, HISTORICAL, PROPOSED, ENVIRONMENT-SPECIFIC, DEPRECATED, and BLOCKED |
| `ai-command-selection.md` | Define the mandatory AI selection and evidence procedure |
| `environments/*.yaml` | Document supported platform, shell, executable, path, package, dependency, and compatibility facts |
| `profiles/project-operational-profile.md` | Reusable repository-specific operational profile template |
| `templates/command-record.yaml` | Standard command record format |
| `templates/project-operational-profile.md` | Portable profile template for individual repositories |
| `examples/` | Educational and project-specific examples backed by evidence |

### C.3 Command record requirements

Each command record should include:

- Unique command ID
- Command name
- Exact command syntax or constrained syntax pattern
- Purpose
- Category
- Operating systems
- Shells
- Required prerequisites
- Expected result
- Risk classification
- File-modification behavior
- Network behavior
- Elevated-privilege requirement
- Approval requirements
- Verification procedure
- Failure conditions
- Known limitations
- Evidence source
- Verification status
- Last verified date, when known

It should also support working directory, argument restrictions, safe/unsafe variants, expected exit codes, secret exposure concerns, source commit, deprecation reason, and linked evidence or verification IDs.

### C.4 Safety classification

The proposed categories are:

- `OBSERVE` — Read-only environment and repository inspection
- `INSPECT` — Read-only source and configuration examination
- `ANALYZE` — Diagnostics, calculations, and non-mutating analysis
- `PREPARE` — Preparing changes or staged operations
- `MODIFY` — Creating, editing, or deleting files
- `EXECUTE` — Running programs, scripts, and services
- `NETWORK` — Downloading, uploading, or communicating externally
- `PRIVILEGED` — Requiring elevated permissions
- `DESTRUCTIVE` — Capable of irreversible data loss
- `PUBLISH` — Commits, pushes, releases, deployments, and publication

Classification must consider exact arguments, redirection, scripts, targets, working directory, and execution context. It must not rely only on executable names.

### C.5 Verification statuses

The registry should use the requested statuses:

- `VERIFIED` — Executed successfully under a recorded environment and evidence reference
- `PROJECT-DOCUMENTED` — Supported by current project documentation but not independently executed for the registry record
- `HISTORICAL` — Execution or result is recorded historically but is not current verification
- `PROPOSED` — Suggested but not yet supported by project evidence
- `ENVIRONMENT-SPECIFIC` — Verified or documented only for a named environment
- `DEPRECATED` — Previously useful but no longer recommended
- `BLOCKED` — Known or suspected failure, missing prerequisite, or prohibited use

Registry status must never be treated as a substitute for current execution evidence.

### C.6 AI command-selection protocol

The future protocol should require an AI assistant to:

1. Inspect the actual environment.
2. Read `AGENTS.md` and other repository instructions.
3. Inspect repository structure and current Git state.
4. Identify the task and intended outcome.
5. Consult the central command registry.
6. Consult the project operational profile.
7. Check prerequisites, shell, platform, and compatibility.
8. Select the safest appropriate command variant.
9. Explain unfamiliar or consequential commands.
10. Obtain approval where required.
11. Execute only authorized operations.
12. Capture actual execution results without exposing secrets.
13. Verify the result using evidence.
14. Record useful discoveries, corrections, and changed assumptions.

If no suitable verified command exists, the AI must investigate before proposing one. It must not invent command availability, execution results, or verification evidence.

## D. Command Inventory

The following inventory was reconstructed from repository documentation and the user-provided examples. No requested example command was executed during this assessment.

| Command | Category | Known purpose | Evidence source | Status | Outstanding uncertainty |
|---|---|---|---|---|---|
| `git status --short --branch` | OBSERVE, INSPECT | Inspect branch and concise working-tree state | `control-desk/milestones/M-2026-001.md`, `M-2026-028.md` | PROJECT-DOCUMENTED | Current output was not collected for an OKCI record |
| `git diff` | INSPECT, ANALYZE | Review unstaged changes | `METHOD.md`, `checklists/before-commit.md` | PROJECT-DOCUMENTED | Exact safe-use guidance is not centralized |
| `git diff --check` | ANALYZE | Detect whitespace errors in changes | `METHOD.md`, verification records | PROJECT-DOCUMENTED | Current execution was not performed for this assessment |
| `python3 control-desk/validate.py` | ANALYZE, EXECUTE | Validate Control Desk records | `control-desk/README.md`, verification records | PROJECT-DOCUMENTED; historical passes exist | Historical passes are not current verification |
| `python3 control-desk/index.py` | ANALYZE, EXECUTE | Produce a read-only record index | `control-desk/README.md`, verification records | PROJECT-DOCUMENTED | Output contract and freshness behavior need a command record |
| `python3 control-desk/index_sqlite.py --database control-desk/control-desk.sqlite3` | ANALYZE, MODIFY | Build a derived SQLite projection | `control-desk/README.md`, `control-desk/sqlite-evaluation.md` | PROJECT-DOCUMENTED | It writes a derived artifact and is not filesystem-read-only |
| `python3 control-desk/render.py --database control-desk/control-desk.sqlite3` | ANALYZE, MODIFY | Generate derived HTML presentation | `control-desk/README.md`, `control-desk/render.py` | PROJECT-DOCUMENTED | Output redirection and generated-file handling need explicit records |
| `python3 control-desk/discover_projects.py` | OBSERVE, ANALYZE | Discover candidate project repositories | `control-desk/README.md`, evidence records | PROJECT-DOCUMENTED | Discovery does not authorize onboarding or indexing |
| `python -m py_compile qr_core.py` | ANALYZE, EXECUTE | Compile one Python file | User-provided example | PROPOSED | `qr_core.py` was not found in this repository |
| `python -m unittest discover -s tests -v` | ANALYZE, EXECUTE | Run Python unittest discovery | User-provided example | PROPOSED | No repository `tests/` contract was found here |
| `python -m pip list` | OBSERVE, ANALYZE | Inspect installed Python packages | User-provided example | PROPOSED | Environment-specific and potentially revealing in some contexts |
| `gh auth status` | OBSERVE, NETWORK | Inspect GitHub CLI authentication state | User-provided example | PROPOSED | Not documented in this repository; may reveal account/server information |
| `curl http://127.0.0.1:8766/health` | OBSERVE, NETWORK | Inspect a local service health endpoint | User-provided example | PROPOSED | Port and endpoint are not documented here |
| `git commit`, `git push`, tags, releases, deployment | PUBLISH | Create durable or external state | `METHOD.md`, checklists | PROJECT-DOCUMENTED as controlled actions | Requires separate authorization and must not be treated as ordinary commands |

### D.1 Context-sensitive classification examples

- `python3 control-desk/index_sqlite.py --database :memory:` differs from writing to a repository database.
- `render.py` writing to stdout differs from redirecting output into `dashboard.html`.
- `curl` against localhost differs from communicating with a public endpoint.
- `git diff` is observational, while `git diff > report.txt` writes a file.
- `pip list` is generally observational, while package installation is modifying and network-accessing.

### D.2 Command families not established by current evidence

The current repository does not establish verified commands for:

- GitHub CLI workflows
- Termux package management
- The requested `qr_core.py` compilation command
- The requested `unittest` discovery command
- Local health checks on port `8766`
- General backup, recovery, and troubleshooting procedures
- Project-specific commands for unrelated repositories

These should remain `PROPOSED` or `ENVIRONMENT-SPECIFIC` until investigated and recorded.

## E. Integration Plan

### E.1 Existing files that may require later updates

No files were changed during this assessment. Future implementation may update:

1. `METHOD.md` — require AI agents to consult OKCI before selecting unfamiliar or consequential commands and to record actual results as evidence.
2. `AGENTS.md` — point assistants to OKCI and require distinction between registry status and execution evidence.
3. `README.md` — document OKCI as a provider-independent toolkit component.
4. `templates/project-status.md` — link to a project operational profile without duplicating it.
5. `templates/verification-record.md` — add command ID, exact command variant, environment profile, and execution-result fields.
6. `control-desk/schema.md` — optionally support command, environment, evidence, and verification links.
7. `control-desk/README.md` — define the boundary between reusable OKCI knowledge and project-specific Control Desk evidence.

The user explicitly restricted this phase from modifying `METHOD.md` or `AGENTS.md`; those changes are therefore future work only.

### E.2 Proposed additions

- `okci/README.md`
- `okci/command-registry.yaml`
- `okci/safety-classification.md`
- `okci/verification-status.md`
- `okci/ai-command-selection.md`
- `okci/environments/`
- `okci/profiles/project-operational-profile.md`
- `okci/templates/command-record.yaml`
- `okci/templates/project-operational-profile.md`
- A project-specific operational profile for this repository

### E.3 Dependencies between changes

1. Approve the architecture and record schema.
2. Define safety and verification vocabularies.
3. Create the initial registry using only supported evidence.
4. Create environment profiles with unknowns explicitly marked.
5. Create the repository operational profile.
6. Define the AI selection protocol.
7. Integrate links and optional metadata with existing methodology and Control Desk records.
8. Verify documentation consistency and inspect the final diff.

## F. Risks

| Risk | Impact | Proposed control |
|---|---|---|
| Documentation duplication | Conflicting instructions or authorities | Keep OKCI for reusable command knowledge and Control Desk for approvals/evidence/history |
| Outdated commands | AI selects obsolete or unsafe commands | Require source, status, date, limitations, and deprecation fields |
| Documented mistaken for verified | False confidence | Enforce distinct verification statuses and evidence links |
| Platform incompatibility | Commands fail or behave differently | Require platform and shell fields; preserve unknowns |
| Argument-dependent side effects | A seemingly safe command modifies files or contacts external systems | Record exact syntax and classify variants by arguments and redirection |
| Unsafe AI command selection | Unauthorized or destructive action | Require protocol checks, approval gates, stop conditions, and evidence |
| Registry encourages automation | Human control boundary weakens | Keep the first system documentation-only and provider-independent |
| Sensitive output in records | Credentials or private data are exposed | Reuse existing redaction rules and prohibit secrets in registry/evidence |
| Excessive documentation overhead | Knowledge becomes stale or ignored | Start with high-frequency commands and require evidence proportional to value |
| Project-profile drift | AI follows obsolete repository instructions | Add freshness, source commit, review date, and limitation fields |
| Historical records treated as current | Old results become false present claims | Preserve `HISTORICAL` status and source dates |

## G. Implementation Milestones

### Milestone 1 — Approve OKCI boundary and schema

Define the OKCI authority boundary, command-record fields, safety classes, and verification statuses.

### Milestone 2 — Create the reusable registry

Document a small initial set of Git, filesystem, Python, and existing Control Desk commands. Mark unsupported examples as `PROPOSED`.

### Milestone 3 — Create environment profiles

Document Android Termux, Linux, macOS, and relevant Windows facts only when evidence exists.

### Milestone 4 — Create the project operational profile

Document this repository’s structure, runtime assumptions, validation tools, derived artifacts, safety restrictions, and evidence procedures.

### Milestone 5 — Create the AI command-selection protocol

Document the mandatory inspect, consult, classify, approve, execute, capture, verify, and record sequence.

### Milestone 6 — Integrate with STS records

Add minimal links from the method, agent instructions, templates, and Control Desk schema. Do not duplicate existing authority.

### Milestone 7 — Validate educational portability

Add beginner-friendly examples and exercises that reference the same registry and safety definitions without introducing a separate methodology.

Each milestone should have its own scope, approval, evidence, verification, and Git checkpoint under the existing STS lifecycle.

## H. Approval Request

### Proposed implementation scope

Approve a documentation-and-YAML OKCI layer that:

- Adds a portable `okci/` directory.
- Defines a central command registry and record format.
- Defines safety classifications and verification statuses.
- Adds platform environment profiles.
- Adds a project operational-profile template and this repository’s profile.
- Adds the AI command-selection protocol.
- Reuses Control Desk approvals, evidence, verification, freshness, and history.
- Makes no command-execution engine or automation.
- Installs no dependencies.
- Does not replace Markdown as the source of truth.
- Does not weaken human approval requirements.
- Does not publish, deploy, commit, push, tag, or create a commercial platform.

### Explicitly out of scope

- Modifying `METHOD.md` or `AGENTS.md` during this assessment phase
- Creating the command registry during this assessment phase
- Creating operational profiles during this assessment phase
- Executing the listed example commands
- Installing packages or dependencies
- Automatic command execution or approval
- Hosted services, commercial software, or external publication

### Human decision requested

Please approve, revise, or reject the proposed implementation scope before any OKCI implementation files are created.

## Final assessment conclusion

The repository already contains the control and evidence foundation required for OKCI. The appropriate improvement is a small, portable knowledge layer that describes commands and operating contexts while leaving authorization, execution evidence, verification, and historical truth with the existing STS Control Desk and methodology.

Implementation has not begun.
