# Style Sheet — LOOK Token Procedure

How to lock a custom LOOK into a `<STYLE-TOKEN>.md` with measurable specs (hex values, IRE numbers, halation/grain amplitudes, contrast ratios) — not generic mood words.

A `<STYLE-TOKEN>` is **measurable**. Hex values, IRE numbers, contrast ratios, halation/grain amplitudes, white point in Kelvin. If it doesn't have measurements, it's a mood board, not a LOOK spec.

---

## When to lock a custom style

| Situation | Path |
|---|---|
| Canned cinema mode fits | Don't lock a style token. Use the mode directly from [camera-grammar.md](camera-grammar.md) |
| User wants a measurable signature LOOK across many shots | Lock a `<STYLE-TOKEN>` |
| User has a reference film/commercial they want to match precisely | Lock a `<STYLE-TOKEN>` with that as the primary reference |
| User wants to swap looks mid-production | Lock multiple `<STYLE-TOKENS>` and use the swap instructions |

---

## Two paths

| Path | When | Output |
|---|---|---|
| **A — From reference frame(s)** | User drops a still or names a film/DP | Measure → name → save token + LOOK spec code block |
| **B — From description** | User describes the mood in words | Translate to measurable specs → save token + LOOK spec code block |

---

## Path A — from reference

### 1. Measure or transcribe

If the user drops a still, extract:
- Dominant palette hex values (5-8 colors)
- Split-tone (warm-shadow / midtone / cool-highlight hexes)
- Saturation register (0-1 scale)
- Contrast ratio
- Skin luma IRE
- White point (Kelvin) + tint

If the user names a film/DP, transcribe known specs (e.g., "Joker 2019, Lawrence Sher, Kodak Vision3 250D, anamorphic, warm Bronx grade, controlled saturation").

### 2. Identify the lens character

Pick one lens family — the LOOK depends on it:
- Cooke S4/i / Hawk V-Lite / Atlas Orion — warm character lift
- Master Anamorphic / Sigma Cine — sterile clinical
- Panavision Ultra Vintage — vintage anamorphic with flare character
- Zeiss Super Speed — classic spherical character

### 3. Identify the film stock LUT

- Kodak Vision3 250D — warmer cinematic
- Kodak Vision3 500T — night/tungsten warmth
- Kodak Portra 400 — portrait warmth
- Fujifilm Eterna — muted naturalism
- Custom split-tone LUT — measurable hex spec

### 4. Mirror back as a LOOK note

Plain language summary. Wait for confirmation.

### 5. Write the token file

Use the template below.

---

## Path B — from description

### 1. LOOK questionnaire

> Quick LOOK brief — what does this look like:
> - **Reference films / commercials** — name 3-5 (Joker 2019, Uncut Gems, Apple AirPods, Beats by Dre, Doritos Super Bowl)
> - **Warm or cool, controlled or saturated** — pick a quadrant
> - **Day or night dominant** — and what's the key light
> - **Lens character** — vintage anamorphic, sterile clean, warm Cooke, period flare-heavy
> - **What this LOOK is NOT** — anti-patterns the user wants to avoid
> - **Palette anchors** — what colors live here, what's banned

### 2. Translate to measurable specs

Convert the mood description into hex values, IRE numbers, contrast ratios, halation amplitude. Don't leave anything as "warm" or "cinematic" — assign a number or hex.

### 3. Mirror back

Show the spec. Wait for confirmation.

### 4. Write the token file

---

## Token file template — mandatory shape

Save to `workspace/projects/<active>/styles/<STYLE-TOKEN>.md` (project-scoped) or `workspace/styles/<STYLE-TOKEN>.md` (global).

````markdown
---
token: <STYLE-TOKEN>
type: style
created: YYYY-MM-DD
modified: YYYY-MM-DD
project: <project-slug>
base_image: null
references:
  - "<reference film + DP, e.g. 'Joker 2019 (Lawrence Sher)'>"
  - "<reference commercial>"
default_palette:
  - "#HEX"
  - "#HEX"
  - "#HEX"
  - "#HEX"
  - "#HEX"
gotchas:
  - <specific failure mode + the fix language>
  - <another>
---

