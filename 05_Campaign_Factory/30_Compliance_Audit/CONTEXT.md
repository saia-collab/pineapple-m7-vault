---
type: stage_contract
room: 30_Compliance_Audit — Guardrail Verification
status: active
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# CONTEXT — 30_Compliance_Audit — Guardrail Verification

**Accepts envelope state:** READY
**Emits envelope state:** APPROVED | REJECTED

## Input Criteria
- Draft copy from 20_Copy_Drafting/output/.

## Output Criteria
- 100% brand-compliant approved.json; delivery_state PAUSED.

> Compliance gate: `brand_firewall.py` must return PASS (0 green violations) before any artifact advances. All outbound delivery remains PAUSED (Outbox Shield).


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
