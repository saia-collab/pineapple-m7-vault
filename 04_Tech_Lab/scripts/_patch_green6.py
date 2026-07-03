"""Sixth-pass: precise surgical replacements for 5 remaining green prose hits."""
import pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

patches = [
    (
        r"03_Knowledge_Mat\00_Atlas\templates\Banana_Squad_-_Image_Agent_Team\paperbanana.md",
        "Blue/Orange, Green/Purple, or Teal/Pink.",
        "Blue/Orange, Gold/Purple, or Teal/Pink.",
    ),
    (
        r"03_Knowledge_Mat\00_Atlas\templates\ClaudeClaw_-_Mega_Prompt_Visual_Guide\REBUILD_PROMPT.md",
        "Use color-coded output (ANSI): ✓ green, ⚠ yellow, ✗ red.",
        "Use color-coded output (ANSI): ✓ cyan, ⚠ yellow, ✗ red.",
    ),
    (
        r"03_Knowledge_Mat\00_Atlas\templates\ClaudeClaw_OS_Blueprint_Kit\POWER_PACKS.md",
        "importance as a colored bar (green > 0.7, yellow > 0.4, red below)",
        "importance as a colored bar (cyan > 0.7, yellow > 0.4, red below)",
    ),
    (
        r"03_Knowledge_Mat\00_Atlas\templates\ClaudeClaw_OS_Blueprint_Kit\POWER_PACKS.md",
        "online status (green/red dot)",
        "online status (cyan/red dot)",
    ),
    (
        r"03_Knowledge_Mat\00_Atlas\templates\ClaudeClaw_OS_Blueprint_Kit\REBUILD_PROMPT_V2.md",
        "Use color-coded output (ANSI): green for success, yellow for warnings, red for errors.",
        "Use color-coded output (ANSI): cyan for success, yellow for warnings, red for errors.",
    ),
]

total = 0
for rel, old, new in patches:
    p = pathlib.Path(rel)
    if not p.exists():
        print(f"MISSING: {rel}")
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    if old in text:
        text = text.replace(old, new)
        p.write_text(text, encoding='utf-8')
        total += 1
        print(f"PATCHED: {p.name[:70]}")
    else:
        print(f"NOT FOUND: {old[:60]}")

print(f"\nTotal patches applied: {total}")
