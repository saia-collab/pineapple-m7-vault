# PM7-004 Codex -> OpenAI (ChatGPT subscription) Cutover — BLOCKED

- Run: 20260816-145338
- Result: BLOCKED (auth + config succeeded; no OpenAI model runs on this ChatGPT account via Codex)

## Config changes (user level, backed up first)
- Backup: C:\Users\estim\.codex\config.toml.PM7-004-backup-20260816-144801 (hash-verified copy of original)
- Primary (top of ~/.codex/config.toml): model = "gpt-5.6", model_provider = "openai", model_reasoning_effort = "medium", approval_policy = "on-request", sandbox_mode = "workspace-write"
- Ollama preserved as opt-in READ-ONLY reviewer: [profiles.ollama-reviewer] (model minimax-m3:cloud, provider ollama-launch-codex-app, sandbox read-only). Invoke: codex --profile ollama-reviewer
- Ollama NOT uninstalled; its data untouched; it is NOT the primary.

## Authentication
- ChatGPT subscription sign-in: SUCCESS ("Logged in using ChatGPT"). auth.json present, ChatGPT tokens.
- No OpenAI API key requested or created (used codex login, not --with-api-key).

## Read-only test (PM7 root)
- workdir: C:\Pineapple Contractors M7 (correct), provider: openai, model shown: gpt-5.6.
- Model CALL FAILED: 400 invalid_request_error - "The 'gpt-5.6' model is not supported when using Codex with a ChatGPT account."
- Diagnostic probes (read-only) also failed identically: gpt-5-codex -> 400 unsupported; gpt-5 -> 400 unsupported.
- Conclusion: this ChatGPT account/plan does not currently grant Codex model access (plan-level entitlement), not a model-name error.

## PASS-criteria status
- ChatGPT subscription authentication ....... PASS
- OpenAI provider shown ..................... PASS (provider = openai)
- GPT-5.6 shown ............................. shown in config/runtime, but NON-FUNCTIONAL (400 unsupported)
- Correct PM7 root .......................... PASS (workdir C:\Pineapple Contractors M7)
- Project .codex not repurposed (by me) ..... PASS (no provider config/credentials/memory added to project .codex)
  FLAG: project .codex\CODEX_SOP already contains pre-existing business SOPs + Brand DNA (NAA_SIONE_BRAND_VOICE.md, handoffs). NOT created by this task; left untouched for your decision.
- Ollama not primary ....................... PASS (primary = openai; Ollama only in reviewer profile)

## RESULT: BLOCKED

## SAFEST REPAIR RECOMMENDATION (recommendation only)
Root cause: On this ChatGPT account, Codex rejects every OpenAI model (gpt-5.6, gpt-5-codex, gpt-5) with "not supported when using Codex with a ChatGPT account." That means the account's ChatGPT plan does not currently include Codex model access.
Fix (in order):
1. Verify the ChatGPT plan includes Codex: sign in at chatgpt.com with the same account and confirm Codex is enabled for the plan tier (Plus/Pro/Business). If Codex is not enabled/available, enable/upgrade it. Then re-run the read-only test - the config here already targets openai/gpt-5.6 and will work once the plan grants access.
2. If the plan is correct but a specific model is required, select the exact Codex model the account exposes and set it as model (user level).
3. Do NOT use an OpenAI API key (per PM7-004 rule). The API-key path would bypass the subscription and is explicitly out of scope.
Interim: Codex currently 400s on the default model until plan access is resolved. The Ollama reviewer profile still works locally (codex --profile ollama-reviewer). Original config backup exists if you choose to revert.

## Guardrails honored
Docker left stopped (not started/repaired). No API key created. No WordPress, Outbox content, Agent OS, GitHub, or public-content changes. Only ~/.codex/config.toml (user level) changed, with a verified backup. Nothing added to the project .codex folder.
