# Before-Commit Checklist

## Purpose

Use this checklist before creating a Git checkpoint.

A commit should represent one coherent, verified, recoverable change. It should not be used to hide incomplete verification or unrelated work.

## Identification

- Project:
- Milestone ID:
- Branch:
- Proposed commit message:
- Reviewed by:
- Date:

## 1. Current State

- [ ] I am in the intended repository.
- [ ] I am on the intended branch.
- [ ] I inspected `git status`.
- [ ] I understand every modified, deleted, and untracked file.
- [ ] The current milestone has human approval where required.
- [ ] No unrelated user changes will be overwritten or included.

## 2. Scope

- [ ] The change matches the approved mission.
- [ ] Every changed file is within scope.
- [ ] Out-of-scope work has not been silently included.
- [ ] Material scope changes received renewed approval.
- [ ] The commit represents one coherent outcome.

### Intended files

-

### Explicitly excluded files

-

## 3. Implementation Review

- [ ] The implementation follows existing architecture and conventions.
- [ ] The change is no larger than necessary.
- [ ] Duplicate or obsolete logic was not introduced.
- [ ] Error paths fail safely.
- [ ] Logging is useful without exposing sensitive data.
- [ ] Comments explain decisions rather than obvious syntax.
- [ ] Temporary debugging code has been removed.

## 4. Verification

- [ ] Acceptance criteria are defined.
- [ ] Targeted checks passed.
- [ ] Broader tests passed where required.
- [ ] Failure paths were tested where required.
- [ ] Manual smoke testing was completed where required.
- [ ] Verification results were recorded.
- [ ] Known limitations are documented.
- [ ] Failed checks were corrected and rerun.

### Verification evidence

-

## 5. Security and Secrets

- [ ] No passwords are included.
- [ ] No API tokens are included.
- [ ] No private keys or seed phrases are included.
- [ ] No production credentials are included.
- [ ] No sensitive personal data is included.
- [ ] Environment files are excluded.
- [ ] Logs and command output are free of secrets.
- [ ] Authentication and authorisation boundaries remain intact.
- [ ] Live execution remains disabled unless explicitly approved.

## 6. Data and Generated Files

- [ ] Local databases are excluded unless intentionally versioned.
- [ ] Database journals and backups are excluded.
- [ ] Logs are excluded.
- [ ] PID and runtime-state files are excluded.
- [ ] Build output and caches are excluded.
- [ ] Temporary files are excluded.
- [ ] Test fixtures contain no real sensitive data.
- [ ] Required migrations preserve existing data.
- [ ] Recovery or rollback is available where required.

## 7. Documentation

- [ ] Documentation matches actual behaviour.
- [ ] Setup instructions remain accurate.
- [ ] New configuration is documented safely.
- [ ] Security boundaries are documented.
- [ ] User-visible changes are explained.
- [ ] Roadmap or status records are updated where required.

## 8. Git Diff Review

- [ ] `git diff --check` passes.
- [ ] I reviewed the unstaged diff.
- [ ] I staged only the intended files.
- [ ] I reviewed the staged diff.
- [ ] The staged diff contains no unexpected deletion.
- [ ] The staged diff contains no unrelated formatting rewrite.
- [ ] The staged file list matches this checklist.
- [ ] The commit message describes the outcome clearly.

### Staged files

-

### Final diff concerns

-

## 9. Approval Boundary

- [ ] The commit itself is authorised.
- [ ] The commit does not imply permission to push.
- [ ] The commit does not imply permission to deploy.
- [ ] External publication has separate approval where required.
- [ ] Tagging or release creation has separate approval where required.

## 10. Final Decision

Select one:

- [ ] Ready to commit
- [ ] Blocked by failed verification
- [ ] Blocked by scope concern
- [ ] Blocked by secret or data concern
- [ ] Requires renewed approval

### Decision evidence

-

### Commit result

- Commit created: Yes / No
- Commit hash:
- Working tree after commit:
- Next authorised action:

> A clean commit is a recovery boundary and an audit record.
