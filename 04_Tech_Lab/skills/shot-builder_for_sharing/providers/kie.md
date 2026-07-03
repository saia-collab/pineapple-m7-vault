# Kie.ai — Provider Catalog

How the skill talks to Kie.ai. Kie is a unified aggregator over 100+ generative models — cheaper than official APIs, all asynchronous, all behind one task-and-poll pattern.


---

## AUTH

| Setting | Value |
|---|---|
| **Header** | `Authorization: Bearer <KIE_API_KEY>` |
| **Key env var** | `KIE_API_KEY` |
| **Default key location** | `~/.shot-builder/.env` |
| **Sign-up** | https://kie.ai/ |
| **Generate key** | https://kie.ai/api-key |
| **Base URL** | `https://api.kie.ai` |

Key reads in this order:
1. `process.env.KIE_API_KEY`
2. `<state_dir>/.env` → `KIE_API_KEY=`
3. `~/.shot-builder/.env` → `KIE_API_KEY=`

---

## THE TASK PATTERN (UNIVERSAL)

**Every Kie operation is async.** HTTP 200 means "queued," not "completed." Always poll.

```bash
# Step 1 — submit task
curl -X POST "https://api.kie.ai/api/v1/jobs/createTask" \
  -H "Authorization: Bearer $KIE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nano-banana-pro",
    "prompt": "...",
    "resolution": "2k"
  }'

# → { "data": { "taskId": "abc123" } }

# Step 2 — poll
curl "https://api.kie.ai/api/v1/jobs/recordInfo?taskId=abc123" \
  -H "Authorization: Bearer $KIE_API_KEY"

# Status: pending → processing → completed | failed

# Step 3 — when completed, the response includes the result URL
# { "data": { "status": "completed", "result": { "url": "https://..." } } }
```

Poll interval recommendations:
- Image: 2s
- Video: 5s
- Music: 3s

Timeout caps (skill defaults):
- Image: 120s
- Video: 300s (5min)
- Music: 240s

---

## IMAGE MODELS

| Model ID | Strengths | Cost |
|---|---|---|
| `nano-banana-pro` | Best text rendering, character consistency, Gemini 3 Pro under hood | $0.02-0.05 |
| `nano-banana-basic` | Cheaper iteration version | $0.01-0.03 |
| `flux-2` | Up to 4MP, multi-reference (8 images), advanced editing | $0.03-0.08 |
| `4o-image` | GPT-Image native, strong instruction following | $0.04-0.10 |
| `ideogram-v2` | Text rendering | $0.05-0.10 |

### Nano Banana Pro params

| Field | Type | Default | Notes |
|---|---|---|---|
| `model` | string | — | `nano-banana-pro` |
| `prompt` | string | — | Required |
| `resolution` | enum | `2k` | `1k`, `2k`, `4k` |
| `aspectRatio` | string | `16:9` | `16:9`, `9:16`, `4:5`, `2.39:1`, `1:1` |
| `referenceImages` | array | — | Up to 8 URLs for image-to-image |
| `seed` | int | random | Lock for iteration |

### Flux 2 params

| Field | Type | Default | Notes |
|---|---|---|---|
| `model` | string | — | `flux-2` |
| `prompt` | string | — | Required. English by default |
| `width` | int | 1024 | Up to 4MP total |
| `height` | int | 1024 | — |
| `enableTranslation` | bool | false | Set true for non-English prompts |
| `referenceImages` | array | — | Up to 8 URLs |
| `seed` | int | random | — |

---

## VIDEO MODELS

| Model ID | Strengths | Cost |
|---|---|---|
| `kling-2.6` | Native audio sync (dialogue, narration, music, SFX), 5-10s | $0.28-1.10 |
| `veo-3.1` | High fidelity, audio | $0.50-2.00 |
| `runway` | Director controls | $0.40-1.50 |
| `sora-2` | Bleeding edge motion | $0.60-2.50 |

### Kling 2.6 params

| Field | Type | Default | Notes |
|---|---|---|---|
| `model` | string | — | `kling-2.6` |
| `prompt` | string | — | Required |
| `imageUrl` | string | — | Optional reference for image-to-video |
| `duration` | int | 5 | 5 or 10 seconds |
| `withAudio` | bool | false | Native audio sync |
| `audioType` | enum | — | `dialogue`, `narration`, `music`, `sfx` (when withAudio=true) |
| `language` | string | `en` | `en`, `zh` (for dialogue/narration) |
| `aspectRatio` | string | `16:9` | `16:9`, `9:16`, `1:1` |

