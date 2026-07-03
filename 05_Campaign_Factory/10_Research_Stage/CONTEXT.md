---
type: stage_contract
room: 10_Research_Stage — Intent Extraction
status: active
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# CONTEXT — 10_Research_Stage — Intent Extraction

**Accepts envelope state:** DRAFT
**Emits envelope state:** READY

## Input Criteria
- Raw Meta webhooks / live search data in input/.

## Output Criteria
- Scored intent profiles (intent.json) in output/.

> Compliance gate: `brand_firewall.py` must return PASS (0 green violations) before any artifact advances. All outbound delivery remains PAUSED (Outbox Shield).

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
