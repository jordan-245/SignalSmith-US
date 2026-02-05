"""Publish the public dashboard to the gh-pages branch (deterministic).

Why:
- Avoid constant commits/rebases on master.
- GitHub Pages can serve the gh-pages branch directly.

Flow:
1) Generate a public-safe snapshot into a temp dir (no secrets).
2) Copy artifacts to a git worktree checked out on gh-pages.
3) Commit + push only if changed.

Artifacts published (to repo root on gh-pages):
- index.html
- dashboard.json
- .nojekyll

Usage:
  python execution/publish_to_gh_pages.py

Requires:
- git remote 'origin' configured with push access.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WORKTREE_DIR = Path(os.getenv("GH_PAGES_WORKTREE", str(REPO / ".gh-pages-worktree")))
BRANCH = os.getenv("GH_PAGES_BRANCH", "gh-pages")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    p = subprocess.run(cmd, cwd=str(cwd or REPO), check=False, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(cmd)}\nstdout: {p.stdout}\nstderr: {p.stderr}")
    return (p.stdout or "").strip()


def ensure_worktree() -> None:
    # If worktree already exists, ensure it is on the right branch.
    if WORKTREE_DIR.exists() and (WORKTREE_DIR / ".git").exists():
        return

    WORKTREE_DIR.parent.mkdir(parents=True, exist_ok=True)

    # Fetch remote refs.
    run(["git", "fetch", "origin", "--prune"])

    # Create gh-pages branch if it doesn't exist locally.
    branches = run(["git", "branch", "--list", BRANCH])
    if not branches.strip():
        # If remote branch exists, create local tracking branch; else create orphan branch.
        remote = run(["git", "ls-remote", "--heads", "origin", BRANCH])
        if remote.strip():
            run(["git", "branch", BRANCH, f"origin/{BRANCH}"])
        else:
            # Create orphan branch via a temporary worktree init.
            tmp = tempfile.mkdtemp(prefix="gh-pages-init-")
            try:
                run(["git", "worktree", "add", tmp, "--detach"])
                run(["git", "-C", tmp, "checkout", "--orphan", BRANCH])
                # Remove all tracked files in orphan.
                run(["git", "-C", tmp, "rm", "-rf", "."], cwd=Path(tmp))
                (Path(tmp) / ".nojekyll").write_text("", encoding="utf-8")
                run(["git", "-C", tmp, "add", "-A"], cwd=Path(tmp))
                run(["git", "-C", tmp, "commit", "-m", "Initialize gh-pages"], cwd=Path(tmp))
                run(["git", "push", "-u", "origin", BRANCH], cwd=Path(tmp))
            finally:
                # Clean up temp worktree
                run(["git", "worktree", "remove", "--force", tmp])
                shutil.rmtree(tmp, ignore_errors=True)

    # Add the worktree
    run(["git", "worktree", "add", str(WORKTREE_DIR), BRANCH])


def main() -> None:
    ensure_worktree()

    with tempfile.TemporaryDirectory(prefix="signalsmith-dashboard-") as td:
        out_dir = Path(td)
        env = os.environ.copy()
        env["DASHBOARD_OUT_DIR"] = str(out_dir)

        # Generate snapshot to temp
        p = subprocess.run(
            [str(REPO / ".venv" / "bin" / "python"), str(REPO / "execution" / "publish_dashboard_snapshot.py")],
            cwd=str(REPO),
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        if p.returncode != 0:
            raise RuntimeError(f"snapshot failed\nstdout: {p.stdout}\nstderr: {p.stderr}")

        src_index = out_dir / "index.html"
        src_json = out_dir / "dashboard.json"
        if not src_index.exists() or not src_json.exists():
            raise RuntimeError("snapshot did not produce index.html/dashboard.json")

        # Copy to gh-pages worktree root
        shutil.copy2(src_index, WORKTREE_DIR / "index.html")
        shutil.copy2(src_json, WORKTREE_DIR / "dashboard.json")
        (WORKTREE_DIR / ".nojekyll").write_text("", encoding="utf-8")

        # Commit if changed
        run(["git", "-C", str(WORKTREE_DIR), "add", "-A"])
        status = run(["git", "-C", str(WORKTREE_DIR), "status", "--porcelain"])
        if not status.strip():
            print("HEARTBEAT_OK")
            return

        run(["git", "-C", str(WORKTREE_DIR), "commit", "-m", "Update public dashboard snapshot"])
        run(["git", "-C", str(WORKTREE_DIR), "push", "origin", BRANCH])
        print("[ok] published to gh-pages")


if __name__ == "__main__":
    main()
