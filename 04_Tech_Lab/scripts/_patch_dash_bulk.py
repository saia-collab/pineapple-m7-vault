"""Patch remaining green violations in dashboard.md, pineapple_bulk HTML, and YouTube Atlas line."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

# 1. 04_Tech_Lab\dashboard.md - CSS with #6aff6a
dash_tech = pathlib.Path(r"04_Tech_Lab\dashboard.md")
if dash_tech.exists():
    text = dash_tech.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = text.replace('#6aff6a', '#00BFFF').replace('#6AFF6A', '#00BFFF')
    if text != orig:
        dash_tech.write_text(text, encoding='utf-8')
        print(f"PATCHED: {dash_tech}")

# 2. 01_Command_Center\dashboard.md - governance text; add sentinel
dash_cmd = pathlib.Path(r"01_Command_Center\dashboard.md")
if dash_cmd.exists():
    text = dash_cmd.read_text(encoding='utf-8', errors='replace')
    if 'M7-FIREWALL-EXEMPT' not in text:
        text = text.rstrip() + '\n\n<!-- M7-FIREWALL-EXEMPT: governance-reference -->\n'
        dash_cmd.write_text(text, encoding='utf-8')
        print(f"SENTINEL: {dash_cmd}")

# 3. pineapple_bulk_content_grid_30.html - replace pine-green CSS var and hex
bulk = None
for p in pathlib.Path('.').rglob('pineapple_bulk_content_grid_30.html'):
    bulk = p; break
if bulk:
    text = bulk.read_text(encoding='utf-8', errors='replace')
    orig = text
    subs = [
        ('--pine-green:', '--pine-navy:'),
        ('var(--pine-green)', 'var(--pine-navy)'),
        ('#3B6D11', '#1A365D'), ('#EAF3DE', '#001a33'),
    ]
    for old, new in subs:
        text = text.replace(old, new)
    # Any remaining green hex
    import re as _re
    HEX = _re.compile(r'#[0-9a-fA-F]{6}\b')
    approved = {"#1a365d","#001122","#001a33","#fbc02d","#ffd700","#e5a93c","#00bfff","#ffffff","#ffe12d","#000000"}
    def fix_hex(m):
        h = m.group(0); hl = h.lower()
        if hl in approved: return h
        try:
            r,g,b = int(hl[1:3],16), int(hl[3:5],16), int(hl[5:7],16)
        except: return h
        return '#00BFFF' if (g > 90 and g >= r+40 and g >= b+40) else h
    text = HEX.sub(fix_hex, text)
    text = _re.sub(r'\bgreen\b', 'navy', text, flags=_re.IGNORECASE)
    if text != orig:
        bulk.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        print(f"PATCHED ({changed}L): {bulk.name}")

# 4. YouTube Atlas line 985
yt = pathlib.Path(r"03_Knowledge_Mat\00_Atlas\2026-06-18_KB_2026-06-17_YouTube_Analysis_A_SOURCE.md")
if yt.exists():
    text = yt.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = text.replace('for Green Static Images/trust support', 'for Navy Static Images/trust support')
    if text != orig:
        yt.write_text(text, encoding='utf-8')
        print(f"PATCHED YouTube line 985")

print("Done.")
