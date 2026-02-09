#!/usr/bin/env python3
"""Signal Foundry — Master Orchestrator

Runs a deterministic daily pipeline for US (and eventually ASX) equities:
  prices → features → labels → models → predictions → backtest → report

Usage examples:
  # Full run for US market
  python3 execution/foundry/foundry_run.py --market US --mode full --date 2026-02-09

  # Dry-run: validates inputs, checks calendar, skips execution
  python3 execution/foundry/foundry_run.py --market US --mode full --date 2026-02-07 --dry-run

  # Both markets
  python3 execution/foundry/foundry_run.py --market both --mode post --date 2026-02-09

CLI args:
  --market   US | ASX | both
  --mode     pre | post | backtest | full
  --date     YYYY-MM-DD  (the target trading date)
  --dry-run  validate inputs without executing pipeline steps
  --years    price history window in years (default 5)
  --limit    optional ticker limit for fast local testing
  --feature-set  feature version tag (default v1)
"""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
import sys
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Ensure repo root and foundry dir are importable
REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "execution"))
sys.path.insert(0, str(REPO / "execution" / "foundry"))

# Load .env early
try:
    from dotenv import load_dotenv
    load_dotenv(REPO / ".env")
except ImportError:
    pass

import yaml
import requests

# Local foundry steps (deterministic execution layer)
from foundry_steps import (
    build_features,
    build_labels,
    is_session,
    latest_session,
    load_quality_gates,
    load_universe,
    ingest_prices,
    predict_and_calibrate,
    quality_gate_check,
)

from foundry_report import generate_report


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PIPELINE_STAGES = [
    "foundry_prices",
    "foundry_features",
    "foundry_labels",
    "foundry_models",
    "foundry_predictions",
    "foundry_quality_gates",
    "foundry_report",
]


# ---------------------------------------------------------------------------
# Supabase logging
# ---------------------------------------------------------------------------

def _supabase_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }


def _append_local_run_log(
    run_id: str,
    stage: str,
    status: str,
    date_str: str,
    timestamp: str,
    stats: Optional[Dict] = None,
    warnings: Optional[List[str]] = None,
) -> None:
    """Append a JSON line to the local run log as a fallback when Supabase is down."""
    log_path = REPO / "data" / "foundry" / "run_log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "run_id": run_id,
        "stage": stage,
        "status": status,
        "date": date_str,
        "timestamp": timestamp,
        "stats": stats or {},
    }
    if warnings:
        entry["warnings"] = warnings
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, default=str) + "\n")
    except Exception as exc:
        print(f"[local-log] write error: {exc}")


def log_pipeline_run(
    run_id: str,
    stage: str,
    status: str,
    date_str: str,
    started_at: str,
    ended_at: str,
    stats: Optional[Dict] = None,
    warnings: Optional[List[str]] = None,
) -> None:
    """Insert a row into Supabase pipeline_runs table + local JSONL fallback."""
    # Always write local fallback first
    _append_local_run_log(
        run_id=run_id,
        stage=stage,
        status=status,
        date_str=date_str,
        timestamp=ended_at or dt.datetime.now(dt.timezone.utc).isoformat(),
        stats=stats,
        warnings=warnings,
    )

    base = os.getenv("SUPABASE_URL", "")
    if not base:
        print(f"[supabase] skipped: SUPABASE_URL not set (stage={stage})")
        return

    payload = {
        "run_id": run_id,
        "stage": stage,
        "status": status,
        "date": date_str,
        "started_at": started_at,
        "ended_at": ended_at,
        "stats_json": json.dumps(stats or {}),
        "warnings_json": json.dumps(warnings or []),
    }

    try:
        url = f"{base}/rest/v1/pipeline_runs"
        resp = requests.post(url, json=payload, headers=_supabase_headers(), timeout=15)
        if resp.status_code >= 300:
            print(f"[supabase] insert failed ({stage}): {resp.status_code} {resp.text[:200]}")
    except Exception as exc:
        print(f"[supabase] insert error ({stage}): {exc}")


# ---------------------------------------------------------------------------
# Telegram notification
# ---------------------------------------------------------------------------

