# STS-OKCI-001 — Stage 2 Scope Proposal

Status: Proposal for human review; Stage 2 implementation is not authorized by this report.

Date: 2026-11-20

Repository: `sts-controlled-ai-engineering`

## 1. Mission and scope

The mission is to prepare an implementation-ready, evidence-based scope for Stage 2 of Operational Knowledge & Command Intelligence (OKCI):

1. a human-readable command-record field contract;
2. a machine-readable validation schema for command records; and
3. a registry template for a future command registry.

This report assesses the smallest coherent file set, proposed structure, validation boundaries, risks, acceptance criteria, and verification plan. It does not implement any Stage 2 deliverable, create command records, populate a registry, create a validator, or change Stage 1 or canonical STS documentation.

Evidence labels used here:

- **Observed fact** — directly established from the current repository or Git state.
- **Historical evidence** — stated by an existing report or record and not re-executed as a new milestone.
- **Inference** — reasoned from observed documents or structure.
- **Recommendation** — proposed design for a future approved implementation.
- **Unresolved decision** — requires human review or evidence not available in this assessment.

## 2. Initial repository state

Observed before creating this report:

- Branch: `main`.
- HEAD: `6c9f7d5` (`Add usage help to Control Desk tools; record M-2026-028 and A-2026-025`).
- Remote relationship: `main...origin/main [ahead 2]`.
- Working tree status: pre-existing untracked `assessments/` and `okci/` directories.
- `okci/architecture-and-classification.md` exists and is untracked.
- This report did not exist before this task.
- No Stage 2 schema, registry template, command registry, environment profile, project operational profile, or validator was observed in the requested OKCI scope.
- The repository is documentation- and control-record-focused; no application test suite is established by `AGENTS.md`.

The pre-existing untracked files were treated as user work and preserved. No Git staging, commit, push, tag, publication, deployment, dependency installation, project script, or illustrative command was performed.

## 3. Files inspected

Instructions and canonical control sources:

- `AGENTS.md`
- `METHOD.md`
- `CONTROL-DESK.md`
- `control-desk/README.md`
- `control-desk/schema.md`

OKCI and Stage 1 sources:

- `okci/architecture-and-classification.md`
- `assessments/OKCI-001/IMPLEMENTATION-SPECIFICATION.md`
- `assessments/OKCI-001/FINAL-REVIEW-COPY.md`
- `assessments/OKCI-001/STAGE-1-SCOPE-PROPOSAL.md`
- `assessments/OKCI-001/STAGE-1-IMPLEMENTATION-REPORT.md`

Additional repository context inspected where relevant:

- `README.md`
- `control-desk/architecture.md`
- `control-desk/model-analysis-boundary.md`
- `control-desk/sqlite-evaluation.md`
- representative existing Control Desk approval, milestone, evidence, risk, and verification records.

The implementation specification and final review copy have identical section structure and content as observed in the existing Stage 1 materials; the Stage 1 implementation report records their prior comparison as byte-identical. That comparison is historical evidence, while the current architecture file and Git state are current observations.

## 4. Stage 1 completion assessment

### Confirmed or directly observed

`okci/architecture-and-classification.md` exists. It defines the three-layer model (OKCI, project operational profiles, and STS Control Desk), responsibility boundaries, provenance limits, unknown-behavior stop conditions, and the Stage 1 classification vocabulary.

The architecture file contains the exact approved values from the implementation specification for:

- operation: `OBSERVE`, `INSPECT`, `ANALYZE`, `PREPARE`, `MODIFY`, `EXECUTE`;
- effects: `FILESYSTEM_READ`, `FILESYSTEM_WRITE`, `NETWORK_ACCESS`, `PRIVILEGED_ACCESS`, `PROCESS_CREATION`, `EXTERNAL_STATE_CHANGE`;
- risk flags: `DESTRUCTIVE`, `SECRET_EXPOSURE`, `DATA_LOSS`, `EXTERNAL_PUBLICATION`, `SERVICE_DISRUPTION`;
- approval requirements: `NONE`, `HUMAN_APPROVAL_REQUIRED`, `EXPLICIT_HIGH_RISK_APPROVAL`;
- reversibility: `REVERSIBLE`, `RECOVERABLE`, `PARTIALLY_REVERSIBLE`, `IRREVERSIBLE`;
- secret handling: `NONE`, `INDIRECT_ONLY`, `SENSITIVE_OUTPUT_POSSIBLE`, `PROHIBITED`; and
- service impact: `NONE`, `LOCAL_ONLY`, `DEGRADED`, `OUTAGE_POSSIBLE`.

