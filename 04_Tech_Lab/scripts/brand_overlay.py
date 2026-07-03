"""
Pineapple Roofing - Static Ad Brand Overlay Script
Adds yellow top banner + navy bottom banner + logo + ad text to all 6 static PNGs
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys

READY_TO_BLAST = r"c:\Pineapple-Mana-Global\02_Media_Vault\Pineapple-Media-HQ\2026_05_GENERAL_READY-TO-BLAST"
LOGO_PATH = r"c:\Pineapple-Mana-Global\02_Media_Vault\Pineapple-Media-HQ\2026_05_GENERAL_BUSINESS-ASSET\Hub\Artboard 4@3x.png"
OUTPUT_DIR = os.path.join(READY_TO_BLAST, "BRANDED_STATIC_ADS")

# Brand colours
YELLOW = (245, 166, 35)    # #F5A623
NAVY   = (26, 26, 46)      # #1A1A2E
WHITE  = (255, 255, 255)

TOP_H    = 110   # px – yellow top banner
BOTTOM_H = 90    # px – navy bottom banner

FONTS = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\impact.ttf",
    r"C:\Windows\Fonts\Arial.ttf",
]

def load_font(size):
    for path in FONTS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

def fit_text(draw, text, font, max_width):
    """Return a (font, actual_text) that fits within max_width; shrinks font if needed."""
    while True:
        bbox = draw.textbbox((0, 0), text, font=font)
        if (bbox[2] - bbox[0]) <= max_width or font.size <= 10:
            return font, text
        font = load_font(font.size - 1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load & pre-process logo once
logo_src = Image.open(LOGO_PATH).convert("RGBA")
logo_h_px = TOP_H - 16
logo_aspect = logo_src.width / logo_src.height
logo_w_px = int(logo_h_px * logo_aspect)
logo = logo_src.resize((logo_w_px, logo_h_px), Image.LANCZOS)

ad_files = sorted(f for f in os.listdir(READY_TO_BLAST) if f.lower().endswith(".png"))

for fname in ad_files:
    src_path = os.path.join(READY_TO_BLAST, fname)
    img = Image.open(src_path).convert("RGBA")
    W, H = img.size

    draw = ImageDraw.Draw(img)

    # ── Top yellow banner ────────────────────────────────────────────────────
    draw.rectangle([(0, 0), (W, TOP_H)], fill=YELLOW)

    # Logo – vertically centred in top banner, left-aligned with 12px padding
    logo_y = (TOP_H - logo_h_px) // 2
    img.paste(logo, (12, logo_y), logo)

    # Headline text in top banner – bold, navy, centred in remaining space
    headline = "HIDDEN ROOF DAMAGE?  COMPLIMENTARY AUDIT"
    font_h = load_font(30)
    left_edge = logo_w_px + 24
    avail_w = W - left_edge - 12
    font_h, headline = fit_text(draw, headline, font_h, avail_w)
    hb = draw.textbbox((0, 0), headline, font=font_h)
    tx = left_edge + (avail_w - (hb[2] - hb[0])) // 2
    ty = (TOP_H - (hb[3] - hb[1])) // 2
    draw.text((tx, ty), headline, fill=NAVY, font=font_h)

    # ── Bottom navy banner ───────────────────────────────────────────────────
    draw.rectangle([(0, H - BOTTOM_H), (W, H)], fill=NAVY)

    # "IKO CERTIFIED" – bold white, centred
    cert_text = "IKO CERTIFIED"
    font_c = load_font(36)
    cb = draw.textbbox((0, 0), cert_text, font=font_c)
    cx = (W - (cb[2] - cb[0])) // 2
    cy = H - BOTTOM_H + (BOTTOM_H - (cb[3] - cb[1])) // 2
    draw.text((cx, cy), cert_text, fill=WHITE, font=font_c)

    # ── Save ─────────────────────────────────────────────────────────────────
    out_name = f"BRANDED_{fname}"
    out_path = os.path.join(OUTPUT_DIR, out_name)
    img.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"  OK  {out_name}  ({W}x{H})")

print(f"\nDone - {len(ad_files)} images saved to:\n  {OUTPUT_DIR}")
