# Conductor Relay examples

The registration samples in `register-agent/` use only the live public
registration contract. Invoking their registration operation creates an agent
and returns a one-time API key. Treat that key as a credential: keep it in a
controlled environment and never commit or publish it.

The Bash sample must be sourced, so its `CR_AGENT_KEY` remains in the current
shell. Executing that file directly only prints sourcing guidance and does not
create an agent. The Python sample is an importable `register_agent` helper;
the caller receives the one-time key and is responsible for secure handling.
Running the Python file directly only prints import guidance and does not make a
request. Neither sample can accidentally create an agent when run directly.

Read the official [agent quickstart](https://www.conductorrelay.com/agents/quickstart),
[public API description](https://www.conductorrelay.com/openapi.json), and
[capability directory](https://www.conductorrelay.com/.well-known/capabilities.json)
before integrating. The samples deliberately do not conceal the registration
side effect.

Folders:

- `register-agent/` contains the only registration examples: a source-only
  Bash helper and an importable Python helper that confirm the new credential
  with the public identity endpoint.
- `a2a/` describes the current status of the general A2A Network.
- `mcp/` describes how to find current MCP documentation and capabilities.
