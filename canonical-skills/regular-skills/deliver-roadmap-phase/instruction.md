# Deliver Roadmap Phase

## Objective

Deliver one approved Roadmap Phase as bounded governed Changes, absorb temporary phase evidence, and stop for Human Phase Acceptance.

## Admission Criteria

Require an exact Roadmap path and Phase ID/heading, approved observable outcome/scope/acceptance, resolved Phase-start Decision Gates, relevant specifications/contracts/ADRs, current Pending inbox, repository rules, and containerized verification. Reject ambiguous or multiple phases, product discovery by assumption, direct Git/release/deployment authority, and a single already-bounded Change.

## Phase Readiness Gate

Read every gate before planning, together with every Pending item relevant to the Phase. A due blocker prevents planning; unrelated Pending items do not. Unresolved consequential choices route to `grill-with-docs`; classification routes to `triage-pending`.

## Phase Workflow

1. Record exact Phase identity, boundaries, Decision Gates and relevant Pending IDs in a temporary `changes/<phase-run-id>/PHASE_WORKING.md` using [the packet template](./references/PHASE_DELIVERY_PACKET_TEMPLATE.md).
2. Perform read-only discovery of durable sources, Git state, tests and container commands.
3. Decompose only enough to define independently verifiable child outcomes, dependency order, risk/mode, paths, checkpoints and rollback. Do not pre-generate full child plans before a child starts.
4. Present one Phase Delivery Packet approval gate. Approval names revision, phase, child graph, risks/modes, paths and checkpoints.
5. After approval, start each child through `work-on-change`. Create its `CHANGE_WORKING.md` only when the child becomes active. Low/medium supervised children may run continuously; high/checkpointed children stop task by task.
6. Capture new out-of-scope discoveries in `docs/PENDING.md`; do not smuggle them into the Phase. A failed or blocked child prevents dependent children.
7. Each required child must complete verification, independent review where required, Human Retention decisions, absorption and final `CHANGE.md` through `close-change` before it counts as closed.
8. Verify Phase outcomes at Phase level without copying child command logs. Reference child final records and record only cross-child evidence, unresolved/deferred outcomes and due Decision Gates.
9. Build a Phase absorption summary: update Roadmap and durable project truth only after applicable decisions and acceptance; route new ADR candidates through the same Human Retention Gate; capture remaining concerns in Pending.
10. Propose deletion or archival of `PHASE_WORKING.md` and unused child drafts after absorption. Keep a concise final Phase summary only when it adds information beyond Roadmap plus child `CHANGE.md` records.
11. Stop for Human Phase Acceptance. Only separately authorized action may update Roadmap completion state or perform Git/release work.

Never commit, push, merge, release, or deploy implicitly.

## Review and Stop Boundaries

Child review follows one full review plus one targeted confirmation by default. Do not launch repeated full reviews for document metadata. Stop for ambiguous identity, missing sources/container entrypoint, material scope/contract/schema/dependency/architecture/security/data deviation, new unapproved core path, unmet checkpoint, failed/incomplete verification outside an approved remediation envelope, production/secrets/destructive access, or another Phase.

## Authority Boundary

Coordination does not weaken atomic skills or grant self-approval, ADR acceptance, retention disposition, review in implementation context, Human Phase Acceptance, commit, push, merge, release or deployment.
