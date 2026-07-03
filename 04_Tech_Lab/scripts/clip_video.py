import os
import subprocess
import sys

# 1. Map our rooms inside the 4-Room Fala Architecture
RAW_VIDEO_DIR = r"C:\Pineapple-Mana-Global\02_Media_Vault\raw_videos"
OUTPUT_DIR = r"C:\Pineapple-Mana-Global\04_Tech_Lab\output\clipped_reels"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------------------
# THE CONTROL PANEL (Change these numbers based on what NotebookLM tells you)
# ------------------------------------------------------------------------
VIDEO_FILE = "viral_input.mp4"  # Put the exact name of your video here

HOOK_START = "00:00:00"
HOOK_END = "00:00:03"  # Cut at 3 seconds

MEAT_START = "00:00:03"
MEAT_END = "00:00:45"  # Cut at 45 seconds

CTA_START = "00:00:45"
CTA_END = "00:00:58"  # Cut at 58 seconds
# ------------------------------------------------------------------------

input_path = os.path.join(RAW_VIDEO_DIR, VIDEO_FILE)

if not os.path.exists(input_path):
    print(f"Error: Cannot find '{VIDEO_FILE}' in 02_Media_Vault\\raw_videos\\")
    print("Please drop your video there and name it correctly.")
    sys.exit(1)

print("Pineapple Video Engine Active. Slicing raw media into Hormozi Lego pieces...")


def slice_video(start_time, end_time, output_name):
    output_path = os.path.join(OUTPUT_DIR, output_name)
    # Fast, lossless slicing using FFmpeg
    cmd = f'ffmpeg -y -i "{input_path}" -ss {start_time} -to {end_time} -c copy "{output_path}"'
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    print(f"Created: {output_name} [{start_time} --> {end_time}]")


# Execute the precision cuts
slice_video(HOOK_START, HOOK_END, "hormozi_1_hook.mp4")
slice_video(MEAT_START, MEAT_END, "hormozi_2_meat.mp4")
slice_video(CTA_START, CTA_END, "hormozi_3_cta.mp4")

print("Execution complete. Your viral Lego bricks are ready in 04_Tech_Lab/output/clipped_reels/")