# <STYLE-TOKEN>

## What this look IS

- **<Adjective 1>** — [one-line explanation, like "Warm cinematic commercial — premium Apple / Beats / Doritos Super Bowl ad register"]
- **<Adjective 2>** — [one-line, like "Hard sun + edged shadows — Manhattanhenge brightness with deep shadow contrast"]
- **<Adjective 3>** — [one-line, like "Lively skin tones — healthy warm flush, real human skin, not pale or sickly"]
- **<Adjective 4>** — [one-line, like "Controlled saturation — colors PRESENT but ALL unified by warm grade"]
- **<Adjective 5>** — [the regional / period anchor]
- **<Adjective 6>** — [the aspect ratio + finish standard]

## What this look is NOT

- ❌ [Anti-pattern 1 — "Near-monochrome / desaturated / pale"]
- ❌ [Anti-pattern 2 — "Documentary / news photography"]
- ❌ [Anti-pattern 3 — "Cool / sea-teal / steel grey"]
- ❌ [Anti-pattern 4 — "Stock-photo oversaturation / neon punch"]
- ❌ [Anti-pattern 5 — "Video-game CGI / illustration"]

## Reference films + commercials

Name 5-15 specific references with DP credit where applicable.

- **<Film 1>** — <DP name> — <one-line of what to take>
- **<Film 2>** — <DP name> — <one-line>
- **<Commercial reference 1>** — <agency or brand> — <one-line>
- **<Commercial reference 2>** — <one-line>

---

## THE LOOK SPEC — paste verbatim into every prompt

```
LOOK: [Full measurable spec as one continuous paragraph, 150-300
words. Required elements in order:

1. Split-tone: warm-shadow #HEX, warm-highlight #HEX, midtone cast
   #HEX.

2. Project palette: 5-8 named hex colors with one-line descriptors
   ("warm brick rust #8C5239", "dirty cream concrete #BFB298",
   "controlled taxi yellow #C9A748 visible but unified to warm
   grade — never punchy school-bus yellow").

3. Saturation register: number on 0-1 scale ("CONTROLLED CINEMATIC
   SATURATION — subjects 0.55, lively skin tones, healthy warm
   flush, visible color"). State what it IS and what it does NOT do.

4. Allowed and banned color behaviors: "allow primary colors to
   read but ALL unified by warm grade. NO neon, NO oversaturation,
   NO commercial-stock-photo punch, NO pale desaturation, NO
   monochrome."

5. White point in Kelvin + tint offset: "White point 5200K (warmer
   than neutral), tint +0.015 (slight magenta warmth)."

6. Contrast ratio: "Contrast 8.5:1 (cinematic punch, not crushing)."

7. Histogram skew: "Bimodal histogram weighted toward warm midtones."

8. Camera body: "ARRI Alexa Mini LF" or "ARRI Alexa 35".

9. Lens placeholder: "[LENS PER SHOT — see lens table below]" — don't
   bake a specific focal length into the LOOK spec; let the shot
   prompt pull from the lens table.

10. Film stock LUT: "Kodak Vision 3 250D film stock LUT" or matching
    spec.

11. Halation: "subtle filmic halation in highlights on strong
    specular / fire / sun sources only (halation amplitude 0.4
    controlled, never overdone)."

12. Grain: "Grain amplitude 1.6 (organic film grain texture, not
    digital noise)."

13. Vignette: "Vignette 0.18 (subtle, not crushing)."

14. Atmospheric haze: "Atmospheric haze 0.22 with <regional> warmth."

15. Skin luma: "Skin luma 47 IRE, healthy warm red-dominant undertone
    (R:G 1.85:1, R:B 2.6:1), slight golden flush."

16. Aspect ratio: "2.39:1 anamorphic cinemascope letterbox crop."

17. Reference films inline: "Photoreal premium commercial
    cinematography — <Film 1>, <Film 2>, <Film 3>."

18. Negatives line: "NOT video-game CGI, NOT illustration, NOT
    documentary, NOT pale, NOT monochrome."

The whole spec reads as continuous prose, paste-ready into any
prompt's LOOK: field.]
```

## Lens table — pick per shot

