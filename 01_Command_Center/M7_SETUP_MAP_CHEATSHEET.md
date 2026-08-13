---
type: setup_map_cheatsheet
title: M7 SETUP MAP — "Where do I do this?" (install, keys, IDEs, models, clones)
status: active
date: 2026-08-13
note: Internal ops doc. "free" here = free-tier AI models, not customer wording.
---

# 🗺️ M7 SETUP MAP — "WHERE DO I DO THIS?"
For when you don't know *where* to run/install/wire something. You almost never need a terminal — the Studio has buttons for most of it.

---

## 🟢 THE ONE RULE
**Start here every day:** double-click **`START PINEAPPLE STUDIO.bat`** on your Desktop. It opens everything at `localhost:3737`. Never double-click a `.ps1` file — that just opens Notepad. Only `.bat` files run.

---

## 🤖 "WAKE UP AN AI AGENT"
- Studio → **Hermes** → **Chat** → tap a profile pill (`roofing`, `seo`, `muse`, `n2`…). Tapping = waking that agent.
- That's it. No terminal.

---

## 🔑 WHERE API KEYS / MODELS GET WIRED (the confusing part — 3 places)
| You want to… | Where | How |
|---|---|---|
| Change **free** coding model | `localhost:8082/admin` (Free Claude Code panel) | dropdown + paste, click Apply |
| Add a **paid** model (GLM/Kimi/Grok) to an agent | Studio → **Hermes → Manage** → the profile | paste key in the box |
| Connect a provider to **OmniRoute** free pool | `localhost:20128` → Providers | click (optional) |

You do **not** edit files for any of this — all point-and-click. (The files behind them: `~/.fcc/.env`, `%LOCALAPPDATA%\hermes\profiles\<name>\.env`. Don't touch unless I tell you.)

---

## 💻 THE IDEs / CODING TOOLS — what each is for
| Tool | Use it for | Where |
|---|---|---|
| **Studio (3737)** | your hub — chat, SEO, content, everything | browser (the .bat) |
| **VS Code** | look at files, run a terminal when needed | desktop app |
| **Antigravity** | Google's agent-IDE — build a whole app by asking | desktop app |
| **Codex** | OpenAI's coder (your ChatGPT login) | Studio → Codex tab |
| **opencode** | free open-source coder | Studio → opencode tab |
| **Free Claude Code** | free `claude` (Groq) | Studio → Free Claude Code tab / terminal |

**Rule of thumb:** stay in the **Studio**. Open VS Code only when I hand you a terminal command.

---

## 📦 INSTALL SOMETHING or CLONE FROM GITHUB — where
- **Terminal = VS Code → top menu → Terminal → New Terminal** (or Windows "PowerShell" from Start).
- Install a tool: `npm install -g <name>`
- Clone a repo: `git clone <url>`
- **You rarely need this.** If a guide says "install X," send it to me and I'll do it.

---

## 🧠 MODEL OPTIONS (free vs paid) — from the guides
| Model | Free? | How to use |
|---|---|---|
| **Groq** llama-3.3 | ✅ FREE | already your free default (Free Claude Code) |
| **N2** (Nex-N2-Pro, 262K) | ✅ FREE via OpenRouter | Hermes → tap the **n2** profile |
| **OmniRoute** pool | ✅ FREE (but often throttled) | Studio in-app free tab |
| **GLM 5.2** (z.ai) | ❌ PAID plan | Hermes **glm-5-2** profile + z.ai key (base `https://api.z.ai/api/coding/paas/v4`) |
| **Kimi K2.7** | ❌ PAID | Hermes **kimi** profile + Moonshot key |
| **Grok** | ❌ PAID (SuperGrok) | Hermes **grok-build** profile + xAI login |
| **Claude / gpt56** | your subscriptions | Studio **Claude** / **Codex** tabs — best for real work |

---

## ❓ "WHAT HAPPENED TO OPENROUTER?"
Still here, still used. **OpenRouter = one key (in Free Claude Code) that unlocks 300+ models**, including free ones and N2. It's a "one key, many models" cloud gateway.
- **OpenRouter** = the cloud key (in `~/.fcc/.env`).
- **OmniRoute** = a *local* router that tries free pools.
- Different things, both part of the setup. Keep OpenRouter — it's your backbone key.

---

## ❓ "DO I NEED TO KEEP ADDING THE ZIP PACKS?"
**No.** Here's the truth:
- The `agent-os-pack-*.zip` = the **Studio app itself** (the tabs/buttons). Download a new one **only when you want newer Studio features**, then run **`M7 UPDATE (new pack).bat`**. Maybe once a week, not daily.
- The zip does **NOT** touch your model keys or free-model wiring — those live in the `.env` files and survive every update.
- To *check* your config is right, run **`M7 HEALTH CHECK.bat`** — don't re-download zips to "verify." You don't need more videos/SOPs to confirm it works; the Health Check tells you.

---

## 🩹 IF IT BREAKS
1. `START PINEAPPLE STUDIO.bat` again (safe to re-click).
2. `M7 HEALTH CHECK.bat` to see what's up/down.
3. Screenshot + send me the black window if it pauses on an error.

<!-- M7-FIREWALL-EXEMPT: governance-reference (setup map; "free" = free-tier models) -->
