# Repository Context for AI Assistants

Read this file at the start of work in this repository, then inspect the current Git state and relevant files. This context is a snapshot, not a substitute for observing the repository.

## Project

STS Controlled AI Engineering is a platform-independent method and toolkit for planning, building, verifying, and shipping software with AI while keeping human judgment and approval in control. Its governing principle is: **Before you add power, add more control.**

This repository contains the canonical method (`METHOD.md`), reusable control
templates and checklists, historical assessment records, the file-based Control
Desk and its read-only inspection/projection tools, and the OKCI command-record
foundation. It remains primarily documentation and control tooling; there is no
product application source or conventional application test suite in the tree.

## How to work here

- Treat `METHOD.md` as the canonical source for the lifecycle and control requirements.
- Follow the 13-stage lifecycle: Mission; Current State—Observe; Problem—Understand; Goal and Scope; Out of Scope; Risks; Acceptance Criteria; Human Approval; Execute in Small Steps; Verify with Evidence; Git Checkpoint; Lessons Learned; Next Milestone.
- Keep documentation and control-tool changes scoped, reviewable, and consistent with the templates and checklists.
- Distinguish confirmed facts, inferences, unknowns, and plans. Do not present planned capability as implemented.
- Sensitive, external, production, destructive, financial, or irreversible actions require the explicit approvals and controls described in `METHOD.md` and the relevant checklist. Repository presence does not imply authorization for those actions.
- Do not create a commit, push, tag, publish, or deploy unless the user asks for that action.
- For changes, inspect the final diff and use proportionate verification. The repository has lightweight executable checks, but no conventional application test suite.

## Repository snapshot observed 2026-11-21

- Branch: `main`
- HEAD: `2e290c4` (`feat(okci): complete stage 2 command record foundation`)
- `main` matched `origin/main` when this context was recorded, with twelve untracked OKCI assessment reports requiring review.
- The README describes v0.1.0 as the method introduction and v0.2.0 as the reusable control toolkit; it says v0.2.0 is complete after review, verification, checkpoint, publication, and tagging. Re-check Git and release state before making claims about completion.
- The repository includes ignored, rebuildable SQLite and HTML projection artifacts under `control-desk/`; Markdown records remain authoritative.

## Key files

- `README.md` — project overview, contents, and stated release status.
- `METHOD.md` — canonical process, risk levels, approval boundaries, verification, and completion standard.
- `control-desk/` — authoritative Markdown records plus read-only validation, indexing, discovery, observation, rendering, and local prototype tools.
- `okci/` — command-record contract, structural schema, and unverified registry template.
- `templates/` — milestone, approval, verification, project status, and risk records.
- `checklists/` — before-commit, before-deployment, and high-risk-action controls.
- `examples/sts-ai-lab/per-agent-tool-permissions.md` — historical example of a completed engineering milestone.
