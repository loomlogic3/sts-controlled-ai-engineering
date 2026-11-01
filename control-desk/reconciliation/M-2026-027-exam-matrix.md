# M-2026-027 Evidence Matrix: Exam Control System

Source packet: `../reviews/STS-EXAM-001.md`  
Evidence record: [E-2026-023](../evidence/E-2026-023.md)

| Candidate | Proposed classification | Evidence-backed rationale | Required next evidence |
|---|---|---|---|
| M-EXAM-001 backend/exam foundation | Provisional | Core implementation and automated boundary tests exist; no formal acceptance record. | Owner acceptance, full dependency-backed test run, deployment target decision. |
| M-EXAM-002 result release/admin controls | Provisional/high-risk | Tests cover authorization, state/link/score checks, audit actor, and idempotence; approval-chain and amendment workflows are documented as absent. | Named release approver, policy sign-off, executed release regression results. |
| M-EXAM-003 student ownership/result privacy | Provisional/high-risk | Tests cover ownership and grading confidentiality paths; no complete denial matrix or environment-backed run is available. | Cross-student denial matrix and passing execution evidence. |
| M-EXAM-004 security/API/database/deployment docs | Incomplete | Security and deployment documents exist, but deployment is explicitly development-only and production controls are planned. | Formal security review, production architecture, backup/recovery and deployment evidence. |
| M-EXAM-005 sensitive question/grading integrity | Provisional/high-risk | Leakage and sensitive-collection tests exist; independent integrity review is not evidenced. | Independent review and approval of question/grading confidentiality controls. |
| M-EXAM-006 exam/question/user hardening | Provisional | Role and validation tests exist; final approved role matrix is not evidenced. | Final role matrix, approval, and negative-path execution evidence. |
| M-EXAM-007 JWT/secret hardening | Incomplete/high-risk | Fail-closed key validation and rotation behavior are documented/tested in source, but no rehearsal or deployment evidence is present. | Rotation rehearsal, restart/token invalidation evidence, secret ownership. |
| M-EXAM-008 migration foundation/session invariants | Provisional/high-risk | Migration and uniqueness tests exist; deployment guide says startup does not migrate and no live-target rehearsal is evidenced. | Disposable upgrade/downgrade result plus approved target migration rehearsal. |

## Review conclusion

No candidate is confirmed complete. The repository supports a controlled continuation focused on evidence closure, beginning with the high-risk ownership/result-release and secret/migration controls. The dependency gap prevents an execution-based test verdict in the current environment.

## Next controlled action

Request the project owner’s evidence for the result-release approval, cross-student denial matrix, independent integrity review, secret rotation rehearsal, and migration rehearsal. Do not change project records or run against production data.
