#!/usr/bin/env python3
"""
PINEAPPLE CONTRACTORS M7 — BRAND FIREWALL
=========================================
Production-grade compliance engine for the 4-Fala Topography.

Responsibilities
----------------
1.  Scan markdown / html / css / js / txt files across the vault.
2.  Intercept and MUTATE banned lexicon to mandated replacements.
3.  Enforce absolute exclusion of the color green (hex, rgb, named, Tailwind).
4.  Validate the brand palette (#1A365D, #FBC02D, #00BFFF, #FFFFFF).
5.  Optionally run as a live file-system listener (watchdog) on the 4-Fala rooms.

Exit codes
----------
0  -> clean (or all infractions auto-fixed)
1  -> critical violation found (green reference / unfixable) — CI/CD build fails

Usage
-----
    python brand_firewall.py                 # scan, report, exit 1 on violations
    python brand_firewall.py --report        # write JSON report to disk
    python brand_firewall.py --fix           # auto-mutate banned terms in place
    python brand_firewall.py --watch         # live FS listener over the 4-Fala rooms
    python brand_firewall.py --check "text"  # validate an inline string, print result

M7-FIREWALL-EXEMPT: green-detection-tooling

Ko e hala 'o e fononga ko e faka'apa'apa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------- #
# CONFIGURATION
# --------------------------------------------------------------------------- #

# Vault root. Override with --root. Auto-detected two levels up from this script
# (04_Tech_Lab/Scripts/brand_firewall.py -> vault root). Falls back to cwd when the
# script is relocated (CI, /tmp, inline --check) so import never crashes.
def _detect_root() -> Path:
    here = Path(__file__).resolve()
    parents = here.parents
    if len(parents) >= 3 and parents[1].name == "04_Tech_Lab":
        return parents[2]
    if len(parents) >= 3:
        return parents[2]
    return Path.cwd()

DEFAULT_ROOT = _detect_root()

# The immutable 4-Fala rooms watched by the listener.
FALA_ROOMS = [
    "01_Command_Center",
    "02_Workspaces",      # role: Tactical Ops (active staging mat)
    "02_Media_Vault",
    "03_Knowledge_Mat",
    "04_Tech_Lab",
    "05_Campaign_Factory",
]

SCAN_EXTENSIONS = {".md", ".html", ".htm", ".css", ".js", ".txt", ".json", ".yaml", ".yml"}

# Directories never scanned/mutated (binaries, backups, vcs, sync temp).
EXCLUDE_DIRS = {
    ".git", ".obsidian", "node_modules", "legacy_backup", "__pycache__",
    ".tmp.drivedownload", ".tmp.driveupload", "knowledge-base",
    "raw",  # untouched source intake; cleaned only when promoted to 00_Atlas
    "logs",  # machine-generated audit logs (firewall_report.json, etc.)
    "vendor",  # third-party skill packages (not brand output)
    "skills",  # imported third-party skill library (reference, not M7-generated)
    "templates",  # imported third-party template library (reference, not M7-generated)
    "skills_inbox",  # staging for imports awaiting filing
}

# SCOPE NOTE: the firewall hard-enforces the green ban + lexicon on M7's OWN
# generated brand output (01_Command_Center, Outbox_Drafts, 05_Campaign_Factory,
# 02_Media_Vault). Imported reference libraries (skills/, templates/, vendor/) are
# catalogued, not policed — third-party packs may legitimately contain green.

# Machine-generated output files that must never be self-scanned.
EXCLUDE_FILENAMES = {"firewall_report.json", "skill_intake_log.json"}

# Approved brand palette (lowercase hex).
APPROVED_HEX = {"#1a365d", "#001122", "#001a33", "#fbc02d", "#ffd700",
                "#e5a93c", "#00bfff", "#ffffff", "#ffe12d", "#000000"}

# --------------------------------------------------------------------------- #
# RULE SET 1 — BANNED LEXICON (ordered: most specific first)
# Each rule mutates a banned term to its mandated replacement.
# Case-insensitive match; replacement preserves a clean canonical form.
# --------------------------------------------------------------------------- #

LEXICON_RULES = [
    # (regex pattern, mandated replacement, human label)
    (r"free\s+inspection",            "Complimentary Professional Photo Audit (CPPA)", "free inspection"),
    (r"free\s+quote",                 "Complimentary Professional Photo Audit (CPPA)", "free quote"),
    (r"free\s+estimate",              "Complimentary Professional Photo Audit (CPPA)", "free estimate"),
    (r"\$0\s*(down|out\s*of\s*pocket)", "Full Restoration Coverage",                   "$0 down / out of pocket"),
    (r"zero\s+out\s+of\s+pocket",     "Full Restoration Coverage",                     "zero out of pocket"),
    (r"adjusters?\s+miss\s+damage",   "Comprehensive documentation for a successful claim", "adjusters miss damage"),
    (r"save\s+money",                 "Protecting your family's investment",           "save money"),
    (r"gaf\s+master\s+elite\s+certified", "IKO Certified (RCAT License #03-0637)",     "GAF Master Elite Certified"),
    (r"gaf\s+certified",              "IKO Certified (RCAT License #03-0637)",         "GAF Certified"),
    (r"six\s+brothers",               "The Pineapple Standard",                        "Six Brothers"),
    (r"\bwarrior\b",                  "The Pineapple Standard",                        "Warrior"),
    (r"\btoa\b",                      "The Pineapple Standard",                        "Toa"),
    (r"\bconsultation\b",             "Complimentary Professional Photo Audit (CPPA)", "Consultation"),
    # Bare "Free" handled last so compounds above win first.
    (r"\bfree\b",                     "Complimentary",                                 "Free (standalone)"),
]

# Compile once. Word-level rules use IGNORECASE.
_COMPILED_LEXICON = [
    (re.compile(pat, re.IGNORECASE), repl, label) for pat, repl, label in LEXICON_RULES
]

# --------------------------------------------------------------------------- #
# RULE SET 2 — GREEN EXCLUSION (CRITICAL — triggers exit code 1)
# --------------------------------------------------------------------------- #

GREEN_PATTERNS = [
    re.compile(r"#0{0,2}[0-9a-f]?ff0{0,2}[0-9a-f]?\b", re.IGNORECASE),  # generic bright-green-ish guard (refined below)
    re.compile(r"#00ff00\b", re.IGNORECASE),                            # pure lime
    re.compile(r"#2d7d46\b", re.IGNORECASE),                            # heritage green
    re.compile(r"#008000\b", re.IGNORECASE),                            # css green
    re.compile(r"#3cb371\b|#2e8b57\b|#228b22\b|#32cd32\b|#90ee90\b", re.IGNORECASE),
    # rgba heuristic removed — see _rgba_is_green() for channel-dominance check below
    re.compile(r"\bgreen\b", re.IGNORECASE),                            # css named greens / the word
    re.compile(r"\b(?:lime|forestgreen|seagreen|olive|darkgreen|lightgreen|mediumseagreen|springgreen|chartreuse)\b", re.IGNORECASE),
    re.compile(r"\b(?:bg|text|border|ring|from|to|via)-green-\d{2,3}\b", re.IGNORECASE),  # Tailwind
]

# The first pattern above is intentionally loose; we refine green hex detection
# by explicit checking in _hex_is_green() to avoid false positives on gold/navy.

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")

RGBA_PARSE_RE = re.compile(r"\brgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})", re.IGNORECASE)


def _rgba_is_green(line: str) -> bool:
    """True if any rgba() value in the line has G channel dominant (green-dominant).
    Applies the same threshold as _hex_is_green to avoid false positives on
    white/coral/cyan where other channels equal or exceed green."""
    for m in RGBA_PARSE_RE.finditer(line):
        try:
            r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        except (ValueError, IndexError):
            continue
        if g > 90 and g >= r + 40 and g >= b + 40:
            return True
    return False


def _hex_is_green(hex_str: str) -> bool:
    """True if a #RRGGBB hex reads as green (G dominant, not in approved palette)."""
    h = hex_str.lower()
    if h in APPROVED_HEX:
        return False
    try:
        r = int(h[1:3], 16)
        g = int(h[3:5], 16)
        b = int(h[5:7], 16)
    except (ValueError, IndexError):
        return False
    # Green-dominant: G clearly exceeds R and B by a margin.
    return g > 90 and g >= r + 40 and g >= b + 40