---

## AUDIO / MUSIC MODELS

| Model ID | Use |
|---|---|
| `suno-v5` | Music generation, 30-180s, stems available |
| `elevenlabs` | TTS, voice cloning |

---

## REFERENCE IMAGES

Kie's `referenceImages` field expects public URLs. Local images need to be uploaded first. Kie does not provide a hosted upload endpoint — the skill uploads to FAL's storage CDN (Complimentary tier works) or any S3-compatible bucket, then passes the URL to Kie.

Alternative: convert local image to base64 data URL and pass directly (some Kie endpoints accept this, some don't — check per-endpoint).

---

## CREDIT SYSTEM

- 1 credit ≈ $0.005 USD
- Check balance: `GET /api/v1/chat/credit`

```bash
curl "https://api.kie.ai/api/v1/chat/credit" \
  -H "Authorization: Bearer $KIE_API_KEY"
```

The skill logs estimated cost per generation in `workspace/INDEX.md` recent-renders block. Refresh balance once per session and warn user if credits run low.

---

## RATE LIMITS

| Constraint | Limit |
|---|---|
| Request rate | 20 requests per 10 seconds |
| 429 response | REJECTED, not queued — implement exponential backoff |
| Concurrent tasks | 100+ supported |
| File retention | 14 days |

The skill enforces a soft cap of 15 req/10s to leave headroom.

---

## FILE RETENTION (CRITICAL)

**Generated files expire after 14 days.** The skill must:
1. Download every artifact immediately when status=completed
2. Save locally to `workspace/shots/<date>/` or `workspace/scenes/<date>/`
3. Save to the configured `output_dir` for end-user access
4. Update `workspace/INDEX.md` with the local path, NOT the Kie URL

Never trust a Kie URL for anything more than the first download.

---

## ERROR HANDLING

| HTTP | Meaning | Skill response |
|---|---|---|
| 401 | Invalid API key | Re-run setup gate |
| 400 | Invalid params | Surface error, ask user to adjust |
| 429 | Rate limited (REJECTED) | Exponential backoff (2s, 4s, 8s, 16s), 4 retries max |
| 500 | Server error | Retry once, then surface |
| Task status `failed` | Generation failed | Read error message, suggest fix, do not auto-retry silently |
| Task status hangs >timeout | Network or queue issue | Cancel client-side, offer FAL fallback |

---

## WEBHOOK ALTERNATIVE (NOT USED BY DEFAULT)

Kie supports webhooks via `callbackUrl` in the create-task request — eliminates polling. Skill does not use this by default (no public webhook receiver in shot-builder's local execution model). If user has a public webhook endpoint, they can configure it in `config.json` and the skill will use it instead of polling.

---

## GOTCHAS

| Issue | Fix |
|---|---|
| HTTP 200 misread as "done" | ALWAYS poll. 200 = queued, never = completed |
| Files expire after 14 days | Download immediately, store local path in INDEX.md |
| Flux 2 only accepts English by default | Set `enableTranslation: true` for non-English prompts |
| Suno `vocalGender` is probabilistic | May not deliver exact gender, run multiple generations if critical |
| Kling complex dialogue lags audio | Keep dialogue lines short, test before production |
| Task hangs >5min on video | Cancel, retry once, then surface to user |
| 429 means REJECTED not queued | Backoff and retry, don't assume retry-after header is correct |
| Lower stability than official APIs | Implement retry logic + offer FAL fallback |
| Webhook signature verification | If using webhooks, verify HMAC signature before processing |
| Concurrent tasks > 100 hit rate limit | Use internal queue if doing bulk |

---

## DISCOVERABILITY

Kie's model catalog: https://kie.ai/market. No API list endpoint — catalog is browsed manually. When new models drop, update `defaults.md` and this file.

---

## REFERENCES

- Website: https://kie.ai/
- API docs: https://docs.kie.ai/
- API keys: https://kie.ai/api-key
- Models market: https://kie.ai/market
- Pricing: https://kie.ai/pricing
