#!/usr/bin/env python3
"""Validate the public Grok plugin and published MCP/A2A contract snapshot."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "conductor-relay"
PUBLIC_ROOTS = (
    ROOT / "README.md",
    ROOT / ".github",
    ROOT / "assets",
    ROOT / "docs",
    ROOT / "examples",
    ROOT / "templates",
    ROOT / "plugins",
)
INVENTORY_DOCUMENTS = (
    ROOT / "README.md",
    ROOT / "docs" / "mcp.md",
    ROOT / "templates" / "conductor-relay-agent-starter" / "README.md",
    PLUGIN / "README.md",
)
LIVE_A2A_DOCUMENTS = (
    ROOT / "README.md",
    ROOT / "docs" / "a2a-network.md",
    ROOT / "templates" / "conductor-relay-agent-starter" / "README.md",
    ROOT / "templates" / "conductor-relay-agent-starter" / "docs" / "A2A.md",
    PLUGIN / "README.md",
)
SELF_HOSTED_DOCUMENTS = (
    ROOT / "docs" / "a2a-network.md",
    ROOT / "templates" / "conductor-relay-agent-starter" / "docs" / "A2A.md",
    ROOT
    / "templates"
    / "conductor-relay-agent-starter"
    / "examples"
    / "a2a"
    / "receive-message.md",
)
EXPECTED_TOOLS = (
    "register_agent",
    "get_balance",
    "request_sandbox_funds",
    "create_funding_checkout",
    "get_funding_status",
    "a2a_enroll",
    "a2a_find_agents",
    "a2a_send_message",
    "a2a_get_messages",
    "a2a_reply",
    "list_direct_offers",
    "get_direct_usage",
    "get_direct_limits",
    "publish_direct_offer",
    "verify_direct_offer",
    "create_direct_provider_verification_challenge",
    "set_direct_offer_status",
    "create_direct_signing_key_challenge",
    "register_direct_signing_key",
    "revoke_direct_signing_key",
    "create_worker_delegation",
    "revoke_worker_delegation",
    "open_direct_session",
    "list_direct_session_requests",
    "approve_direct_session",
    "reject_direct_session",
    "get_direct_session",
    "send_direct_message",
    "submit_direct_receipt",
    "close_direct_session",
    "list_jobs",
    "claim_job",
    "submit_job_result",
    "resolve_commercial_intent",
    "get_status",
    "get_network_stats",
    "get_cptm_price",
    "get_capabilities",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def public_text_files() -> list[Path]:
    files: list[Path] = []
    for root in PUBLIC_ROOTS:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and path.suffix in {".md", ".svg", ".yml"}
            )
    return files


def load(relative: str) -> dict[str, object]:
    path = PLUGIN / relative
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {error.msg}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain an object")
    return value


def validate_public_status() -> None:
    for path in public_text_files():
        text = path.read_text(encoding="utf-8")
        if re.search(r"\bin development\b", text, flags=re.IGNORECASE):
            fail(f"stale 'In development' status in {path.relative_to(ROOT)}")
    for path in LIVE_A2A_DOCUMENTS:
        text = path.read_text(encoding="utf-8")
        if "Live" not in text or "A2A" not in text:
            fail(f"{path.relative_to(ROOT)} must identify A2A as Live")
    for path in SELF_HOSTED_DOCUMENTS:
        text = path.read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        if "already-owned eligible registered runtime" not in normalized:
            fail(
                f"{path.relative_to(ROOT)} must qualify self-hosted enrollment "
                "as requiring an already-owned eligible registered runtime"
            )


def validate_inventories() -> None:
    if len(EXPECTED_TOOLS) != 38 or len(set(EXPECTED_TOOLS)) != 38:
        fail("expected MCP inventory must contain 38 unique tool names")
    for path in INVENTORY_DOCUMENTS:
        if not path.is_file():
            fail(f"missing inventory document {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        missing = [tool for tool in EXPECTED_TOOLS if f"`{tool}`" not in text]
        if missing:
            fail(f"{path.relative_to(ROOT)} omits MCP tools: {', '.join(missing)}")


def validate_plugin() -> None:
    manifest = load(".grok-plugin/plugin.json")
    if manifest.get("name") != "conductor-relay":
        fail("plugin manifest name must be conductor-relay")
    if manifest.get("license") != "MIT":
        fail("plugin manifest must declare MIT")
    if manifest.get("homepage") != "https://www.conductorrelay.com":
        fail("plugin manifest must use the public Conductor Relay homepage")
    if manifest.get("repository") != (
        "https://github.com/Zman504/Zman504-conductor-relay-public"
    ):
        fail("plugin manifest must use the published repository")

    config = load(".mcp.json")
    servers = config.get("mcpServers")
    expected = {
        "conductor-relay": {
            "type": "http",
            "url": "https://www.conductorrelay.com/mcp",
        }
    }
    if servers != expected:
        fail("MCP config must contain only the public Conductor Relay endpoint")

    files = ("README.md", "skills/conductor-relay/SKILL.md")
    for relative in files:
        if not (PLUGIN / relative).is_file():
            fail(f"missing plugins/conductor-relay/{relative}")

    source = "\n".join(
        (PLUGIN / relative).read_text(encoding="utf-8")
        for relative in (".mcp.json", *files)
    )
    for forbidden in ("cr_agent_", "api_key", "curl |", "hooks"):
        if forbidden in source:
            fail(f"plugin source must not embed {forbidden!r}")


def main() -> None:
    validate_public_status()
    validate_inventories()
    validate_plugin()
    print("PASS: public A2A, MCP inventory, and Grok plugin contract are coherent")


if __name__ == "__main__":
    main()
