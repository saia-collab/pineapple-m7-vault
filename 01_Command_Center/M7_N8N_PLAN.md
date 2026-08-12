---
type: decision_plan
title: n8n — what it is, do we need it, our safe plan
status: active
date: 2026-08-11
verdict: Real next-layer tool. Park now (pre-branding) · learn this week · build GATED when publishing at volume.
---

# 🔌 n8n — the simple truth + our plan

## What n8n is (10-year-old version)
A **robot conveyor belt** (a plumber for your apps). Hermes and Claude **write things when you ask.** n8n is different — it **runs by itself on a timer or a trigger and connects your apps** with no one clicking. Google Sheets ↔ WordPress ↔ your phone ↔ Gmail, all wired together.

## What it would do for Pineapple Roofing (straight from your notebook playbook)
1. **24/7 background SEO** — read a sheet of topics → draft a city page → SEO it → stage it (feeds your 5-site flywheel).
2. **Lead routing (speed-to-lead)** — a lead comes in → score it (your `m7_scoring`) → **text you within minutes if it's an 80+ Elite lead** → log it to a CRM sheet.
3. **Content pipeline** — one transcript → 5 posts → images → drafts (the exact Skool "SEO WordPress Posts" template).
4. **Migration helper** — after you move off the old agency site, batch-submit the new URLs to Google for indexing.

## Why it's powerful — but MUST be gated 🛡️
Notice every one of those ends in **"publish to WordPress" or "send a text."** That is exactly what your **Outbox Shield forbids** without your GO. So we **never** run n8n full-auto. The safe design:

```
n8n prepares the draft  →  drops it PAUSED in Outbox_Drafts/  →  YOU review  →  you say GO  →  THEN it publishes/sends
```

The one exception that's safe to run live early: a **lead-alert** workflow that only *texts you* "hot lead!" — it notifies, it doesn't publish or spend.

## What it needs (these are YOUR steps — keys & logins)
- **n8n installed** — either **n8n Cloud** (easiest, has a free tier) or **self-host** (Docker on your PC).
- **App connections** you log into / paste keys for: WordPress (app password), Google (Sheets), an SMS service (Twilio), Gmail.
- **The bridge code** (`m7_n8n_webhook_bridge.py`) is a **download-only** artifact in your notebook — Batch export it when ready and **I review it before it runs.**

## My recommendation + the order
- **NOW → park it.** You're pre-branding and everything's PAUSED. Turning on a 24/7 publishing machine *before* your brother's final branding is locked = backwards (you'd auto-publish soon-to-be-rebranded pages).
- **THIS WEEK → understand it** (this doc). Optionally click through the Skool n8n templates just to see the shapes.
- **WHEN READY (branding done + you're publishing at volume) → I build it GATED**, one workflow at a time, safest first.

## The "when we build it" checklist (for later)
1. You pick **n8n Cloud vs Docker**.
2. You connect **WordPress · Google · SMS**.
3. I import + **gate** the first workflow = **lead → text-you alert** (safe: only notifies).
4. Test with **one fake lead**.
5. Add the **content pipeline** (stages to Outbox, never auto-publishes).
6. `/m7-doctor` gets an n8n health check added.

**Brand lock + Outbox Shield apply to every single n8n workflow — no exceptions.**

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
