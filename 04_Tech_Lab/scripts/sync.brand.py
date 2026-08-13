#!/usr/bin/env python3
"""
PINEAPPLE CONTRACTORS & ROOFING - ALL-IN-ONE MASTER BRAND FACTORY (sync.brand.py)
Hardcodes and locks corporate guidelines, personal social branding data, and overlay safety boundaries.
Enforces an airtight, synchronized local context baseline across core files.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED_RELATIVE_TARGETS = {
    Path("CLAUDE.md"),
    Path("01_Command_Center/CLAUDE.md"),
    Path("01_Command_Center/design.md"),
    Path("memory/decisions.md"),
    Path("01_Command_Center/Brand_DNA/TATAFU_BRAND.md"),
    Path("03_Knowledge_Mat/00_MANA_MAP.md"),
}


def resolve_safe_target(relative_path: str) -> Path:
    rel = Path(relative_path)
    if rel not in ALLOWED_RELATIVE_TARGETS:
        raise ValueError(f"Refusing to write non-approved target: {relative_path}")

    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside workspace root: {target}") from exc

    return target


def force_lock_file(relative_path: str, content: str) -> None:
    try:
        target = resolve_safe_target(relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"SYNCHRONIZED AND SHIELDED: {target}")
    except Exception as exc:
        print(f"RECONCILIATION FAILURE ON {relative_path}: {exc}")


def main() -> None:
    print("Initializing Unified Corporate and Personal Moat Synchronization Matrix...")

    claude_template = """
# PINEAPPLE BUSINESS BRAIN (CLAUDE.md)

