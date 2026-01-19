"""
Minimal monitor stub: checks the latest baseline run log and reports staleness or missing runs.
Extend to push alerts (Slack/webhook) as needed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Optional
import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitor baseline run freshness.")
    parser.add_argument(
        "--runs-dir",
        default=Path(__file__).resolve().parents[1] / "output" / "baseline" / "runs",
        type=Path,
        help="Directory containing baseline run JSON logs.",
    )
    parser.add_argument("--stale-hours", type=int, default=24, help="Max allowed age in hours before flagging stale.")
    parser.add_argument("--webhook-url", default=os.getenv("WEBHOOK_URL", ""), help="Webhook URL (generic).")
    parser.add_argument("--notify", action="store_true", help="Send alert on stale condition.")
    parser.add_argument("--telegram-bot-token", default=os.getenv("TELEGRAM_BOT_TOKEN", ""), help="Telegram bot token.")
    parser.add_argument("--telegram-chat-id", default=os.getenv("TELEGRAM_CHAT_ID", ""), help="Telegram chat id.")
    return parser.parse_args()


def latest_run_file(runs_dir: Path) -> Optional[Path]:
    if not runs_dir.exists():
        return None
    files = sorted(runs_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def main() -> None:
    args = parse_args()
    run_file = latest_run_file(args.runs_dir)
    if not run_file:
        print("[monitor] No run logs found.")
        if args.notify:
            send_alert(
                webhook_url=args.webhook_url,
                telegram_bot=args.telegram_bot_token,
                telegram_chat=args.telegram_chat_id,
                level="error",
                title="Baseline monitor",
                body="No run logs found.",
            )
        raise SystemExit(1)

    data = json.loads(run_file.read_text())
    run_time = dt.datetime.fromisoformat(data["date"])
    age_hours = (dt.datetime.utcnow() - run_time).total_seconds() / 3600
    stale = age_hours > args.stale_hours

    print(f"[monitor] Latest run: {run_file.name} (age ~ {age_hours:.1f}h, val_auc={data.get('val_auc')})")
    if stale:
        print(f"[monitor] STALE: older than {args.stale_hours} hours.")
        if args.notify:
            body = f"Run {run_file.name} is stale (~{age_hours:.1f}h old)."
            send_alert(
                webhook_url=args.webhook_url,
                telegram_bot=args.telegram_bot_token,
                telegram_chat=args.telegram_chat_id,
                level="warn",
                title="Baseline monitor",
                body=body,
            )
        raise SystemExit(1)

def send_alert(webhook_url: str, telegram_bot: str, telegram_chat: str, level: str, title: str, body: str) -> None:
    text = f"*{level.upper()}* - {title}\n{body}"
    if telegram_bot and telegram_chat:
        try:
            url = f"https://api.telegram.org/bot{telegram_bot}/sendMessage"
            resp = requests.post(url, json={"chat_id": telegram_chat, "text": text, "parse_mode": "Markdown"})
            if resp.status_code >= 400:
                print(f"[monitor] Telegram send failed: {resp.status_code} {resp.text}")
        except Exception as exc:  # pragma: no cover
            print(f"[monitor] Telegram send error: {exc}")
    if webhook_url:
        try:
            resp = requests.post(webhook_url, json={"text": text})
            if resp.status_code >= 400:
                print(f"[monitor] Webhook failed: {resp.status_code} {resp.text}")
        except Exception as exc:  # pragma: no cover
            print(f"[monitor] Webhook error: {exc}")


if __name__ == "__main__":
    main()
