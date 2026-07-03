#!/usr/bin/env python3
"""
memory_sync.py — M7 Shared Memory Compiler & Sync Daemon
Rebuilds the [SYNC] sections of SHARED_MEMORY.md from authoritative source files.
Standard-library only. Safe: read-only on source files, write-only on SHARED_MEMORY.md.

Usage:
    python memory_sync.py           # single compile pass
    python memory_sync.py --watch   # loop every 60s (daemon mode)
    python memory_sync.py --log "claude_code" "wrote research brief" "10_Research_Stage"
"""
import argparse
import logging
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
VAULT = Path(__file__).resolve().parent.parent.parent
SHARED_MEM = VAULT / "03_Knowledge_Mat" / "SHARED_MEMORY.md"
GROUNDING  = VAULT / "03_Knowledge_Mat" / "GROUNDING.md"
MEMORY_SRC = VAULT / "03_Knowledge_Mat" / "MEMORY.md"
DAILY_LOGS = VAULT / "03_Knowledge_Mat" / "Daily_Logs"
DB_PATH    = VAULT / "04_Tech_Lab" / "m7_tracking.db"

LOG_TABLE_HEADER = "| UTC Timestamp | Agent | Action | Note |"
LOG_TABLE_SEP    = "|---|---|---|---|"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-7s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("memory_sync")


# ── DB ────────────────────────────────────────────────────────────────────────
def _db_connect() -> sqlite3.Connection | None:
    try:
        conn = sqlite3.connect(str(DB_PATH))
        conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_log (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                ts         TEXT NOT NULL,
                agent      TEXT NOT NULL,
                action     TEXT NOT NULL,
                note       TEXT
            )
        """)
        conn.commit()
        return conn
    except Exception as exc:
        log.warning("DB unavailable (%s) — log entries will still write to SHARED_MEMORY.md", exc)
        return None


def _db_record(conn: sqlite3.Connection | None, ts: str, agent: str, action: str, note: str) -> None:
    if conn is None:
        return
    try:
        conn.execute(
            "INSERT INTO agent_log (ts, agent, action, note) VALUES (?,?,?,?)",
            (ts, agent, action, note),
        )
        conn.commit()
    except Exception as exc:
        log.error("DB write failed: %s", exc)


# ── Source extraction ─────────────────────────────────────────────────────────
def _read_safe(path: Path, default: str = "") -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        log.warning("Cannot read %s: %s", path, exc)
        return default


def _extract_section(md: str, heading: str) -> str:
    """Extract content under a ## heading until the next ##."""
    try:
        pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
        m = re.search(pattern, md, re.MULTILINE | re.DOTALL)
        return m.group(1).strip() if m else ""
    except Exception:
        return ""


def _latest_daily_log() -> str:
    """Return content of the most recent date-log file."""
    try:
        logs = sorted(DAILY_LOGS.glob("????-??-??.md"), reverse=True)
        if logs:
            content = logs[0].read_text(encoding="utf-8").strip()
            return f"**Latest log ({logs[0].stem}):**\n\n{content}" if content else ""
        return ""
    except Exception as exc:
        log.warning("Could not read daily logs: %s", exc)
        return ""


# ── SHARED_MEMORY.md rebuild ──────────────────────────────────────────────────
def _current_log_rows(shared_text: str) -> list[str]:
    """Extract existing log table rows from SHARED_MEMORY.md."""
    try:
        rows = []
        in_log = False
        for line in shared_text.splitlines():
            if line.strip() == LOG_TABLE_HEADER:
                in_log = True
                continue
            if in_log and line.strip() == LOG_TABLE_SEP:
                continue
            if in_log and line.startswith("|") and "|" in line[1:]:
                rows.append(line)
            elif in_log and line.startswith("##"):
                break
        return rows
    except Exception:
        return []


def _build_log_row(ts: str, agent: str, action: str, note: str) -> str:
    return f"| {ts} | {agent} | {action} | {note} |"


