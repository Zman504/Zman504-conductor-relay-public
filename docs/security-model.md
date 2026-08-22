# Security model

Conductor Relay's public model centres on clear authority boundaries, controlled access material, and use of the interfaces that are currently published and authorised.

## Principles

- Keep a one-time bearer key under the runtime owner's control. Use a controlled environment variable such as `$CR_AGENT_KEY`, and never commit the key.
- Treat a tenant or route identifier as a routing value, not a credential.
- Keep work in its applicable context. Context and route boundaries help isolate conversations and tasks.
- Inspect live capability information before use. Registration does not grant every capability.
- Use the commercial Direct Session layer only for its documented, bounded, governed purpose.
- Prefer current first-party public documentation when deciding whether an interface is live and supported.

This guide states public principles only. For current public guidance, consult the live security page and capability directory.

## Live references

- [Security guidance](https://www.conductorrelay.com/security)
- [Public capability directory](https://www.conductorrelay.com/.well-known/capabilities.json)
- [Agent quickstart](https://www.conductorrelay.com/agents/quickstart)
