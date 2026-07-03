# Character Sheet — Cast Lock Procedure

## Required reading before using this file

Reading character-sheet.md in isolation produces drift. Read in this order, every time:

1. **This file** (character-sheet.md) — defines the file shape, frontmatter, sections, the 3-view turnaround prompt.
2. **[cinematic-grounding.md](cinematic-grounding.md)** — defines the language used in Reaction Faces (weight cue / micro-action / held beat). Required for the Reaction Faces table to read correctly.
3. **[grids.md](grids.md) §1x3-3view-turnaround** — the canonical character ref grid layout (FRONT + SIDE + DETAIL).
4. **Workflow mode from config.json** — determines whether Reaction Faces include signature features (text2video) or are pose+expression only (ref2video).

```bash
python -c "import json,os; print(json.load(open(os.path.expanduser('~/.claude/skills/shot-builder/workspace/config.json')))['defaults']['workflow_mode'])"
```

Do NOT skip steps 2-4. Multiple production sessions have shipped Reaction Faces written without reading cinematic-grounding.md — they were rewritten on the spot because the language was wrong.

---

How to lock a character into a `<TOKEN>.md` that survives across shots and projects.

**The single Prompt code block in every cast file is a 3-VIEW TURNAROUND GRID prompt.** Not a single-character description. When pasted into MJ / Flux / Nano-Banana / Runway / ComfyUI with the user's reference image attached, it produces a sheet with FRONT body view + SIDE body profile + tight DETAIL HEADSHOT in one image. That's the canonical character identity reference — generate it once per character, save the output, attach it to every later shot prompt.

**ONE code block per file.** This is non-negotiable. Obsidian's renderer has a known bug where multiple consecutive code blocks break ("after the second code block, all text can be treated as code"). Internal section labels (CHARACTER / ICONIC SIGNATURE / LAYOUT / LIGHTING / COSTUME / ANTI-PATTERNS / BACKGROUND / FINISH) give the prompt structure without breaking into multiple blocks.

## Two paths

| Path | When | Output |
|---|---|---|
| **A — From reference image** | User drops a face/body ref | Extract → mirror back → token .md with 3-view grid prompt |
| **B — From scratch** | User describes / develops new character | Casting questionnaire → mirror back → token .md with 3-view grid prompt |

## Path A — from reference image

1. **Extract by visual description only.** Never use the real person's name in the prompt body. Never invent details. Never use age numbers — describe by build.
2. **Mirror back the lock** in plain language. Wait for confirmation.
3. **Write the token file** using the template below.

Per-character checklist for extraction:

| Field | Capture |
|---|---|
| Build & posture | Frame, shoulder width, neck, gait, posture default |
| Face geometry | Face shape, jawline, brow ridge, nose, lip shape, ear size and angle |
| Hair | Color in full nuance, length, texture, parting, styling, signature haircut |
| Eyes | Color with descriptor, set depth, brow shape and density |
| Skin | Tone, finish, pores / lines / sun-creases, freckles or beauty marks if visible |
| Facial hair | None / stubble / styled scruff / full short beard / long beard, color, density |
| Eyewear | Frame shape, material, color, fit, lens detail |
| Mouth & expression default | What the face reads at rest |
| Wardrobe (head to toe) | Every garment with fabric, color, fit, structural details, layering, footwear |
| Body markers | Piercings, tattoos, nail polish, scars — only if visible |

## Path B — from scratch

Ask in one message, like a casting brief:

> Quick casting brief — tell me about this character:
> - Build & energy
> - Face & signature feature (the one thing that MUST read every shot)
> - Era & wardrobe register
> - Default expression
> - Role in the production
> - Reference images (optional)

Mirror back the lock, wait for confirmation, then write the token file.

## Token file template — exact shape

Save to `workspace/projects/<active>/cast/<TOKEN>.md` (project-scoped) or `workspace/cast/<TOKEN>.md` (global).

**The template is locked.** Every token file follows this exact structure. Sections are: H1 + blockquote identifier → ## Prompt — 3-view turnaround sheet (ONE code block) → ## Reaction faces (table, optional) → ## Variants (bullets) → ## Related (bullets).

The Prompt block is the 3-view turnaround grid prompt. It produces ONE image with three panels: LEFT full-body front, CENTER full-body side profile, RIGHT tight detail headshot. That image becomes the user's master reference for the character across every later shot.

````markdown
---
token: <TOKEN>
references:
  - "<real-person-name> face reference (likeness replication required)"
gotchas:
  - "<specific failure mode in one short sentence>"
  - "<another>"
  - "<3-5 total max>"
---

# `<TOKEN>` — <Short role description>

> <2-3 sentence identifier — signature feature, wardrobe register, scene context. ~30-60 words. Use a blockquote.>

