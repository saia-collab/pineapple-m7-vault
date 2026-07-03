---
name: shot-builder
description: "Image and video director that generates via FAL.ai, Kie.ai, or prompt-only (no API). Builds reusable token packs for cast, locations, styles. Composes single shots, 3-view character turnarounds (front, side, detail headshot), 2x2 location plates, 3x3 and 6-panel contact sheets, cinematic plates across five camera modes. Setup stores provider, key, output paths, workflow mode, defaults. Distinguishes ref2video (attach a reference image plus a LIKENESS REPLICATION anchor) from text2video (description only) to prevent identity and wardrobe drift. Each cast token's Prompt block is a paste-ready 3-view turnaround grid; run once, save the reference, attach to every later shot. Use when developing a character, locking a location or style, generating a still or contact sheet, building a turnaround, or kicking off a cinematic video. Triggers: character sheet, model sheet, ref sheet, turnaround, 3-view, location plate, establishing shot, contact sheet, 3x3, 9-angle, cinematic video, ref2video, text2video."
---

# Shot Builder — Full-Pack Image + Video Director

Reusable token packs in, generated pixels out. One skill for cast, locations, styles, single shots, contact sheets, and cinematic video — all running directly against FAL.ai or Kie.ai (or pure prompt-only mode).

The skill is **workflow-aware, token-aware, and provider-aware**: it composes prompts from your saved `<TOKENS>`, picks the right cinema grammar, and dispatches generation to the provider you set up.

---

## STEP -1 — HARD RULES (READ FIRST, NEVER VIOLATE)

These rules prevent the most common drifts observed in production sessions. They override anything else in this file.

1. **NEVER skip the scripts.** If `setup.py`, `project.py`, or `token_resolver.py` exists at the path below, you MUST run it before doing the same thing by hand. No "I'll just write config.json manually" — the script writes the canonical schema, hand-edits drift.
2. **NEVER delete files under `workspace/` or `<output_dir>/`** without explicit user confirmation in this turn. Not even at session end. Not even if they look like scratch data.
3. **NEVER overwrite `INDEX.md` from scratch.** It is auto-managed by scripts. Read it. Append via `fal_gen.py` / `kie_gen.py` / `prompt_only.py`. If you think it needs structural change, fix `setup.py.seed_index()` and re-seed — never hand-edit.
4. **NEVER add routing logic to `INDEX.md`.** Routing lives in this file (SKILL.md). INDEX.md is a hot cache only.
5. **NEVER inline a `<TOKEN>` by paraphrasing it.** Run `token_resolver.py` and paste the locked block verbatim. Paraphrasing = drift.
6. **NEVER mix conflicting lighting in a 2x2 location plate** (day + night in the same plate). One light state per plate. Need both? Two separate plates, with the day plate fed as reference into the night-plate generation so the architecture stays consistent.
7. **NEVER write a video prompt before the cast/location tokens it references exist.** Run `token_resolver.py <TOKEN>` first. If missing, lock it via §2A/2B/2C before composing.
8. **When stuck on naming or structure, run a script — do not debate.** Token name unclear? `python "$SKILL_DIR/scripts/token_resolver.py" --list-projects --roster`. Provider down? `python "$SKILL_DIR/scripts/cost.py" balance --provider kie`. Test before theorizing.

---

## SCRIPT LOCATIONS (ABSOLUTE PATHS)

Set `$SKILL_DIR` to the absolute path of this skill once per session, then use it for every script call:

```bash
# macOS / Linux — pick the one that resolves to this file's parent directory
SKILL_DIR="$HOME/.claude/skills/shot-builder"
# or, if symlinked from MasterMind:
SKILL_DIR="~/.claude/skills/shot-builder"
```

| Script | Absolute path | What it does |
|---|---|---|
| `setup.py` | `"$SKILL_DIR/scripts/setup.py"` | First-time setup gate |
| `project.py` | `"$SKILL_DIR/scripts/project.py"` | List / create / switch projects |
| `token_resolver.py` | `"$SKILL_DIR/scripts/token_resolver.py"` | Look up `<TOKEN>` files (project-first, global fallback) |
| `cost.py` | `"$SKILL_DIR/scripts/cost.py"` | Estimate cost, session totals, balance checks |
| `fal_gen.py` | `"$SKILL_DIR/scripts/fal_gen.py"` | Generate via FAL |
| `kie_gen.py` | `"$SKILL_DIR/scripts/kie_gen.py"` | Generate via Kie |
| `prompt_only.py` | `"$SKILL_DIR/scripts/prompt_only.py"` | Write prompt sidecar with NO API call |

