# Failure Modes — Symptom → Cause → Fix

The recurring ways AI image/video generation goes wrong, and the exact prompt-language fix for each. Consult before re-rolling — the prompt is almost always the lever, not the model.

---

## Motion & physics

| Symptom | Cause | Fix |
|---|---|---|
| Actor floats / no weight | No body-weight cue in Actor Behavior block | Add `"weight settled on her right hip"` / `"shoulders dropped"` / `"hand braced on the counter"` |
| Bouncy weightless sprint | "Sprinting" / "running furiously" verbs | Replace with `"compact stride, shoulder leading, arms tucked"` |
| Hair, fabric, environment static | No environmental force block | Add wind/gravity/surface line — single-element wind reads as a fan on set, multi-element wind reads real |
| Slow-motion drift | Unprompted slo-mo bias | Append negative: `"no slow-motion, no time-dilation"` |
| Random extra shot at the end of a long video | Duration too long for the prompt's beats | Shorten the duration, or add explicit per-beat coverage with bracketed timecodes |

## Performance & expression

| Symptom | Cause | Fix |
|---|---|---|
| Tears stream / over-acting grief | "Cries" / "weeps" verb in actor behavior | Replace with `"her eyes glass over; she does not blink. She swallows once."` |
| Smile too wide / unnatural laugh | "Smiles widely" / "laughs hard" | Replace with `"the corner of her mouth lifts, then settles"` |
| Telegraphed rage / fury | "Rages" / "fumes" verb | Replace with `"his jaw tightens once; the hand on the table flattens"` |
| Face reads "AI smile" — symmetric / plastic | No micro-action; no held beat | Add micro-action ("she swallows", "her thumb traces the fold") + 1-3s held beat |
| Eye contact dies between cuts | Cuts breaking the gaze continuity | Anchor the gaze in continuity block: `"she has held his gaze since the previous shot"` |

## Camera

| Symptom | Cause | Fix |
|---|---|---|
| Camera flies / drones / swoops | "Sweeping" / "epic" / "drone" / "cinematic camera movement" verbs | Replace with `"locked-off"` / `"slow handheld breathing, micro-drift"` / `"dolly-in at walking pace"` |
| Camera morphs / warps / glitches on rotation | "360-degree rotation" or aggressive orbit prompts | Don't orbit. Use slow truck right/left instead |
| Driving scene reads music video | Camera moves too much inside cabin | Lock the frame: `"locked-off frame on the driver, slight handheld breathing"` |
| Wide reads soundstage | Locked-off + no environmental force | Add wind/dust/light-movement to Environmental Force block |

## Identity & wardrobe

| Symptom | Cause | Fix |
|---|---|---|
| Identity drifts across cuts | Face reference passed once, not doubled | Pass face ref in `--image-url` AND restate identity in prompt body: `"use the attached face image as the EXACT identity reference; preserve facial features, beard line, eye shape, nose, lip shape exactly"` |
| Wardrobe simplifies in wides | Token block was paraphrased instead of inlined | Inline the full reusable prompt token verbatim — never abbreviate |
| Wrong watch / wrong logo on product close-up | Model invented because product wasn't shown | Build the destination shot as a still first; pass it as `end_image`. Always pass product ref images |
| Generic-looking product in final video frame | No end-frame anchor generated | Generate end-frame still, pass as `end_image` to video call |
| Two characters get visually swapped / reversed | Distinguishing detail not restated per prompt | Restate the distinguishing markers in every prompt — e.g., `"<TOKEN_A> = bald with red tracksuit; <TOKEN_B> = long hair with teal tracksuit"`. Critical for two-cast scenes where the wardrobe/hair distinction is the only differentiator. |

## Continuity

| Symptom | Cause | Fix |
|---|---|---|
| Lighting changes between cuts | No lighting anchor repeated per shot | Copy lighting line verbatim into every shot's prompt — `"late-afternoon window light from screen-left"` |
| Wardrobe changes between cuts | No wardrobe anchor repeated | Restate full wardrobe in every shot — never `"(as above)"` |
| Time-of-day drifts | No explicit anchor | Add `"overcast late afternoon, ~4pm light"` to every shot |
| Geography doesn't match (actor teleports) | No transition cue | Open each shot with `"continuing from previous shot, she has just..."` |
| Audio bed shifts between cuts | No audio anchor repeated | Lock the ambient bed in Block 6 — same wording across interior shots |
| Locked environment drifts | Anchor details not restated | Restate every anchor detail per shot — e.g., for KillCo back room always include `"dark room, desk, red neon lighting, oriental carpets on the floor"` |

## Environment & background

| Symptom | Cause | Fix |
|---|---|---|
| Background too bright / blown highlights | No exposure direction; window key dominating | Reduce key, drop BG exposure −1 stop: `"small warm practicals only, no blown windows"` |
| Background too dark / horror look | Tungsten dominating, no key | Reaffirm sunset/window as hero key: `"bright interior, sunset is the hero key, NOT dark tungsten"` |
| Flat overhead fluorescent wash | Default ceiling lighting taking over | `"interior sculpted by directional window light + practicals only, no overhead fluorescent wash"` |
| Hallucinated extra people | Model loves to add cashiers / extras | `"EMPTY environment, no people, no hands, no silhouettes on any panel"` |
| Hallucinated text / logos / signage | No constraint | Append negative: `"no text overlay, no logos, no signage, no watermark, no captions"` |
| Color drift across grid panels | Per-panel re-light | `"identical color grade and white balance across all panels, same time of day, same sun position"` |
| Anamorphic disappears | Model defaulted to spherical | `"anamorphic lens character, oval bokeh on highlights, horizontal flare streaks, 2.39:1"` |

## Cost & efficiency

| Symptom | Cause | Fix |
|---|---|---|
| Burning credits on bad video renders | Skipped storyboard / preview tier | Always: storyboard still → end-frame still → 480p preview → 1080p hero. Never jump to hero |
| Burning credits on regenerated stills | No reference lock between attempts | Save first decent base as token; subsequent calls inline the token |
| 4K storyboard sheets eat credits | Panels are small; 4K adds no resolvable detail | Render storyboard sheets at 2K |
| Identity drift forces re-rolls | Face ref not doubled in prompt body | Double the face ref (see Identity section) |

## Reinforcement language patterns

Reusable lines for restating critical anchors:

- **Identity lock**: *"Use the attached face image as the EXACT identity reference; preserve facial features, beard line, eye shape, nose, lip shape exactly. Likeness replication, not inspiration."*
- **Wardrobe lock**: *"Wardrobe locked: [full description]. Do not simplify, do not substitute, do not invent additional garments."*
- **Location lock**: *"Use the EXACT location from the attached reference; same counter, same shelves, same signage, same practicals. Background defocused but identifiable."*
- **One-action-per-shot**: *"One clear action arc; do not stack multiple actions or beats in this shot."* (Kling 3.0 especially)
- **No abbreviation**: *"Full description restated; do not infer from previous shots."*
- **Empty plate**: *"EMPTY environment — no people, no hands, no silhouettes, no characters of any kind."*

---

## Related

- [cinematic-grounding.md](cinematic-grounding.md) — the five pillars + six-block structure (the prevention)
- [camera-grammar.md](camera-grammar.md) — M1-M5 cinema modes
- [photoreal-stack.md](photoreal-stack.md) — locked photoreal block for stills
