#!/usr/bin/env bash
set -euo pipefail

# Run the baseline daily wrapper with a 365-day lookback.
# Usage: ./run_baseline.sh [--lookback-days N] [--cash X] [--end-date YYYY-MM-DD]

cd "$(dirname "$0")"
python execution/baseline_daily_runner.py "$@"
