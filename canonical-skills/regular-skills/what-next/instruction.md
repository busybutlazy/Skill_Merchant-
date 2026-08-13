# What Next

## Objective

Tell the user where the repository is in the governed development lifecycle and select the safest next human-facing workflow entrypoint. This is the installation root for the Development Workflow bundle, not a super-skill with authority to run every stage.

## Workflow

1. Inspect repository evidence without modifying production code: project rules, specifications, contracts, ADRs, Roadmap, `changes/`, reports, Git state, and available container commands.
2. State only what the artifacts prove:

   ```text
   Current state: <observed lifecycle/change/phase state>
   Evidence: <key paths>
   Next entrypoint: <skill or human action>
   Next gate: <approval, decision, review, or acceptance>
   ```

3. Choose the first matching route:
   - Consequential choices remain unresolved: `grill-with-docs` through the applicable project or Change workflow.
   - Decisions are ready but a new project lacks approval-ready definition: `define-project`.
   - A greenfield Project Definition is approved but lacks its engineering baseline: `bootstrap-project`.
   - One bounded Change should move forward: `work-on-change`.
   - One exact approved Roadmap Phase should move forward: `work-on-phase`.
   - Completed implementation needs adversarial review: ask the user to open a fresh agent and invoke `review-change` directly.
   - Git or PR work is requested: require a separate explicit `commit` or `create-pr` invocation and authority.
4. If evidence is ambiguous, report the smallest missing fact instead of guessing a route.

## Rules

- Do not treat the presence of a file as proof of human approval unless the repository's approval mechanism says so.
- Do not automatically cross a Human Approval, Decision Gate, independent review, Phase Acceptance, Git, release, or deployment boundary.
- Do not execute multiple human entrypoints merely because they are installed as dependencies.
- Keep `review-change` independently invocable so it can run in a clean adversarial context.
