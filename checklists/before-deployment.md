# Before-Deployment Checklist

## Purpose

Use this checklist before changing a staging or production environment.

Deployment approval applies only to the exact version, environment, scope, limits, and time window recorded here.

## Identification

- Project:
- Milestone ID:
- Deployment record ID:
- Version or commit:
- Target environment:
- Deployment owner:
- Approver:
- Planned date and time:
- Status: Proposed

## 1. Deployment Mission

### Intended outcome

-

### User or operational impact

-

### Exact target

- Service:
- Environment:
- Region or location:
- Version:
- Database:
- External integrations:

## 2. Scope and Approval

- [ ] Deployment scope is documented.
- [ ] Out-of-scope actions are documented.
- [ ] The exact target environment is confirmed.
- [ ] The exact commit or version is confirmed.
- [ ] Required human approval is recorded.
- [ ] Approval remains valid and has not expired.
- [ ] Material changes received renewed approval.
- [ ] Deployment does not include unapproved automation.

### Approval record

-

## 3. Source and Release State

- [ ] Working tree is clean.
- [ ] Intended commit exists on the remote.
- [ ] Branch protection requirements are satisfied.
- [ ] Required reviews are complete.
- [ ] CI checks passed.
- [ ] Release notes match the actual change.
- [ ] Tag or version points to the intended commit.
- [ ] No unrelated commits are included.

### Source evidence

-

## 4. Build and Dependency Verification

- [ ] Production build succeeds.
- [ ] Dependency versions are reviewed.
- [ ] Lock files are current where required.
- [ ] No unexpected dependency was introduced.
- [ ] Dependency vulnerability checks were reviewed.
- [ ] Runtime versions match the target environment.
- [ ] Build artifacts come from the approved source state.

## 5. Configuration and Secrets

- [ ] Environment configuration is documented.
- [ ] Required variables are present.
- [ ] Secrets are stored outside the repository.
- [ ] No secret is present in logs or command history.
- [ ] Production values are not copied into documentation.
- [ ] Secret rotation requirements are understood.
- [ ] Least-privilege credentials are used.
- [ ] Debug mode is disabled where required.
- [ ] Live-execution settings match the approval record.

## 6. Data and Migration Safety

- [ ] Database backup or snapshot is complete.
- [ ] Backup restoration has been verified where required.
- [ ] Migration order is documented.
- [ ] Migration was tested on representative data.
- [ ] Existing records are preserved.
- [ ] Duplicate and conflict behaviour is controlled.
- [ ] Downgrade or rollback limitations are documented.
- [ ] Offline-created data is protected where required.
- [ ] Synchronisation behaviour is verified where required.

### Backup or recovery reference

-

## 7. Security Review

- [ ] Authentication is enabled and tested.
- [ ] Authorisation rules are tested.
- [ ] Sensitive endpoints reject unauthorised access.
- [ ] Transport security is configured.
- [ ] CORS and trusted-host settings are appropriate.
- [ ] Error responses avoid sensitive disclosure.
- [ ] Audit logging is active where required.
- [ ] Rate limits or abuse controls are active where required.
- [ ] Private keys and financial controls remain isolated.
- [ ] No safety boundary is removed by configuration.

## 8. Operational Readiness

- [ ] Health checks are available.
- [ ] Logs are available and protected.
- [ ] Monitoring is active.
- [ ] Alert recipients are confirmed.
- [ ] Storage and resource capacity are sufficient.
- [ ] Required external services are reachable.
- [ ] Background workers are understood.
- [ ] Start, stop, and restart procedures are documented.
- [ ] Support or incident owner is available.

## 9. Deployment Plan

### Steps

1.
2.
3.

### Limits

- Maximum attempts:
- Automatic retry allowed: No
- Deployment window:
- Stop conditions:
- Required observer:

### Expected duration

-

## 10. Rollback and Recovery

- [ ] Previous known-good version is identified.
- [ ] Rollback command or procedure is documented.
- [ ] Data recovery procedure is documented.
- [ ] Rollback owner is present.
- [ ] Rollback triggers are defined.
- [ ] Irreversible effects are documented.
- [ ] Recovery verification steps are ready.

### Rollback target

-

### Rollback triggers

-

## 11. Post-Deployment Verification

- [ ] Service starts successfully.
- [ ] Health check passes.
- [ ] Critical user workflow passes.
- [ ] Authentication and roles behave correctly.
- [ ] Database state is valid.
- [ ] Logs contain no unexpected error.
- [ ] Monitoring receives current data.
- [ ] External integrations behave as approved.
- [ ] Offline operation works where required.
- [ ] No unapproved live action occurred.

### Verification record

-

## 12. Communication and Audit

- [ ] Deployment decision is recorded.
- [ ] Relevant stakeholders are informed.
- [ ] Release notes are available.
- [ ] Deployment start and finish times are recorded.
- [ ] Unexpected effects are recorded.
- [ ] Approval and verification records are linked.
- [ ] Incident process is ready if required.

## Deployment Decision

Select one:

- [ ] Approved to deploy
- [ ] Approved with conditions
- [ ] Blocked
- [ ] Deferred
- [ ] Cancelled
- [ ] Recovery required

### Conditions or blocker

-

### Final approval

- Approved by:
- Date and time:
- Approval statement:

### Result

- Deployment status: Not started
- Actual version deployed:
- Completion time:
- Verification result:
- Rollback required: Yes / No
- Incident reference:

> Deployment is an operational change, not merely a Git action.