## Prompt — 3-view turnaround sheet

```
Photorealistic character reference sheet for film production. Exactly 3 views of the SAME CHARACTER in a single image. No more, no less. This is the MASTER IDENTITY REFERENCE.

USE THE EXACT face from the attached <reference description>. LIKENESS REPLICATION, not inspiration. Replicate face shape, jawline, eye shape and color, brow shape, skin tone, <signature 1>, and <signature 2> precisely. Do NOT idealize, smooth, or symmetrize the face.

CHARACTER: <Full physical description in continuous prose, ~120-180 words. Face geometry, hair, eyes, nose, mouth, skin texture, stubble/facial hair, glasses if worn, build, posture default. Real human skin texture: visible pores, fine lines, sun-creases, real natural imperfections, no airbrushing.>

ICONIC SIGNATURE — NON-NEGOTIABLE: <The features that must read in every shot. End with a fail-test: "If <X>, <Y>, or <Z>, the character has failed.">

BASELINE EXPRESSION across all 3 views: <what the face reads at rest. One-two sentences.>

The same exact person must appear in all 3 views.

LAYOUT (STRICTLY 3 VIEWS ONLY):

LEFT — Full body FRONT view: standing straight facing camera, arms relaxed at sides, head to toe visible, neutral natural pose, <outerwear detail>, <signature features visible>.

CENTER — Full body SIDE PROFILE: facing left, clean silhouette showing the build, head to toe visible, natural relaxed stance, <signature features reading in profile>.

RIGHT — Tight close-up FRONTAL HEADSHOT: face filling this section of the frame, eyes looking directly at camera, <baseline expression>, <signature features visible>. Shot on 85mm lens. Hyper-detailed skin rendering: visible pores, <stubble or beard texture>, fine natural lines, real natural imperfections, subsurface scattering. Sharp focus on eyes with soft catchlights.

Do NOT generate extra views. Exactly 3 views.

LIGHTING: Even, flat studio lighting across all views. No dramatic shadows, no mood lighting. Soft key light from front-left on the close-up headshot.

COSTUME (identical across all 3 views, render fabric textures with photographic clarity — visible weave, stitching, material weight, creases, surface detail): <Full wardrobe list. Garment 1 with detail. Garment 2 with detail. Accessories. Eyewear if worn. Footwear.>

ANTI-PATTERNS — DO NOT render: <Comma-separated list of specific things to avoid.>

BACKGROUND: Simple flat neutral grey seamless. No gradients, no vignetting, no environmental elements.

FINISH: Photorealistic. No stylization. Raw natural photograph look. ARRI color science, subtle film grain, maximum resolution.

If the 3 views do not look like the same person, it has failed. The <signature 1> + <signature 2> + <signature 3> + <signature 4> combination is the signature.
```

## Reaction faces

**HARD CEILING: maximum 5 entries. STOP at 5. Do not exceed "to be thorough."** Six or more entries makes the model ignore the most important ones. If you've got more beats than fit in 5 rows, split into a variant token, don't pad this one.

**Content rules by workflow mode** (check `config.json` → `defaults.workflow_mode` before writing this table):

- **`ref2video`** — each entry is **pose + expression only**. The reference image carries hair color, eye color, build, costume. Do NOT repeat those in every row. Repeat only what the body / face is doing in this specific beat.
- **`text2video`** — each entry MUST include the signature features (hair, eyes, build, jaw shape) because the model has no reference image to anchor identity to. Without these in the text, identity drifts shot to shot.
- **`mixed`** — write the table in ref2video shape (pose + expression only). Add a `## Reaction faces — text2video variant` block below it with the same beats re-written with signature features included, if the production needs both modes.

**Block 3 grammar** (from cinematic-grounding.md — required reading): every entry must specify a **weight cue** (where mass settles), a **micro-action** (small involuntary motion), and a **held beat** (intent stillness). Three sentences max per entry.

| Beat | Token |
|---|---|
| <Beat 1> | <weight cue + micro-action + held beat — pose+expression in ref2video, +signature features in text2video> |
| <Beat 2> | <same shape> |
| <Beat 3> | <same shape> |
| <Beat 4> | <same shape> |
| <Beat 5> | <same shape — STOP HERE> |

## Variants

- `<TOKEN-VARIANT-1>` — <one-line override delta>
- `<TOKEN-VARIANT-2>` — <one-line override delta>

## Related

- `<STYLE-TOKEN>`
- `<LOCATION-TOKEN>`
- `<OTHER-CAST-TOKEN>`
````

## How the 3-view sheet is used downstream

The 3-view sheet is **the character's master reference image**. The workflow:

