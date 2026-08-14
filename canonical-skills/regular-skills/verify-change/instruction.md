# Verify Change

## Objective

Produce reproducible evidence for an implemented Change. Verification is evidence-only; its default destination is the Verification Evidence section of `CHANGE_WORKING.md`, not another permanent report.

## Required Inputs

Require Change ID, request/acceptance, current working record or approved legacy plan, attributable diff, and existing canonical format/lint/type/unit/integration/contract/E2E/build/security commands. Missing acceptance or an attributable diff is a blocker. Missing container support routes to `bootstrap-project`; never run project tools on the host.

## Workflow

1. Map consequential requirements to implementation and candidate tests.
2. Record environment, services, mocks, baseline failures, and whether any command can spend money, mutate persistent data, use secrets, or reach production. Such commands require prior explicit authority.
3. Run risk-applicable canonical commands through Docker/Compose/Make/container wrappers.
4. Record each exact command once with exit, relevant counts/result, skips, and uncertainty. Do not copy volatile totals into multiple summaries.
5. Distinguish automated evidence, manual observation, inference, and unsupported claim.
6. Append results to `CHANGE_WORKING.md` using [the template](./references/VERIFICATION_REPORT_TEMPLATE.md). Produce a standalone `VERIFICATION_REPORT.md` only when audit policy or the user explicitly requires it.
7. Capture valid out-of-scope discoveries in `docs/PENDING.md` without implementing them.
8. Stop with Pass/Fail/Incomplete. Do not edit implementation while in verification mode.

After a failure, a separate implementation step may use an already approved remediation envelope; all affected and required checks must then be rerun. Verification itself never silently repairs a failure.

## Evidence Standard

Prioritize executable evidence. Trace only consequential acceptance criteria; do not manufacture rows for trivial statements. List unrun tests, mock boundaries, known risk, review hotspots, and claims not proved.
