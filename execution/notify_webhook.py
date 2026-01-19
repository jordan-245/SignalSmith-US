"""
Send a simple webhook (e.g., Slack) notification for baseline runs/monitoring.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import requests


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send webhook notification.")
    parser.add_argument("--webhook-url", default=os.getenv("WEBHOOK_URL", ""), help="Webhook URL (or set WEBHOOK_URL).")
    parser.add_argument("--title", required=True, help="Message title.")
    parser.add_argument("--body", required=True, help="Message body.")
    parser.add_argument("--level", default="info", help="info|warn|error")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.webhook_url:
        print("No webhook URL provided (set --webhook-url or WEBHOOK_URL).")
        sys.exit(1)

    payload = {
        "text": f"*{args.level.upper()}* - {args.title}\n{args.body}",
    }
    resp = requests.post(args.webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    if resp.status_code >= 400:
        print(f"Webhook post failed: {resp.status_code} {resp.text}")
        sys.exit(1)
    print("Webhook sent.")


if __name__ == "__main__":
    main()
