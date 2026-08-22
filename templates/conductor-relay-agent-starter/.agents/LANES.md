# Active agent lanes

Record active work here before changing a shared project surface.

| Lane | Agent | Scope | Claimed paths | State |
|---|---|---|---|---|
| example-build | example agent | Illustration only | `src/example.ts` | CLOSED |

## States

- `OPEN` — active work; the claimed paths are write-owned by the listed agent.
- `BLOCKED` — work cannot safely proceed; retain the claim and record the
  blocker in a handoff.
- `CLOSED` — work is complete and the claim is released.

## Rules

1. Claim a lane before editing a shared file. Keep the scope and path list
   specific.
2. There is one active write owner for each claimed path. Others may read the
   file, but must not edit it until the claim is released or explicitly
   transferred.
3. Knowing what should change does not grant edit ownership. Operator authority
   likewise does not automatically transfer a lane claim.
4. Use a narrow, unclaimed handoff file when the owner needs input; do not edit
   around an active claim.
5. Record verification, limitations, and the next action in a handoff before
   closing or transferring material work.
6. Release claims promptly by marking them `CLOSED`.

Copy [templates/lane-claim.md](templates/lane-claim.md) for a new claim, then
add its essential fields to the table above.
