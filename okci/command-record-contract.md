# OKCI Command-Record Contract

Status: Human-readable Stage 2 File 1 contract for STS-OKCI-001.

This is a knowledge contract for reusable command meaning and selection
constraints. It is not a registry, command record, schema, validator, project
profile, execution protocol, evidence store, approval record, or authorization
mechanism. OKCI does not execute commands or create evidence by assertion.

## 1. Authority and boundaries

The STS Control Desk remains authoritative for human approval, exact scope,
risks, milestones, decisions, execution evidence, verification, freshness,
invalidation, checkpoints, and history. Project documentation or a future
project profile is authoritative only for its explicitly declared project
context. OKCI may project and reference those facts, but must not copy,
replace, reconcile, broaden, or override them.

A record, classification, compatibility claim, reference, schema-valid
document, verification projection, or approval requirement never constitutes
permission or authorization. The applicable STS process and Control Desk
record govern the exact operation and target.

This File 1 contract does not define JSON Schema dialect or encoding,
validator behavior, fixtures, registry records, project profiles, automatic
freshness/invalidation, external-locator resolution, execution tooling, or a
separate AI execution protocol. These remain File 2 or later work.

## 2. Identity and versioning

One record describes one reusable command variant, including exact or bounded
syntax and the context needed to interpret it safely.

- `identity.command_id` is stable identity for the variant, unique in a future
  registry, not reused for a materially different command, and retained after
  deprecation.
- `identity.record_version` is a positive integer revision of the record,
  separate from command identity and contract version. Semantic changes
  increment it and retain lineage.
- `identity.schema_version` is a positive integer identifying the contract and
  schema compatibility level. It does not prove migration or consumer
  compatibility.
- Revision reasons and lineage belong in `provenance.review_history`.
  Proposed lexical conventions such as `CMD-` do not establish uniqueness.

Version numbers do not establish execution authority, freshness, validity, or
safety. A contract/schema change may be backward-compatible,
migration-compatible, or breaking; that policy is not inferred from a number.

## 3. Approved root structure

Every field belongs to exactly one of these eleven nested root groups. There
is no twelfth root group; `provenance.source` is nested, not top-level.

```text
identity
command_definition
classification
execution_context
target_constraints
environment_compatibility
verification_projection
references
provenance
lifecycle
limitations
```

## 4. Complete field contract

The following is the authoritative File 1 field map. Required means required
in a complete record unless the stated nullable or conditional rule applies.
Every entry states purpose, semantics, constraints, provenance, sensitivity,
and validation limits.

### 4.1 Identity and command definition

| Field | Contract |
|---|---|
| `identity.command_id` | Required non-secret stable string for one command variant; proposed `CMD-` convention. Must not be reused. Registry-wide uniqueness is outside structural validation. |
| `identity.record_version` | Required integer `>= 1`; semantic revision, distinct from schema version. Change history cannot be proven by structure alone. |
| `identity.schema_version` | Required integer `>= 1`; contract/schema compatibility identifier. It cannot prove migration or consumer support. |
| `command_definition.name` | Required non-empty descriptive name of intent. It must not imply authorization or contain credentials/tokens. |
| `command_definition.purpose` | Required non-empty plain-language intended outcome. It is not proof of behavior, safety, execution, approval, or success; `provenance.source` may support meaning. |
| `command_definition.syntax` | Required object. Conceptual fields: `kind` (`exact`, `constrained`, or `template`), command text, executable, arguments, shell/interpreter, and invocation constraints. Address quoting, redirection, pipelines, globbing, substitution, retry, and substitution limits when relevant. Executable name alone is insufficient. Redact secrets; structure cannot establish shell semantics or actual effects. |
| `command_definition.expected_results` | Required non-empty array of observable intended outcomes, not execution evidence or status assertions. Redact sensitive output. |
| `command_definition.verification_procedure` | Required non-empty plain-language checks identifying target, scope, evidence, and Control Desk handoff where applicable. It does not execute checks or claim results. |
| `command_definition.failure_conditions` | Required non-empty stop/escalation/reassessment conditions, including unknown targets and material compatibility, approval, permission, or side-effect failures when relevant. Actual failures require evidence. |

### 4.2 Classification

