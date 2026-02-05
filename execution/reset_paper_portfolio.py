"""Reset a paper portfolio back to cash and no positions.

This is used when we want to restart a book cleanly (e.g., switching to swing-only).

What it does:
- Deletes paper_positions rows for portfolio_id
- Deletes paper_equity_curve rows for portfolio_id

It intentionally does NOT delete paper_orders/paper_fills because those tables
are not keyed by portfolio_id in the current schema.

Usage:
  python execution/reset_paper_portfolio.py --portfolio-id swing

WARNING: Destructive for the chosen portfolio_id.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Dict

import requests
from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_env() -> None:
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)


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
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Reset a paper portfolio (delete positions + equity curve)")
    p.add_argument("--portfolio-id", default="swing")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def delete_where(table: str, portfolio_id: str, dry_run: bool) -> int:
    base = supabase_base()
    url = f"{base}/rest/v1/{table}"
    params = {"portfolio_id": f"eq.{portfolio_id}"}
    if dry_run:
        # count rows
        r = requests.get(url, headers=supabase_headers(), params={"select": "*", **params, "limit": "1"}, timeout=20)
        if r.status_code >= 300:
            raise RuntimeError(f"{table} precheck failed: {r.status_code} {r.text}")
        return -1

    r = requests.delete(url, headers=supabase_headers(), params=params, timeout=30)
    if r.status_code >= 300:
        raise RuntimeError(f"{table} delete failed: {r.status_code} {r.text}")
    # PostgREST doesn't return affected rows by default.
    return 0


def main() -> None:
    load_env()
    args = parse_args()

    pid = args.portfolio_id
    if args.dry_run:
        print(f"[dry-run] would delete paper_positions and paper_equity_curve where portfolio_id={pid}")
        return

    delete_where("paper_positions", pid, dry_run=False)
    delete_where("paper_equity_curve", pid, dry_run=False)

    print(f"[ok] reset portfolio {pid}: positions cleared; equity curve cleared")


if __name__ == "__main__":
    main()
