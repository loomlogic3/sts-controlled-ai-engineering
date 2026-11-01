# M-2026-027 Evidence Matrix: CivicOS

Source packet: `../reviews/STS-CIVICOS-001.md`  
Project repository: `../sts-civicos`  
Current state: `main`, no October commits, `.sts-project.json` and `control-desk/` untracked.

| Candidate | Proposed classification | Evidence-backed rationale | Required next evidence |
|---|---|---|---|
| M-CIVICOS-001 foundation/customer registry | Provisional | Committed foundation and registry evidence exist; acceptance and deployment evidence are absent. | Owner acceptance and data/deployment conditions. |
| M-CIVICOS-002 routes/collectors/collections | Provisional | Relationship and collection implementation exists; operational acceptance and data-integrity evidence are absent. | Route/collection integrity checks against approved fixture or data export. |
| M-CIVICOS-003 dashboard/assignments/UI | Provisional | UI and assignment artifacts exist; accepted dashboard behaviors and role boundaries are not recorded. | Acceptance scenarios and role review. |
| M-CIVICOS-004 payment history | Incomplete/high-risk | Payment history and ledger code exist; reconciliation against source data is unknown. | Reconciliation report with source, period, totals, and exception handling. |
| M-CIVICOS-005 invoice management | Incomplete/high-risk | Invoice model/API/UI and currency/date handling exist; financial approval and production-data controls are unknown. | Financial-control approval and invoice/payment reconciliation evidence. |
| M-CIVICOS-006 service plans | Provisional/high-risk | Service-plan model/API/page exist; billing-rule acceptance and existing-data migration are unknown. | Billing-rule test evidence and migration conditions. |
| M-CIVICOS-007 relationship integrity | Provisional/high-risk | Migration and relationship tests exist, including customer and collector-route constraints; production decision and approval are absent. | Independent orphan/constraint results and approved target decision. |
| M-CIVICOS-008 migrations/recovery | Incomplete/critical | Documentation defines preflight, immutable backup, rehearsal, and recovery controls; no evidence shows production execution or historical approval. | Disposable rehearsal, backup integrity/checksum, recovery result, and explicit production approval. |

## Review conclusion

No CivicOS candidate is confirmed complete. Financial and migration claims remain high-risk until reconciliation, backup/recovery, and target-environment evidence is supplied. No live data or production system was accessed.
