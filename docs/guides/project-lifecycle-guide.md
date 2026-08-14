# Project Lifecycle Guide

This guide explains the human-facing workflow entrypoints. The managed [agent guideline](../../canonical-configs/agent-guideline/guideline.md) remains the governance source of truth.

## Install the Workflow

In **Install / Update skills**, install **Development Workflow** and reload the Claude or Codex session. The package installs these entrypoints and their atomic dependencies together:

- `what-next`: inspect repository evidence and identify the appropriate next workflow;
- `work-on-change`: move one bounded Change forward;
- `work-on-phase`: move one exact Roadmap Phase forward;
- `review-change`: adversarially review completed work in a fresh agent context.
- `triage-pending`: classify deferred discoveries without expanding active scope;
- `close-change`: absorb temporary evidence, ask humans which ADR candidates are worth retaining, and create final durable records.

Atomic skills such as `grill-with-docs`, `plan-change`, `implement-task`, `verify-change`, and `report-change` remain independently governed. They are primarily selected by the entrypoints, but advanced users may invoke one directly for a precise rerun.

## Choose the Entry Point

| Intent | Human entrypoint | Expected result |
|--------|------------------|-----------------|
| You do not know the current workflow state or next action | `what-next` | Evidence-based routing without crossing an authority gate |
| An existing project needs one bounded change | `work-on-change` | Planning, approved implementation, verification, and review handoff |
| One exact Roadmap Phase is the delivery target | `work-on-phase` | Governed delivery evidence for that Phase |
| Implementation and current verification are ready | `review-change` in a fresh agent | One risk-prioritized review with stable findings |
| Review disposition and remediation are complete | `close-change` | Absorption, Human ADR Retention Gate, and final `CHANGE.md` |
| Deferred discoveries need classification | `triage-pending` | Destination and blocking-trigger assessment without implementation |

For a new or ambiguous project, start with `what-next`. It can route to decision discovery, project definition, or bootstrap workflows based on repository evidence.

## Typical Greenfield Sequence

```text
what-next
→ decision discovery and project definition
→ Human Project Approval
→ engineering baseline when needed
→ work-on-phase
→ verification and review handoff
→ review-change in a fresh agent
→ human finding disposition and targeted confirmation
→ close-change and Human ADR Retention Gate
→ Human Phase Acceptance
→ commit
→ create-pr
```

Each workflow stops at its own authority boundary. Project approval does not authorize implementation, and Phase acceptance does not authorize commit, push, merge, release, or deployment. `commit` and `create-pr` remain separately invoked skills.

## Example Prompts

### Find the next action

```text
Use what-next. Inspect the repository evidence, tell me the current workflow
state, and route to the next appropriate skill without crossing an approval gate.
```

### Work on one Change

```text
Use work-on-change for <change goal>.
Mode: one-task-at-a-time.
Use existing specifications and approval evidence; stop at the next authority gate.
```

### Work on one Roadmap Phase

```text
Use work-on-phase.
Roadmap: docs/ROADMAP.md
Phase: <exact phase ID or heading>
Mode: one-task-at-a-time
```

The Phase must have an approved observable outcome, scope, acceptance criteria, and satisfied Phase-start Decision Gates. An ambiguous or multi-Phase request must stop for clarification.

### Review in a fresh agent

```text
Use review-change to adversarially review <change path or review handoff>.
Rely on repository evidence rather than the implementer's claims.
```

Formal review must run in a fresh agent context. The implementation agent may self-check its work, but that does not satisfy the independent review gate.

## Advanced Atomic Reruns

Invoke an atomic skill directly only when the required step is already known, for example:

- `plan-change` to revise only the plan;
- `implement-task` to run one approved task;
- `verify-change` to rerun canonical verification;
- `report-change` to regenerate current delivery evidence.
- `report-change` to refresh the compatibility Review Handoff in `CHANGE_WORKING.md`;
- `triage-pending` to classify the Pending inbox;
- `close-change` to converge reviewed evidence after human disposition.

Direct invocation does not bypass admission criteria or approval boundaries.

## 繁體中文摘要

在 **Install / Update skills** 安裝 **Development Workflow** 後，使用者平常只需記住：

- 不知道目前在哪或下一步：`what-next`
- 處理一個明確且有邊界的 Change：`work-on-change`
- 處理唯一指定的 Roadmap Phase：`work-on-phase`
- 實作與驗證完成後，另開新 agent 做一次風險優先的對抗式審查：`review-change`
- 延後發現需要分類：`triage-pending`
- 審查與 remediation 完成後收斂 durable truth：`close-change`

`plan-change`、`implement-task`、`verify-change` 等 atomic skills 仍保持獨立，主要由人類入口根據 repository evidence 選用；進階使用者仍可在已知精確步驟時單獨重跑。安裝整包不代表獲得跨過批准、審查或 Git 權限邊界的授權。
