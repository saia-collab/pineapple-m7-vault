---
type: outbox_draft
status: PAUSED
delivery_channel: SMS / text
send_to: [Customer Phone]
send_when: 3 calendar days after job complete (only if no review left yet)
template_source: M7_LEAD_ENGINE.md — LAYER 2 (3-day nudge)
created_by: Hermes (assistant)
created_on: 2026-06-22
created_for: Pineapple Contractors — Roofing
activation_required: YES — explicit human authorization from authorized operator before send
---

# REVIEW REQUEST — 3-DAY NUDGE (Placeholder: David Thompson)

> ⚠️ **PAUSED.** This draft is staged in `01_Command_Center/Outbox_Drafts/` per Outbox Shield.
> Live activation requires explicit human authorization. Do NOT send until Saia or an
> authorized operator approves.
>
> **Send rule:** only fire this nudge if no Google review has been posted since the
> same-day ask went out.

## Message Body

```
Hi David, no pressure at all — if you had a good experience, a 1-line Google review would
mean the world to our family business: [GOOGLE_REVIEW_LINK]. Thank you!
```

## Placeholder Fields To Fill Before Send

| Field | Value |
| :--- | :--- |
| Customer name | David Thompson (placeholder) |
| Customer phone | [FILL — phone number] |
| Google review link | [FILL — short link from Google Business Profile → Ask for reviews] |

## Brand Firewall Check

- [x] No banned lexicon (no "Free", "Warrior", "Toa", "Six Brothers", "Consultation")
- [x] No pressured CTA — soft ask per template spec
- [x] CPPA / IKO / RCAT credentials not required (review ask only)
- [x] Phone 972-928-0788 not required here (review ask only)
- [ ] **Compliance audit pass:** ___________ (initial)

<!-- M7-FIREWALL-EXEMPT: outbound-staging -->