## SYSTEM IDENTITY & ROOT LEADERSHIP CONTEXT
- **Corporate Entity Name**: Pineapple Roofing & Restoration (Pineapple Contractors)
- **Account / Profile Owner**: Tatafu Nunumoveisini Moeakiola Veehala
- **Co-Owner & Senior Operations Manager**: Saia Moeakiola
- **The Core Story**: Family-owned and proudly operated by six Polynesian brothers protecting Frisco and North Texas families like family.
- **Geographic Base Coordinate**: Based natively in Frisco, Texas (Primary HQ address: 1 Cowboys Way, Suite 270W, Frisco, TX 75034). Active regional branch footprints out of Lewisville, TX and Austin, TX. Out-of-state parameters are unauthorized.
- **Moat Credentials**: RCAT Licensed (#03-0637), Certified Installer of IKO High-Performance Shingle Systems, GAF Certified, 5.0-Star regional rating with a 42 verified map review baseline.
- **Business Certification Layer**: Historically Underutilized Business (HUB #1861616404400) maintained for public-sector and credential-led trust positioning.

## MANDATORY COMPLIANCE FILTERS & GUARDRAIL CORES
- **Outbound Safety Gate (DEC-005)**: Every ad layout payload, social content grid, or technical configuration brief generated locally must enter a fully locked, strictly PAUSED state. Direct live execution or unchecked budget deployment is prohibited without manual human-in-the-loop sign-off.
- **Anti-Spam Rejection Law**: Ruthlessly block all low-tier discount terms like "FREE", "$0 Down", or aggressive insurance-chasing strings from consumer-facing copy. Substitute exclusively with elite tradesman terms: "Complimentary Professional Photo Audit" and "Full Restoration Coverage via insurance claim advocacy".
- **Minimum Target Revenue Parameter**: Only process leads and marketing materials optimized to secure premium storm restoration contracts maintaining a minimum project size of $18,000+ per file.

## VISUAL PALETTE SYSTEM
- **Master Structural Foundational Color**: Royal Navy Blue (#1A365D) - used for navigation bars, primary headings, text overlays, footers, and core text corporate marks.
- **Master Action CTA Highlight Color**: Pineapple Gold (#FBC02D) - used exclusively for CTA buttons, scroll-stopping graphic banners, and primary icon leaves highlights.
- **Visual Logo Assembly Standard**: Modern, geometric pineapple mark. Top leaves (crown) = Royal Navy Blue; Main fruit body = Pineapple Gold faceted grid pattern. Text is clean, bold, all-caps sans-serif.

## ACTIVE WORKSPACE ROOM ROUTING
- `01_Command_Center/` -> Strategic brand kit metrics, business profile metadata, playbooks, and local .env keys.
- `02_Media_Vault/` -> Uncompressed 39GB content pipeline bank (drone sweeps, job sites, and raw clips).
- `03_Knowledge_Mat/` -> Obsidian local wiki, hyper-local search questions (AEO), and Tongan proverb arrays.
- `04_Tech_Lab/` -> Executable script handlers, video-multiplier layout codes, and local CLI connectors.
"""

    tatafu_brand_template = """
# TATAFU PERSONAL BRAND OPERATING MAT (TATAFU_BRAND.md)

## SOCIAL MEDIA BRAND IDENTITY
- **Account Owner**: Tatafu Nunumoveisini Moeakiola Veehala
- **Core Focus**: Professional Services, Roofing, and Contracting Moats.
- **Role in the System**: Personal trust engine that captures community attention and routes qualified demand into premium restoration outcomes.

## VERIFIED 28-DAY PERFORMANCE PROFILE
- **Views**: 6,266 (+9%)
- **Engagement**: 772 (+27%)
- **Net Follows**: 8 (+500%)
- **Signal Summary**: Engagement momentum is outpulling view growth, which confirms trust depth is stronger than top-of-funnel reach velocity.

## AI PROMPT FRAMEWORK OBJECTIVES
- **Objective A - Capitalize on Engagement Momentum**: Prioritize deep-dive project walkthroughs, drone roof scans, and client testimonials to match current audience behavior.
- **Objective B - Follower Growth CTAs**: End each post with a high-converting follow CTA so the +500% audience acquisition trajectory keeps compounding.
- **Objective C - Facebook Stars Launch Plan**: Execute a 3-post introduction roadmap that activates fan gifting support while preserving premium positioning and Tongan family heritage values.

## CONTENT GOVERNANCE RULES
- **Anti-Slop Language Ban**: Permanently block the word "FREE" in consumer-facing copy. Use "Complimentary Professional Photo Audit" instead.
- **Visual Law Compliance**: All personal content that references branded layouts must honor the active standards in `01_Command_Center/design.md` including 180px top banner, 42px hook font, 860px wrap envelope, and 95px bottom credential bar.
- **Proverb Anchor**: Seal authority posts with: ** (The path of the journey is respect).
"""

    design_template = """
# PINEAPPLE GRAPHIC IDENTITY LAWS & DISPLAY STANDARDS

## SECTION 1: CORE BRAND COLOR PARAMETERS
- **Primary Structural Anchor**: Royal Navy Blue (`#1A365D`) - Structural typography authority, H1/H2 scannability.
- **Primary Action Accent**: Pineapple Gold (`#FBC02D`) - High-visibility CTA elements, scroll-stopping visual anchors.
- **Paragraph Neutral**: Charcoal / Slate Gray (`#333333`) - Soft paragraph body text copy readability.
- **Grid Background Spacing Neutral**: Crisp White (`#FFFFFF`) - Protects scannability and negative white space padding.

## SECTION 11: LOGO LAYOUT LAW & APPROVED FILE NAMING
- **Icon Structure**: Geometric pineapple mark. Crown leaves are Royal Navy Blue, fruit grid body is faceted Pineapple Gold.
- **Approved Naming API Conventions**:
  - `Pineapple_Logo_Navy_1x1.png`
  - `Pineapple_Icon_Master_9x16.png`
  - `Pineapple_Banner_Gold_1080x1920.png`

## SECTION 12: MOBILE CALIBRATED VERTICAL SHORT VIDEO SPECIFICATIONS
All short vertical reels processed natively via local computer hardware must map layouts strictly to these padding constants to ensure flawless mobile display:
- **Top Solid Hook Banner Height**: Set to exactly **180px** with a solid Pineapple Gold (`#FBC02D`) background.
- **Hook Title Typography**: Set to **42px font size** using centered bold Impact typography.
- **Horizontal Mobile Safe Wrapping Gate**: Constrained to a tight **860px max width** boundary (`fix_bounds=1`) with an auto-wrap character limit of 37 maximum spaces per line to eliminate screen-edge cropping.
- **Bottom Solid Credential Anchor Bar Height**: Set to exactly **95px** in solid Royal Navy Blue (`#1A365D`). Text displays centered yellow typography: `Pineapple Roofing | RCAT Licensed #03-0637 | 50-Year Product Edge`.
"""

    decisions_template = """
# LIVING RECONCILIATION LEDGER OF LOCKED CORPORATE DECISIONS

### DEC-001 through DEC-004: Workspace Folder Isolation and Directory Mapping
- **Status**: LOCKED / ARMED
- **Choice**: Configured the 4-room Fala directory layout to separate strategy files from technical scripts and raw media.

### DEC-005: Outbound Account Delivery Safety Guardrail
- **Status**: LOCKED / STRICT COMPLIANCE
- **Choice**: Enforced a strict PAUSED safety gate across all outbound scripts and marketing data submissions. Direct un-reviewed API publishing is permanently blocked to eliminate random timeline drift or accidental ad spend.

### DEC-013: Global Erasure of Hallucinated Project Contexts
- **Status**: ENFORCED / HARD GROUNDING
- **Choice**: Permanently scrubbed and banned all out-of-state template references regarding "West Palm Beach, Florida, Heritage Green, and Sila Naming Conventions". Anchored corporate operations entirely inside our real geography footprint: Frisco, Texas.

### DEC-019: Integration of Verified Personal Brand Analytics Dashboard
- **Status**: ACTIVE / HARDENED
- **Choice**: Embedded Tatafu Nunumoveisini Moeakiola Veehala's verified 28-day performance profile directly into our contextual memory loops: Views 6,266 (+9%), Engagement 772 (+27%), Net Follows 8 (+500%).
- **Strategic Direction**: Because engagement momentum is growing significantly faster than views, all content creation models must prioritize deep behind-the-scenes trade authority, raw project summaries, and client reviews rather than hollow awareness layouts.
- **Facebook Stars Blueprint**: Queue a native 3-post introduction sequence inside our content sheets to promote the activation of fan support and virtual gifts to turn high interactions into direct community rapport.
- **Cultural Proverb Anchor**: Seal major statements with our signature Tongan Proverb to project absolute brand authenticity: *""* (The path of the journey is respect).
"""

    mana_map_template = """
# PINEAPPLE OPERATING SYSTEM - MASTER MAP OF CONTENT (00_MANA_MAP.md)

This index file acts as the primary master thread for your Obsidian Second Brain. It maps out your entire operation so your local layout viewer is neatly structured.

## CORE WORKSPACE COMPLIANCE DIRECTORY
- [[01_Command_Center/CLAUDE.md|Root Constitution Brain]]
- [[01_Command_Center/business-profile.md|Business Coordinates Profile]]
- [[01_Command_Center/design.md|Locked Brand Design Laws]]
- [[01_Command_Center/Brand_DNA/TATAFU_BRAND.md|Tatafu Personal Brand Performance Ledger]]

## TONGAN HERITAGE & SOCIAL BLUEPRINTS
- [[03_Knowledge_Mat/10_Heritage/WARRIOR_GOVERNANCE.md|Personal Brand Constitution]]
- Mined Google AI Overview (AEO) Questions Ledger: `03_Knowledge_Mat/30_Scripts/hail_queries_2026.txt`
- May Production Copy Dashboard: `01_Command_Center/Playbooks/MAY_ORGANIC_BLITZ.md`

## FUNCTIONAL ENGINE CORE COMMANDS
- Programmatic Video-as-Code Compiler: `04_Tech_Lab/video-multiplier.py`
- Google GBP Reputation Shield: `04_Tech_Lab/review-appeal-janitor.ps1`
"""

    force_lock_file("CLAUDE.md", claude_template)
    force_lock_file("01_Command_Center/CLAUDE.md", claude_template)
    force_lock_file("01_Command_Center/design.md", design_template)
    force_lock_file("memory/decisions.md", decisions_template)
    force_lock_file("01_Command_Center/Brand_DNA/TATAFU_BRAND.md", tatafu_brand_template)
    force_lock_file("03_Knowledge_Mat/00_MANA_MAP.md", mana_map_template)

    print("\nSYSTEM HARDENING RECONCILIATION PASSED: Workspace synchronized with zero-slop context tracking rules.")


if __name__ == "__main__":
    main()
