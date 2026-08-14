# Prepare Change Review Handoff

## Objective

Prepare or refresh the concise completion claim and Review Handoff inside `changes/<change-id>/CHANGE_WORKING.md`. This compatibility workflow no longer creates a separate pre-review `CHANGE_REPORT.md`; final durable reporting belongs to `close-change` after review and human disposition.

## Use When

- Implementation and current verification exist, but the working record is not ready for independent review.
- A legacy workflow explicitly invokes `report-change`.

Do not use for implementation, verification execution, review, closure, ADR acceptance, or release notes.

## Workflow

1. Establish the attributable diff base and inspect the full diff, working record, approval, verification and CI evidence.
2. Compare consequential acceptance and planned outcomes with the implementation.
3. Update only the Review Handoff with: completion claim, observable behavior, material contract/schema/migration/dependency/configuration effect, deviations, limitations, rollback, diff base, Pending candidates, and ADR candidates.
4. Keep evidence by reference; do not duplicate command tables, file inventories, volatile counts, SHA lists, or task history.
5. Mark the lifecycle `ready-for-review` only when verification is current and no known blocker is hidden.
6. Stop for a fresh `review-change` session. Do not write `CHANGE.md`, delete working artifacts, or claim acceptance.

## Boundaries

The only permitted write is the owned working record. Missing or conflicting evidence must be marked incomplete. Report preparation cannot repair code or turn an inference into proof.