No additional enum value was observed. `target_scope` is intentionally described as structured scope information rather than an invented Stage 1 enum.

### Historical evidence and assessment

`STAGE-1-IMPLEMENTATION-REPORT.md` records the approved one-file implementation, comparison against the specification and final review copy, acceptance-criteria results, and documentation verification. It states that Stage 1 did not create a registry, command records, schema, validator, profiles, examples, protocol, or Control Desk records.

Assessment: Stage 1 is complete as a documentation implementation milestone, subject to the historical report’s stated evidence and the current existence of its architecture file. This does not mean the broader OKCI initiative is complete, and it does not authorize Stage 2. The Stage 1 file remains untracked in the current working tree, so its repository checkpoint/publication state is not inferred to be complete.

### Classification integrity requirement for Stage 2

Stage 2 must import the exact Stage 1 values without silently adding, renaming, narrowing, or broadening them. Any proposed new enum must be identified as a change request and separately approved; it must not be introduced merely to make schema design convenient.

## 5. Schema design analysis

### Recommended representation

Recommendation: represent one command record as a nested YAML document, with the YAML parsed into a data model and validated by a JSON Schema document. JSON Schema is appropriate because it can express types, required fields, enumerations, arrays, nested objects, property restrictions, and many conditional requirements. YAML is the authoring/registry serialization; JSON Schema validates the resulting data model, not YAML syntax, comments, anchors, duplicate-key behavior, or every YAML-specific semantic.

Recommendation: use JSON Schema Draft 2020-12, pending approval. It provides the needed conditional and composition vocabulary (`if`/`then`/`else`, `oneOf`, `$defs`, `$ref`, `const`, and `unevaluatedProperties`) and has a clear current standard form. The schema file must declare its `$schema` URI and `$id`; the Stage 2 implementation should record the chosen validator and supported dialect in its verification evidence. This is a recommendation, not an assumption that a validator or dependency is approved.

### Nested structure versus flat structure

Recommendation: use a nested structure with separate objects for:

- `identity` — stable command ID, human title, lifecycle status, and version lineage;
- `syntax` — executable or command form, arguments/constraints, shell assumptions, and invocation limitations;
- `context` — target and working-context assumptions, without embedding secrets;
- `classification` — operation, effects, risk flags, approval requirement, reversibility, secret handling, and service impact;
- `prerequisites` — required tools, permissions, files, state, or human checks;
- `compatibility` — independent compatibility claims, scope, evidence references, and limitations;
- `verification` — status summary and authoritative verification references, with current and historical evidence kept distinct;
- `provenance` — source authority, authorship, review information, and source references; and
- `limitations` — unknowns, exclusions, non-guarantees, and known failure boundaries.

Nested separation makes independent dimensions visible and reduces accidental coupling, while allowing a future validator to reject unrelated or misspelled properties. A flat structure would be shorter but would make ownership, conditional rules, and future migration less clear. The final nesting and field names remain subject to approval and contract review.

### Versioning and identity

Recommendation:

- Use a stable, immutable `command_id` for identity and references. IDs must not be reused after deprecation.
- Use a record `record_version` or equivalent revision for changes to the record, separate from `command_id`.
- Include a top-level `schema_version` identifying the command-record contract; do not use a free-form prose label as the only version indicator.
- Use lowercase `snake_case` field names and uppercase exact enum values, matching Stage 1.
- Use repository-relative or explicitly typed references for repository records, and stable IDs for Control Desk records. Do not use ambiguous bare filenames where an authoritative record ID is available.
- Preserve deprecated records and link replacements or superseding records; do not overwrite history or recycle IDs.

Schema version compatibility must be documented as a policy in the contract. A schema version change may be backward-compatible, migration-compatible, or breaking; passing a newer schema must not be treated as proof that an older consumer understands new semantics.

### Additional-property restrictions

Recommendation: reject unknown properties in controlled command-record objects using `additionalProperties: false` or the Draft 2020-12 equivalent where composition requires `unevaluatedProperties: false`. This protects classification integrity and prevents silent typos. Extension points, if needed, should be explicit and namespaced rather than an unrestricted catch-all. The implementation must verify how the selected validator handles composition before relying on the restriction.

