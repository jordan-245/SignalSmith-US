"""Telegram formatting + sending helpers.

We use parse_mode=HTML because it's predictable and doesn't require escaping
characters like MarkdownV2.

- text_to_html(): turns a plain-text multiline message into nicer HTML.
- send_telegram(): sends with disable_web_page_preview.

All HTML special chars are escaped.
"""

from __future__ import annotations

import html
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import requests


def text_to_html(text: str) -> str:
    """Best-effort conversion of a plain text message to readable Telegram HTML."""
    lines = (text or "").splitlines()
    if not lines:
        return ""

    out: list[str] = []
    for i, raw in enumerate(lines):
        ln = raw.rstrip("\n")
        if not ln.strip():
            out.append("")
            continue

        # escape first
        esc = html.escape(ln)

        # heuristic formatting
        if i == 0:
            out.append(f"<b>{esc}</b>")
        elif esc.startswith("- "):
            out.append(f"• {esc[2:]}")
        else:
            out.append(esc)

    return "\n".join(out)


def _fallback_chat_id_from_openclaw_config() -> str:
    """Fallback for chat_id when TELEGRAM_CHAT_ID isn't set.

    We prefer explicit TELEGRAM_CHAT_ID because bots may post to a group/channel.
    But for ops alerts, DMing the first allowlisted user is better than silence.
    """
    # OpenClaw default config location (see gateway.config.get)
    candidates = [
        os.getenv("OPENCLAW_CONFIG_PATH", ""),
        str(Path.home() / ".openclaw" / "openclaw.json"),
        "/root/.openclaw/openclaw.json",
    ]
    for p in candidates:
        if not p:
            continue
        path = Path(p)
        if not path.exists():
            continue
        try:
            cfg = json.loads(path.read_text(encoding="utf-8"))
            allow_from = (((cfg.get("channels") or {}).get("telegram") or {}).get("allowFrom") or [])
            if allow_from:
                return str(allow_from[0])
        except Exception:
            continue
    return ""


def get_default_chat_id() -> str:
    """Return TELEGRAM_CHAT_ID if set, otherwise a best-effort fallback."""
    return os.getenv("TELEGRAM_CHAT_ID", "") or _fallback_chat_id_from_openclaw_config()


def send_telegram(
    text: str,
    *,
    token: Optional[str] = None,
    chat_id: Optional[str] = None,
    timeout: int = 15,
    warn_if_missing: bool = False,
) -> None:
    bot_token = token or os.getenv("TELEGRAM_BOT_TOKEN", "")
    to = chat_id or os.getenv("TELEGRAM_CHAT_ID", "")
    if not to:
        to = _fallback_chat_id_from_openclaw_config()
        if to and warn_if_missing:
            print(f"[telegram] TELEGRAM_CHAT_ID missing; falling back to DM allowFrom[0]={to}")

    if not bot_token or not to:
        if warn_if_missing:
            print("[telegram] skipped: missing TELEGRAM_BOT_TOKEN and/or TELEGRAM_CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload: Dict[str, Any] = {
        "chat_id": to,
        "text": text_to_html(text),
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    try:
        resp = requests.post(url, json=payload, timeout=timeout)
        if resp.status_code >= 300:
            print(f"[telegram] send failed: {resp.status_code} {resp.text}")
    except Exception as exc:
        print(f"[telegram] send error: {exc}")