def append_log_entry(agent: str, action: str, note: str) -> None:
    """Append a single agent log entry to SHARED_MEMORY.md and DB."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    row = _build_log_row(ts, agent, action, note)

    conn = _db_connect()
    _db_record(conn, ts, agent, action, note)
    if conn:
        try:
            conn.close()
        except Exception:
            pass

    try:
        text = _read_safe(SHARED_MEM)
        if LOG_TABLE_HEADER in text:
            # Insert row immediately after the separator line
            lines = text.splitlines()
            insert_at = None
            for i, line in enumerate(lines):
                if line.strip() == LOG_TABLE_SEP and i > 0 and lines[i - 1].strip() == LOG_TABLE_HEADER:
                    insert_at = i + 1
                    break
            if insert_at is not None:
                lines.insert(insert_at, row)
                SHARED_MEM.write_text("\n".join(lines) + "\n", encoding="utf-8")
                log.info("Log entry appended: [%s] %s — %s", agent, action, note)
                return
        # Fallback: just append to end
        with SHARED_MEM.open("a", encoding="utf-8") as f:
            f.write(f"\n{row}\n")
        log.info("Log entry appended (fallback): [%s] %s", agent, action)
    except Exception as exc:
        log.error("Failed to append log entry: %s", exc)


def compile_shared_memory() -> bool:
    """Rebuild [SYNC] sections of SHARED_MEMORY.md from source files."""
    log.info("Compiling SHARED_MEMORY.md from source files...")

    try:
        existing = _read_safe(SHARED_MEM)
        existing_rows = _current_log_rows(existing)

        grounding_text = _read_safe(GROUNDING)
        memory_text    = _read_safe(MEMORY_SRC)
        daily_note     = _latest_daily_log()

        # Pull dynamic sections from sources
        metrics = _extract_section(grounding_text, "4. HIGH-VALUE METRICS")
        guardrails = _extract_section(grounding_text, "5. EXECUTION GUARDRAILS")
        identity_extra = _extract_section(memory_text, "Identity")
        session_log = _extract_section(memory_text, "Session log")

        compile_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        log_rows = "\n".join(existing_rows) if existing_rows else _build_log_row(
            compile_ts, "memory_sync", "INITIAL_COMPILE", "First compilation"
        )

        # Build the dynamic supplement section
        dynamic_block = ""
        if metrics:
            dynamic_block += f"\n## [SYNC] LIVE METRICS (from GROUNDING.md)\n\n{metrics}\n"
        if guardrails:
            dynamic_block += f"\n## [SYNC] EXECUTION GUARDRAILS (from GROUNDING.md)\n\n{guardrails}\n"
        if daily_note:
            dynamic_block += f"\n## [SYNC] DAILY LOG SUMMARY\n\n{daily_note}\n"
        if session_log:
            dynamic_block += f"\n## [SYNC] VAULT SESSION LOG\n\n{session_log}\n"

        # Read existing SHARED_MEMORY up to the AGENT LOG section, preserve it, splice dynamic
        static_top = existing
        if "## [SYNC] LIVE METRICS" in existing:
            static_top = existing[:existing.index("## [SYNC] LIVE METRICS")]
        elif "## AGENT LOG" in existing:
            static_top = existing[:existing.index("## AGENT LOG")]

        # Rebuild compile timestamp in frontmatter
        static_top = re.sub(
            r"last_compiled: .*",
            f"last_compiled: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
            static_top,
        )

        final = (
            static_top.rstrip()
            + "\n"
            + dynamic_block
            + "\n---\n\n"
            + "## AGENT LOG\n"
            + "<!-- APPEND-ONLY — memory_sync.py prepends new entries. Do not reorder or delete. -->\n\n"
            + f"{LOG_TABLE_HEADER}\n{LOG_TABLE_SEP}\n"
            + log_rows
            + "\n"
        )

        SHARED_MEM.write_text(final, encoding="utf-8")
        log.info("SHARED_MEMORY.md compiled successfully (%d bytes)", len(final.encode("utf-8")))
        return True

    except Exception as exc:
        log.error("Compile failed: %s", exc)
        return False


# ── Entry point ───────────────────────────────────────────────────────────────
def main() -> int:
    parser = argparse.ArgumentParser(description="M7 Memory Sync — shared memory compiler")
    parser.add_argument("--watch", action="store_true", help="Daemon mode: recompile every 60s")
    parser.add_argument("--log", nargs=3, metavar=("AGENT", "ACTION", "NOTE"),
                        help="Append one log entry then exit")
    args = parser.parse_args()

    if args.log:
        agent, action, note = args.log
        append_log_entry(agent, action, note)
        return 0

    if args.watch:
        log.info("Daemon mode — recompiling every 60s. Ctrl+C to stop.")
        while True:
            try:
                compile_shared_memory()
            except Exception as exc:
                log.error("Daemon cycle error: %s", exc)
            try:
                time.sleep(60)
            except KeyboardInterrupt:
                log.info("Daemon stopped.")
                return 0
    else:
        return 0 if compile_shared_memory() else 1


if __name__ == "__main__":
    sys.exit(main())
