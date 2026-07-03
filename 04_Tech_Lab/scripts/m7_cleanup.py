#!/usr/bin/env python3
"""
M7 CLEANUP — MD5 deduper, drift purge, and housekeeping.
Walks the 4-Fala vault, finds duplicate files by content hash, archives the
duplicates into !_ARCHIVE_<YYYY_MM>, and removes empty directories.

Dry-run by default. Pass --apply to actually move files.

Usage
-----
    python m7_cleanup.py                 # dry-run report
    python m7_cleanup.py --apply         # archive duplicates + prune empties
    python m7_cleanup.py --root <path>   # override vault root

Ko e hala 'o e fononga ko e faka'apa'apa.
"""
from __future__ import annotations
import argparse, hashlib, json, shutil, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents) >= 3 else Path.cwd()
EXCLUDE = {".git", ".obsidian", "node_modules", "__pycache__", ".venv",
           ".tmp.drivedownload", ".tmp.driveupload"}
SKIP_PREFIX = ("!_ARCHIVE_", "legacy_backup")


def md5(path: Path, chunk=1 << 16) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for blk in iter(lambda: f.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


def iter_files(root: Path):
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in EXCLUDE for part in p.parts):
            continue
        if any(part.startswith(SKIP_PREFIX) for part in p.parts):
            continue
        yield p


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 vault deduper / housekeeping")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--apply", action="store_true", help="actually move duplicates (default: dry-run)")
    args = ap.parse_args(argv)
    root = args.root.resolve()

    by_hash = defaultdict(list)
    scanned = 0
    for f in iter_files(root):
        try:
            by_hash[md5(f)].append(f)
            scanned += 1
        except (PermissionError, OSError):
            continue

    dup_groups = {h: ps for h, ps in by_hash.items() if len(ps) > 1}
    archive = root / f"!_ARCHIVE_{datetime.now():%Y_%m}"
    moved = []

    for h, paths in dup_groups.items():
        # keep the shortest path (most canonical); archive the rest
        keep = min(paths, key=lambda p: (len(str(p)), str(p)))
        for dup in paths:
            if dup == keep:
                continue
            if args.apply:
                rel = dup.relative_to(root)
                dest = archive / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                try:
                    shutil.move(str(dup), str(dest))
                    moved.append({"from": str(rel), "kept": str(keep.relative_to(root))})
                except (OSError, shutil.Error):
                    pass
            else:
                moved.append({"would_archive": str(dup.relative_to(root)),
                              "kept": str(keep.relative_to(root))})

    empties = []
    if args.apply:
        for d in sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if d.is_dir() and not any(part in EXCLUDE for part in d.parts):
                try:
                    if not any(d.iterdir()):
                        d.rmdir()
                        empties.append(str(d.relative_to(root)))
                except OSError:
                    pass

    report = {
        "root": str(root), "scanned": scanned,
        "duplicate_groups": len(dup_groups),
        "files_affected": len(moved),
        "mode": "apply" if args.apply else "dry-run",
        "moved": moved[:200], "empty_dirs_removed": empties,
        "closing": "Ko e hala 'o e fononga ko e faka'apa'apa.",
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
