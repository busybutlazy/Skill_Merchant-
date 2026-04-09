# Source Inventory

## Source Identity

- source root: `tmp/foreign_skills/soxakore-codex-engineering-skills-verified-operator-1`
- source type: single skill folder
- requested canonical name: `verified-operator`
- source-declared name: `verified-operator`

## Capability List

- Turn user requests into verified execution rather than hypothetical advice
- Build and maintain a live world model before each action
- Grade actions by risk: `L0`, `L1`, `L2`, `L3`
- Design bounded mutations with explicit preconditions, receipts, and rollback
- Maintain a working ledger and append-only audit trail for high-stakes tasks
- Verify every mutation with receipts stronger than exit-code-only confirmation
- Redact secrets from receipts, logs, summaries, and delegation prompts
- Resolve conflicting signals by preferring the nearest system of record
- Recover from drift caused by retries, stale assumptions, partial writes, auth expiry, or human interference
- Ask for approval before external, destructive, financial, or security-sensitive actions
- Handle async handoffs that require human action outside the agent's tools
- Delegate to sub-agents only when available and explicitly authorized
- Apply a verified completion bar and operator-style final response contract
- Manage long-running context with ledger compression and handoff summaries
- Track metrics and telemetry across tasks
- Avoid common anti-patterns such as narrating instead of executing
- Handle edge cases including cascading rollback, partial failures, throttling, concurrent human changes, and ambiguous success
- For complex tasks, reason with dependency graphs, confidence scores, invariant monitoring, failure taxonomy, multi-phase orchestration, and temporal reasoning

## Trigger List

- User asks to operate live systems instead of only advising
- Task spans files, terminals, browsers, APIs, devices, or external services
- User wants proof, receipts, screenshots, diffs, status codes, IDs, or logs
- Task is high-stakes, long-running, or multi-step with drift or rollback risk
- Task requires multi-system coordination or multi-phase deployment/migration

## Do-Not-Use Boundaries

- Pure Q&A or explanation with no system interaction
- Single-file code edits that do not depend on external state
- Creative writing, brainstorming, or hypothetical scenarios
- Research-only requests where no mutation or verification is needed
- Tasks where the user explicitly says to only explain and not act

## Explicit Support-File References

- `templates/templates.md`
- `examples/deploy-static-site.md`
- `examples/api-integration.md`
- `examples/multi-service-coordination.md`
- `examples/device-control.md`
- `examples/multi-phase-orchestration.md`
- `agents/openai.yaml`

## When To Consult Support Files

- Consult `templates/templates.md` at task start when a ledger, audit trail, checkpoint, delegation prompt, final summary, metrics log, dependency graph, phase plan, invariant checklist, confidence-scored trail, or temporal timer needs a concrete template
- Consult `examples/deploy-static-site.md` for a simple deploy-and-verify loop
- Consult `examples/api-integration.md` for receipt-driven API wiring and secret redaction patterns
- Consult `examples/multi-service-coordination.md` for coordinated Docker, Nginx, and DNS changes with drift recovery
- Consult `examples/device-control.md` for ADB/device workflows with backup and rollback
- Consult `examples/multi-phase-orchestration.md` when the task spans multiple environments or phases and needs advanced sections §16-§21
- Consult `agents/openai.yaml` only to recover target-specific invocation wording for frontmatter; it is not part of the canonical instruction body

## Important Workflow Order / Section Structure

- Quick start: `BEFORE -> RISK -> ACT -> PROVE -> CONFIRM`
- Complex mode prep: `GRAPH -> PHASE -> INVARIANTS`
- Operating loop: map world, grade risk, design smallest action, execute, verify, update world model, recover/escalate/continue, close on verified end state
- Escalate from approval rules before L2/L3 actions unless exact approval already exists
- Use checkpointing after every 3 verified mutations or any L2+ mutation
- Advanced sections §16-§21 extend, not replace, the base loop

## Output Contract

- Use a compact working ledger during execution
- For L2+ tasks, maintain an append-only audit trail with redacted receipts
- Close with an operator-style summary covering:
  - what changed
  - what evidence proved it
  - what remains risky, partial, or blocked
  - what the next safe action is

## External Dependencies

- None required for installation
- Runtime examples assume tools/services such as shell, browser, curl, SSH, Docker, Nginx, Cloudflare API, Vercel CLI, ADB, databases, and external APIs depending on the task

## Permission-Sensitive Behaviors

- L2 and L3 mutations require explicit user approval unless already pre-approved for that exact action class
- External side effects, paid resources, security posture changes, credential handling, data deletion, or user-visible mutations are approval-sensitive
- Secrets must be redacted before logging, summarizing, or delegating
- Concurrent human changes must halt the chain instead of being silently overwritten
