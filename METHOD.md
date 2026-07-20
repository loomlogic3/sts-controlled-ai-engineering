# STS Controlled AI Engineering Method

## 1. Purpose

This document defines the canonical method for planning, building, testing, and shipping software with AI while preserving human control.

The method is platform-independent. It can be used with terminal tools, coding agents, local models, cloud models, or traditional development environments.

AI may assist throughout the lifecycle, but it does not independently decide scope, approve sensitive actions, or declare work complete.

## 2. Canonical Lifecycle

Every controlled milestone follows these stages:

1. Mission
2. Current State — Observe
3. Problem — Understand
4. Goal and Scope
5. Out of Scope
6. Risks
7. Acceptance Criteria
8. Human Approval
9. Execute in Small Steps
10. Verify with Evidence
11. Git Checkpoint
12. Lessons Learned
13. Next Milestone

A stage should not be skipped merely because the implementation appears simple.

## 3. Mission

State the outcome the milestone is intended to produce.

A good mission is:

- Specific
- Limited
- Verifiable
- Connected to a real project need

The mission should describe the desired outcome, not a list of premature implementation decisions.

### Required record

- Milestone identifier
- Mission statement
- Reason the milestone matters

## 4. Current State — Observe

Inspect the system before changing it.

Observation may include:

- Repository status
- Current branch and recent commits
- Relevant files and architecture
- Existing tests
- Runtime behaviour
- Logs and error messages
- Documentation
- Security boundaries
- Deployment state

Do not assume that remembered project state still matches the repository.

### Required evidence

Record the commands, files, outputs, or observations used to establish the current state.

## 5. Problem — Understand

Explain the gap between the current state and the desired state.

Understanding should separate:

- Confirmed facts
- Reasonable inferences
- Unknowns requiring investigation
- Symptoms
- Root causes

Do not implement a fix before the problem is sufficiently understood.

## 6. Goal and Scope

Define exactly what the milestone will change.

Scope should identify:

- Files or components in scope
- Behaviour being added or changed
- Required tests
- Required documentation
- Expected user-visible outcome

Prefer one file or a closely related group of changes at a time.

## 7. Out of Scope

Explicitly record what the milestone will not do.

This prevents:

- Accidental architecture expansion
- Unapproved automation
- Unnecessary refactoring
- Live execution by implication
- Unrelated cleanup
- Premature deployment

Out-of-scope work should be recorded as a possible future milestone instead of being silently added.

## 8. Risks

Identify technical, operational, security, data, and product risks before execution.

### Risk levels

#### Low

Examples:

- Documentation
- Comments
- Minor styling
- Non-functional naming improvements

Expected controls:

- Review
- Formatting or consistency checks

#### Medium

Examples:

- API endpoints
- Database models
- Authentication behaviour
- Business logic
- Dependency changes

Expected controls:

- Explicit acceptance criteria
- Automated tests
- Diff review
- Recovery plan where appropriate

#### High

Examples:

- Payments
- Examination integrity
- Production data
- Destructive migrations
- Sensitive user information
- External messaging or automated actions

Expected controls:

- Explicit human approval
- Strong test evidence
- Dry run or staging validation
- Audit record
- Rollback or recovery procedure

#### Critical

Examples:

- Private keys
- Live financial execution
- Treasury movement
- Irreversible deletion
- Production-wide deployment
- Security-boundary removal

Expected controls:

- Separate explicit approval
- Exact target confirmation
- Minimal authorised scope
- Preflight verification
- One controlled execution path
- Independent post-action verification
- Recovery or incident plan

## 9. Acceptance Criteria

Define the evidence required to consider the milestone complete.

Acceptance criteria should be:

- Observable
- Testable
- Unambiguous
- Connected to the mission

Examples:

- A specified test passes.
- An unauthorised request is rejected.
- A database migration preserves existing records.
- Offline-created records synchronize without duplication.
- Documentation matches implemented behaviour.
- Live execution remains disabled.

“Code was written” is not an acceptance criterion.

## 10. Human Approval

Present the plan before implementation when approval is required.

The approval record should include:

- Mission
- Scope
- Out of scope
- Risks
- Acceptance criteria
- Proposed execution steps

Approval applies only to the stated milestone. It does not grant unlimited permission for related future work.

If scope materially changes, stop and request renewed approval.

## 11. Execute in Small Steps

Implementation should proceed through small, reviewable changes.

For each step:

1. State the intended change.
2. Modify one file or closely related set of files.
3. Inspect the result.
4. Run proportionate verification.
5. Correct any failure before continuing.

Do not combine unrelated changes merely to reduce the number of commits.

Sensitive execution should default to:

- One target
- One approved action
- One attempt
- No automatic retry unless explicitly approved

## 12. Verify with Evidence

Verification must be proportionate to the risk.

Possible verification includes:

- Syntax or compilation checks
- Unit tests
- Integration tests
- Security tests
- Database inspection
- API smoke tests
- Browser or interface checks
- Offline behaviour tests
- Secret scanning
- `git diff --check`
- Manual review of the final diff

Record what was tested and the actual result.

Absence of an observed error is not sufficient evidence by itself.

## 13. Git Checkpoint

Create a Git checkpoint only after verification succeeds.

Before committing:

1. Review `git status`.
2. Review the final diff.
3. Confirm no secret or unrelated file is included.
4. Confirm acceptance criteria are satisfied.
5. Use a focused commit message.

After committing:

1. Record the commit hash.
2. Confirm the working tree is clean.
3. Push only when the remote action is intended and authorised.

A Git checkpoint is a controlled recovery boundary, not merely a record that files changed.

## 14. Lessons Learned

After completing a milestone, record:

- What worked
- What failed
- What was surprising
- What should be repeated
- What should change next time
- Any newly discovered risk or technical debt

Lessons should influence later milestones instead of becoming inactive documentation.

## 15. Next Milestone

Choose the next milestone only after the current one has been verified and checkpointed.

The next milestone should:

- Follow the project roadmap
- Address validated needs
- Remain small enough to control
- Preserve established safety boundaries
- Avoid adding power before the required controls exist

## 16. Completion Standard

A milestone is complete only when:

- Its acceptance criteria are satisfied.
- Required tests pass.
- The final diff has been reviewed.
- No unintended changes or secrets are present.
- Documentation reflects actual behaviour.
- A Git checkpoint has been created.
- Lessons have been recorded.
- The next milestone has been identified.

Until those conditions are met, the milestone remains in progress.

## 17. Governing Principle

> Before you add power, add more control.

The purpose of this method is not to slow engineering down. Its purpose is to make speed safe, evidence-based, recoverable, and worthy of trust.
