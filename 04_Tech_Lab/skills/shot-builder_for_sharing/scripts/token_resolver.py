#!/usr/bin/env python3
"""
Shot Builder — Token resolver.

Loads `<TOKEN>` references from workspace/cast|locations|styles/ and from
workspace/projects/<project>/cast|locations|styles/. Project-scoped tokens
shadow global tokens of the same name — useful when HERO means different
things in different productions.

Returns one of:
  - canonical prompt-token block (default — for prompt assembly)
  - full token file              (--full — for the skill to read into context)
  - roster summary               (--roster — for INDEX.md refresh)

Lookup order:
  1. workspace/projects/<project>/<kind>/<TOKEN>.md  (if --project or config.active_project set)
  2. workspace/<kind>/<TOKEN>.md                      (global fallback)

Usage:
    python token_resolver.py HERO
    python token_resolver.py HERO --project post-it
    python token_resolver.py STATION-INT-SHOP --full
    python token_resolver.py --roster                   # all kinds, project + global
    python token_resolver.py --roster --project post-it # roster scoped to that project
    python token_resolver.py --list cast                # list cast tokens (global + active project)
    python token_resolver.py --list-projects            # list project slugs

Exit codes:
    0  success
    1  token / project not found, or no prompt block in file
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _common import (  # noqa: E402
    PROJECTS_DIR,
    TOKEN_KINDS,
    WORKSPACE,
    ShotBuilderError,
    get_active_project,
    list_projects,
    resolve_token_dir,
    slugify_project,
)


def find_token_file(token: str, project: str | None = None) -> tuple[str, str, Path] | None:
    """
    Search project-scoped then global for a matching token across all kinds.
    Returns (kind, scope, path) where scope is "project:<slug>" or "global", or None.
    """
    needle = token.strip().lstrip("<").rstrip(">").upper()
    for kind in TOKEN_KINDS:
        for directory in resolve_token_dir(kind, project):
            candidate = directory / f"{needle}.md"
            if candidate.exists():
                # Tag with scope so callers / messages can show where it came from
                if directory.is_relative_to(PROJECTS_DIR):
                    scope_slug = directory.relative_to(PROJECTS_DIR).parts[0]
                    scope = f"project:{scope_slug}"
                else:
                    scope = "global"
                return (kind, scope, candidate)
    return None


def extract_prompt_block(content: str) -> str | None:
    """
    Pull the `Reusable prompt token` fenced code block from a token file.

    Matches:
        ## Reusable prompt token
        ```
        <TOKEN> := ...
        ```
    """
    section_re = re.compile(
        r"##\s+Reusable prompt token.*?```[a-z]*\n(.*?)```",
        re.DOTALL | re.IGNORECASE,
    )
    m = section_re.search(content)
    if m:
        return m.group(1).strip()
    return None


def extract_summary(content: str) -> str:
    """Pull a one-line summary from frontmatter or the canonical-description section."""
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        for field in ("summary", "description"):
            m = re.search(rf"^{field}:\s*(.+)$", fm, re.MULTILINE)
            if m:
                return m.group(1).strip().strip('"').strip("'")

    canon_match = re.search(r"##\s+Canonical description\s*\n+>?\s*(.+)", content)
    if canon_match:
        line = canon_match.group(1).strip()
        line = re.split(r"(?<=[.!?])\s", line, maxsplit=1)[0]
        return line[:120] + ("…" if len(line) > 120 else "")
    return "(no summary)"


def list_kind(kind: str, project: str | None = None) -> list[tuple[str, str, str]]:
    """
    Return [(<TOKEN>, summary, scope), ...] for a kind.
    Scope is "project:<slug>" or "global". Project tokens come first; a global
    token with the same name as a project token is hidden (the project one shadows it).
    """
    if kind not in TOKEN_KINDS:
        return []

    seen: set[str] = set()
    out: list[tuple[str, str, str]] = []

    for directory in resolve_token_dir(kind, project):
        if not directory.exists():
            continue
        scope = (
            f"project:{directory.relative_to(PROJECTS_DIR).parts[0]}"
            if directory.is_relative_to(PROJECTS_DIR)
            else "global"
        )
        for path in sorted(directory.glob("*.md")):
            if path.name.startswith(".") or path.stem in seen:
                continue
            seen.add(path.stem)
            token = f"<{path.stem}>"
            content = path.read_text()
            out.append((token, extract_summary(content), scope))
    return out


def roster(project: str | None = None) -> dict[str, list[tuple[str, str, str]]]:
    """Full roster for INDEX.md — every kind, project-scoped if a project is passed."""
    return {kind: list_kind(kind, project) for kind in TOKEN_KINDS}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("token", nargs="?", help="Token name (with or without angle brackets)")
    ap.add_argument(
        "--project",
        help="Project slug to scope the lookup (defaults to config.active_project)",
    )
    ap.add_argument("--full", action="store_true", help="Print full token file")
    ap.add_argument("--roster", action="store_true", help="Print all tokens, grouped by kind")
    ap.add_argument(
        "--list",
        choices=list(TOKEN_KINDS),
        help="List tokens in a specific kind",
    )
    ap.add_argument(
        "--list-projects",
        action="store_true",
        help="List all project slugs (one per line, active marked with *)",
    )
    args = ap.parse_args()

    # Resolve project: explicit --project wins, otherwise config.active_project
    project = slugify_project(args.project) if args.project else None
    if project is None:
        try:
            project = get_active_project()
        except ShotBuilderError:
            project = None

    if args.list_projects:
        try:
            active = get_active_project()
        except ShotBuilderError:
            active = None
        for slug in list_projects():
            marker = " *" if slug == active else "  "
            print(f"{marker}{slug}")
        return 0

    if args.roster:
        scope_note = f"(project: {project})" if project else "(global only)"
        print(f"# Token roster {scope_note}")
        print()
        for kind, items in roster(project).items():
            print(f"## {kind}")
            if not items:
                print("  (empty)")
            else:
                for token, summary, scope in items:
                    tag = "" if scope == "global" else f" [{scope}]"
                    print(f"  {token}{tag} — {summary}")
            print()
        return 0

    if args.list:
        for token, summary, scope in list_kind(args.list, project):
            tag = "" if scope == "global" else f" [{scope}]"
            print(f"{token}{tag} — {summary}")
        return 0

    if not args.token:
        ap.error("token name required (or use --roster / --list / --list-projects)")

    found = find_token_file(args.token, project)
    if not found:
        searched = []
        for kind in TOKEN_KINDS:
            searched.extend(str(p) for p in resolve_token_dir(kind, project))
        print(
            f"token not found: {args.token}\n"
            f"  searched: {searched}",
            file=sys.stderr,
        )
        return 1

    kind, scope, path = found

    if args.full:
        # Print a small header so callers see which file they're getting
        print(f"# token: {args.token}  kind: {kind}  scope: {scope}", file=sys.stderr)
        print(path.read_text())
        return 0

    content = path.read_text()
    block = extract_prompt_block(content)
    if not block:
        print(
            f"no `Reusable prompt token` block in {path}. "
            f"Token files should include one — see references/character-sheet.md.",
            file=sys.stderr,
        )
        return 1

    # Log the scope to stderr so prompt-assembly stays clean on stdout
    print(f"# resolved from {scope}: {path}", file=sys.stderr)
    print(block)
    return 0


if __name__ == "__main__":
    sys.exit(main())
