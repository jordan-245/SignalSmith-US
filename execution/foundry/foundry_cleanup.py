#!/usr/bin/env python3
"""Signal Foundry — Data Retention Cleanup

Removes stale data to keep disk usage under control:
  - Parquet date partitions older than 90 days (prices, features, labels)
  - Prediction run_id directories older than 30 days
  - Backtest run_id directories older than 60 days

Usage:
  python execution/foundry/foundry_cleanup.py --dry-run   # preview what would be removed
  python execution/foundry/foundry_cleanup.py              # actually remove stale data
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data" / "foundry"

# Retention policies (days)
PARTITION_RETENTION_DAYS = 90    # date-partitioned parquet dirs (prices, features, labels)
PREDICTION_RETENTION_DAYS = 30   # prediction run_id dirs
BACKTEST_RETENTION_DAYS = 60     # backtest run_id dirs

# Regex patterns
DATE_PARTITION_RE = re.compile(r"^date=(\d{4}-\d{2}-\d{2})$")
RUN_ID_RE = re.compile(r"^run_id=(\d{14})$")  # YYYYMMDDHHmmss


def _parse_run_id_date(run_id_str: str) -> dt.date | None:
    """Extract date from a run_id like '20260207122009'."""
    try:
        return dt.datetime.strptime(run_id_str[:8], "%Y%m%d").date()
    except (ValueError, IndexError):
        return None


def find_stale_date_partitions(
    base_dir: Path, cutoff: dt.date
) -> List[Tuple[Path, str]]:
    """Find date= partition directories older than cutoff."""
    stale = []
    if not base_dir.exists():
        return stale
    for market_dir in base_dir.iterdir():
        if not market_dir.is_dir():
            continue
        for child in market_dir.iterdir():
            if not child.is_dir():
                continue
            m = DATE_PARTITION_RE.match(child.name)
            if m:
                try:
                    partition_date = dt.date.fromisoformat(m.group(1))
                    if partition_date < cutoff:
                        stale.append((child, f"date partition {m.group(1)}"))
                except ValueError:
                    continue
    return stale


def find_stale_run_dirs(
    base_dir: Path, cutoff: dt.date
) -> List[Tuple[Path, str]]:
    """Find run_id= directories older than cutoff date."""
    stale = []
    if not base_dir.exists():
        return stale
    for market_dir in base_dir.iterdir():
        if not market_dir.is_dir():
            continue
        for child in market_dir.iterdir():
            if not child.is_dir():
                continue
            m = RUN_ID_RE.match(child.name)
            if m:
                run_date = _parse_run_id_date(m.group(1))
                if run_date and run_date < cutoff:
                    stale.append((child, f"run_id {m.group(1)} (date: {run_date})"))
    return stale


def cleanup(dry_run: bool = True) -> dict:
    """Run the full cleanup. Returns summary dict."""
    today = dt.date.today()
    partition_cutoff = today - dt.timedelta(days=PARTITION_RETENTION_DAYS)
    prediction_cutoff = today - dt.timedelta(days=PREDICTION_RETENTION_DAYS)
    backtest_cutoff = today - dt.timedelta(days=BACKTEST_RETENTION_DAYS)

    results = {
        "dry_run": dry_run,
        "today": today.isoformat(),
        "removed": [],
        "errors": [],
    }

    # Collect stale items
    stale_items: List[Tuple[Path, str, str]] = []

    # Date-partitioned directories: prices, features, labels
    for subdir_name in ("prices", "features", "labels"):
        subdir = DATA / subdir_name
        for path, desc in find_stale_date_partitions(subdir, partition_cutoff):
            stale_items.append((path, desc, f"{subdir_name} (>{PARTITION_RETENTION_DAYS}d)"))

    # Prediction run_id directories
    for path, desc in find_stale_run_dirs(DATA / "predictions", prediction_cutoff):
        stale_items.append((path, desc, f"predictions (>{PREDICTION_RETENTION_DAYS}d)"))

    # Backtest run_id directories
    for path, desc in find_stale_run_dirs(DATA / "backtests", backtest_cutoff):
        stale_items.append((path, desc, f"backtests (>{BACKTEST_RETENTION_DAYS}d)"))

    if not stale_items:
        print("✓ No stale data found. Nothing to clean up.")
        return results

    action = "Would remove" if dry_run else "Removing"
    print(f"\n{'DRY RUN — ' if dry_run else ''}Foundry Data Cleanup")
    print(f"Today: {today} | Partition cutoff: {partition_cutoff} | "
          f"Prediction cutoff: {prediction_cutoff} | Backtest cutoff: {backtest_cutoff}")
    print(f"{'=' * 70}")

    for path, desc, category in stale_items:
        size_str = ""
        try:
            size = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
            size_mb = size / (1024 * 1024)
            size_str = f" ({size_mb:.1f} MB)"
        except Exception:
            pass

        print(f"  {action}: {path.relative_to(REPO)} — {desc}{size_str} [{category}]")

        if not dry_run:
            try:
                shutil.rmtree(path)
                results["removed"].append(str(path))
            except Exception as exc:
                err_msg = f"Failed to remove {path}: {exc}"
                print(f"  ❌ {err_msg}")
                results["errors"].append(err_msg)
        else:
            results["removed"].append(str(path))

    print(f"\n{'Would remove' if dry_run else 'Removed'} {len(stale_items)} item(s)")
    if results["errors"]:
        print(f"Errors: {len(results['errors'])}")

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Signal Foundry — data retention cleanup",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be removed without deleting anything",
    )
    args = parser.parse_args()

    results = cleanup(dry_run=args.dry_run)
    if results["errors"] and not args.dry_run:
        sys.exit(1)


if __name__ == "__main__":
    main()
