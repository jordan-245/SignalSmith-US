"""Safety notifier (systemd-friendly, deterministic).

Checks output/state/trading_pause.json and, if paused and not notified, disables
swing trading cron jobs (via local jobs.json) and sends a Telegram alert.

This bypasses OpenClaw cron RPC flakiness.

No buttons (plain text).
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

REPO = Path(__file__).resolve().parents[1]
PAUSE_PATH = REPO / "output" / "state" / "trading_pause.json"

# OpenClaw cron store
CRON_STORE = Path("/root/.openclaw/cron/jobs.json")

SWING_PRE_JOB = "02839187-43d3-4512-bef7-00f313ec7053"
SWING_POST_JOB = "82ce4ac6-6683-4e0e-a954-dae8b19ff834"

DASHBOARD_URL = "https://dashboard.getflowtide.com/"


def send_telegram(text: str) -> None:
    from telegram_fmt import send_telegram as _send

    _send(text, timeout=15)


def load_pause() -> Optional[Dict[str, Any]]:
    if not PAUSE_PATH.exists():
        return None
    try:
        return json.loads(PAUSE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def save_pause(obj: Dict[str, Any]) -> None:
    PAUSE_PATH.parent.mkdir(parents=True, exist_ok=True)
    PAUSE_PATH.write_text(json.dumps(obj, indent=2, default=str) + "\n", encoding="utf-8")


def disable_cron_job(job_id: str) -> None:
    if not CRON_STORE.exists():
        return
    try:
        store = json.loads(CRON_STORE.read_text(encoding="utf-8"))
    except Exception:
        return

    jobs = store.get("jobs") or []
    changed = False
    for j in jobs:
        if j.get("id") == job_id:
            if j.get("enabled", True):
                j["enabled"] = False
                changed = True

    if changed:
        CRON_STORE.write_text(json.dumps(store, indent=2, default=str) + "\n", encoding="utf-8")


def main() -> None:
    st = load_pause()
    if not st or not st.get("paused"):
        print("HEARTBEAT_OK")
        return

    if st.get("notified"):
        print("HEARTBEAT_OK")
        return

    # Disable swing jobs (best-effort)
    disable_cron_job(SWING_PRE_JOB)
    disable_cron_job(SWING_POST_JOB)

    kind = st.get("kind") or "unknown"
    detail = st.get("detail") or "(no detail)"

    msg = (
        f"TRADING PAUSED — {kind}\n"
        f"{detail}\n\n"
        f"Dashboard: {DASHBOARD_URL}\n"
        f"Reply: safety_details | safety_resume"
    )

    try:
        send_telegram(msg)
    except Exception:
        # still mark notified to avoid spam loops
        pass

    st["notified"] = True
    save_pause(st)

    print("HEARTBEAT_OK")


if __name__ == "__main__":
    main()