## 6. Field contract design analysis

The human-readable contract should be the explanatory authority for field meaning and limitations; the machine-readable schema should be the structural enforcement artifact. They must be reviewed together and must not diverge silently.

### Proposed field groups

The contract should define, for every field: name, purpose, type, required/optional status, allowed values or format, conditional rules, provenance expectations, and limitations.

| Group | Representative fields and design intent |
|---|---|
| Identity | `command_id`, `record_version`, `schema_version`, `name`, `status`, `replaced_by`; stable identity and lifecycle traceability. |
| Syntax | command form, executable, argument model, shell/interpreter assumptions, quoting/redirection constraints; must not imply that a name alone determines safety. |
| Context | target kind/constraints, working directory assumptions, environment assumptions, permissions, authentication boundary; unknown context remains unknown. |
| Classification | exact Stage 1 enums and multi-valued effects/risk flags; independent dimensions, not a safety score or authorization. |
| Prerequisites | required tools/versions, permissions, files/state, human checks, and preflight conditions. |
| Compatibility | independent compatibility claims with scope, basis, evidence references, and limitations; not a substitute for verification status. |
| Verification | status summary, scope, current/historical distinction, verification references, and invalidation/freshness fields as applicable. |
| Provenance | source type, source references, author/owner, created/reviewed timestamps, review basis, and record lineage. |
| Limitations | unknowns, exclusions, unsupported targets, failure conditions, redaction notes, and non-guarantees. |

The contract should explicitly state which fields are required for every record, which are required for each lifecycle status, and which are optional only when a stated condition does not apply. Dates should use a declared format (recommendation: RFC 3339 timestamps); identifiers should have documented lexical constraints; lists should specify whether order is meaningful and whether duplicates are allowed.

### Provenance and sensitive data

Command records may reference authoritative records but must not embed secrets, credentials, private keys, access tokens, sensitive command output, or unnecessary personal data. Syntax must be representable without copying secret-bearing arguments. If a command inherently requires sensitive input, the contract should record the handling limitation and a redacted or indirect reference, not the value.

Provenance should identify where the command meaning and each material status claim came from. A source reference alone does not prove that the source is current, authoritative, in scope, or compatible with the record’s target.

### Limitations

The contract must state that a valid record can describe a command without proving that the command is safe to run, applicable to a current project, authorized, compatible with a target, reversible in practice, or verified in the present environment.

## 7. Registry template design analysis

### Recommendation

Recommendation: create one initial registry template file, containing registry metadata and an empty `commands` collection, with no command records. This is preferable to a minimal illustrative record because an illustrative record could be mistaken for evidence-backed content or permission to execute. It is also preferable to multiple files at this stage because no evidence-backed registry population or indexing workflow is authorized.

The template should be a valid YAML document with a declared schema reference, registry format version, registry identifier, and empty command collection. It may include comments explaining where future records belong, but comments must not be the only expression of required structure. The template must not contain a real executable, example target, evidence claim, approval claim, or invented command ID.

### Registry design requirements

- One registry file is the initial source artifact; future partitioning is a migration decision, not an implicit Stage 2 expansion.
- Registry metadata must identify the schema version and registry format version.
- Every future record must have a unique stable `command_id`; duplicate IDs must be invalid.
- Cross-record references must use stable IDs and be resolvable by a future validation workflow.
- Lifecycle status, deprecation, replacement, provenance, and limitations must remain visible.
- The registry is a knowledge artifact, not an approval list, execution queue, evidence store, or Control Desk projection.
- A future index may be derived from the registry, but the authoritative source and rebuild behavior must be documented before indexing is implemented.
- Future migration to multiple files or a database must preserve IDs, meanings, history, and reference resolution.

## 8. Proposed exact file list

The following is the smallest coherent Stage 2 recommendation. All three paths are new and require explicit human approval before implementation.

### 8.1 `okci/command-record-contract.md` — new

**Purpose:** Human-readable field contract and normative explanation of command-record semantics.

**Proposed structure:** status and authority; scope and non-goals; record identity/versioning; field-by-field contract; exact classification vocabulary; syntax/context; prerequisites; compatibility; verification and historical evidence; provenance; limitations; conditional rules; reference conventions; redaction rules; structural/semantic/evidence boundaries; schema relationship; migration/compatibility notes; unresolved limitations.

