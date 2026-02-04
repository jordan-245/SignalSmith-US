"""Telegram formatting + sending helpers.

We use parse_mode=HTML because it's predictable and doesn't require escaping
characters like MarkdownV2.

- text_to_html(): turns a plain-text multiline message into nicer HTML.
- send_telegram(): sends with disable_web_page_preview.

All HTML special chars are escaped.
"""

from __future__ import annotations

import html
import os
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


def send_telegram(text: str, *, token: Optional[str] = None, chat_id: Optional[str] = None, timeout: int = 15) -> None:
    bot_token = token or os.getenv("TELEGRAM_BOT_TOKEN", "")
    to = chat_id or os.getenv("TELEGRAM_CHAT_ID", "")
    if not bot_token or not to:
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
