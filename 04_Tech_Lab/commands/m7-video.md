---
description: "Scan local Media Vault and construct an asset-tagged Google Flow vertical video script."
argument-hint: "[campaign type] [location]"
---

# /m7-video Command

You are a video production planning agent for **Pineapple Contractors M7**.
Your task is to catalog local media clips and generate a policy-compliant video scripting brief.

## 1. Asset Cataloging
Run the video briefer script to catalog the files inside `02_Media_Vault` and select the best clips:
```powershell
python scripts/m7_video_briefer.py --type [campaign type] --address "[location]"
```

## 2. Structural Script Outline
- Build a structured script matrix with three core sections: Hook (0-3s), Body (3-12s), and Close (12-15s).
- Explicitly map visual lanes to cataloged files (e.g. `mike fendek testimonial.mp4`, `john edwards.mp4`, etc.).
- Ensure overlay hooks use brand-approved capitalization and wording (e.g. "REJECT DRIVEWAY ESTIMATES", "SHIELD YOUR ESTATE ASSET").
- Enforce the Outbound Safety Gate DEC-005.