| Shot type | Lens recommendation |
|---|---|
| Ultra-wide hero / street-level low-angle | <focal length + lens family> |
| Hyperwide ground-level looking up | <focal length + lens family> |
| Standard wide tracking / wide action | <focal length + lens family> |
| Normal / mid-shot eye-level | <focal length + lens family> |
| Medium close-up portrait | <focal length + lens family> |
| Tight portrait close-up | <focal length + lens family> |
| Macro extreme close-up | <focal length + lens family> |
| Long-lens compression | <focal length + lens family> |
| Aerial drone | <camera + rig> |
| Mounted (mirror, dashboard) | <focal length + lens family> |

[Lens-family rationale — one-line of why this family fits the LOOK.]

## Quick swap instructions

How to apply this LOOK to existing shot prompts:

1. In each existing prompt, find the `LOOK:` block at the bottom.
2. DELETE the entire old LOOK block.
3. PASTE the new LOOK spec (from "THE LOOK SPEC — paste verbatim" above).
4. Replace `[LENS PER SHOT]` with the appropriate lens from the table above.
5. The action description, camera position, subject, and references stay the same. ONLY the LOOK paragraph swaps.

## Variants

### `<STYLE-TOKEN-NIGHT>`
For night beats. Override deltas only:
- White point → <K>
- Halation → <amplitude>
- Skin IRE → <value>
- Palette → <hex shifts>

### `<STYLE-TOKEN-INTERIOR>`
For interior beats. Override deltas only.

## Anti-patterns

- **<Failure mode 1>** — [how to spot + how to recover with restate language]
- **<Failure mode 2>** — same pattern
- **<Failure mode 3>** — same
- **<Failure mode 4>** — same

## Related tokens

- `<CAST-TOKEN>` — [one-line — cast that runs under this LOOK]
- `<LOCATION-TOKEN>` — [one-line — locations that run under this LOOK]
- `<STYLE-TOKEN-VARIANT>` — [one-line — alternate beats]
````

---

## Critical rules

1. **The LOOK SPEC is one big copy-paste-ready code block.** Pasteable into the `LOOK:` field of any shot prompt verbatim. No fragments.

2. **Every spec is MEASURABLE.** Hex values, IRE numbers, contrast ratios, halation amplitude, grain amplitude, white point Kelvin. Generic "warm" or "cinematic" is forbidden.

3. **Lens stays as `[LENS PER SHOT]` placeholder.** Don't bake a focal length into the LOOK — the shot prompt pulls from the lens table per shot type.

4. **Reference films are named with DP credits.** "Joker (2019) Lawrence Sher" not "moody cinematic film". Specificity is the whole game.

5. **"What this look IS" and "What this look is NOT" are both required.** Anti-patterns are as important as positive patterns.

6. **Palette gets 5-8 named hexes with descriptors.** Not "warm brown" — `#8C5239 warm brick rust`.

7. **Skin IRE is mandatory.** Skin luma value (typically 40-55 IRE) + R:G + R:B ratios. Without this, skin drifts.

8. **Halation, grain, vignette, haze get explicit amplitudes.** Numbers, not adjectives.

9. **Negatives line ends every spec.** "NOT video-game CGI, NOT illustration, NOT documentary, NOT pale, NOT monochrome."

10. **Swap instructions are explicit.** Step-by-step. Users should never have to figure out how to apply the LOOK.

---

## Anti-patterns the skill should never produce

- Mood words instead of measurable specs ("warm", "moody", "cinematic")
- No "What this look IS / IS NOT" sections
- Missing lens table
- Halation / grain as adjectives instead of amplitudes
- Skin tone described in words instead of IRE
- Reference film with no DP credit
- Wikilink-style references or platform-specific frontmatter

---

## Related

- [character-sheet.md](character-sheet.md) — cast tokens that run under this LOOK
- [location-sheet.md](location-sheet.md) — locations that run under this LOOK
- [camera-grammar.md](camera-grammar.md) — canned cinema modes if a full LOOK spec isn't needed
- [photoreal-stack.md](photoreal-stack.md) — the universal photoreal block layered under custom LOOKs
- [failure-modes.md](failure-modes.md) — grade drift recovery
