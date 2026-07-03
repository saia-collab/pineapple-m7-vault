# Grids — All Multi-Panel Formats

How to compose every grid format the skill supports. One prompt → one image → N panels. Never deliver N separate prompts.

---

## FORMAT INDEX

| Format | Panels | Aspect (output) | Use case |
|---|---|---|---|
| 1x1 — single | 1 | 16:9 / 4:5 / 2.39:1 / 1:1 | Base reference, scene plate, isolated detail |
| 1x1 — character base | 1 | 4:5 or 9:16 | White-seamless character lock |
| 2x2 — location plate | 4 | 2.39:1 per panel | Empty location, pre-lit, 4 angles |
| 1x3 — 3-view turnaround | 3 | 16:9 master | **Character identity reference** — FRONT body + SIDE body + DETAIL headshot. THE canonical character ref. |
| 3x2 — 6-panel character sheet | 6 | 16:9 master | Multi-angle character + outfit (extended detail) |
| 3x3 — contact sheet | 9 | 16:9 master | Beat coverage, cast + location locked, 9 angles |
| 3x3 — 9-angle turnaround | 9 | 16:9 master | Character consistency from single face shot |
| 1x4 — horizontal location | 4 | 2.39:1 per panel | Wide-format location reference |
| Video single shot | 1 | 16:9 / 2.39:1 / 9:16 | Cinematic beat 5-15s |
| Video multi-shot sequence | N | 16:9 / 2.39:1 / 9:16 | Stitched beats with hard cuts |

---

## §1x1-character-base — CHARACTER BASE REFERENCE

The first image generated for any new character. Pure white seamless studio, full styling readable, locked as the canonical reference.

**Prompt structure:**

```
[<CAST_TOKEN> prompt block inlined here — identity + default wardrobe +
default expression].

Pure white seamless studio background, no shadow falloff to grey, no visible
seam line, perfectly even backdrop. Soft three-point classical lighting — key
from camera-left at 45 degrees, gentle fill from camera-right, subtle rim
light defining the shoulder and hair separation. Subject centered, weight on
one hip, body angled 15 degrees from camera, chin level, eyes to camera, neutral
controlled expression. Full body framing from head to just below the footwear.

[Photoreal stack v3 here]
```

**Variation strategy** (multiple base shots for the same character — same backdrop, vary one param):
- Pose: cocked-hip front → angled three-quarter → seated → side profile → back-to-camera over-shoulder
- Framing: full body → waist-up → head-to-shoulders
- Expression: neutral → smirk → eyes-closed → looking off-frame
- Lighting direction: key from L → R → top → backlit

Don't vary face, skin, or core identity markers. Those stay locked.

---

## §1x1-scene-plate — CINEMATIC SCENE PLATE

A single still that captures the world (and cast, when present) and the camera grammar — as if a cinematographer locked off and grabbed a photo on the same camera package mid-take.

**Prompt structure:**

```
[A single cinematic photograph descriptor — register the still aspires to.
E.g., "A cinematic anamorphic still photograph, the kind of frame a director
of photography would grab on set between takes."]

[If cast present: <CAST_TOKEN(s)> inlined — every character described].

[<LOCATION_TOKEN> inlined OR full environment description — location,
architecture, materials, time of day, weather, lighting direction and color
temperature, set dressing, props, atmospheric conditions, palette].

[<STYLE_TOKEN> inlined OR camera grammar block from M1-M5].

[Framing — wide / medium / tight / extreme close-up]. [Depth of field
and focus plane].

[Photoreal stack v3 OR v3-ENV based on cast presence]
```

---

## §2x2-location — EMPTY LOCATION PLATE (4 ANGLES)

For locking a location's geometry and lighting BEFORE talent is composited in. Empty environment, pre-lit so future cast drops in with consistent rim/key.

**Output:** 2x2 grid, 4 distinct camera angles, each panel cinematic 2.39:1.

**Canonical panel layout:**

| Position | Angle | Lens | Purpose |
|---|---|---|---|
| **TL_WIDE** | Eye-level establishing front | 35mm anamorphic | Full architecture readable |
| **TR_LOW** | Low angle looking up at storefront/fascia/ceiling | 24mm anamorphic | Reveals signage, neon, ceiling geometry |
| **BL_HIGH** | High angle down over counter/key surface | 35mm anamorphic | Spatial footprint, counter/floor relationship |
| **BR_DETAIL** | Macro close-up of signature element | 100mm anamorphic | Material + light quality at micro scale |

