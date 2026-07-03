---
name: pineapple-blog-post
description: Write SEO-optimised roofing/restoration blog posts in the Pineapple Contractors voice. Draft-only to the Outbox — never publishes. Author JR. Moeakiola.
author: JR. Moeakiola
user_invocable: true
brand: Pineapple Contractors M7
compliance: DEC-005 Outbox Shield — DRAFT ONLY
---

# 🍍 Pineapple SEO Blog Writer — Draft-to-Outbox

> This is the M7-compliant rewrite of the AIPB 5-site pipeline. It writes ONE strong,
> factually-grounded, SEO-optimised article per keyword, in the Pineapple voice, and
> saves it **PAUSED** to `01_Command_Center/Outbox_Drafts/SEO_Posts/`. It NEVER deploys,
> NEVER pings an indexer, NEVER edits a live site or sheet. Saia is the only publisher.

---

## 🚦 HARD RULES (read first — non-negotiable)

1. **Outbox Shield (DEC-005):** Save every post to `01_Command_Center/Outbox_Drafts/SEO_Posts/<slug>.md` with a `DRAFT — DO NOT PUBLISH` banner. Do **not** run any deploy, Netlify, Omega Indexer, Google Sheet, or publish command. Ever.
2. **Banned words → required swaps** (hard block):
   - "free" / "free inspection" → **Complimentary Professional Photo Audit (CPPA)**
   - "$0 down" / "$0 out of pocket" → **Full Restoration Coverage Evaluation**
   - "cheap" / "bargain" / "discount" → **value-engineered** or CPPA
   - "GAF" → **IKO Certified**
   - "warrior" / "toa" / "six brothers" → **The Pineapple Standard**
   - "we beat your insurance" / "denial-buster" → **Comprehensive documentation for a successful claim**
3. **Colour law:** Any HTML/OG imagery references Navy `#1A365D`, Gold `#FBC02D`, Cyan `#00BFFF`. **GREEN is banned** (`#00FF00`, `#2D7D46`, any green).
4. **Author byline is always `JR. Moeakiola`.** Company: Pineapple Contractors.
5. **Verify, don't invent.** Facts come from M7 brand data (below) or a source the user pastes. If a stat/claim isn't sourced, leave it out or mark `<<VERIFY>>`.
6. **Brand routing — NEVER mix vocabularies:**
   - **Pineapple Roofing** (pineapplecontractors.com): storm, hail, thermal shock, IKO-certified roof replacement/repair. Roofing words only.
   - **Pineapple Restorations** (pineapplerestorations.com): fire recovery, water mitigation, mold remediation, biohazard. Restoration words only.
   - A roofing keyword → roofing article on the roofing site. A restoration keyword → restoration article on the restoration site. Do not blend.
7. Every consumer-facing post ends with a **Tongan proverb** where it fits naturally.

---

## 🧾 M7 Brand Facts (the source of truth)

- **Company:** Pineapple Contractors — Polynesian-owned, family owned & operated.
- **Since:** 2005. **Author/voice:** JR. Moeakiola.
- **Credentials:** RCAT License #03-0637 · HUB Certification #1861616404400 · IKO Certified · 5-Star Rated.
- **Phone:** 972-928-0788. **HQ:** 1 Cowboys Way, Suite 270W, Frisco, TX 75034. Branches: Lewisville, TX and Austin, TX.
- **Service area ZIPs:** 75033, 75034, 75035, 75067, 75068. Luxury enclaves: Starwood, Newman Village.
- **Signature offer:** Complimentary Professional Photo Audit (CPPA).
- **Quote frame:** Full Restoration Coverage Evaluation.
- **Avatars (roofing):** Frisco multi-unit property managers; luxury homeowners; commercial owners/hotel operators.
- **Speed-to-lead:** contact within 5 minutes. **Min project:** premium estate & commercial portfolio restoration.

## 🎥 Media Library (embed where relevant)

- **Client testimonial (YouTube):** video id `MSJaGroxnB4` → embed near the top of roofing posts.
  ```html
  <iframe width="848" height="485" src="https://www.youtube.com/embed/MSJaGroxnB4" title="Pineapple Contractors — Client Testimonial" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  ```
