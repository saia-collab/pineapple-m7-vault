---
type: playbook
title: M7 Storm Response Playbook — Your Unfair Advantage
status: active
last_updated: 2026-07-16
---

# ⛈️ The Storm Response Playbook (D2D × Digital)

**Why this beats every other data feed:** competitor YouTube and keyword scrapes don't ring
the phone. **A hail storm does.** When hail hits a Frisco ZIP, hundreds of homeowners need
exactly what you sell — *that week*. You already have the thing most digital-only roofers
don't: **a family crew that will knock the door.** This play marries the two.

## 📡 The free data source (no Grok, no API key)
- **NWS Fort Worth** — weather.gov/fwd (local storm reports, warnings)
- **NOAA SPC Storm Reports** — spc.noaa.gov/climo/reports (daily hail reports w/ size + location)
- **NCEI Storm Events** — ncdc.noaa.gov/stormevents (historical, by county)

Check after every North Texas storm. You're looking for: **hail size + the ZIP/county hit.**

## 🔁 The 72-hour storm loop (run it every time hail hits)

**Hour 0–24 — Know & claim it**
1. Pull the NWS/SPC report → identify the **exact ZIPs** hit (e.g., 75034 Frisco).
2. **GBP post that day** (BOTH profiles): *"Hail hit [neighborhood] last night. Damage is often invisible from the ground. Book your Complimentary Professional Photo Audit — (972) 928-0788."*
3. **Publish a storm-event page**: `/hail-storm-[month]-[year]-[city]-tx/` — dated, specific, cites the NWS report. Google loves fresh, local, event-specific content.

**Hour 24–72 — Own the neighborhood (your superpower)**
4. **Canvass that exact ZIP.** This is where you win. Digital-only competitors are still writing ads; your family is on the doorstep with a real face and a real license.
5. **Door hanger + QR** → straight to the CPPA form on the new page.
6. **Social + LSA:** post the storm content; bump LSA budget for that area for 2 weeks.

**Week 1–2 — Convert & compound**
7. Every CPPA → documented photo report → insurance claim handled.
8. Every completed job → **review request that names the neighborhood** ("we did a roof in [neighborhood]") → feeds the local pack.
9. Before/after photos → GBP posts + social → proof for the next homeowner.

## 🎯 Why this is your unfair advantage
| Digital-only roofer | Pineapple |
|---|---|
| Sees the storm, buys ads | Sees the storm, **posts + publishes + KNOCKS THE DOOR** |
| Faceless lead form | A family, a license (#03-0637), a handshake |
| Fights on ad spend | Wins on trust + speed |

**The machine finds the storm and captures the searchers. Your family closes the street.**
That combination is very hard to beat in a local market.

## 🤖 Offload to Hermes → Mixture (MoA) — runs via OpenRouter (not the capped Ollama)
Paste these into the **Mixture** panel when Goal Mode is capped:

**Storm-event page:**
```
Write a storm-event landing page for Pineapple Roofing: "Hail Storm [Month Year] — [City], TX".
Cite that NWS/SPC reported [size] hail in [ZIP] on [date]. AEO hook in sentence 1, what to check,
why documentation matters for the claim, FAQ, CPPA CTA. BRAND: CPPA (never "free"), IKO Certified
(never GAF), The Pineapple Standard, RCAT #03-0637, (972) 928-0788, zero green. Output markdown
with frontmatter (title, meta).
```

**Review replies (draft only — you approve):**
```
Write warm, human, keyword-light replies to these Google reviews for Pineapple Roofing (family-owned,
IKO Certified, RCAT #03-0637). Reference what each customer actually said. Never sound like a bot.
Never use "free" — say Complimentary Professional Photo Audit. Reviews: [paste]
```

**GBP storm posts:**
```
Write 3 Google Business Profile posts for a hail event in [neighborhood], Frisco TX. Urgent but not
fear-mongering. CPPA offer, phone (972) 928-0788, IKO Certified, RCAT #03-0637. Under 1500 characters each.
```

## ⚡ The rule
**Automate the machine. Never automate the handshake.**
AI finds the storm, writes the page, drafts the post and the reply.
**You** knock the door, climb the roof, and look the homeowner in the eye.
That's how a family business wins the digital game without losing what made it work.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: playbook -->