**Prompt structure (JSON-friendly for nano-banana / Flux / GPT-Image):**

````
Cinematic 2x2 grid of [<LOCATION_TOKEN>] across 4 distinct camera angles.
EMPTY environment — no people, no hands, no silhouettes, no characters of
any kind. Location is pre-lit so that when [<CAST_TOKEN(s)>] later stands at
[anchor position], the [light source] hits them as [rim / key / fill].

[<LOCATION_TOKEN> canonical description inlined — architecture, materials,
set dressing, signage, default lighting direction, atmospheric character.]

PANEL TL (top-left) — TL_WIDE: Eye-level, 35mm anamorphic, 2.39:1 framing.
Wide establishing front view showing full interior architecture. [Specific
elements visible — counter, back-bar, storefront, signage, neon strip, etc.]

PANEL TR (top-right) — TR_LOW: Low angle, 24mm anamorphic, 2.39:1. Camera
near floor tilted up. [What's visible from below — ceiling, soffit, fascia,
upper merch, hot sun window]. Horizontal anamorphic lens flare on backlit
windows.

PANEL BL (bottom-left) — BL_HIGH: High angle, 35mm anamorphic, 2.39:1.
Elevated above counter, tilted down. [What's visible from above — counter
surface, till position, coffee equipment, shadow patterns on floor].

PANEL BR (bottom-right) — BR_DETAIL: Macro, 100mm anamorphic, 2.39:1. Tight
shot of [signature element catching backlight — counter edge, chrome detail,
branded prop, signage edge, fabric texture]. Shallow DOF, creamy anamorphic
oval bokeh on out-of-focus background.

CONSISTENCY (all 4 panels): same exact [<LOCATION_TOKEN>] architecture, same
exact sun/light direction, same exact practicals ON, same exact color grade
and white balance, same exact atmospheric character. Empty environment in
every panel. Distinct visual variety between angles (WIDE reads fundamentally
different from DETAIL).

[<STYLE_TOKEN> OR M5 Atmospheric camera block]

OUTPUT: ONE image, 2x2 grid, 4 panels, clean thin white panel borders ~20px,
NO text NO labels NO captions NO watermarks NO signatures anywhere.

[Photoreal stack v3-ENV here]
````

**Gotchas baked into the prompt:**
- Sun direction drift between panels → "sun in same position across all 4 panels"
- Signature lighting (neon, practicals) vanishing → "[neon strip / practicals] ON across all 4 panels at same intensity"
- People hallucinating → "EMPTY, no people, no hands, no silhouettes on any panel"
- Panel grade drift → "identical color grade and white balance across all 4 panels"

---

## §1x3-3view-turnaround — 3-VIEW CHARACTER TURNAROUND (canonical character ref)

**THE primary character identity reference.** Every cast `<TOKEN>` file ships this as its Prompt block. Run once per character with the user's face reference attached → produces a sheet with FRONT body view + SIDE body profile + tight DETAIL HEADSHOT in one image. Save the result as `<TOKEN>-ref.png` and attach to every later shot of that character.

**Canonical panel layout (left to right, single row):**

| Position | Shot | What it captures |
|---|---|---|
| LEFT | Full body FRONT | Standing straight facing camera, neutral pose, full outfit head-to-toe, signature features in silhouette |
| CENTER | Full body SIDE PROFILE | Facing left, clean silhouette showing build + posture, full outfit from angle, signature features in profile |
| RIGHT | Tight FRONTAL HEADSHOT | Face filling frame, 85mm lens, hyper-detailed skin (pores, stubble texture, micro-lines, sharp eye focus with catchlights) |

**Why this is the canonical character ref (not the 6-panel):**
- Three panels are easier for models to compose with consistent identity than six
- One body + one profile + one face = covers the three identity-critical reads
- Output works as character-ref image in MJ char-ref / Runway / Kling / Nano-Banana reference-image input
- Smaller files, faster iteration, cheaper renders

**Prompt structure:**

