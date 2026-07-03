# Defaults — Resolutions, Models, Parameters

The values the skill defaults to when the user doesn't specify. Set during the setup gate, override per shot.

---

## RECOMMENDED DEFAULTS (NEW USER)

| Setting | Default | Reason |
|---|---|---|
| **Provider** | Kie.ai | 30-50% cheaper, larger model catalog, nano-banana-pro is excellent |
| **Image model** | `nano-banana-pro` (Kie) | Best text rendering, strong character consistency, Gemini 3 Pro under the hood |
| **Image resolution** | `2K` | Good detail without 4K cost. Bump to 4K for hero stills only. |
| **Image aspect** | `2.39:1` | Cinematic default. Override to `4:5` for portraits, `16:9` for standard, `9:16` for vertical. |
| **Video model** | `kling-2.6` (Kie) | Native audio sync, strong motion, $0.28-$1.10 per clip |
| **Video resolution** | `1080p` | Good detail without 4K cost |
| **Video aspect** | `16:9` | Standard cinematic. Override to `9:16` for vertical, `2.39:1` for ultra-wide. |
| **Video duration** | `5s` | Default ask if user doesn't specify. Never assume longer. |
| **Frame rate** | `24fps, 180° shutter` | Cinema standard |
| **Output dir** | `~/shot-builder-output/<YYYY-MM-DD>/` | Global, easy to find, easy to back up |
| **State dir** | `skills/shot-builder/workspace/` | Self-contained, gitignored except INDEX.md |
| **API key location** | `~/.shot-builder/.env` | Shared with shot-prompter and other skills |

---

## FAL.AI MODEL CATALOG (CURATED)

Full list lives in [../providers/fal.md](../providers/fal.md). These are the curated defaults:

### Image generation

| Model | Endpoint | Best for | Cost (approx) |
|---|---|---|---|
| **Flux Pro 1.1 Ultra** | `fal-ai/flux-pro/v1.1-ultra` | High-fidelity general image, strong prompt adherence | $0.05 / image |
| **Flux Pro 1.1** | `fal-ai/flux-pro/v1.1` | Faster Flux, slightly lower fidelity | $0.04 / image |
| **Flux Dev** | `fal-ai/flux/dev` | Cheap iteration, lower fidelity | $0.025 / image |
| **Flux Schnell** | `fal-ai/flux/schnell` | Fastest, lowest cost, lower fidelity | $0.003 / image |
| **Recraft v3** | `fal-ai/recraft-v3` | Brand-consistent, vector-clean | $0.04 / image |
| **Ideogram v2** | `fal-ai/ideogram/v2` | Strong text rendering in image | $0.08 / image |
| **Nano Banana Pro (FAL)** | `fal-ai/nano-banana-pro` (if available) | Same as Kie version | $0.05 / image |

### Video generation

| Model | Endpoint | Best for | Cost (approx) |
|---|---|---|---|
| **Kling 2.1** | `fal-ai/kling-video/v2.1/master` | Strong motion, image-to-video | $0.28-1.10 / clip |
| **Veo 3** | `fal-ai/veo-3` | Native audio, high fidelity | $0.50-2.00 / clip |
| **Seedance** | `fal-ai/bytedance/seedance/v1/pro/image-to-video` | Cinematic motion | $0.30-0.80 / clip |
| **Runway Gen-3** | `fal-ai/runway-gen3/turbo/image-to-video` | Strong director controls | $0.40-1.50 / clip |

---

## KIE.AI MODEL CATALOG (CURATED)

Full catalog in [../providers/kie.md](../providers/kie.md). Curated defaults:

### Image generation

| Model | Model ID | Best for | Cost (approx) |
|---|---|---|---|
| **Nano Banana Pro** | `nano-banana-pro` | Best text rendering, character consistency | $0.02-0.05 |
| **Nano Banana Basic** | `nano-banana-basic` | Cheaper iteration | $0.01-0.03 |
| **Flux 2** | `flux-2` | High-fidelity, multi-reference up to 8 | $0.03-0.08 |
| **4o Image** | `4o-image` | GPT-Image native, strong instruction following | $0.04-0.10 |

### Video generation

| Model | Model ID | Best for | Cost (approx) |
|---|---|---|---|
| **Kling 2.6** | `kling-2.6` | Native audio sync, dialogue + narration | $0.28-1.10 |
| **Veo 3.1** | `veo-3.1` | High fidelity, audio | $0.50-2.00 |
| **Runway** | `runway` | Director controls | $0.40-1.50 |
| **Sora 2** | `sora-2` | Bleeding edge motion | $0.60-2.50 |

### Audio/Music

| Model | Model ID | Use case |
|---|---|---|
| **Suno V5** | `suno-v5` | AI music generation |
| **ElevenLabs** | `elevenlabs` | TTS, voice cloning |

---

## RESOLUTION CHEAT SHEET

| Label | Width | Height | Common aspect |
|---|---|---|---|
| HD | 1280 | 720 | 16:9 |
| FHD / 1080p | 1920 | 1080 | 16:9 |
| 2K | 2048 | 1152 | 16:9 |
| 2K (square) | 2048 | 2048 | 1:1 |
| 2K (portrait) | 1152 | 2048 | 9:16 |
| 4K | 3840 | 2160 | 16:9 |
| Anamorphic 2.39:1 (2K) | 2048 | 858 | 2.39:1 |
| Anamorphic 2.39:1 (4K) | 3840 | 1608 | 2.39:1 |
| Portrait 4:5 (2K) | 1638 | 2048 | 4:5 |

