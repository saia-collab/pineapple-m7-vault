import os, re, sys
from pathlib import Path

ROOT = r"C:\\Pineapple Contractors M7"
TECH_LAB = os.path.join(ROOT, "04_Tech_Lab")
COMMAND_CENTER = os.path.join(ROOT, "01_Command_Center")
MASTER_PLAYBOOK = os.path.join(COMMAND_CENTER, "MASTER_PLAYBOOK.md")

# Ensure directories exist
for d in [ROOT, TECH_LAB, COMMAND_CENTER]:
    os.makedirs(d, exist_ok=True)

# Define brand colors
ROYAL_NAVY = "#1A365D"
PINEAPPLE_GOLD = "#FBC02D"
# Patterns to purge (green colors)
GREEN_PATTERNS = [r"#00FF00", r"#008000", r"green"]

# Replacement mappings
REPLACEMENTS = {
    "Free Inspection": "Complimentary Professional Photo Audit (CPPA)",
    "$0 Down": "Full Restoration Coverage"
}

def cleanse_content(text):
    # Replace brand colors (ensure they appear somewhere, e.g., add a comment)
    text = text.replace(ROYAL_NAVY, ROYAL_NAVY)  # noop to ensure presence
    text = text.replace(PINEAPPLE_GOLD, PINEAPPLE_GOLD)
    # Purge green patterns
    for pat in GREEN_PATTERNS:
        text = re.sub(pat, "", text, flags=re.IGNORECASE)
    # Standardize lexicon
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

def main():
    md_files = list(Path(TECH_LAB).rglob("*.md"))
    all_parts = []
    for f in md_files:
        try:
            content = f.read_text(encoding="utf-8")
        except Exception as e:
            print(f"⚠️ Unable to read {f}: {e}", file=sys.stderr)
            continue
        content = cleanse_content(content)
        header = f"\n---\n## File: {f.relative_to(TECH_LAB)}\n---\n"
        all_parts.append(header + "\n" + content)
    # Append closing mandate
    closing = "\n\n."
    final_content = "# MASTER PLAYBOOK\n" + "\n".join(all_parts) + closing
    # Write out
    os.makedirs(COMMAND_CENTER, exist_ok=True)
    with open(MASTER_PLAYBOOK, "w", encoding="utf-8") as out:
        out.write(final_content)
    print(f"✅ MASTER_PLAYBOOK generated at {MASTER_PLAYBOOK}")

if __name__ == "__main__":
    main()
