# Run Approved Change

## Objective

Execute the explicitly approved continuous scope of a low/medium-risk Change, append concise evidence to its working record, verify it, and stop before independent review.

## Admission Gate

Require `changes/<change-id>/CHANGE_WORKING.md` with current approval or a documented low-risk lightweight admission, `Automation mode: supervised-auto`, exact outcomes/tasks and path scope, checkpoints, rollback, acceptance criteria, attributable Git state, and canonical container commands. Use [the checklist](./references/AUTO_EXECUTION_CHECKLIST.md).

Reject high/extreme risk; production/secrets; irreversible or bulk data operations; authentication/payment/privilege/deployment; ambiguous or superseded approval; and `one-task-at-a-time` mode. A separate bounded task uses `implement-task`.

## Workflow

1. Read the working record, sources of truth, relevant Pending items, approved scope, remediation envelope, and stop conditions.
2. Inspect Git state and preserve unrelated work.
3. Execute approved outcomes in order. For each, make the minimum implementation/tests, run task-local container checks, and append one concise evidence entry. Do not restate unchanged scope or duplicate command output across files.
4. Correct ordinary implementation mistakes inside the approved boundary. Stop for a material change as defined by the working record.
5. Capture valid out-of-scope discoveries in `docs/PENDING.md` without implementing them; update an existing matching item instead of duplicating it.
6. Enter evidence-only verification and run applicable canonical checks. Append results to the working record using the `verify-change` evidence standard.
7. If verification fails, leave evidence-only mode. A correction may proceed only inside the pre-approved remediation envelope; then rerun affected and required full verification. Otherwise stop for the smallest human decision.
8. On success, inspect the attributable diff and complete the working record's Review Handoff: completion claim, limitations, Pending candidates, possible ADR candidates, and diff base.
9. Stop for a fresh `review-change` session or human reviewer. Do not create a separate Change Report, review your own work, close the Change, or commit/push/merge/release/deploy.

## Mandatory Stop Conditions

Stop for changed observable scope/acceptance; an unapproved contract/schema/dependency/security/data/architecture consequence; increased risk; a core path outside approval; unmet checkpoint; destructive/production/secret access; missing container support; unexplained Git changes; or verification failure outside the remediation envelope.

## Authority Boundary

Supervised-auto grants implementation and verification authority only for the approved envelope. It does not grant review, Human Retention decisions, ADR acceptance, closure, acceptance, or Git/release authority.
