#!/usr/bin/env python3
"""
PINEAPPLE CONTRACTORS - PERSONAL BRAND SYNC FACTORY (sync.personal.py)
Calibrates personal profile brand governance for Tatafu Veehala & Saia Moeakiola.
Bakes the 28-day Facebook performance profile directly into the local data layer.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
ALLOWED_RELATIVE_TARGETS = {
    Path("01_Command_Center/Brand_DNA/TATAFU_BRAND.md"),
    Path("03_Knowledge_Mat/10_Heritage/WARRIOR_GOVERNANCE.md"),
}


def resolve_safe_target(relative_path: str) -> Path:
    """Resolve a target path and block path traversal outside the workspace root."""
    rel = Path(relative_path)
    if rel not in ALLOWED_RELATIVE_TARGETS:
        raise ValueError(f"Refusing to write non-approved target: {relative_path}")

    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside workspace root: {target}") from exc
    return target


def write_file(relative_path: str, content: str) -> None:
    try:
        target = resolve_safe_target(relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"SYNCED: {target}")
    except Exception as exc:
        print(f"SYNC ERROR on {relative_path}: {exc}")


def main() -> None:
    print("Synchronizing Personal Brand Moat and Dashboard Ledgers...")

    warrior_content = """
# PINEAPPLE PERSONAL BRAND CONSTITUTION (WARRIOR.md)

## SYSTEM IDENTITY & INFLUENCE CORES
- **Profile Anchors**: Tatafu Nunumoveisini Moeakiola Veehala & Saia Moeakiola
- **Core Mission**: Leverage personal mindset, discipline, and entrepreneurial traction to build deep local relationships and route organic value to Pineapple Contractors.
- **Geographic Base**: Frisco, Texas (DFW Metroplex & Austin networks).
- **Cultural Mat (Fa'i Kaveikoula)**: Woven strands of the fala guiding all community engagement:
  1. *Faka'apa'apa* (Respect) - Honor the person before the position.
  2. *Tauhi Va* (Maintaining Relationships) - Protect and repair connection lines.
  3. *Loto To* (Humility) - Stay teachable; let actions carry your name.
  4. *Mamahi'i me'a* (Loyalty/Passion) - Unyielding commitment to family and craftsmanship.

## ACTIVE SOCIAL METRICS LEDGER (LATEST 28-DAY SYNC)
- **Views**: 6,266 (+9%)
- **Engagement**: 772 (+27%) - *Core Vector: Engagement outpulling view scale. Prioritize deep community value.*
- **Net Follows**: 8 (+500%)
- **Monetization Status**: Facebook Stars Available to set up.

## THE PERSONAL-TO-BUSINESS "BRIDGE" CADENCE
Content formatting maps strictly to the 3-day weekly programmatic rhythm:
- **Monday (The Mindset)**: Elite focus on execution, character strength, and resilience. This top-of-funnel angle drives mass algorithmic reach and impressions.
- **Wednesday (The Craft)**: Operational value proof. Behind-the-scenes roof surveys, aerial drone scans, and breaking down the IKO ArmourZone structural performance edge against Texas storms.
- **Friday (The Result)**: Completed project high-contrast showcases, transformation lookbooks, and verified regional customer reviews.
- **Stars Activation Rule**: Weave an implicit "Support the Village" CTA into Friday Reels to introduce the community gifting track natively without breaking premium positioning.

## CRITICAL SEPARATION AND LEADER COMPLIANCE LAWS
- **Platform Separation Mandate**: Personal content and mindset assets are restricted to personal platforms (e.g., @saiamoe handles) to keep corporate profiles focused strictly on local business trade authority.
- **Lead Generation Hook Enforcements**: Never post discount language like "FREE" or "$0 out of pocket". Personal profiles must position services as premium: "Complimentary Professional Photo Audit" and "Full Restoration Coverage available via insurance claim advocacy".
"""

    write_file("01_Command_Center/Brand_DNA/TATAFU_BRAND.md", warrior_content)
    write_file("03_Knowledge_Mat/10_Heritage/WARRIOR_GOVERNANCE.md", warrior_content)

    print("\nPERSONAL MOAT FACTORY DEPLOYED: System data sets are locked end-to-end.")


if __name__ == "__main__":
    main()
