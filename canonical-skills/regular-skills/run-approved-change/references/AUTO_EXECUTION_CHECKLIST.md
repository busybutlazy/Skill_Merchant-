# Supervised-Auto Checklist

## Admission

- [ ] Stable Change ID and `CHANGE_WORKING.md` exist.
- [ ] Current approval or low-risk lightweight admission is recorded.
- [ ] Risk is low/medium and mode is `supervised-auto`.
- [ ] Outcomes/tasks, paths, checkpoints, verification, rollback, and remediation envelope are explicit.
- [ ] No prohibited high-risk operation is included.
- [ ] Git state is attributable and canonical container entrypoints exist.

## Per-Outcome Evidence

Append only this delta to the working record:

```markdown
### <task/outcome ID>
- Result and files:
- Container commands/exits:
- Tests omitted and consequence:
- Deviation or Pending item: none / <details>
```

## Completion

- [ ] All approved outcomes passed.
- [ ] Current full verification is recorded once.
- [ ] Review Handoff identifies diff base, limitations, Pending and ADR candidates.
- [ ] Independent review, retention, closure, acceptance, and Git/release actions remain unperformed.
