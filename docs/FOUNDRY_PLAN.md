# Signal Foundry — Implementation Plan (OpenClaw + deterministic pipeline)

Source: `docs/signal_foundry_prd.md`

## Principles
- Deterministic execution in `execution/`.
- OpenClaw orchestrates (cron + alerts + approvals) and can spawn sub-agents for analysis.
- Parquet is the *canonical* analytics store; Supabase is optional ops/UI.
- Quality gates block publication.

## Directory structure

### New
- `directives/foundry/`
  - `universe_us.txt` (20–50 tickers)
  - `universe_asx.txt` (20–50 tickers; include `.AX` suffix)
  - `quality_gates.yaml` (thresholds)
  - `feature_sets.yaml` (feature versions; e.g. v1)
  - `report_template_us.md`
  - `report_template_asx.md`

- `execution/foundry/`
  - `foundry_run.py` (conductor)
  - `ingest_prices.py` (market param: US|ASX)
  - `build_features.py` (writes parquet features)
  - `build_labels.py` (writes parquet labels for 1d/5d/20d)
  - `train_models.py` (logreg + tree)
  - `predict.py` (writes parquet predictions)
  - `calibrate.py` (Platt/Isotonic; writes calibrated probs)
  - `backtest_walkforward.py` (3–5y walk-forward)
  - `quality_gates.py` (enforces YAML gates)
  - `render_report.py` (markdown → html)
  - `publish_report.py` (copy to `docs/foundry/` or gh-pages)

- `data/foundry/` (parquet store)
  - `features/market=US/feature_set=v1/date=YYYY-MM-DD/part.parquet`
  - `features/market=ASX/feature_set=v1/date=YYYY-MM-DD/part.parquet`
  - `labels/market=US/horizon=5d/date=YYYY-MM-DD/part.parquet`
  - `predictions/market=US/run_id=YYYYMMDDHHMM/part.parquet`
  - `backtests/market=US/run_id=YYYYMMDDHHMM/part.parquet`
  - `diagnostics/market=US/run_id=.../calibration.parquet`

- `docs/foundry/`
  - `US/latest.md` + `US/latest.html`
  - `ASX/latest.md` + `ASX/latest.html`
  - archive by date.

### Reuse
- Keep Swing Book as-is.
- Reuse `execution/telegram_fmt.py` for all comms.

## Conductor: `execution/foundry/foundry_run.py`
Inputs:
- `--market US|ASX`
- `--mode pre|post`
- `--as-of YYYY-MM-DD` (optional)
- `--feature-set v1`

Pipeline (deterministic order):
1) Load universe list (directives/foundry/universe_<market>.txt)
2) Ingest daily OHLCV (+ benchmark proxies) for window needed.
3) Build features (write parquet).
4) Build labels (write parquet) for 1d/5d/20d.
5) Train baseline models (logreg + tree) OR load last model if unchanged.
6) Predict probabilities + expected return; write parquet.
7) Calibrate probabilities; write calibration diagnostics.
8) Walk-forward backtest summary (lightweight for MVP).
9) Quality gates:
   - coverage >= threshold
   - minimum rows
   - no lookahead checks
   - calibration error bounds
   - performance exceeds baseline margin
10) Render report (md + html), archive, and publish **only if gates pass**.
11) Notify Telegram with a short summary and links.

## Quality gates (MVP defaults)
Stored in `directives/foundry/quality_gates.yaml`.
- Coverage (price rows present) >= 95% tickers
- Min training rows per ticker >= 400
- Leakage checks: label date strictly > feature date for all horizons
- Calibration: slope within [0.7, 1.3], Brier <= threshold
- Backtest: AUC >= baseline + 0.01 (or hit-rate >= baseline + margin)

## OpenClaw cron schedule (PRD-aligned)
US:
- pre-open: 08:15 America/New_York
- post-close: 16:45 America/New_York

ASX:
- pre-open: 09:30 Australia/Sydney
- post-close: 16:30 Australia/Sydney

Each cron job runs:
- `./.venv/bin/python -u execution/foundry/foundry_run.py --market <...> --mode <...> --feature-set v1`

## Agent team integration (OpenClaw)
When gates fail repeatedly, OpenClaw spawns sub-agents:
- Data QA agent: diagnose missingness/coverage; propose data fixes.
- Modeling agent: adjust model config; improve calibration.
- Skeptic agent: hunt leakage, impl bugs, overfit.
- Report agent: improve clarity and operator usefulness.

Sub-agents propose patches; conductor reruns; publish only on pass.

## MVP rollout (1–2 weeks)
1) Create directory skeleton + configs.
2) Implement ingest_prices + feature/label pipeline for US only.
3) Implement baseline logreg + one tree model.
4) Implement report rendering + local publish.
5) Add quality gates + cron for US.
6) Repeat for ASX (decide OHLCV source if yfinance weak).

## Decisions needed from Jordan
- US universe seed list (20–50) or rule (e.g. watchlist file).
- ASX OHLCV source preference if yfinance gaps.
- Where to publish: existing GitHub Pages vs separate static page.
