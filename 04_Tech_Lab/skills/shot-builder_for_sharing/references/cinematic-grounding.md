# Cinematic Grounding — The Craft Layer

## Required reading

This file is the language layer. It defines what to write in every Block 3 (Actor Behavior) and every Reaction Faces entry. Read it whenever:

- Writing a video prompt (every time, no exceptions)
- Writing the Reaction Faces table in any cast token
- Writing the Action / Dynamic Description in a multi-shot video sequence
- Recovering from a "telegraphed grief" / "epic sweeping drone" / "stares deeply" drift

Paired files: [camera-grammar.md](camera-grammar.md), [audio-grammar.md](audio-grammar.md), [character-sheet.md](character-sheet.md) (for Reaction Faces — uses the Block 3 grammar defined here).

---

## Workflow mode awareness

This file applies to BOTH `ref2video` and `text2video`. The difference is ONE line:

- **ref2video** — when a reference image is attached, add the anchor line:
  ```
  use attached <reference description> for face — LIKENESS REPLICATION, do NOT idealize
  ```
  Place this after Block 2 (Shot Direction) and before Block 3 (Actor Behavior). The Block 3 grammar (weight + micro-action + held beat) still applies — the anchor doesn't replace it.

- **text2video** — no reference attached, omit the anchor line. All six blocks unchanged.

Common drift to avoid: assuming ref2video means "drop the description." It does NOT. Theo's actual ref2video prompts include the full character description AND the LIKENESS REPLICATION anchor — the anchor tells the model "use the ref for face geometry, use the text for everything else (costume, build, posture, expression)." Dropping the text causes wardrobe / build / posture drift.

---

How to write a prompt that doesn't read as "AI cinema." Five pillars + six-block structure + forbidden patterns + scene templates.

Load this whenever generating a video prompt where the subject is a real human in a real space. Skip for stylized animation, motion design, abstract, or product-on-white.

---

## Core principle

Cinematic realism is built from **restraint, not spectacle**. Every block enforces grounding so video diffusion models don't drift into the over-animated, floaty, smiling, telegraphed failure modes.

A prompt that drops any pillar produces "AI cinema" — technically a video, structurally a tell.

---

## The Five Grounding Pillars

Every video prompt must respect all five.

### 1. Body weight & physics
Actors have mass. Movement has friction, momentum, contact force.

- Settle the weight somewhere explicit: *"weight on her right hip"*, *"shoulders dropped"*, *"hand braced on the counter"*.
- Specify contact with the world: *"foot pressing into wet pavement"*, *"hip cocked against the door frame"*.
- Forbidden: floating, gliding, weightless poses.

### 2. Environmental force
Wind, water, gravity, fabric, surface — the world pushes back on the actor.

- Multi-element wind: hair, coat, grass, gulls — not just hair.
- Rain weight on shoulders, droplet trails, surface sheen.
- Gravity transfer: knee bend, hip shift on weight change.
- Floor compliance: carpet absorbs step, hardwood transmits.
- Forbidden: actors in a vacuum, single-element wind, perfectly still environments.

### 3. Emotional restraint
Micro-expressions, held beats, breath. Performance lives in stillness.

- Replace "cries" with *"her eyes glass over; she does not blink"*.
- Replace "smiles widely" with *"the corner of her mouth lifts, then settles"*.
- Replace "rages" with *"his jaw tightens once; the hand on the table flattens"*.
- Always include one held beat: 1-3 seconds of intent stillness.
- Forbidden: tears streaming, laughing hard, telegraphed grief / joy / fury.

### 4. Camera as observer
The lens has weight, intent, and limits. Not a drone, not a god.

- Use specific lexicon: *"locked-off static frame"*, *"slow handheld breathing, micro-drift"*, *"dolly-in at walking pace"*, *"slow truck right, following her shoulder"*.
- Lock the frame more often than not — especially driving, intimacy, emotional close-ups.
- Forbidden: *"epic sweeping drone shot"*, *"cinematic camera movement"* (too vague — the model defaults to floaty), *"360-degree rotation"* (almost always morphs).

