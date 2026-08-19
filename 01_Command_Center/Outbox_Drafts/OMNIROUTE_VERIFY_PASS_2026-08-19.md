---
title: OmniRoute Verification — PASS receipt
status: PASS — verification only, no content published. Outbox Shield intact.
date: 2026-08-19
scope: /goal "verify OmniRoute + default aliases route to auto/best-chat + brand firewall check + PASS receipt"
---

# 🍍 OmniRoute Verification — PASS

| Check | Result |
|---|---|
| OmniRoute gateway `http://127.0.0.1:20128/v1/models` | ✅ **PASS** — HTTP 200 |
| Model catalog | ✅ **177 models** live |
| Default auto-routers present | ✅ `auto/best-chat`, `auto/best-coding`, `auto/best-reasoning`, `auto/best-fast`, `auto/best-vision` + more — **no combo setup needed**, use `auto/best-chat` as the default alias |
| Live free generation (earlier today) | ✅ generated 3 GBP posts at **$0** (routed `big-pickle`) → `Outbox_Drafts/SEO_Posts/2026-08-19_GBP_PostPack_hail-season_OMNIROUTE_PAUSED.md` |
| Brand firewall (`brand_firewall.py --check`) | ✅ **PASS** — "free roof inspection" allowed, IKO/storm-damage-report clean, current-brand (#003299/#ffdd17) rules intact |
| Firewall integrity | ✅ on-disk firewall is the **correct Naa Sione version** (NOT the old-brand CPPA version from the Downloads handoff) |

**Default alias to use everywhere:** `auto/best-chat` (writing), `auto/best-coding` (code). Base URL `http://127.0.0.1:20128/v1`, any dummy key.

**STATUS: PASS — PAUSED_PENDING_HUMAN_REVIEW.** No content published, no spend, Outbox Shield intact.

<!-- M7-FIREWALL-EXEMPT: verification receipt -->
