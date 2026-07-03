#!/usr/bin/env python3
"""
Shot Builder — Cost estimation and session tracking.

Every video render consults this before submitting. Image renders are too cheap
to gate, but their cost is still logged for session totals.

Estimates are USD. Per-model price tables live in references/defaults.md and are
mirrored here in PRICE_TABLE — keep them in sync.

Usage:
    python cost.py estimate --provider kie --model kling-2.6 --type video --duration 8 --resolution 1080p
    python cost.py estimate --provider fal --model fal-ai/flux-pro/v1.1-ultra --type image
    python cost.py session                    # session total from workspace/session_costs.jsonl
    python cost.py session --reset            # clear session log
    python cost.py log --provider <p> --model <m> --type <t> --cost <usd> --path <file>
    python cost.py balance --provider kie     # check remaining credits (calls provider)
    python cost.py gate --type video --resolution 480p --cost <usd>   # exit 0 if ok, 2 if needs confirmation

Exit codes:
    0  ok / under threshold
    1  invalid args / unknown model
    2  cost exceeds threshold (caller must confirm)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from _common import (  # noqa: E402
    WORKSPACE,
    ShotBuilderError,
    load_api_key,
    load_config,
)

SESSION_LOG = WORKSPACE / "session_costs.jsonl"

# Approximate USD per render. Source: providers/fal.md, providers/kie.md, vendor pricing docs.
# Format: PRICE_TABLE[provider][model] = {"image": price, "video_per_second": price, ...}
# Where applicable, give a midpoint of the published range.
PRICE_TABLE: dict[str, dict[str, dict[str, float]]] = {
    "fal": {
        # Image models — flat per-image price
        "fal-ai/flux-pro/v1.1-ultra": {"image": 0.05},
        "fal-ai/flux-pro/v1.1": {"image": 0.04},
        "fal-ai/flux-pro/kontext": {"image": 0.04},
        "fal-ai/flux/dev": {"image": 0.025},
        "fal-ai/flux/schnell": {"image": 0.003},
        "fal-ai/recraft-v3": {"image": 0.04},
        "fal-ai/ideogram/v2": {"image": 0.08},
        "fal-ai/nano-banana": {"image": 0.039},
        "fal-ai/nano-banana/edit": {"image": 0.039},
        "fal-ai/nano-banana-pro": {"image": 0.05},
        "fal-ai/nano-banana-pro/edit": {"image": 0.05},
        # Video models — per-second base price
        "fal-ai/kling-video/v2.1/master": {"video_per_second": 0.10},
        "fal-ai/kling-video/v3/pro/image-to-video": {"video_per_second": 0.15},
        "fal-ai/bytedance/seedance/v1/pro/image-to-video": {"video_per_second": 0.08},
        "fal-ai/veo-3": {"video_per_second": 0.20},
        "fal-ai/runway-gen3/turbo/image-to-video": {"video_per_second": 0.15},
    },
    "kie": {
        # Image
        "nano-banana-pro": {"image": 0.035},
        "nano-banana-basic": {"image": 0.02},
        "flux-2": {"image": 0.055},
        "4o-image": {"image": 0.07},
        # Video — Kie's Kling 2.6 list: ~$0.28 (5s, no audio), ~$1.10 (10s + audio)
        # Approximate as base + per-second + audio uplift.
        "kling-2.6": {
            "video_base": 0.10,
            "video_per_second": 0.036,
            "video_audio_uplift": 0.30,
        },
        "veo-3.1": {
            "video_base": 0.20,
            "video_per_second": 0.18,
            "video_audio_uplift": 0.30,
        },
        "runway": {"video_per_second": 0.15},
        "sora-2": {"video_per_second": 0.25},
        # Audio
        "suno-v5": {"audio_track": 0.10},
    },
}

# Resolution multipliers — pricing usually scales sub-linearly with resolution.
RESOLUTION_MULTIPLIER = {
    "image": {"1K": 1.0, "2K": 1.4, "4K": 2.5},
    "video": {"480p": 0.45, "720p": 0.7, "1080p": 1.0, "4K": 2.5},
}

# Cost thresholds (USD) for gating. ~$0.50 ≈ 100 credits at most providers.
GATE_THRESHOLDS = {
    "image": None,  # never gate on images
    "video_preview": 0.50,  # >$0.50 preview => confirm
    "video_hero": 1.00,  # >$1.00 hero => always confirm
}


def estimate_image(provider: str, model: str, resolution: str = "2K") -> float:
    table = PRICE_TABLE.get(provider, {})
    spec = table.get(model)
    if not spec or "image" not in spec:
        raise ShotBuilderError(
            f"no price for image model '{model}' on '{provider}'. "
            f"Add to PRICE_TABLE in scripts/cost.py."
        )
    base = spec["image"]
    mult = RESOLUTION_MULTIPLIER["image"].get(resolution, 1.0)
    return round(base * mult, 4)


def estimate_video(
    provider: str,
    model: str,
    duration: int,
    resolution: str = "1080p",
    with_audio: bool = False,
) -> float:
    table = PRICE_TABLE.get(provider, {})
    spec = table.get(model)
    if not spec:
        raise ShotBuilderError(
            f"no price for video model '{model}' on '{provider}'. "
            f"Add to PRICE_TABLE in scripts/cost.py."
        )
    base = spec.get("video_base", 0.0)
    per_sec = spec.get("video_per_second", 0.0)
    audio_uplift = spec.get("video_audio_uplift", 0.0) if with_audio else 0.0
    raw = base + (per_sec * duration) + audio_uplift
    mult = RESOLUTION_MULTIPLIER["video"].get(resolution, 1.0)
    return round(raw * mult, 4)


def cmd_estimate(args: argparse.Namespace) -> int:
    try:
        if args.type == "image":
            cost = estimate_image(args.provider, args.model, args.resolution or "2K")
        elif args.type == "video":
            cost = estimate_video(
                args.provider,
                args.model,
                duration=args.duration or 5,
                resolution=args.resolution or "1080p",
                with_audio=args.with_audio,
            )
        else:
            print(f"unknown --type: {args.type}", file=sys.stderr)
            return 1
    except ShotBuilderError as e:
        print(str(e), file=sys.stderr)
        return 1

    print(f"{cost:.4f}")
    if args.verbose:
        params = f"{args.provider}/{args.model} {args.type} {args.resolution or 'default'}"
        if args.type == "video":
            params += f" {args.duration or 5}s"
            if args.with_audio:
                params += " +audio"
        print(f"# {params} = ${cost:.4f}", file=sys.stderr)
    return 0


def cmd_log(args: argparse.Namespace) -> int:
    SESSION_LOG.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "provider": args.provider,
        "model": args.model,
        "type": args.type,
        "cost_usd": args.cost,
        "path": args.path or "",
        "project": args.project or "",
    }
    with SESSION_LOG.open("a") as f:
        f.write(json.dumps(row) + "\n")
    print(f"logged ${args.cost:.4f} ({args.provider}/{args.model})", file=sys.stderr)
    return 0


def cmd_session(args: argparse.Namespace) -> int:
    if args.reset:
        if SESSION_LOG.exists():
            SESSION_LOG.unlink()
            print("session log cleared")
        else:
            print("no session log to clear")
        return 0

    if not SESSION_LOG.exists():
        print("Session total: $0.0000 (no renders yet)")
        return 0

    total = 0.0
    count = 0
    by_provider: dict[str, float] = {}
    by_project: dict[str, float] = {}
    with SESSION_LOG.open() as f:
        for line in f:
            try:
                row = json.loads(line)
                cost = float(row.get("cost_usd", 0))
                total += cost
                count += 1
                by_provider[row.get("provider", "?")] = (
                    by_provider.get(row.get("provider", "?"), 0) + cost
                )
                if row.get("project"):
                    by_project[row["project"]] = by_project.get(row["project"], 0) + cost
            except json.JSONDecodeError:
                continue

    print(f"Session total: ${total:.4f}  ({count} renders)")
    if by_provider:
        print("By provider:")
        for p, c in sorted(by_provider.items()):
            print(f"  {p:<6} ${c:.4f}")
    if by_project:
        print("By project:")
        for p, c in sorted(by_project.items()):
            print(f"  {p:<20} ${c:.4f}")
    return 0


def cmd_balance(args: argparse.Namespace) -> int:
    """Hit the provider's credit/balance endpoint. Read-only."""
    config = load_config()
    api_key = load_api_key(args.provider, config)

    if args.provider == "kie":
        url = "https://api.kie.ai/api/v1/chat/credit"
        headers = {"Authorization": f"Bearer {api_key}"}
    elif args.provider == "fal":
        # FAL doesn't expose a public credit endpoint; fail with a helpful message.
        print(
            "FAL does not expose a public balance endpoint. "
            "Check https://fal.ai/dashboard/usage in your browser.",
            file=sys.stderr,
        )
        return 1
    else:
        print(f"unknown --provider: {args.provider}", file=sys.stderr)
        return 1

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:  # noqa: S310 — trusted vendor
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} from {args.provider}: {e.read().decode(errors='replace')}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"network error: {e}", file=sys.stderr)
        return 1

    print(json.dumps(body, indent=2))
    return 0


