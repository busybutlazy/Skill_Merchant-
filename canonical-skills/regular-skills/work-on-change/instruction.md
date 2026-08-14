# Work on Change

## Objective

Move one bounded Change forward with ceremony proportional to risk. Route among planning, implementation, verification, review handoff, remediation, Pending capture, and closure while preserving human gates.

## Routing Workflow

1. Identify one Change and inspect its `CHANGE_WORKING.md` or legacy artifacts, final `CHANGE.md`, related specifications/contracts/ADRs, relevant Pending items, Git state, and container commands.
2. Report:

   ```text
   Change: <id>
   Current state/risk: <observed>
   Relevant Pending: <IDs or none>
   Next action: <atomic skill or human gate>
   Allowed now: <bounded actions>
   ```

3. Choose the first applicable route:
   - due Pending blocker or unresolved consequential choice: `triage-pending` / `grill-with-docs`;
   - no adequate plan: `plan-change`, using lightweight planning for eligible low risk;
   - one checkpointed task: `implement-task`;
   - approved continuous low/medium scope: `run-approved-change`;
   - implementation complete but verification missing/stale: `verify-change`;
   - verification current but Review Handoff incomplete: `report-change` compatibility workflow;
   - ready for independent review: hand off to a fresh `review-change` session;
   - accepted findings need bounded remediation: use the approved mode/envelope, then targeted reviewer confirmation;
   - review/disposition complete: `close-change`;
   - final `CHANGE.md` complete: stop for Human Change Acceptance.
4. Execute one atomic workflow by default. Chain only within explicitly authorized continuous scope and when no new decision, approval, checkpoint, independent-review, retention, acceptance, Git, release, or deployment gate intervenes.
5. Re-evaluate evidence after each workflow. Necessary tests, documentation synchronization, ordinary in-scope corrections, and accepted findings within a pre-approved remediation envelope do not automatically invalidate the plan.

## Risk-Adaptive Ceremony

- trivial: direct bounded edit, targeted verification and concise handoff when repository policy permits;
- low: lightweight working record, implementation, verification, closure; independent review when risk or policy warrants it;
- medium: approved plan, implementation, verification, one full review plus one targeted confirmation, closure;
- high/extreme: full traceability, one-task checkpoints, explicit approvals, independent review and human acceptance.

## Authority Boundary

This router does not weaken atomic admission criteria. It cannot self-approve, accept/supersede ADRs, disposition retention, review in implementation context, expand scope, or implicitly commit/push/merge/release/deploy.