1. Lock the character → write the token .md
2. Run the Prompt block in MJ / Flux / Nano-Banana / Runway / ComfyUI with the user's reference image attached
3. Save the resulting 3-view sheet as `<TOKEN>-ref.png` (or `.jpg`)
4. For every later shot of this character, attach `<TOKEN>-ref.png` as the reference image and inline `<TOKEN>` in the shot prompt

This way you never re-describe the character — the locked 3-view image carries identity, the inlined `<TOKEN>` carries wardrobe + posture + baseline expression, and the shot prompt only adds what's specific to that beat (action, location, lighting mood, framing).

## Inlining tokens into shot prompts

When the user asks for a shot like *"shot of HERO walking down the hallway"*, the skill builds the shot prompt by:

1. Loading `<HERO>` token via `token_resolver.py`
2. Extracting the inline-token description from inside the Prompt block (the CHARACTER + COSTUME paragraphs read together as a paste-ready description)
3. Combining with the location token, style token, and shot-specific action/framing

The Prompt block serves **two purposes** with one code block:
- Standalone: generate the 3-view reference sheet
- Inlined: provide the character description for shot prompts (the CHARACTER + COSTUME sections re-read as inline content)

## Critical rules

1. **ONE code block per file.** Never two, never three. Internal labels give structure.

2. **The Prompt block is a 3-view turnaround grid prompt.** Not a single-character description. Output is FRONT + SIDE + DETAIL HEADSHOT in one image.

3. **No `---` in the body.** Only as frontmatter delimiters at the top. No horizontal rules.

4. **`##` headings only.** Section breaks come from headings, not horizontal rules.

5. **Frontmatter is 3 fields.** `token`, `references` (list), `gotchas` (list). Drop `type`, `project`, `created`, `modified`, `base_image` — the filename and folder location carry that info.

6. **No casting note paragraph, no canonical description blockquote, no signature features list outside the prompt, no anti-patterns list outside the prompt, no visual references list, no example shot block.** The single Prompt code block contains everything the model needs.

7. **Internal section labels inside the Prompt block** — CHARACTER / ICONIC SIGNATURE — NON-NEGOTIABLE / BASELINE EXPRESSION / LAYOUT / LIGHTING / COSTUME / ANTI-PATTERNS — DO NOT render / BACKGROUND / FINISH. These give the prompt structure without breaking into multiple blocks.

8. **Layout = LEFT (full body front) + CENTER (full body side profile) + RIGHT (tight detail headshot).** Two body shots + one detail. This is the locked turnaround format.

9. **Reaction-faces table only for characters with performance range.** Skip for still-face characters with controlled stillness.

10. **No example shot inside the cast file.** Example shots live in `start-frames/` or `shots/` — never in the cast token file.

## File length budget — ENFORCED CEILINGS

**STOP at the ceiling. Do not exceed "to be thorough." Over-elaboration causes the model to ignore the most important features.**

| Section | Lines (HARD CEILING) |
|---|---|
| Frontmatter | 6-12 |
| H1 + blockquote identifier | 3-5 |
| `## Prompt — 3-view turnaround sheet` + code block | 35-50 |
| `## Reaction faces` table | **5 entries max** (= ~7 lines incl. headers, or skip section entirely) |
| `## Variants` | 2-4 |
| `## Related` | 3-5 |
| **Total file** | **~60-80 lines — STOP** |

If you find yourself writing entry #6 in Reaction Faces or hitting line 90+, you're over-elaborating. Stop. Save the file. The user will tell you if it needs more.

## Anti-patterns the skill should never produce

- Multiple code blocks in one file (any number above 1)
- `---` horizontal rules in the body
- Casting note paragraph
- Canonical description blockquote outside the Prompt block
- Signature features numbered list outside the Prompt block (the ICONIC SIGNATURE line inside the Prompt is canonical)
- Anti-patterns bullet list outside the Prompt block
- Visual references section
- Single-character description prompt (not a grid) — the Prompt block MUST produce 3 views
- Example shot code block (lives in start-frames/, not in cast token)
- Frontmatter with more than 3 top-level fields
- `[[wikilink]]` syntax in frontmatter (non-portable across markdown editors)
- `created` / `modified` / `uid` in frontmatter (filesystem has this)

## Related

- [location-sheet.md](location-sheet.md) — same single-code-block philosophy for locations (2x2 empty plate output)
- [style-sheet.md](style-sheet.md) — same for LOOK tokens (measurable spec output)
- [grids.md](grids.md) — additional grid formats (3x3 contact sheet, 9-angle turnaround) for downstream usage
- [failure-modes.md](failure-modes.md) — symptom → cause → fix for character drift
- [photoreal-stack.md](photoreal-stack.md) — referenced inside scene/shot prompts, not the cast file (the 3-view sheet has its own photoreal language baked in)
