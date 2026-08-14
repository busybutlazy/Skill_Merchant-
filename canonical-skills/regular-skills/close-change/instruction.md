# Close Change

## Objective

After implementation, current verification, independent review, remediation, and human disposition, compress temporary evidence into durable project truth and one final `changes/<change-id>/CHANGE.md`. Never rediscover or re-review the implementation.

## Fresh Closure Context

Prefer a fresh agent context that did not implement the Change. Freshness prevents the implementer's narrative from becoming the final truth, but the closer must use bounded inputs rather than rereading the whole conversation: final diff/base, `CHANGE_WORKING.md`, current verification, `REVIEW.md`, human disposition, relevant durable documents, ADR index, and Pending inbox.

The closer is not a second reviewer. Missing or conflicting evidence is a stop condition, not permission to reconstruct history by assumption.

## Admission Criteria

- Final verification is current for the attributable diff.
- Accepted Blocking/High/Medium findings are resolved, rejected with human rationale, or explicitly deferred by authorized disposition.
- Targeted confirmation is present where required.
- Human disposition for review findings exists.
- No material implementation work remains.

## Workflow

1. Establish final diff/base and confirm closure inputs agree on current lifecycle state.
2. Build an Absorption Matrix using [the closure template](./references/CLOSURE_TEMPLATE.md). Every consequential item in temporary artifacts must be:
   - absorbed into an existing durable source;
   - captured in `docs/PENDING.md`;
   - proposed as an ADR candidate;
   - retained in final `CHANGE.md`; or
   - intentionally discarded with a reason.
3. Update specifications, contracts, Roadmap, runbooks or other durable truth only to reflect already-approved outcomes. Do not make new product or architecture decisions during closure.
4. Assemble a Decision Retention Packet for all possible ADR candidates. For each, state why it may deserve an ADR, existing coverage, alternatives evidenced, and a recommendation: Create ADR / Keep in Change Record / Defer to Pending / Discard.
5. Stop at the mandatory Human Retention Gate. Ask whether each candidate is worth an ADR, preferably as one batch. Silence is not approval.
6. Only after the human chooses `Create ADR`, draft a `Proposed` ADR. A second explicit human confirmation is required before marking it `Accepted` or changing/superseding an Accepted ADR.
7. Apply the approved retention dispositions, update Pending item statuses/destinations, and write concise final `CHANGE.md`: outcome, consequential behavior/decisions, current verification reference, review disposition, limitations, rollback, and durable destinations. Do not reproduce task logs or every command.
8. Propose the exact temporary artifacts to delete or archive. Delete only after the Absorption Matrix is complete and repository/user authority permits it; preserve Git history and unrelated files.
9. Request a narrow closure-integrity check from the prior reviewer or a human when available: confirm that final durable text does not distort accepted findings. This is not another full code review.
10. Stop for Human Change Acceptance and separately authorized Git actions.

## ADR Authority Gate

Deleting or archiving a working artifact never authorizes promotion of its rationale into an ADR. Agents may identify candidates and draft only after the human selects `Create ADR`; only explicit human confirmation may mark an ADR Accepted, modify an Accepted decision, or mark it Superseded.

## Boundaries

Do not edit implementation/tests, run a new full review, approve the Change, infer retention, or commit/push/merge/release/deploy. If closure exposes a product defect or material decision, capture it as Pending or stop for the applicable workflow.
