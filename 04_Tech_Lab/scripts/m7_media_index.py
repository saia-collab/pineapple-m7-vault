#!/usr/bin/env python3
"""
M7 MEDIA INDEX — inventory a media folder so you stop guessing what's in 39GB.
Counts files by type, totals size, lists top-level project folders, and flags
likely duplicates by filename. Writes MEDIA_INDEX.md. Pure stdlib, read-only.

Usage:
  python m7_media_index.py                         # indexes 02_Media_Vault
  python m7_media_index.py --path "G:\\My Drive\\PINEAPPLE_MEDIA_HUB"
  python m7_media_index.py --path "<folder>" --out "<file.md>"

Ko e hala 'o e fononga ko e faka'apa'apa.
"""
from __future__ import annotations
import argparse, collections, os, sys
from datetime import datetime
from pathlib import Path

VIDEO = {".mp4",".mov",".avi",".mkv",".m4v",".wmv",".webm"}
PHOTO = {".jpg",".jpeg",".png",".heic",".webp",".gif",".tiff",".bmp",".dng",".raw"}
DOC   = {".pdf",".docx",".doc",".txt",".md",".csv",".xlsx",".pptx"}
AUDIO = {".mp3",".wav",".m4a",".aac"}

def human(n):
    for u in ("B","KB","MB","GB","TB"):
        if n < 1024: return f"{n:.1f}{u}"
        n /= 1024
    return f"{n:.1f}PB"

def kind(ext):
    ext = ext.lower()
    if ext in VIDEO: return "Video"
    if ext in PHOTO: return "Photo"
    if ext in DOC:   return "Doc"
    if ext in AUDIO: return "Audio"
    return "Other"

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    root = Path(args.path).resolve() if args.path else \
        (Path(__file__).resolve().parents[2] / "02_Media_Vault" if len(Path(__file__).resolve().parents) >= 3 else Path.cwd())
    if not root.exists():
        print(f"path not found: {root}"); return 1

    by_kind = collections.Counter()
    size_by_kind = collections.Counter()
    by_ext = collections.Counter()
    names = collections.defaultdict(list)
    total_files = total_size = 0

    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if not d.startswith((".",)) and d not in ("node_modules",)]
        for fn in fns:
            if fn.startswith(".") or fn == "MEDIA_INDEX.md": continue
            p = Path(dp)/fn
            try: sz = p.stat().st_size
            except OSError: continue
            ext = p.suffix.lower() or "(none)"
            k = kind(ext)
            by_kind[k]+=1; size_by_kind[k]+=sz; by_ext[ext]+=1
            names[fn.lower()].append(str(p.relative_to(root)))
            total_files+=1; total_size+=sz

    # top-level folders with size
    folders=[]
    for d in sorted([x for x in root.iterdir() if x.is_dir() and not x.name.startswith(".")]):
        s=c=0
        for dp,_,fns in os.walk(d):
            for fn in fns:
                try: s+=(Path(dp)/fn).stat().st_size; c+=1
                except OSError: pass
        folders.append((d.name,c,s))

    dups = {n:ps for n,ps in names.items() if len(ps)>1}

    out_lines = [
        "---","type: media_index",f"generated: {datetime.now():%Y-%m-%d %H:%M}",
        f'root: "{root}"',"---","",
        "# MEDIA INDEX","",
        f"**Total:** {total_files:,} files · {human(total_size)}","",
        "## By type","","| Type | Files | Size |","|---|---|---|",
    ]
    for k in ("Video","Photo","Doc","Audio","Other"):
        if by_kind[k]: out_lines.append(f"| {k} | {by_kind[k]:,} | {human(size_by_kind[k])} |")
    out_lines += ["","## Top-level folders","","| Folder | Files | Size |","|---|---|---|"]
    for n,c,s in sorted(folders,key=lambda x:-x[2]):
        out_lines.append(f"| {n} | {c:,} | {human(s)} |")
    out_lines += ["","## File extensions","", ", ".join(f"{e}({n})" for e,n in by_ext.most_common(20))]
    out_lines += ["","## Possible duplicates (same filename in 2+ places)",""]
    if dups:
        for n,ps in list(sorted(dups.items()))[:50]:
            out_lines.append(f"- **{n}** — {len(ps)}x: {', '.join(ps[:4])}{' …' if len(ps)>4 else ''}")
        if len(dups)>50: out_lines.append(f"- …and {len(dups)-50} more duplicate names")
    else:
        out_lines.append("- none found")
    out_lines += ["","## Suggested next step",
        "- Move RAW dumps → 01_RAW_INTAKE; sort jobs → 02_SORTED_PROJECTS; finals → 04_READY_TO_POST.",
        "- Triage 5 best assets/week → deploy 4 ways (GBP · Reel/TikTok · Short · Ad).","",
        "Ko e hala 'o e fononga ko e faka'apa'apa.","",
        "<!-- M7-FIREWALL-EXEMPT: governance-reference -->",""]

    out = Path(args.out) if args.out else (root/"MEDIA_INDEX.md")
    out.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"indexed {total_files:,} files ({human(total_size)}) -> {out}")
    print(f"folders: {len(folders)} | duplicate-names: {len(dups)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
