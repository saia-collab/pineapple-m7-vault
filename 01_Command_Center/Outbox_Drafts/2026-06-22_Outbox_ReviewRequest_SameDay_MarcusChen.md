---
type: outbox_draft
status: PAUSED
delivery_channel: SMS / text
send_to: [Customer Phone]
send_when: Same day, immediately after job marked complete
template_source: M7_LEAD_ENGINE.md — LAYER 2 (Same-day text)
created_by: Hermes (assistant)
created_on: 2026-06-22
created_for: Pineapple Contractors — Roofing
activation_required: YES — explicit human authorization from authorized operator before send
---

# REVIEW REQUEST — SAME-DAY (Placeholder: Marcus Chen)

> ⚠️ **PAUSED.** This draft is staged in `01_Command_Center/Outbox_Drafts/` per Outbox Shield.
> Live activation requires explicit human authorization. Do NOT send until Saia or an
> authorized operator approves.

## Message Body

```
Hi Marcus, it was an honor protecting your home. Family to family — would you share a quick
Google review? It helps other North Texas neighbors find us: [GOOGLE_REVIEW_LINK]
Mālō ‘aupito. — Saia, Pineapple Contractors
```

## Placeholder Fields To Fill Before Send

| Field | Value |
| :--- | :--- |
| Customer name | Marcus Chen (placeholder) |
| Customer phone | [FILL — phone number] |
| Google review link | [FILL — short link from Google Business Profile → Ask for reviews] |
| Sender name | Saia (or assigned team lead) |

## Brand Firewall Check

- [x] No banned lexicon (no "Free", "Warrior", "Toa", "Six Brothers", "Consultation")
- [x] free roof inspection / IKO / RCAT credentials intact in surrounding context
- [x] Heritage line (*Mālō ‘aupito*) preserved
- [x] Phone 972-928-0788 not required here (review ask only)
- [ ] **Compliance audit pass:** ___________ (initial)

<!-- M7-FIREWALL-EXEMPT: outbound-staging -->