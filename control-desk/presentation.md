# Read-Only Control Desk Presentation Contract

## Purpose

The first presentation layer is a generated HTML document produced from the file-based records. It is a view, not a second source of truth.

## Required overview content

The overview must show:

- Project name and source-of-truth location
- Record count
- Milestone count
- Per-project milestone totals, approved/proposed counts, high/critical risk count, and incomplete count
- Each milestone ID, title, status, current stage, risk level, approval, verification, and next action
- Linked record IDs
- A visible read-only notice

## Required milestone detail content

For each milestone, the view must show:

- Full Markdown milestone content
- Structured metadata
- Linked approvals, risks, evidence, verifications, decisions, and checkpoints
- Current control state
- A link or reference to the source Markdown record

## Safety requirements

- The renderer must read records only.
- Generated HTML must not contain forms that imply approval or execution.
- The view must not display secrets or unredacted sensitive values.
- The view must identify generated data as derived.
- Missing or invalid records must be reported rather than silently omitted.

## Non-goals

- Authentication
- Editing records
- Approving milestones
- Running commands from the page
- Deployment
- SQLite persistence

## Future extension boundary

Interactive filtering and search may be added while the view remains read-only. The initial controls are browser-local search plus status, stage, and risk filters. Any write action requires a new milestone with explicit approval boundaries, audit records, and recovery controls.

