# Location Sheet — Environment Lock Procedure

## Required reading before using this file

1. **This file** (location-sheet.md) — defines the file shape AND the 2x2 empty plate prompt.
2. **[photoreal-stack.md](photoreal-stack.md)** — closes every plate prompt. Required for plate generation.
3. **[grids.md](grids.md) §2x2-location** — the canonical layout (wide / low / high / detail).

The 2x2 empty plate prompt includes a `REFERENCE (NON-NEGOTIABLE)` block. **That block is load-bearing.** Without it, the model invents a generic version of the location instead of replicating the architectural source. Always include it when a reference image is attached.

**Plate-generation order (critical):**
- Generate the **day plate** (or whatever the dominant lighting is) FIRST.
- For a night / dusk / blue-hour variant of the SAME location, feed the day plate as a reference into the new prompt with language like: `same architecture as attached <LOCATION> reference, but at <new lighting state>`. This keeps building, columns, materials identical across lighting changes.
- **NEVER mix lighting states in one 2x2 plate** (day + night in same grid). The model picks one and ignores the other, or blends them into something incoherent. One light state per plate.

---

How to lock a location into a `<TOKEN>.md` that holds architecture, lighting defaults, palette, and atmospheric character across every shot in that space. The shape below is non-negotiable.

---

## Two paths

| Path | When | Output |
|---|---|---|
| **A — From reference image** | User drops an interior/exterior/plate | Extract → mirror back → token .md + **mandatory 2x2 empty plate** |
| **B — From scratch** | User describes the world from imagination or treatment | Questionnaire → mirror back → token .md + **mandatory 2x2 empty plate** |

The 2x2 empty location plate is **always** included — that's the pre-lit empty world the user pastes into any image model to lock geography before adding cast.

---

## Path A — from reference image

### 1. Extract by visual description only

Never use real brand names in the prompt body (describe generically). Never invent details not in the reference. Per-location checklist:

| Field | Capture |
|---|---|
| **Type** | Interior / exterior / hybrid |
| **Geography & era** | Real-world region anchor, period (modern / 1970s / period-future / dystopian) |
| **Architecture** | Building style, materials, scale, structural elements, ceiling height, signature features |
| **Materials** | Floors, walls, countertops, signage substrate, glass |
| **Set dressing** | Every visible object that shapes the world — vehicles, signage, debris, furniture, props, vegetation, vendors, equipment |
| **Brand signature** | Generic geometry + color only — never the brand name. Note where signage sits and what color it is |
| **Time of day default** | Golden hour / dusk / blue hour / dawn / overcast daylight / hard noon / night / interior anytime |
| **Lighting direction default** | Window position(s), practical fixtures, dominant light source, color temperature in Kelvin if measurable |
| **Atmospheric character** | Haze, dust, smoke, rain, snow, dry, humid — and density |
| **Color palette** | Dominant tones + accent colors + contrast structure. Hex values if measurable |
| **Crowd density default** | Empty / sparse / dense / commuter rush — at the locked time of day |
| **Continuity anchors** | Things that MUST appear in every shot of this location (specific shelf, signage, license card, neon strip) |

### 2. Mirror back the lock

Plain-language summary in conversation. Wait for confirmation.

### 3. Write the token file

Use the template below.

### 4. Generate the 2x2 empty plate

The 2x2 empty plate is the reference image for locking the world before cast goes in. It is not optional.

---

## Path B — from scratch

### 1. World questionnaire

> Quick world brief — tell me about this location:
> - **Type & geography** — interior / exterior / hybrid, and what city / region / era this is from
> - **Time of day default** — when does this location want to live
> - **Signature element** — the ONE thing that must read in every shot (specific neon strip / cast shadow direction / wet pavement / building geometry)
> - **Palette logic** — what colors live here, and what does NOT
> - **Crowd & dressing** — empty / sparse / dense, and what props anchor continuity
> - **Reference images** — optional, drop any architectural / lighting / commercial refs

### 2. Mirror back as a world note

