"""Trading safety controller (deterministic).

Creates a local pause flag when trading-impacting invariants fail.
This is intentionally simple and file-based so it works even when Supabase is down.

Files:
- output/state/trading_pause.json

The OpenClaw cron notifier job reads this file and sends Telegram with buttons.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any, Dict, Optional

REPO = Path(__file__).resolve().parents[1]
STATE_DIR = REPO / "output" / "state"
PAUSE_PATH = STATE_DIR / "trading_pause.json"


def _now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def pause(kind: str, detail: str, run_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Set pause flag (idempotent). Returns current pause payload."""

    STATE_DIR.mkdir(parents=True, exist_ok=True)

    if PAUSE_PATH.exists():
        try:
            obj = json.loads(PAUSE_PATH.read_text(encoding="utf-8"))
            if obj.get("paused"):
                return obj
        except Exception:
            pass

    payload: Dict[str, Any] = {
        "paused": True,
        "created_at_utc": _now_utc(),
        "kind": kind,
        "detail": detail,
        "notified": False,
        "run_context": run_context or {},
    }
    PAUSE_PATH.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    return payload


def get() -> Optional[Dict[str, Any]]:
    if not PAUSE_PATH.exists():
        return None
    try:
        return json.loads(PAUSE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def mark_notified() -> None:
    obj = get() or {}
    if not obj.get("paused"):
        return
    obj["notified"] = True
    obj["notified_at_utc"] = _now_utc()
    PAUSE_PATH.write_text(json.dumps(obj, indent=2, default=str) + "\n", encoding="utf-8")


def clear() -> None:
    if PAUSE_PATH.exists():
        PAUSE_PATH.unlink()