```
Photorealistic character reference sheet for film production. Exactly 3 views of the SAME CHARACTER in a single image. No more, no less. This is the MASTER IDENTITY REFERENCE.

USE THE EXACT face from the attached <reference description>. LIKENESS REPLICATION, not inspiration. Replicate face shape, jawline, eye shape and color, brow shape, skin tone, [signature 1], and [signature 2] precisely. Do NOT idealize, smooth, or symmetrize the face.

CHARACTER: [Full physical description in continuous prose, ~120-180 words. Face geometry, hair, eyes, nose, mouth, skin texture, stubble/facial hair, glasses if worn, build, posture default. Real human skin texture: visible pores, fine lines, sun-creases, real natural imperfections, no airbrushing.]

ICONIC SIGNATURE — NON-NEGOTIABLE: [the features that must read in every shot. End with a fail-test: "If [X], [Y], or [Z], the character has failed."]

BASELINE EXPRESSION across all 3 views: [what the face reads at rest]

The same exact person must appear in all 3 views.

LAYOUT (STRICTLY 3 VIEWS ONLY):

LEFT — Full body FRONT view: standing straight facing camera, arms relaxed at sides, head to toe visible, neutral natural pose, [outerwear detail], [signature features visible].

CENTER — Full body SIDE PROFILE: facing left, clean silhouette showing the build, head to toe visible, natural relaxed stance, [signature features reading in profile].

RIGHT — Tight close-up FRONTAL HEADSHOT: face filling this section of the frame, eyes looking directly at camera, [baseline expression], [signature features visible]. Shot on 85mm lens. Hyper-detailed skin rendering: visible pores, [stubble or beard texture], fine natural lines, real natural imperfections, subsurface scattering. Sharp focus on eyes with soft catchlights.

Do NOT generate extra views. Exactly 3 views.

LIGHTING: Even, flat studio lighting across all views. No dramatic shadows, no mood lighting. Soft key light from front-left on the close-up headshot.

COSTUME (identical across all 3 views, render fabric textures with photographic clarity — visible weave, stitching, material weight, creases, surface detail): [Full wardrobe list with detail per garment.]

ANTI-PATTERNS — DO NOT render: [comma-separated list of specific things to avoid for this character.]

BACKGROUND: Simple flat neutral grey seamless. No gradients, no vignetting, no environmental elements.

FINISH: Photorealistic. No stylization. Raw natural photograph look. ARRI color science, subtle film grain, maximum resolution.

If the 3 views do not look like the same person, it has failed. The [signature 1] + [signature 2] + [signature 3] + [signature 4] combination is the signature.
```

**Critical rules:**
- ONE image output with 3 panels. Never deliver 3 separate prompts for the 3 views.
- Layout is LEFT (front body) + CENTER (side profile body) + RIGHT (tight headshot detail). Never swap order, never add extra views.
- Identity description (CHARACTER paragraph) lives once at the top — applies to all 3 panels.
- COSTUME applies uniformly to all 3 panels — same wardrobe across LEFT and CENTER.
- The 85mm lens spec is only on RIGHT (the headshot) — LEFT and CENTER use standard full-body framing.
- Background is flat grey seamless. The locked reference image must be clean for downstream char-ref use.
- Output aspect: 16:9 master (each panel ends up roughly 1:1.78 vertical when split).

**When to use the 6-panel instead:** when the user explicitly needs back view, hand detail, or extreme face-only macro that the 3-view doesn't cover. The 6-panel is supplementary, generated AFTER the 3-view exists.

**Downstream use of the 3-view output:**
1. Generate the sheet, save as `<TOKEN>-ref.png`
2. For every later shot, attach `<TOKEN>-ref.png` as the character-ref image
3. Inline `<TOKEN>` in the shot prompt — the skill pulls CHARACTER + COSTUME from inside the Prompt block as the inline description
4. The shot prompt only adds beat-specific content (action, location, lighting mood, framing)

---

## §3x2-6panel-character — 6-PANEL CHARACTER SHEET

Multi-angle character sheet showing the same character from 6 angles in one 16:9 master frame, 3 columns × 2 rows.

**Canonical panel layout (top row left-to-right, bottom row left-to-right):**

| Position | Shot | What it captures |
|---|---|---|
| 1 — top-left | Full body front | Straight-on neutral stance, full styling head-to-boots |
| 2 — top-center | Full body 3/4 turn | Body angled 30° from camera, weight on back hip |
| 3 — top-right | Full body back | Straight back view — hair fall, pant drape, accessory back-detail |
| 4 — bottom-left | Waist-up portrait | Head, shoulders, upper torso — face and upper styling |
| 5 — bottom-center | Hands detail close-up | Both hands forward, ring stack, nail finish, held prop |
| 6 — bottom-right | Face detail close-up | Tight crop collarbone up — earrings, lips, skin texture, eyes |