Classification is assessed against exact syntax, arguments, shell, working
directory, environment, permissions, authentication, target, and recovery
boundary. Dimensions are independent and may have multiple applicable values.

| Field | Contract |
|---|---|
| `classification.operation` | Required non-empty array of only `OBSERVE`, `INSPECT`, `ANALYZE`, `PREPARE`, `MODIFY`, `EXECUTE`. `PREPARE` is not automatically safe. |
| `classification.effects` | Required non-empty array of only `FILESYSTEM_READ`, `FILESYSTEM_WRITE`, `NETWORK_ACCESS`, `PRIVILEGED_ACCESS`, `PROCESS_CREATION`, `EXTERNAL_STATE_CHANGE`; include all applicable effects. |
| `classification.risk_flags` | Required array of only `DESTRUCTIVE`, `SECRET_EXPOSURE`, `DATA_LOSS`, `EXTERNAL_PUBLICATION`, `SERVICE_DISRUPTION`; empty requires contextual justification. `DATA_LOSS` needs target, consequence, and recovery analysis; database writes alone do not establish it. |
| `classification.approval_requirement` | Required one of `NONE`, `HUMAN_APPROVAL_REQUIRED`, `EXPLICIT_HIGH_RISK_APPROVAL`. Minimum-control classification for exact scope; never an approval. |
| `classification.reversibility` | Required one of `REVERSIBLE`, `RECOVERABLE`, `PARTIALLY_REVERSIBLE`, `IRREVERSIBLE`, based on actual target and recovery boundary. |
| `classification.secret_handling` | Required one of `NONE`, `INDIRECT_ONLY`, `SENSITIVE_OUTPUT_POSSIBLE`, `PROHIBITED`; cover sensitive input, output, environment, and target handling without reproducing secrets. |
| `classification.service_impact` | Required one of `NONE`, `LOCAL_ONLY`, `DEGRADED`, `OUTAGE_POSSIBLE`; compatibility or verification does not remove service risk. |

These are the exact approved Stage 1 vocabularies. No new enum is created.

### 4.3 Execution context and target constraints

| Field | Contract |
|---|---|
| `execution_context.prerequisites` | Required non-empty collection identifying tools/versions, files/state, permissions, authentication, and human checks. Unknown critical prerequisites remain unknown and block selection. No credentials; structure cannot establish the live environment. |
| `execution_context.working_directory` | Required object with conceptual `required`, `rule`, and optional typed path constraint. Must distinguish repository, subdirectory, and external context. Project-specific paths are not generalized. Redact sensitive absolute paths. |
| `target_constraints.target_scope` | Required object with conceptual `kind`, `target`, `constraints`, `exclusions`, `permissions`, `authentication_boundary`, and `recovery_boundary`. Exact/bounded target identity is required for writes, destructive, external-state, privileged, service-impacting, high-risk, and potentially irreversible operations. It never approves a live target. |

### 4.4 Environment compatibility

This is a per-environment map, not a universal support claim. Each entry may
include `profile_ref`, `status`, `shell`, `executable`, `version_constraints`,
`conditions`, and `references`.

| Field | Contract |
|---|---|
| `environment_compatibility.<environment>.status` | Required per entry; only `SUPPORTED`, `CONDITIONAL`, `UNSUPPORTED`, or `NOT_ASSESSED`. `SUPPORTED` needs environment-scoped support; `CONDITIONAL` names material conditions; `UNSUPPORTED` explains why; `NOT_ASSESSED` means insufficient evidence. Metadata only, not authorization or verification. |
| `environment_compatibility.<environment>.references` | Required per entry, empty only for `NOT_ASSESSED`. Must support the exact environment claim. One platform, shell, runtime, tool version, or project does not establish another. |

### 4.5 Verification projection

These fields project authoritative support and never create verification.

