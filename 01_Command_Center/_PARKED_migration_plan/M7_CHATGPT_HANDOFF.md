---
type: handoff_pack
title: M7 — ChatGPT / Fable hand-off (finish the open items)
status: active
last_updated: 2026-07-21
---

# 🤝 M7 — HAND THESE TO CHATGPT / FABLE (copy-paste, done for you)

Here's what's finished vs. what to hand off, so nothing stalls on time or tokens.

## ✅ DONE (no action needed)
- **Capture page** (`Outbox_Drafts/CPPA_Capture_Page/index.html`) — editorial design, compliant (CPPA, no
  green), your real Meta Pixel active, tracking + form wired. **Grain toned to .10** (polish applied).
  Only 2 placeholders left before publishing: `FORM_ENDPOINT` (Apps Script /exec URL) + `GA4_ID` (optional).
- **Design benchmark + Neal formula** — `03_Knowledge_Mat/00_Atlas/M7_DESIGN_BENCHMARK_NEAL_AND_SITE_FIX.md`.
- **Marketing kit** — Offer, Leads, Sales, Content, Capture (all in `Outbox_Drafts/`).

---

## 🅰️ HAND-OFF #1 — Fix "FREE" on the live WordPress site (needs YOUR login)
*I can't edit your live WordPress from here. Do this (5 min) or paste the prompt below to ChatGPT to walk you through it.*

**Fastest way (WordPress plugin):**
1. WP Admin → Plugins → Add New → install & activate **"Better Search Replace"**.
2. Tools → Better Search Replace. **Tick "Run as dry run" first.** Run each pair, review, then untick and run for real:
   - `FREE Quote` → `Complimentary Quote`
   - `Free Quote` → `Complimentary Quote`
   - `Free Estimate` → `Complimentary Estimate`
   - `Get a Free` → `Get a Complimentary`
   - `free inspection` → `Complimentary Professional Photo Audit`
3. In **Elementor** (Home → Edit with Elementor): fix the hero form heading, the yellow button, and the top-nav button to **"Get Your Complimentary Quote."** Update → check the live site.

**Paste-to-ChatGPT prompt (if you want it to guide you live):**
```
Act as my WordPress + Elementor assistant. My site pineappleroofingllc.com (Elementor) still says "Get your
FREE Quote Today" and "Get A FREE Quote." My brand rule bans the word "free" — everything must say
"Complimentary" or "Complimentary Professional Photo Audit (CPPA)." Walk me step by step, click by click, to
(1) install Better Search Replace and swap: "FREE Quote"→"Complimentary Quote", "Free Estimate"→"Complimentary
Estimate", "Get a Free"→"Get a Complimentary" (dry-run first), and (2) fix the hero form heading, the yellow
button, and the top-nav button in Elementor. Keep phone 972-928-0788, License #03-0637, and never introduce
green. Tell me exactly where to click.
```

---

## 🅱️ HAND-OFF #2 — Build the 5 city location pages (Neal format, CPPA, tracked)
*Big build — hand this whole block to ChatGPT / Fable / Free Claude Code. It uses your capture page as the base.*

```
Act as my senior web designer. Using the attached index.html (my Pineapple Roofing CPPA capture page) as the
exact design system — same fonts (Libre Caslon Display + DM Sans), palette (navy #1A365D, gold #FBC02D, cyan
#00BFFF, paper #F7F5EF, ZERO green), same header/footer, same lead form + Meta Pixel (2545389655696737) +
UTM tracking + FORM_ENDPOINT placeholder — build 5 CITY LANDING PAGES, one file each:
Frisco, Lewisville, Plano, McKinney, Allen (Texas).

Model the STRUCTURE on nealrfg.com location pages, but keep MY words (never "free" → CPPA):
1. Hero: "[City]'s Documentation-First Roofing" + the CPPA promise + the lead form + trust badges.
2. A repeatable trust band: "5.0★ · 200+ reviews · License #03-0637 · IKO Certified · 50-year warranty".
3. "As certified" row: minority-owned (NMSDC), IKO, BBB, since 2005.
4. Our Standards — 3 differentiators (Documentation-First audit · insurance claim advocacy · IKO install).
5. Service cards (Roof Replacement, Roof Repair, Storm Damage, Gutters, Siding).
6. Real Google-review testimonials placeholders + a spot for a video reel.
7. Family/founder story: Polynesian-owned, family-operated, Frisco/North Texas since 2005, Tauhi Vā.
8. City-specific FAQ + JSON-LD LocalBusiness + FAQ schema (answer in the first 40 words).
9. Contact: phone 972-928-0788 · support@pineappleroofingllc.com · License #03-0637 · map.
Every CTA = "Reserve Your Complimentary Professional Photo Audit." Mobile-first. Add honest insurance
disclaimers (do not guarantee claim approval, homeowner pays deductible). Output each as its own .html file:
frisco.html, lewisville.html, plano.html, mckinney.html, allen.html.
```

---

## 🅲️ (Optional) HAND-OFF #3 — Rebuild the WHOLE public site in this style
When ready to leave the Scorpion/WordPress look behind, hand ChatGPT/Fable the capture page + Neal benchmark
and say: *"Rebuild pineappleroofingllc.com as a clean multi-page site in this exact style, CPPA everywhere,
zero green, then I'll host it free on Cloudflare Pages."*

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