**Variation rule:** if the user wants a different panel mix (profile side, midriff close-up, boot detail, back-of-head showing hair clip), swap by name but keep 3×2 grid and single-prompt format.

**Prompt structure:**

```
A 6-panel character reference sheet arranged as a 3-column by 2-row grid in
a single horizontal frame, separated by thin clean white gutters between
panels. Each panel shows the same single character — [<CAST_TOKEN> inlined
with full identity + default wardrobe + body markers + held props].

Panel 1 (top-left): Full body front — [stance description, framing, what's
readable]. Panel 2 (top-center): Full body 3/4 turn — [stance, angle].
Panel 3 (top-right): Full body back — [what's visible from behind]. Panel 4
(bottom-left): Waist-up portrait — [framing]. Panel 5 (bottom-center): Hands
detail close-up — [hand positioning, what's visible]. Panel 6 (bottom-right):
Face detail close-up — [tight portrait crop, what's filling the frame].

Pure white seamless studio backdrop applied uniformly across all six panels.
Soft three-point classical lighting — key from camera-left at 45 degrees,
gentle fill from camera-right, subtle rim defining shoulder and hair
separation — applied uniformly across all six panels. Sharp focus across
every panel. Identical character identity locked across all six panels —
same face, same skin, same hair, same wardrobe, same accessories, same
proportions in every cell.

[Photoreal stack v3 here]
```

**Critical rules:**
- One prompt, one fenced code block, one image output. Never 6 separate prompts.
- Identity description lives in the opening paragraph — described once, applies to all 6 panels.
- Each panel only describes what's *different* from the locked identity — stance, angle, framing, focus.
- Every panel must include the explicit panel position label so the model composes the grid correctly.

---

## §3x3-contact-sheet — 3x3 BEAT CONTACT SHEET

Same beat/action across 9 panels, cast + location locked, only angle and framing change. The workhorse format for storyboard coverage.

**Prompt structure** (the locked grammar for this format):

````
Cinematic 3x3 contact sheet, one master image, 9 panels in a clean 3x3 grid,
thin minimal dividers only. NO text, NO labels, NO KF numbers, NO watermarks.
Row-major order implicit. Photoreal premium commercial finish.

IMPORTANT — REFERENCE LOCK (NON-NEGOTIABLE):
- USE THE EXACT [<CAST_TOKEN_1>] from the attached reference image. LIKENESS
  REPLICATION, not inspiration. Replicate face shape, jawline, nose, eyes, brows,
  skin tone, hair color and texture precisely. Do NOT idealize, smooth, symmetrize,
  or "improve" the face. Wardrobe locked: [full outfit from token].
- USE THE EXACT [<CAST_TOKEN_2>] from the attached reference image. LIKENESS
  REPLICATION — [full outfit from token].
- USE THE EXACT [<LOCATION_TOKEN>] from the attached reference image — [same
  architecture, same signage, same set dressing, etc. from token]. Background
  must clearly read as this exact location, but fully OUT OF FOCUS in panels
  (heavy bokeh). FOCUS IS ON THE ACTORS.

SUBJECT + ACTION:
[One-paragraph description of the beat — who does what, where they are, what's
happening in the scene. Same continuous action across all 9 panels.]