def cmd_gate(args: argparse.Namespace) -> int:
    """
    Return 0 if cost is under threshold, 2 if it exceeds.
    Caller (kie_gen / fal_gen) checks the exit code before submitting.
    """
    if args.type == "image":
        return 0  # never gate images

    if args.tier == "hero":
        threshold = GATE_THRESHOLDS["video_hero"]
    else:
        threshold = GATE_THRESHOLDS["video_preview"]

    if args.cost > threshold:
        print(
            f"cost ${args.cost:.4f} exceeds {args.tier} threshold ${threshold:.2f}. "
            f"Require explicit user confirmation before submitting.",
            file=sys.stderr,
        )
        return 2
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Cost estimation + session tracking.")
    sub = ap.add_subparsers(dest="command", required=True)

    p_est = sub.add_parser("estimate", help="estimate USD cost for a render")
    p_est.add_argument("--provider", required=True, choices=["fal", "kie"])
    p_est.add_argument("--model", required=True)
    p_est.add_argument("--type", required=True, choices=["image", "video"])
    p_est.add_argument("--resolution")
    p_est.add_argument("--duration", type=int)
    p_est.add_argument("--with-audio", action="store_true")
    p_est.add_argument("--verbose", action="store_true")

    p_log = sub.add_parser("log", help="append a render row to session log")
    p_log.add_argument("--provider", required=True)
    p_log.add_argument("--model", required=True)
    p_log.add_argument("--type", required=True, choices=["image", "video"])
    p_log.add_argument("--cost", type=float, required=True)
    p_log.add_argument("--path")
    p_log.add_argument("--project")

    p_sess = sub.add_parser("session", help="show session total")
    p_sess.add_argument("--reset", action="store_true")

    p_bal = sub.add_parser("balance", help="check remaining credits with provider")
    p_bal.add_argument("--provider", required=True, choices=["fal", "kie"])

    p_gate = sub.add_parser(
        "gate",
        help="check if a cost requires confirmation (exit 0 ok / exit 2 needs confirm)",
    )
    p_gate.add_argument("--type", required=True, choices=["image", "video"])
    p_gate.add_argument("--cost", type=float, required=True)
    p_gate.add_argument("--tier", choices=["preview", "hero"], default="preview")

    args = ap.parse_args()

    if args.command == "estimate":
        return cmd_estimate(args)
    if args.command == "log":
        return cmd_log(args)
    if args.command == "session":
        return cmd_session(args)
    if args.command == "balance":
        return cmd_balance(args)
    if args.command == "gate":
        return cmd_gate(args)

    ap.error(f"unknown command: {args.command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
