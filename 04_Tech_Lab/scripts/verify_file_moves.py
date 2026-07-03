#!/usr/bin/env python3
"""Verify that file moves did not lose content.

Usage:
  python verify_file_moves.py snapshot --root <dir> --out <manifest.json>
  python verify_file_moves.py compare --before <manifest.json> --after <manifest.json>

The script compares file hashes between two manifests. Files can be moved/renamed;
verification is content-based, not path-based.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def build_manifest(root: Path) -> Dict[str, object]:
    files: List[Dict[str, object]] = []
    for p in sorted(root.rglob("*")):
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            files.append(
                {
                    "relative_path": rel,
                    "size": p.stat().st_size,
                    "sha256": sha256_file(p),
                }
            )

    hash_counts = Counter(item["sha256"] for item in files)
    return {
        "root": str(root),
        "file_count": len(files),
        "files": files,
        "hash_counts": dict(hash_counts),
    }


def load_manifest(path: Path) -> Dict[str, object]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def compare_manifests(before: Dict[str, object], after: Dict[str, object]) -> Dict[str, object]:
    before_counts = Counter(before.get("hash_counts", {}))
    after_counts = Counter(after.get("hash_counts", {}))

    missing = before_counts - after_counts
    added = after_counts - before_counts

    return {
        "before_file_count": before.get("file_count", 0),
        "after_file_count": after.get("file_count", 0),
        "missing_content_hashes": dict(missing),
        "added_content_hashes": dict(added),
        "content_loss_detected": bool(missing),
    }


def write_json(path: Path, data: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify that file moves did not lose content.")
    sub = parser.add_subparsers(dest="command", required=True)

    snap = sub.add_parser("snapshot", help="Create a manifest snapshot of a directory.")
    snap.add_argument("--root", required=True, help="Directory to snapshot")
    snap.add_argument("--out", required=True, help="Output manifest JSON path")

    comp = sub.add_parser("compare", help="Compare two manifest snapshots.")
    comp.add_argument("--before", required=True, help="Path to before-manifest JSON")
    comp.add_argument("--after", required=True, help="Path to after-manifest JSON")
    comp.add_argument("--out", required=False, help="Optional output report JSON path")

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.command == "snapshot":
        root = Path(args.root).expanduser().resolve()
        out = Path(args.out).expanduser().resolve()
        manifest = build_manifest(root)
        write_json(out, manifest)
        print(f"Snapshot created: {out}")
        print(f"Files indexed: {manifest['file_count']}")
        return 0

    before = load_manifest(Path(args.before).expanduser().resolve())
    after = load_manifest(Path(args.after).expanduser().resolve())
    report = compare_manifests(before, after)

    if args.out:
        write_json(Path(args.out).expanduser().resolve(), report)
        print(f"Comparison report written: {args.out}")

    print(json.dumps(report, indent=2))
    return 1 if report["content_loss_detected"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
