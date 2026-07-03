# FAL.ai — Provider Catalog

How the skill talks to FAL.ai. Endpoint catalog, auth pattern, request/response shapes, polling for queue endpoints, error handling.

---

## AUTH

| Setting | Value |
|---|---|
| **Header** | `Authorization: Key <FAL_API_KEY>` |
| **Key env var (preferred)** | `FAL_KEY` |
| **Key env var (alt)** | `FAL_API_KEY` |
| **Default key location** | `~/.shot-builder/.env` |
| **Sign-up** | https://fal.ai/dashboard |
| **Generate key** | https://fal.ai/dashboard/keys |

Key reads in this order:
1. `process.env.FAL_KEY`
2. `process.env.FAL_API_KEY`
3. `<state_dir>/.env` → `FAL_KEY=`
4. `~/.shot-builder/.env` → `FAL_KEY=`

---

## ENDPOINT FORMAT

```
https://fal.run/<endpoint_id>                  # sync call (image, fast inference)
https://queue.fal.run/<endpoint_id>            # queue-based call (video, long-running)
https://queue.fal.run/<endpoint_id>/requests/<request_id>/status   # poll status
https://queue.fal.run/<endpoint_id>/requests/<request_id>          # fetch result
```

`<endpoint_id>` is always `fal-ai/<model>` or `fal-ai/<vendor>/<model>/<variant>`.

---

## SYNC PATTERN (FAST IMAGE INFERENCE)

POST a single request, get the result back in the response (typically 5-30s).

```bash
curl -X POST "https://fal.run/fal-ai/flux-pro/v1.1-ultra" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "...",
    "image_size": "landscape_16_9",
    "num_images": 1,
    "enable_safety_checker": false
  }'
```

Response (image generation):
```json
{
  "images": [
    {
      "url": "https://v3.fal.media/files/.../image.png",
      "width": 1920,
      "height": 1080,
      "content_type": "image/png"
    }
  ],
  "timings": { "inference": 4.2 },
  "seed": 12345,
  "has_nsfw_concepts": [false],
  "prompt": "...echoed..."
}
```

**Critical:** image URLs expire — download immediately.

---

## QUEUE PATTERN (VIDEO, LONG INFERENCE)

POST creates a request, returns a request_id. Poll status until done. Fetch result.

```bash
# Step 1 — submit
curl -X POST "https://queue.fal.run/fal-ai/kling-video/v2.1/master" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "prompt": "...", "image_url": "https://...", "duration": "5" }'

# → returns: { "request_id": "abc123", "status": "IN_QUEUE", ... }

# Step 2 — poll
curl "https://queue.fal.run/fal-ai/kling-video/v2.1/master/requests/abc123/status" \
  -H "Authorization: Key $FAL_KEY"

# Status values: IN_QUEUE → IN_PROGRESS → COMPLETED | FAILED

# Step 3 — fetch result (only when COMPLETED)
curl "https://queue.fal.run/fal-ai/kling-video/v2.1/master/requests/abc123" \
  -H "Authorization: Key $FAL_KEY"

# → returns the model's output (video URL, etc.)
```

Recommended poll interval: 3s for video. Timeout cap: 300s (5min).

---

## IMAGE MODELS — CURATED

| Endpoint | Aliases | Strengths | Cost |
|---|---|---|---|
| `fal-ai/flux-pro/v1.1-ultra` | Flux Pro Ultra | Best general image, prompt adherence, photorealism | $0.05 |
| `fal-ai/flux-pro/v1.1` | Flux Pro | Faster, slightly lower fidelity | $0.04 |
| `fal-ai/flux/dev` | Flux Dev | Cheap iteration | $0.025 |
| `fal-ai/flux/schnell` | Flux Schnell | Fastest, lowest fidelity | $0.003 |
| `fal-ai/flux-pro/kontext` | Flux Kontext | Reference-image editing, in-context image-to-image | $0.05 |
| `fal-ai/recraft-v3` | Recraft v3 | Brand-clean, vector-friendly | $0.04 |
| `fal-ai/ideogram/v3` | Ideogram v3 | Strong text rendering in image | $0.08 |
| `fal-ai/bytedance/seedream/v5/lite` | Seedream Lite | Cheap high-volume image | $0.02 |
| `fal-ai/bytedance/seedream/v5/lite/edit` | Seedream Edit | Image-to-image edit | $0.025 |
| `fal-ai/imagineart/imagineart-2.0-preview/text-to-image` | ImagineArt | Editorial, stylized | $0.03 |

---

## VIDEO MODELS — CURATED

| Endpoint | Aliases | Strengths | Cost |
|---|---|---|---|
| `fal-ai/kling-video/v2.1/master` | Kling 2.1 | Strong motion, image-to-video | $0.28-1.10 |
| `fal-ai/kling-video/v3/pro/image-to-video` | Kling 3 Pro | Higher fidelity, native motion control | $0.50-1.50 |
| `fal-ai/bytedance/seedance/v1/pro/image-to-video` | Seedance Pro | Cinematic motion, anamorphic feel | $0.30-0.80 |
| `fal-ai/bytedance/seedance-2.0/image-to-video` | Seedance 2.0 | Latest motion model | $0.40-1.00 |
| `fal-ai/veo-3` | Veo 3 | Native audio, high fidelity | $0.50-2.00 |
| `fal-ai/runway-gen3/turbo/image-to-video` | Runway Gen-3 Turbo | Director controls | $0.40-1.50 |

