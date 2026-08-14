# What Next

## Objective

Report the repository's governed lifecycle state and select the safest human-facing workflow entrypoint. This is the Development Workflow installation root, not authority to run every stage.

## Evidence Model

Inspect repository rules, durable specifications/contracts/ADRs/Roadmap, `docs/PENDING.md`, active `CHANGE_WORKING.md` records, final `CHANGE.md` records, `REVIEW.md`, Git state, and container commands. Working artifacts may be retired after closure; their absence is not missing evidence when final durable destinations and Git history prove closure.

Report:

```text
Current state: <observed lifecycle/change/phase state>
Evidence: <key paths>
Pending: <blocking / untriaged / relevant / unrelated counts>
Next entrypoint: <skill or human action>
Next gate: <approval, decision, retention, review, or acceptance>
```

## Routing Order

1. A Pending item whose recorded trigger is due and directly blocks the candidate next action: `triage-pending`, then `grill-with-docs` if a consequential decision is unresolved.
2. Consequential unresolved project/change choices: `grill-with-docs`.
3. Resolved new-project decisions lacking approval-ready definition: `define-project`.
4. Approved greenfield definition lacking engineering baseline: `bootstrap-project`.
5. An active bounded Change: `work-on-change`, using its lifecycle status.
6. A reviewed/remediated Change ready for absorption or waiting on ADR retention: `close-change` or its Human Retention Gate.
7. A final `CHANGE.md` waiting on Human Change Acceptance: request acceptance; do not recreate retired working artifacts.
8. One exact approved Roadmap Phase: `work-on-phase`.
9. No active Change and meaningful untriaged Pending items: suggest `triage-pending`.
10. Git/PR work: require separate `commit` or `create-pr` authority.

Unrelated Pending items are summarized but do not block current work. If evidence is ambiguous, report the smallest missing fact instead of guessing.

## Rules

- File presence is not human approval or ADR acceptance.
- Do not cross Human Approval, Retention, Decision, Review, Acceptance, Git, release, or deployment boundaries.
- Formal review requires current verification and a concise Review Handoff for the attributable diff, not a separate pre-review Change Report.
- Keep `review-change` fresh and adversarial; keep `close-change` fresh but bounded to convergence.
- Do not treat deletion of absorbed temporary artifacts as evidence loss.