def send_notification(text: str) -> None:
    """Send a Telegram notification via telegram_fmt helper or direct API."""
    try:
        from telegram_fmt import send_telegram
        send_telegram(text, warn_if_missing=True)
    except Exception as exc:
        print(f"[telegram] notification failed: {exc}")


# ---------------------------------------------------------------------------
# Quality gates (extended wrapper)
# ---------------------------------------------------------------------------

def check_quality_gates_extended(
    gates: dict,
    diagnostics: Dict,
    market: str,
) -> Dict:
    """Run quality gate checks from quality_gates.yaml.

    Wraps foundry_steps.quality_gate_check and adds extra checks.
    Returns dict with 'ok' bool, 'warnings' list, 'details' dict.
    Gates never block report generation — they add warnings.
    """
    # Use the canonical gate check from foundry_steps
    base_result = quality_gate_check(gates, market, diagnostics)

    warnings: List[str] = list(base_result.get("reasons", []))
    details: Dict[str, Any] = {}

    universe = load_universe(market)
    predicted = int(diagnostics.get("tickers_predicted") or 0)
    total = len(universe) or 1

    details["coverage_frac"] = round(predicted / total, 3)
    details["tickers_predicted"] = predicted
    details["train_rows"] = int(diagnostics.get("train_rows") or 0)

    # -- Model: min_auc (if available in diagnostics) --
    model_cfg = gates.get("model") or {}
    min_auc = float(model_cfg.get("min_auc") or 0.0)
    diag_auc = diagnostics.get("val_auc")
    if diag_auc is not None:
        details["val_auc"] = round(float(diag_auc), 4)
        if min_auc and float(diag_auc) < min_auc:
            warnings.append(f"val_auc {float(diag_auc):.4f} < min {min_auc}")

    # -- Model: max_calibration_error (if available) --
    max_cal = float(model_cfg.get("max_calibration_error") or 1.0)
    cal_err = diagnostics.get("calibration_error")
    if cal_err is not None:
        details["calibration_error"] = round(float(cal_err), 4)
        if float(cal_err) > max_cal:
            warnings.append(f"calibration_error {float(cal_err):.4f} > max {max_cal}")

    # -- Brier scores --
    try:
        b = diagnostics.get("calibration", {}).get("5d", {}).get("brier_uncal")
        if b is not None:
            details["brier_5d"] = round(float(b), 4)
    except Exception:
        pass

    ok = len(warnings) == 0
    return {"ok": ok, "warnings": warnings, "details": details}


# ---------------------------------------------------------------------------
# Pipeline step runner (with timing + logging)
# ---------------------------------------------------------------------------

class StepTimer:
    """Context manager that tracks wall-clock time for a pipeline step."""

    def __init__(self, stage: str, run_id: str, date_str: str, dry_run: bool = False):
        self.stage = stage
        self.run_id = run_id
        self.date_str = date_str
        self.dry_run = dry_run
        self.started_at = ""
        self.ended_at = ""
        self.elapsed = 0.0
        self._t0 = 0.0

    def __enter__(self):
        self.started_at = dt.datetime.now(dt.timezone.utc).isoformat()
        self._t0 = time.monotonic()
        print(f"[{self.stage}] started …")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.monotonic() - self._t0
        self.ended_at = dt.datetime.now(dt.timezone.utc).isoformat()
        status = "ok" if exc_type is None else "error"
        print(f"[{self.stage}] {status} ({self.elapsed:.1f}s)")

        if not self.dry_run:
            stats = {"elapsed_s": round(self.elapsed, 2)}
            if exc_val:
                stats["error"] = str(exc_val)[:500]
            log_pipeline_run(
                run_id=self.run_id,
                stage=self.stage,
                status=status,
                date_str=self.date_str,
                started_at=self.started_at,
                ended_at=self.ended_at,
                stats=stats,
            )
        return False  # don't suppress exceptions


# ---------------------------------------------------------------------------
# Dry-run validation
# ---------------------------------------------------------------------------

