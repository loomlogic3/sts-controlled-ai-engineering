# High-Risk-Action Checklist

## Purpose

Use this checklist before any High or Critical action involving sensitive data, production systems, payments, examinations, private keys, live financial execution, destructive changes, or irreversible external effects.

This checklist does not itself grant approval.

## Identification

- Project:
- Milestone ID:
- Action record ID:
- Action owner:
- Independent verifier:
- Date:
- Risk level: High / Critical
- Status: Proposed

## 1. Action Classification

Select every applicable category:

- [ ] Production change
- [ ] Destructive file or data operation
- [ ] Database migration
- [ ] Sensitive personal data
- [ ] Authentication or authorisation boundary
- [ ] Payment or financial operation
- [ ] Private key or wallet operation
- [ ] Live trading execution
- [ ] Examination integrity
- [ ] External message or notification
- [ ] Infrastructure or network change
- [ ] Irreversible third-party action
- [ ] Other

### Classification explanation

-

## 2. Exact Action

### Proposed action

Describe one exact action.

### Expected result

-

### Prohibited expansion

-

The action must not silently expand into related targets, retries, follow-up operations, or automation.

## 3. Exact Target

- Repository:
- Branch or version:
- Environment:
- Service:
- Database:
- Record or dataset:
- User or organisation:
- Account or wallet:
- Network or chain:
- Transaction pair or asset:
- Amount or resource limit:
- External recipient:
- Geographic scope:

### Target confirmation

- [ ] Target values are explicit.
- [ ] No unresolved environment variable identifies the target.
- [ ] No broad wildcard identifies the target.
- [ ] No command substitution identifies the target.
- [ ] No unreviewed list or group identifies the target.
- [ ] Target ownership and authority are confirmed.

## 4. Human Authority

- [ ] The action is within the human approver’s authority.
- [ ] The affected system or data belongs to the approved scope.
- [ ] Legal, contractual, or institutional authority is confirmed where required.
- [ ] External recipients are resolved and verified where required.
- [ ] Separate Critical approval exists where required.

### Approval record

-

### Exact approval statement

-

### Approval expiry

-

## 5. Preconditions

- [ ] Current state has been observed.
- [ ] Risk register is current.
- [ ] Acceptance criteria are defined.
- [ ] Dry run, simulation, paper mode, or staging test passed where applicable.
- [ ] Required test suite passed.
- [ ] Backup or recovery checkpoint exists.
- [ ] Independent verifier is available.
- [ ] Audit recording is active.
- [ ] Stop and recovery procedures are ready.
- [ ] Approval remains valid.

## 6. Secrets and Sensitive Material

- [ ] No secret will be pasted into chat.
- [ ] No secret will be displayed in terminal output.
- [ ] No secret will be captured in screenshots.
- [ ] No private key will be committed to Git.
- [ ] No seed phrase will be stored digitally without an approved control.
- [ ] Sensitive values are loaded through an approved mechanism.
- [ ] Logs redact credentials and sensitive identifiers.
- [ ] Least-privilege credentials are used.
- [ ] Key or credential rotation is available if exposure occurs.

## 7. Execution Limits

- Maximum attempts:
- Maximum financial amount:
- Maximum number of affected records:
- Maximum execution duration:
- Approved time window:
- Automatic retry allowed: No
- Automatic scheduling allowed: No
- Automatic scope expansion allowed: No
- Parallel execution allowed: No
- Human observer required: Yes / No

### Stop conditions

-

If a stop condition occurs, execution must stop. Do not reinterpret failure as permission to continue.

## 8. Recovery and Reversibility

- [ ] Reversibility has been evaluated.
- [ ] Previous safe state is known.
- [ ] Backup, snapshot, or Git checkpoint is identified.
- [ ] Recovery steps are documented.
- [ ] Recovery owner is present.
- [ ] Recovery verification is defined.
- [ ] Irreversible effects are explicitly accepted.

### Recovery checkpoint

-

### Recovery procedure

-

### Irreversible effects

-

## 9. Domain-Specific Controls

### Payments and financial operations

- [ ] Amount and currency are explicit.
- [ ] Source and destination are verified.
- [ ] Duplicate payment is blocked.
- [ ] Reconciliation evidence will be recorded.
- [ ] Financial cap is enforced independently of the prompt.

### Wallets and live trading

- [ ] Wallet role is correct.
- [ ] Derived address matches the configured address.
- [ ] Chain or network is explicit.
- [ ] Token pair and amount are explicit.
- [ ] Quote and transaction preview are fresh.
- [ ] Signing boundary is approved.
- [ ] Broadcast is one-shot.
- [ ] Retry, DCA, bridge, perps, and treasury actions remain blocked unless separately approved.
- [ ] Transaction hash and receipt will be recorded.

### Examination systems

- [ ] Student question data is protected.
- [ ] Correct answers are not exposed before submission.
- [ ] Exam-session ownership is enforced.
- [ ] Offline records preserve integrity.
- [ ] Synchronisation conflict behaviour is controlled.
- [ ] Audit evidence is append-only where required.
- [ ] Recovery cannot silently change submitted answers.

### Destructive data operations

- [ ] Exact records or paths are enumerated.
- [ ] Broad recursive targets are prohibited.
- [ ] Backup restoration is verified.
- [ ] Referential impact is understood.
- [ ] Recoverable deletion is preferred.
- [ ] Record count is checked before execution.

## 10. Final Preflight

- [ ] Action matches the approval record exactly.
- [ ] Target matches the approval record exactly.
- [ ] Limits match the approval record exactly.
- [ ] Current state has not materially changed.
- [ ] Required evidence remains fresh.
- [ ] No blocker is active.
- [ ] Stop conditions are understood.
- [ ] Independent verifier is ready.

### Preflight result

- [ ] Ready
- [ ] Blocked
- [ ] Approval expired
- [ ] Scope changed
- [ ] Evidence stale
- [ ] Recovery unavailable

## 11. Execution Record

- Start time:
- Executed by:
- Attempt number:
- Command or controlled action:
- Actual target:
- Actual limits:
- Immediate result:
- Stop condition triggered: Yes / No
- Recovery initiated: Yes / No
- Completion time:

## 12. Independent Verification

- Verified by:
- Verification time:
- Expected outcome:
- Actual outcome:
- Evidence:
- Audit reference:
- Verification result: Pass / Fail / Inconclusive

## Final Decision

Select one:

- [ ] Action completed and verified
- [ ] Action completed with limitation
- [ ] Action blocked before execution
- [ ] Action stopped safely
- [ ] Recovery completed
- [ ] Incident escalation required

### Decision summary

-

### Follow-up actions

Any follow-up requires its own scope and approval where applicable.

-

> High-risk capability must remain narrower than its control boundary.
