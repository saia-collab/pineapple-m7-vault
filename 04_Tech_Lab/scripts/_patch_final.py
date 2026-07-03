"""Final patch pass:
1. Add M7-FIREWALL-EXEMPT sentinel to CONTEXT.md governance files.
2. Fix AD-CREATIVE-STORM-CAMPAIGN.md legacy green palette.
3. Add M7-FIREWALL-EXEMPT sentinel to 04_Tech_Lab/main.js compiled bundle.
"""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

SENTINEL = "<!-- M7-FIREWALL-EXEMPT: governance-reference -->"
JS_SENTINEL = "// M7-FIREWALL-EXEMPT: green-detection-tooling\n"

total = 0

# 1. CONTEXT.md files - add sentinel
for p in pathlib.Path('.').rglob('CONTEXT.md'):
    text = p.read_text(encoding='utf-8', errors='replace')
    if 'M7-FIREWALL-EXEMPT' not in text:
        text = text.rstrip() + '\n\n' + SENTINEL + '\n'
        p.write_text(text, encoding='utf-8')
        total += 1
        print(f"SENTINEL: {p}")

# 2. main.js - add sentinel at top
main_js = pathlib.Path(r"04_Tech_Lab\main.js")
if main_js.exists():
    text = main_js.read_text(encoding='utf-8', errors='replace')
    if 'M7-FIREWALL-EXEMPT' not in text:
        text = JS_SENTINEL + text
        main_js.write_text(text, encoding='utf-8')
        total += 1
        print(f"SENTINEL: {main_js}")

# 3. AD-CREATIVE-STORM-CAMPAIGN.md - fix legacy green palette
campaign = pathlib.Path(r"Projects\Pineapple Marketing & Heritage HQ\AD-CREATIVE-STORM-CAMPAIGN.md")
if campaign.exists():
    text = campaign.read_text(encoding='utf-8', errors='replace')
    orig = text
    # Replace legacy green palette entries with brand colors
    subs = [
        ('Green #2D7D46 (trust, local authority, nature)', 'Royal Navy #1A365D (trust, authority, heritage)'),
        ('(green/yellow)', '(navy/gold)'),
        ('white text on green background', 'white text on Royal Navy background'),
        ('white text, dark shadow', 'white text on Royal Navy'),
        ('"Hidden Roof Damage? Find Out Free"', '"Hidden Roof Damage? Schedule Your Complimentary Professional Photo Audit"'),
    ]
    for old, new in subs:
        text = text.replace(old, new)
    # Regex for remaining green word uses
    text = re.sub(r'\bgreen\b', 'navy', text, flags=re.IGNORECASE)
    if text != orig:
        campaign.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        total += changed
        print(f"PATCHED ({changed}L): {campaign.name}")

print(f"\nTotal items processed: {total}")
