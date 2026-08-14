# Bootstrap Working Artifact

Create one temporary `changes/<change-id>/CHANGE_WORKING.md` only after the approved bootstrap plan permits it.

```markdown
# Bootstrap Working Record: <change-id>

## Status and Approval
## Goal, Scope, and Exact Approved Files
## Stack, Image, Package/Lock, and Canonical Commands
## Risks, Checkpoints, and Rollback
## Execution Evidence
## Verification Evidence
## Review Handoff
- Diff base and completion claim
- Unsupported or unverified claims
- Pending candidates
- Durable-decision / ADR candidates for Human Retention
```

After independent review and human disposition, use `close-change` to absorb durable rules into Docker/CI files, agent rules, project documentation, Pending, and—only after explicit human retention approval—ADRs. Final `CHANGE.md` replaces the temporary record; do not preserve five duplicate reports by default.
