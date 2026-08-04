---
type: design_skill
title: M7 DESIGN SKILL — C.R.A.F.T. front-end engine, filtered into Pineapple M7 branding
status: active
last_updated: 2026-07-06
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🎨 M7 DESIGN SKILL — the C.R.A.F.T. Engine, on-brand (zero green)

> **How to use:** any agent building a landing page, website, deck, or HTML asset for Pineapple reads
> THIS file first. It's the C.R.A.F.T. front-end + copywriting system, with the palette **filtered to the
> M7 brand law** (the source kit used emerald `#5ab896` and aubergine `#15101a` — both BANNED here).
> Prompt shortcut: *"Using the M7 Design Skill, build the [section] of [page]."*

## ⚠️ WHAT CHANGED FROM THE SOURCE KIT (brand firewall)
| Source C.R.A.F.T. | ❌ Why banned | ✅ M7 replacement |
|---|---|---|
| Background `#15101a` (aubergine) | off-brand | **Royal Navy field `#0f2444` / `#1A365D`** |
| Success `#5ab896` (emerald/teal) | **GREEN — banned everywhere** | **Status Cyan `#00BFFF`** |
| Accent `#d4a574` (muted gold) | off-brand gold | **Pineapple Gold `#FBC02D`** |
| Failure `#c97c5e` (rust) | ok (not green) | keep rust `#c97c5e` OR red `#e5484d` |

## TYPOGRAPHY (kept — premium, brand-neutral)
- **Headlines:** Bricolage Grotesque (700–800).
- **Body:** Manrope.
- **Accents / eyebrows:** Caveat (handwritten) — rendered in **Gold `#FBC02D`**.
- Link the Google Fonts block + `styles.css` in every `<head>`.

## M7 PALETTE (the only colors — ZERO green)
```
--navy:      #1A365D   /* structural authority, panels, headings */
--navy-deep: #0f2444   /* page background field */
--panel:     #12233f   /* cards / surfaces */
--cream:     #f3ebda   /* warm body text on dark (or #eef3fa cool) */
--gold:      #FBC02D   /* accents, eyebrows, CTAs, two-tone H1 span */
--cyan:      #00BFFF   /* SUCCESS state, status, links, highlights (never green) */
--rust:      #c97c5e   /* failure/limit state (warm, not green) */
```
Negative space = white `#FFFFFF`. Any green hex/rgba/named/Tailwind class = critical build failure.

## MANDATORY LANDING-PAGE STRUCTURE (10-part skeleton)
1. **Hero** — Gold eyebrow (Caveat) · two-tone H1 (`<span class="accent">` in Gold) · 3–4 sentence intro · hero art · 3 stats.
2. **Source-quote** — Caveat attribution line.
3. **The Problem (I —)** — name the pain in plain English.
4. **What's Different (II —)** — with a `.pull` quote.
5. **The Framework (III —)** — 3 `.surface-card` moves, each an emoji + verb.
6. **Setup / Execution Path (IV —)**.
7. **Demo 1: The Win (V —)**.
8. **Demo 2: The Honest Limits (VI —)** — builds trust by admitting limits.
9. **CTA Band (`.agentos-cta`)**.
10. **Data Verification (VII —) → Belief-breakers (VIII —) → 30-Day Roadmap (IX —) → Recap (X —) → Final CTA (`.final-cta`)**.

## COMPONENTS (class names to emit)
- Two-tone headings: `<h1>Frisco's <span class="accent">Documentation-First</span> Roofing</h1>`
- `.surface-card` (framework moves), `.pull` (pull quote), `.way-box.new` (contrast box), `.agentos-cta` / `.final-cta` bands, `.stat` (hero stats), `.moat` (10px Navy border on project photos).

## COPYWRITING RULES (C.R.A.F.T. + M7 lexicon)
- **Plain English only** — explain like the reader is 12, use vivid analogies. No "AI slop", no "leverage/synergize".
- **One sentence per line** in markdown/chat drafts (kills the wall-of-text look).
- **Name the framework**: "The ___ Method™" or "The ___ Engine™" — 3 rhythmic, chantable steps.
- **M7 lexicon is non-negotiable:** CPPA (never "free") · IKO Certified (never "GAF") · "Full Restoration Coverage" (never "$0 down") · The Pineapple Standard (never warrior/toa) · RCAT #03-0637 · IKO · 5-Star · Since 2005 · 972-928-0788.
- **Close long-form** with the proverb: *Ko e hala 'o e fononga ko e faka'apa'apa*.
- **Every asset PAUSED** to `01_Command_Center/Outbox_Drafts/` — Saia publishes.

## HERO / LAYOUT ENVELOPES (Brand Firewall visual law)
- Top banner 140px (Gold on Navy, impact font) · Hook font 42px · Wrap envelope 860–1080px · Bottom credential bar 95px (Navy, gold text: "Pineapple Contractors | RCAT #03-0637 | IKO Certified").
- Navy Photo Moat: 10px solid Navy `#1A365D` border on all before/after project photos.

## THE M7 NAME FOR THIS SKILL
**The Documentation-First Engine™** — *Show. Don't sell. Prove.* (Problem → Proof → Path.)

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference (palette table lists banned hexes as definitions) -->