Convert the answer into a flowing world note paragraph in director's voice (~80-150 words).

### 3. Wait for confirmation

Iterate until locked. Then write the token file + 2x2 empty plate.

---

## Token file template — mandatory shape

Save to `workspace/projects/<active>/locations/<TOKEN>.md` (project-scoped, default) or `workspace/locations/<TOKEN>.md` (global).

````markdown
---
token: <TOKEN>
type: location
created: YYYY-MM-DD
modified: YYYY-MM-DD
project: <project-slug>
base_image: null
references:
  - "<reference description>"
gotchas:
  - <specific failure mode + the fix language>
  - <another>
---

# <TOKEN>

## World note

[One LONG flowing paragraph in director's voice — ~150-250 words. Cover: the geographic anchor (real city / real region / era), the architecture in two sentences, the time-of-day choice and why, the palette logic and what's deliberately excluded, the signature element that has to read every shot, and the emotional role the location plays in the production.]

## Scenes that use this token

| Scene / shot ID | Beat | Notes |
|---|---|---|
| <Scene 01> | <Beat name> | <Anything specific to this scene's dressing> |
| <Scene 04.02> | <Beat name> | <Same> |

## Canonical description

> [ONE long continuous paragraph as a blockquote — ~150-250 words. Pure visual description, every world element in flowing prose. Architecture → materials → set dressing → light source → atmospheric character → palette → crowd density. Not bullets.]

## Reusable prompt token

```
<TOKEN> := [LONG copy-paste-ready paragraph, 100-250 words, ONE
continuous block. Include: geographic descriptor, time-of-day with
light direction, architectural detail (2-3 phrases), atmospheric
character (haze, dust, water sheen, neon glow), palette logic with
hex values or named colors, crowd density default, signature
continuity anchor, camera/lens character spec, explicit NEGATIVES
line ("no neon signage in daylight beats, no colored umbrellas, no
loud advertising, no incidental color"). Pasteable into any image
model as the location anchor in shot prompts.]
```

## Shot variants

Multiple shorter code blocks — one per scene that uses this location. Each variant references the main `<TOKEN>` and adds shot-specific framing.

**`<TOKEN-VARIANT-1>`** — Scene <N> <beat>:
```
<TOKEN>, [framing: wide establishing / medium tracking / low-angle
hero / locked static], [crowd state: dense rush-hour / sparse /
empty], [cast presence: <CAST-TOKEN> visible / off-frame / absent],
[shot-specific atmospheric note], [aspect]
```

**`<TOKEN-VARIANT-2>`** — Scene <N> <beat>:
```
<TOKEN>, [framing], [crowd state], [cast presence], [shot-specific
note], [aspect]
```

[Add as many variants as the production has beats in this location. Each variant is its own small code block — multiple small blocks here, not one big one.]

## 2x2 empty location plate — copy-ready

Reference image generator for the empty world, pre-lit so when cast enters later they hit the locked light correctly.

