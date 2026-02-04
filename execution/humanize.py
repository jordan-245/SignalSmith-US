"""Human-friendly messaging helpers.

Goals:
- Consistent voice + structure across notifications.
- Reduce noise: prefer saying nothing over repetitive "OK" updates.

Config via env:
- SIGNALSMITH_VIBE: one of {minimalist_operator,friendly_coworker,formal_risk_officer,snarky_analyst}
- SIGNALSMITH_NOTIFY_LEVEL: {low,medium,high}

These helpers are intentionally lightweight (no external deps).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class Style:
    vibe: str
    notify_level: str


def style() -> Style:
    return Style(
        vibe=os.getenv("SIGNALSMITH_VIBE", "friendly_coworker").strip() or "friendly_coworker",
        notify_level=os.getenv("SIGNALSMITH_NOTIFY_LEVEL", "low").strip() or "low",
    )


def heading(tag: str) -> str:
    s = style()
    if s.vibe == "formal_risk_officer":
        return f"[{tag}]"
    if s.vibe == "minimalist_operator":
        return f"[{tag}]"
    if s.vibe == "snarky_analyst":
        return f"[{tag}]"
    return f"[{tag}]"


def bullets(lines: Iterable[str]) -> str:
    out = []
    for ln in lines:
        ln = (ln or "").strip()
        if not ln:
            continue
        out.append(f"- {ln}")
    return "\n".join(out)


def brief(
    tag: str,
    what: str,
    why: Optional[str] = None,
    next_step: Optional[str] = None,
    need: Optional[str] = None,
) -> str:
    """Return a compact, consistent message."""
    parts = [f"{heading(tag)} {what.strip()}".strip()]
    bl = []
    if why:
        bl.append(f"Why it matters: {why.strip()}")
    if next_step:
        bl.append(f"Next: {next_step.strip()}")
    if need:
        bl.append(f"Need from you: {need.strip()}")
    if bl:
        parts.append(bullets(bl))
    return "\n".join(parts).strip() + "\n"


def should_notify(kind: str) -> bool:
    """Coarse notification gating.

    kind examples: ok, change, action, warning, error
    """
    lvl = style().notify_level
    if lvl == "high":
        return True
    if lvl == "medium":
        return kind in {"change", "action", "warning", "error"}
    # low
    return kind in {"action", "warning", "error"}
