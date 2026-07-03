#!/usr/bin/env python3
"""
Shot Builder — Project management.

Renders, tokens, and INDEX entries can be scoped to a project. Projects live
under `workspace/projects/<slug>/{cast,locations,styles}/`. The "active project"
is stored in `workspace/config.json` and read by the generation scripts to:
  - route renders to <output_dir>/<date>/<slug>/<kind>/
  - look up tokens in workspace/projects/<slug>/<kind>/ before workspace/<kind>/

Usage:
    python project.py list                  # show all projects + which is active
    python project.py current               # print active project slug (empty if none)
    python project.py new "OMV Post-It"     # create new project; does NOT auto-switch
    python project.py set post-it           # switch active project (must exist)
    python project.py clear                 # unset active project — renders go to _unsorted/

Exit codes:
    0  success
    1  user error (project not found, missing arg, etc.)
    2  ShotBuilderError (missing config etc.)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Local helpers
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _common import (  # noqa: E402
    PROJECTS_DIR,
    ShotBuilderError,
    ensure_project_scaffold,
    get_active_project,
    list_projects,
    load_config,
    set_active_project,
    slugify_project,
)


def cmd_list() -> int:
    active = get_active_project()
    projects = list_projects()
    if not projects:
        print("No projects yet. Create one with `python project.py new <name>`.")
        return 0
    print(f"{'Active':<8} {'Slug':<30} {'Path'}")
    print("-" * 70)
    for slug in projects:
        marker = "  *" if slug == active else "   "
        path = PROJECTS_DIR / slug
        print(f"{marker:<8} {slug:<30} {path}")
    if not active:
        print()
        print("No active project. Renders will go to `_unsorted/`.")
        print("Set one with `python project.py set <slug>`.")
    return 0


def cmd_current() -> int:
    active = get_active_project()
    if active:
        print(active)
    return 0


def cmd_new(name: str, switch: bool) -> int:
    slug = slugify_project(name)
    target = PROJECTS_DIR / slug
    if target.exists():
        print(f"project '{slug}' already exists at {target}", file=sys.stderr)
        return 1

    ensure_project_scaffold(slug)
    print(f"Created project '{slug}' at {target}")
    print(f"  cast/      → {target / 'cast'}")
    print(f"  locations/ → {target / 'locations'}")
    print(f"  styles/    → {target / 'styles'}")

    if switch:
        try:
            set_active_project(slug)
            print(f"\nSwitched to '{slug}'. Renders will go to <output_dir>/<date>/{slug}/")
        except ShotBuilderError as e:
            print(f"created, but failed to switch: {e}", file=sys.stderr)
            return 2
    else:
        print(f"\nNot switched. Run `python project.py set {slug}` to activate.")
    return 0


def cmd_set(slug: str) -> int:
    slug = slugify_project(slug)
    try:
        set_active_project(slug)
    except ShotBuilderError as e:
        print(str(e), file=sys.stderr)
        return 1
    print(f"Active project: {slug}")
    print(f"Renders will save to <output_dir>/<date>/{slug}/")
    return 0


def cmd_clear() -> int:
    try:
        set_active_project(None)
    except ShotBuilderError as e:
        print(str(e), file=sys.stderr)
        return 2
    print("Active project cleared. Renders will save to `_unsorted/`.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Manage shot-builder projects.")
    sub = ap.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list all projects (active marked with *)")
    sub.add_parser("current", help="print active project slug (empty if none)")

    p_new = sub.add_parser("new", help="create a new project")
    p_new.add_argument("name", help='project name (e.g., "OMV Post-It")')
    p_new.add_argument(
        "--switch",
        action="store_true",
        help="switch active project to the new one (default: just create)",
    )

    p_set = sub.add_parser("set", help="switch active project (must exist)")
    p_set.add_argument("slug", help="project slug (use `list` to see options)")

    sub.add_parser("clear", help="unset active project (renders go to _unsorted/)")

    args = ap.parse_args()

    # Ensure config exists before any subcommand — they all touch it.
    try:
        load_config()
    except ShotBuilderError as e:
        print(str(e), file=sys.stderr)
        return 2

    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.command == "list":
        return cmd_list()
    if args.command == "current":
        return cmd_current()
    if args.command == "new":
        return cmd_new(args.name, args.switch)
    if args.command == "set":
        return cmd_set(args.slug)
    if args.command == "clear":
        return cmd_clear()

    ap.error(f"unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
