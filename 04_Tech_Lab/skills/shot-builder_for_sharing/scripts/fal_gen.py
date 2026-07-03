#!/usr/bin/env python3
"""
Shot Builder — FAL.ai generation script.

Calls FAL endpoints (sync or queue-based), downloads the result, saves locally,
and logs the render to workspace/INDEX.md.

Usage:
    python fal_gen.py --type image --model fal-ai/flux-pro/v1.1-ultra \\
        --prompt "..." --aspect "16:9" --label "HERO_base"

    python fal_gen.py --type video --model fal-ai/kling-video/v2.1/master \\
        --prompt "..." --image-url "https://..." --duration 5 --label "scene_01"

    python fal_gen.py --type upload --file /path/to/local.png
        # → uploads to FAL CDN, returns hosted URL (useful for image-to-video refs)
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

FAL_RUN_BASE = "https://fal.run"
FAL_QUEUE_BASE = "https://queue.fal.run"
FAL_STORAGE_UPLOAD = "https://fal.run/storage/upload"

# Endpoints that should use the queue API (long inference)
QUEUE_PREFIXES = (
    "fal-ai/kling-video/",
    "fal-ai/bytedance/seedance",
    "fal-ai/veo-",
    "fal-ai/runway-gen3/",
)


def is_queue_endpoint(endpoint_id: str) -> bool:
    return any(endpoint_id.startswith(p) for p in QUEUE_PREFIXES)


def http_post_json(url: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310 — trusted host
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise ShotBuilderError(f"FAL {url} → HTTP {e.code}: {body}") from e


def http_get_json(url: str, api_key: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Key {api_key}"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise ShotBuilderError(f"FAL {url} → HTTP {e.code}: {body}") from e


def upload_to_fal_storage(local_path: Path, api_key: str) -> str:
    """Upload a local file to FAL's CDN, return the hosted URL."""
    import mimetypes
    import secrets

    mime, _ = mimetypes.guess_type(local_path.name)
    mime = mime or "application/octet-stream"
    boundary = f"----shotbuilder{secrets.token_hex(8)}"
    body_parts: list[bytes] = []
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{local_path.name}"\r\n'.encode()
    )
    body_parts.append(f"Content-Type: {mime}\r\n\r\n".encode())
    body_parts.append(local_path.read_bytes())
    body_parts.append(f"\r\n--{boundary}--\r\n".encode())
    body = b"".join(body_parts)

    req = urllib.request.Request(
        FAL_STORAGE_UPLOAD,
        data=body,
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:  # noqa: S310
            data = json.loads(resp.read().decode("utf-8"))
            return data["url"]
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        raise ShotBuilderError(f"FAL upload failed → HTTP {e.code}: {body_text}") from e


def submit_sync(endpoint_id: str, payload: dict[str, Any], api_key: str) -> dict[str, Any]:
    """Sync inference — returns the result directly."""
    url = f"{FAL_RUN_BASE}/{endpoint_id}"
    return http_post_json(url, payload, api_key)


def submit_queue(
    endpoint_id: str, payload: dict[str, Any], api_key: str, poll_interval: float = 3.0, timeout: float = 300
) -> dict[str, Any]:
    """Queue inference — submit, poll status, fetch result."""
    submit_url = f"{FAL_QUEUE_BASE}/{endpoint_id}"
    submitted = http_post_json(submit_url, payload, api_key)
    request_id = submitted.get("request_id")
    if not request_id:
        raise ShotBuilderError(f"FAL queue submit returned no request_id: {submitted}")

    status_url = f"{FAL_QUEUE_BASE}/{endpoint_id}/requests/{request_id}/status"
    result_url = f"{FAL_QUEUE_BASE}/{endpoint_id}/requests/{request_id}"

    print(f"  queued: {request_id}", file=sys.stderr)
    deadline = time.time() + timeout
    while time.time() < deadline:
        status = http_get_json(status_url, api_key)
        s = status.get("status", "").upper()
        if s == "COMPLETED":
            return http_get_json(result_url, api_key)
        if s == "FAILED":
            raise ShotBuilderError(f"FAL queue task failed: {status}")
        print(f"  status: {s}", file=sys.stderr)
        time.sleep(poll_interval)

    raise ShotBuilderError(f"FAL queue task timed out after {timeout}s for {endpoint_id}")


def extract_artifact_url(result: dict[str, Any], kind: str) -> str:
    """Pull the artifact URL out of a FAL response. Different models nest differently."""
    # Common shapes:
    #   images: [{ url, content_type, width, height }, ...]
    #   image:  { url, ... }
    #   video:  { url, ... }
    #   audio:  { url, ... }
    if "images" in result and result["images"]:
        return result["images"][0]["url"]
    if "image" in result and isinstance(result["image"], dict):
        return result["image"]["url"]
    if "video" in result and isinstance(result["video"], dict):
        return result["video"]["url"]
    if "audio" in result and isinstance(result["audio"], dict):
        return result["audio"]["url"]
    # Some endpoints flatten the URL
    if "url" in result and isinstance(result["url"], str):
        return result["url"]
    raise ShotBuilderError(f"No artifact URL found in FAL response: {list(result.keys())}")


def build_image_payload(args: argparse.Namespace) -> dict[str, Any]:
    payload: dict[str, Any] = {"prompt": args.prompt}
    if args.aspect:
        payload["aspect_ratio"] = args.aspect
    elif args.image_size:
        payload["image_size"] = args.image_size
    if args.seed is not None:
        payload["seed"] = args.seed
    if args.image_url:
        payload["image_url"] = args.image_url
    if args.image_urls:
        payload["image_urls"] = args.image_urls
    if args.num_images is not None:
        payload["num_images"] = args.num_images
    if args.safety_tolerance is not None:
        payload["safety_tolerance"] = args.safety_tolerance
    if args.raw:
        payload["raw"] = True
    payload["enable_safety_checker"] = not args.disable_safety_checker
    return payload


def build_video_payload(args: argparse.Namespace) -> dict[str, Any]:
    payload: dict[str, Any] = {"prompt": args.prompt}
    if args.image_url:
        payload["image_url"] = args.image_url
    if args.duration is not None:
        payload["duration"] = str(args.duration)  # Kling takes string
    if args.aspect:
        payload["aspect_ratio"] = args.aspect
    if args.seed is not None:
        payload["seed"] = args.seed
    if args.negative_prompt:
        payload["negative_prompt"] = args.negative_prompt
    if args.cfg_scale is not None:
        payload["cfg_scale"] = args.cfg_scale
    return payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", required=True, choices=["image", "video", "upload"], help="Generation type")
    ap.add_argument("--model", help="FAL endpoint_id (e.g., fal-ai/flux-pro/v1.1-ultra)")
    ap.add_argument("--prompt", help="Prompt text")
    ap.add_argument("--label", default="render", help="Filename label (slugified)")

    # Image params
    ap.add_argument("--aspect", help="aspect_ratio (16:9, 2.39:1, 4:5, etc.)")
    ap.add_argument("--image-size", help="image_size enum (landscape_16_9, etc.) — alternative to --aspect")
    ap.add_argument("--num-images", type=int)
    ap.add_argument("--safety-tolerance", type=int)
    ap.add_argument("--raw", action="store_true")
    ap.add_argument("--disable-safety-checker", action="store_true")

    # Reference images (image-to-image, image-to-video)
    ap.add_argument("--image-url", help="Reference image URL")
    ap.add_argument("--image-urls", nargs="+", help="Multiple reference image URLs")

    # Video params
    ap.add_argument("--duration", type=int)
    ap.add_argument("--negative-prompt")
    ap.add_argument("--cfg-scale", type=float)

    # Shared
    ap.add_argument("--seed", type=int)
    ap.add_argument("--timeout", type=float, default=300.0, help="Queue poll timeout (s)")
    ap.add_argument(
        "--project",
        help="Project slug to route renders into (defaults to config.active_project)",
    )
    ap.add_argument(
        "--tier",
        choices=["preview", "hero"],
        default="preview",
        help="Cost tier — 'preview' uses $0.50 threshold, 'hero' uses $1.00",
    )
    ap.add_argument(
        "--confirm-cost",
        action="store_true",
        help="Bypass cost gate (user approved). Without this, video > threshold refuses to submit.",
    )
    ap.add_argument(
        "--token",
        action="append",
        default=[],
        help="Token used in this render (e.g. <HERO>). Repeatable. Logged to the sidecar.",
    )

    # Upload
    ap.add_argument("--file", help="Local file to upload (--type upload)")

    args = ap.parse_args()

    config = load_config()
    api_key = load_api_key("fal", config)

    if args.type == "upload":
        if not args.file:
            ap.error("--type upload requires --file")
        local = Path(args.file).expanduser()
        if not local.exists():
            raise ShotBuilderError(f"file not found: {local}")
        url = upload_to_fal_storage(local, api_key)
        print(url)
        return 0

    if not args.model or not args.prompt:
        ap.error("--type image/video requires --model and --prompt")

    if args.type == "image":
        payload = build_image_payload(args)
        kind = "shots"
        ext = "png"
    else:  # video
        payload = build_video_payload(args)
        kind = "scenes"
        ext = "mp4"

    print(f"→ FAL {args.type} call: {args.model}", file=sys.stderr)
    print(f"  payload: {json.dumps(payload, indent=2)}", file=sys.stderr)

    if is_queue_endpoint(args.model):
        result = submit_queue(args.model, payload, api_key, timeout=args.timeout)
    else:
        result = submit_sync(args.model, payload, api_key)

    # Pre-flight cost gate
    estimated_cost: float | None = None
    try:
        if args.type == "image":
            estimated_cost = estimate_image(
                "fal", args.model, resolution=getattr(args, "resolution", None) or "2K"
            )
        else:
            estimated_cost = estimate_video(
                "fal",
                args.model,
                duration=args.duration or 5,
                resolution=getattr(args, "resolution", None) or "1080p",
                with_audio=False,
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

    artifact_url = extract_artifact_url(result, args.type)
    output_dir = resolve_output_dir(kind, config, project=args.project)
    label = slugify(args.label)
    target = unique_path(output_dir, label, ext)
    download_to_local(artifact_url, target)
    print(f"  saved: {target}", file=sys.stderr)

    # Sidecar
    log_project = args.project or config.get("active_project") or "_unsorted"
    sidecar_settings = {
        "aspect": getattr(args, "aspect", None) or getattr(args, "image_size", None),
    }
    if args.type == "video":
        sidecar_settings["duration"] = args.duration
    if getattr(args, "seed", None):
        sidecar_settings["seed"] = args.seed
    sidecar = write_render_sidecar(
        target,
        provider="fal",
        model=args.model,
        render_type=args.type,
        project=log_project,
        prompt=args.prompt,
        cost_usd=estimated_cost,
        tokens_used=args.token,
        settings=sidecar_settings,
    )
    print(f"  sidecar: {sidecar}", file=sys.stderr)

    # Log
    now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    append_index_render(
        {
            "date": now_date,
            "provider": "fal",
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
                "provider": "fal",
                "model": args.model,
                "type": args.type,
                "cost_usd": estimated_cost,
                "path": str(target),
                "project": log_project,
            }) + "\n")

    # stdout = clean path for caller
    print(str(target))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ShotBuilderError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
