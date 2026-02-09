# Signal Foundry Pipeline — SOP Directive

## Purpose

The Signal Foundry pipeline produces daily probabilistic direction forecasts, catalyst context, and trade plan candidates for US and ASX equities. It runs as a deterministic, idempotent pipeline orchestrated by `execution/foundry/foundry_run.py`.

## Architecture

This follows the 3-layer architecture (Directives → Orchestration → Execution):

- **Directive** (this file): Defines what to do, quality standards, and edge cases.
- **Orchestration**: `foundry_run.py` — reads this directive, calls execution scripts in order, handles errors.
- **Execution**: `foundry_steps.py` — deterministic Python functions for each pipeline stage.

## Inputs

| Input | Source | Location |
|-------|--------|----------|
| Universe (US) | S&P 500 watchlist | `directives/foundry/universe_us.txt` |
| Universe (ASX) | ASX watchlist | `directives/foundry/universe_asx.txt` |
| Quality gates | YAML thresholds | `directives/foundry/quality_gates.yaml` |
| Price data | yfinance (free) | Downloaded at runtime |
| Exchange calendar | `exchange-calendars` lib | Checked at runtime |
| Supabase credentials | `.env` | `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE` |
| Telegram credentials | `.env` | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` |

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Price parquet | `data/foundry/prices/market={M}/run_id={ID}/part.parquet` | Parquet |
| Feature parquet | `data/foundry/features/market={M}/feature_set=v1/date={D}/part.parquet` | Parquet |
| Label parquet | `data/foundry/labels/market={M}/date={D}/part.parquet` | Parquet |
| Prediction parquet | `data/foundry/predictions/market={M}/run_id={ID}/part.parquet` | Parquet |
| Dated report | `docs/foundry/{M}/{D}.md` | Markdown |
| Latest report | `docs/foundry/{M}/latest.md` | Markdown |
| Pipeline run logs | Supabase `pipeline_runs` table | JSON rows |
| Telegram summary | Telegram chat | HTML message |

## Pipeline Steps (in order)

### 1. Calendar Check
- Uses `exchange-calendars` to verify the target date is a trading session.
- If not a trading day → skip with `status=skipped`, log to Supabase, notify Telegram.
- Script: `foundry_run.py` → `is_trading_day()`

### 2. Load Universe
- Reads ticker list from `directives/foundry/universe_{market}.txt`.
- Strips comments, de-dupes, uppercases.
- Optional `--limit N` for testing.
- Script: `foundry_steps.py` → `load_universe()`

### 3. Ingest Prices
- Downloads daily OHLCV for all universe tickers using yfinance.
- Window: `--years` (default 5) of history up to target date.
- Writes to parquet feature store.
- Script: `foundry_steps.py` → `write_prices_parquet()`

### 4. Build Features
- Computes: ret_1d, ret_5d, ret_20d, vol_20d, sma50, sma200, px_gt_sma200, sma50_gt_sma200.
- Writes features to parquet, partitioned by market/feature_set/date.
- Script: `foundry_steps.py` → `build_features()`

### 5. Build Labels
- Forward returns: y_up_1d, y_up_5d, y_up_20d (binary direction).
- Also stores continuous forward returns for calibration.
- Writes labels to parquet, partitioned by market/date.
- Script: `foundry_steps.py` → `build_labels()`

### 6. Train Models + Predict
- Pooled cross-sectional model (all tickers combined).
- Models: Logistic Regression baseline + Random Forest.
- Calibration: Isotonic regression on held-out tail window.
- Horizons: 1D, 5D, 20D + ensemble average.
- Writes predictions to parquet.
- Script: `foundry_steps.py` → `predict_and_calibrate()`

### 7. Quality Gates
- Checks thresholds from `directives/foundry/quality_gates.yaml`.
- Gates do NOT block report generation — they add warnings to the report.
- Gate checks:
  - `coverage`: min fraction of tickers with predictions (default: 80%)
  - `min_tickers`: minimum absolute tickers predicted (default: 5)
  - `min_training_rows`: minimum pooled training rows (default: 200)
  - `min_auc`: walk-forward AUC threshold (default: 0.52)
  - `max_calibration_error`: max ECE (default: 0.15)
  - `max_brier`: legacy Brier score bound (default: 0.30)
- Script: `foundry_run.py` → `check_quality_gates()`

### 8. Render Report
- Generates Markdown report with: top candidates, probabilities, coverage stats, calibration, gate status.
- Writes dated report AND promotes to `latest.md`.
- Reports with gate warnings include a visible ⚠️ section.
- Script: `foundry_steps.py` → `render_report()`

### 9. Log + Notify
- Each step logs to Supabase `pipeline_runs` table with stage, status, timing.
- Final summary sent to Telegram with per-market status and warnings.

## CLI Usage

```bash
# Full run for US
python3 execution/foundry/foundry_run.py --market US --mode full --date 2026-02-09

# Dry-run (validates inputs, no execution)
python3 execution/foundry/foundry_run.py --market US --mode full --date 2026-02-07 --dry-run

# Both markets
python3 execution/foundry/foundry_run.py --market both --mode post --date 2026-02-09

# Limited tickers for testing
python3 execution/foundry/foundry_run.py --market US --mode full --date 2026-02-09 --limit 10
```

## Modes

| Mode | Description |
|------|-------------|
| `pre` | Pre-open run: prices + features + predictions for the upcoming session |
| `post` | Post-close run: full pipeline including labels + model retraining |
| `backtest` | Walk-forward backtest only (no report publishing) |
| `full` | Complete pipeline: all steps including backtest and report |

## Edge Cases

1. **Market holiday**: Detected via `exchange-calendars`. Pipeline skips cleanly, logs `skipped` status.
2. **Weekend date**: Same as holiday — detected and skipped.
3. **Missing price data**: yfinance may return gaps. Coverage gate catches insufficient data.
4. **yfinance rate limits**: Tickers fetched in chunks of 50 with error handling.
5. **Supabase down**: Logging failures are caught and printed but don't stop the pipeline.
6. **Telegram not configured**: Notification skipped silently (credentials commented out in .env).
7. **ASX not implemented**: Raises clean error. Universe file exists but is empty.
8. **Model training fails**: predict_and_calibrate returns empty predictions + diagnostic error.

## Execution Scripts Reference

| Script | Purpose |
|--------|---------|
| `execution/foundry/foundry_run.py` | Master orchestrator — CLI entry point |
| `execution/foundry/foundry_steps.py` | Deterministic pipeline functions |
| `execution/telegram_fmt.py` | Telegram formatting + sending |
| `directives/foundry/quality_gates.yaml` | Quality gate thresholds |
| `directives/foundry/universe_us.txt` | US ticker universe |
| `directives/foundry/universe_asx.txt` | ASX ticker universe (future) |

## Learnings

_Updated as the system self-anneals._

- **2026-02-09**: Initial build. Feb 7 2026 is a Saturday — calendar check correctly skips.
- yfinance `group_by="column"` returns MultiIndex for multi-ticker downloads; handled in `write_prices_parquet`.
- Supabase `pipeline_runs` table has columns: id, run_id, tag, date, val_auc, top, positions, equity, report_path, missing_tickers, created_at, stage, status, started_at, ended_at, stats_json, warnings_json.
- Telegram credentials are commented out in .env; notifications will be skipped until configured.
- Quality gates are advisory, not blocking — reports always generate but include gate warnings.
