#!/usr/bin/env python3
"""
M7 AGGREGATE — flatten 03_Knowledge_Mat/raw/ into the 00_Atlas index.
Deduplicates raw markdown by content hash, stamps frontmatter, and rebuilds
00_Atlas/INDEX.md so RAG queries hit a clean, low-latency substrate.

Usage
-----
    python m7_aggregate.py                # process raw/ -> 00_Atlas/
    python m7_aggregate.py --root <path>

"""
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents) >= 3 else Path.cwd()


def md5_text(s: str) -> str:
    return hashlib.md5(s.encode("utf-8", "ignore")).hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 Knowledge_Mat aggregator")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = ap.parse_args(argv)
    root = args.root.resolve()

    raw_dir = root / "03_Knowledge_Mat" / "raw"
    atlas = root / "03_Knowledge_Mat" / "00_Atlas"
    atlas.mkdir(parents=True, exist_ok=True)

    seen = {}
    processed, skipped = [], []
    today = f"{datetime.now():%Y-%m-%d}"

    if not raw_dir.exists():
        print(json.dumps({"error": f"no raw dir at {raw_dir}"}, indent=2))
        return 0

    for src in sorted(raw_dir.glob("*.md")):
        try:
            text = src.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue
        h = md5_text(text)
        if h in seen:
            skipped.append({"file": src.name, "dup_of": seen[h]})
            continue
        seen[h] = src.name
        topic = src.stem.replace(" ", "_")
        dest = atlas / f"{today}_KB_{topic}.md"
        fm = (f"---\ntype: knowledge_atlas\nsource: {src.name}\n"
              f"created: {today}\nhash: {h}\nagent_origin: m7_aggregate\n---\n\n")
        body = text if text.lstrip().startswith("---") else fm + text
        dest.write_text(body, encoding="utf-8")
        processed.append(dest.name)

    # Rebuild INDEX.md
    index = [f"# 00_Atlas INDEX  ({today})", ""]
    for f in sorted(atlas.glob("*.md")):
        if f.name == "INDEX.md":
            continue
        index.append(f"- [[{f.stem}]]")
    index.append("")
    index.append(".")
    (atlas / "INDEX.md").write_text("\n".join(index), encoding="utf-8")

    print(json.dumps({
        "root": str(root), "processed": processed,
        "deduped": skipped, "atlas_files": len(list(atlas.glob('*.md'))),
        "closing": ".",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
