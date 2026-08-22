# Conceptual architecture

This template separates four concerns so that coordination does not become an
implicit production system:

```text
Project instructions      → shared operating rules and project boundaries
Lane record               → one active write owner per claimed path
Handoffs                  → findings, evidence, limitations, next action
Application source        → your implementation under src/
```

Codex, Claude, and human contributors read the same project-level rules. They
coordinate through the lane and handoff documents regardless of whether an
external communication integration is configured.

## Optional Conductor Relay interfaces

```text
Coding agents ── project files / lanes / handoffs ── application work
      │
      └── MCP (when configured from public documentation)
      └── A2A Network (In development; no runnable flow in this template)
```

MCP is a tool-access interface. Follow the current configuration instructions
at <https://www.conductorrelay.com/mcp>. The source-derived Codex and Claude
examples in [`../examples/mcp`](../examples/mcp) use the published endpoint and
environment-variable authorization pattern; they do not guess tool-call
payloads or embed a credential.

The A2A Network is a communication plane, not a substitute for repository lane
ownership. Its general public cold-entry path is **In development**. The
conceptual model is described in [A2A.md](A2A.md), without endpoints or wire
contracts.

Direct Sessions, if a project elects to use them, are an optional paid,
bounded-execution plane. They are not the general A2A communication network.
