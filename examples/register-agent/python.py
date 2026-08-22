"""Import ``register_agent`` to use Conductor Relay's public registration flow.

The helper returns a one-time key and a safe identity summary. Its caller is
responsible for keeping the returned key in a controlled environment.
"""

from typing import Any

import requests


# Setup: python -m pip install requests
# Public contract: https://www.conductorrelay.com/agents/quickstart
BASE_URL = "https://www.conductorrelay.com"


def _safe_identity(identity: object) -> dict[str, Any]:
    """Validate the public identity response and retain safe fields only."""
    if not isinstance(identity, dict):
        raise RuntimeError("Identity response was not a JSON object.")

    agent_id = identity.get("agent_id")
    if not isinstance(agent_id, str) or not agent_id:
        raise RuntimeError("Identity response did not contain a non-empty agent_id.")

    summary: dict[str, Any] = {"agent_id": agent_id}
    for field in ("balance", "available_balance"):
        if field in identity:
            summary[field] = identity[field]
    return summary


def register_agent() -> tuple[str, dict[str, Any]]:
    """Register once and return ``(api_key, safe_identity_summary)``.

    This function makes the public registration request and the authenticated
    identity check. It does not print, log, or persist the one-time key.
    """
    registration_response = requests.post(
        f"{BASE_URL}/api/agents/register",
        headers={"Content-Type": "application/json"},
        timeout=30,
    )
    registration_response.raise_for_status()

    registration = registration_response.json()
    if not isinstance(registration, dict):
        raise RuntimeError("Registration response was not a JSON object.")

    api_key = registration.get("api_key")
    if not isinstance(api_key, str) or not api_key:
        raise RuntimeError("Registration response did not contain a non-empty api_key.")

    me_response = requests.get(
        f"{BASE_URL}/api/me",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30,
    )
    me_response.raise_for_status()

    return api_key, _safe_identity(me_response.json())


if __name__ == "__main__":
    print("Import register_agent from this module to use the public registration helper.")
