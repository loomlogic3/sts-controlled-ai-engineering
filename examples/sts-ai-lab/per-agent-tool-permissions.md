# Worked Example: Per-Agent Tool Permissions

## Example Status

This is a historical reconstruction of a completed STS AI Lab milestone.

It demonstrates how the STS Controlled AI Engineering method can document real engineering work after the implementation has already been completed.

## Identification

- Project: STS AI Lab
- Milestone: Per-agent tool permissions
- Repository: `loomlogic3/sts-ai-lab`
- Pull request: `#5`
- Feature commit: `5408dbe`
- Merge commit: `d4b1e8a`
- Completion date: 2026-07-16
- Risk level: Medium
- Final status: Completed and merged

## 1. Mission

Add explicit tool permissions to each canonical STS AI Lab agent so that an active agent can use only its authorised registered tools.

The milestone must preserve existing commands, stateful memory behaviour, and unknown-command fallthrough.

### Why this mattered

A shared tool registry without agent-specific permissions allows every active agent to reach the same registered tools.

That weakens the control boundary between agents with different responsibilities.

The milestone introduced a permission layer before adding more tools or more powerful agent behaviour.

## 2. Current State — Observe

Before the milestone:

- Canonical agent definitions already existed.
- Existing stateless slash commands used the command registry.
- `/memory` and `/clear` remained stateful commands handled through the active conversation-memory object.
- Agent definitions did not yet declare explicit allowed tools.
- No new command or permission interface was required.

### Relevant components

- Canonical agent JSON definitions
- Agent-definition loader
- Command registry
- Tool router
- Conversation memory
- Pytest regression suite

## 3. Problem — Understand

### Confirmed facts

- Registered stateless tools were available through shared command-routing infrastructure.
- Agents had distinct definitions and responsibilities.
- The definitions did not contain explicit tool allowlists.
- Stateful memory commands required the active `ConversationMemory` instance.

### Root problem

The system had a shared execution path but lacked an explicit per-agent authorization boundary before registered stateless tool execution.

## 4. Goal and Scope

### Goal

Introduce explicit per-agent tool allowlists and enforce them before registered stateless tool handlers execute.

### In scope

- Add `allowed_tools` to existing canonical agent definitions.
- Load permissions through the canonical definition path.
- Enforce permissions for registered stateless tools.
- Preserve stateful memory commands.
- Preserve unknown-command fallthrough.
- Add regression tests.

## 5. Out of Scope

The milestone explicitly excluded:

- New commands
- `/doctor`
- Model profiles
- Permission-management UI
- Memory redesign
- Command-registry rewrite
- A new configuration format
- A second test framework

Pytest remained the only test framework.

## 6. Risks

| Risk | Impact | Control |
|---|---|---|
| Existing commands become unavailable | Agent workflows break | Regression tests for allowed tools |
| Unauthorised tools remain executable | Permission boundary fails | Denied-tool tests |
| `/memory` or `/clear` break | Stateful conversation control regresses | Stateful memory tests |
| Unknown commands are blocked prematurely | AI fallthrough behaviour changes | Unknown-command fallthrough tests |
| Registry architecture changes unnecessarily | Scope and maintenance cost expand | Explicit out-of-scope boundary |

### Recovery plan

Because the change was isolated and version-controlled, the branch could be corrected before merge or reverted to the previous Git checkpoint if regression evidence appeared.

## 7. Acceptance Criteria

The milestone required evidence that:

- [x] Every canonical agent definition declares allowed tools.
- [x] Allowed registered tools execute for the active agent.
- [x] Disallowed registered tools are denied.
- [x] `/memory` and `/clear` remain stateful and available.
- [x] Unknown slash commands retain their existing fallthrough behaviour.
- [x] The command registry remains structurally intact.
- [x] No new commands or unrelated architecture are introduced.
- [x] The complete pytest suite passes.
- [x] Python compilation succeeds.

## 8. Human Approval

The implementation was limited to the pull request’s stated permission milestone and explicit exclusions.

The surviving GitHub record confirms that the scoped change was reviewed through pull request `#5` and merged on 2026-07-16.

The exact original approval statement is not reproduced here because it is not part of the available pull-request record.

## 9. Execute in Small Steps

### Step 1: Extend canonical definitions

- Added `allowed_tools` to each existing canonical agent JSON definition.
- Preserved existing agent metadata and prompts.

### Step 2: Load permissions canonically

- Used the existing canonical agent-definition path.
- Avoided introducing another configuration source.

### Step 3: Enforce permissions

- Checked the active agent’s allowed tools before executing registered stateless handlers.
- Preserved the existing stateful memory path.

### Step 4: Preserve fallthrough

- Kept unknown slash commands available for existing AI handling where applicable.

### Step 5: Add regression tests

Tests covered:

- Allowed tools
- Denied tools
- Canonical permission loading
- Unknown-command fallthrough
- Stateful memory commands
- Command-registry integrity

## 10. Verify with Evidence

The pull request recorded these verification commands:

    PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 venv/bin/python -m compileall -q app

The recorded result confirms that the regression suite and compilation checks passed before merge.

### Scope verification

The pull request also confirmed:

- No new commands
- No `/doctor`
- No model profiles
- No permission UI
- No memory redesign
- No registry rewrite
- No new configuration format
- Pytest remained the only test framework

## 11. Git Checkpoint

- Feature commit: `5408dbe` — Add per-agent tool permissions
- Merge commit: `d4b1e8a` — Merge pull request #5
- Target branch: `main`
- Pull request status: Merged
- Pull request comments: None recorded

## 12. Lessons Learned

### What worked

- Permissions were added to the canonical agent definitions instead of a parallel configuration system.
- Enforcement occurred before registered tool execution.
- Existing stateful and fallthrough behaviours were protected by tests.
- Explicit exclusions prevented the milestone from expanding into a broader permissions platform.

### What should be repeated

- Add control boundaries before adding new agent power.
- Preserve established architecture unless the milestone requires changing it.
- Test both authorised and unauthorised behaviour.
- Record explicit out-of-scope items in the pull request.
- Verify scope as well as functionality.

### Technical debt deferred intentionally

The milestone did not attempt to provide:

- Permission-management UI
- Dynamic permission editing
- Model profiles
- A diagnostic `/doctor` command

Those capabilities require separate observation, scope, risk analysis, and approval.

## 13. Next Milestone

The next completed STS AI Lab milestone introduced one canonical runtime for shared agent-execution behaviour.

That sequencing was appropriate because permission controls were established before execution behaviour was further consolidated.

## Completion Decision

- Status: Completed
- Acceptance criteria: Satisfied
- Tests: Passed
- Compilation: Passed
- Pull request: Merged
- Evidence source: GitHub pull request `#5` and its commits

> Before you add power, add more control.
