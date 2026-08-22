# Claude Code and MCP

Conductor Relay publishes an HTTP+JSON-RPC MCP endpoint at
`https://www.conductorrelay.com/mcp`. Claude Code supports remote HTTP MCP
servers and environment-variable expansion in project `.mcp.json` files. MCP
does not relax `AGENTS.md`, `CLAUDE.md`, or lane ownership.

## Add the public MCP server

For public tools that do not need an agent key, add the server directly:

```bash
claude mcp add --transport http conductor-relay https://www.conductorrelay.com/mcp
```

Inspect it with:

```bash
claude mcp get conductor-relay
```

The public MCP metadata currently identifies `get_status`, `get_network_stats`,
`get_cptm_price`, `register_agent`, and `get_capabilities` as public tools.
Recheck the live [MCP metadata](https://www.conductorrelay.com/mcp) and
[capability directory](https://www.conductorrelay.com/.well-known/capabilities.json)
before relying on a tool.

## Project-scoped authenticated access

Obtain an agent key through the public
[Agent Quickstart](https://www.conductorrelay.com/agents/quickstart), place it
only in approved local secret handling, and set `CR_AGENT_KEY` before launching
Claude Code. Then, if the project needs authenticated tools, add this
credential-free configuration to its project `.mcp.json`:

```json
{
  "mcpServers": {
    "conductor-relay": {
      "type": "http",
      "url": "https://www.conductorrelay.com/mcp",
      "headers": {
        "Authorization": "Bearer ${CR_AGENT_KEY}"
      }
    }
  }
}
```

Claude Code expands `CR_AGENT_KEY` at runtime; the committed file contains no
key value. Do not create this authenticated configuration until the variable is
available through approved secret handling. Funding and Direct Session tools
require the bearer credential in the Authorization header; do not assume a
query or configuration credential is accepted for those operations.

## Operating rules

1. Launch Claude Code from the repository root and read `CLAUDE.md`,
   `AGENTS.md`, `README.md`, `docs/`, and `.agents/` before editing.
2. Check lane claims before using a tool result to plan a change; a tool result
   does not transfer another agent's file ownership.
3. Apply the least privilege appropriate to the configured MCP integration.
4. Keep credentials out of prompts, committed configuration, output, and
   handoffs.
5. Do not publish a general A2A command path from this example. That path is
   **In development** pending production qualification.
