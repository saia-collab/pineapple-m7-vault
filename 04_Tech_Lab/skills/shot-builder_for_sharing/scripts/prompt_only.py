#!/usr/bin/env python3
"""
Shot Builder — Prompt-only export (no provider call).

Writes a prompt sidecar markdown to:
    <output_dir>/<YYYY-MM-DD>/<project>/prompts/<label>_<NNN>.md

No API call, no spend, no image file. The user pastes the prompt anywhere they
want — Higgsfield UI, ComfyUI, Midjourney, Replicate web UI, OpenAI DALL-E,
a collaborator's chat — and brings back the result manually if they want.

Why this exists:
  - Iterate on prompt language for free before any render
  - Use a provider shot-builder doesn't have direct integration for
  - Share a prompt with a collaborator who has different tools
  - Generate the prompt now, render later when you're ready

Usage:
    python prompt_only.py \\
      --type image \\
      --prompt "<full prompt text>" \\
      --label HERO_at_counter \\
      --token "<HERO>" --token "<STATION-INT-SHOP>" \\
      --resolution 2K --aspect 2.39:1

Exit codes:
    0  success
    1  user error (missing args, etc.)
    2  ShotBuilderError (no config, no project, etc.)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _common import (  # noqa: E402
    WORKSPACE,
    ShotBuilderError,
    get_active_project,
    load_config,
    slugify,
    slugify_project,
    unique_path,
    write_render_sidecar,
)


def resolve_prompts_dir(config: dict, project: str | None = None) -> Path:
    """
    Build <output_dir>/<date>/<project>/prompts/ — mirrors resolve_output_dir
    but uses 'prompts/' as the kind subfolder instead of shots/scenes.
    """
    from datetime import datetime, timezone

    project_slug = (
        slugify_project(project) if project else get_active_project(config) or "_unsorted"
    )
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    target = Path(config["paths"]["output_dir"]) / date / project_slug / "prompts"
    target.mkdir(parents=True, exist_ok=True)

    mirror = WORKSPACE / "prompts" / date / project_slug
    mirror.mkdir(parents=True, exist_ok=True)
    return target


def main() -> int:
    ap = argparse.ArgumentParser(description="Write a prompt sidecar without generating.")
    ap.add_argument("--type", choices=["image", "video"], default="image")
    ap.add_argument("--prompt", required=True, help="Full prompt text")
    ap.add_argument("--label", default="prompt", help="Filename label (slugified)")
    ap.add_argument(
        "--token",
        action="append",
        default=[],
        help="Token used in this prompt (e.g. <HERO>). Repeatable.",
    )
    ap.add_argument("--project", help="Project slug (defaults to config.active_project)")

    # Setting hints (purely informational — these are not enforced anywhere)
    ap.add_argument("--resolution", help="Intended resolution (logged to sidecar)")
    ap.add_argument("--aspect", help="Intended aspect ratio (logged to sidecar)")
    ap.add_argument("--duration", type=int, help="Intended duration for video (s)")
    ap.add_argument("--target-provider", help="Where the user plans to run this (logged)")
    ap.add_argument("--target-model", help="Which model they plan to use (logged)")

    args = ap.parse_args()

    config = load_config()
    project = args.project or get_active_project(config) or "_unsorted"

    prompts_dir = resolve_prompts_dir(config, project=args.project)
    label = slugify(args.label)
    # Use a fake .md extension for the artifact path — sidecar writer adds .md so we'd get
    # double .md. Instead, write directly without going through write_render_sidecar's
    # path-mangling: build the sidecar at <prompts_dir>/<label>_NNN.md
    target = unique_path(prompts_dir, label, "md")

    settings = {
        "resolution": args.resolution,
        "aspect": args.aspect,
    }
    if args.type == "video":
        settings["duration"] = args.duration

    # Re-use the same sidecar writer for consistency. We pass the .md path as the
    # "artifact" and the writer appends .md — so we strip the suffix before passing in.
    # write_render_sidecar uses with_suffix(suffix + ".md") so passing 'foo.md' becomes
    # 'foo.md.md'. Workaround: pass a base path with no .md extension.
    base_path = target.with_suffix("")  # "foo" → sidecar writer makes "foo.md"

    sidecar = write_render_sidecar(
        base_path,
        provider=args.target_provider or "prompt-only",
        model=args.target_model or "—",
        render_type=args.type,
        project=project,
        prompt=args.prompt,
        cost_usd=0.0,
        tokens_used=args.token,
        settings=settings,
        extra={"mode": "prompt-only"},
    )

    print(f"prompt: {sidecar}", file=sys.stderr)
    print(str(sidecar))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ShotBuilderError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
