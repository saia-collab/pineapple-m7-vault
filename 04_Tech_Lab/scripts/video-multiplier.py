"""
Pineapple Contractors - Zero-Cost Video Cut-Up Engine
Corporate Meta Ads Campaign | 9:16 Vertical Format
IKO Certified | Full Restoration Coverage | Complimentary Inspection
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ─── PATHS ────────────────────────────────────────────────────────────────────
BASE_DIR      = Path(r"C:\Pineapple-Mana-Global")
RAW_VIDEO_DIR = BASE_DIR / r"02_Media_Vault\Pineapple-Media-HQ\2026_05_GENERAL_INBOX\Raw_Mana_Capture\VIDEOS\REELS"
OUTPUT_DIR    = BASE_DIR / r"02_Media_Vault\2026_05_GENERAL_READY-TO-BLAST"
MATRIX_JSON   = BASE_DIR / r"03_Knowledge_Mat\hormozi-matrix.json"

# FFmpeg drawtext requires forward-slash font paths and no Windows drive colon issues.
# Use the escaped colon form: C\:/Windows/Fonts/...
FONT_IMPACT   = "C\\:/Windows/Fonts/impact.ttf"
FONT_ARIAL_BD = "C\\:/Windows/Fonts/arialbd.ttf"

# ─── FORMAT CONSTANTS ─────────────────────────────────────────────────────────
WIDTH         = 1080
HEIGHT        = 1920
HOOK_BAR_H    = 140
TRUST_BAR_H   = 95
HOOK_BG       = "0xFBC02D"   # Pineapple Gold (#FBC02D)
HOOK_FG       = "0x1A365D"   # Royal Navy (#1A365D)
TRUST_BG      = "0x1A365D"   # Royal Navy (#1A365D)
TRUST_FG      = "0xFBC02D"   # Pineapple Gold (#FBC02D)
TRUST_TEXT    = "Pineapple Contractors | IKO Certified | Full Restoration Coverage"
CLIP_SECONDS  = 15

# ─── COMPLIANCE GUARD ─────────────────────────────────────────────────────────
FORBIDDEN = ["GAF", "Free", "free", "$0", "zero dollars"]

def compliance_check(text: str) -> None:
    for word in FORBIDDEN:
        if word in text:
            raise ValueError(f"COMPLIANCE VIOLATION: '{word}' found in: {text!r}")


# ─── TEXT HELPERS ─────────────────────────────────────────────────────────────
def escape_dt(text: str) -> str:
    """Escape text for FFmpeg drawtext."""
    text = text.replace("\\", "\\\\")
    text = text.replace("'",  "\u2019")   # replace straight apostrophe with curly to avoid filter parse issues
    text = text.replace(":",  r"\:")
    text = text.replace("\u2014", "-")    # em-dash -> hyphen
    text = text.replace("%",  r"\%")
    return text


def wrap_hook(text: str, max_chars: int = 37) -> str:
    """Split hook onto multiple lines within 860px safety boundary at 42px Impact; return FFmpeg drawtext string."""
    if len(text) <= max_chars:
        return escape_dt(text)
    words = text.split()
    lines = []
    current = []
    for w in words:
        if current and len(" ".join(current + [w])) > max_chars:
            lines.append(" ".join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append(" ".join(current))
    return r"\n".join(escape_dt(ln) for ln in lines)


# ─── VIDEO DISCOVERY ──────────────────────────────────────────────────────────
def find_raw_videos(directory: Path) -> list:
    videos = []
    for ext in ("*.mp4", "*.mov", "*.m4v", "*.MP4", "*.MOV"):
        videos.extend(directory.rglob(ext))
    return sorted(videos)


# ─── FFMPEG BUILDER ───────────────────────────────────────────────────────────
def build_cmd(video_path: Path, output_path: Path, hook_text: str) -> list:
    compliance_check(hook_text)

    hook_dt  = wrap_hook(hook_text)
    trust_dt = escape_dt(TRUST_TEXT)
    trust_y  = HEIGHT - TRUST_BAR_H          # 1825

    mid_h = HEIGHT - HOOK_BAR_H - TRUST_BAR_H  # 1685

    # Linear vf chain — no semicolons needed (single input)
    vf = (
        # Scale to fill 1080 wide, crop to mid zone height
        f"scale={WIDTH}:{mid_h}:force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{mid_h},"
        # Pad to full 1920, video starts after hook bar
        f"pad={WIDTH}:{HEIGHT}:0:{HOOK_BAR_H}:color=black,"
        # Yellow hook banner
        f"drawbox=x=0:y=0:w={WIDTH}:h={HOOK_BAR_H}:color={HOOK_BG}:t=fill,"
        # Hook text — Impact, navy, centered
        f"drawtext=fontfile='{FONT_IMPACT}'"
        f":text='{hook_dt}'"
        f":fontcolor={HOOK_FG}"
        f":fontsize=42"
        f":x=max(110\\, min((w-text_w)/2\\, w-110))"
        f":y=({HOOK_BAR_H}-text_h)/2"
        f":line_spacing=8"
        f":fix_bounds=1,"
        # Navy trust banner
        f"drawbox=x=0:y={trust_y}:w={WIDTH}:h={TRUST_BAR_H}:color={TRUST_BG}:t=fill,"
        # Trust text — Arial Bold, yellow, centered
        f"drawtext=fontfile='{FONT_ARIAL_BD}'"
        f":text='{trust_dt}'"
        f":fontcolor={TRUST_FG}"
        f":fontsize=28"
        f":x=(w-text_w)/2"
        f":y={trust_y}+({TRUST_BAR_H}-text_h)/2"
    )

    return [
        "ffmpeg", "-y",
        "-ss", "0",
        "-i", str(video_path),
        "-t", str(CLIP_SECONDS),
        "-vf", vf,
        "-vcodec", "libx264",
        "-crf", "23",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-an",                      # muted — Meta ads default
        "-movflags", "+faststart",
        str(output_path),
    ]


# ─── MAIN ENGINE ──────────────────────────────────────────────────────────────
def run_engine():
    print("=" * 70)
    print("  PINEAPPLE CONTRACTORS — ZERO-COST VIDEO CUT-UP ENGINE (CULT MODE)")
    print("  IKO Certified | Full Restoration Coverage | Complimentary")
    print("=" * 70)

    hooks = [
        {"id": "CULT-001", "text": "THE $10,000 BAND-AID", "video_name": "8900 Ohio Commerical reel.mp4"},
        {"id": "CULT-002", "text": "REJECT DRIVEWAY ESTIMATES", "video_name": "4494 Hartebeest trail, Frisco.mp4"},
        {"id": "CULT-003", "text": "SHIELD YOUR FRISCO ASSET", "video_name": "4581 Hartebeest trail frisco.mp4"}
    ]
    print(f"\n  Loaded {len(hooks)} custom Cult Fandom hooks")

    raw_videos = find_raw_videos(RAW_VIDEO_DIR)
    if not raw_videos:
        print(f"\nERROR: No videos found under {RAW_VIDEO_DIR}")
        sys.exit(1)
    print(f"  Found {len(raw_videos)} raw video files in vault")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success, skipped, failed = [], [], []
    total = len(hooks)
    print(f"\n  Rendering {total} ad variations -> {OUTPUT_DIR}\n")
    print("-" * 70)

    for idx, hook in enumerate(hooks, start=1):
        hook_id   = hook["id"]
        hook_text = hook["text"]
        target_video_name = hook["video_name"]

        # Find the specific video by name
        video_path = None
        for v in raw_videos:
            if v.name == target_video_name:
                video_path = v
                break
        
        if not video_path:
            # Fallback to cycling if not found
            video_path = raw_videos[(idx - 1) % len(raw_videos)]

        output_path = OUTPUT_DIR / f"Ad_Variation_{hook_id}.mp4"

        # Compliance gate
        try:
            compliance_check(hook_text)
        except ValueError as e:
            print(f"  [{idx:02d}/{total}] BLOCKED  {hook_id} — {e}")
            skipped.append(hook_id)
            continue

        if not video_path.exists():
            print(f"  [{idx:02d}/{total}] SKIP     {hook_id} — missing: {video_path.name}")
            skipped.append(hook_id)
            continue

        cmd = build_cmd(video_path, output_path, hook_text)
        print(f"  [{idx:02d}/{total}] RENDER   {hook_id}: {hook_text[:52]}...")
        print(f"           src : {video_path.name}")

        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if proc.returncode == 0:
                mb = output_path.stat().st_size / 1_048_576
                print(f"           out : {output_path.name}  ({mb:.1f} MB)  OK")
                success.append(hook_id)
            else:
                print(f"           FAILED (exit {proc.returncode})")
                for line in proc.stderr.strip().splitlines()[-4:]:
                    print(f"             {line}")
                failed.append(hook_id)
        except subprocess.TimeoutExpired:
            print(f"           TIMEOUT — skipping")
            failed.append(hook_id)
        except Exception as e:
            print(f"           ERROR: {e}")
            failed.append(hook_id)
        print()

    print("=" * 70)
    print(f"  ENGINE COMPLETE")
    print(f"  [OK]  Success : {len(success)}")
    print(f"  [--]  Skipped : {len(skipped)}")
    print(f"  [!!]  Failed  : {len(failed)}")
    print(f"  Output dir : {OUTPUT_DIR}")
    print("=" * 70)
    if failed:
        print(f"\n  Failed IDs : {', '.join(failed)}")


if __name__ == "__main__":
    run_engine()
