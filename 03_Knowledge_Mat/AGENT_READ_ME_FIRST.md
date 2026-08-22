---
INTENT: Non-negotiable M7 agent anchor
type: agent_anchor
last_verified: 2026-08-22
status: ACTIVE
authority: CLAUDE.md + CONTEXT.md + SHARED_MEMORY.md
---

# AGENT — READ ME FIRST

## Identity and verified constants

Pineapple Contractors is a Polynesian family-owned roofing and construction company based in Frisco, Texas. Use RCAT Licensed Roofing Contractor #03-0637, IKO Certified, founded 2021, and `(972) 928-0788`. Do not invent or revive an older founding year, manufacturer credential, address, review count, or family-story claim.

## Required execution loop

1. Read `CLAUDE.md`.
2. Read root `CONTEXT.md` and enter only the room needed.
3. Read `SHARED_MEMORY.md` for current decisions.
4. Work only inside `C:\Pineapple Contractors M7` unless Saia explicitly directs otherwise.
5. Stage outbound work PAUSED in `01_Command_Center/Outbox_Drafts/`.
6. Run the brand firewall and relevant technical tests.
7. Log what was actually tested; label anything else NOT TESTED.
8. Wait for Saia's explicit GO before publishing, sending, or spending.

## Brand rules

| Rule | Current value |
|---|---|
| Primary color | Pineapple Blue `#003299` |
| CTA color | Pineapple Yellow `#ffdd17` |
| Prohibited color | green |
| Approved manufacturer | IKO Certified |
| Approved CTA | free roof inspection/estimate |
| Prohibited inducements | free work/repairs, waived or no deductible, guaranteed claim payout |
| Field offer | storm damage report / licensed roof inspection report |
| Retired positioning | CPPA, GAF, warrior, toa, six brothers, proverbs, since 2005 |

## Model and routing rules

- OmniRoute is the primary model gateway at `http://127.0.0.1:20128`.
- Discover providers and model IDs from the running gateway; do not rely on old screenshots or hardcoded provider names.
- Prefer `auto/best-chat`, `auto/best-coding`, and `auto/best-reasoning` when available.
- Provider access depends on current free tiers, OAuth sessions, or API keys and is never guaranteed by a model name alone.
- Ollama is an optional lightweight local fallback on the 16 GB Windows computer. Never auto-download a large model.
- Never store tokens in Markdown, Python, BAT, JSON, Git, or receipts.

## Outbox Shield

No agent may call a send, publish, post, deploy, or ad-spend API without explicit human authorization. A technically successful draft is still PAUSED.

## Historical-conflict rule

Files containing retired Navy/Gold/Cyan, CPPA, "since 2005," GAF, proverb, warrior/toa, or six-brothers rules are reference material only unless a newer signed decision explicitly reactivates them.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