The skill writes width/height into the API call. Aspect ratio is not in the prompt text.

---

## ASPECT RATIO PICKS

| Use case | Aspect | Why |
|---|---|---|
| Cinematic still / scene plate | 2.39:1 anamorphic | Cinema standard, dramatic horizon |
| Standard cinematic video | 16:9 | Widely compatible, YouTube default |
| Vertical content (Shorts, Reels, TikTok) | 9:16 | Mobile-first |
| Editorial portrait | 4:5 | Magazine, Instagram feed |
| Square (Instagram feed, profile) | 1:1 | Versatile |
| Character base on white seamless | 4:5 or 9:16 | Vertical favors full-body |
| 3x3 contact sheet master | 16:9 | Each panel becomes ~1.78:1 |
| 2x2 location grid master | 4:5 or 1:1 | Each panel ≈ 2.39:1 anamorphic |
| Ultra-wide environmental | 21:9 or 2.39:1 | Atmospheric, wide horizon |

---

## SEED + STRENGTH DEFAULTS

| Param | Default | When to override |
|---|---|---|
| **seed** | random | Lock seed when iterating on micro-tweaks of the same shot |
| **guidance_scale** (Flux) | 3.5 | Bump to 5-7 for strict prompt adherence, drop to 2-3 for more creative latitude |
| **num_inference_steps** | 28 (Flux Pro) | More steps = higher fidelity, slower. 50 for hero stills, 28 for iteration. |
| **strength** (image-to-image) | 0.75 | Lower (0.4-0.6) for closer to ref, higher (0.8-0.95) for more re-interpretation |
| **safety_tolerance** (Flux) | 2 | Stays default unless brand requires stricter |

---

## CONFIG.JSON SCHEMA

`workspace/config.json` after setup:

```json
{
  "version": "1.0",
  "created": "2026-05-21T18:00:00Z",
  "modified": "2026-05-21T18:00:00Z",
  "provider": {
    "primary": "kie",
    "fallback": "fal",
    "fal_key_path": "~/.shot-builder/.env",
    "kie_key_path": "~/.shot-builder/.env"
  },
  "defaults": {
    "image_model": "nano-banana-pro",
    "image_resolution": "2K",
    "image_aspect": "2.39:1",
    "video_model": "kling-2.6",
    "video_resolution": "1080p",
    "video_aspect": "16:9",
    "video_duration": 5,
    "frame_rate": "24fps_180shutter"
  },
  "paths": {
    "output_dir": "~/shot-builder-output",
    "state_dir": "~/.claude/skills/shot-builder/workspace"
  },
  "active_project": null,
  "default_style_token": null
}
```

---

## STANDARD NEGATIVE BASELINE

Applied to every prompt unless the user overrides. Don't make the user re-specify these per shot.

```
distorted faces, extra limbs, warped hands, low resolution, blurry, watermark, text overlay, cartoonish, plastic skin
```

**Scene-specific additions** (append to baseline when applicable):

| Scene type | Add |
|---|---|
| Emotional close-up | `no tears streaming, no telegraphed grief, no exaggerated facial movement` |
| Action / chase | `no slow-motion, no flying poses, no weightless bounce` |
| Driving | `no music-video swoops, no exterior drone shots` |
| Intimacy | `no kissing unless explicitly requested, no over-acted faces, no music-video lighting` |
| Empty location plate | `no people, no hands, no silhouettes, no characters of any kind` |
| Contact sheet / grid | `no text, no labels, no KF numbers, no captions, no panel borders with text` |
| Project-specific (per-token) | Any explicit negatives the token's gotchas enforce |
| Period / historical | `no modern technology, no digital displays, no contemporary clothing` |

---

## COST GATES

The skill stops and asks before spending if a render is expensive:

| Threshold | Action |
|---|---|
| Image, any cost | No gate — image renders are cheap ($0.01-$0.10) |
| Video preview (≤100 credits) | No gate — proceed |
| Video preview (>100 credits) | Confirm before submitting |
| Video hero (>200 credits) | Always confirm; default workflow is preview-then-hero |
| Batch (>5 video renders in one call) | Confirm batch as a whole |

After every render, the skill logs estimated cost to `INDEX.md` and to the session total. Run `python scripts/cost.py session` to see the running total.

---

## VIDEO RENDER TIERS (Always escalate, never skip)

The right workflow for any video render:

1. **Storyboard still** — 2K image. ~$0.04. Validates composition + characters + location.
2. **End-frame still** — 2K image. ~$0.04. Validates the destination shot, products, hero pose.
3. **Cheap preview video** — 480p, 5-8s. ~$0.20-0.50. Validates motion + pacing.
4. **Hero render video** — 1080p, full duration. ~$0.60-2.00. Final deliverable.

Skipping the storyboard or preview tier is the single most common way to burn credits unnecessarily. The skill enforces the escalation by default; the user can override with `"skip to hero"`.

---

## RESET / RE-RUN SETUP

If config is broken or user wants to switch defaults:

```bash
python ~/.claude/skills/shot-builder/scripts/setup.py --reset
```

This wipes config.json (keeps tokens and shots) and re-runs the setup gate.
