"""
One-command reel pipeline for Pineapple testimonial repurposing.

What it does:
1) Cuts 3 approved clips from one or many long-form videos.
2) Generates 2 hook variants per clip (comment-rate, share-rate).
3) Optionally overlays a photo in the opening seconds.
4) Exports ready-to-post MP4 files to READY-TO-BLAST.
5) Writes post-ready caption packs (.md) and manifest (.json).

Run:
    python 04_Tech_Lab/reel_hook_pipeline.py
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


DEFAULT_SOURCE = Path(
    r"C:\Pineapple-Mana-Global\02_Media_Vault\Pineapple-Media-HQ\2026_05_GENERAL_INBOX\Raw_Mana_Capture\Testimonials\mike fendek testimonial.mp4"
)
DEFAULT_OUTPUT = Path(
    r"C:\Pineapple-Mana-Global\02_Media_Vault\2026_05_GENERAL_READY-TO-BLAST"
)
DEFAULT_PHOTO_DIR = Path(
    r"C:\Pineapple-Mana-Global\02_Media_Vault\Pineapple-Media-HQ\2026_05_GENERAL_PERSONAL-ASSET"
)

FONT_PATH = r"C\:/Windows/Fonts/arialbd.ttf"

# Approved cut windows (from transcript analysis)
CLIPS = [
    {
        "id": "01",
        "slug": "INSURANCE_PUSHBACK",
        "start": "00:01:14.640",
        "end": "00:01:33.620",
        "cta_keyword": "ROOF",
    },
    {
        "id": "02",
        "slug": "UMPIRE_RULED",
        "start": "00:04:11.460",
        "end": "00:04:33.660",
        "cta_keyword": "CLAIM",
    },
    {
        "id": "03",
        "slug": "PEACE_OF_MIND",
        "start": "00:09:42.020",
        "end": "00:10:06.340",
        "cta_keyword": "SAFE",
    },
]

VARIANTS = {
    "CMT": {
        "label": "comment-rate",
        "hook_text": {
            "01": "INSURANCE SAID NO. WOULD YOU PUSH BACK?",
            "02": "PERSISTENCE OR LUCK?",
            "03": "LOWEST BID OR PEACE OF MIND?",
        },
        "ig_caption": {
            "01": "Denied once? Would you have pushed back or moved on? This homeowner stayed persistent and got traction. Strength, integrity, elite execution. Comment {keyword} for a Complimentary Roof Inspection.",
            "02": "Delay after delay, then the ruling moved in the homeowner's favor. Most people quit too early. Agree or disagree? Comment {keyword} for a Complimentary Roof Inspection.",
            "03": "What matters most to you after storm damage: lowest price or real peace of mind? This homeowner made his choice. Comment {keyword} for a Complimentary Roof Inspection.",
        },
        "fb_caption": {
            "01": "Insurance pushed back first. This homeowner did not fold. Would you keep fighting or move on? Comment {keyword} and we will walk you through a Complimentary Roof Inspection.",
            "02": "The process was long, but persistence changed the outcome. Do you think most homeowners quit too soon? Comment {keyword} for a Complimentary Roof Inspection.",
            "03": "Honest question: lowest bid, or confidence your home is protected? This story says a lot. Comment {keyword} for a Complimentary Roof Inspection.",
        },
    },
    "SHR": {
        "label": "share-rate",
        "hook_text": {
            "01": "DENIED ONCE? DO THESE 3 THINGS FIRST.",
            "02": "HOW TO SURVIVE CLAIM DELAYS.",
            "03": "SAVE THIS: WHAT REAL PEACE OF MIND LOOKS LIKE.",
        },
        "ig_caption": {
            "01": "Denied claim? Do this: 1) Request a real adjuster review. 2) Document visible damage clearly. 3) Work with a contractor that supports the full process. Save or share this with a homeowner. Comment {keyword} for a Complimentary Roof Inspection.",
            "02": "When claims drag out: stay polite, stay persistent, document everything. This homeowner stayed the course and got movement. Save this for storm season and share it. Comment {keyword} for a Complimentary Roof Inspection.",
            "03": "Real restoration is more than shingles. It is leak protection, confidence, and peace of mind. Save this and share it with a homeowner who needs clarity. Comment {keyword} for a Complimentary Roof Inspection.",
        },
        "fb_caption": {
            "01": "If a claim is denied, do not panic. Ask for a proper review, gather evidence, and stay persistent. Share this with a homeowner who needs it. Comment {keyword} for a Complimentary Roof Inspection.",
            "02": "Claim delays are common. Documentation and persistence matter. Save this as a reminder and send it to someone dealing with storm damage. Comment {keyword} for a Complimentary Roof Inspection.",
            "03": "The goal is not only a new roof. The goal is confidence your home is protected. Share this with someone who needs this perspective. Comment {keyword} for a Complimentary Roof Inspection.",
        },
    },
}

HASHTAGS = (
    "#PineappleRoofing #RoofDamage #InsuranceClaimHelp #StormDamage "
    "#DFWHomeowners #RoofRestoration #HomeProtection #TexasRoofing"
)


def _slugify(name: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", name.strip()).strip("_")
    return cleaned.upper()[:36] if cleaned else "SOURCE"


def _ffprobe_duration_seconds(path: Path) -> float:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffprobe failed for {path}: {proc.stderr.strip()}")
    return float(proc.stdout.strip())


def _hms_to_seconds(value: str) -> float:
    hh, mm, ss = value.split(":")
    return int(hh) * 3600 + int(mm) * 60 + float(ss)


def _seconds_to_hms(seconds: float) -> str:
    seconds = max(0.0, seconds)
    hh = int(seconds // 3600)
    mm = int((seconds % 3600) // 60)
    ss = seconds - (hh * 3600 + mm * 60)
    return f"{hh:02d}:{mm:02d}:{ss:06.3f}"


def _resolve_window(duration: float, start: str, end: str, mode: str, clip_index: int) -> tuple[str, str] | None:
    start_s = _hms_to_seconds(start)
    end_s = _hms_to_seconds(end)

    if end_s <= duration:
        return start, end

    if mode == "skip":
        return None

    # Adaptive fallback for short sources:
    # keep the original clip length target when possible, otherwise use available duration.
    target_len = max(8.0, end_s - start_s)
    usable_len = min(target_len, max(8.0, duration))

    # Stagger starting point by clip index to avoid identical windows.
    offset = min(float(clip_index) * 1.5, max(0.0, duration - usable_len))
    new_start = offset
    new_end = min(duration, new_start + usable_len)
    return _seconds_to_hms(new_start), _seconds_to_hms(new_end)


def _discover_photos(photo_dir: Path) -> list[Path]:
    if not photo_dir.exists():
        return []
    out: list[Path] = []
    for pattern in ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.JPG", "*.JPEG", "*.PNG", "*.WEBP"):
        out.extend(photo_dir.glob(pattern))
    return sorted(set(out))


def _escape_drawtext(text: str) -> str:
    text = text.replace("\\", "\\\\")
    text = text.replace(":", r"\:")
    text = text.replace("'", "\\'")
    text = text.replace("%", r"\%")
    return text


def _ffmpeg_cmd(
    source: Path,
    out_file: Path,
    start: str,
    end: str,
    hook_text: str,
    intro_photo: Path | None,
    intro_seconds: float,
) -> list[str]:
    escaped = _escape_drawtext(hook_text)
    base_vf = "scale=1920:-2,crop=1920:1080"

    draw_layer = (
        "drawbox=x=0:y=0:w=1920:h=170:color=black@0.55:t=fill:enable='between(t,0,3)',"
        f"drawtext=fontfile='{FONT_PATH}':"
        f"text='{escaped}':"
        "fontcolor=white:fontsize=62:"
        "x=(w-text_w)/2:y=48:"
        "enable='between(t,0,3)'"
    )

    cmd = [
        "ffmpeg",
        "-y",
        "-ss",
        start,
        "-to",
        end,
        "-i",
        str(source),
    ]

    if intro_photo is not None:
        cmd.extend(["-loop", "1", "-t", f"{intro_seconds:.2f}", "-i", str(intro_photo)])
        vf = (
            "[0:v]"
            + base_vf
            + "[base];"
            "[1:v]scale=1920:1080[photo];"
            f"[base][photo]overlay=0:0:enable='between(t,0,{intro_seconds:.2f})',"
            + draw_layer
        )
        cmd.extend([
            "-filter_complex",
            vf,
            "-map",
            "0:v:0",
            "-map",
            "0:a:0",
        ])
    else:
        vf = base_vf + "," + draw_layer
        cmd.extend([
            "-vf",
            vf,
            "-map",
            "0:v:0",
            "-map",
            "0:a:0",
        ])

    cmd.extend(
        [
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-profile:v",
            "high",
            "-level",
            "4.1",
            "-pix_fmt",
            "yuv420p",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-ac",
            "2",
            "-movflags",
            "+faststart",
            str(out_file),
        ]
    )
    return cmd


def _write_pack(
    pack_dir: Path,
    clip: dict,
    variant_key: str,
    video_path: Path,
    source_name: str,
    intro_photo: Path | None,
) -> Path:
    variant = VARIANTS[variant_key]
    cid = clip["id"]
    keyword = clip["cta_keyword"]

    content = (
        f"# Pineapple Reel Post Pack\n\n"
        f"- Source: {source_name}\n"
        f"- Clip ID: {cid}\n"
        f"- Variant: {variant['label']} ({variant_key})\n"
        f"- Intro photo: {intro_photo if intro_photo else 'none'}\n"
        f"- Video: {video_path}\n"
        f"- On-screen hook (0-3s): {variant['hook_text'][cid]}\n\n"
        f"## Instagram Caption\n"
        f"{variant['ig_caption'][cid].format(keyword=keyword)}\n\n"
        f"## Facebook Caption\n"
        f"{variant['fb_caption'][cid].format(keyword=keyword)}\n\n"
        f"## Hashtags\n"
        f"{HASHTAGS}\n"
    )

    source_tag = _slugify(Path(source_name).stem)
    out = pack_dir / f"PACK_{source_tag}_{cid}_{clip['slug']}_{variant_key}.md"
    out.write_text(content, encoding="utf-8")
    return out


def _discover_sources(source: Path | None, source_glob: str | None) -> list[Path]:
    sources: list[Path] = []
    if source is not None:
        if not source.exists():
            raise FileNotFoundError(f"Source video not found: {source}")
        sources.append(source)
    if source_glob:
        for item in sorted(Path().glob(source_glob)):
            if item.is_file() and item.suffix.lower() in {".mp4", ".mov", ".m4v", ".avi"}:
                sources.append(item.resolve())
    # De-duplicate while preserving order
    unique: list[Path] = []
    seen: set[str] = set()
    for s in sources:
        key = str(s)
        if key not in seen:
            unique.append(s)
            seen.add(key)
    return unique


def run_pipeline(
    source: Path | None,
    source_glob: str | None,
    output_dir: Path,
    render: bool,
    packs: bool,
    photo_dir: Path | None,
    intro_seconds: float,
    short_video_mode: str,
) -> None:
    sources = _discover_sources(source, source_glob)
    if not sources:
        raise ValueError("No source videos found. Provide --source or --source-glob.")

    output_dir.mkdir(parents=True, exist_ok=True)
    pack_dir = output_dir / "post_packs"
    pack_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "sources": [str(s) for s in sources],
        "output_dir": str(output_dir),
        "clips": [],
    }

    photos = _discover_photos(photo_dir) if photo_dir else []
    manifest["photo_pool"] = [str(p) for p in photos]

    photo_idx = 0

    for source_item in sources:
        source_tag = _slugify(source_item.stem)
        duration = _ffprobe_duration_seconds(source_item)

        for clip_idx, clip in enumerate(CLIPS):
            resolved = _resolve_window(duration, clip["start"], clip["end"], short_video_mode, clip_idx)
            if resolved is None:
                print(
                    f"[skip] {source_item.name} clip {clip['id']} ({clip['end']}) exceeds video duration {duration:.2f}s"
                )
                continue
            render_start, render_end = resolved

            cid = clip["id"]
            for variant_key in ("CMT", "SHR"):
                out_name = f"REEL_{source_tag}_{cid}_{clip['slug']}_{variant_key}.mp4"
                out_file = output_dir / out_name

                intro_photo = None
                if photos:
                    intro_photo = photos[photo_idx % len(photos)]
                    photo_idx += 1

                if render:
                    cmd = _ffmpeg_cmd(
                        source_item,
                        out_file,
                        render_start,
                        render_end,
                        VARIANTS[variant_key]["hook_text"][cid],
                        intro_photo=intro_photo,
                        intro_seconds=intro_seconds,
                    )
                    print(f"[render] {out_name}")
                    proc = subprocess.run(cmd, capture_output=True, text=True)
                    if proc.returncode != 0:
                        msg = "\n".join(proc.stderr.splitlines()[-8:])
                        raise RuntimeError(f"ffmpeg failed for {out_name}\n{msg}")

                pack_path = None
                if packs:
                    pack_path = _write_pack(
                        pack_dir,
                        clip,
                        variant_key,
                        out_file,
                        source_item.name,
                        intro_photo,
                    )

                manifest["clips"].append(
                    {
                        "source": str(source_item),
                        "clip_id": cid,
                        "slug": clip["slug"],
                        "variant": variant_key,
                        "variant_label": VARIANTS[variant_key]["label"],
                        "video": str(out_file),
                        "pack": str(pack_path) if pack_path else None,
                        "intro_photo": str(intro_photo) if intro_photo else None,
                        "start": render_start,
                        "end": render_end,
                    }
                )

    manifest_path = output_dir / "reel_hook_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"[ok] wrote manifest: {manifest_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cut Pineapple reel variants + post packs.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Path to source testimonial video")
    parser.add_argument(
        "--source-glob",
        type=str,
        default=None,
        help="Optional glob for additional videos to test, e.g. '02_Media_Vault/**/REEL_*.mp4'",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT, help="Output directory")
    parser.add_argument(
        "--photo-dir",
        type=Path,
        default=DEFAULT_PHOTO_DIR,
        help="Optional directory of photos to overlay in first seconds",
    )
    parser.add_argument(
        "--intro-photo-seconds",
        type=float,
        default=1.2,
        help="How long intro photo overlay stays on-screen",
    )
    parser.add_argument(
        "--short-video-mode",
        choices=["adapt", "skip"],
        default="adapt",
        help="For short sources, adapt clip windows or skip them",
    )
    parser.add_argument("--packs-only", action="store_true", help="Write post packs/manifest without rendering video")
    parser.add_argument("--render-only", action="store_true", help="Render videos only (skip post packs)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.packs_only and args.render_only:
        raise ValueError("Use either --packs-only or --render-only, not both.")

    render = not args.packs_only
    packs = not args.render_only

    run_pipeline(
        source=args.source,
        source_glob=args.source_glob,
        output_dir=args.output_dir,
        render=render,
        packs=packs,
        photo_dir=args.photo_dir,
        intro_seconds=args.intro_photo_seconds,
        short_video_mode=args.short_video_mode,
    )


if __name__ == "__main__":
    main()