### 5. Continuity anchors
Multi-shot scenes don't carry context automatically. Anchors must be repeated in every prompt.

- **Lighting**: source, direction, color temperature — verbatim across shots.
- **Wardrobe**: full description, same wording — never *"as above"*.
- **Time of day**: explicit — *"overcast late afternoon, ~4pm light"*.
- **Geography**: where the actor ended the previous shot.
- **Audio bed**: same ambient signature across interior shots.

For identity continuity across shots, also pass the same reference image / generated base shot every time. Identity drift compounds — passing a face ref once isn't enough.

---

## The Six-Block Video Prompt Structure

The order is **load-bearing** — video diffusion models weight earliest blocks most heavily for composition, later blocks for motion and audio.

```
[STYLE & MOOD]
[SHOT DIRECTION]
[LIKENESS ANCHOR]      ← ref2video only; omit in text2video
[ACTOR BEHAVIOR]
[ENVIRONMENTAL FORCE]
[CAMERA BEHAVIOR]
[AUDIO]
```

The LIKENESS ANCHOR is one line:

```
use attached <reference description> for face — LIKENESS REPLICATION, do NOT idealize, do NOT smooth, do NOT symmetrize
```

For locations:

```
the attached <LOCATION> reference image MUST be the architectural source — do NOT invent a generic version
```

### Block 1 — Style & Mood (1 line)

One sentence. Cinematographer's lexicon. Pick a film stock or DP reference; default if nothing given: *"35mm anamorphic, naturalistic skin tones, soft contrast."*

- ✓ *"35mm anamorphic, naturalistic skin tones, soft window light, muted teal-and-amber palette."*
- ✗ *"Cinematic, beautiful, dramatic, epic."* (adjective stacks flatten output)

### Block 2 — Shot Direction (1 sentence)

The action distilled. Subject, verb, object, location. No adjectives that aren't structural.

- ✓ *"A woman in her forties leans against a kitchen counter, reading a folded letter."*
- ✗ *"A beautiful sad woman sadly reads a heartbreaking letter in a sad kitchen."*

### Block 3 — Actor Behavior (2-3 sentences)

The grounding lives here. Director's notes — physical, specific, restrained.

**Always include:**
- A **weight cue** — where mass is settled
- A **micro-action** — small involuntary motion
- A **held beat** — moment of stillness with intent

### Block 4 — Environmental Force (1-2 sentences)

What pushes back. Without this, the shot reads soundstage.

Pick from: air (wind on hair, fabric, dust), water (rain weight, sheeting, droplets), gravity (weight transfer, knee bend), surface (floor compliance, wall texture), light (moving sources — passing headlights, candle flicker).

### Block 5 — Camera Behavior (1 sentence)

Specific lexicon only. Default to locked-off or slow handheld breathing unless the scene demands movement.

### Block 6 — Audio (1 line)

Diegetic first, then any vocal. Modern video models (Kling 2.6, Veo, Sora 2) generate native audio.

- ✓ *"Ambient: rain on glass, refrigerator hum, paper rustling. No music. No dialogue."*
- ✓ *"Ambient: tire hum on asphalt, faint heater fan. She whispers: 'I'm still here.'"*
- If silence intended: *"Ambient: room tone only. No dialogue, no music."*

---

## Forbidden Verbs / Phrases — Always Rewrite

| Don't write | Write instead |
|---|---|
| "Tears stream down her face" | "Her eyes glass over; she does not blink." |
| "Cries / weeps / sobs" | "She swallows once. A breath catches." |
| "Smiles widely / laughs hard / grins" | "The corner of her mouth lifts, then settles." |
| "Rages / explodes / fumes" | "His jaw tightens once. The hand on the table flattens." |
| "Runs furiously / sprints" | "He breaks into a run, shoulder leading, arms compact." |
| "Stares deeply / intensely" | "She holds his gaze for two seconds without blinking." |
| "Epic sweeping drone shot" | "Slow truck right at walking pace, eye-level." |
| "Cinematic camera movement" | (Be specific — locked off, slow handheld, dolly-in walking pace.) |
| "Beautiful / stunning / amazing" | (Cut. Specify a film stock or DP reference instead.) |
| "As above / see previous" | (Restate the full description every shot. Never abbreviate.) |

