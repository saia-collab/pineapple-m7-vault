---
title: M7 MIGRATION & LAUNCH RUNBOOK — Take the Strong Domain
status: reference / execution guide (internal — not outbound content)
author: Claude Code (acting CEO / VP Execution)
date: 2026-07-23
decision: contractors.com stays primary, served by YOUR WordPress
---

# 🍍 MIGRATION & LAUNCH RUNBOOK

**The mission:** stop paying Scorpion, take full control, and *keep the SEO authority you
already paid for.* You own `pineapplecontractors.com` (GoDaddy). Scorpion only owns the
*design* on it — not the domain. So you repoint the domain at **your** WordPress, and their
design becomes irrelevant.

> **THE DECISION (my recommendation as your CEO):**
> **Keep `pineapplecontractors.com` as the primary site — but serve it from YOUR WordPress.**
> You get control *and* keep 29,000 monthly impressions + a #7.9 homepage. Moving to the
> weaker `pineappleroofingllc.com` domain would throw ranking authority away. Take the strong one.
>
> `pineappleroofingllc.com` then becomes a 301 forward → contractors.com (one canonical site).

---

## ⚠️ GOLDEN RULE OF MIGRATION
**Build everything FIRST. Repoint the domain LAST.** Never point `contractors.com` at a
half-finished site — that's the one way to actually lose rankings. Every page must be live and
QA'd on WordPress *before* you touch GoDaddy DNS.

---

