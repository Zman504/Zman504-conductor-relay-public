# Project guide

Use this repository as a language-neutral starting point for a project with
one or more coding agents. Put application code under [`../src`](../src) and
replace these generic documents with project-specific decisions as the project
matures.

## Working agreement

1. Read the repository README, `AGENTS.md`, `CLAUDE.md`, and relevant project
   documents before editing.
2. Claim shared paths in [`.agents/LANES.md`](../.agents/LANES.md) before
   modifying them. The claim establishes edit ownership, not broad authority.
3. Keep changes bounded to the assigned task. Record material work in a
   handoff with evidence, limitations, and a next action.
4. Run verification appropriate to the change. A passing command is evidence,
   not permission to publish, deploy, or handle credentials.

## Conductor Relay touchpoints

Use only the public onboarding material for the platform:

- [Agent Quickstart](https://www.conductorrelay.com/agents/quickstart) for the
  currently published registration guidance.
- [MCP documentation](https://www.conductorrelay.com/mcp) for the current
  client configuration and available tools.

Never copy keys into this repository. If a project uses an agent key, keep it
in a local, ignored environment and follow the public quickstart’s handling
guidance.

The general Conductor Relay A2A Network is **In development**. See
[A2A.md](A2A.md); this starter intentionally does not provide a runnable A2A
enrollment, discovery, or message command.
