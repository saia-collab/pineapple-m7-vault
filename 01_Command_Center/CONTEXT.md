---
type: stage_contract
room: 01_Command_Center — Strategic Brain
status: active
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# CONTEXT — 01_Command_Center — Strategic Brain

**Accepts envelope state:** n/a
**Emits envelope state:** READ-ONLY

## Input Criteria
- Authorized strategic updates from the Lead Systems Architect only.

## Output Criteria
- Immutable, read-only .md rulesets for all local agents to ground against.

> Compliance gate: `brand_firewall.py` must return PASS (0 green violations) before any artifact advances. All outbound delivery remains PAUSED (Outbox Shield).

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
