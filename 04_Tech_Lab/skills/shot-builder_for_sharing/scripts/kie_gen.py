#!/usr/bin/env python3
"""
Shot Builder — Kie.ai generation script.

Kie is task-based and asynchronous. Submit → poll → download.

Usage:
    python kie_gen.py --type image --model nano-banana-pro \\
        --prompt "..." --resolution 2k --aspect 16:9 --label "HERO_base"

    python kie_gen.py --type video --model kling-2.6 \\
        --prompt "..." --image-url "https://..." --duration 5 --label "scene_01"

    python kie_gen.py --type credit
        # → print remaining credit balance
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from _common import (
    ShotBuilderError,
    append_index_render,
    download_to_local,
    load_api_key,
    load_config,
    resolve_output_dir,
    slugify,
    touch_index_modified,
    unique_path,
    write_render_sidecar,
)
from cost import (  # noqa: E402
    GATE_THRESHOLDS,
    SESSION_LOG,
    estimate_image,
    estimate_video,
)

KIE_BASE = "https://api.kie.ai"
KIE_CREATE_TASK = f"{KIE_BASE}/api/v1/jobs/createTask"
KIE_RECORD_INFO = f"{KIE_BASE}/api/v1/jobs/recordInfo"
KIE_CREDIT = f"{KIE_BASE}/api/v1/chat/credit"


def http_post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310 — trusted host
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise ShotBuilderError(f"Kie {url} → HTTP {e.code}: {body}") from e


def http_get_json(url: str, api_key: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    if params:
        from urllib.parse import urlencode
        url = f"{url}?{urlencode(params)}"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise ShotBuilderError(f"Kie {url} → HTTP {e.code}: {body}") from e


def submit_task(payload: dict[str, Any], api_key: str) -> str:
    """POST to createTask. Returns taskId."""
    body = http_post_json(KIE_CREATE_TASK, payload, api_key)
    task_id = body.get("data", {}).get("taskId")
    if not task_id:
        raise ShotBuilderError(f"Kie createTask returned no taskId: {body}")
    return task_id


def poll_task(task_id: str, api_key: str, poll_interval: float, timeout: float) -> dict[str, Any]:
    """Poll recordInfo until the task succeeds or fails. Returns the final data block."""
    # Kie returns the state under `data.state` (success / fail / waiting / generating / ...).
    # Older docs say `status` + `completed/failed`; the live API uses `state` + `success/fail`.
    # Keep both for forward compat.
    deadline = time.time() + timeout
    while time.time() < deadline:
        info = http_get_json(KIE_RECORD_INFO, api_key, params={"taskId": task_id})
        data = info.get("data") or {}
        state = (data.get("state") or data.get("status") or "").lower()
        if state in ("success", "completed"):
            return data
        if state in ("fail", "failed"):
            err = data.get("failMsg") or data.get("error") or "unknown error"
            raise ShotBuilderError(f"Kie task {task_id} failed: {err}")
        print(f"  state: {state}", file=sys.stderr)
        time.sleep(poll_interval)
    raise ShotBuilderError(f"Kie task {task_id} timed out after {timeout}s")


def extract_artifact_url(data: dict[str, Any]) -> str:
    # Modern Kie shape: data.resultJson is a JSON-encoded string with resultUrls: [..].
    raw = data.get("resultJson")
    if isinstance(raw, str) and raw:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = {}
        urls = parsed.get("resultUrls") or parsed.get("urls") or []
        if urls and isinstance(urls, list):
            return urls[0]
    # Legacy shape: data.result.{url,imageUrl,...} or data.result.files[].url
    result = data.get("result") or {}
    if isinstance(result, dict):
        for key in ("url", "imageUrl", "videoUrl", "audioUrl", "outputUrl"):
            if key in result and result[key]:
                return result[key]
        files = result.get("files") or []
        if files and isinstance(files, list) and "url" in files[0]:
            return files[0]["url"]
    raise ShotBuilderError(f"No artifact URL in Kie response: {data}")


def build_image_payload(args: argparse.Namespace) -> dict[str, Any]:
    # Kie's createTask requires params under an `input` wrapper. `resolution` must be uppercase ("1K", "2K", "4K").
    inp: dict[str, Any] = {"prompt": args.prompt}
    if args.resolution:
        inp["resolution"] = args.resolution.upper()
    if args.aspect:
        inp["aspectRatio"] = args.aspect
    if args.width:
        inp["width"] = args.width
    if args.height:
        inp["height"] = args.height
    if args.reference_images:
        inp["referenceImages"] = args.reference_images
    if args.enable_translation:
        inp["enableTranslation"] = True
    if args.seed is not None:
        inp["seed"] = args.seed
    return {"model": args.model, "input": inp}


def build_video_payload(args: argparse.Namespace) -> dict[str, Any]:
    inp: dict[str, Any] = {"prompt": args.prompt}
    if args.image_url:
        inp["imageUrl"] = args.image_url
    if args.duration is not None:
        inp["duration"] = args.duration
    if args.aspect:
        inp["aspectRatio"] = args.aspect
    if args.with_audio:
        inp["withAudio"] = True
        if args.audio_type:
            inp["audioType"] = args.audio_type
        if args.language:
            inp["language"] = args.language
    if args.seed is not None:
        inp["seed"] = args.seed
    return {"model": args.model, "input": inp}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--type",
        required=True,
        choices=["image", "video", "credit"],
        help="Generation type or credit check",
    )
    ap.add_argument("--model", help="Kie model id (nano-banana-pro, flux-2, kling-2.6, etc.)")
    ap.add_argument("--prompt", help="Prompt text")
    ap.add_argument("--label", default="render", help="Filename label")

    # Image params
    ap.add_argument("--resolution", help="1k / 2k / 4k")
    ap.add_argument("--aspect", help="aspectRatio (16:9, 9:16, 2.39:1, 4:5, 1:1)")
    ap.add_argument("--width", type=int)
    ap.add_argument("--height", type=int)
    ap.add_argument("--reference-images", nargs="+", help="Up to 8 reference image URLs")
    ap.add_argument("--enable-translation", action="store_true")

    # Video params
    ap.add_argument("--image-url", help="Reference image URL for image-to-video")
    ap.add_argument("--duration", type=int)
    ap.add_argument(
        "--with-audio",
        action="store_true",
        help="Native audio sync (Kling 2.6)",
    )
    ap.add_argument(
        "--audio-type",
        choices=["dialogue", "narration", "music", "sfx"],
    )
    ap.add_argument("--language", choices=["en", "zh"])

    # Shared
    ap.add_argument("--seed", type=int)
    ap.add_argument(
        "--poll-interval",
        type=float,
        default=None,
        help="Override poll interval (s) — image default 2.0, video default 5.0",
    )
    ap.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Override timeout (s) — image default 120, video default 300",
    )
    ap.add_argument(
        "--project",
        help="Project slug to route renders into (defaults to config.active_project)",
    )
    ap.add_argument(
        "--tier",
        choices=["preview", "hero"],
        default="preview",
        help="Cost tier — 'preview' uses lower threshold ($0.50), 'hero' uses higher ($1.00)",
    )
    ap.add_argument(
        "--confirm-cost",
        action="store_true",
        help="Bypass cost gate (user has already approved). Without this, video >threshold will refuse to submit.",
    )
    ap.add_argument(
        "--token",
        action="append",
        default=[],
        help="Token used in this render (e.g. <HERO>). Repeatable. Logged to the sidecar.",
    )

    args = ap.parse_args()

    config = load_config()
    api_key = load_api_key("kie", config)

    if args.type == "credit":
        body = http_get_json(KIE_CREDIT, api_key)
        print(json.dumps(body, indent=2))
        return 0

    if not args.model or not args.prompt:
        ap.error("--type image/video requires --model and --prompt")

    if args.type == "image":
        payload = build_image_payload(args)
        kind = "shots"
        ext = "png"
        poll_interval = args.poll_interval or 2.0
        timeout = args.timeout or 120.0
    else:  # video
        payload = build_video_payload(args)
        kind = "scenes"
        ext = "mp4"
        poll_interval = args.poll_interval or 5.0
        timeout = args.timeout or 300.0

    # Pre-flight cost gate (video only — images too cheap to gate)
    estimated_cost: float | None = None
    try:
        if args.type == "image":
            estimated_cost = estimate_image(
                "kie", args.model, resolution=args.resolution or "2K"
            )
        else:
            with_audio = bool(getattr(args, "audio_type", None))
            estimated_cost = estimate_video(
                "kie",
                args.model,
                duration=args.duration or 5,
                resolution=args.resolution or "1080p",
                with_audio=with_audio,
            )
    except ShotBuilderError as e:
        print(f"  cost lookup failed: {e}", file=sys.stderr)

    if args.type == "video" and estimated_cost is not None:
        threshold = GATE_THRESHOLDS["video_hero"] if args.tier == "hero" else GATE_THRESHOLDS["video_preview"]
        if estimated_cost > threshold and not args.confirm_cost:
            raise ShotBuilderError(
                f"estimated cost ${estimated_cost:.4f} exceeds {args.tier} threshold ${threshold:.2f}. "
                f"Re-run with --confirm-cost after explicit user approval."
            )
        print(f"  estimated cost: ${estimated_cost:.4f} (tier={args.tier}, threshold=${threshold:.2f})", file=sys.stderr)

    print(f"→ Kie {args.type} task: {args.model}", file=sys.stderr)
    print(f"  payload: {json.dumps(payload, indent=2)}", file=sys.stderr)

    task_id = submit_task(payload, api_key)
    print(f"  taskId: {task_id}", file=sys.stderr)

    data = poll_task(task_id, api_key, poll_interval=poll_interval, timeout=timeout)
    artifact_url = extract_artifact_url(data)

    output_dir = resolve_output_dir(kind, config, project=args.project)
    label = slugify(args.label)
    target = unique_path(output_dir, label, ext)
    download_to_local(artifact_url, target)
    print(f"  saved: {target}", file=sys.stderr)

    # Write markdown sidecar
    log_project = args.project or config.get("active_project") or "_unsorted"
    sidecar_settings = {
        "resolution": args.resolution,
        "aspect": args.aspect,
    }
    if args.type == "video":
        sidecar_settings["duration"] = args.duration
        if getattr(args, "audio_type", None):
            sidecar_settings["audio_type"] = args.audio_type
        if getattr(args, "language", None):
            sidecar_settings["language"] = args.language
    if getattr(args, "seed", None):
        sidecar_settings["seed"] = args.seed
    sidecar = write_render_sidecar(
        target,
        provider="kie",
        model=args.model,
        render_type=args.type,
        project=log_project,
        prompt=args.prompt,
        cost_usd=estimated_cost,
        tokens_used=args.token,
        settings=sidecar_settings,
        extra={"task_id": task_id},
    )
    print(f"  sidecar: {sidecar}", file=sys.stderr)

    # Log
    now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    append_index_render(
        {
            "date": now_date,
            "provider": "kie",
            "model": args.model,
            "project": log_project,
            "format": args.type,
            "cost": f"${estimated_cost:.4f}" if estimated_cost is not None else "—",
            "path": str(target),
        }
    )
    touch_index_modified()

    # Append to session cost log
    if estimated_cost is not None:
        SESSION_LOG.parent.mkdir(parents=True, exist_ok=True)
        with SESSION_LOG.open("a") as f:
            f.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "provider": "kie",
                "model": args.model,
                "type": args.type,
                "cost_usd": estimated_cost,
                "path": str(target),
                "project": log_project,
            }) + "\n")

    # stdout = clean path
    print(str(target))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ShotBuilderError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