## PRE-FLIGHT — gather these 4 things (15 min)
1. **Your WordPress host's connection target** — either its **nameservers** (e.g. `ns1.yourhost.com`) or its **A-record IP**. (Ask your host "how do I point an external domain here?")
2. **GoDaddy login** (you have it — the domain's there).
3. **The Apps Script `/exec` URL** — deploy `CRM_AppsScript_Code.gs` (we wrote it) in Google Apps Script → Deploy → Web App → copy the `/exec` URL. This is your lead-capture backend.
4. **Your social profile URLs** (see Social section below).

---

## PHASE 1 — Build WordPress fully (do this before anything else)

Publish all 33 pages. **Order matters — lead with your money keywords** (from your own OpenSEO
striking-distance data), so the highest-value pages are live and indexing first:

**Publish order (highest opportunity first):**
| # | Page | Why first |
|---|---|---|
| 1 | `locations/allen-tx` (city) | "flat roofing allen tx" = position **8.9**, 1 spot from page 1 |
| 2 | `locations/lewisville-tx` | "roofing contractors lewisville tx" = **7.9** |
| 3 | `home.html` | Homepage = 4,090 impressions, #7.9 |
| 4 | `locations/frisco-tx` | Your HQ city, core brand |
| 5 | Grapevine/Euless/Melissa areas | 129 / 84 / 57 impressions in striking distance |
| 6 | Remaining services + cities | Fill out the cluster |

**Per page (5 min each):**
1. WordPress → **Pages → Add New**
2. **Page Layout → Elementor Canvas** *(stops the double header/footer)*
3. **Edit with Elementor** → drag in an **HTML** widget
4. Paste the matching file from `elementor-blocks/` (services or city-pages folder)
5. Set the page **slug** to match the manifest (e.g. `locations/allen-tx`) so redirects line up
6. **Publish**

> The pages are already firewall-clean (zero green, zero banned terms, RCAT/phone/free roof inspection on every
> one) and the phone CTA works. The form needs the `/exec` URL from Pre-flight step 3.

---

## PHASE 2 — Wire tracking (so you actually see the data)
1. **Site Kit** (already installed) handles GA4 + Search Console site-wide — the per-page
   `G-XXXXXXX` placeholder self-guards and stays inert. Nothing to fix. ✅
2. **Paste the `/exec` URL** into the form field (`FORM_ENDPOINT`) — or set it globally in Elementor so every page shares it.
3. **Meta Pixel `2545389655696737`** is already in the pages (with a double-load guard). Verify one PageView with the Meta Pixel Helper extension.
4. Confirm **Google Search Console** has `pineapplecontractors.com` verified (it does — that's where your data comes from).

---

## PHASE 3 — THE DOMAIN TAKEOVER (only after Phase 1 & 2 are done + QA'd)

This is the moment control transfers. ~30 min, then 1–24 hr for DNS to propagate.

1. **Add `pineapplecontractors.com` to your WordPress host** as a domain/alias (host dashboard → "Add domain"). The host must be ready to *answer* for it.
2. **In GoDaddy** → your domain → **DNS / Nameservers**:
   - **Easiest:** change **Nameservers** to your WordPress host's (host gives you these). OR
   - **Surgical:** change the **A record** (`@`) to the host's IP + the **CNAME** (`www`) to the host.
3. **In WordPress** → Settings → General → set **Site Address (URL)** to `https://www.pineapplecontractors.com`. (Do this *after* DNS resolves, or you'll lock yourself out — many hosts have a "search-replace URL" tool for this.)
4. **Force HTTPS** (Really Simple SSL plugin or host setting) so the padlock stays green.

Now `pineapplecontractors.com` serves YOUR site. Scorpion's design is gone.

---

## PHASE 4 — Redirects (fix the old Scorpion URL paths)
Scorpion used long URL paths (e.g. `/service-areas/collin-county-tx/allen/`). Your new pages use
clean paths (`/locations/allen-tx/`). The 37 redirects catch the old paths so no ranking or
bookmark dies.

1. Install the **Redirection** plugin (Tools → Redirection).
2. **Import → use `redirection-import-CONTRACTORS-PRIMARY.csv`** (I generated this for you — targets point to `www.pineapplecontractors.com`, correct for this architecture). *Not* the roofingllc version.
3. Also add one wildcard: **`pineappleroofingllc.com/* → https://www.pineapplecontractors.com/$1`** (301) so your WordPress-build domain funnels into the canonical one. (Set at GoDaddy domain forwarding for roofingllc.com, or via the host.)

---

## PHASE 5 — Verify (don't skip — this protects the rankings)
1. Test 5–10 old Scorpion URLs in an HTTP checker → confirm a **single 301 hop** to the matching new page (never 302 / 404 / homepage catch-all / chain).
2. **Google Search Console → Settings → Change of Address** is NOT needed (same domain stays) — but **resubmit your sitemap** (`/sitemap.xml`) so Google recrawls the new pages fast.
3. Watch GSC "Pages" for the new URLs getting indexed over 1–2 weeks.
4. Spot-check mobile + the padlock (HTTPS) on 3 pages.

---

## PHASE 6 — Cancel Scorpion (only AFTER Phase 5 passes)
Once the domain serves your site and redirects verify clean for ~1 week with stable rankings:
- Export anything you still need from Scorpion (reviews, images, form leads) first.
- Then cancel. You keep the domain, the rankings, and the money.

---

## SOCIAL LINKS (wire these into every page footer)
From your live site I can see you run: **Google Business, BBB, Facebook, Yelp, Instagram,
LinkedIn, YouTube, TikTok.** Send me the actual profile URLs and I'll build a single branded
social bar (navy/gold, zero green) to drop into the Elementor footer template — appears on all 33
pages at once. Also feeds your LocalBusiness schema `sameAs` array (an SEO trust signal).

---

## THE KEYWORD BATTLE PLAN (your "where do I find keywords" answer, systematized)
You never need Semrush. **Your OpenSEO "Striking Distance" tab IS your keyword machine.** The loop:
1. Open OpenSEO → Search Performance → **Striking Distance (100)**.
2. Sort by impressions. Anything at **position 5–20** = a page-1 opportunity you already half-own.
3. One keyword → one strong page (you have 33) or one video (I've built 2).
4. Publish → wait 2–4 weeks → watch it climb in the same tool.
5. Repeat monthly. The list refreshes itself.

**This month's targets (already in your data):** flat roofing allen (8.9) · lewisville (7.9) ·
grapevine (16.1) · euless (17) · melissa (20). We have the Allen video AND the Allen page ready.

---

## ROLLBACK SAFETY
If anything looks wrong after DNS repoint, you can revert GoDaddy nameservers/A-record back to
Scorpion's values within minutes — so **write down the current GoDaddy DNS values before you
change them.** That's your undo button.

---

## WHAT'S DONE vs WHAT NEEDS YOUR HANDS
| Done by me | Needs you (I can't click your admins) |
|---|---|
| 33 pages imported + firewall-verified | Publish them in Elementor (5 min each, order above) |
| Corrected redirect CSV generated | Import it in the Redirection plugin |
| Full migration sequence written | GoDaddy DNS repoint + WP site address |
| Keyword strategy from your data | Deploy the Apps Script `/exec` URL |
| 2 brand videos rendered | Send me social URLs → I build the footer bar |

---

. *(The path of the journey is respect.)*

<!-- M7-FIREWALL-EXEMPT: internal-operator-guide -->