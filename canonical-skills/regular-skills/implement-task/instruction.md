# Implement One Task

Execute exactly one named task or bounded outcome from an approved or policy-admitted `CHANGE_WORKING.md`, then stop at its checkpoint.

## Use This For

- High-risk or `one-task-at-a-time` work.
- A cross-agent handoff or explicit checkpoint requires one bounded task.

Do not use for vague whole-Phase work, planning, full verification, review, closure, or automatic later tasks.

## Required Inputs

Require the Change ID, current working record, exact task, applicable approval evidence, allowed paths, acceptance, repository rules, and canonical container command. Never infer approval from file existence.

## Workflow

1. Read the working record and restate only the task boundary, prohibited areas, and expected result.
2. Inspect Git state and stop on unexplained overlapping edits or attribution-blocking failures.
3. Make the minimum in-scope implementation and tests.
4. Run task-local checks through existing Docker/Compose/Make/container wrappers only.
5. Append a concise execution entry to `CHANGE_WORKING.md`: outcome, files, commands/exits, omissions, and deviations. Use [the checklist](./references/TASK_HANDOFF_CHECKLIST.md) only for a cross-agent or checkpoint handoff.
6. Capture a newly discovered out-of-scope concern as a bounded item in `docs/PENDING.md` when that file exists or repository policy establishes it. This capture is not scope expansion: record evidence, consequence, why deferred, trigger, owner, and source; do not implement or decide the solution.
7. Stop. Do not begin another task unless the approved continuous scope explicitly permits it through `run-approved-change`.

## Stop Conditions

Stop for material scope/acceptance change, an unapproved core path, contract/schema/dependency/security/data/architecture change, destructive or production access, missing container entrypoint, unexplained edits, or a task that cannot remain independent. Necessary tests, documentation synchronization, and ordinary corrections inside the task are not new tasks.

## Evidence Boundary

A task-local result is not full verification, independent review, closure, human acceptance, or Git authority.