def dry_run_validate(market: str, date: dt.date, mode: str) -> Dict:
    """Validate inputs without executing. Returns summary dict."""
    result: Dict[str, Any] = {
        "dry_run": True,
        "market": market,
        "date": date.isoformat(),
        "mode": mode,
    }

    # Calendar check
    trading = is_session(market, date)
    result["is_trading_day"] = trading
    if not trading:
        try:
            prev = latest_session(market, date)
            result["previous_trading_day"] = prev.isoformat()
        except Exception:
            result["previous_trading_day"] = "unknown"
        result["note"] = f"{date} is not a trading day for {market}; pipeline would skip."

    # Universe check
    tickers = load_universe(market)
    result["universe_count"] = len(tickers)
    result["universe_sample"] = tickers[:5]

    # Quality gates
    gates = load_quality_gates()
    result["quality_gates"] = gates

    # Supabase connectivity
    base = os.getenv("SUPABASE_URL", "")
    result["supabase_configured"] = bool(base)

    # Telegram connectivity
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    result["telegram_configured"] = bool(bot_token)

    return result


# ---------------------------------------------------------------------------
# Full pipeline execution
# ---------------------------------------------------------------------------

_LOCK_PATH = REPO / ".foundry.lock"


def run_pipeline(
    market: str,
    mode: str,
    date: dt.date,
    run_id: str,
    years: int = 5,
    limit: int = 0,
    feature_set: str = "v1",
) -> Dict:
    """Execute the full foundry pipeline for a single market.

    Returns a result dict with status, gate results, and timing.
    """
    # ── Prevent concurrent pipeline runs via file lock ──
    lock_fd = open(_LOCK_PATH, "w")
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock_fd.close()
        return {
            "market": market,
            "mode": mode,
            "date": date.isoformat(),
            "run_id": run_id,
            "ok": False,
            "error": "Another foundry pipeline is already running (lock held)",
        }

    try:
        return _run_pipeline_locked(
            market=market,
            mode=mode,
            date=date,
            run_id=run_id,
            years=years,
            limit=limit,
            feature_set=feature_set,
        )
    finally:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        lock_fd.close()


