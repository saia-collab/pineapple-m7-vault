import os

# Define the absolute workspace updates based on Protocol DEC-006
workspace_updates = {
    "01_Command_Center/design.md": """# Section 1: Brand Color Law (Strict Enforcement)
- Pineapple Gold / Yellow (#FBC02D): High-visibility visual anchors, CTA buttons, special banners, and logo highlights. Do not use for body text.
- Royal Navy Blue (#1A365D): Primary structural anchor color. Enforced for typography, navigation, footers, website headers (H1, H2), and core text logo assets.
- Readability Neutrals: Charcoal/Slate Gray (#333333) for body copy text; Crisp White (#FFFFFF) for negative spacing.
- Material Shingle Alignment: Visual layouts must map color balances to match premium IKO Dynasty/Cambridge shingle profiles (Charcoal, Dual Black, Harvard Slate) to establish a premium trade contrast.

# Section 11: Logo Asset & Naming Law
- Iconography Blueprint: Modern, geometric pineapple icon. The top crown leaves are rendered in Royal Navy Blue (#1A365D), and the main body features the Pineapple Gold (#FBC02D) grid format.
- Typography Law: Bold, clean, all-caps sans-serif font spelling out PINEAPPLE ROOFING or PINEAPPLE CONTRACTORS in Royal Navy Blue.
- Approved AI Context File Naming Patterns:
  - `Pineapple_Logo_Gold_9x16.png`
  - `Pineapple_Logo_Navy_1x1.png`
  - `Pineapple_Icon_Asset_Master.png`

# Section 12: Branded Static Image Protocol
- Vault Directory: All high-contrast assets reside under `02_Media_Vault/2026_05_GENERAL_BUSINESS-ASSET/`
- Text Overlays: Hook banners are constrained to a 140px high-contrast Pineapple Gold block containing deep Royal Navy Blue Impact typography.""",

    "01_Command_Center/CLAUDE.md": """PINEAPPLE BUSINESS BRAIN (CLAUDE.md)

WHO WE ARE
- Identity: Pineapple Roofing & Restoration (Pineapple Contractors)
- Leadership: J. Dunn (Owner / Principal)
- Structure: Family-owned, certified minority-owned (MBE credentials enabled for bids), locally operated
- Authority Specs: RCAT Licensed (#03-0637), GAF Certified, 100+ five-star regional reviews, premium IKO 50-year product warranty partnership""",

    "memory/decisions.md": """### DEC-013: Rescission of Generic Color and Naming Hallucinations
- Status: LOCKED / ENFORCED
- Choice: Completely revoked unapproved "Heritage Green" metrics and "Sila" nomenclature. Re-anchored the system entirely to the strict #1A365D Royal Navy and #FBC02D Pineapple Gold color laws.

### DEC-014: Visual Asset Synchronization Gate
- Status: LOCKED / ENFORCED
- Choice: The folder path `02_Media_Vault/2026_05_GENERAL_BUSINESS-ASSET/` is restricted to hosting official high-fidelity corporate brand files. No temporary stock mockups or off-brand color files are permitted to pass through the rclone automation pipeline."""
}

print("Initializing Pineapple Workspace Refinement Pipeline...")

for filepath, content in workspace_updates.items():
    # Automatically handle folder structures if missing
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder layer: {folder}")

    # Write the clean compliance data
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Successfully synchronized and locked: {filepath}")

print("Execution Complete. Protocol DEC-006 is fully active across all room layers.")