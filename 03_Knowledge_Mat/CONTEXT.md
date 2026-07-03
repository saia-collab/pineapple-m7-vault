---
type: stage_contract
room: 03_Knowledge_Mat — Neural Substrate (RAG)
status: active
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# CONTEXT — 03_Knowledge_Mat — Neural Substrate (RAG)

**Accepts envelope state:** DRAFT
**Emits envelope state:** READY

## Input Criteria
- Unstructured transcripts, field data, historical debriefs (into raw/).

## Output Criteria
- Flattened, deduplicated markdown mapped to 00_Atlas for low-latency RAG.

> Compliance gate: `brand_firewall.py` must return PASS (0 green violations) before any artifact advances. All outbound delivery remains PAUSED (Outbox Shield).

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
