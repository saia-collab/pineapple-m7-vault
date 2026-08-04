---
type: tool_setup
title: OpenSEO — install, wiring, and the one key to add
status: installed_running
last_updated: 2026-07-06
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🔍 OpenSEO — INSTALLED & RUNNING (free self-hosted Semrush/Ahrefs)

**What it is:** the official open-source OpenSEO (github.com/every-app/open-seo) — keyword research, rank
tracking, backlinks, and site audits. No subscription; you pay only DataForSEO's per-use API cost.

## ✅ Status (2026-07-06)
- **Installed at:** `C:\Users\estim\open-seo` (this is the `~/open-seo` path the dashboard expects).
- **Running:** Docker container `open-seo-open-seo-1` on **http://localhost:3001** (HTTP 200).
- **Dashboard-connected:** the Agentic OS **SEO → OpenSEO** tab now shows "running" and embeds it.
- **Auto-starts:** `restart: unless-stopped` — comes back automatically when Docker Desktop starts.
- **Auth:** `AUTH_MODE=local_noauth` (local trusted admin — no login needed on your machine).

## 🔑 THE ONE ACTION FOR SAIA — add your DataForSEO key
OpenSEO runs, but keyword/backlink/rank data needs a DataForSEO key (new accounts get **$1 free credit**).
1. Sign up: **https://app.dataforseo.com/register** (do this yourself — never let an AI create the account).
2. Copy your **API credentials** (login + password) from the DataForSEO dashboard.
3. Open `C:\Users\estim\open-seo\.env` and set the line (OpenSEO's onboarding screen shows the exact format
   it wants — usually `login:password`):
   ```
   DATAFORSEO_API_KEY=your_login:your_password
   ```
4. Restart it: open a terminal and run:
   ```
   cd ~/open-seo
   docker compose up -d
   ```
5. Reload the dashboard **SEO → OpenSEO** tab — keyword research is now live.

## 🕹️ Managing it (rare — it auto-restarts)
| Goal | Command (in `~/open-seo`) |
|------|---------------------------|
| Start / apply new key | `docker compose up -d` |
| Stop | `docker compose down` |
| View logs | `docker compose logs -f` |
| Update to latest | `docker compose pull && docker compose up -d` |

## 🧭 How it fits M7
- Use OpenSEO for **keyword ideas + competitor/backlink data** feeding the SEO city-page batches.
- Use **Google Search Console** (dashboard Research tab, free) for **your own** live ranks once the site
  is published — see `01_Command_Center/M7_SEO_TRACKER.md`.
- Everything drafts PAUSED to Outbox; Saia publishes. OpenSEO reads data only — it never posts or spends
  beyond the DataForSEO per-query cost you control.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
