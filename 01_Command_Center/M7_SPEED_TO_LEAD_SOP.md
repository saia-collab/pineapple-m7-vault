---
type: sop
title: M7 Speed-to-Lead + AI Voice Pre-Qualification
status: active
last_updated: 2026-07-15
---

# ⚡ M7 Speed-to-Lead + AI Voice Pre-Qualification

**Why this is the #1 lever:** leads contacted within **5 minutes** convert up to **3x higher**.
You already get LSA + GBP leads — this makes sure none go cold.

## 🎯 The flow (all lead sources → one funnel)
```
[LSA lead] [GBP call/message] [Website CPPA form]
                     │
                     ▼
   Instant auto-text (<60 sec): "Thanks [Name]! Pineapple Roofing here —
   calling you in the next 5 min about your [service]. Reply STOP to opt out."
                     │
                     ▼
   AI Voice agent calls (or answers) → pre-qualifies → books CPPA → hands hot leads to you
                     │
                     ▼
   Booked CPPA in calendar + logged (Airtable/CRM) → Field rep runs the photo audit
```

## 🤖 AI Voice Pre-Qualification Script (give this to the voice platform)
**Persona:** warm, local, helpful — "Pineapple Roofing's scheduling assistant." Never pushy.

1. **Open:** "Hi, this is the scheduling assistant for Pineapple Roofing — thanks for reaching out! I just need a few quick details to get you booked for your Complimentary Professional Photo Audit. Sound good?"
2. **Service:** "What's going on with your roof — storm/hail damage, a leak, an aging roof, or something else?"
3. **Location (lead score):** "And what city are you in?" → *Frisco/75033-35, Lewisville, Plano, McKinney = high priority.*
4. **Insurance (lead score):** "Have you noticed damage after a recent storm, or are you thinking about filing an insurance claim?"
5. **Urgency:** "Is this an active leak/emergency, or are you planning ahead?"
6. **Book:** "Perfect — we do a no-cost, no-pressure photo audit. I have [day/time] or [day/time]. Which works?"
7. **Confirm + handoff:** "You're booked for [time]. A licensed, IKO Certified Pineapple team member (RCAT #03-0637) will document everything and send a report within 24 hours. We'll text a reminder. Anything else?"

**Brand law:** "Complimentary Professional Photo Audit" (never "free"), IKO Certified (never GAF),
The Pineapple Standard, RCAT #03-0637, (972) 928-0788. No price quotes on the call.

## 📊 Lead score (route hot leads to a human fast)
| Signal | Points |
|---|---|
| Frisco core ZIP (75033/34/35) | +25 |
| Storm/hail + insurance | +30 |
| Active leak / emergency | +20 |
| Commercial / multi-unit / HOA | +25 |
**Score ≥ 60 = ELITE** → text/call the owner immediately, don't wait for the AI to finish.

## 🛠️ What it takes to build it (honest split)
| Piece | Who | Options |
|---|---|---|
| **Instant auto-text on new lead** | You set up | A lead-router (GoHighLevel, or Zapier/Make → SMS via Twilio). Fastest first win. |
| **AI voice agent** (answer/callback + qualify) | Platform + your accounts | **ElevenLabs Conversational AI** (you have ElevenLabs), or Vapi / Bland.ai / Retell — all need a phone number + your account |
| **Lead capture from LSA/GBP** | You connect | LSA leads → forward to the router; GBP calls → forward to the AI number |
| **The script + qualification logic** | ✅ Me (above) | Done — paste into the platform |

## ▶️ Recommended rollout (start simple, don't boil the ocean)
1. **Week 1 — instant auto-text** on every new lead (biggest, cheapest win). No AI needed.
2. **Week 2 — AI voice callback** using ElevenLabs/Vapi + the script above, for missed/after-hours leads.
3. **Week 3 — full inbound AI receptionist** answering the main line + booking.

> The OS writes the script, logic, and copy (done). The **phone number + voice platform account** are yours to set up — I can't create telephony accounts, but I'll wire the script + qualification flow once you pick a platform.

<!-- M7-FIREWALL-EXEMPT: sop -->
