# Repository Context for AI Assistants

Read this file at the start of work in this repository, then inspect the current Git state and relevant files. This context is a snapshot, not a substitute for observing the repository.

## Project

STS Controlled AI Engineering is a platform-independent method and toolkit for planning, building, verifying, and shipping software with AI while keeping human judgment and approval in control. Its governing principle is: **Before you add power, add more control.**

This repository currently contains the canonical method (`METHOD.md`), reusable approval, verification, status, milestone, and risk templates, operational checklists, and a historical worked example. It is documentation-focused; there is no application source or test suite in the current tree.

## How to work here

- Treat `METHOD.md` as the canonical source for the lifecycle and control requirements.
- Follow the 13-stage lifecycle: Mission; Current State—Observe; Problem—Understand; Goal and Scope; Out of Scope; Risks; Acceptance Criteria; Human Approval; Execute in Small Steps; Verify with Evidence; Git Checkpoint; Lessons Learned; Next Milestone.
- Keep documentation changes scoped, reviewable, and consistent with the templates and checklists.
- Distinguish confirmed facts, inferences, unknowns, and plans. Do not present planned capability as implemented.
- Sensitive, external, production, destructive, financial, or irreversible actions require the explicit approvals and controls described in `METHOD.md` and the relevant checklist. Repository presence does not imply authorization for those actions.
- Do not create a commit, push, tag, publish, or deploy unless the user asks for that action.
- For changes, inspect the final diff and use proportionate verification. There is no code test suite in the current repository.

## Repository snapshot observed 2026-10-06

- Branch: `main`
- HEAD: `07a88ee` (`Add reusable engineering control toolkit`)
- Working tree was clean when this context was recorded.
- The README describes v0.1.0 as the method introduction and v0.2.0 as the reusable control toolkit; it says v0.2.0 is complete after review, verification, checkpoint, publication, and tagging. Re-check Git and release state before making claims about completion.
- `rg` was unavailable in the environment used for this snapshot; use available alternatives such as `find` if needed.

## Key files

- `README.md` — project overview, contents, and stated release status.
- `METHOD.md` — canonical process, risk levels, approval boundaries, verification, and completion standard.
- `templates/` — milestone, approval, verification, project status, and risk records.
- `checklists/` — before-commit, before-deployment, and high-risk-action controls.
- `examples/sts-ai-lab/per-agent-tool-permissions.md` — historical example of a completed engineering milestone.
