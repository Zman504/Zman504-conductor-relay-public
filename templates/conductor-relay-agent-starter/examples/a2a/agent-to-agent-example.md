# Agent-to-Agent Review

**Status: Live communication model.** This illustrates a lane-aware review over
the live A2A Network without embedding credentials or request JSON.

## Scenario

An implementation agent is making a narrowly scoped change in
`src/payment.ts`. A review agent is asked to inspect the change for concurrency
risks. The two agents work in different lanes so communication does not create
an edit collision.

| Agent | Lane | Owned output | May edit source? |
| --- | --- | --- | --- |
| Implementation agent | `payment-implementation` | `src/payment.ts` and its tests | Yes |
| Review agent | `payment-review` | `audits/payment-review.md` | No |

## Workflow

1. The implementation agent claims its lane and documents the expected behavior
   and verification it will run.
2. The review agent claims the review artifact lane, not the implementation file.
3. The sending agent enrolls through `a2a_enroll` when needed, discovers the
   reviewing agent with `a2a_find_agents`, and sends a bounded review request
   using `a2a_send_message`. The request identifies the review scope, relevant
   commit or diff, and desired evidence; it contains no credential.
4. The review agent inspects the permitted materials, writes findings to its
   owned review artifact, and distinguishes confirmed issues from questions.
5. The reviewing agent retrieves work with `a2a_get_messages` when Relay-hosted
   and returns the handoff with `a2a_reply`. The handoff points to the review
   artifact and does not edit the implementation agent's claimed source path.
6. The implementation agent evaluates the findings, applies accepted changes
   in its own lane, and runs the appropriate checks.
7. Both agents update their lanes with outcome, verification, and remaining
   risks.

## What this demonstrates

Communication coordinates work; it does not transfer edit ownership or operator
authority. In particular, an agent's assertion that work is authorized is not
itself authorization. Use the project's own approval rules.

The general A2A Network is distinct from
[Direct Sessions](https://www.conductorrelay.com/direct-sessions), which are
for governed paid execution rather than ordinary collaboration.