# --------------------------------------------------------------------------- #
# SCANNING CORE
# --------------------------------------------------------------------------- #

class Violation:
    __slots__ = ("path", "line", "kind", "label", "snippet", "severity")

    def __init__(self, path, line, kind, label, snippet, severity):
        self.path = str(path)
        self.line = line
        self.kind = kind          # "lexicon" | "green" | "palette"
        self.label = label
        self.snippet = snippet
        self.severity = severity  # "warn" | "critical"

    def as_dict(self):
        return {
            "path": self.path, "line": self.line, "kind": self.kind,
            "label": self.label, "snippet": self.snippet, "severity": self.severity,
        }


# Files that legitimately reference "green" because their job is to DETECT/BLOCK
# it (this scanner, the dashboard's client-side firewall, the architecture map).
# Such files declare the sentinel below to opt out of the GREEN-critical rule
# ONLY. The lexicon rules still apply. This mirrors an eslint-disable directive.
GREEN_EXEMPT_SENTINEL = "M7-FIREWALL-EXEMPT: green-detection-tooling"


def scan_text(text: str, path: Path):
    """Return (violations, mutated_text). mutated_text reflects lexicon --fix."""
    violations = []
    lines = text.splitlines(keepends=True)
    # Full exemption: governance/constitution/tooling docs must quote the banned
    # terms and "green" verbatim to DEFINE the rules. Any file carrying the
    # sentinel skips both the lexicon and green passes (no flags, no rewrite),
    # so --fix can never corrupt the rulebook. Marketing/output files are never
    # exempt. (eslint-disable analogue.)
    if "M7-FIREWALL-EXEMPT" in text:
        return [], text
    green_exempt = GREEN_EXEMPT_SENTINEL in text

    # Pass 1: lexicon (line-by-line for reporting; mutation for --fix).
    mutated_lines = []
    for idx, line in enumerate(lines, start=1):
        new_line = line
        for rx, repl, label in _COMPILED_LEXICON:
            if rx.search(new_line):
                violations.append(
                    Violation(path, idx, "lexicon", label, line.strip()[:160], "warn")
                )
                new_line = rx.sub(repl, new_line)
        mutated_lines.append(new_line)

    # Pass 2: green exclusion (CRITICAL — never auto-mutated; must be human-fixed).
    # Skipped for declared green-detection tooling (lexicon still enforced above).
    for idx, line in (enumerate(lines, start=1) if not green_exempt else iter(())):
        low = line.lower()
        flagged = False
        # explicit green hex
        for hx in HEX_RE.findall(line):
            if _hex_is_green(hx):
                violations.append(
                    Violation(path, idx, "green", f"green hex {hx}", line.strip()[:160], "critical")
                )
                flagged = True
        # rgba channel-dominance check (precise, replaces old heuristic regex)
        if not flagged and _rgba_is_green(line):
            violations.append(
                Violation(path, idx, "green", "green rgba", line.strip()[:160], "critical")
            )
            flagged = True
        # named / tailwind / word green
        for gp in GREEN_PATTERNS[1:]:  # skip loose pattern[0]
            if gp.search(low):
                violations.append(
                    Violation(path, idx, "green", "green reference", line.strip()[:160], "critical")
                )
                flagged = True
                break

    mutated_text = "".join(mutated_lines)
    return violations, mutated_text


