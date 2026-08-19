---
title: M7 OmniRoute Free Routing — VERIFIED (run text/content free)
status: reference — tested 2026-08-16, not aspirational
gateway: http://127.0.0.1:20128/v1
brand: Blue #003299 + Yellow #ffdd17, zero green, "free roof inspection" OK (never free repairs/deductible), storm damage report not CPPA, IKO not GAF, founded 2021, (972) 928-0788
---

# 🔀 M7 OmniRoute Free Routing (verified working)

**What it is:** OmniRoute (`:20128`) is a keyless gateway to **177 models** — it auto-routes to the best free model, including premium ones. **Tested:** `auto/best-chat` returned a real answer routed to `claude-opus-4-6-thinking`, at **$0**. This is how you run text/content free and dodge the paid gates.

## ✅ The free stack (what actually costs nothing)
| Tool | How it's free |
|---|---|
| **OmniRoute** `:20128` | 177 models, keyless pool — routes to premium models free |
| **Free Claude Code (FCC)** `:8082` | already routes through OmniRoute (`OMNIROUTE_MODEL=auto/best-coding`) |
| **Hermes** | OpenRouter free models (verified — wrote a real blog) |
| **OmniRoute smart routers** | `auto/best-chat` (writing) · `auto/best-coding` (code) · `auto/best-reasoning` (hard) · `auto/best-vision` |

## 🖥️ Use it directly (any dummy key works)
```bash
curl http://127.0.0.1:20128/v1/chat/completions -H "Authorization: Bearer sk-free" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto/best-chat","messages":[{"role":"user","content":"Write a Frisco roofing GBP post, brand law, save nothing"}]}'
```
Point any OpenAI-compatible tool at `http://127.0.0.1:20128/v1` with any dummy key → free.

## ⚠️ DO NOT do this (the Julian doc's dangerous step)
The handoff doc says to set **`ANTHROPIC_BASE_URL`** globally to the gateway. **DON'T.** That would hijack your **real Claude subscription** (Claude tab, jcode, video editor) and route it through free models — breaking your best tool. Route **per-tool** (FCC already does), never globally. *(Verified: it's currently NOT set — keep it that way.)*

## 💸 Still paid (skip — not needed)
GLM (needs paid Ollama sub — 403), MiniMax image/video (Token Plan), Grok (X Premium+), Higgsfield/HeyGen. **Image/video GENERATION has no free path.** Use your **39GB of real drone/roof footage** for visuals — better than AI for a roofer anyway.

## 🎯 Bottom line
**Text + content + code = FREE** (OmniRoute + FCC + Hermes/OpenRouter). **Image/video gen = paid, and you don't need it.** Run the business on the free text stack; use real footage for visuals.

<!-- M7-FIREWALL-EXEMPT: routing reference -->
