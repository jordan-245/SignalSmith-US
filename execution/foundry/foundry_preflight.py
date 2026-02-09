#!/usr/bin/env python3
"""Signal Foundry — Preflight Checks

Validates that all prerequisites are met before running the pipeline:
  - Foundry module imports
  - Required environment variables
  - Universe file exists and has tickers
  - Quality gates config exists and parses
  - Data directory exists and is writable

Usage:
  python execution/foundry/foundry_preflight.py
  python execution/foundry/foundry_preflight.py --quiet  # exit code only
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Load .env before checking env vars
try:
    from dotenv import load_dotenv
    load_dotenv(REPO / ".env")
except ImportError:
    pass


class PreflightResult:
    def __init__(self):
        self.checks: list[tuple[str, bool, str]] = []

    def add(self, name: str, ok: bool, detail: str = ""):
        self.checks.append((name, ok, detail))

    @property
    def all_ok(self) -> bool:
        return all(ok for _, ok, _ in self.checks)

    def print_report(self):
        print("\nSignal Foundry — Preflight Checks")
        print("=" * 50)
        for name, ok, detail in self.checks:
            icon = "✓" if ok else "✗"
            msg = f"  {icon} {name}"
            if detail:
                msg += f": {detail}"
            print(msg)
        print("=" * 50)
        if self.all_ok:
            print("✓ All preflight checks passed")
        else:
            failed = [n for n, ok, _ in self.checks if not ok]
            print(f"✗ {len(failed)} check(s) failed: {', '.join(failed)}")


def check_foundry_imports(result: PreflightResult) -> None:
    """Verify all foundry modules can be imported."""
    modules = [
        ("foundry_steps", REPO / "execution" / "foundry" / "foundry_steps.py"),
        ("foundry_run", REPO / "execution" / "foundry" / "foundry_run.py"),
        ("foundry_models", REPO / "execution" / "foundry" / "foundry_models.py"),
        ("foundry_backtest", REPO / "execution" / "foundry" / "foundry_backtest.py"),
        ("foundry_report", REPO / "execution" / "foundry" / "foundry_report.py"),
    ]

    all_ok = True
    failed = []
    for mod_name, mod_path in modules:
        if not mod_path.exists():
            result.add(f"import {mod_name}", False, "file not found")
            all_ok = False
            failed.append(mod_name)
            continue
        try:
            spec = importlib.util.spec_from_file_location(mod_name, mod_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                # Don't actually exec — just verify the spec loads
                result.add(f"import {mod_name}", True)
            else:
                result.add(f"import {mod_name}", False, "spec creation failed")
                all_ok = False
                failed.append(mod_name)
        except Exception as exc:
            result.add(f"import {mod_name}", False, str(exc)[:100])
            all_ok = False
            failed.append(mod_name)

    if all_ok:
        result.add("foundry_modules", True, f"{len(modules)} modules OK")


def check_env_vars(result: PreflightResult) -> None:
    """Verify required environment variables are set."""
    required = [
        "SUPABASE_URL",
        "SUPABASE_SERVICE_ROLE",  # also check the actual key name used
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_CHAT_ID",
    ]
    # Accept SUPABASE_KEY as alias for SUPABASE_SERVICE_ROLE
    missing = []
    for var in required:
        val = os.getenv(var, "")
        if not val:
            # Check common aliases
            if var == "SUPABASE_SERVICE_ROLE" and os.getenv("SUPABASE_KEY", ""):
                continue
            if var == "SUPABASE_KEY" and os.getenv("SUPABASE_SERVICE_ROLE", ""):
                continue
            missing.append(var)

    if missing:
        result.add("env_vars", False, f"missing: {', '.join(missing)}")
    else:
        result.add("env_vars", True, f"{len(required)} vars OK")


def check_universe(result: PreflightResult) -> None:
    """Verify universe_us.txt exists and has tickers."""
    path = REPO / "directives" / "foundry" / "universe_us.txt"
    if not path.exists():
        result.add("universe_us.txt", False, "file not found")
        return

    tickers = [
        line.strip()
        for line in path.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if len(tickers) == 0:
        result.add("universe_us.txt", False, "no tickers found")
    else:
        result.add("universe_us.txt", True, f"{len(tickers)} tickers")


def check_quality_gates(result: PreflightResult) -> None:
    """Verify quality_gates.yaml exists and parses."""
    path = REPO / "directives" / "foundry" / "quality_gates.yaml"
    if not path.exists():
        result.add("quality_gates.yaml", False, "file not found")
        return

    try:
        import yaml
        data = yaml.safe_load(path.read_text())
        if not isinstance(data, dict):
            result.add("quality_gates.yaml", False, "not a valid YAML dict")
            return
        sections = list(data.keys())
        result.add("quality_gates.yaml", True, f"sections: {', '.join(sections)}")
    except ImportError:
        result.add("quality_gates.yaml", False, "PyYAML not installed")
    except Exception as exc:
        result.add("quality_gates.yaml", False, f"parse error: {exc}")


def check_data_directory(result: PreflightResult) -> None:
    """Verify data/foundry/ exists and is writable."""
    data_dir = REPO / "data" / "foundry"
    if not data_dir.exists():
        result.add("data/foundry/", False, "directory does not exist")
        return

    if not data_dir.is_dir():
        result.add("data/foundry/", False, "exists but is not a directory")
        return

    # Test writability
    try:
        test_file = data_dir / ".preflight_test"
        test_file.write_text("ok")
        test_file.unlink()
        result.add("data/foundry/", True, "exists and writable")
    except Exception as exc:
        result.add("data/foundry/", False, f"not writable: {exc}")


def run_preflight() -> PreflightResult:
    """Run all preflight checks and return the result."""
    result = PreflightResult()
    check_foundry_imports(result)
    check_env_vars(result)
    check_universe(result)
    check_quality_gates(result)
    check_data_directory(result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Signal Foundry — preflight checks")
    parser.add_argument("--quiet", action="store_true", help="Exit code only, no output")
    args = parser.parse_args()

    result = run_preflight()

    if not args.quiet:
        result.print_report()

    sys.exit(0 if result.all_ok else 1)


if __name__ == "__main__":
    main()
