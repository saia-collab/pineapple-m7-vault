#!/usr/bin/env python3
"""
m7_tidy.py — 4-Fala Topography Maintenance Daemon
Moves orphan root files into their dedicated rooms.
Standard-library only. Safe: dry-run by default, use --commit to execute.
"""
import argparse
import logging
import os
import shutil
import sqlite3
import sys
from pathlib import Path
from datetime import datetime

# ── Paths ────────────────────────────────────────────────────────────────────
VAULT = Path(__file__).resolve().parent.parent.parent   # 04_Tech_Lab/scripts/ -> vault root
KNOWLEDGE = VAULT / "03_Knowledge_Mat"
LAUNCHER_ARCHIVE = VAULT / "04_Tech_Lab" / "Launcher_Archive"
DB_PATH = VAULT / "04_Tech_Lab" / "m7_tracking.db"

# ── Routing rules ─────────────────────────────────────────────────────────────
# Each rule: (match_fn, destination_dir, label)
def _is_date_log(p: Path) -> bool:
    import re
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", p.name))

ROUTING_RULES = [
    (lambda p: p.name == "GROUNDING.md",                KNOWLEDGE,        "grounding-doc"),
    (lambda p: p.name == "MEMORY.md",                   KNOWLEDGE,        "memory-doc"),
    (lambda p: _is_date_log(p),                          KNOWLEDGE,        "date-log"),
    (lambda p: p.suffix.lower() == ".bat",               LAUNCHER_ARCHIVE, "bat-engine"),
]

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("m7_tidy")


# ── DB tracking ───────────────────────────────────────────────────────────────
def _init_db(conn: sqlite3.Connection) -> None:
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tidy_log (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                run_at    TEXT NOT NULL,
                src       TEXT NOT NULL,
                dst       TEXT NOT NULL,
                label     TEXT NOT NULL,
                dry_run   INTEGER NOT NULL
            )
        """)
        conn.commit()
    except Exception as exc:
        log.error("DB init failed — continuing without persistence: %s", exc)


def _record(conn: sqlite3.Connection, src: Path, dst: Path, label: str, dry_run: bool) -> None:
    try:
        conn.execute(
            "INSERT INTO tidy_log (run_at, src, dst, label, dry_run) VALUES (?,?,?,?,?)",
            (datetime.now().isoformat(timespec="seconds"), str(src), str(dst), label, int(dry_run)),
        )
        conn.commit()
    except Exception as exc:
        log.error("DB record failed for %s -> %s: %s", src.name, dst, exc)


# ── Core logic ────────────────────────────────────────────────────────────────
def collect_orphans(vault: Path) -> list[tuple[Path, Path, str]]:
    """Return list of (src, dest_dir, label) for each orphan root file."""
    moves: list[tuple[Path, Path, str]] = []
    try:
        candidates = [p for p in vault.iterdir() if p.is_file()]
    except Exception as exc:
        log.error("Cannot list vault root: %s", exc)
        return moves

    for p in sorted(candidates):
        # Never touch hidden or system files
        if p.name.startswith("."):
            continue
        for match_fn, dest_dir, label in ROUTING_RULES:
            try:
                if match_fn(p):
                    moves.append((p, dest_dir, label))
                    break
            except Exception as exc:
                log.error("Rule check failed for %s: %s", p.name, exc)
    return moves


def safe_move(src: Path, dest_dir: Path, dry_run: bool) -> Path | None:
    """Move src into dest_dir, auto-incrementing filename on collision. Returns dest path or None."""
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name

        # Resolve name collision without overwriting
        if dest.exists() and not dry_run:
            stem, suffix = src.stem, src.suffix
            counter = 1
            while dest.exists():
                dest = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        if dry_run:
            log.info("[DRY-RUN] %s  ->  %s", src, dest)
        else:
            shutil.move(str(src), str(dest))
            log.info("MOVED     %s  ->  %s", src.name, dest)
        return dest
    except PermissionError as exc:
        log.error("Permission denied moving %s: %s", src.name, exc)
    except OSError as exc:
        log.error("OS error moving %s: %s", src.name, exc)
    except Exception as exc:
        log.error("Unexpected error moving %s: %s", src.name, exc)
    return None


# ── Entry point ───────────────────────────────────────────────────────────────
def main() -> int:
    parser = argparse.ArgumentParser(description="M7 Tidy — vault root janitor")
    parser.add_argument("--commit", action="store_true", help="Actually move files (default: dry-run)")
    parser.add_argument("--vault", type=Path, default=VAULT, help="Override vault root path")
    args = parser.parse_args()

    vault: Path = args.vault.resolve()
    dry_run: bool = not args.commit

    log.info("=== M7 TIDY  vault=%s  mode=%s ===", vault, "DRY-RUN" if dry_run else "COMMIT")

    # DB connection — kept open for the run; failures are non-fatal
    conn: sqlite3.Connection | None = None
    try:
        conn = sqlite3.connect(str(DB_PATH))
        _init_db(conn)
    except Exception as exc:
        log.warning("Could not open tracking DB (%s) — moves will still execute.", exc)

    orphans = collect_orphans(vault)
    if not orphans:
        log.info("No orphan files found. Vault root is clean.")
        return 0

    log.info("Found %d orphan file(s) to route.", len(orphans))
    moved = 0
    failed = 0

    for src, dest_dir, label in orphans:
        dest = safe_move(src, dest_dir, dry_run)
        if dest is not None:
            moved += 1
            if conn:
                _record(conn, src, dest, label, dry_run)
        else:
            failed += 1

    if conn:
        try:
            conn.close()
        except Exception:
            pass

    log.info("=== DONE  moved=%d  failed=%d  dry_run=%s ===", moved, failed, dry_run)
    if dry_run:
        log.info("Re-run with --commit to apply changes.")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
