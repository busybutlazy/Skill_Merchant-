# Work on Phase

## Objective

Provide the human-friendly entrypoint for moving one exact Roadmap Phase forward without requiring the user to remember the underlying phase-delivery skill name.

## Workflow

1. Require the Roadmap path and one uniquely matching Phase ID or heading. Never infer “the next phase,” accept multiple phases, or silently choose an ambiguous heading.
2. Inspect Phase-start Decision Gates and current phase artifacts. Report the selected Phase, observed state, next action, and next human gate.
3. Delegate the governed planning, approved execution, verification, reporting, and review handoff to the installed `deliver-roadmap-phase` workflow.
4. Preserve every admission criterion, checkpoint, stop condition, Human Phase Acceptance boundary, and Git/release authority boundary defined by that workflow.

This facade grants no additional authority. It must not fill missing requirements by assumption, weaken an atomic workflow, review its own implementation, advance Roadmap completion state without explicit acceptance, or implicitly commit, push, merge, release, or deploy.
