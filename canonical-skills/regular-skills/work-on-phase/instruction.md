# Work on Phase

## Objective

Move one exact Roadmap Phase forward while keeping Phase planning temporary and child Change results durable only after closure.

## Workflow

1. Require a Roadmap path and one uniquely matching Phase ID/heading. Never infer the next Phase or accept multiple phases.
2. Inspect Phase Decision Gates, relevant blocking/untriaged Pending items, child Change closure state, and current phase artifacts.
3. Report selected Phase, observed state, relevant Pending IDs, next action, and next human gate.
4. Delegate governed delivery to `deliver-roadmap-phase` without weakening its criteria.
5. A Phase closes only after required child Changes have final durable records, due Decision Gates are resolved, phase outcomes are verified, temporary phase artifacts are absorbed, and Human Phase Acceptance occurs.

This facade grants no implementation, review, retention, ADR acceptance, Git, release, or deployment authority.
