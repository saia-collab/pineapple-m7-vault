# Hermes routing configuration

**Status:** current
**Last verified against OmniRoute upstream:** 2026-08-22

Hermes is the PM7 planning/orchestration surface. OmniRoute is the model gateway. Do not hardcode remembered Gemini, Claude, DeepSeek, Kimi, GLM, or MiniMax model IDs here; providers and free tiers change.

## Current endpoints

- Hermes dashboard: `http://127.0.0.1:9119`
- Local Studio Hermes tab: `http://127.0.0.1:3737/hermes`
- OmniRoute root for Anthropic clients: `http://127.0.0.1:20128`
- OmniRoute OpenAI-compatible API: `http://127.0.0.1:20128/v1`

## Routing policy

1. Start with `auto/best-chat` for content and general tasks.
2. Use `auto/best-coding` for code and technical changes.
3. Use `auto/best-reasoning` for complex analysis.
4. If a route fails, inspect `/v1/models` and the OmniRoute provider dashboard. Choose only a currently returned model backed by a valid OAuth session, free tier, or API key.
5. A model name appearing in a catalog does not prove the provider is funded or authenticated.

## Verification

Double-click `PM7_REPAIR_AND_VERIFY.bat`. The verifier checks Hermes, OmniRoute, the Studio, Ollama, and the three automatic text routes. Results are written as a dated PAUSED receipt in `01_Command_Center/Outbox_Drafts/`.

Never place an API key or OAuth token in this folder.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
