#!/usr/bin/env python3
"""
M7 Video Briefer — Google Flow asset-tagged video script generator.
Scans the local Media Vault and builds policy-compliant, structured marketing scripts.
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Path references
SCRIPT_DIR = Path(__file__).resolve().parent
# scripts/ lives at 04_Tech_Lab/scripts/, so the workspace root is TWO levels up
WORKSPACE_ROOT = SCRIPT_DIR.parent.parent
VAULT_DIR = WORKSPACE_ROOT / "02_Media_Vault"
# Outbox Calibration Shield (Master Constitution v2.0 §3): all automated outbound
# copy must land strictly as DRAFTs for manual review. Customer-facing video
# briefs are outbound copy, so they route to Outbox_Drafts, not scripts/output.
OUTBOX_DRAFTS_DIR = WORKSPACE_ROOT / "01_Command_Center" / "Outbox_Drafts"
LEGACY_OUTPUT_DIR = SCRIPT_DIR / "output"  # retained for non-customer artifacts only

VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".avi"}


def scan_media_vault(vault_path: Path) -> dict[str, list[str]]:
    """Scan the media vault and categorize available video files."""
    catalog = {
        "drone": [],
        "testimonial": [],
        "marketing_pool": [],
        "general": []
    }
    
    if not vault_path.exists():
        return catalog
        
    for p in vault_path.rglob("*"):
        if p.is_file() and p.suffix.lower() in VIDEO_EXTENSIONS:
            rel_name = p.name
            path_str = str(p.relative_to(vault_path))
            
            # Categorize based on path containing keyword
            path_lower = path_str.lower()
            if "01_drone_footage_raw" in path_lower:
                catalog["drone"].append(rel_name)
            elif "02_client_testimonials" in path_lower or "testimonial" in path_lower:
                catalog["testimonial"].append(rel_name)
            elif "03_marketing_reels_pool" in path_lower or "reels" in path_lower:
                catalog["marketing_pool"].append(rel_name)
            else:
                catalog["general"].append(rel_name)
                
    return catalog


def select_best_assets(catalog: dict[str, list[str]], campaign_type: str) -> dict[str, str]:
    """Select the most appropriate video file name based on campaign type."""
    assets = {
        "hook_broll": "Default_Hook_Visual.mp4",
        "body_broll": "Default_Body_Visual.mp4",
        "cta_broll": "Default_CTA_Visual.mp4",
    }
    
    # Simple selection helpers with fallback
    def get_fallback(cat_list, default):
        return cat_list[0] if cat_list else default

    drone_files = catalog["drone"]
    testi_files = catalog["testimonial"]
    reels_files = catalog["marketing_pool"]
    all_files = drone_files + testi_files + reels_files + catalog["general"]
    
    if campaign_type == "testimonial":
        assets["hook_broll"] = get_fallback(testi_files, "testimonial_default.mp4")
        assets["body_broll"] = get_fallback(drone_files, "drone_default.mp4")
        assets["cta_broll"] = get_fallback(reels_files, "reels_default.mp4")
    elif campaign_type == "roofing":
        # Find roof related drone footage
        roof_drones = [d for d in drone_files if "roof" in d.lower()]
        assets["hook_broll"] = get_fallback(roof_drones or drone_files, "drone_roof.mp4")
        
        # Try to find a roof visual in reels or general
        roof_reels = [r for r in reels_files if "roof" in r.lower()]
        assets["body_broll"] = get_fallback(roof_reels or reels_files, "reels_roof.mp4")
        
        assets["cta_broll"] = get_fallback(testi_files, "testimonial_close.mp4")
    else: # general / restoration
        assets["hook_broll"] = get_fallback(reels_files, "marketing_reels_hook.mp4")
        assets["body_broll"] = get_fallback(drone_files, "drone_property.mp4")
        assets["cta_broll"] = get_fallback(testi_files, "testimonial_restoration.mp4")
        
    # Final check: if we have any files scanned, map defaults to actual filenames
    if all_files:
        if assets["hook_broll"] not in all_files:
            assets["hook_broll"] = all_files[0]
        if assets["body_broll"] not in all_files:
            assets["body_broll"] = all_files[min(1, len(all_files)-1)]
        if assets["cta_broll"] not in all_files:
            assets["cta_broll"] = all_files[min(2, len(all_files)-1)]
            
    return assets


def generate_flow_script(campaign_type: str, location: str, assets: dict[str, str]) -> str:
    """Generate a policy-compliant Google Flow video script."""
    
    if campaign_type == "testimonial":
        title = "Pineapple Standard Customer Proof Reel"
        hook_overlay = "REJECT DRIVEWAY ESTIMATES"
        hook_vo = f"Before you let someone write a quick driveway estimate for your {location} home, listen to this..."
        
        body_overlay = "The Pineapple Standard"
        body_vo = "We build to a higher standard. Authority documentation, professional crews, and premium materials."
        
        cta_overlay = "Complimentary Professional Photo Audit"
        cta_vo = "Don't settle. Text us to book your Complimentary Professional Photo Audit. Family Owned, Operated & Minority Owned."
        
    elif campaign_type == "roofing":
        title = "Pineapple Contractors Premium Estate Restoration Brief"
        hook_overlay = "SHIELD YOUR ESTATE ASSET"
        hook_vo = f"Storms hit {location} hard, but hidden damage is often missed from the ground."
        
        body_overlay = "Full Restoration Coverage"
        body_vo = "Our RCAT Licensed team advocates for your full restoration coverage, backing qualifying installs with IKO shingles."
        
        cta_overlay = "Book Your CPPA Today"
        cta_vo = "Protect your family like family. Claim your Complimentary Professional Photo Audit today."
        
    else: # restoration
        title = "Pineapple Restorations Rapid Damage Control Brief"
        hook_overlay = "THE $10,000 BAND-AID"
        hook_vo = f"Water and fire damage don't wait. Temporary fixes cost thousands in the long run."
        
        body_overlay = "Emergency Mitigation Standard"
        body_vo = "Our rapid-response mitigation teams document the full scope of interior and structural damage immediately."
        
        cta_overlay = "Rapid-Response Audit"
        cta_vo = "Call the Pineapple Restorations emergency line. Your rapid-response mitigation and audit starts now."

    script = f"""# Google Flow Video Script: {title}
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Campaign Type: {campaign_type.upper()}
Target Market: {location}
Compliance: LOCKED - PENDING SIGN-OFF (DEC-005)