---

## Standard Negative Baseline

Apply to every prompt unless the user overrides:

```
distorted faces, extra limbs, warped hands, low resolution, blurry, watermark, text overlay, cartoonish, plastic skin
```

Append scene-specific negatives:
- Action / chase: *"no slow-motion, no flying poses, no weightless bounce"*
- Emotional close-up: *"no tears streaming, no telegraphed grief, no exaggerated facial movement"*
- Driving: *"no music-video swoops, no exterior drone shots"*
- Project-specific bans (e.g., *"no cross symbols"* if a token enforces it via its gotchas)

---

## Scene-Specific Templates

Six battle-tested templates. Use as a starting frame, not a rigid form. All defaults assume photoreal cinematic — adjust per locked style token.

### Driving scene (interior, day or night)

```
[STYLE & MOOD]   35mm anamorphic, naturalistic skin tones, low-key interior with passing exterior light.
[SHOT DIRECTION] A man in his late thirties drives alone on a two-lane highway at dusk.
[ACTOR BEHAVIOR] His hands rest on the wheel at 9 and 3, grip relaxed. He glances at the rearview
                 mirror once, then back to the road. His jaw is set; he has not spoken in some time.
[ENVIRONMENTAL]  Light from passing streetlamps and oncoming headlights sweeps across his face in
                 slow rhythmic bands. The cabin is enclosed; dust motes catch in the side window.
[CAMERA]         Locked-off frame on the driver, slight handheld breathing. Background out-of-focus
                 highway moving at speed.
[AUDIO]          Ambient: tire hum on asphalt, faint heater fan, occasional passing vehicle.
                 No music, no dialogue.
```
**Critical:** lock the camera or use very gentle handheld. Aggressive camera in a driving cabin reads as music video, not film.

### Emotional close-up (held, restrained)

```
[STYLE & MOOD]   35mm anamorphic, naturalistic skin tones, soft north-facing window light, shallow DOF.
[SHOT DIRECTION] A woman in her forties stands at a kitchen window, holding a folded letter.
[ACTOR BEHAVIOR] She does not open it. Her thumb traces the fold once. Her shoulders settle, weight
                 shifting to her left foot. Her eyes glass over but she does not blink; she
                 swallows once.
[ENVIRONMENTAL]  Daylight from the window catches the side of her face; the curtain behind her
                 stirs faintly. Dust visible in the light beam.
[CAMERA]         Slow push from medium to tight close-up over the full shot duration, ending at her eyes.
[AUDIO]          Ambient: distant kitchen radio under the noise floor, refrigerator hum, paper
                 rustling between her fingers. No dialogue.
```
**Critical:** no tears, no telegraphed grief. The performance lives in the held beat and the micro-action.

### Action / foot chase (grounded)

```
[STYLE & MOOD]   35mm anamorphic, naturalistic color, overcast daylight, handheld vérité.
[SHOT DIRECTION] A man in his thirties runs down a narrow alley between brick buildings, pursued
                 from off-screen.
[ACTOR BEHAVIOR] His stride is compact, arms tucked, shoulder leading into each turn. He clips a
                 steel trash can with his hip without slowing. His breathing is audible, irregular.
                 He glances back once, then forward.
[ENVIRONMENTAL]  Wet pavement catches the gray sky; puddles splash where his feet land. A loose
                 plastic bag tumbles past him in the wind. Brick walls close on both sides.
[CAMERA]         Handheld camera following at his shoulder height, two paces behind, breathing
                 with his stride. Lens flares briefly when he passes an open doorway.
[AUDIO]          Ambient: footsteps on wet concrete, his breathing, distant city traffic, bag
                 scraping against the wall. No music.
```
**Critical:** keep stride compact. Video models over-render "sprinting" as bouncy, weightless action-hero pose. Write "compact, shoulder-leading" to ground it.

### Intimacy (restrained, close)

