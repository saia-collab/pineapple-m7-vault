# CONTEXT.md — 04_Tech_Lab (ICM Layer 4 — the engine room)
**One job:** run the mechanical scripts (video render, scraping, Meta/Google uploaders). Deterministic — NO AI copywriting happens here. Configs, `.env`, and CLI tools live here.

## Rules
- Scripts read inputs (JSON contracts from `03_Knowledge_Mat`, assets from `02_Media_Vault`) and write outputs to a pipeline `output/` or `Outbox_Drafts/`.
- Anything customer-facing that a script produces is still **PAUSED** — e.g. Meta campaigns upload in a PAUSED state; nothing spends without Saia's GO.
- Keep `.env` / keys here; never print or commit secrets.
- This is where `icm-architect` (installed skill) can scaffold new pipelines with the "walk test".