**Dependencies:** `okci/architecture-and-classification.md`, `METHOD.md`, `CONTROL-DESK.md`, `control-desk/README.md`, `control-desk/schema.md`, and the approved implementation specification.

**Why it belongs in Stage 2:** It defines meanings and control boundaries that cannot be safely delegated to schema keywords.

**Risks:** Contract/schema drift; accidental duplication of Control Desk authority; enum expansion; overly broad claims about verification.

**Acceptance criteria:** Every schema field has a contract entry; required/optional and conditional behavior is explicit; exact Stage 1 values match; provenance, redaction, limitations, and reference semantics are documented; the contract states what it cannot establish; no command record or execution authority is added.

### 8.2 `okci/schema/command-record.schema.json` — new

**Purpose:** Machine-readable structural validation for individual command records, with a declared JSON Schema dialect and schema identity.

**Proposed structure:** `$schema`, `$id`, title/description; top-level type and required groups; `$defs` for reusable identifiers, timestamps, references, enum sets, and nested objects; strict property declarations; conditional rules; compatibility and verification structures; version fields; deprecation/replacement structures; explicit extension policy.

**Dependencies:** The approved field contract and exact Stage 1 vocabulary. A future validator and dependency are not part of Stage 2 unless separately approved; the schema must remain usable independently of a particular validator.

**Why it belongs in Stage 2:** It provides a reviewable structural contract for future YAML records without implementing a validator or populating the registry.

**Risks:** A schema can create false confidence; dialect/validator differences; incomplete conditional expression; unknown-property behavior under composition; structural acceptance of semantically invalid or stale references.

**Acceptance criteria:** The schema declares its dialect and ID; validates types, required fields, exact enums, nested structures, additional-property policy, schema version, compatibility and verification shapes; includes documented conditional rules that are expressible structurally; rejects representative malformed structures; and explicitly leaves semantic/reference/human checks outside schema validation.

### 8.3 `okci/registry-template.yaml` — new

**Purpose:** Empty initial registry container showing how future records will be organized without creating or asserting any command record.

**Proposed structure:** registry identity; registry format version; schema reference/version; provenance for the template itself; empty `commands: []`; optional explicit migration/indexing notes.

**Dependencies:** The approved contract and schema path/identifier.

**Why it belongs in Stage 2:** It establishes the future registry boundary and validates the decision to start with one empty source file.

**Risks:** Empty template mistaken for a complete registry; schema path drift; future duplicate IDs or unresolved references; premature partitioning; accidental inclusion of executable examples.

**Acceptance criteria:** YAML parses as the intended empty structure; it contains no command records or evidence-backed claims; its schema reference matches the approved schema; it documents that it is a template and not authorization; its future duplicate-ID/reference/lifecycle expectations are stated or linked.

### Scope alternatives considered

- A blank file was rejected because it would not communicate the required registry shape.
- A minimal illustrative command record was rejected because Stage 2 must not create command records or imply evidence.
- Multiple registry files were rejected for the initial milestone because they add indexing and migration complexity before evidence-backed population is approved.
- A validator, project profile, environment profile, or Control Desk record was rejected because each is explicitly out of scope.

## 9. Conditional validation requirements

The implementation must distinguish conditions that can be represented in JSON Schema from conditions that require an external resolver or human decision. At minimum, the contract and schema design must address:

1. A `VERIFIED` record must reference valid, appropriately scoped, current verification evidence. Schema can require a verification object and reference shape; it cannot resolve the record or determine freshness and scope.
2. Historical verification must remain historical. A historical reference must not satisfy a current-verification condition merely because it exists.
3. `last_verified` must not be inferred from historical evidence. It must be explicitly sourced from an authoritative current record, or omitted/blocked.
4. Compatibility must be independent of verification status. A compatible record may be unverified; a verified record may be incompatible with a different target.
5. Unknown or ambiguous targets must not be treated as eligible. Schema can require target fields or an explicit unknown state; semantic selection must block eligibility.
6. Evidence references must resolve to appropriate authoritative records, with the correct record type, scope, status, and relation to the command. This is repository/Control Desk resolution, not ordinary schema validation.
7. Source provenance must be present for command meaning and material claims; the source must be reviewed for authority and applicability.
8. Sensitive information must not be embedded in command records. Schema can restrict fields and require redaction metadata; content inspection and secret detection need separate controls.
9. Deprecated records must retain identity and traceability, and a replacement reference must resolve when one is declared. Schema can require shape and conditional presence; lifecycle resolution is semantic.
10. Status values must not be used as authorization. `APPROVED`, if represented as a descriptive status in a future design, must not replace a Control Desk approval record or broaden its scope.

