# PINEAPPLE CONTRACTORS M7 — COMMAND CENTER RULES

**Status:** active
**Last verified:** 2026-08-22
**Precedence:** `CLAUDE.md` and `03_Knowledge_Mat/SHARED_MEMORY.md` override older playbooks.

## Identity

- Pineapple Contractors / Pineapple Roofing
- Polynesian family-owned
- Frisco, Texas
- RCAT Licensed Roofing Contractor #03-0637
- IKO Certified
- Founded 2021
- `(972) 928-0788`

Do not publish a street address, review count, certification, service territory, or ownership story unless it is verified in a current source.

## Brand and legal rules

- Primary colors: Pineapple Blue `#003299` and Pineapple Yellow `#ffdd17`.
- Green is prohibited in Pineapple brand output.
- "Free roof inspection/estimate" is allowed.
- Never imply free roof work, free repairs, a waived/no deductible, or guaranteed insurance proceeds.
- Use "storm damage report" or "licensed roof inspection report" as the field offer; CPPA is retired.
- Use IKO Certified, never GAF.
- Do not use warrior, toa, six-brothers, or Tongan-proverb positioning.
- Core slogan: "Roofing Made Sweeter" and "The Pineapple Promise."

## Outbox Shield (DEC-005)

Every ad, page, post, email, message, publishing payload, or spend configuration must land PAUSED in `01_Command_Center/Outbox_Drafts/`. No agent may publish, send, post, or spend without Saia's explicit GO.

Run `python 04_Tech_Lab/scripts/brand_firewall.py --check "<copy>"` before staging consumer-facing copy.

## Current operational map

- `M7_START_HERE.md` — business-system overview
- `M7_SYSTEM_RECOVERY_AND_ROUTING_SOP_2026-08-22.md` — current Local Studio and OmniRoute recovery SOP
- `M7_MASTER_SOP_AND_VERIFICATION_MATRIX.md` — historical 2026-08-19 test evidence; re-test before relying on its model counts
- `Outbox_Drafts/` — human-review gate

Historical files remain evidence, not authority, when they conflict with the active boot chain.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
