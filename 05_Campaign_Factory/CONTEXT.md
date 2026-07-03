---
type: stage_contract
room: 05_Campaign_Factory — Assembly Line
status: active
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# CONTEXT — 05_Campaign_Factory (Assembly Line)

The factory runs a strict 3-stage asynchronous pipeline. Work advances only when it meets the next stage's input contract and passes the brand firewall.

**Pipeline:** `10_Research_Stage → 20_Copy_Drafting → 30_Compliance_Audit → 01_Command_Center/Outbox_Drafts (PAUSED)`

## Stage contracts
- **10_Research_Stage** — INPUT: raw Meta webhooks / search data (`input/`). OUTPUT: scored intent profiles (`output/intent.json`), state READY.
- **20_Copy_Drafting** — INPUT: scored intent. OUTPUT: unverified copy blocks (`output/draft_copy.json`), compliance_prechecked.
- **30_Compliance_Audit** — INPUT: draft copy. OUTPUT: `approved.json` (100% compliant) + PAUSED drafts written to Outbox_Drafts.

## Gate rules
- Every artifact travels in the universal envelope (see `01_Command_Center/CROSS_AGENT_PROTOCOL.md`).
- `firewall_pass` must be true and `green_violations` zero to advance.
- Delivery state stays PAUSED until human authorization (Outbox Shield).

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
