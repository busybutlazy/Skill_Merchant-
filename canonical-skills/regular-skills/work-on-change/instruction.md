# Work on Change

## Objective

Act as the human-friendly entrypoint for moving one bounded Change forward. Inspect repository evidence, select the applicable installed atomic workflow skill, preserve every approval and authority boundary, and stop at the next human gate.

## Use When

- The user wants to plan, implement, resume, verify, or report one bounded Change.
- The user does not want to remember which atomic Change Workflow skill matches the current state.

Do not use for a complete Roadmap Phase; use `work-on-phase`. Do not perform independent adversarial review in the implementation context; the user should open a fresh agent and invoke `review-change`.

## Routing Workflow

1. Identify exactly one Change and inspect `changes/<change-id>/`, applicable specifications, contracts, ADRs, project rules, Git state, and available container commands.
2. Report a compact header before acting:

   ```text
   Change: <change-id>
   Current state: <observed state>
   Next action: <atomic skill or human gate>
   Allowed now: <bounded actions>
   ```

3. Select the first matching route:
   - Requirements contain consequential unresolved choices: use `grill-with-docs`, then stop at its decision boundary.
   - No approved current Implementation Plan: use `plan-change`, then stop for Human Plan Approval.
   - An approved Plan authorizes one named Task: use `implement-task` and stop after that Task's local verification.
   - An approved low/medium-risk Plan explicitly authorizes `supervised-auto`: use `run-approved-change` only for the approved Task IDs and paths.
   - Approved implementation is complete but canonical verification evidence is missing or stale: use `verify-change`.
   - Verification is complete but the Change Report is missing or stale: use `report-change`.
   - Implementation, Verification Report, and Change Report are complete: stop and provide a Review Handoff for a fresh `review-change` agent.
4. By default, execute one atomic workflow, report the resulting state and next action, then return control to the user. This is a recommended interaction boundary, not an unconditional ban on chaining.
5. Multiple atomic workflows may be chained only when no new Human Approval, decision, checkpoint, independent-review, Git, release, or deployment authority gate lies between them, and the entry request explicitly authorizes the continuous scope. Re-evaluate repository evidence between workflows and stop immediately if the next workflow's admission criteria are not proven.
6. Do not infer approval from the user's original request, an older Plan revision, or completion of a previous stage.

## Review Handoff

The final handoff must identify the Change directory, approved Plan revision, Verification Report, Change Report, relevant specification/contract paths, and diff base. Ask the user to open a fresh agent and invoke `review-change` against those artifacts.

## Authority Boundary

This skill routes and coordinates installed skills; it does not weaken their admission criteria or gain their combined authority. Never self-approve, review the implementation in the same context, expand scope, modify an unapproved contract, install production dependencies, run migrations, access production/secrets, commit, push, merge, release, or deploy unless a separate applicable workflow and explicit authority allow that action.