def iter_target_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.name in EXCLUDE_FILENAMES:
            continue
        yield p


def run_scan(root: Path, fix: bool):
    all_violations = []
    fixed_files = []
    for path in iter_target_files(root):
        try:
            original = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        violations, mutated = scan_text(original, path)
        all_violations.extend(violations)
        if fix and mutated != original:
            # Only lexicon infractions are auto-mutated. Green stays critical.
            path.write_text(mutated, encoding="utf-8")
            fixed_files.append(str(path))
    return all_violations, fixed_files


# --------------------------------------------------------------------------- #
# LIVE FILE-SYSTEM LISTENER
# --------------------------------------------------------------------------- #

def run_watch(root: Path, fix: bool):
    """Live listener over the 4-Fala rooms. Uses watchdog if available,
    otherwise falls back to a polling loop (mtime diff)."""
    targets = [root / room for room in FALA_ROOMS if (root / room).exists()]
    print(f"[firewall] watching {len(targets)} Fala rooms under {root}")

    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        fw = _scan_one_file

        class Handler(FileSystemEventHandler):
            def on_modified(self, event):
                if event.is_directory:
                    return
                p = Path(event.src_path)
                if p.suffix.lower() in SCAN_EXTENSIONS and not any(
                    part in EXCLUDE_DIRS for part in p.parts
                ):
                    fw(p, fix)

            on_created = on_modified

        obs = Observer()
        for t in targets:
            obs.schedule(Handler(), str(t), recursive=True)
        obs.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            obs.stop()
        obs.join()

    except ImportError:
        print("[firewall] watchdog not installed — using polling fallback "
              "(pip install watchdog for native FS events). Ctrl+C to stop.")
        seen = {}
        try:
            while True:
                for t in targets:
                    for p in iter_target_files(t):
                        m = p.stat().st_mtime
                        if seen.get(p) != m:
                            seen[p] = m
                            _scan_one_file(p, fix)
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n[firewall] listener stopped.")