| Field | Contract |
|---|---|
| `verification_projection.verification_status` | Required one of `VERIFIED`, `PROJECT-DOCUMENTED`, `HISTORICAL`, `PROPOSED`, `DEPRECATED`, `BLOCKED`. `VERIFIED` requires resolving authoritative Control Desk verification plus linked supporting evidence for exact claim, scope, target, and context. Missing, stale, invalidated, conflicting, or mismatched support cannot establish it. `DEPRECATED` is an OKCI metadata projection that the command is not recommended for new selection; it is not itself lifecycle, unverified, or invalid. |
| `verification_projection.last_verified` | Required nullable ISO 8601 timestamp with timezone. Non-null only from authoritative verification; never registry edit time. Schema cannot prove freshness or invalidation. |
| `verification_projection.review_due` | Required nullable ISO 8601 date. Non-null only when an authoritative Control Desk policy/decision supplies it; no local review window or expiration is invented. Unknown policy remains null with explanation. |
| `verification_projection.stale_reason` | Required nullable plain-language reason; required for `HISTORICAL`, `BLOCKED`, or stale/invalidated/mismatched support. It describes authority limits and cannot create a new state. |

### 4.6 References

`references` is a required claim-support index, not copied evidence. It has
five distinct typed collections: `control_desk_records`, `repository_files`,
`project_documentation`, `external_documentation`, and `okci_records`.

| Field | Contract |
|---|---|
| `references.control_desk_records` | Required array, conditionally non-empty. Each object normatively has `type`, stable `record_id`, optional `section_or_claim`, and `support_scope`. Type identifies approval, evidence, verification, risk, decision, milestone, or another established class; IDs may be `A-...`, `E-...`, `V-...`, `R-...`, `D-...`, `M-...`. `VERIFIED` requires resolving verification and linked evidence. No fictional IDs; a record supports only its own scope and never implies authorization. |
| `references.repository_files` | Required array, possibly empty. Each object has `type: repository_file`, repository-relative `path`, optional `section_or_claim`, and bounded `support_scope`. Supports source meaning/constraints/context, not execution, current verification, freshness, authorization, or live compatibility. |
| `references.project_documentation` | Required array, possibly empty. Each object has `type: project_documentation`, project-scoped `path_or_locator`, optional `section_or_claim`, and bounded `support_scope`. Cannot generalize to another project or establish live execution, verification, freshness, or authorization. |
| `references.external_documentation` | Required array, possibly empty. Each object has `type: external_documentation`, identified `locator`, optional `title_or_publisher` and `section_or_claim`, and bounded `support_scope`. Supports only identified informational claims. URI syntax, resolution, trust, and version pinning are deferred; it cannot establish approval, evidence, verification, freshness, or authorization. |
| `references.okci_records` | Required array, possibly empty. Each object has `type: okci_record`, record identity, optional `section_or_claim`, and bounded contextual/historical `support_scope`. No transitive Control Desk authority. |

### 4.7 Provenance

`provenance` records the origin and lineage of the knowledge used to create
the command record. It does not replace `references`, copied evidence, or
authoritative Control Desk history.

| Field | Contract |
|---|---|
| `provenance.source` | Required non-empty collection containing at least one source-origin record. Each record has required `origin_type`, `description`, and `scope`, plus optional or nullable `locator` and `revision`. `origin_type` is a required descriptive classification, not a new enum; illustrative values include repository inspection, official documentation, project documentation, user-provided information, observed execution, historical research, and analytical synthesis. The collection describes where knowledge came from and which claims it contributed; it does not establish verification, approval, freshness, compatibility, safety, or execution success. |
| `provenance.source[].origin_type` | Required non-empty descriptive classification of the source origin. It is extensible text, not an approved enumeration. |
| `provenance.source[].description` | Required non-empty explanation of what information was obtained from this origin. |
| `provenance.source[].scope` | Required non-empty explanation of which knowledge or claims this origin contributed. |
| `provenance.source[].locator` | Optional or nullable location identifying the source. Locator syntax and resolution remain deferred where not otherwise specified. |
| `provenance.source[].revision` | Optional or nullable version, commit, date, or other source-revision identifier where available. It does not establish freshness or validity. |
| `provenance.recorded_by` | Required non-secret attribution for the person, process, or role that recorded the provenance. It is not approval authority or ownership of the source. |
| `provenance.recorded_at` | Required timestamp with timezone for recording this provenance metadata. It is record metadata only and cannot establish freshness or verification. |
| `provenance.review_history` | Required non-secret record-lineage collection with revision reasons and bounded references where applicable; it may contain zero entries for a newly created record. It does not duplicate authoritative Control Desk history. |

