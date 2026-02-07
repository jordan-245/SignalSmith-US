"""
Auto-deny stale approval requests.

- Finds pending approvals older than timeout (default 15 minutes)
- Updates approval_requests status -> denied
- Writes approval_actions audit rows
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
from typing import Dict, List

import requests
from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Auto-deny stale approval requests in Supabase.")
    parser.add_argument("--timeout-minutes", type=int, default=15, help="Minutes before auto-deny.")
    parser.add_argument("--limit", type=int, default=200, help="Max pending approvals to sweep.")
    parser.add_argument("--dry-run", action="store_true", help="Report what would change without writing.")
    parser.add_argument("--notify-telegram", action="store_true", help="Send Telegram summary if denies occur.")
    return parser.parse_args()


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def supabase_enabled() -> bool:
    return bool(os.getenv("SUPABASE_URL")) and bool(os.getenv("SUPABASE_SERVICE_ROLE"))


def supabase_base() -> str:
    base = os.getenv("SUPABASE_URL", "")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base.rstrip("/")


def supabase_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    if not key:
        raise RuntimeError("SUPABASE_SERVICE_ROLE not set")
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def fetch_expired(cutoff: dt.datetime, limit: int) -> List[dict]:
    """Return expired approval rows.

    If the approvals tables haven't been deployed to Supabase yet (common in early
    environments), PostgREST returns PGRST205 (404). In that case we log and
    exit cleanly so cron doesn't flap.
    """
    url = f"{supabase_base()}/rest/v1/approval_requests"
    params = {
        "select": "request_id,request_type,created_ts",
        "status": "eq.pending",
        "created_ts": f"lt.{cutoff.isoformat()}",
        "order": "created_ts.asc",
        "limit": str(limit),
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)

    if resp.status_code == 404 and "PGRST205" in resp.text:
        print(
            "[approval_timeout] approvals tables not found in Supabase (PGRST205). "
            "Skipping sweep. (Did you deploy schema/approvals.sql?)"
        )
        return []

    if resp.status_code >= 300:
        raise RuntimeError(f"Supabase fetch failed: {resp.status_code} {resp.text}")
    return resp.json()


def mark_denied(cutoff: dt.datetime, now_iso: str, dry_run: bool) -> None:
    if dry_run:
        return
    url = f"{supabase_base()}/rest/v1/approval_requests"
    params = {
        "status": "eq.pending",
        "created_ts": f"lt.{cutoff.isoformat()}",
    }
    payload = {
        "status": "denied",
        "approved_by": "auto_timeout",
        "approved_ts": now_iso,
    }
    resp = requests.patch(url, headers=supabase_headers(), params=params, json=payload, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"Supabase update failed: {resp.status_code} {resp.text}")


def insert_actions(requests_expired: List[dict], now_iso: str, timeout_minutes: int, dry_run: bool) -> None:
    if not requests_expired:
        return
    actions = [
        {
            "request_id": row.get("request_id"),
            "action_ts": now_iso,
            "channel": "system",
            "actor": "auto_timeout",
            "action": "deny",
            "notes": f"Auto-denied after {timeout_minutes} minutes.",
        }
        for row in requests_expired
    ]
    if dry_run:
        return
    url = f"{supabase_base()}/rest/v1/approval_actions"
    resp = requests.post(url, headers=supabase_headers(), json=actions, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"Supabase insert failed: {resp.status_code} {resp.text}")


def send_telegram_summary(expired: List[dict], timeout_minutes: int) -> None:
    if not expired:
        return
    max_items = 10
    lines = [
        f"Approval timeout sweep: auto-denied {len(expired)} request(s) (>{timeout_minutes} min)"
    ]
    for row in expired[:max_items]:
        rid = row.get("request_id", "unknown")
        rtype = row.get("request_type", "unknown")
        created = row.get("created_ts", "unknown")
        lines.append(f"- {rid} | {rtype} | created {created}")
    if len(expired) > max_items:
        lines.append(f"- ...and {len(expired) - max_items} more")

    from telegram_fmt import send_telegram as _send

    _send("\n".join(lines), timeout=10, warn_if_missing=True)


def main() -> None:
    load_env()
    args = parse_args()

    # If Supabase isn't configured, we can't sweep approvals. This is usually a
    # deployment/config issue, so (optionally) notify Telegram.
    if not supabase_enabled():
        msg = "[approval_timeout] skipped: missing SUPABASE_URL or SUPABASE_SERVICE_ROLE"
        print(msg)
        if args.notify_telegram:
            try:
                from telegram_fmt import send_telegram as _send

                _send(
                    "Approval timeout sweep could not run: missing SUPABASE_URL and/or SUPABASE_SERVICE_ROLE.\n"
                    "No approval requests were checked or auto-denied.\n"
                    "Fix: set SUPABASE_URL + SUPABASE_SERVICE_ROLE in .env (or process env) for this deployment.",
                    timeout=10,
                    warn_if_missing=True,
                )
            except Exception as exc:
                print(f"[approval_timeout] telegram notify failed: {exc}")
        return

    now = dt.datetime.now(dt.timezone.utc)
    cutoff = now - dt.timedelta(minutes=args.timeout_minutes)
    expired = fetch_expired(cutoff, args.limit)
    # Noise control: if nothing to do, exit cleanly and stay quiet (cron should not flap).
    if not expired:
        return
    now_iso = now.isoformat()
    print(f"[approval_timeout] Expired approvals: {len(expired)}")
    mark_denied(cutoff, now_iso, args.dry_run)
    insert_actions(expired, now_iso, args.timeout_minutes, args.dry_run)
    if args.notify_telegram and not args.dry_run:
        send_telegram_summary(expired, args.timeout_minutes)


if __name__ == "__main__":
    main()
