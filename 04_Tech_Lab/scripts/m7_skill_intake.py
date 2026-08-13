#!/usr/bin/env python3
"""
M7 SKILL INTAKE — drop-and-go ingestion for Claude Skill / Template assets.
Handles the varied ways Gumroad (and others) deliver products:
  * .zip archives
  * loose files (.md .pdf .txt .json .yaml .html .docx)
  * dropped folders (already-extracted packages)

For each item it:
  1. (zip) safe-extracts / (folder) reads in place / (loose) wraps,
  2. classifies SKILL (contains SKILL.md) vs TEMPLATE (everything else),
  3. files into the correct vault location,
  4. runs the brand firewall over text files,
  5. logs to 04_Tech_Lab/logs/skill_intake_log.json.

Inbox:    04_Tech_Lab/skills_inbox/         <- drop the 47 products here (any format)
Skills →  04_Tech_Lab/skills/<name>/
Templates 03_Knowledge_Mat/00_Atlas/templates/<name>/

Usage
-----
    python m7_skill_intake.py            # process everything in the inbox once
    python m7_skill_intake.py --watch    # keep watching the inbox (poll)
    python m7_skill_intake.py --keep     # don't delete source after intake

"""
from __future__ import annotations
import argparse, json, re, shutil, sys, time, zipfile
from datetime import datetime
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents) >= 3 else Path.cwd()

LEXICON = [
    (re.compile(r"free\s+inspection", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"free\s+quote", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"\$0\s*(down|out\s*of\s*pocket)", re.I), "Full Restoration Coverage"),
    (re.compile(r"save\s+money", re.I), "Protecting your family's investment"),
    (re.compile(r"gaf\s+certified", re.I), "IKO Certified (RCAT License #03-0637)"),
    (re.compile(r"six\s+brothers", re.I), "The Pineapple Standard"),
    (re.compile(r"\bwarrior\b", re.I), "The Pineapple Standard"),
    (re.compile(r"\btoa\b", re.I), "The Pineapple Standard"),
    (re.compile(r"\bconsultation\b", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"\bfree\b", re.I), "Complimentary"),
]
TEXT_EXT = {".md", ".txt", ".json", ".yaml", ".yml", ".html", ".css", ".js"}
ASSET_EXT = TEXT_EXT | {".pdf", ".docx", ".csv", ".png", ".jpg", ".jpeg", ".mp4", ".mov"}
SAFE_NAME = re.compile(r"[^A-Za-z0-9._-]+")


def firewall_text(text):
    n = 0
    for rx, repl in LEXICON:
        if rx.search(text):
            n += len(rx.findall(text))
            text = rx.sub(repl, text)
    return text, n


def safe(name: str) -> str:
    return SAFE_NAME.sub("_", name).strip("_") or "asset"


def is_within(base: Path, target: Path) -> bool:
    try:
        target.resolve().relative_to(base.resolve())
        return True
    except ValueError:
        return False


def classify(folder: Path) -> str:
    for p in folder.rglob("*"):
        if p.is_file() and p.name.lower() == "skill.md":
            return "skill"
    return "template"


def dest_for(kind: str, name: str, root: Path) -> Path:
    base = (root / "04_Tech_Lab" / "skills" / name) if kind == "skill" \
        else (root / "03_Knowledge_Mat" / "00_Atlas" / "templates" / name)
    if base.exists():
        base = base.with_name(base.name + f"_{datetime.now():%H%M%S}")
    base.parent.mkdir(parents=True, exist_ok=True)
    return base


def firewall_tree(dest_root: Path):
    mutated_files, total = 0, 0
    for f in dest_root.rglob("*"):
        if f.is_file() and f.suffix.lower() in TEXT_EXT:
            try:
                orig = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue
            new, n = firewall_text(orig)
            if n:
                f.write_text(new, encoding="utf-8")
                mutated_files += 1
                total += n
    return mutated_files, total


def file_package(src_base: Path, name: str, root: Path, log: list, origin: str):
    kind = classify(src_base)
    dest_root = dest_for(kind, name, root)
    shutil.copytree(src_base, dest_root)
    mf, tm = firewall_tree(dest_root)
    log.append({"source": origin, "ok": True, "kind": kind,
                "filed_to": str(dest_root.relative_to(root)),
                "files_mutated": mf, "terms_mutated": tm})


def process_zip(zpath: Path, root: Path, keep: bool, log: list):
    name = safe(zpath.stem)
    tmp = root / "04_Tech_Lab" / "logs" / "_intake_tmp" / name
    if tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(zpath) as z:
            z.extractall(tmp)
    except (zipfile.BadZipFile, OSError) as e:
        log.append({"source": zpath.name, "ok": False, "error": str(e)})
        return
    entries = [p for p in tmp.iterdir() if p.name not in ("__MACOSX",)]
    base = entries[0] if len(entries) == 1 and entries[0].is_dir() else tmp
    file_package(base, name, root, log, zpath.name)
    shutil.rmtree(tmp, ignore_errors=True)
    if not keep:
        try: zpath.unlink()
        except OSError: pass


def process_folder(folder: Path, root: Path, keep: bool, log: list):
    name = safe(folder.name)
    file_package(folder, name, root, log, folder.name + "/")
    if not keep:
        shutil.rmtree(folder, ignore_errors=True)


def process_loose(fpath: Path, root: Path, keep: bool, log: list):
    name = safe(fpath.stem)
    # wrap the loose file in a one-file package so classification + filing is uniform
    tmp = root / "04_Tech_Lab" / "logs" / "_intake_tmp" / name
    if tmp.exists():
        shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fpath, tmp / fpath.name)
    file_package(tmp, name, root, log, fpath.name)
    shutil.rmtree(tmp, ignore_errors=True)
    if not keep:
        try: fpath.unlink()
        except OSError: pass


def run_once(root: Path, keep: bool):
    inbox = root / "04_Tech_Lab" / "skills_inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    log = []
    # 1) zips
    for z in sorted(inbox.glob("*.zip")):
        process_zip(z, root, keep, log)
    # 2) dropped folders (skip helper/marker dirs)
    for d in sorted([p for p in inbox.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))]):
        process_folder(d, root, keep, log)
    # 3) loose files (skip the marker readme + non-asset junk)
    for f in sorted([p for p in inbox.iterdir()
                     if p.is_file() and p.suffix.lower() in ASSET_EXT
                     and not p.name.startswith(("_", "."))]):
        process_loose(f, root, keep, log)

    log_path = root / "04_Tech_Lab" / "logs" / "skill_intake_log.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    record = {"run": datetime.now().isoformat(), "processed": len(log), "results": log,
              "closing": "."}
    log_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(json.dumps(record, indent=2))
    return len(log)


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 Skill / Template intake")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--watch", action="store_true", help="keep polling the inbox")
    ap.add_argument("--keep", action="store_true", help="keep sources after intake")
    args = ap.parse_args(argv)
    root = args.root.resolve()

    if args.watch:
        inbox = root / "04_Tech_Lab" / "skills_inbox"
        print(f"[intake] watching {inbox} — Ctrl+C to stop")
        try:
            while True:
                have = any(p for p in inbox.glob("*")
                           if not p.name.startswith(("_", "."))) if inbox.exists() else False
                if have:
                    run_once(root, args.keep)
                time.sleep(5)
        except KeyboardInterrupt:
            print("\n[intake] stopped.")
        return 0

    run_once(root, args.keep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
