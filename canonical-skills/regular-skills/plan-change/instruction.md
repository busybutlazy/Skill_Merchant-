# Plan Change

## Objective

Create or revise the planning section of one `changes/<change-id>/CHANGE_WORKING.md` without implementing the Change. Use the least ceremony justified by risk and keep one fact in one working location.

## Admission Criteria

Use for a non-trivial feature, fix, migration, contract change, or refactor whose scope or verification needs planning. A trivial, reversible edit with explicit acceptance and validation may proceed without a formal plan when repository policy allows it.

Required inputs are a stable Change ID, request, acceptance criteria, repository rules, relevant specifications/contracts/ADRs, related items from `docs/PENDING.md`, Git state, code/tests, and canonical container commands. Conflicting sources of truth or missing consequential requirements are blockers.

## Decision Readiness Gate

If load-bearing product, domain, externally observable contract, security, data-model, data-ownership, or major architecture decisions remain unresolved, stop and route to `grill-with-docs`. Do not resolve them by assumption or treat a recommendation as approval.

## Risk and Ceremony

- `low`: a lightweight plan may contain objective, scope, acceptance, affected paths, verification, and rollback only.
- `medium`: add bounded tasks, risks, checkpoints, and explicit execution mode.
- `high` or `extreme`: require full traceability, one-task-at-a-time checkpoints, and explicit human approval; prohibited operations remain manual.

Human Plan Approval is mandatory for public contract, schema/migration, authorization/security, irreversible or bulk data operations, production/external spend, dependency/major architecture changes, high/extreme risk, or competing consequential choices. Repository policy may require it more broadly.

## Workflow

1. Read sources of truth, related Pending items and accepted ADRs before implementation details.
2. Inspect Git state and record only evidence that changes the plan; do not produce a repository tour or copy volatile counts.
3. Define objective, scope, observable acceptance, affected paths, risk, rollback, verification, and unresolved questions.
4. Classify risk and choose `one-task-at-a-time` or, for low/medium risk only, `supervised-auto`.
   When `supervised-auto` requires approval, the human must approve the mode explicitly together with its outcomes/Tasks, paths, checkpoints, and remediation envelope.
5. Divide work only as finely as independent verification or checkpoints require.
6. Record relevant Pending IDs as absorbed, scheduled, still unrelated, or blocking. Do not silently expand scope to consume them.
7. Identify durable-decision hotspots, but do not create or accept an ADR during planning without the applicable human decision workflow.
8. Create or update `changes/<change-id>/CHANGE_WORKING.md` using [the template](./references/IMPLEMENTATION_PLAN_TEMPLATE.md). This is a temporary working artifact, not permanent project truth.
9. If approval is required, present the current revision and stop for explicit approval. Otherwise record why the Change qualifies for the lighter path.

## Material Change Rule

Approval is invalidated by changed observable scope or acceptance, a new contract/schema/dependency/security/data/architecture consequence, increased risk, or core implementation outside approved boundaries. Necessary tests, documentation synchronization, ordinary in-scope corrections, and accepted review remediation inside a pre-approved remediation envelope are not material changes.

## Authority Boundary

Do not implement, install dependencies, run migrations, access production/secrets, approve the plan, or commit/push. Missing container support routes to `bootstrap-project`; it never authorizes host execution.
