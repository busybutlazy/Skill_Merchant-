# Review Change

## Objective

Try to disprove the completion claim in a fresh context. Review behavior, risk and evidence before document cosmetics; never repair, approve, retain decisions, or close the Change.

## Independence Gate

Formal review requires a fresh agent/session that did not inherit the implementation conversation. A subagent qualifies only when isolation is guaranteed. Otherwise stop and ask for a fresh session. Same-context self-checks are not formal review.

## Required Inputs

Require Change ID, request/acceptance, approval where applicable, `CHANGE_WORKING.md`, attributable diff, current verification, relevant project truth and CI/contract history. Legacy artifacts may be read, but their quantity is not evidence of correctness.

## Review Priority

Review in this order:

1. observable behavior and core completion claim;
2. security, authorization, data integrity and destructive effects;
3. contract, migration and compatibility;
4. acceptance criteria and whether tests can fail for the claimed defect;
5. scope, dependencies, rollback and operational risk;
6. misleading completion or verification claims;
7. durable user/operator/project documentation.

Pure working-record metadata, stale round numbers, duplicated prose, formatting, line/file counts, or historical narration are not product findings unless they could mislead an operator, conceal failed evidence, falsify approval/security/migration/rollback, or cause a later agent to take an unsafe action.

## Workflow

1. Establish diff base, scope, claimed outcome and fresh-context independence.
2. Trace consequential acceptance through implementation and discriminating tests; challenge mock-only or self-referential evidence.
3. Inspect normal/failure paths and the risk areas above.
4. Use stable finding IDs in one `changes/<change-id>/REVIEW.md`; update statuses in that file rather than creating `REVIEW_REPORT_2`, `_3`, and later copies.
5. Classify findings as Blocking, High, Medium, Low, or Suggestion with evidence, impact and bounded direction.
6. Identify valid out-of-scope concerns as Pending candidates. Do not make unrelated Pending items block this Change unless their trigger is due or they disprove acceptance.
7. Flag a `Durable Decision Gap` when a consequential long-lived tradeoff exists only in temporary artifacts. This creates an ADR candidate for Human Retention review; it does not authorize an ADR.
8. Stop for human disposition.

## Review Round Budget

Default to one full review and one targeted confirmation of accepted findings. A new full review is justified only when remediation changes observable behavior, introduces consequential scope/contract/schema/security/data/architecture effects, broadly repairs Blocking/High findings, or a human explicitly requests it. Documentation-only or metadata remediation does not restart full review.

## Targeted Confirmation

After human-authorized remediation, confirm only accepted finding IDs and affected risk surfaces. Update their statuses and note any genuinely new consequential defect. Do not reopen settled cosmetic history or rewrite the implementer's final narrative.

## Authority Boundary

The only permitted write is `REVIEW.md`. The reviewer does not edit implementation, decide scope, accept an ADR, disposition Pending items, write final `CHANGE.md`, delete working artifacts, approve, commit, merge, release or deploy.
