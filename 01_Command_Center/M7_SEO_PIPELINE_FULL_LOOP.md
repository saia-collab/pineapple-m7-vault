---
type: workflow
title: M7 SEO Pipeline — The Full Loop (Keyword → Lead → Repeat)
status: active
last_updated: 2026-07-15
---

# 🔄 M7 SEO Pipeline — The Full Loop

**The whole machine, step by step. Each step names the tool + the output.**
Everything runs in Local Studio (localhost:3000) + WordPress. Nothing needs Hermes specifically.

```
① RESEARCH → ② WRITE → ③ FIREWALL → ④ PUBLISH → ⑤ INDEX →
⑥ TRACK → ⑦ AMPLIFY → ⑧ CONVERT → ⑨ SPEED-TO-LEAD → ⑩ OPTIMIZE → (back to ①)
```

## ① RESEARCH — find what's almost ranking
- **Tool:** OpenSEO → **Search Performance → Striking distance**
- **Do:** pick keywords at position 5–20 with high impressions (e.g., "flat roofing allen tx" pos 8.6).
- **Output:** a keyword + the page it's tied to.

## ② WRITE — a page built to win that keyword
- **Tool:** **Me (Claude)** or the free-agent rotation (OmniRoute / GLM / Kimi / Local) — see the Fallback Chain
- **Do:** write a Location Service Page — AEO hook (answer in sentence 1), keyword H1, local landmarks, FAQ, CPPA CTA. Corey Haines format.
- **Output:** a brand-compliant `.md` in `Outbox_Drafts/Website_Pages/`.

## ③ FIREWALL — enforce brand law
- **Tool:** `python 04_Tech_Lab/scripts/brand_firewall.py --check <folder>`
- **Do:** confirm STATUS OK (no "free"/GAF/green). Free-model output ALWAYS gets this pass.
- **Output:** verified-clean page.

## ④ PUBLISH — push it live
- **Tool:** `python 04_Tech_Lab/scripts/wp_publish.py <file>.md pages` → then set status=publish + clean slug
- **Do:** page goes live on pineappleroofingllc.com (app-password API — agent-independent).
- **Output:** a live URL (200).

## ⑤ INDEX — get Google to see it
- **Tool:** **Yoast sitemap** (auto) + **Google Search Console** (via Site Kit)
- **Do:** Yoast adds the page to `/sitemap_index.xml`; GSC crawls it (days–weeks for a new site).
- **Output:** page indexed in Google.

## ⑥ TRACK — watch it climb
- **Tool:** **Site Kit** (in WordPress) + **OpenSEO** Search Performance
- **Do:** monitor the keyword's position weekly. Data fills in ~1–2 weeks after indexing.
- **Output:** position + impressions + clicks.

## ⑦ AMPLIFY — drive signals to the page
- **Tool:** **GBP post** + **Blotato** (social) linking to the new page
- **Do:** a GBP update + 1–2 social posts pointing at it; add real photos.
- **Output:** engagement + freshness signals that help ranking.

## ⑧ CONVERT — page ranks → visitor acts
- **Tool:** the page's **CPPA form + click-to-call**
- **Do:** the ranking page turns a searcher into a call or form submission.
- **Output:** a new lead.

## ⑨ SPEED-TO-LEAD — respond in 5 minutes
- **Tool:** **Twilio** (auto-text + AI voice) — see `M7_SPEED_TO_LEAD_SOP.md`
- **Do:** instant text → AI voice pre-qualifies → books the CPPA → hot leads to the owner.
- **Output:** a booked photo audit.

## ⑩ OPTIMIZE — compound the winners
- **Tool:** OpenSEO + Me/free agents
- **Do:** pages at position 5–10 get a refresh (more FAQ, internal links, photos) to push into top 3. Then pick the next keyword → back to ①.
- **Output:** more page-1 rankings, more leads, every week.

---

## ⏱️ The cadence
- **Weekly:** 1–2 pages (②–④) + GBP/social (⑦) + review texts + answer leads in 5 min (⑨)
- **Monthly:** SEO audit (①), 1 competitor/city page, refresh top performers (⑩)
- **Always-on (automatic):** ⑤ index · ⑥ track · ⑧ convert

## 🧠 The one-sentence version
**OpenSEO tells you what to write → you write + publish it → Google indexes + ranks it →
Site Kit/OpenSEO track it → GBP/social amplify it → the page converts → speed-to-lead books it → repeat.**

That's the full loop. Run it weekly and it compounds. 🍍

<!-- M7-FIREWALL-EXEMPT: workflow -->
