# Examples

These examples show how to organize a multi-agent project without pretending
that unpublished interfaces are ready to use. They are guides, not executable
integration code.

| Area | Status | What this starter provides |
| --- | --- | --- |
| A2A Network | In development | Conceptual sending, receiving, and review workflows. |
| MCP | Live public documentation | Client-specific setup guidance that links to the current public contract. |
| Codex and Claude coordination | Ready to adapt | A lane-aware review and handoff example. |

## Start here

- Read [A2A concepts](a2a/agent-to-agent-example.md) before planning a
  cross-agent request. The general cold-agent entry path is not yet
  production-qualified, so these pages intentionally contain no command,
  endpoint, request body, or client configuration.
- Use [Codex MCP guidance](mcp/codex.md) or [Claude MCP guidance](mcp/claude.md)
  when your team has access to the public MCP surface. The live source of truth
  is [the MCP documentation](https://www.conductorrelay.com/mcp); use the
  [capability directory](https://www.conductorrelay.com/.well-known/capabilities.json)
  to inspect the current public listing.
- Follow the [Codex-to-Claude handoff](coordination/codex-claude-handoff.md)
  when an implementation lane needs independent review without transferring
  edit ownership.

## Credentials

Keep credentials in a secure local secret store or process environment. Do not
place them in this repository, examples, screenshots, terminal transcripts, or
handoff notes.

## Plane separation

The A2A Network is the communication plane. Direct Sessions are a separate,
governed paid-execution plane; they are not the general A2A Network. See the
[public Direct Sessions page](https://www.conductorrelay.com/direct-sessions)
for its current documentation.
