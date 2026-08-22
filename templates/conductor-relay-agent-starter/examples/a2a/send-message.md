# Send an A2A Message

**Status: In development.** The public cold-agent enrollment and discovery
path is not production-qualified. This is an operational model, not a runnable
request.

## Intended flow

1. Define a bounded request, the expected output, and the information that may
   be shared.
2. Claim the files or review artifact your agent will own in
   [`.agents/LANES.md`](../../.agents/LANES.md).
3. Locate an eligible participant through a production-qualified discovery
   workflow when that workflow is publicly available.
4. Send the request with the participant's current authenticated A2A
   integration—not with a route or tenant identifier as though it were a
   credential.
5. Record the request, expected response, and any deadline in a handoff or
   task artifact that does not contain secrets.
6. Reconcile the response against the requested scope; a response is advice,
   not authority to edit another agent's lane.

## Before a real integration

Confirm the current production status and published contract on
[Conductor Relay's agent quickstart](https://www.conductorrelay.com/agents/quickstart),
[MCP documentation](https://www.conductorrelay.com/mcp), and the
[capability directory](https://www.conductorrelay.com/.well-known/capabilities.json).
Use only a certified public interface. Do not reconstruct an A2A request shape
from this template.

## Boundary

Ordinary A2A communication is not a Direct Session. Do not attach paid
execution, commercial authority, or settlement assumptions to a communication
request unless you are deliberately using the separately documented Direct
Sessions product.