```
[STYLE & MOOD]   35mm, naturalistic skin tones, warm low-key practical light from a bedside lamp, shallow DOF.
[SHOT DIRECTION] Two people in their thirties sit close on the edge of a bed, neither speaking.
                 One rests their forehead against the other's temple.
[ACTOR BEHAVIOR] They breathe in near-sync. One hand finds the other's, fingers settling without
                 grip. Neither moves to kiss; the stillness holds. A small smile passes between
                 them, then fades.
[ENVIRONMENTAL]  The bedside lamp throws warm light across one side of both faces; the room
                 behind is in shadow. Bedding compresses where they sit.
[CAMERA]         Static frame, no camera movement. Shallow focus held on the contact point
                 between their foreheads.
[AUDIO]          Ambient: room tone, faint clock ticking, soft fabric movement. No dialogue, no music.
```
**Critical:** intimacy is built from non-action. Resist the urge to add a kiss, a tear, a whispered line — over-rendered every time.

### Environmental interaction (weather as character)

```
[STYLE & MOOD]   35mm anamorphic, naturalistic color, late-afternoon overcast, slight teal cast.
[SHOT DIRECTION] A woman in her fifties walks slowly along a coastal cliff path, hands in her
                 coat pockets.
[ACTOR BEHAVIOR] Her stride is measured, weight settling into each step against the slope. The
                 wind catches her hair from the left; she does not push it back. Her coat collar
                 flutters; she pulls it tighter once.
[ENVIRONMENTAL]  Strong onshore wind shapes everything in frame — grass laid flat, coat pressed
                 against her body, salt spray visible in the air. Sea below gray and churning;
                 gulls hold position against the wind.
[CAMERA]         Slow truck right, matching her pace, framing her in medium-wide profile with the
                 sea beyond. Horizon line stays level.
[AUDIO]          Ambient: wind through grass, distant surf, gull calls. Footsteps soft on the path.
                 No dialogue, no music.
```
**Critical:** wind must shape multiple elements (hair, coat, grass, gulls) — single-element wind reads as a fan on set.

### Dialogue (two-shot or single, anchored)

```
[STYLE & MOOD]   35mm, naturalistic skin tones, motivated practical light, slight shadow contrast.
[SHOT DIRECTION] Two people sit across a small cafe table, mid-conversation; he leans back, she
                 leans slightly forward.
[ACTOR BEHAVIOR] He sets his cup down without looking at it; his fingers stay curled around the
                 handle for two beats. She tucks a strand of hair behind her ear, holds his gaze.
                 Neither smiles. He takes a breath before speaking.
[ENVIRONMENTAL]  Steam rises from the cup, drifting in the window light. Faint motion of other
                 patrons out of focus behind them. Wooden table catches a warm reflection.
[CAMERA]         Static two-shot, slight handheld breathing. No movement.
[AUDIO]          Ambient: low cafe chatter under noise floor, espresso machine in the distance,
                 cup settling on saucer. He: "I know." (single line, low volume.)
```
**Critical:** the line lands harder when everything else is restrained. Over-direct the body, under-direct the words.

---

## How the skill applies this

When composing a video prompt, the skill loads this file along with the relevant cinema mode (M1-M5) and the locked tokens (cast, location, style). The six-block structure is the **output template**. The five pillars are the **silent checklist** run before delivery.

Order of operations:

1. Identify scene type → pick template (or compose freestyle).
2. Inline cast + location + style tokens verbatim into Block 2 + Block 3 + Block 4.
3. Verify all five pillars present: body weight cue, environmental force, held beat, specific camera, continuity anchors.
4. Append standard negatives + scene-specific negatives.
5. Deliver in six-block fenced format.

If a pillar can't be satisfied (e.g., user asks for a stylized shot that explicitly wants weightless motion), note the exception in a one-liner before the prompt block — don't silently drop the pillar.

---

## Related

- [camera-grammar.md](camera-grammar.md) — M1-M5 cinema modes (camera + lens + grade specs)
- [audio-grammar.md](audio-grammar.md) — diegetic audio rules
- [photoreal-stack.md](photoreal-stack.md) — the locked hyperreal block (still images)
- [failure-modes.md](failure-modes.md) — symptom→cause→fix table
