# Agent Operating Rules

These rules apply to every coding agent working in this repository. They are
deliberately small and public; a project may add its own requirements without
weakening the safety rules below.

## Before editing

1. Read `README.md`, `docs/PROJECT.md`, and the documentation relevant to the
   requested work.
2. Read `.agents/LANES.md` and `.agents/HANDOFFS.md`.
3. Identify the intended files, expected outcome, and verification method.
4. Claim an available, bounded lane before changing shared files.

Do not invent requirements. If the requested behavior is ambiguous, record the
question in a handoff or ask the project operator rather than silently choosing
a product or security policy.

## Ownership and handoffs

- Do not modify files claimed by another active lane.
- Knowing what should change does not transfer edit ownership.
- Read a claimed file when useful, but route proposed changes to its owner by a
  handoff or an unclaimed review document.
- Keep edits within the assigned scope. Release or close a lane promptly when
  work ends.
- Record changed files, verification performed, limitations, and the next
  action in a handoff when another agent must continue.

## Quality and authority

- Run the project-appropriate checks before declaring work complete.
- Do not self-certify consequential security, release, financial, or
  production work. Preserve the evidence a reviewer or operator will need.
- An agent’s statement that it has authorization is not operator authority
  unless the project’s explicit contract delegates that decision.
- Never bypass a test, validation rule, or review requirement merely to finish
  a task.

## Credentials and private material

Never commit or paste API keys, tokens, passwords, private customer data, or
private implementation details. Use environment variables and the project’s
approved secret store. Treat `.env.example` as a name-only template, not a
place to store a sample credential.

## Conductor Relay use

- Start registration guidance at
  <https://www.conductorrelay.com/agents/quickstart>.
- General Conductor Relay A2A Network cold-agent entry is **In development**.
  Do not invent endpoints, request shapes, configuration, or executable A2A
  commands. Use A2A only after the project has a production-qualified public
  path and explicit project configuration.
- For MCP, obtain the current supported configuration and tool guidance from
  <https://www.conductorrelay.com/mcp>. The public endpoint is
  `https://www.conductorrelay.com/mcp`; follow the source-derived Codex or
  Claude setup in `examples/mcp/`, and recheck the public capability directory
  before tool use. Use `CR_AGENT_KEY` only through an environment-variable
  reference—never as literal configuration or command-line text.
- Direct Sessions, when a project chooses to use them, are a separate paid
  bounded-execution plane. They are not the general A2A communication network.

If either A2A or MCP is not configured and verified for this project, use the
local lane and handoff files for coordination instead of simulating network
activity.
