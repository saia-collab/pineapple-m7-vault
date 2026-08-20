---
title: PM7 OmniRoute Backoffice Configuration & Verification Cheat Sheet
status: ACTIVE_GUIDE
canonical_root: C:\Pineapple Contractors M7
gateway: http://127.0.0.1:20128/v1
brand_law: Blue #003299 + Yellow #ffdd17 | Zero-Green | CTA "free roof inspection" ALLOWED | Field Copy "storm damage report" (CPPA internal only) | IKO Certified (never GAF) | RCAT #03-0637 | Outbox Shield PAUSED
verified: 2026-08-19 — auto/best-chat routed live at $0 (model "big-pickle"); CORS allows local pages
---

<!-- M7-FIREWALL-EXEMPT: config/tooling cheat sheet — names providers, model IDs, and the rule lexicon verbatim; no marketing output. -->

# 🍍 OmniRoute Backoffice Master Configuration Cheat Sheet

**Purpose:** step-by-step guide to eliminate OmniRoute errors, fix OpenRouter 401s, set up combos, map aliases, and lock Cursor / Codex / Free Claude Code / Hermes into the $0 local proxy.

## ⚙️ STEP 1 — Settings & Feature Flags (`:20128/settings`)
| Setting | Value | Purpose |
|---|---|---|
| Allow Private / Local Provider URLs | ON | Lets OmniRoute reach local Ollama on `http://localhost:11434` |
| RTK Token Compression | ON | Compresses context up to ~95% to stay in free rate limits |
| Auto-Failover Retries | 3 | Retries the next model in the combo on a temporary rate limit |
| Default Model Alias | `auto/best-chat` | Universal smart router for writing/marketing copy |

## 🔌 STEP 2 — Providers (`:20128/providers`)
**2.1 Fix OpenRouter 401:** Providers → OpenRouter → paste key from openrouter.ai/keys (no leading/trailing spaces) → toggle **"Free Models Only"** (`:free`) if you have no credits → **Save & Test** (status: **200 OK / healthy**).
**2.2 Ollama (local):** Add Provider → Ollama → Base URL `http://localhost:11434`, key `ollama` (dummy) → Test & Save. *(Only works if you've re-installed Ollama + pulled models; you removed local models for memory — this is optional.)*
**2.3 Free cloud:** add Groq (`https://api.groq.com/openai/v1`, free tier). OpenCode Zen / Z.ai are optional. **Note: GLM / Z.ai deep models may require a paid plan** (GLM via Ollama Cloud returned 403 here).

## 🔀 STEP 3 — Combos (`:20128/combos`) — currently 0
Create a fallback chain (**note: `auto/best-chat` already auto-fails-over with no setup — a combo is optional**):
- Name: **`pm7-free`**
- Primary: `deepseek-v4-flash-free` (or `openrouter/deepseek/deepseek-r1:free`)
- Fallback 1: `groq/llama-3.3-70b-versatile`
- Fallback 2 (optional, local): `gemma2:9b` via Ollama

## 🏷️ STEP 4 — Model Aliases (`:20128/aliases`)
Map frontend-requested model IDs → your free target so tools never bypass OmniRoute or 404:
| Requested model ID | Redirect → | Tool |
|---|---|---|
| `claude-3-7-sonnet-*` / `claude-3-5-sonnet-*` / `claude-3-opus-*` | `auto/best-chat` (or `pm7-free`) | Claude Code / FCC / Cursor |
| `gpt-4o` / `gpt-4o-mini` | `auto/best-chat` | Cursor / Codex |
| `zmf/deepseek/deepseek-chat` | `oc/deepseek-v4-flash-free` | Hermes |

## 💻 STEP 5 — CLI / Frontend Connection
```powershell
# Free Claude Code (FCC)
$env:ANTHROPIC_BASE_URL="http://127.0.0.1:20128"; $env:ANTHROPIC_API_KEY="sk-pm7-free-local-token"; claude
# Codex
codex config set base_url http://127.0.0.1:20128/v1 ; codex config set api_key sk-pm7-free-local-token
```
Cursor → `.cursor/settings.json`: `{ "openai.baseUrl": "http://127.0.0.1:20128/v1", "openai.apiKey": "sk-pm7-free-local-token" }`
**Hermes** → use `oc/deepseek-v4-flash-free` as the default. ⚠️ **Correction:** `auto/best-chat` returned EMPTY streams inside Hermes here — `oc/deepseek-v4-flash-free` is the one verified working:
```
hermes config set model.base_url http://127.0.0.1:20128/v1
hermes config set model.default oc/deepseek-v4-flash-free
```

## 🧪 STEP 6 — Verification (PowerShell PASS test)
```powershell
$Uri="http://127.0.0.1:20128/v1/chat/completions"
$Headers=@{ "Authorization"="Bearer sk-pm7-free-local-token"; "Content-Type"="application/json" }
$Body=@{ model="auto/best-chat"; messages=@(@{ role="user"; content="Confirm PM7 OmniRoute free routing is live in 1 sentence." }) } | ConvertTo-Json
try { $r=Invoke-RestMethod -Uri $Uri -Method Post -Headers $Headers -Body $Body -TimeoutSec 15
  Write-Host "[PASS] OmniRoute free routing live:" $r.choices[0].message.content -ForegroundColor Yellow
} catch { Write-Host "[FAIL] $_" -ForegroundColor Red }
```