## 🎥 Core Asset Map
- **Hook B-Roll**: {assets['hook_broll']}
- **Body B-Roll**: {assets['body_broll']}
- **CTA Close B-Roll**: {assets['cta_broll']}

---

## ⚡ The Flow Script Grid

| Scene / Time | Visual B-Roll Asset | Text Overlay (9:16 Center) | Audio Voiceover (VO) |
| :--- | :--- | :--- | :--- |
| **01. Hook**<br>(0:00 - 0:03) | **Asset**: `{assets['hook_broll']}`<br>*Action*: Slow zoom on storm impact / transition. | **"{hook_overlay}"**<br>Font: Impact (Navy on Gold)<br>Size: 42px | "{hook_vo}" |
| **02. The Standard**<br>(0:03 - 0:12) | **Asset**: `{assets['body_broll']}`<br>*Action*: Professional crew roof installation close-up. | **"{body_overlay}"**<br>Font: Arial Bold (Gold on Navy)<br>Size: 28px | "{body_vo}" |
| **03. The Close**<br>(0:12 - 0:15) | **Asset**: `{assets['cta_broll']}`<br>*Action*: Satisfied client with corporate gold logo mark. | **"{cta_overlay}"**<br>Font: Impact (Navy on Gold)<br>Size: 42px | "{cta_vo}" |

---

## 🛠️ Production Notes
1. **Ratio**: 9:16 Vertical Video format.
2. **Safety Guidelines**: Keep all text overlays within the 860px horizontal safety margin.
3. **Monetization**: Integrate Meta Stars badge CTAs in the supporting video captions.
"""
    return script


def main():
    parser = argparse.ArgumentParser(description="M7 Video script generator")
    parser.add_argument("--type", type=str, choices=["roofing", "restoration", "testimonial"], default="roofing", help="Campaign category")
    parser.add_argument("--address", type=str, default="Frisco, TX", help="Target geo-location")
    parser.add_argument("--output", type=str, help="Output markdown file path")
    args = parser.parse_args()

    print(f"Scanning media vault directory: {VAULT_DIR}...")
    catalog = scan_media_vault(VAULT_DIR)
    
    total_assets = sum(len(v) for v in catalog.values())
    print(f"Cataloged {total_assets} video assets across media vault categories:")
    print(f"  - Drone raw files  : {len(catalog['drone'])}")
    print(f"  - Testimonials     : {len(catalog['testimonial'])}")
    print(f"  - Marketing reels  : {len(catalog['marketing_pool'])}")
    print(f"  - General files    : {len(catalog['general'])}")

    selected_assets = select_best_assets(catalog, args.type)
    
    script_content = generate_flow_script(args.type, args.address, selected_assets)
    
    if args.output:
        out_path = Path(args.output)
    else:
        # Constitution v2.0 §3: customer-facing copy -> Outbox_Drafts as DRAFT
        OUTBOX_DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = OUTBOX_DRAFTS_DIR / f"{stamp}_video_{args.type}_DRAFT.md"

    # Inject DRAFT header per Constitution v2.0 §3 schema
    draft_header = (
        "STATUS: DRAFT — DO NOT SEND\n"
        "INTENT: Generate policy-compliant Google Flow video brief for the "
        f"{args.type} campaign targeting {args.address}.\n"
        "TARGET_PERSONA: See Master Constitution §6 avatar routing.\n"
        "GUARDRAILS_PASSED: [ ] Compliance [ ] Skeptic [ ] Brand Manager\n"
        "OUTBOX_SHIELD: Locked — manual review required before any send/publish.\n"
        "---\n\n"
    )
    out_path.write_text(draft_header + script_content, encoding="utf-8")
    
    print("\n" + "=" * 60)
    print(f"VIDEO BRIEF GENERATION COMPLETE")
    print(f"=" * 60)
    print(f"Target Campaign : {args.type.upper()}")
    print(f"Script Brief    : {out_path.name}")
    print(f"Saved to        : {out_path}")
    print("=" * 60)
    print("\nPreview of script:")
    print(script_content[:400] + "...\n[Full script output saved to file]")


if __name__ == "__main__":
    main()
