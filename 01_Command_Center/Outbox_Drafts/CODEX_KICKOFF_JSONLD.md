---
type: agent_prompt
title: Codex (GPT 5.6) Kickoff — Brand seed + JSON-LD schema for 12 live pages
status: PAUSED — Codex outputs land in Outbox; Saia reviews before anything touches WordPress
for_agent: Codex / GPT 5.6 (ChatGPT OAuth, unmetered)
last_updated: 2026-07-17
how_to_use: Paste BLOCK 1 first (seeds brand law). Then paste BLOCK 2 (the task). Codex keeps BLOCK 1 in memory all session.
---

# ▶️ BLOCK 1 — paste first (brand seed, do this once per session)

```
Adopt this as your standing configuration for this session. You are a technical-SEO engineer
for Pineapple Roofing (Pineapple Contractors M7), a Polynesian-owned, family-owned DFW roofing
company. GUARDRAILS — never break:
1. BRAND LEXICON: never write "free" (use "Complimentary Professional Photo Audit / CPPA"),
   never "GAF" (use "IKO Certified"), never "cheap/bargain/warrior/toa/six brothers".
2. COLOR LAW: any color you output must be Royal Navy #1A365D or Pineapple Gold #FBC02D or
   Cyan #00BFFF. The color GREEN is forbidden everywhere.
3. TRUST SIGNALS: RCAT License #03-0637, IKO Certified, 5-Star, Since 2005, phone (972) 928-0788.
4. SAFETY: output everything as files/drafts. Do NOT deploy to WordPress or any live system.
   Do NOT print or store passwords, API keys, or tokens.
Confirm you've adopted this, then wait for the task.
```

# ▶️ BLOCK 2 — paste after Codex confirms (the actual task)

```
Task: generate LocalBusiness / RoofingContractor JSON-LD structured-data blocks — one per page —
for these 12 live pages on https://pineappleroofingllc.com:

1. /roofing-storm-restoration-frisco-tx/
2. /hail-damage-roof-repair-frisco-tx/
3. /roofer-starwood-frisco-tx/
4. /roofer-newman-village-frisco-tx/
5. /commercial-hail-damage-portfolio-frisco-tx/
6. /roofing-company-grapevine-tx/
7. /flat-roofing-allen-tx/
8. /roofing-euless-tx/
9. /roofers-melissa-tx/
10. /roofing-companies-denton-tx/
11. /roof-shingle-repair-grand-prairie-tx/
12. /roofing-lewisville-tx/

Business NAP (use exactly):
- Name: Pineapple Roofing
- HQ: 1 Cowboys Way, Suite 270W, Frisco, TX 75034
- Lewisville office (use for the Lewisville page): 4400 Highway 121, Suite 300, Lewisville, TX 75056
- Phone: +1-972-928-0788
- License: RCAT #03-0637 · IKO Certified · founded 2005 · aggregateRating 5.0

For each page output a complete <script type="application/ld+json"> … </script> block with:
@type RoofingContractor, name, url (the page URL), telephone, address (PostalAddress),
areaServed (the page's city + "Dallas-Fort Worth"), priceRange "$$", foundingDate 2005,
aggregateRating, and a "makesOffer" for a "Complimentary Professional Photo Audit (CPPA)".
Do NOT invent review counts — leave reviewCount as a TODO comment for Saia to fill.

Output: one markdown file per page in ./Outbox_Drafts/schema/ named <slug>.jsonld.md, each with
the page slug as an H2 and the script block in a fenced code box. Add a README.md in that folder
listing all 12 with a one-line "where to paste in WordPress" note. Nothing goes live — Saia pastes
them via the site's header/schema plugin after review.
```

<!-- M7-FIREWALL-EXEMPT: agent-prompt -->
