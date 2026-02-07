"""Print a human-friendly safety pause summary.

Used by the main agent when user types `safety_details`.
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAUSE_PATH = REPO / "output" / "state" / "trading_pause.json"


def main() -> None:
    if not PAUSE_PATH.exists():
        print("No pause flag set.")
        return
    try:
        obj = json.loads(PAUSE_PATH.read_text(encoding="utf-8"))
    except Exception:
        print(f"Pause flag exists but could not parse: {PAUSE_PATH}")
        return

    print("Trading pause status")
    print("- paused:", obj.get("paused"))
    print("- kind:", obj.get("kind"))
    print("- created_at_utc:", obj.get("created_at_utc"))
    print("- notified:", obj.get("notified"))
    if obj.get("detail"):
        print("- detail:", obj.get("detail"))

    rc = obj.get("run_context") or {}
    if rc:
        print("- run_context:")
        for k in sorted(rc.keys()):
            print(f"  - {k}: {rc[k]}")


if __name__ == "__main__":
    main()
