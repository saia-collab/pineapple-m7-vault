import os
from PIL import Image, ImageOps, ImageDraw, ImageFont

# Define strict architecture paths
ROOT_DIR = r"C:\Pineapple-Mana-Global"
RAW_DIR = os.path.join(ROOT_DIR, r"02_Media_Vault\raw_photos")
OUTPUT_LSA = os.path.join(ROOT_DIR, r"04_Tech_Lab\output\lsa")
OUTPUT_GADS = os.path.join(ROOT_DIR, r"04_Tech_Lab\output\google_ads")
OUTPUT_LP = os.path.join(ROOT_DIR, r"04_Tech_Lab\output\landing_pages")

# Ensure output folders exist
for folder in [OUTPUT_LSA, OUTPUT_GADS, OUTPUT_LP, RAW_DIR]:
    os.makedirs(folder, exist_ok=True)


def process_creative_pipeline():
    print("Starting Programmatic Asset Engine Pipeline...")

    for filename in os.listdir(RAW_DIR):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue

        img_path = os.path.join(RAW_DIR, filename)
        with Image.open(img_path) as raw:
            # Ensure RGB for JPEG/WEBP output compatibility
            img = raw.convert("RGB") if raw.mode != "RGB" else raw.copy()

        base_name = os.path.splitext(filename)[0]

        # ─── 1. GOOGLE LSA PROTOCOL (Strict Raw 1:1 Smart Crop, No Text) ───
        print(f"  [LSA]  {filename}")
        lsa_img = ImageOps.fit(img, (1000, 1000), Image.Resampling.LANCZOS)
        lsa_img.save(os.path.join(OUTPUT_LSA, f"{base_name}_lsa.jpg"), "JPEG", quality=95)

        # ─── 2. GOOGLE ADS MATRIX (16:9 Banner, Royal Navy Border, RCAT License) ───
        print(f"  [GADS] {filename}")
        gads_img = ImageOps.fit(img, (1200, 628), Image.Resampling.LANCZOS)
        # Apply Royal Navy (#1A365D) framing border — 15px solid
        gads_img = ImageOps.expand(gads_img, border=15, fill="#1A365D")

        # Stamp RCAT License in lower-left corner
        draw = ImageDraw.Draw(gads_img)
        try:
            font = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", size=18)
        except OSError:
            font = ImageFont.load_default()
        draw.text((30, gads_img.height - 38), "RCAT License #03-0637", fill="#FFFFFF", font=font)
        gads_img.save(os.path.join(OUTPUT_GADS, f"{base_name}_gads_169.jpg"), "JPEG", quality=90)

        # ─── 3. HIGH-SPEED LANDING PAGE ASSETS (Ultra-Fast WebP Conversion) ───
        print(f"  [LP]   {filename}")
        lp_img = img.copy()
        lp_img.save(os.path.join(OUTPUT_LP, f"{base_name}_optimized.webp"), "WEBP", quality=75)

    print("Pipeline execution complete. Output folders successfully stocked.")


if __name__ == "__main__":
    process_creative_pipeline()
