---
type: golive_checklist
title: M7 — Domain Go-Live + Search Console Change-of-Address (don't drop rankings)
status: active
last_updated: 2026-07-21
---

# 🚦 M7 — GO-LIVE CHECKLIST (migrate without losing Google)

> Print this. Do it in order. Each step is a human click or a copy-paste to an AI agent. The one job:
> move to the new site **without dropping the rankings the old site earned.**

## 🅐 BEFORE YOU FLIP ANYTHING (build + prep)
- [ ] **Full backup** of both sites (old export + new WordPress backup — UpdraftPlus plugin, free).
- [ ] **Export the old site's full URL list.** Free tool: **Screaming Frog SEO Spider** (crawl
      pineapplecontractors.com → Export → All URLs). Or use the old `/site-map/` page.
- [ ] **Finish the redirect map.** Open `M7_Redirect_Map.csv` — I filled the core + top ~25 city rows.
      Hand the full crawl + this CSV to an AI to complete every remaining URL (prompt below).
- [ ] **Build the new pages** (core → roofing → city) in our format, CPPA/IKO/no-green, tracked.
- [ ] **Confirm tracking** on the new site: Meta Pixel `2545389655696737` fires, GA4 set, lead form → CRM.

## 🅑 SET THE 301 REDIRECTS (this is what saves your SEO)
- [ ] WordPress → install the free **"Redirection"** plugin (Tools → Redirection).
- [ ] Import `M7_Redirect_Map.csv` (Redirection supports CSV import: old URL → new URL, type 301).
- [ ] Test 10 old URLs in a browser → each must land on the matching new page (not a 404, not the homepage).
- [ ] Keep the **old domain live** and pointing/redirecting for **6–12 months** (don't cancel it).

## 🅒 SEARCH CONSOLE — CHANGE OF ADDRESS (only if changing domains)
*(Do this AFTER the 301s are live and tested.)*
- [ ] Verify **both** domains in Google Search Console (old + new) — you already have the old one verified.
- [ ] Submit the **new sitemap**: Search Console (new property) → Sitemaps → add `sitemap.xml`.
- [ ] Old property → **Settings → Change of Address** → select the new site → Google processes the move.
      *(Requirement: site-wide 301s from old → new must already be in place — that's step 🅑.)*
- [ ] Resubmit key pages for indexing (URL Inspection → Request Indexing) on your top city + money pages.

## 🅓 AFTER GO-LIVE (watch it)
- [ ] Week 1–4: check the **Redirection plugin's 404 log** weekly → add any missed redirects.
- [ ] Watch Search Console **Coverage + Performance** — expect a small dip, then recovery in 4–8 weeks.
- [ ] Update your **Google Business Profile, GBP posts, LSA, Meta, Yelp, BBB** to the new domain (NAP consistency).
- [ ] Update internal links, footer, and any ad URLs to the new domain.

---

## 🤝 HAND-OFF — finish the redirect map (paste to ChatGPT / Fable / Free Claude Code)
```
Attached is my old-site URL crawl (CSV of every pineapplecontractors.com URL) and my started redirect map
(M7_Redirect_Map.csv). Complete the redirect map: for EVERY old URL, give the best matching new URL on
pineappleroofingllc.com. Rules: service-area city pages -> /locations/<city>-tx/ ; roofing service pages ->
/services/<service>-dallas-tx/ ; keep core pages mapped to the existing new pages already in my CSV; if no
match exists, target the closest parent page and mark Status=BUILD. Output a clean CSV with columns:
Old URL, New URL, Status (LIVE/BUILD), Priority (1-3), Notes. Never introduce green; never use "free" or "GAF".
```

## ✅ WHAT'S DONE
- `M7_Redirect_Map.csv` — core pages + top ~25 city redirects (ready for the Redirection plugin).
- `M7_SITE_MIGRATION_MASTER_PLAN.md` — full inventory + build hand-off.
- `M7_CHATGPT_HANDOFF.md` — the page-build prompts.

## 🌅 ORDER OF OPERATIONS (one line)
Backup → crawl old URLs → finish redirect CSV → build new pages → import 301s → test → Change of Address →
watch the 404 log. **Never cancel the old domain until rankings have moved over.**

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
