# Triage Pending

## Objective

Triage project discoveries that were valid but out of scope when found. `docs/PENDING.md` is a controlled inbox, not a Roadmap, FIFO task queue, decision record, or permission to implement.

## Use When

- Pending items are untriaged, their blocking trigger may be due, or planning needs their disposition.
- `what-next`, Phase planning, or Change closure needs to know where a discovery belongs.

Do not use to invent a solution, make a product/architecture decision, expand an active Change, or implement backlog work.

## Pending Item Contract

Use [the format](./references/PENDING_FORMAT.md). Every item needs a stable ID, evidence, source, reason deferred, potential consequence, blocking trigger, suggested destination, owner, and status:

- `untriaged`
- `triaged`
- `scheduled`
- `blocking`
- `absorbed`
- `dismissed`

## Workflow

1. Read `docs/PENDING.md`, repository rules, current specifications/contracts, ADR index and relevant ADRs, Roadmap, active Changes, and current code evidence.
2. Revalidate each selected item. Merge duplicates under one stable ID and preserve source references.
3. Decide the information destination, not the technical solution:
   - product behavior → specification or a decision gate;
   - external contract/schema → contract source;
   - long-lived architecture tradeoff → ADR candidate;
   - bounded executable work → future Change;
   - cross-Phase outcome → Roadmap;
   - operational recovery → runbook;
   - temporary limitation → final Change record;
   - no longer valid or not worth carrying → dismissed with rationale.
4. Evaluate the recorded blocking trigger against current evidence. Only a due trigger or a direct contradiction of the next workflow may block it.
5. For a consequential unresolved choice, stop and route to `grill-with-docs`; do not choose it during triage.
6. For an ADR candidate, explain why existing durable sources are insufficient and place it in a later Human Retention Packet. Do not create or accept an ADR.
7. Update statuses and destinations in `docs/PENDING.md`. Compact absorbed/dismissed items or rely on Git history according to repository policy.
8. Return counts for blocking, untriaged, relevant-to-next-action, and unrelated items. Unrelated items do not block current work.

## Capture Boundary

Other workflow skills may add a bounded Pending item without expanding their Change scope. Capture evidence and consequence only; never smuggle a proposed solution in as an approved decision.

## Authority Boundary

This skill may edit only the Pending inbox and, when explicitly authorized, move already-decided text to its approved durable destination. It does not approve decisions, create Accepted ADRs, edit production code, schedule a Roadmap item without human authority, or commit/push/merge/release/deploy.
