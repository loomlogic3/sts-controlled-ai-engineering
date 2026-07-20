# STS Controlled AI Engineering

A practical, platform-independent method for planning, building, testing, and shipping software with AI while keeping humans in control.

## Purpose

AI can increase the speed and power of software development, but greater power also increases the need for deliberate control.

STS Controlled AI Engineering provides a repeatable workflow for using AI coding assistants without surrendering human judgment, security boundaries, verification, or accountability.

The method can be used with Codex, ChatGPT, terminal-based tools, local AI systems, or other engineering assistants.

## Core Principle

> Before you add power, add more control.

AI may help observe, explain, plan, implement, test, and document work. A human remains responsible for approving sensitive actions, evaluating evidence, and deciding when a milestone is complete.

## Controlled Engineering Lifecycle

The canonical lifecycle is:

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

Each stage creates a control boundary. Work should not advance merely because an AI system is capable of continuing.

## Operating Principles

- Research first, build second, deploy third.
- Observe the existing system before changing it.
- Define scope before implementation.
- Keep changes small, reviewable, and reversible.
- Require explicit human approval for sensitive actions.
- Use deterministic tools and tests wherever possible.
- Treat AI output as a proposal until verified.
- Never expose secrets, credentials, private keys, or production data.
- Do not enable live execution by implication.
- Preserve offline operation where the product requires it.
- Use Git checkpoints as controlled recovery boundaries.
- Record lessons before beginning the next milestone.

## What This Repository Contains

This repository will provide:

- The canonical STS Controlled AI Engineering method
- Reusable milestone and approval templates
- Verification and deployment checklists
- Risk-classification guidance
- Worked examples from real STS projects
- A versioned record of how the method evolves

## Documentation and Toolkit

### Canonical method

- [Controlled AI Engineering Method](METHOD.md)

### Reusable templates

- [Milestone Record](templates/milestone.md)
- [Human Approval Record](templates/approval-record.md)
- [Verification Record](templates/verification-record.md)
- [Project Status Record](templates/project-status.md)
- [Risk Register](templates/risk-register.md)

### Operational checklists

- [Before-Commit Checklist](checklists/before-commit.md)
- [Before-Deployment Checklist](checklists/before-deployment.md)
- [High-Risk-Action Checklist](checklists/high-risk-actions.md)

### Worked examples

- [STS AI Lab: Per-Agent Tool Permissions](examples/sts-ai-lab/per-agent-tool-permissions.md)

## Who This Is For

This method is designed for:

- Solo developers working with AI coding assistants
- Small teams that need traceable human approval
- Builders learning software engineering through real projects
- Systems involving payments, examinations, infrastructure, automation, AI, or trading
- Projects where safety and recovery matter as much as development speed

## Example Projects

The method is being developed through practical use across SynthThinkingSystems projects, including:

- STS AI Lab
- STS Exam Control System
- STS CivicOS
- SynthThinking POS
- STS AlertHub
- SynthQuant control systems


## Current Status

Version `v0.1.0` established:

- The project introduction
- The canonical controlled engineering method
- A reusable milestone template
- One worked example from STS AI Lab

Version `v0.2.0` adds the reusable control toolkit:

- Human approval records
- Verification records
- Project-status records
- Risk registers
- Before-commit checks
- Before-deployment checks
- High-risk-action controls

This toolkit release is complete only after it is reviewed, verified, checkpointed, published, and tagged as `v0.2.0`.


## Licence

This project is available under the MIT License.