def _run_pipeline_locked(
    market: str,
    mode: str,
    date: dt.date,
    run_id: str,
    years: int = 5,
    limit: int = 0,
    feature_set: str = "v1",
) -> Dict:
    """Internal: execute the pipeline while holding the lock."""
    date_str = date.isoformat()
    result: Dict[str, Any] = {
        "market": market,
        "mode": mode,
        "date": date_str,
        "run_id": run_id,
    }

    # -- Calendar check --
    if not is_session(market, date):
        try:
            prev = latest_session(market, date)
            result["previous_trading_day"] = prev.isoformat()
        except Exception:
            pass
        result["skipped"] = True
        result["reason"] = f"{date} is not a trading day for {market}"
        log_pipeline_run(
            run_id=run_id,
            stage="foundry_calendar_check",
            status="skipped",
            date_str=date_str,
            started_at=dt.datetime.now(dt.timezone.utc).isoformat(),
            ended_at=dt.datetime.now(dt.timezone.utc).isoformat(),
            stats={"reason": result["reason"]},
        )
        return result

    # -- Load universe --
    tickers = load_universe(market)
    if limit and limit > 0:
        tickers = tickers[:limit]
    result["universe_count"] = len(tickers)

    prices = None
    feats = None
    labels = None
    preds = None
    diagnostics: Dict = {}
    gate_res: Dict = {"ok": True, "warnings": []}

    try:
        # STEP 1: Prices
        with StepTimer("foundry_prices", run_id, date_str):
            prices = ingest_prices(
                tickers, market=market, as_of=date, years=years,
            )
            if prices is None or prices.empty:
                raise RuntimeError("No price data returned")
            result["price_rows"] = len(prices)

        # STEP 2: Features
        with StepTimer("foundry_features", run_id, date_str):
            feats = build_features(prices, market=market, feature_set=feature_set, as_of=date)
            result["feature_rows"] = len(feats) if feats is not None else 0

        # STEP 3: Labels
        with StepTimer("foundry_labels", run_id, date_str):
            labels = build_labels(prices, market=market, as_of=date)
            result["label_rows"] = len(labels) if labels is not None else 0

        # STEP 4 + 5: Models + Predictions (combined in predict_and_calibrate)
        with StepTimer("foundry_models", run_id, date_str):
            preds, diagnostics = predict_and_calibrate(
                feats, labels, market=market, as_of=date, run_id=run_id
            )
            result["diagnostics"] = diagnostics

        # STEP 6: Quality gates
        with StepTimer("foundry_quality_gates", run_id, date_str):
            gates = load_quality_gates()
            gate_res = check_quality_gates_extended(gates, diagnostics, market)
            result["quality_gates"] = gate_res

            if gate_res["warnings"]:
                log_pipeline_run(
                    run_id=run_id,
                    stage="foundry_quality_gates",
                    status="warn",
                    date_str=date_str,
                    started_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                    ended_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                    warnings=gate_res["warnings"],
                )

        # STEP 7: Report (always generated, even with gate warnings)
        # Uses foundry_report.generate_report() which produces both MD + HTML
        with StepTimer("foundry_report", run_id, date_str):
            report_md, report_html = generate_report(
                market=market,
                as_of_str=date_str,
                run_id=run_id,
            )

            # Also write to docs/ for backward compatibility
            report_dir = REPO / "docs" / "foundry" / market
            report_dir.mkdir(parents=True, exist_ok=True)
            dated_path = report_dir / f"{date_str}.md"
            dated_path.write_text(report_md, encoding="utf-8")

            latest_path = report_dir / "latest.md"
            latest_path.write_text(report_md, encoding="utf-8")
            result["report_path"] = str(dated_path)

        result["ok"] = True
        result["gate_pass"] = gate_res.get("ok", True)

    except Exception as exc:
        result["ok"] = False
        result["error"] = str(exc)
        result["traceback"] = traceback.format_exc()
        print(f"[foundry] pipeline error: {exc}")
        traceback.print_exc()

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Signal Foundry — master orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--market",
        choices=["US", "ASX", "both"],
        default="US",
        help="Which market to run (default: US)",
    )
    p.add_argument(
        "--mode",
        choices=["pre", "post", "backtest", "full"],
        default="full",
        help="Pipeline mode (default: full)",
    )
    p.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Target date YYYY-MM-DD (default: today)",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate inputs without executing pipeline",
    )
    p.add_argument(
        "--years",
        type=int,
        default=5,
        help="Price history window in years (default: 5)",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Optional ticker limit for faster local testing",
    )
    p.add_argument(
        "--feature-set",
        default="v1",
        help="Feature version tag (default: v1)",
    )
    return p.parse_args()


def check_early_close(date: dt.date, markets: List[str]) -> Optional[str]:
    """Check if today is an early-close day for any of the given markets.

    Uses exchange-calendars to detect early-close sessions. Returns a note
    string if any market has an early close, or None otherwise.
    Informational only — does not block the pipeline.
    """
    try:
        import exchange_calendars as xcals
    except ImportError:
        return None

    market_to_exchange = {"US": "XNYS", "ASX": "XASX"}
    notes: List[str] = []

    for market in markets:
        exchange = market_to_exchange.get(market)
        if not exchange:
            continue
        try:
            cal = xcals.get_calendar(exchange)
            import pandas as pd
            ts = pd.Timestamp(date)
            if cal.is_session(ts):
                close_time = cal.session_close(ts)
                # NYSE normal close is 16:00 ET, early close is 13:00 ET
                # ASX normal close is 16:00 AEST, early close varies
                # exchange_calendars marks early closes with shorter sessions
                open_time = cal.session_open(ts)
                session_hours = (close_time - open_time).total_seconds() / 3600
                # NYSE normal is ~6.5h (9:30-16:00), early is ~3.5h (9:30-13:00)
                # ASX normal is ~6h (10:00-16:00)
                if market == "US" and session_hours < 6.0:
                    notes.append(f"{market}: Early close on {date} (session {session_hours:.1f}h)")
                elif market == "ASX" and session_hours < 5.5:
                    notes.append(f"{market}: Early close on {date} (session {session_hours:.1f}h)")
        except Exception as exc:
            print(f"[early-close] check failed for {market}: {exc}")
            continue

    if notes:
        return "Early close detected: " + "; ".join(notes)
    return None


