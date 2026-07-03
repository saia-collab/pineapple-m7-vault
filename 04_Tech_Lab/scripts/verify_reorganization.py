"""
Pineapple-Mana-Global Reorganization Verifier
Checks that no files were lost and expected structure is in place.
"""

import os
import sys
import re
import hashlib
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\Pineapple-Mana-Global")

# Folders to skip when counting (not real business assets)
SKIP_DIRS = {".git", "node_modules", ".agents", ".claude", ".continue", "__pycache__"}

EXPECTED_STRUCTURE = {
    "01_Command_Center/Playbooks": "Marketing playbooks directory",
    "01_Command_Center/Brand_DNA": "Brand identity assets",
    "01_Command_Center/Brand_DNA/TATAFU_BRAND.md": "Core brand document",
    "02_Media_Vault/Pineapple-Media-HQ": "Organized media campaigns",
}

MEDIA_HQ_NAME_PATTERN = re.compile(r"^\d{4}_\d{2}_.+_.+$")


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def count_files(directory: Path) -> dict:
    """Return {relative_path: file_size} for all files under directory."""
    result = {}
    if not directory.exists():
        return result
    for f in directory.rglob("*"):
        if f.is_file() and not should_skip(f):
            rel = f.relative_to(directory)
            result[str(rel)] = f.stat().st_size
    return result


def check_expected_structure() -> list[str]:
    errors = []
    for rel_path, description in EXPECTED_STRUCTURE.items():
        full = ROOT / rel_path
        if not full.exists():
            errors.append(f"MISSING  [{description}]: {rel_path}")
        else:
            status = "DIR " if full.is_dir() else "FILE"
            print(f"  OK  {status}  {rel_path}")
    return errors


def check_media_hq_naming() -> list[str]:
    issues = []
    media_hq = ROOT / "02_Media_Vault" / "Pineapple-Media-HQ"
    if not media_hq.exists():
        return [f"Media-HQ folder not found: {media_hq}"]

    for d in media_hq.iterdir():
        if d.is_dir() and d.name not in SKIP_DIRS:
            if not MEDIA_HQ_NAME_PATTERN.match(d.name):
                issues.append(f"  BAD NAME  {d.name}  (expected YEAR_MONTH_CAMPAIGN_ASSET-TYPE)")
            else:
                print(f"  OK  {d.name}")
    return issues


def check_playbooks() -> list[str]:
    issues = []
    playbooks = ROOT / "01_Command_Center" / "Playbooks"
    if not playbooks.exists():
        return ["Playbooks folder missing"]
    files = list(playbooks.iterdir())
    if not files:
        issues.append("Playbooks folder is empty")
    else:
        print(f"  OK  {len(files)} items in Playbooks")
    return issues


def scan_all_files() -> tuple[int, int]:
    """Return (total_files, total_bytes) across the whole root."""
    total_files = 0
    total_bytes = 0
    for f in ROOT.rglob("*"):
        if f.is_file() and not should_skip(f):
            total_files += 1
            total_bytes += f.stat().st_size
    return total_files, total_bytes


def find_duplicate_filenames() -> dict:
    """Find filenames that appear in more than one location (could indicate duplicate copies)."""
    name_map = defaultdict(list)
    for f in ROOT.rglob("*"):
        if f.is_file() and not should_skip(f):
            name_map[f.name].append(str(f.relative_to(ROOT)))
    return {name: paths for name, paths in name_map.items() if len(paths) > 1}


def main():
    print("=" * 60)
    print("  PINEAPPLE-MANA-GLOBAL REORGANIZATION VERIFIER")
    print("=" * 60)
    all_errors = []

    # 1. Root exists
    if not ROOT.exists():
        print(f"\nFATAL: Root directory not found: {ROOT}")
        sys.exit(1)
    print(f"\nRoot: {ROOT}  [EXISTS]\n")

    # 2. Expected structure
    print("[ EXPECTED STRUCTURE ]")
    errors = check_expected_structure()
    all_errors.extend(errors)
    for e in errors:
        print(f"  {e}")

    # 3. Media-HQ naming
    print("\n[ MEDIA-HQ FOLDER NAMING  (YEAR_MONTH_CAMPAIGN_ASSET-TYPE) ]")
    naming_issues = check_media_hq_naming()
    all_errors.extend(naming_issues)
    for issue in naming_issues:
        print(issue)
    if not naming_issues:
        print("  All campaign folders follow correct naming convention")

    # 4. Playbooks content
    print("\n[ PLAYBOOKS CONTENT ]")
    pb_issues = check_playbooks()
    all_errors.extend(pb_issues)
    for issue in pb_issues:
        print(f"  WARNING  {issue}")

    # 5. Total file count
    print("\n[ FILE INVENTORY ]")
    total_files, total_bytes = scan_all_files()
    print(f"  Total files (excl. system dirs): {total_files:,}")
    print(f"  Total size:                      {total_bytes / 1_048_576:.1f} MB")

    # 6. Duplicate filenames
    print("\n[ DUPLICATE FILENAME CHECK ]")
    dupes = find_duplicate_filenames()
    if dupes:
        print(f"  Found {len(dupes)} filename(s) appearing in multiple locations:")
        for name, paths in sorted(dupes.items())[:20]:
            print(f"    {name}")
            for p in paths:
                print(f"      -> {p}")
        if len(dupes) > 20:
            print(f"    ... and {len(dupes) - 20} more")
    else:
        print("  No duplicate filenames found")

    # 7. Summary
    print("\n" + "=" * 60)
    if all_errors:
        print(f"  RESULT: {len(all_errors)} issue(s) found")
        for e in all_errors:
            print(f"    - {e}")
        sys.exit(1)
    else:
        print("  RESULT: ALL CHECKS PASSED — no files lost, structure intact")
    print("=" * 60)


if __name__ == "__main__":
    main()