The exact status vocabulary and verification model described in the implementation specification require contract-level review before encoding. Stage 2 must not silently turn a summary status into an authoritative Control Desk state.

## 10. Structural versus semantic versus evidence validation boundaries

| Boundary | Schema can validate | Requires semantic/repository validation | Requires human review or cannot be automated reliably |
|---|---|---|---|
| Structure | Types, required fields, object nesting, array shape, exact enum values, formats where supported, schema/version fields, known-property policy | Whether fields agree with one another and whether references resolve | Whether the record’s structure communicates the intended meaning without ambiguity |
| Classification | Allowed Stage 1 vocabulary and array types | Whether classification matches the exact command, arguments, shell, target, permissions, and effects | Whether unknown behavior warrants blocking, reclassification, or investigation |
| Compatibility | Shape of compatibility claims, scope fields, evidence-reference shape | Target/tool/version/environment resolution and whether evidence supports the claim | Whether evidence is sufficiently current and representative |
| Verification | Shape of status and reference objects; conditional presence of references | Control Desk record existence, type, scope, freshness, invalidation, commit/environment match, and current versus historical status | Acceptance of limited evidence, conflict resolution, and authorization boundaries |
| Provenance | Required source fields and reference syntax | Source existence, authority, lineage, and relation to the claim | Whether a source is trustworthy and appropriate for the decision |
| Security/privacy | Forbidden structural fields and redaction metadata | Secret scanning, content inspection, and sensitive-data classification | Whether a redaction is sufficient and whether publication is appropriate |
| Lifecycle | Status/replacement field shape and permitted values | Duplicate IDs, deprecation traceability, replacement resolution, migration compatibility | Whether a record should be accepted, retired, or blocked |

Passing schema validation therefore establishes only structural conformity. It does not establish command safety, compatibility, verification, authorization, reversibility, absence of secrets, or permission to execute.

## 11. Risks and mitigations

| Risk | Mitigation in Stage 2 design |
|---|---|
| Schema pass is mistaken for safety or authorization | Put the limitation in the contract, schema description, registry template, and acceptance criteria; keep Control Desk authority explicit. |
| Classification vocabulary drifts from Stage 1 | Copy exact values under review; compare against the architecture and approved specification; require separate approval for any new value. |
| Current and historical verification are conflated | Separate current/historical references and status semantics; require explicit authoritative current evidence; never infer `last_verified`. |
| Compatibility is treated as verification | Model compatibility as an independent object and test cases; prohibit status derivation across the two dimensions. |
| Invalid or ambiguous references are accepted | Require typed stable references; plan repository/Control Desk resolution as a separate validation layer; block unresolved required references. |
| Sensitive data enters records | Prohibit secrets in the contract; avoid example commands; use redaction/indirect references; add content review to verification. |
| Additional properties hide typos or unofficial enums | Use strict property policy with explicit extension handling and validator-specific testing. |
| Registry scope expands prematurely | Use one empty template; no records, profiles, validator, index, or execution protocol in Stage 2. |
| Future migration breaks traceability | Require stable immutable IDs, explicit versions, replacement links, and a documented source/derived boundary. |
| Contract and schema diverge | Require paired review, field-to-schema mapping, and negative/conditional test cases before acceptance. |

## 12. Acceptance criteria

Stage 2 should be considered complete only if an explicitly approved implementation satisfies all of the following:

1. Only the approved Stage 2 file paths are added or modified.
2. The human-readable contract defines every schema field, type, requiredness, allowed value, conditional rule, provenance expectation, and limitation.
3. The schema declares a justified dialect and identifier, and its dialect is verified with the selected validator or documented validation method.
4. The schema validates types, required fields, exact Stage 1 enums, nested groups, version fields, compatibility and verification structures, and the approved additional-property policy.
5. The registry template is valid YAML with no command records and clearly states that it is not evidence, authorization, or an execution registry.
6. Stable command IDs, record/schema/registry versioning, naming conventions, deprecation traceability, and reference conventions are documented.
7. Conditional rules distinguish structural requirements from semantic and evidence/reference requirements.
8. Current verification, historical verification, `last_verified`, compatibility, target eligibility, provenance, sensitive-data handling, and deprecated-record traceability are addressed without unsupported inference.
9. No new classification enum is introduced without explicit change approval.
10. The contract and schema do not replace or duplicate Control Desk authority for approvals, evidence, verification, freshness, invalidation, risks, checkpoints, or history.
11. Negative and boundary cases are reviewed, including missing required fields, invalid enum values, unknown properties, invalid conditional combinations, stale/historical references, ambiguous targets, and prohibited sensitive fields.
12. Final diff, whitespace, reference, and Git-status review confirms no Stage 1 file, canonical STS file, Control Desk record, registry record, validator, profile, dependency, or unrelated file was changed.

