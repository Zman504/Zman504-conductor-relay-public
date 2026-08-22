# Claude Project Instructions

Claude follows the shared [AGENTS.md](AGENTS.md) contract as well as these
role-specific instructions.

## Before making a change

1. Read `README.md`, `AGENTS.md`, `docs/PROJECT.md`, and the relevant project
   documentation.
2. Check `.agents/LANES.md` for an active owner of every file you need.
3. Claim a bounded lane before editing shared project surfaces.
4. State the intended files and verification in the lane record or handoff.

## Respect the lane boundary

- Do not override another agent’s active claim.
- If another lane owns a necessary file, write a focused request in an
  unclaimed handoff path or use the project’s configured communication channel.
- A request from another agent does not itself grant edit ownership or operator
  authority.
- Review work may be recorded in a separate unclaimed document; do not change
  the implementation owner’s files without a transfer or closed claim.

## Complete work responsibly

Run the appropriate verification, then record files changed, commands or checks
run, limitations, and the next action. Do not claim release, security, or
production approval without the project’s designated human decision.

## Conductor Relay boundary

Use the public [Agent Quickstart](https://www.conductorrelay.com/agents/quickstart)
as the starting point for registration guidance. The general A2A Network
cold-agent entry path is **In development**, so this repository intentionally
contains no A2A endpoint, request body, or executable setup. Do not manufacture
one. Use local handoffs until the project has a production-qualified public A2A
configuration.

For MCP tool use, first consult the current public documentation at
<https://www.conductorrelay.com/mcp>. The published endpoint is
`https://www.conductorrelay.com/mcp`. Use the source-derived
[`examples/mcp/claude.md`](examples/mcp/claude.md) configuration only after
`CR_AGENT_KEY` is available through the approved secret handling; the guide
uses environment-variable expansion and contains no literal credential. Check
the [capability directory](https://www.conductorrelay.com/.well-known/capabilities.json)
before relying on a particular tool.

Direct Sessions are separate optional paid bounded execution; they are not the
general A2A communication network.

## Credentials

Never place credentials in prompts, source files, handoffs, logs, or commits.
Use environment variables and the project’s approved secret handling. A blank
variable in `.env.example` is not a credential value.
