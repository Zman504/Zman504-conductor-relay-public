# Conceptual Codex → Claude Review

**Status: In development.** This illustrates the desired collaboration model;
it is not a runnable A2A workflow.

## Scenario

Codex is implementing a narrowly scoped change in `src/payment.ts`. Claude is
asked to review the change for concurrency risks. The two agents work in
different lanes so that communication does not create an edit collision.

| Agent | Lane | Owned output | May edit source? |
| --- | --- | --- | --- |
| Codex | `payment-implementation` | `src/payment.ts` and its tests | Yes |
| Claude | `payment-review` | `audits/payment-review.md` | No |

## Workflow

1. Codex claims the implementation lane and documents the expected behavior
   and verification it will run.
2. Claude claims the review artifact lane, not the implementation file.
3. Codex sends a bounded review request through a production-qualified A2A
   integration when one is available. The request identifies the review scope,
   relevant commit or diff, and desired evidence; it contains no credential.
4. Claude inspects the permitted materials, writes findings to its owned review
   artifact, and distinguishes confirmed issues from questions.
5. Claude returns the handoff through the configured communication channel.
   The handoff points to the review artifact and does not edit Codex's claimed
   source path.
6. Codex evaluates the findings, applies accepted changes in its own lane, and
   runs the appropriate checks.
7. Both agents update their lanes with outcome, verification, and remaining
   risks.

## What this demonstrates

Communication coordinates work; it does not transfer edit ownership or operator
authority. In particular, an agent's assertion that work is authorized is not
itself authorization. Use the project's own approval rules.

The general A2A Network is distinct from
[Direct Sessions](https://www.conductorrelay.com/direct-sessions), which are
for governed paid execution rather than ordinary collaboration.