Every invocation in this file uses the `"$SKILL_DIR/scripts/<name>.py"` form. Do not assume relative paths work — they break when the agent is invoked from a different CWD.

---

## STEP 0 — SETUP GATE (RUN ONCE PER WORKSPACE)

Before any generation, check `"$SKILL_DIR/workspace/config.json"`. If it does not exist, **the setup gate is mandatory** — do not compose any prompt yet. Do not write `config.json` by hand. Run the script:

```bash
python "$SKILL_DIR/scripts/setup.py"
```

The script walks the user through:

1. **Provider** — FAL.ai, Kie.ai, both, or `prompt_only`. Recommend Kie if cost matters (30-50% cheaper, multi-model), FAL if speed and ecosystem matter, `prompt_only` if the user runs generations elsewhere (MJ / ComfyUI / Higgsfield / Replicate / a provider UI). See [providers/fal.md](providers/fal.md) and [providers/kie.md](providers/kie.md).
2. **API key** (skipped for `prompt_only`) — paste prompt-side, saved to `~/.shot-builder/.env` (shared with other skills) or `workspace/.env`. Chmod 600. Confirm before writing.
3. **Default image model** — recommend `nano-banana-pro` (Kie) or `fal-ai/flux-pro/v1.1-ultra` (FAL). User can override per shot.
4. **Default resolution / aspect** — recommend `2K` stills / `1080p` video, `16:9` video / `2.39:1` cinematic stills / `4:5` portraits.
5. **Workflow mode** — `ref2video` (default, attaches a reference in every shot), `text2video` (no reference, identity from prompt text), or `mixed` (ask per-shot). See §STEP 1.5 below — this is the most load-bearing setting in the skill.
6. **Output directory** — one root for every project; per-project subfolder added automatically.
7. **State directory** — `"$SKILL_DIR/workspace/"`, already in place.

After the script writes `workspace/config.json` and seeds `workspace/INDEX.md`, proceed to §0.5. **Do not edit config.json by hand** — re-run setup with `--reset` if anything needs changing.

**Re-run the gate** when the user says: "switch provider", "use FAL instead", "reset setup", "switch to text2video", or `config.json` is missing.

---

## STEP 0.5 — PROJECT GATE (RUN ONCE PER SESSION)

After setup is confirmed, **before composing any prompt**, ensure there is an active project. The project decides where renders save and which token namespace gets searched first.

**At session start:**

1. Run `python "$SKILL_DIR/scripts/project.py" list` to see what exists.
2. If exactly one project exists and the user hasn't named another, set it active and proceed.
3. If multiple exist, **ask:** "which project is this session for? (`<list>`, or `new <name>`)". Wait for the user to pick.
4. If none exist, ask: "this looks like the first session — give the project a name" and run `python "$SKILL_DIR/scripts/project.py" new "<name>" --switch`.

**Mid-session switch — triggered by the user saying:**
- "switch to <slug>"
- "this one's for <project>"
- "actually let's do this for <project>"

→ Run `python "$SKILL_DIR/scripts/project.py" set <slug>`. Confirm the switch in a one-liner ("Switched to `<slug>` — renders will go to `<date>/<slug>/`").

**Where renders land:**

```
<output_dir>/<YYYY-MM-DD>/<project-slug>/shots|scenes/<token>_<NNN>.{png,mp4}
```

If no project is active (user cleared it or skipped), renders go to `<date>/_unsorted/` — flagged for the user so they can sort later.

