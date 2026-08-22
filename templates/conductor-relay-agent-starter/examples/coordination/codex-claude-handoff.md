# Codex–Claude Lane-Aware Handoff

This example keeps a cross-agent review useful without letting two agents edit
the same work surface.

## Example assignment

| Role | Owner | Lane | Write scope |
| --- | --- | --- | --- |
| Implementation | Codex | `invoice-implementation` | `src/invoice.ts`, relevant tests |
| Review | Claude | `invoice-review` | `audits/invoice-review.md` |

Codex owns the implementation. Claude owns a review record. Claude may inspect
the agreed material but does not edit Codex's claimed files. If a review needs a
source change, the finding is returned to Codex; it is not silently applied by
the review lane.

## Handoff sequence

1. Codex records its lane claim, intended behavior, and verification plan in
   [`.agents/LANES.md`](../../.agents/LANES.md).
2. Claude records a separate review lane and the path of its review artifact.
3. Codex shares the bounded review context through an approved project channel.
   When a production-qualified A2A integration is configured, that channel may
   be Conductor Relay A2A; the general cold-agent path is currently **In
   development**.
4. Claude writes a review artifact containing the scope reviewed, concrete
   findings, evidence, questions, and limitations. It excludes secrets and
   unneeded private material.
5. Claude returns a handoff that points to the artifact and states that Codex
   retains implementation ownership.
6. Codex independently evaluates the findings, makes any accepted repairs, and
   runs the relevant checks.
7. Both lanes record the outcome and close or mark themselves blocked.

## Minimal handoff record

Use [the reusable handoff template](../../.agents/templates/handoff.md) for the
record. A completed handoff should identify:

- the sender and receiving lane;
- the bounded request and reviewed inputs;
- the artifact path or immutable reference;
- findings, evidence, and limitations;
- verification performed; and
- the next owner and remaining decision, if any.

## Authority boundary

An agent can request, review, and report. It cannot grant itself permission to
change protected scope, override a lane owner, or treat another agent's claim of
operator approval as operator authority.

MCP can assist only through the configuration and tools documented at
[conductorrelay.com/mcp](https://www.conductorrelay.com/mcp). Direct Sessions
remain a separate paid-execution plane, not the general A2A Network.
