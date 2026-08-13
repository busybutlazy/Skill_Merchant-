# Review Change

Try to disprove the completion claim. The only permitted write is the owned review report; never repair or approve the implementation.

## Use This For

- A change has implementation, verification, and change-report evidence ready for adversarial review.

## Do Not Use This For

- Reviewing work from the same agent/session/context that planned or implemented the change.
- Implementing fixes, authoring the plan under review, running a self-approval gate, merging, releasing, or replacing human review.

## Independence Gate

Formal review requires a fresh agent context that did not inherit the implementation conversation. A subagent qualifies only when the platform guarantees that its context does not inherit that conversation. If independence cannot be established, stop and ask the user to open a fresh agent/session; do not write or update the formal `REVIEW_REPORT.md`.

Self-checks and same-context review notes may help implementation, but they cannot satisfy the independent review gate and must not be represented as formal review evidence.

## Required Inputs

- Change ID, request/acceptance criteria, approved plan and approval evidence.
- Full attributable diff, tests, task handoffs, verification report, change report, and relevant CI/contract history.

If core artifacts are missing after the independence gate is satisfied, report the evidence gap as a finding.

## Workflow

1. Establish scope, comparison base, and claimed outcome. Prove fresh-context independence before reviewing or writing the report.
2. Trace every acceptance criterion through implementation and tests; challenge unsupported or mock-only claims.
3. Inspect normal and failure paths for correctness, error handling, authorization/security, data consistency, backward compatibility, and hidden contract/dependency/migration effects.
4. Look for out-of-scope edits, over-abstraction, missing rollback, skipped tests, misleading reports, and untracked/generated artifacts.
5. Classify findings as Blocking, High, Medium, Low, or Suggestion. Give evidence, impact, and a bounded remediation direction; do not edit code.
6. Write `changes/<change-id>/REVIEW_REPORT.md` using [the checklist/template](./references/REVIEW_REPORT_TEMPLATE.md).
7. Stop for human disposition. Do not approve, implement findings, merge, release, or silently call another workflow.

## Stop Conditions and Boundaries

Use read-only inspection and existing containerized checks only when necessary to challenge evidence. Never install dependencies or run project commands directly on the host. Stop before destructive commands, production/secret access, migrations, implementation edits, or scope decisions. Unexplained worktree state and missing container entrypoints must be recorded, not bypassed.

## Evidence Standard

Distinguish verified defects, evidence gaps, and suggestions. Cite paths, symbols, commands, outputs, and report contradictions. Absence of findings is not proof of correctness; state unreviewed areas and residual risk.