`provenance.source` is distinct from `references`: source-origin records
describe origin and lineage, while `references` identify sources supporting
bounded claims. `verification_projection` is a separate projection of
authoritative verification and evidence. An observed-execution source may
describe that execution as an origin of knowledge, but it does not
automatically imply `VERIFIED`; that status remains subject to authoritative
Control Desk verification and supporting evidence for the exact claim, target,
scope, and context. No source-origin record duplicates references, evidence,
or authoritative Control Desk history. Replacement lineage remains solely in
`lifecycle.replacement_command_id`.

### 4.8 Lifecycle and limitations

`lifecycle` is independent of verification status and Control Desk lifecycle.
Catalog deprecation controls recommendation and lineage; a command may retain
historically valid verification while deprecated, and historical verification
does not make it current.

| Field | Contract |
|---|---|
| `lifecycle.deprecated_at` | Nullable date/time; required when catalog-deprecated. Catalog metadata, not Control Desk invalidation or freshness. |
| `lifecycle.deprecation_reason` | Nullable non-empty string; required when deprecated and bounded to the catalog decision. |
| `lifecycle.replacement_command_id` | Nullable stable ID; required when a replacement exists. Null requires explanation; old identity is retained. |
| `lifecycle.migration_limitations` | Nullable collection required when needed for deprecation migration. It cannot authorize automatic substitution or target expansion. |
| `limitations` | Required non-empty array of bounded unknowns, exclusions, unsupported targets, redaction limits, stale/conflicting support, and non-guarantees. It cannot waive stop conditions or contain secrets. |

## 5. Exact targets, operational semantics, and stop boundaries

Target identity, scope, exclusions, permission/authentication boundary, and
recovery boundary must be precise enough for the operation. Unknown,
ambiguous, unresolved, or out-of-boundary targets stop selection. Backup,
confirmation, and dry-run controls do not establish eligibility or
authorization. Target expansion, substitution, command drift, changed scope,
fallback, retry, or recovery substitution requires reassessment and applicable
new approval.

The contract may describe syntax, shell interpretation, prerequisites,
expected results, failure conditions, and safe verification methods, but never
executes commands, implies execution, generates evidence, or defines automatic
fallback/retry. Classifications are context-dependent; an executable name
alone cannot establish safety.

An AI may use a record to compare meaning and constraints, but must stop and
surface unknown or conflicting target, side-effect, permission, recovery,
context, compatibility, authority, or evidence facts. It must not infer
authorization from status, references, timestamps, schema validity,
compatibility, or approval classification. This is a selection boundary, not a
separate execution protocol; human authorization remains with STS Control Desk.

## 6. Verification, evidence, and portability

`VERIFIED` requires an authoritative Control Desk verification and linked
supporting evidence resolving to the exact claim, target, scope, and context.
No fictional identifiers, evidence, or claims are allowed. Repository/project
documentation, external documentation, and other OKCI records have only their
bounded support; none can substitute for Control Desk authority. This contract
defines no local expiration rule.

Compatibility is independently assessed per environment, shell, executable,
version, permissions, platform, and project configuration. `NOT_ASSESSED`
means insufficient evidence and is not `SUPPORTED`. Linux, macOS, Windows,
Android/Termux, shells, runtimes, and tool versions are not interchangeable by
assumption. Portability means the semantics travel; it does not claim universal
compatibility.

## 7. Validation boundaries and deferred work

A future schema may check structure, types, requiredness, and enum membership;
it cannot establish shell behavior, target identity, permissions,
recoverability, secret absence, environment match, reference resolution,
evidence scope, freshness, invalidation, semantic correctness, human review,
or authorization. Schema validity is not safety validation.

Deferred work includes JSON Schema dialect/encoding, `$defs` and property
policy, validator/version, fixtures/tests, dependencies/tool integration,
registry behavior, automatic freshness/invalidation, project profiles, and
machine-readable external-documentation locator policy. No deferred work may
introduce a new enum, local freshness rule, automatic target selection,
transitive authority, or execution behavior without separate approval.

Changing the eleven groups, approved vocabularies, authority boundaries,
verification conditions, reference domains, exact-target rules,
lifecycle/verification separation, or deferred scope requires human review and
applicable approval.
