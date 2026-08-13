# Project Agent Rules

## Purpose and Source of Truth

- Specification:
- Contracts:
- Architecture/ADRs:
- Change artifacts:

## Docker-Only Execution

Project dependencies and project commands must run through the approved Docker/Compose/canonical task entrypoint. Do not install or run them on the host. Host use is limited to repository text operations, Git, and Docker invocation.

## Canonical Commands

| Purpose | Command | Availability/notes |
|---|---|---|
| Setup | | |
| Format check | | |
| Lint | | |
| Type check | | |
| Unit test | | |
| Integration test | | |
| Full verify | | |
| Build | | |
| Run | | |

## Architecture Boundaries

## Protected Files and Operations

## Change Workflow and Approval Gates

Non-trivial work follows request → read-only plan → human approval → approved execution → container verification → reports → independent review → human acceptance. One atomic workflow at a time is the recommended default; adjacent workflows may be chained only when the request explicitly authorizes that scope and no new authority gate intervenes. Material deviations stop for approval.

Formal independent review must run in a fresh agent/session that did not inherit the implementation conversation. A subagent qualifies only when the platform guarantees that isolation; same-context self-review cannot satisfy the formal review gate.

## Stop Conditions

- Requirements/contracts conflict or scope must expand.
- Existing unexplained worktree changes overlap the task.
- Docker or a required container entrypoint is unavailable.
- A dependency, migration, secret, production access, destructive action, or protected-file change needs new approval.
- Required verification cannot run.

## Definition of Done

List project-specific implementation, verification, documentation, review, and CI gates. Never claim completion for unrun checks or unresolved blocking findings.
