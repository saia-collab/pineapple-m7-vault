---
type: setup_card
title: Google Search Console — Connect Once, Stay Connected
status: active
last_updated: 2026-07-13
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🔌 Google Search Console (GSC) — Setup Card

> GSC = your OWN live Google ranking data (free). It feeds the SEO pipeline's
> **Research** step so you write pages that are *this close* to page 1.
> GSC connects **through OpenSEO** (http://localhost:3001) — ignore the old
> "run gsc-report.py" message on the Research tab; that script was never shipped.

## ✅ One-time setup (≈5 min — YOUR part; involves a login + your own secret)

**Step 1 — Paste your Google client secret**
Open `C:\Users\estim\open-seo\.env` and set the line:
```
GOOGLE_CLIENT_SECRET=<paste your secret from Google Cloud Console>
```
(GOOGLE_CLIENT_ID and BETTER_AUTH_SECRET are already set.)

**Step 2 — Register the EXACT redirect URI** (this is what fixes the 403)
Google Cloud Console → APIs & Services → Credentials → your OAuth client →
**Authorized redirect URIs → Add**:
```
http://localhost:3001/api/gsc/oauth/callback
```
Save. (Must match exactly — http, localhost, port 3001, that path.)

**Step 3 — Restart OpenSEO** so it reads the new secret
Dashboard → OpenSEO tab (or restart the open-seo Docker container).

**Step 4 — Connect**
Double-click `04_Tech_Lab\scripts\GSC_Connect.bat` → OpenSEO opens →
**Search Performance** → **Connect Google Search Console** → sign in as
**marketing@pineapplecontractors.com** (the verified owner of the property).

→ Done. It now pulls your live ranking data.

## 🔁 "Always click and login when needed"
- **The button:** `04_Tech_Lab\scripts\GSC_Connect.bat` — pin it to your taskbar
  or copy a shortcut to your Desktop. One double-click = straight to the connect
  screen, any time it asks you to sign in again.
- **The permanent fix (do this so it rarely asks again):** In Google Cloud
  Console → **OAuth consent screen** → set **Publishing status = In production**
  (Published). While it's in "Testing", Google expires the login every **7 days**.
  Published = the login lasts until you revoke it. This is the real "stay logged
  in forever" switch.

## Why I can't do this part for you
Pasting a secret and doing a Google sign-in are credential actions — those are
yours by design. Everything around them is wired; you just paste + click.

<!-- M7-FIREWALL-EXEMPT: setup-card -->