def main() -> None:
    args = parse_args()
    target_date = dt.date.fromisoformat(args.date)
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")

    markets: List[str] = []
    if args.market == "both":
        markets = ["US", "ASX"]
    else:
        markets = [args.market]

    # ---- Dry-run mode ----
    if args.dry_run:
        print("=" * 60)
        print("SIGNAL FOUNDRY — DRY RUN")
        print("=" * 60)
        for m in markets:
            result = dry_run_validate(m, target_date, args.mode)
            print(json.dumps(result, indent=2, default=str))
        print("=" * 60)
        print("Dry run complete. No pipeline steps executed.")
        return

    # ---- Live run ----
    print("=" * 60)
    print(f"SIGNAL FOUNDRY — {args.mode.upper()} RUN")
    print(f"Markets: {', '.join(markets)} | Date: {target_date} | Run ID: {run_id}")
    print("=" * 60)

    all_results: List[Dict] = []
    overall_ok = True

    for m in markets:
        print(f"\n{'—' * 40}")
        print(f"Market: {m}")
        print(f"{'—' * 40}")

        result = run_pipeline(
            market=m,
            mode=args.mode,
            date=target_date,
            run_id=run_id,
            years=args.years,
            limit=args.limit,
            feature_set=args.feature_set,
        )
        all_results.append(result)

        if not result.get("ok", False) and not result.get("skipped", False):
            overall_ok = False

    # ---- Summary ----
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for r in all_results:
        m = r.get("market", "?")
        if r.get("skipped"):
            print(f"  {m}: SKIPPED — {r.get('reason', 'holiday')}")
        elif r.get("ok"):
            gate_status = "PASS" if r.get("gate_pass") else "WARN"
            warnings = r.get("quality_gates", {}).get("warnings", [])
            w_str = f" ({'; '.join(warnings)})" if warnings else ""
            print(f"  {m}: OK — gates {gate_status}{w_str}")
        else:
            print(f"  {m}: ERROR — {r.get('error', 'unknown')}")

    # ---- Output full JSON ----
    print("\n" + json.dumps(all_results, indent=2, default=str))

    # ---- Early-close detection ----
    early_close_note = check_early_close(target_date, markets)
    if early_close_note:
        print(f"\n📋 {early_close_note}")
        # Include in all results for report visibility
        for r in all_results:
            r["early_close_note"] = early_close_note

    # ---- Telegram notification ----
    _send_summary_notification(all_results, overall_ok, run_id, target_date, args.mode)


def _send_summary_notification(
    results: List[Dict],
    overall_ok: bool,
    run_id: str,
    date: dt.date,
    mode: str,
) -> None:
    """Build and send a Telegram summary."""
    emoji = "✅" if overall_ok else "❌"
    lines = [f"{emoji} Signal Foundry — {mode.upper()} — {date.isoformat()}"]
    lines.append(f"Run: {run_id}")
    lines.append("")

    for r in results:
        m = r.get("market", "?")
        if r.get("skipped"):
            lines.append(f"📅 {m}: Skipped (not a trading day)")
        elif r.get("ok"):
            gate_pass = r.get("gate_pass", True)
            gate_emoji = "✅" if gate_pass else "⚠️"
            lines.append(f"{gate_emoji} {m}: Complete")
            warnings = r.get("quality_gates", {}).get("warnings", [])
            if warnings:
                for w in warnings:
                    lines.append(f"  ⚠️ {w}")
            tickers = r.get("diagnostics", {}).get("tickers_predicted", "?")
            lines.append(f"  Tickers: {tickers} | Report: docs/foundry/{m}/latest.md")
        else:
            lines.append(f"❌ {m}: Error — {r.get('error', 'unknown')[:100]}")

    # Include early-close note if present
    for r in results:
        note = r.get("early_close_note")
        if note:
            lines.append(f"\n📋 {note}")
            break

    text = "\n".join(lines)
    try:
        send_notification(text)
    except Exception as exc:
        print(f"[telegram] notification error: {exc}")


if __name__ == "__main__":
    main()
