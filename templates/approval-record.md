# Human Approval Record

## Purpose

Use this template to record a human decision before an action that changes scope, data, security, infrastructure, finances, external systems, or production state.

Approval applies only to the exact action and boundaries recorded here.

## Identification

- Project:
- Milestone ID:
- Approval record ID:
- Requested by:
- Decision owner:
- Date requested:
- Decision status: Pending

## 1. Proposed Action

### Action summary

Describe exactly what is proposed.

### Reason

Explain why the action is necessary.

### Expected outcome

Describe the observable result expected after execution.

## 2. Exact Target

- Repository:
- Branch:
- Environment:
- Service or component:
- File, record, account, wallet, or resource:
- External system:
- Geographic or organisational scope:

Do not use unresolved variables, broad wildcards, or ambiguous target descriptions.

## 3. Scope

### In scope

-

### Out of scope

-

### Explicitly prohibited

-

## 4. Risk Classification

Select one:

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical

### Risk explanation

Explain why this classification applies.

### Identified risks

| Risk | Likelihood | Impact | Control |
|---|---|---|---|
|  |  |  |  |

## 5. Preconditions

Execution is blocked until:

- [ ] Current state has been observed.
- [ ] Exact target has been confirmed.
- [ ] Acceptance criteria are defined.
- [ ] Required tests or dry runs have passed.
- [ ] Recovery procedure is available.
- [ ] Secrets and sensitive data are protected.
- [ ] Required approver has reviewed this record.

### Additional preconditions

-

## 6. Proposed Execution

### Steps

1.
2.
3.

### Execution limits

- Maximum number of attempts:
- Time window:
- Financial or resource cap:
- Automatic retry allowed: No
- Automatic expansion allowed: No
- Stop conditions:

## 7. Recovery Plan

### Reversible action

Describe how the change can be reversed.

### Recovery checkpoint

- Backup, snapshot, commit, or restore point:
- Recovery owner:
- Recovery verification:

### Irreversible effects

List any effect that cannot be reversed.

## 8. Evidence Presented for Approval

-

## 9. Decision

Select one:

- [ ] Approved
- [ ] Approved with conditions
- [ ] Rejected
- [ ] Deferred
- [ ] Revoked

### Decision statement

Record the approver’s exact decision.

### Conditions

-

### Approved by

- Name:
- Role:
- Date and time:
- Approval channel:

## 10. Approval Boundary

This approval authorises only the action, target, scope, limits, and time window recorded above.

It does not authorise:

- Material scope expansion
- Additional targets
- Automatic retries
- Follow-up actions
- Future milestones
- Removal of established controls

A material change requires a new or amended approval record.

## 11. Expiry and Revocation

- Approval expires:
- Conditions that invalidate approval:
- Revocation method:
- Revoked by:
- Revocation date and time:
- Revocation reason:

## 12. Post-Execution Record

- Execution status: Not started
- Executed by:
- Start time:
- Completion time:
- Attempts used:
- Actual outcome:
- Unexpected effects:
- Recovery required: Yes / No
- Verification record:
- Audit reference:

## Completion Decision

- Approval conditions satisfied: Yes / No
- Action remained within scope: Yes / No
- Independent verification completed: Yes / No
- Record closed by:
- Closure date:

> Approval is a limited control boundary, not unlimited permission.