- **Instagram:** @pineappleroofing — link as social proof: `[See recent Pineapple projects on Instagram](https://www.instagram.com/pineappleroofing/)`.
- **02_Media_Vault/** — 39GB of real project photos/reels. Reference filenames for photo callouts (read filenames, not bytes).

---

## 🪜 THE STEPS

### Step 1 — Get the keyword + confirm brand
Ask the user for the target **keyword** if not given. Decide the brand by the keyword (Rule 6). Make a `slug` = lowercase-hyphenated keyword.

### Step 2 — Gather real facts
Pull from M7 Brand Facts above + any transcript/source in `02_Media_Vault/Raw_Transcripts/<slug>.txt` the user provides. If a client testimonial transcript exists, quote it. Never invent stats.

### Step 3 — CTR-optimised title + meta (NO "free")
Treat the title like a headline that earns the click. 50–60 chars, keyword included, power words allowed EXCEPT banned ones. Good roofing formulas:
- "Hail Damage Roof Repair in Frisco (What To Do First)"
- "IKO Certified Roofer Frisco TX — The Pineapple Standard"
- "Storm Damage? Book a Complimentary Photo Audit in Frisco"
Meta description: 140–155 chars, payoff-first, keyword early, ends on the CPPA hook or a number. No "free".

### Step 4 — Write ONE strong long-form article (2,000–3,000 words)
Roofing-only means one authoritative post per keyword (no near-duplicate copies).

**Voice & format (Pineapple × Hormozi rhythm):**
- Write as **JR. Moeakiola**, 1st person, warm, confident, culturally rooted, no corporate filler.
- **Every line is a COMPLETE sentence on its own line** (subject + verb). Never fragments like "Three reasons." or "More coverage."
- Keyword in the **very first line** and the **very last line**. Keyword in H2/H3 naturally.
- Sprinkle LSI/related terms (roof replacement, hail impact, insurance claim, shingle, decking, Frisco storm season, property manager).
- Clear H2/H3 headers; short scannable sections; bold key benefits; tables for comparisons where they fit.

**Required blocks in every post:**
1. Benefit-led opening line (a real worry the homeowner/property manager has).
2. Primary testimonial video embed (roofing → `MSJaGroxnB4`).
3. JSON-LD schema (Step 5).
4. Body sections answering the search intent with real Pineapple facts.
5. **FAQ section** (4–6 Q&As using the keyword + related terms).
6. **CPPA call-to-action** blocks (see Step 6).
7. **Trust-signal block** (RCAT #03-0637, HUB #1861616404400, IKO Certified, 5-Star, Since 2005, 972-928-0788).
8. **Author bio block** (JR. Moeakiola — Step 7).
9. Tongan proverb close.
10. Keyword in the final line.

### Step 5 — Schema markup (rich results)
Insert JSON-LD after the video, before the first H2. Use **RoofingContractor / LocalBusiness** + **Article** + **FAQPage**.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "RoofingContractor",
  "name": "Pineapple Contractors",
  "image": "[OG image or default]",
  "telephone": "+1-972-928-0788",
  "address": {"@type":"PostalAddress","streetAddress":"1 Cowboys Way, Suite 270W","addressLocality":"Frisco","addressRegion":"TX","postalCode":"75034","addressCountry":"US"},
  "areaServed": ["Frisco TX","Lewisville TX","Austin TX"],
  "url": "[site url]",
  "priceRange": "$$$",
  "founder": {"@type":"Person","name":"JR. Moeakiola"}
}
</script>
```
Add an **Article** block (author = JR. Moeakiola) and a **FAQPage** block for the FAQ. These render inline as raw HTML.

### Step 6 — Conversion (Pineapple CTAs — CPPA, never "free")
Use the styled CTA box 2–3×, personalised to the topic:
```markdown
> **🍍 Worried about storm damage on your Frisco roof?**
> Book a **Complimentary Professional Photo Audit (CPPA)** — our IKO-certified team documents every shingle so you have a comprehensive record for a successful claim.
> **[→ Book your CPPA — call 972-928-0788](tel:+19729280788)**
```
Primary CTA = book a CPPA / call **972-928-0788**. Wrap every URL in markdown link syntax (bare URLs don't render). Optional: link Instagram as social proof.

### Step 7 — Author bio block (E-E-A-T)
```markdown
## About the Author

I'm **JR. Moeakiola** with **Pineapple Contractors** — a Polynesian-owned, family-run roofing and restoration company serving Frisco and North Texas since 2005.

- RCAT Licensed #03-0637 · HUB Certified #1861616404400
- IKO Certified · 5-Star Rated
- Serving Frisco, Lewisville, and Austin

**[→ Book your Complimentary Professional Photo Audit — 972-928-0788](tel:+19729280788)**
```

### Step 8 — Front matter + save PAUSED to Outbox
```yaml
---
title: "[CTR title, max 60 chars, keyword, no 'free']"
description: "[payoff-first meta, max 155 chars, keyword early]"
brand: "Pineapple Roofing"          # or "Pineapple Restorations"
site: "pineapplecontractors.com"    # or pineapplerestorations.com
category: "[Roofing / Storm / Restoration]"
date: [YYYY-MM-DD]
keywords: "[target keyword, related terms]"
author: "JR. Moeakiola"
status: "DRAFT — DO NOT PUBLISH — awaiting Saia GO (DEC-005)"
---
```
Save to `01_Command_Center/Outbox_Drafts/SEO_Posts/<slug>.md`. Begin the file body with:
`> ⏸ DRAFT — PAUSED. Do not publish. Awaiting Saia's explicit GO. (Outbox Shield / DEC-005)`

### Step 9 — Compliance self-check (before you finish)
Run this checklist (mirrors `04_Tech_Lab/scripts/brand_firewall.py`):
- ❌ No "free", "cheap", "bargain", "GAF", "warrior", "toa", "six brothers", "$0 down".
- ✅ CPPA present · IKO (not GAF) · RCAT #03-0637 · phone 972-928-0788.
- ✅ Zero green anywhere. Navy/Gold/Cyan only.
- ✅ Author = JR. Moeakiola. Keyword in first + last line. FAQ + schema + CTA + trust block present.
- ✅ File saved in Outbox_Drafts/SEO_Posts, marked PAUSED.
Report the checklist result to Saia with the draft path.

### Step 10 — What we do NOT do (removed from the AIPB original)
- ❌ No 5-site deploy · ❌ no Netlify · ❌ no Omega Indexer (that key was Julian's) · ❌ no Google Sheet edit · ❌ no Julian Goldie bio/voice/CTAs · ❌ no AI-Profit-Boardroom/Skool/Mastermind links.

---

*Ko e hala 'o e fononga ko e faka'apa'apa — the path of the journey is respect.* 🌺
