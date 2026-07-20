# Verification Record

## Purpose

Use this template to record evidence that a milestone, change, recovery action, or deployment behaves as intended.

Verification must test defined claims. It should not rely only on the absence of visible errors.

## Identification

- Project:
- Milestone ID:
- Verification record ID:
- Change or action being verified:
- Commit or version:
- Environment:
- Verified by:
- Date:
- Status: In Progress

## 1. Verification Objective

### Claim

State the behaviour or outcome that must be proven.

### Why verification is required

Explain the risk or acceptance criterion addressed by this record.

## 2. Scope

### In scope

-

### Out of scope

-

### Components under test

-

## 3. Starting State

- Repository:
- Branch:
- Commit:
- Working tree:
- Runtime state:
- Database or storage state:
- External dependencies:
- Safety controls:

### Evidence of starting state

-

## 4. Acceptance Criteria

| ID | Criterion | Required evidence | Status |
|---|---|---|---|
| AC-01 |  |  | Pending |
| AC-02 |  |  | Pending |
| AC-03 |  |  | Pending |

## 5. Verification Plan

### Checks to perform

1.
2.
3.

### Test data

Describe the fixtures, records, scenarios, or inputs used.

### Expected results

-

### Failure conditions

-

## 6. Verification Environment

- Operating system:
- Runtime and version:
- Dependency versions:
- Database:
- Network state:
- Offline or online mode:
- Configuration profile:
- Sensitive values redacted: Yes / No

### Environment differences

Record differences between this environment and the intended deployment environment.

## 7. Evidence

### Commands or actions

-

### Relevant output

Summarise the output without including secrets, tokens, personal data, or private keys.

### Files, logs, or records inspected

-

## 8. Results

| Check | Expected | Actual | Result |
|---|---|---|---|
|  |  |  | Pass / Fail |
|  |  |  | Pass / Fail |

### Failures observed

-

### Corrections made

-

### Retest evidence

-

## 9. Security and Control Checks

- [ ] No secrets are present in files, output, or Git history.
- [ ] Unauthorised behaviour is rejected.
- [ ] Error paths fail safely.
- [ ] Audit or history records are created where required.
- [ ] Established approval boundaries remain active.
- [ ] Live execution remains disabled unless explicitly approved.
- [ ] Automatic retry remains disabled unless explicitly approved.
- [ ] Recovery controls remain available.

### Additional security evidence

-

## 10. Data and Recovery Checks

- [ ] Existing data remains intact.
- [ ] New records have the expected structure.
- [ ] Duplicate or conflicting operations are controlled.
- [ ] Backup or restore procedure is available where required.
- [ ] Offline behaviour is verified where required.
- [ ] Synchronisation behaviour is verified where required.

### Additional data evidence

-

## 11. Diff and Repository Checks

- [ ] Final diff contains only intended changes.
- [ ] Generated files are excluded.
- [ ] Local databases, logs, PID files, and environment files are excluded.
- [ ] Documentation matches implemented behaviour.
- [ ] `git diff --check` passes.
- [ ] Working tree state is understood.

### Repository evidence

-

## 12. Limitations

### Not tested

-

### Reason

-

### Residual risk

-

A limitation must not be silently treated as a passing result.

## 13. Independent Verification

- Required: Yes / No
- Reviewer:
- Review date:
- Evidence reviewed:
- Result:
- Concerns:

## 14. Acceptance-Criteria Assessment

| ID | Final status | Evidence reference |
|---|---|---|
| AC-01 |  |  |
| AC-02 |  |  |
| AC-03 |  |  |

## Final Decision

Select one:

- [ ] Verified
- [ ] Verified with limitations
- [ ] Failed verification
- [ ] Blocked
- [ ] Requires recovery

### Decision summary

-

### Approved for Git checkpoint

- Decision: Yes / No
- Decided by:
- Date:

### Follow-up required

-

> Evidence determines completion, not confidence alone.
