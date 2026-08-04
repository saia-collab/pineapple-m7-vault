---
type: onboarding
title: M7 Mission Control — Onboarding Cheat Sheet (for the team)
status: active
last_updated: 2026-07-13
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🍍 M7 Mission Control — Onboarding Cheat Sheet

**Open the command center: http://localhost:3000. To start everything: double-click
`LAUNCH_ALL.bat`. That's the whole daily on-ramp.**

---

## 🗺️ 1. What the left sidebar is (two kinds of tabs)

**A. AGENTS = different AI "brains" (CLIs).** Same job (help you build/write), different
engine. You rarely need more than a couple:
| Agent | Use it for | Cost |
|---|---|---|
| **Hermes** ⭐ | THE workhorse. Writes SEO pages, captions, SOPs via Goal Mode | free |
| **Claude** | General help, code | plan |
| OpenClaw / Codex / Kimi / GLM / Grok Build / Antigravity | Alt coding brains — optional | varies |

**B. STUDIO / FEATURES = tools that DO a thing:**
| Tab | What it does |
|---|---|
| **OpenSEO** ⭐ | Your ranking data (Search Console) — what to write next |
| **Video Editor** ⭐ | Turn raw job clips into polished captioned reels |
| **Generate / Deploy** | Make SEO drafts → publish them |
| **Thumbnails / Music / OpenMontage** | YouTube thumbnails, audio, montages |
| **Astros** | 24/7 YouTube competitor topic watcher (needs Grok login — see §6) |
| **Memory / Notebook / Kanban** | Shared brain, notes, task board |

**Golden rule:** you mostly live in **OpenSEO → Hermes → Deploy**, plus **Video Editor**
for reels. Ignore the rest until you need it.

---

## 🔁 2. The SEO workflow (the money loop)
Full version: `M7_SEO_LSA_SOP.md`. Short version:
1. **OpenSEO → Search Performance → Striking distance** = keywords we ALMOST rank for.
2. **Hermes → Goal Mode** writes/upgrades the page (free). Lands in **Outbox_Drafts/**.
3. **You review** the draft in Outbox → approve.
4. **Deploy tab** → pushes it live.
5. Watch the position climb next week. Repeat.

---

## 🚀 3. What "Netlify deploy" means (the Deploy tab)
The Deploy tab runs two commands:
- `npx @11ty/eleventy` → **builds** your Markdown SEO posts into a real website (HTML) in a `_site` folder.
- `netlify deploy --prod --dir=_site` → **publishes** that website LIVE on the internet.

**Netlify** = a free web host (like a landlord for your website). "Make sure your sites
are linked" = the folder must be connected to your Netlify account first
(`netlify login` + `netlify link`, done once). **Deploying = going public**, so only
hit Deploy after you've approved the drafts.

---

## 🎬 4. The Video Editor tab (for marketing reels)
Turn raw roofing footage into post-ready clips — locally, free (uses FFmpeg):
1. **Upload video** (a raw job clip / drone shot).
2. Pick a **brief**: *Tighten + captions*, *Rough cut → polished*, *60s highlight*, or *Captions only*.
3. Hit **Edit this video** → outputs `edit/final.mp4` (playable + downloadable).
4. That polished clip → post it (see §5).

Use it to cut dead air, add bold captions, make a 60-sec highlight for Reels/TikTok/Shorts.

---

## 📦 5. The 39GB media (Google Drive) → posting
The raw reels/photos live on Google Drive. The path to get them POSTED:
1. **Pull the clip** you want (Drive) → optionally polish it in the **Video Editor** (§4).
2. **Post via Blotato** — the social scheduler wired into the OS. It pushes one clip to
   IG / TikTok / FB / YouTube at once, on a schedule.
3. Caption comes from **Hermes** (brand voice, CPPA/IKO, zero green) → Outbox → approve → schedule.

> Honest note: Blotato posting needs your Blotato account connected, and posting is a
> "GO" action (it goes public) — drafts stay PAUSED until you approve. We don't bulk-post
> 39GB blindly; we pick the best clips and schedule them.

---

## 🛰️ 6. Astros → Hermes (competitor watcher)
Astros scans competitors' YouTube 24/7 and hands you trending topics + titles. It needs
Hermes signed into **xAI Grok**, which requires a **SuperGrok or X Premium+** subscription:
```
hermes auth add xai-oauth
```
- **Have X Premium+ / SuperGrok?** Run that once → Astros lights up.
- **Don't have it?** Skip Astros — it's a nice-to-have, not required for SEO or posting.

---

## 🧠 7. Free local models (so it all costs ~$0)
Hermes and the agents run on **free models** (Groq, OmniRoute's 92 free models, local
Ollama) — that's how content/SEO/SOP work costs nothing. Voice is free too (browser +
`M7_JARVIS_VOICE.md`). The only paid extras are optional: DataForSEO (keyword volumes),
Grok (Astros), and any ad spend (LSA).

---

## ✅ Brother's Day-1 checklist
1. Double-click **LAUNCH_ALL.bat** → open **localhost:3000**.
2. Read this sheet + `M7_SEO_LSA_SOP.md`.
3. Open **OpenSEO → Search Performance** → see our live rankings.
4. Try one **Hermes Goal Mode** task (paste an SEO goal from the SOP).
5. Everything the AI makes lands in **Outbox_Drafts/** — you approve before it's live.

**The 5 rules never change:** Outbox Shield (nothing goes live without GO) · never delete/
restructure · brand lexicon (CPPA/IKO/Pineapple Standard, zero green) · verify don't
guess · run the brand firewall before staging.

<!-- M7-FIREWALL-EXEMPT: onboarding -->
