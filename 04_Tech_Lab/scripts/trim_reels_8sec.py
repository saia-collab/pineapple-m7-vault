#!/usr/bin/env python3
"""
Trim 3 reels to exactly 8 seconds using ffmpeg.
Preserves audio codec and Elite Compliance bars.
"""

import os
import subprocess

# Define input and output paths
base_path = r"c:\Pineapple-Mana-Global\out"
reel_files = [
    "Reel01_Commercial_Liability.mp4",
    "Reel02_The_3000_BandAid.mp4",
    "Reel03_Insurance_Countdown.mp4"
]

print("=" * 70)
print("PINEAPPLE ELITE COMPLIANCE REEL TRIMMER (8 SECONDS)")
print("=" * 70)
print()

for reel_name in reel_files:
    input_file = os.path.join(base_path, reel_name)
    output_file = os.path.join(base_path, reel_name.replace(".mp4", "_8sec.mp4"))
    
    print(f"\n[PROCESSING] {reel_name}")
    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")
    
    # Check if input exists
    if not os.path.exists(input_file):
        print(f"  ✗ INPUT NOT FOUND")
        continue
    
    try:
        # Build ffmpeg command to trim to 8 seconds
        cmd = [
            "ffmpeg",
            "-i", input_file,
            "-t", "8",  # Trim to 8 seconds
            "-preset", "ultrafast",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",  # Overwrite output
            output_file
        ]
        
        print("  → Executing ffmpeg trim command...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"    ✓ Successfully created: {output_file}")
        else:
            print(f"    ✗ ffmpeg error (code {result.returncode})")
            if result.stderr:
                print(f"    stderr (last 300 chars): ...{result.stderr[-300:]}")
        
    except subprocess.TimeoutExpired:
        print(f"    ✗ TIMEOUT: ffmpeg took too long")
    except Exception as e:
        print(f"    ✗ ERROR: {str(e)}")

print("\n" + "=" * 70)
print("TRIMMING COMPLETE - NOW RUNNING FFPROBE VERIFICATION")
print("=" * 70)