**Why this matters:** tokens are project-scoped first, global fallback. `<HERO>` in one project can differ from `<HERO>` in another. Reusable cross-project tokens (e.g., `<SELF>` for the user's own face) live in the global `workspace/cast/` directory.

---

## STEP 1 — WORKFLOW MODE (THE MOST LOAD-BEARING SETTING IN THIS SKILL)

Two ways to compose every image/video prompt. Pick one at setup; you can override per-shot.

### `ref2video` (default)

The user attaches a reference image (face portrait, 3-view turnaround sheet, location plate, 6-panel character sheet) in every generation. The model's job is to **animate / re-frame / re-light / re-pose** that reference, not invent identity from text.

**The prompt STILL includes the full character + costume description.** Identity comes from the reference, but wardrobe + posture + expression + costume detail come from the text. Drop the description and the model drifts on outfit / build / hair.

The prompt also includes one explicit anchor line per attached reference:

```
use attached <reference description> for face — LIKENESS REPLICATION, do NOT idealize
```

Or for locations:

```
the attached <LOCATION> reference image MUST be the architectural source — do NOT invent a generic version
```

This is non-negotiable. The anchor line is the load-bearing instruction that prevents drift toward "generic AI face / generic AI architecture."

**When in ref2video mode:**
- Cast description: **INCLUDE IT** in the prompt (full physical + costume).
- Likeness anchor: **INCLUDE IT** as a separate line ("LIKENESS REPLICATION, do not idealize").
- Reaction faces (in cast tokens): expression + pose only, NOT signature features. The reference image carries hair color, build, eye color — repeating those in every Reaction Face entry is redundant and bloats the prompt.

### `text2video`

No reference image. Identity, costume, posture, expression all come from text. Used for synthetic characters with no ref, first-pass design exploration, or stylized content where likeness isn't the goal.

**When in text2video mode:**
- Cast description: full physical + costume description in the prompt (same as ref2video).
- Likeness anchor: **OMIT IT** (no reference attached to anchor to).
- Reaction faces: **INCLUDE** signature features (the model has no image to refer to, so the text must carry the lock).

### `mixed`

Skill asks per-shot before composing. Use when half the shots have references and half don't.

### How the skill checks workflow mode

```bash
python -c "import json; print(json.load(open('$SKILL_DIR/workspace/config.json'))['defaults']['workflow_mode'])"
```

If mode is `ref2video`, every generated prompt must include the LIKENESS REPLICATION anchor when a reference is attached. If mode is `text2video`, the anchor is omitted. The skill **never silently drops the cast description** — only the anchor line varies.

### Per-shot override

User says any of:
- "this one is text2video" → override for this shot
- "ref2video this time" → override for this shot
- "drop the description" → still asks: "are you sure? in ref2video, omitting the description causes wardrobe drift"

---

## STEP 2 — THE TOKEN SYSTEM

Every reusable element of a production gets saved as a `<TOKEN>.md`. Tokens carry across shots and sessions. Three flavors, two scopes each:

| Token type | Global folder | Per-project folder | What it locks |
|---|---|---|---|
| **Cast** | `workspace/cast/` | `workspace/projects/<slug>/cast/` | Identity: face, hair, body markers, wardrobe, default expression |
| **Location** | `workspace/locations/` | `workspace/projects/<slug>/locations/` | Architecture, set dressing, signage, materials, geography |
| **Style** | `workspace/styles/` | `workspace/projects/<slug>/styles/` | Camera body, lens, filter, grade, palette, light direction |

**Lookup order** — when the user names a token, the skill (via `token_resolver.py`) checks the active project's folder first, then falls back to global. A project token with the same name **shadows** a global token of the same name — useful when names overlap across productions.

**When to save where:**
- **Project-scoped** (default) — character / location / style belongs to one production. Saves to `workspace/projects/<active-project>/<kind>/`. Use for `<HERO>`, `<CASHIER>`, `<STATION-INT-SHOP>`.
- **Global** — token reusable across many productions. Saves to `workspace/<kind>/`. Use for `<SELF>` (your own face), a personal LOOK profile, a recurring favorite location.

If the user doesn't specify, ask: *"project-scoped or global?"* once at the first lock; remember the choice for subsequent same-session locks unless they say "make this global / make this project".

**Each token file follows the same shape** (defined in [references/character-sheet.md](references/character-sheet.md), [references/location-sheet.md](references/location-sheet.md), [references/style-sheet.md](references/style-sheet.md)):

- Frontmatter (token name, created date, base image path if any)
- **Canonical description** — the long-form prose lock
- **Reusable prompt token** — fenced code block for paste-in
- **Variants** — alternate wardrobes / lighting / configs
- **Reference images** — paths to refs already shot/generated
- **Gotchas** — known failure modes

When the user invokes a token (typing `<HERO>` or just "hero" in a shot request), the skill loads the token file and inlines the prompt block at composition time. Do **not** paraphrase the token — paste the locked block verbatim.

---

## STEP 3 — THE WORKFLOW (STRICT ORDER FOR NEW PRODUCTIONS)

The skill enforces this order. Skip steps only when the user explicitly says they already have a lock. **Trying to compose a video prompt before locking cast + location = drift guaranteed.**

```
Setup gate  →  Project gate  →  Workflow mode  →  Cast lock  →  Location lock  →  Style lock  →  Shot/Scene compose  →  Generate
   (once)       (per session)    (from config)     (per char)    (per location)   (per look)      (per beat)        (FAL/Kie/prompt_only)
```

### 3A — Develop cast (character sheet)

Triggered by: "new character", "develop a character", "character sheet", "model sheet", "lock <name>".

**REQUIRED READING before composing the cast token:** [references/character-sheet.md](references/character-sheet.md) AND [references/cinematic-grounding.md](references/cinematic-grounding.md). The character-sheet defines the file shape; cinematic-grounding defines the reaction-face / hold-beat language. Reading only one will produce drift.

Procedure:

1. Ask: "reference image, or developing from scratch?"
2. If ref: study and lock identity by visual description only (no names, no brands, no age). Mirror back. Confirm.
3. If scratch: walk the development questionnaire (face, hair, body, wardrobe register). Mirror back. Confirm.
4. Save to `"$SKILL_DIR/workspace/projects/<active>/cast/<TOKEN>.md"` (project-scoped, default) OR `"$SKILL_DIR/workspace/cast/<TOKEN>.md"` (global, if user said it's reusable across productions).
5. **The cast token file contains ONE Prompt block — a 3-view turnaround grid prompt (FRONT body + SIDE body + DETAIL headshot in one image).** When generated, the output IS the character's master identity reference. The user runs the Prompt block in MJ / Flux / Nano-Banana / Runway with their face reference attached, saves the result as `<TOKEN>-ref.png`, and attaches it as the character-ref image on every later shot of that character.
6. **Reaction-faces table mode-awareness:**
   - In `ref2video` mode (default): each reaction face is **pose + expression only** — no signature features (hair color, build, eye color, costume). The reference image carries those. Repeating them bloats the prompt and the model double-processes identity, causing drift.
   - In `text2video` mode: include signature features in every reaction face (the model has no image to anchor identity to).
   - In `mixed` mode: ask before composing the table.
7. **Line-budget enforcement:** Reaction-faces table = max 5 entries. Total file = 60-80 lines. **STOP at the budget — do not exceed "to be thorough."** Over-elaboration causes the model to ignore the most important features.
8. **Offer** to generate the 3-view turnaround sheet immediately after the token file is written (the user usually wants the reference image right away). See [references/grids.md](references/grids.md) §1x3-3view-turnaround.
9. INDEX.md updates itself when a render happens — do not hand-edit it after a lock.

### 3B — Develop location (location sheet)

Triggered by: "location", "environment", "world", "set", "establishing shot of <place>".

**REQUIRED READING:** [references/location-sheet.md](references/location-sheet.md). The 2x2 empty plate has a `REFERENCE (NON-NEGOTIABLE)` block that explicitly anchors architecture to the attached reference — skipping that block means the model invents a generic version.

The pattern is the same as cast but the lock covers architecture, set dressing, signage, materials, time-of-day defaults, and atmospheric character.

**Plate-generation order (load-bearing):**
1. Generate the **day plate** first (or whatever the dominant lighting state is).
2. To generate a **night / dusk / blue-hour variant of the SAME location**, feed the day plate as a reference image with the prompt language: `same architecture as attached <LOCATION> reference, but at <new lighting state>`. This keeps the building, the columns, the materials identical across lighting changes.
3. **Never mix lighting states in one 2x2 plate.** Day + night in the same plate = model picks one and ignores the other, or worse, blends them into something incoherent. One light state per plate.

**Always offer** to generate an empty 2x2 location plate grid (pre-lit, no characters) as the reference — see [references/grids.md](references/grids.md) §2x2-location.

### 3C — Develop style (look / cinema mode)

Triggered by: "look", "grade", "vibe", "style", "match this reference's color", or when the user picks one of the canned cinema modes M1-M5.

Two paths:
- **Canned mode (fastest)** — pick from M1-M5 in [references/camera-grammar.md](references/camera-grammar.md). No new token saved unless the user wants a custom variant.
- **Custom style (token)** — measure or transcribe the look (camera body, lens, T-stop, filter, grade, hex palette, light direction, halation, grain). Save to `workspace/projects/<active>/styles/<TOKEN>.md` (project-scoped, default) or `workspace/styles/<TOKEN>.md` (global). See [references/style-sheet.md](references/style-sheet.md).

### 3D — Compose shot or scene

Triggered by: any request that names a beat, action, or moment. Examples: "single shot of HERO at the counter", "3x3 sheet of HERO + CASHIER coffee handoff", "10s video of HERO entering the shop", "establishing wide of STATION at golden hour".

**REQUIRED PREP — DO NOT SKIP:**
1. Resolve every `<TOKEN>` named in the request before composing:
   ```bash
   python "$SKILL_DIR/scripts/token_resolver.py" --token <HERO> --token <LOCATION>
   ```
   If any token is missing, STOP. Lock it via §3A / 3B / 3C first. Composing a video prompt against a missing token = invented identity = drift.
2. Check workflow mode (see §STEP 1). Decide: include LIKENESS REPLICATION anchor (ref2video) or omit (text2video).
3. For video prompts, also read [references/cinematic-grounding.md](references/cinematic-grounding.md) — the six-block structure and the five grounding pillars are MANDATORY for every video prompt.

The skill assembles the prompt by stacking: `<CAST_TOKENS>` + `<LOCATION_TOKEN>` + `<STYLE_TOKEN>` + per-shot Action/Framing + photoreal stack + (if ref2video) LIKENESS REPLICATION anchor + grid format. See [references/grids.md](references/grids.md) for the layout options.

### 3E — Pre-prompt check (MANDATORY before every generation)

Format — bullet points only, never prose:

```
Pre-flight check:
- **Cast:** <CAST_TOKENS in shot, or "none / environment plate">
- **Location:** <LOCATION_TOKEN, or "white seamless / void / specified">
- **Style:** <STYLE_TOKEN or cinema mode (M1-M5)>
- **Format:** <single / 2x2 / 3x3 / 6-panel / 9-angle / video Xs>
- **Workflow mode:** <ref2video (anchor included) | text2video (no anchor)>
- **References attached:** <list of files attached as inputs, or "none">
- **Provider:** <fal | kie | prompt_only> · **Model:** <model_id> · **Resolution:** <2K | 4K | 1080p> · **Aspect:** <2.39:1 | 16:9 | 4:5>

Run it?
```

Wait for authorization. Then deliver the prompt + dispatch generation.

**Exception — minor iteration on an already-approved prompt** (composition tweak, framing shift, palette nudge, single wardrobe swap): skip the check, deliver and dispatch directly. Still check on: new cast entering, new location, new mode, full outfit swap, switching provider, switching workflow mode (ref2video ↔ text2video).

### 3F — Generate

Call the right script based on provider:

| Provider | Image | Video |
|---|---|---|
| **FAL** | `python "$SKILL_DIR/scripts/fal_gen.py" --type image --model <id>` | `python "$SKILL_DIR/scripts/fal_gen.py" --type video --model <id>` |
| **Kie** | `python "$SKILL_DIR/scripts/kie_gen.py" --type image --model <id>` | `python "$SKILL_DIR/scripts/kie_gen.py" --type video --model <id>` |
| **Prompt-only** | `python "$SKILL_DIR/scripts/prompt_only.py" --type image --label <label>` | `python "$SKILL_DIR/scripts/prompt_only.py" --type video --label <label>` |

Scripts handle: API call (or skip for prompt_only), polling (Kie), image/video download, save to `<output_dir>/<date>/<project>/<kind>/` + mirror log at `workspace/<kind>/<date>/<project>/`, write a **markdown sidecar** next to every render (`<file>.png.md` / `<file>.mp4.md`) containing prompt + cost + tokens used + settings, append to `workspace/INDEX.md` recent-renders, and log to `workspace/session_costs.jsonl`. Pass `--project <slug>` to override the active project. Pass `--token <TOKEN>` (repeatable) to record which tokens were inlined into this render.

**Why the sidecar:** users browse renders in Obsidian, in a Chrome extension, or in the file system — and every artifact carries its own metadata page. They can read the prompt that made it, see the cost, click through to the locked tokens, and regenerate by copy-pasting the prompt. The sidecar is the audit trail.

**Cost gate** runs before every video render. The script calls `cost.estimate_video()`, compares to `$0.50` (preview tier) or `$1.00` (hero tier), and refuses to submit if over threshold unless `--confirm-cost` is passed. The skill asks the user before passing that flag — never auto-fires.

Return the saved path + a one-line summary to the user.

---

## STEP 4 — GRID FORMATS

Pick by intent. Full layouts and prompt templates in [references/grids.md](references/grids.md).

| Format | When to use | Layout |
|---|---|---|
| **1x1 single** | Base reference, isolated detail, scene plate | 1 image |
| **2x2 location** | Empty environment, pre-lit for talent comp, 4 angles | 2x2 grid, 4 angles per [references/grids.md](references/grids.md) §2x2-location |
| **3x3 contact sheet** | Beat coverage — same action across 9 angles, cast + location locked | 3x3 grid, 9 angles per [references/grids.md](references/grids.md) §3x3 |
| **3-view turnaround (canonical character ref)** | THE character identity reference. Run once per character, save as `<TOKEN>-ref.png` | 1x3 grid: FRONT body / SIDE body / DETAIL headshot |
| **6-panel character sheet** | Extended multi-angle character + outfit detail | 3x2 grid: front / 3/4 / back / waist-up / hands / face |
| **9-angle turnaround** | Character consistency reference from one face shot | 3x3 grid: MCU, MS, OS / WS, HA, LA / P, 3/4, Back |
| **Single video shot** | Cinematic beat, 5-15s | Mode-locked, diegetic audio only |
| **Multi-shot video sequence** | Stitched beats, hard cuts inline | Per-shot timing labels, mode per shot if stacked |

**Critical:** never deliver N separate prompts for a grid. One prompt → one image → N panels.

---

## STEP 5 — UNIVERSAL PROMPT RULES

These apply to every prompt the skill writes, no exceptions:

1. **No character names** — describe by hair, wardrobe, identity markers. Tokens (`<HERO>`) get inlined as their locked block.
2. **No real brand names** — generic visual descriptors only. Internal chat can reference brands; the prompt output is brand-neutral.
3. **Age-blind** — never `boy`, `girl`, `child`, `teen`, `young`, `middle-aged`, `elderly`. Describe by build, role, wardrobe.
4. **No `@image` tags, no `<<<image_n>>>` placeholders** — reference images attach in the provider's API (FAL `image_url` array, Kie `referenceImages` array). Prompt text is clean.
5. **Photoreal stack baked in** — every still prompt closes with the locked photoreal stack from [references/photoreal-stack.md](references/photoreal-stack.md). For pure environment plates, drop the human-skin lines, keep light/lens/grain/grade.
6. **No aspect ratios in prompt body** — aspect is a generation parameter, not prompt text. Skill writes it in the API call.
7. **No meta-commentary** — no "the read is...", "this sells the moment", "carried through the scene". Every word describes a visible thing in the frame.
8. **No music or lyrics in audio** — diegetic only per [references/audio-grammar.md](references/audio-grammar.md). Music attaches separately in post.
9. **Pre-flight check, always** — except minor iteration per §2E.
10. **One fenced code block per shot** — clean copy-paste, no preamble inside the block.

---

## STEP 6 — PROVIDER ROUTING

Three branches. Default to the user's setup-gate choice for the first two; the third is always available.

| Branch | Script | When |
|---|---|---|
| **Kie.ai** | `scripts/kie_gen.py` | Default for most users. Cheaper, large catalog, native-audio Kling |
| **FAL.ai** | `scripts/fal_gen.py` | Speed-sensitive shots, bleeding-edge models, brand-clean vector |
| **Prompt only** | `scripts/prompt_only.py` | User wants the prompt but will run it elsewhere — Higgsfield UI, ComfyUI, Replicate, Midjourney, a collaborator, or just for Complimentary iteration. **No API call. No spend.** |

**Override the default when:**

| Situation | Switch to | Why |
|---|---|---|
| User says "use FAL" / "use Kie" / "just the prompt" | their choice | Explicit request always wins |
| Default provider's model doesn't exist for the format | the other | Some models are exclusive to one platform |
| Cost-sensitive batch (many panels, many seeds) | Kie | 30-50% cheaper per call |
| Speed-sensitive single shot | FAL | Faster polling, fewer retries |
| Native audio video (Kling 2.6 with dialogue) | Kie | Kling 2.6 native audio sync is a Kie strength |
| Bleeding-edge model just dropped | FAL | Usually first to ship new models |
| User wants Higgsfield / ComfyUI / Midjourney / OpenAI / Replicate | Prompt only | shot-builder doesn't have direct integration; user runs externally and brings the file back |
| Iterating on prompt language without spending credits | Prompt only | Zero-cost feedback loop |
| Generating for a collaborator who has different tools | Prompt only | Share the `.md` file; they run it on their side |

When switching, do **not** re-run setup. The skill keeps both keys and the prompt-only path is always Complimentary. Update `workspace/INDEX.md` to log the override.

**Prompt-only output:** writes to `<output_dir>/<date>/<project>/prompts/<label>_NNN.md` instead of `shots/` or `scenes/`. Same sidecar shape — frontmatter + body + tokens-used. The user pastes the prompt into whatever tool they want; the sidecar is the canonical record.

---

## STEP 7 — HOT CACHE (workspace/INDEX.md)

`workspace/INDEX.md` is the single source of truth for live workspace state. **Read it first** at the start of any session before composing anything.

**CRITICAL: INDEX.md is auto-managed. Do not edit it by hand.**

- Sections labeled `[auto]` are updated by scripts (`setup.py`, `fal_gen.py`, `kie_gen.py`, `prompt_only.py`, `project.py`).
- Sections labeled `[manual]` (just one — `Active gotchas / notes`) are for the user only. The agent must not edit any section, including the `[manual]` one, without explicit user instruction.
- **Do NOT add a "routing table" or "reference-file restrictions" to INDEX.md.** Routing lives in this file (SKILL.md). INDEX.md is a hot cache.
- **Do NOT overwrite INDEX.md.** If structure needs to change, edit `setup.py.seed_index()` and re-seed by running `python "$SKILL_DIR/scripts/setup.py" --reset`.

Sections (locked template, do not invent new ones):

- **Setup** — provider, workflow mode, key locations, defaults, output dir
- **Active project** — the slug currently in `config.active_project`
- **Workflow mode** — `ref2video` / `text2video` / `mixed`
- **Projects** — every project under `workspace/projects/` with counts
- **Cast / Locations / Styles roster** — global tokens; project-scoped surface via `token_resolver.py --roster --project <slug>`
- **Recent renders** — appended on every successful generation
- **Active gotchas / notes** — the only `[manual]` block

If the file drifts from reality (token file deleted but still listed), the skill reconciles silently on next read.

---

## STEP 8 — WHAT THE SKILL DOES NOT DO

- **No `02-Inbox/` dumps** — token files live in `workspace/`, not Obsidian vault. The user can manually link them later.
- **No retroactive renaming** — once a token is `<HERO>`, it stays `<HERO>`. Renaming breaks every prompt that uses it. Make a new token + deprecate the old.
- **No prompts longer than 800 words** — if the assembled prompt blows past that, the skill warns and offers to drop the photoreal stack to a short ref `(use locked photoreal stack v3)` instead of inlining the full block.
- **No silent provider downgrades** — if the user-specified model fails, the skill reports the failure and asks before retrying on a different model.
- **No automatic style mixing** — only one `<STYLE_TOKEN>` per shot. Cinema modes M1-M5 don't stack inside a single still.

---

## STEP 9 — REFERENCES (LOAD ON DEMAND)

**Dependencies, not just "load on demand":** some reference files MUST be read together. Loading one in isolation produces drift (e.g., reading `character-sheet.md` for the Reaction Faces table without reading `cinematic-grounding.md` for the weight-cue / micro-action / held-beat language).

| File | When to load | Must be paired with |
|---|---|---|
| [references/character-sheet.md](references/character-sheet.md) | Cast development, lock, base-ref generation | `cinematic-grounding.md` (for Reaction Faces) |
| [references/location-sheet.md](references/location-sheet.md) | Location development, lock, 2x2 location plate | `photoreal-stack.md` (for plate look) |
| [references/style-sheet.md](references/style-sheet.md) | Custom style token, look-matching from reference | `camera-grammar.md` |
| [references/cinematic-grounding.md](references/cinematic-grounding.md) | Every video prompt; every Reaction Faces table | `camera-grammar.md`, `audio-grammar.md` |
| [references/photoreal-stack.md](references/photoreal-stack.md) | Always — closes every still prompt | — |
| [references/camera-grammar.md](references/camera-grammar.md) | Mode selection (M1-M5), drop-in camera blocks | — |
| [references/grids.md](references/grids.md) | Any multi-panel grid format | — |
| [references/defaults.md](references/defaults.md) | Resolutions, model IDs, parameter defaults | — |
| [references/audio-grammar.md](references/audio-grammar.md) | Any video prompt | `cinematic-grounding.md` |
| [references/failure-modes.md](references/failure-modes.md) | When a render came back wrong — symptom→cause→fix | — |
| [providers/fal.md](providers/fal.md) | FAL endpoint catalog, auth, polling | — |
| [providers/kie.md](providers/kie.md) | Kie endpoint catalog, auth, polling | — |

---

## STEP 10 — ERROR HANDLING

| Symptom | Fix |
|---|---|
| `config.json` missing | Run setup gate (§0) — `python "$SKILL_DIR/scripts/setup.py"` |
| `setup.py: file not found` | Wrong path. Set `SKILL_DIR` correctly (see SCRIPT LOCATIONS at top of this file) |
| No active project at session start | Run project gate (§0.5) — list, ask, set or create |
| Token referenced but file missing | Stop. Run `python "$SKILL_DIR/scripts/token_resolver.py" --roster`. If truly missing, ask user to lock it via §3A/3B/3C — never invent identity |
| Provider call returns 401 | API key invalid. Re-run setup gate, ask for new key |
| Kie task hangs >120s (image) or >300s (video) | Cancel. Log to INDEX. Offer FAL fallback |
| FAL rate limit (429) | Exponential backoff in script. If 4 retries fail, surface to user |
| Output file already exists | Append `_v2`, `_v3`, etc. — never overwrite |
| Generated image looks wrong (cast drift, location drift) | Pull gotchas from the offending token file. Suggest reinforcement lines. Do not silently re-roll |
| You're debating naming or structure for >2 turns | STOP THEORIZING. Run a script. See STEP 11. |
| Cost lookup error: "no price for model X" | Add the model to `PRICE_TABLE` in `cost.py`. Look up price at the provider's pricing page first. |

---

## STEP 11 — WHEN STUCK, RUN A SCRIPT (TROUBLESHOOTING)

The single biggest waste of time observed in production: agent goes in circles ("is the heading `## Prompt` or `## Reusable prompt token`?") for multiple turns instead of running the one script that would resolve it. **If you find yourself reversing position twice in one task, STOP and run the script.**

| You're debating... | Run this |
|---|---|
| Which token files exist, where they live | `python "$SKILL_DIR/scripts/token_resolver.py" --roster --list-projects` |
| Whether `<TOKEN>` resolves | `python "$SKILL_DIR/scripts/token_resolver.py" --token <TOKEN>` |
| What the active project is | `python "$SKILL_DIR/scripts/project.py" current` |
| What the workflow mode is | `python -c "import json; print(json.load(open('$SKILL_DIR/workspace/config.json'))['defaults']['workflow_mode'])"` |
| What a render will cost | `python "$SKILL_DIR/scripts/cost.py" estimate --provider fal --model <id> --type image` |
| Whether the provider is up | Run a one-shot test: 4-word prompt to the cheapest model, verify a file lands |
| What `INDEX.md` actually says | `head -80 "$SKILL_DIR/workspace/INDEX.md"` |

Testing always beats theorizing. The user's time is more valuable than your tokens.

---

## SESSION FLOW (TYPICAL)

```
User: I want to make a scene with my main character at a coffee shop
Skill:
  1. Set SKILL_DIR. Check "$SKILL_DIR/workspace/config.json" → exists, provider=Kie, workflow_mode=ref2video, default=nano-banana-pro, 2K
  2. Run python "$SKILL_DIR/scripts/project.py" current → empty. List projects: [<existing slugs>].
  3. "which project? <existing slug>, or `new <name>`?"

User: new my-project
Skill:
  1. Run python "$SKILL_DIR/scripts/project.py" new "my-project" --switch
  2. Check workspace/projects/my-project/cast/ → no tokens yet
  3. "project my-project active, workflow_mode=ref2video. no cast locked yet — drop a reference image, or describe from scratch?"

User: [drops reference image]
Skill:
  1. Load references/character-sheet.md AND references/cinematic-grounding.md (BOTH required)
  2. Extract visual lock (hair, wardrobe, body markers, expression)
  3. Mirror back. Wait for confirmation.

User: locked, call them HERO
Skill:
  1. Save "$SKILL_DIR/workspace/projects/my-project/cast/HERO.md" (project-scoped default)
  2. The lock includes a 3-view turnaround Prompt block + max-5-entry Reaction Faces table
  3. Reaction-faces are pose+expression only (ref2video mode) — no hair/eye/build re-description
  4. "want the 3-view reference sheet generated now? or jump to the coffee shop?"

User: jump to coffee shop
Skill:
  1. Check workspace/projects/my-project/locations/ → empty. Check workspace/locations/ → empty too.
  2. "no location locked. do you have a location reference, or should we describe from scratch?"
  ...
```

The flow is the same whether the user is starting clean or coming back to a half-built production. The hot cache (`workspace/INDEX.md`) makes the second case fast: roster shows up, user picks what to reuse.