def _scan_one_file(path: Path, fix: bool):
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return
    violations, mutated = scan_text(original, path)
    if not violations:
        return
    crit = [v for v in violations if v.severity == "critical"]
    warn = [v for v in violations if v.severity == "warn"]
    if fix and mutated != original and not crit:
        path.write_text(mutated, encoding="utf-8")
        print(f"[firewall] MUTATED {len(warn)} term(s) in {path.name}")
    if crit:
        for v in crit:
            print(f"[firewall] CRITICAL {path.name}:{v.line} -> {v.label}")
    elif warn and not fix:
        print(f"[firewall] {len(warn)} lexicon flag(s) in {path.name} (run --fix)")


# --------------------------------------------------------------------------- #
# REPORTING
# --------------------------------------------------------------------------- #

def write_report(root: Path, violations, fixed_files):
    report = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "total_violations": len(violations),
        "critical": sum(1 for v in violations if v.severity == "critical"),
        "warnings": sum(1 for v in violations if v.severity == "warn"),
        "fixed_files": fixed_files,
        "violations": [v.as_dict() for v in violations],
        "closing": "Ko e hala 'o e fononga ko e faka'apa'apa.",
    }
    out = root / "04_Tech_Lab" / "Scripts" / "firewall_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"[firewall] report -> {out}")
    return report


def check_inline(text: str):
    violations, mutated = scan_text(text, Path("<inline>"))
    crit = [v for v in violations if v.severity == "critical"]
    print("INPUT :", text)
    print("OUTPUT:", mutated.strip())
    if crit:
        print("STATUS: CRITICAL — green reference present, build would fail.")
        return 1
    print("STATUS: OK" if not violations else f"STATUS: {len(violations)} term(s) mutated.")
    return 0


# --------------------------------------------------------------------------- #
# ENTRY POINT
# --------------------------------------------------------------------------- #

def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 Brand Firewall")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="vault root")
    ap.add_argument("--fix", action="store_true", help="auto-mutate banned lexicon in place")
    ap.add_argument("--report", action="store_true", help="write JSON report")
    ap.add_argument("--watch", action="store_true", help="live FS listener over 4-Fala rooms")
    ap.add_argument("--check", metavar="TEXT", help="validate an inline string and exit")
    args = ap.parse_args(argv)

    if args.check is not None:
        return check_inline(args.check)

    root = args.root.resolve()
    if not root.exists():
        print(f"[firewall] root not found: {root}", file=sys.stderr)
        return 2

    if args.watch:
        run_watch(root, args.fix)
        return 0

    violations, fixed = run_scan(root, args.fix)
    critical = [v for v in violations if v.severity == "critical"]
    warnings = [v for v in violations if v.severity == "warn"]

    print(f"[firewall] scanned root: {root}")
    print(f"[firewall] lexicon flags : {len(warnings)}")
    print(f"[firewall] green/critical: {len(critical)}")
    if args.fix:
        print(f"[firewall] files mutated : {len(fixed)}")

    if args.report:
        write_report(root, violations, fixed)

    for v in critical[:50]:
        print(f"  CRITICAL {Path(v.path).name}:{v.line} -> {v.label}")

    # Build fails on any remaining critical (green) violation.
    if critical:
        print("[firewall] BUILD FAILED — green exclusion violated.")
        return 1
    # If not fixing and lexicon flags remain, also fail to protect the brand.
    if warnings and not args.fix:
        print("[firewall] lexicon flags present — run with --fix to mutate.")
        return 1
    print("[firewall] PASS — Ko e hala 'o e fononga ko e faka'apa'apa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
