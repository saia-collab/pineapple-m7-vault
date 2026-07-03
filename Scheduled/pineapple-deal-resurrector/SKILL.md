---
name: pineapple-deal-resurrector
description: Bi-weekly dead lead revival — scans Closed Lost / No Response leads, cross-references against storm data and roof age, generates personalized re-engagement drafts for Saia review
---


# PINEAPPLE DEAL RESURRECTOR — Bi-Weekly Run
## Owner: Saia Moeakiola | saia@pineappleroofingllc.com | 972-928-0788
## SOP: C:\PineappleHQ\workflows\deal-resurrector.md

Run the full Deal Resurrector workflow per the SOP. Today's date is used for all storm cross-references and cooldown checks.

---

## STEP 1 — SCAN PHASE

Pull all leads from Airtable base `appntOsAVKy9pwuiF`, table `tblCLEysILQhl6N7I`.

Filter for dead leads where ALL of these are true:
- Status = "Closed Lost" OR "No Response" OR "Attempted Contact" with no update in 14+ days
- Status is NOT "Booked", "In Progress", or "Closed Won"
- Do Not Contact field is blank or false
- Last Resurrection Attempt field is blank OR was more than 30 days ago
- Address field is not blank
- Phone OR Email field is not blank

Score each qualifying lead (0-10):
- +3 if roof age >= 15 years
- +2 if lead notes mention storm, hail, or insurance
- +2 if estimated property value >= $350,000
- +3 if claim was previously denied

Sort descending by score. Take top 20.

---

## STEP 2 — INTELLIGENCE PHASE

For each of the top 20 leads, run Firecrawl web search:

**Storm check:** Search `hail storm [ZIP] [CITY] TX last 30 days roof damage`
- If hail confirmed in lead's ZIP within last 30 days → tag STORM_TRIGGER = true
- Record storm date and hail size

**Neighbor permit check:** Search `roofing permit [ADDRESS] [CITY] TX 2026 building permit`
- If permit activity found near address → tag NEIGHBOR_ACTIVITY = true

**Assign trigger tags per lead:** STORM_TRIGGER / AGING_ROOF (if roof age >= 15) / CRITICAL_ROOF (if >= 20) / NEIGHBOR_ACTIVITY

---

## STEP 3 — DRAFT GENERATION

For each qualified lead, generate a personalized SMS + Email using the matching template from the SOP:

- STORM_TRIGGER → Template A (storm urgency, 30-day window, hail size + date)
- AGING_ROOF / CRITICAL_ROOF → Template B (roof age, insurance review window)
- NEIGHBOR_ACTIVITY → Template C (neighbor permit activity as social proof)

If a lead has multiple triggers, use the highest-priority one (STORM > NEIGHBOR > AGING).

Every SMS must be under 160 characters. Every email must include:
- Personalized first line referencing their specific situation
- Complimentary photo audit offer
- 972-928-0788 phone number
- Saia's name + RCAT license + IKO Certified (RCAT License #03-0637)

---

## STEP 4 — AIRTABLE UPDATE

For each lead processed:
1. Write to AI Interaction Log: `[DEAL_RESURRECTOR] [timestamp] Lead [NAME] queued. Trigger: [TAG]. Score: [N]. Template: [A/B/C]. Pending Saia review.`
2. Update Last Resurrection Attempt field to today's date
3. Set Resurrection Trigger field to the trigger tag

---

## STEP 5 — SAIA REVIEW PACKAGE

Present a complete package to Saia:

```
🔁 DEAL RESURRECTOR — [DATE]

Dead leads scanned:       [N]
Qualified for contact:    [N]
Storm triggers:           [N]
Aging roof triggers:      [N]
Neighbor activity:        [N]

TOP LEADS READY FOR REVIEW:
  1. [NAME] | [ADDRESS] | Score: [N] | Trigger: [TAG] | Template: [A/B/C]
  ... (up to top 10)

DRAFTS READY:
  ☐ SMS drafts — [N] leads
  ☐ Email drafts — [N] leads

HARD STOP: Saia sends all messages manually. No auto-send.
```

---

## STEP 6 — ARCHIVE

Save the complete run report to:
`C:\PineappleHQ\reports\deal-resurrector\[YYYY-MM-DD].md`

Include: leads scanned, qualified list with scores, storm citation URLs, all draft messages, trigger tags.

---

## GUARDRAILS
- NEVER auto-send any message — Saia sends manually
- NEVER contact leads on DNC list
- 30-day cooldown per lead — check Last Resurrection Attempt
- NEVER fabricate storm data — cite Firecrawl URLs only
- Gemma 4 routing: batch scoring only (non-legal, non-brand content)
- All outputs follow brand lock: Navy #1F3050, Yellow #FFE12D