---

## AUDIO MODELS

| Endpoint | Use |
|---|---|
| `fal-ai/elevenlabs/tts/multilingual-v2` | TTS |
| `fal-ai/elevenlabs/sound-effects` | Diegetic sound effect generation |

---

## UTILITY ENDPOINTS

| Endpoint | Use |
|---|---|
| `fal-ai/aura-sr` | Image upscale 4x |
| `fal-ai/clarity-upscaler` | Detail upscale |
| `fal-ai/face-restoration` | Face cleanup |
| `fal-ai/birefnet` | Background removal |
| `fal-ai/bria/background/replace` | Background replacement |
| `fal-ai/florence-2-large` | Image captioning / analysis |

---

## INPUT FIELDS (FLUX PRO 1.1 ULTRA)

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Required. Up to ~1500 tokens reliable |
| `image_size` | enum | `landscape_16_9` | `square_hd`, `square`, `portrait_4_3`, `portrait_16_9`, `landscape_4_3`, `landscape_16_9`. Custom via `{width, height}` object |
| `num_images` | int | 1 | 1-4 |
| `safety_tolerance` | int | 2 | 1 (strictest) - 6 (permissive) |
| `output_format` | enum | `jpeg` | `jpeg` or `png` |
| `aspect_ratio` | enum | — | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `9:21`. Overrides `image_size` |
| `enable_safety_checker` | bool | true | Set false for production runs |
| `raw` | bool | false | If true, less stylized output |
| `seed` | int | random | Lock for iteration |

---

## INPUT FIELDS (KLING V2.1 MASTER)

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string | — | Required |
| `image_url` | string | — | Required for image-to-video |
| `duration` | enum | `5` | `5` or `10` (seconds) |
| `negative_prompt` | string | — | Optional |
| `cfg_scale` | float | 0.5 | Prompt adherence |
| `aspect_ratio` | enum | `16:9` | `16:9`, `9:16`, `1:1` |

---

## REFERENCE IMAGES (IMAGE-TO-IMAGE, VIDEO)

FAL endpoints that accept a reference image take `image_url` (single) or `image_urls` (array). Image URLs must be publicly accessible. The skill uploads local images to FAL's CDN first via:

```bash
curl -X POST "https://fal.run/storage/upload" \
  -H "Authorization: Key $FAL_KEY" \
  -F "file=@/path/to/local.png"

# → returns: { "url": "https://fal.media/files/.../local.png" }
```

That returned URL goes into the model's `image_url` field.

---

## RATE LIMITS

| Constraint | Limit |
|---|---|
| Without API key | Very low (public list endpoint only) |
| With API key | High — practically unlimited for paid usage |
| Concurrent jobs | 5-10 typical, scales with account |
| 429 response | Implement exponential backoff (skill does 2s, 4s, 8s, 16s, then surfaces) |

---

## ERROR HANDLING

| HTTP | Meaning | Skill response |
|---|---|---|
| 401 | Invalid key | Re-run setup gate |
| 422 | Validation error | Surface error message to user, ask for fix |
| 429 | Rate limit | Backoff, then retry up to 4 times |
| 500 | FAL server error | Retry once, then surface |
| 524 | Cloudflare timeout | Switch to queue endpoint, retry |

---

## DISCOVERABILITY

To list all available FAL models (useful for finding new endpoints):

```bash
curl "https://api.fal.ai/v1/models?limit=100" \
  -H "Authorization: Key $FAL_KEY"
```

Returns paginated list with endpoint_id, display_name, category, description, status. The skill can sync this catalog into `workspace/INDEX.md` under "Available models" on user request.

---

## GOTCHAS

| Issue | Fix |
|---|---|
| Image URL 404s after a day | Download immediately on COMPLETED, never trust the URL long-term |
| `safety_tolerance` blocking valid prompts | Drop to 4-5 if no real safety issue |
| `image_size` ignored when `aspect_ratio` is set | Pick one, don't send both |
| Kling expects `image_url`, you sent `image_urls` | Field names matter — check schema per endpoint |
| LLM endpoints (`anthropic/`, `openai/`, etc.) follow different schema | Skill treats them separately, not used for image/video gen |
| Sync endpoint hits 524 on slow inference | Switch to queue endpoint with same endpoint_id |
| Streaming response not parsed | FAL supports SSE streaming via `?stream=true` — only used for LLM passthroughs, not image/video |
| Cost surprise | Always check `pricing` field on the endpoint's API page; some models charge per second of video |

---

## REFERENCES

- Dashboard: https://fal.ai/dashboard
- Model catalog: https://fal.ai/models
- API docs: https://docs.fal.ai
- Pricing: https://fal.ai/pricing
- Status page: https://status.fal.ai
