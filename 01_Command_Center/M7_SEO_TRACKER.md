---
type: seo_rank_tracker
title: M7 SEO TRACKER — target keywords, ranks, and the free tracking method
status: active
last_updated: 2026-07-05
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 📈 M7 SEO TRACKER — what we're ranking for, and how we watch it (free)

> **The rule (VP):** we do NOT pay for Semrush/Ahrefs/OpenSEO. Rank + keyword tracking runs on **Google
> Search Console (free, official)** through the dashboard **SEO → Research** tab. This sheet is the manual
> ledger until the site is live + GSC-connected.

## 🎯 TARGET KEYWORDS (from the 13 AEO pages already staged in Outbox)
| # | Target keyword | Page | Area | Rank | Last checked |
|---|---|---|---|---|---|
| 1 | roof replacement Frisco TX | CityPage_Frisco | Frisco | — | — |
| 2 | storm damage roof repair Lewisville TX | CityPage_Lewisville | Lewisville | — | — |
| 3 | roofing contractor McKinney TX | CityPage_McKinney | McKinney | — | — |
| 4 | hail damage roof inspection Plano TX | CityPage_Plano | Plano | — | — |
| 5 | roof replacement Allen TX | CityPage_Allen | Allen | — | — |
| 6 | roof repair The Colony TX | CityPage_TheColony | The Colony | — | — |
| 7 | roof replacement Prosper TX | CityPage_Prosper | Prosper | — | — |
| 8 | storm damage roof repair Little Elm TX | CityPage_LittleElm | Little Elm | — | — |
| 9 | roofing contractor Castle Hills TX | CityPage_CastleHills | Castle Hills | — | — |
| 10 | roof replacement 75033 Frisco | ZIP_75033 | 75033 | — | — |
| 11 | roof replacement 75034 Frisco | ZIP_75034 | 75034 | — | — |
| 12 | roof replacement 75035 Frisco | ZIP_75035 | 75035 | — | — |
| 13 | hail damage roof Frisco TX | Topic_FriscoHailDamage | Frisco | — | — |

## 🔎 HOW TO CHECK RANK (free, 3 ways)
1. **Google Search Console (the real one)** — after the site is live + verified: dashboard **SEO → Research**
   tab shows impressions, clicks, average position, and top queries per page. $0, official Google data.
2. **Manual spot-check** — open an **incognito** Google window (so it's un-personalized), search the keyword,
   note where `pineapplecontractors.com` ranks. Log it in the table above.
3. **Coverage check** — search `site:pineapplecontractors.com` to confirm Google has indexed each city page.

## 🚦 THE SEQUENCE TO TURN TRACKING ON
- [ ] **Publish the site** (Fable "rebuild roofing site" task → Outbox → Saia approves → deploy).
- [ ] **Verify pineapplecontractors.com in Google Search Console** (search.google.com/search-console — free).
- [ ] **Connect GSC** to the dashboard (OAuth saved to `~/.agentic-os/gsc-*`) → Research tab goes live.
- [ ] **Submit the sitemap** in GSC so the 13 city pages get crawled fast.

## 📅 CADENCE
- **Weekly (weekend):** update the Rank column from GSC (or incognito spot-check). Note movement.
- **Monthly:** add the next SEO batch's keywords; retire any that plateau.

## ❌ WHY NOT OpenSEO
OpenSEO isn't bundled with the pack and needs a **paid DataForSEO API key**. Google Search Console gives us
the same rank/keyword truth for free, tied to our own site. Revisit OpenSEO only if we ever want bulk
competitor backlink data — and only with a funded DataForSEO key.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