## 13. Verification plan

Verification for a future approved implementation should be read-only and proportionate:

- inspect the exact final diff and confirm the approved file list only;
- compare the contract’s enum values against `okci/architecture-and-classification.md` and the approved implementation specification;
- validate the JSON Schema’s declared dialect, `$id`, internal references, required fields, enum sets, conditionals, and additional-property behavior using an approved or explicitly documented validator;
- parse the empty registry template and verify its schema reference, empty command collection, and absence of command records;
- perform contract-to-schema field coverage review;
- review representative positive, negative, and conditional data fixtures in memory or temporary files without adding fixtures to the repository unless separately approved;
- verify that malformed structure is rejected and that structurally valid but semantically unsupported references are identified as requiring external resolution;
- review links and stable-ID conventions against Control Desk documentation;
- inspect for secrets, embedded credentials, real target details, and accidental executable examples;
- run `git diff --check` and inspect final `git status --short --branch`;
- record reviewer decisions, limitations, and any validator/version details as evidence under a separately approved STS process.

No command execution, project script execution, dependency installation, external network action, Control Desk record creation, staging, commit, push, tag, publication, or deployment is implied by this plan.

## 14. Explicit implementation boundary requiring future approval

Future implementation may be authorized only after a human reviews and explicitly approves the exact paths, contents, risks, acceptance criteria, and verification plan. The recommended boundary is:

- add `okci/command-record-contract.md`;
- add `okci/schema/command-record.schema.json`;
- add `okci/registry-template.yaml`;
- create `okci/schema/` only as required for the schema file;
- add no command records, evidence-backed examples, environment profiles, project operational profiles, validator, selection protocol, index, Control Desk record, or canonical STS-document change;
- use only approved read-only/documentation validation and any separately approved schema-validation dependency or tool;
- do not stage, commit, push, tag, publish, deploy, or execute illustrative/project commands unless separately authorized.

Approval of this report is not implementation approval unless the human explicitly states that this exact boundary, or a named revised boundary, is approved. Any material scope change requires renewed approval.

## 15. Unresolved decisions

1. Confirm the exact three filenames and whether `okci/schema/` is preferred over another layout.
2. Confirm JSON Schema Draft 2020-12, or select another dialect with documented reasons and validator support.
3. Decide the exact top-level and nested field names, including whether status/version data belongs under `identity` or at the top level.
4. Decide the final lifecycle/status vocabulary for command records without confusing it with Control Desk milestone states.
5. Decide the exact representation of current versus historical verification and the definition of a valid scoped verification reference.
6. Decide whether compatibility claims are embedded in each record or referenced through a later environment-profile model; Stage 2 should define only the approved boundary.
7. Decide the reference URI/ID convention for repository paths, Control Desk records, and future external authoritative sources.
8. Decide whether schema validation will use a repository-approved existing tool, a future dependency, or a documented manual/temporary validation method.
9. Decide the extension policy if future consumers need vendor/project-specific fields; unrestricted additional properties are not recommended.
10. Confirm that the initial registry template must remain empty and that no illustrative record is desired.
11. Confirm the required evidence format and reviewer/approver for the future implementation milestone.

## 16. Final Git status and changes made

After creating this report, the expected final status is:

```text
## main...origin/main [ahead 2]
?? assessments/
?? okci/
```

The only file created by this task is:

- `assessments/OKCI-001/STAGE-2-SCOPE-PROPOSAL.md`

The existing untracked Stage 1 and assessment files were preserved. No Stage 1 file, canonical STS documentation, Control Desk record, schema, registry template, command record, or validator was modified or created. No file was staged or committed. Stage 2 implementation remains unauthorized pending explicit human approval.