9 PANELS — same beat, same continuous action, only angle / framing changes:
1. [Angle 1 description — e.g., "Wide 2-shot — hero just inside doors mid-ground,
   cashier small at counter deep background."]
2. [Angle 2]
3. [Angle 3]
4. [Angle 4]
5. [Angle 5]
6. [Angle 6]
7. [Angle 7]
8. [Angle 8]
9. [Angle 9]

LIGHT (every panel): [<STYLE_TOKEN> light direction inlined — key source,
fill character, rim character, BG defocus]. [Specific notes for this beat —
e.g., "no sky drama, no colored flare, no tungsten blowout"].

LOOK (every panel, baked in): [<STYLE_TOKEN> full technical lock inlined —
camera, lens, T-stop, filter, grade, grain, palette hex values, contrast,
black floor, skin IRE].

CONTINUITY: same exact [<CAST_TOKEN_1>] (same face, same wardrobe), same exact
[<CAST_TOKEN_2>], same exact [<LOCATION_TOKEN>], ONE grade across all 9 panels.
Background defocused in every panel. [Specific anti-patterns from style token
gotchas].

OUTPUT: ONE image, 3x3 grid, 9 panels, photoreal, cinematic, zero text baked in.

[Photoreal stack v3 here]
````

**Fall-back if 3x3 keeps breaking:** drop to single-panel prompts using the same lock structure, generate the 9 panels separately, composite in post. Prioritize panels 1, 3, 5, 6 (widest continuity value).

---

## §3x3-9angle-turnaround — 9-ANGLE TURNAROUND (FROM SINGLE FACE SHOT)

Character consistency reference generated from one close-up. 9 camera angles of the same subject, no text, no labels. The `cinematic-9-angle-grid` pattern.

**Panel layout:**

| Row | L | C | R |
|---|---|---|---|
| **Row 1** | MCU | MS | OS |
| **Row 2** | WS | HA | LA |
| **Row 3** | P | 3/4 | B |

Where:
- **MCU** — Macro Close-Up — facial details, eyes, textures. Crop top of head and chin.
- **MS** — Medium Shot — waist or chest up. Standard cinematic portrait framing.
- **OS** — Over the Shoulder — camera behind vague foreground shoulder, looking at subject.
- **WS** — Wide Shot — full body, posture, outfit, environment.
- **HA** — High Angle — physically higher than subject, looking down.
- **LA** — Low Angle — physically lower, looking up.
- **P** — Profile — strictly side, 90°. Subject looks completely left or right.
- **3/4** — 3/4 View — turned 45° away from camera.
- **B** — Back View — directly behind subject.

**Prompt structure (JSON for nano-banana / Flux / GPT-Image):**

```json
{
  "project_name": "9_Angle_Turnaround",
  "instructions_for_ai": {
    "step_1_analysis": "Analyze the input image for subject identity, lighting, skin/material texture, emotion, and color palette.",
    "step_2_inference": "If the input is a close-up, logically infer the subject's outfit, body type, and environment based on the style of the face. Maintain strictly consistent character design across all 9 panels.",
    "step_3_execution": "Generate a 3x3 grid where each panel corresponds to the specific camera definitions below."
  },
  "character_lock": "[<CAST_TOKEN> inlined here — full identity + default wardrobe]",
  "camera_angle_specifications": {
    "MCU": "Macro Close Up: Focus intensely on facial details, eyes, or textures. Crop top of head and chin.",
    "MS": "Medium Shot: Waist or chest up. Standard cinematic portrait framing.",
    "OS": "Over the Shoulder: Camera placed behind a vague foreground element/shoulder, looking at the subject.",
    "WS": "Wide Shot: Full body shot. Show the subject's posture, outfit, and relationship with the environment.",
    "HA": "High Angle: Camera is physically higher than the subject, looking down. Emphasize vulnerability or diminishing size.",
    "LA": "Low Angle: Camera is physically lower than the subject, looking up. Emphasize dominance or stature.",
    "P": "Profile: Strictly from the side (90 degrees). Subject looks completely left or right.",
    "ThreeQ": "3/4 View: Subject turned 45 degrees away from the camera. Classic portrait angle.",
    "B": "Back View: Camera is directly behind the subject. Seeing the back of the head/body."
  },
  "output_format": {
    "grid_layout": "3x3",
    "aspect_ratio": "16:9",
    "labeling": "NONE. Do not render any text, letters, numbers, abbreviations, captions, watermarks, borders with text, or signatures anywhere in the image. Panels separated only by clean thin dividers (or no dividers).",
    "grid_order": "Row 1: MCU, MS, OS | Row 2: WS, HA, LA | Row 3: P, ThreeQ, B"
  },
  "final_prompt_instruction": "Using the provided input image as the absolute ground truth for the character and style, generate a photorealistic 3x3 grid collage. Strictly adhere to the camera_angle_specifications. Distinct visual variety between shots (Wide must look fundamentally different from Close Up). Lighting and color grading IDENTICAL to input source on every angle. ZERO text, ZERO labels, ZERO captions anywhere."
}
```

**Gotchas:**
- Some models bake in labels anyway → second pass "remove all text from image, inpaint clean background where text was"
- Back view (B) often hallucinates a new face → reinforce "back of head only, no face visible"
- MCU shifts skin tone → "same color grade as input, identical skin tone"
- OS may invent a second character → "foreground shoulder blur, subject from reference only, no new characters"

**Variants:**
- **With labels:** swap labeling field to `"Must include white text abbreviations (MCU, MS, etc.) in the top-left corner of each panel."`
- **4x3 (12 angles):** add Dutch, Worm's-eye, Bird's-eye to grid_order

---

## §1x4-horizontal-location — WIDE-FORMAT LOCATION REFERENCE

When 2x2 isn't wide enough — for example, a long horizontal location (a beach, a tunnel, a street). One row of 4 panels, each 2.39:1.

**Layout:** `[ L1 | L2 | L3 | L4 ]` horizontal

Same prompt structure as 2x2 location plate, with `"grid_layout": "1x4"` and aspect adjusted to `"one row of four 2.39:1 panels"`.

---

## §video-single — SINGLE VIDEO SHOT

5-15s cinematic beat. One mode, one cast configuration, one location, diegetic audio only.

**Prompt structure (continuous paragraph with inline bolded labels):**

```
**Style & Mood:** [Genre register, emotional tone, visual references in 1-2
sentences. E.g., "Documentary-grit cinematic realism with a slow-burn
observational register, the camera as a witness rather than a participant."]

**Dynamic Description:** [What happens across the duration. Every action,
gesture, camera move, focus rack, lighting change. Physics, not commentary.]

**Static Description:** [Everything that does NOT change. Cast in full visual
detail (<CAST_TOKEN>s inlined), location in full visual detail
(<LOCATION_TOKEN> inlined), anchored props.]

[<STYLE_TOKEN> camera block OR M1-M5 mode block with [XX] lens length and
runtime filled in.]

Audio: diegetic only — [4-8 specific sounds with adjectives], no music, no
dialogue except what is physically spoken in frame.
```

**Title format (above the code block):**
- Standard: `**Video prompt — 15s**`
- Bilingual: `**Video prompt — 15s, EN+ZH**`

**Runtime rules:**
- Always ask the user for runtime, never assume
- Runtime appears in three places: title, dynamic description (if shot duration is referenced), and camera block end
- Default frame rate: 24fps with 180° shutter

---

## §video-multishot — MULTI-SHOT VIDEO SEQUENCE

Multiple stitched beats with hard cuts. Per-shot timing inline.

**Format:** same as §video-single, but Dynamic Description labels each shot with its time range:

```
**Dynamic Description:** Shot 1 (0–3s): [action]. Hard cut to Shot 2 (3–8s):
[action]. Hard cut to Shot 3 (8–15s): [action].
```

**Multi-mode stacking:** if shots are in different cinema modes, write each shot's camera block separately. Don't average the specs.

**Title format:** `**Video prompt — 15s, 3 shots**`

The timing in the inline labels MUST add up to the total runtime in the title and camera block.

---

## UNIVERSAL GRID RULES

1. **One image, one prompt, one code block** — never N separate prompts for an N-panel grid
2. **Identity / location / style described once at the top** — applies to every panel
3. **Each panel describes only what's *different*** — angle, framing, focus, action moment
4. **CONSISTENCY paragraph at the end** — reaffirms what stays locked across panels
5. **No text in output** — explicit "NO text, NO labels, NO captions, NO watermarks, NO signatures anywhere"
6. **Aspect ratio in the API parameter, not the prompt body**
7. **Photoreal stack closes every prompt** — v3 if cast present, v3-ENV if empty
8. **Fall-back to single-panel** if multi-panel keeps breaking — composite in post

---

## CHOOSING A GRID — DECISION TREE

```
Is it video? ──► §video-single OR §video-multishot
   │
   no
   │
Is it for character consistency from one face shot? ──► §3x3-9angle-turnaround
   │
   no
   │
Is it for character multi-angle + outfit? ──► §3x2-6panel-character
   │
   no
   │
Is it for beat coverage (same action, multiple angles)? ──► §3x3-contact-sheet
   │
   no
   │
Is it for empty location pre-light? ──► §2x2-location OR §1x4-horizontal-location
   │
   no
   │
Single still scene plate? ──► §1x1-scene-plate
   │
   no
   │
Character base reference on white seamless? ──► §1x1-character-base
```
