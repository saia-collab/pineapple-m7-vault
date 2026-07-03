import os
import subprocess

# Define directory architecture
ROOT_DIR = r"C:\Pineapple-Mana-Global"
RAW_REELS_DIR = os.path.join(ROOT_DIR, r"02_Media_Vault\raw_reels")
OUTPUT_LP_DIR = os.path.join(ROOT_DIR, r"04_Tech_Lab\output\landing_pages")

# Ensure output destination exists
os.makedirs(OUTPUT_LP_DIR, exist_ok=True)

def process_video_pipeline():
    print("🎬 Starting Programmatic Video Slicing Engine...")

    if not os.path.exists(RAW_REELS_DIR):
        print(f"❌ Error: Raw reels directory not found at {RAW_REELS_DIR}")
        return

    for filename in os.listdir(RAW_REELS_DIR):
        if not filename.lower().endswith((".mp4", ".mov", ".avi")):
            continue

        input_path = os.path.join(RAW_REELS_DIR, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(OUTPUT_LP_DIR, f"{base_name}_loop_15s.mp4")

        print(f"⚡ Slicing and compressing: {filename}")

        # FFmpeg command: Cuts first 15 seconds, resizes to 1080x1920, strips audio (-an) for lightning-fast page speed
        cmd = [
            "ffmpeg",
            "-y",
            "-i",
            input_path,
            "-ss",
            "00:00:00",
            "-t",
            "00:00:15",
            "-vf",
            "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
            "-c:v",
            "libx264",
            "-crf",
            "28",
            "-an",
            output_path,
        ]

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✅ Successfully exported to output/landing_pages/")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to process video: {filename}. Ensure FFmpeg is installed in your system PATH.")

    print("🏁 Video pipeline execution complete.")


if __name__ == "__main__":
    process_video_pipeline()