```
Generate a 2x2 grid of the SAME EMPTY <LOCATION> across 4 distinct
camera angles. EMPTY environment — no people, no hands, no
silhouettes, no characters of any kind. Location is pre-lit so that
when <CAST-TOKEN> later stands at <specific position> they hit
<specific light setup>.

[Time of day spec — exact language. Example: "Golden magic-hour
sunset transitioning to early blue-hour. Sun low ~8-15 degrees above
horizon, positioned <relative direction>."]

[Interior practical lighting spec — exact language. Which fixtures
are ON, what color, where they sit, how they relate to the hero
light.]

[Atmospheric character — dust, haze, particles, weather, density.]

[Sun/key light angle non-negotiable — explicit fail-test language.
Example: "SUN angle staged so the rim-light path behind the counter
(future cashier position) remains visibly unobstructed and hot with
raking sunset light in every panel."]

CAMERA ANGLES:
- TOP LEFT — Wide establishing front view: [eye-level, lens, aspect,
  framing — what fills the frame]
- TOP RIGHT — Low angle looking up: [floor-level tilt-up, lens, what's
  emphasized]
- BOTTOM LEFT — High angle looking down: [elevated tilt-down, what's
  emphasized]
- BOTTOM RIGHT — Macro detail close-up: [tight shot of one signature
  element with the locked light hitting it]

CINEMATIC LOOK:
[Camera body + lenses + filter + finish — exact spec.]

[Grade spec with hex values where the palette is intentional.]

OUTPUT:
- Grid layout: 2x2
- Aspect: each panel <aspect>
- Borders: clean thin white panel borders
- Labeling: NONE — zero text, zero captions, zero watermarks
- Resolution: highest available native, sharp focus, balanced exposure

CONSISTENCY RULES:
- Same <LOCATION> architecture across all 4 panels
- Same sun position and angle across all 4 panels (sun does not move
  between frames)
- Same practical lighting ON in all 4 panels at same intensity
- Same color grade, white balance, halation, saturation, lifted
  blacks across all 4 panels
- EMPTY environment — NO people on any panel
- <Signature element> visible in every panel where relevant
- Distinct visual variety between angles (wide reads fundamentally
  different from detail)

REFERENCE (NON-NEGOTIABLE):
The attached <LOCATION> reference image MUST be the architectural
source. Replicate <specific architectural elements>. Do NOT invent a
generic version. Do NOT redesign the signage / logo / signature
element. Location must be instantly recognizable.
```

## Signature elements (non-negotiable)

The elements that MUST read in every shot of this location. If any is missing, the location has failed.

1. **<Signature 1>** (the primary — if missing, location has failed)
2. **<Signature 2>**
3. **<Signature 3>**

## Anti-patterns

- **<Failure mode 1>** — [how to spot + how to recover with restate language]
- **<Failure mode 2>** — same pattern
- **<Failure mode 3>** — same

## Visual references

- **<Primary reference film / commercial>** — [one-line why]
- **<Secondary reference>** — [one-line]
- **<Real-world reference>** — [one-line]

## Related tokens

- `<CAST-TOKEN>` — [one-line — who lives in this location]
- `<STYLE-TOKEN>` — [one-line — what LOOK spec this location runs under]
- `<OTHER-LOCATION>` — [one-line — adjacent space if shots cut between]
````

---

## Critical rules

1. **The reusable prompt token is one copy-paste paragraph.** 100-250 words. Continuous prose. Pasteable as-is.

2. **Shot variants are multiple small code blocks** — one per scene/beat that uses the location. Each references the main token and adds shot-specific framing. Not one big code block.

3. **The 2x2 empty plate is one big code block.** Pre-lit for cast comp later. Always 4 angles (wide establishing / low angle / high angle / macro detail). Always with consistency rules + reference non-negotiable.

4. **Time of day + light direction is locked.** Single specification across all variants — sun doesn't move between cuts.

5. **Palette logic spelled out with hex values where measurable.** Generic "warm" isn't enough.

6. **Explicit negatives.** What does NOT appear at this location.

7. **Signature element gets repeated.** In summary, world note, canonical description, reusable token, every shot variant, the 2x2 plate, and the signature-elements list.

8. **Reference real films, real commercials, real DPs.** Generic "cinematic" produces generic output.

9. **Empty plate is empty.** No cast, no hands, no silhouettes. Says so explicitly in the prompt body.

10. **Continuity anchors are mandatory.** The specific shelf, signage, brand mark — these are the visual continuity glue that makes shots cut together.

---

## Anti-patterns the skill should never produce

- Thin canonical description
- Short reusable token
- No 2x2 empty plate code block
- No signature elements list
- Wikilink-style references or platform-specific frontmatter
- Real brand names inside prompt bodies

---

## Related

- [character-sheet.md](character-sheet.md) — cast tokens that live in these locations
- [style-sheet.md](style-sheet.md) — the LOOK spec each location runs under
- [grids.md](grids.md) — the 2x2 plate is a grid format, see for layout rules
- [failure-modes.md](failure-modes.md) — location drift fixes
