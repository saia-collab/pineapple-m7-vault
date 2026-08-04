---
type: handoff
title: GSC Setup — Handoff Sheet for [Brother]
status: active
last_updated: 2026-07-13
owner_email: marketing@pineapplecontractors.com
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🤝 Google Search Console Setup — Quick Handoff

**Hey [brother] — I'm connecting our SEO tool (OpenSEO) to our Google Search
Console so it can see how pineapplecontractors.com ranks. You set up our Google
stuff, so I need 3 quick things from you. Should take ~10 minutes.**

Everything below happens in **Google Cloud Console** (console.cloud.google.com)
and **Google Search Console** (search.google.com/search-console), signed in as
**marketing@pineapplecontractors.com**.

---

## ✅ PART A — 3 things I need you to DO

### 1. Grab the "Client Secret" and send it to me
This pairs with the Client ID I already have.
1. Go to **console.cloud.google.com** → sign in as marketing@pineapplecontractors.com
2. Top project picker → make sure you're in the project that has this OAuth ID:
   `86493178999-r22iji8t2smjn6ptf7lm7qngl240nv41.apps.googleusercontent.com`
3. Left menu → **APIs & Services → Credentials**
4. Under **OAuth 2.0 Client IDs**, click the client that starts with `86493178999-…`
5. On the right you'll see **Client secret** → copy it
6. **Send it to me privately** (text/Signal — not a public post). It looks like
   `GOCSPX-xxxxxxxxxxxxxxxxxxxx`

### 2. Add one Redirect URI (same screen)
While you're on that OAuth client page:
1. Find **Authorized redirect URIs** → click **+ ADD URI**
2. Paste EXACTLY this (must match character-for-character):
   ```
   http://localhost:3001/api/gsc/oauth/callback
   ```
3. Click **SAVE**

### 3. Publish the consent screen (so it never logs me out)
1. Left menu → **APIs & Services → OAuth consent screen**
2. If **Publishing status** says **"Testing"** → click **PUBLISH APP** →
   confirm to set it to **"In production."**
   *(Why: while it's "Testing," Google forces a re-login every 7 days. Published
   = stays connected. If Google asks to "verify the app," ignore it — it still
   works for us since it's our own internal tool.)*

---

## ✅ PART B — confirm I can see the data

I need to log in and read our Search Console. Two options — pick whichever is
easier for you:

**Option 1 (simplest):** Tell me you'll log me in with the
marketing@pineapplecontractors.com account when I click "Connect" (you enter the
password on my screen, or we do it together on a call).

**Option 2 (cleaner, no password sharing):** Add MY personal Google account as a
user so I log in as myself:
1. **search.google.com/search-console** → pick the **pineapplecontractors.com**
   property
2. **Settings → Users and permissions → Add user**
3. Enter my email: **__________________** (Saia fills this in)
4. Permission: **Full** → Add

---

## 📋 What to send back to Saia
- [ ] The **Client Secret** (`GOCSPX-…`) — privately
- [ ] "Redirect URI added + Saved" ✅
- [ ] "Consent screen published (In production)" ✅
- [ ] "Search Console access confirmed" (or added your email) ✅

That's it — once I have the secret and you've done the 3 steps, I paste it in and
we're pulling live ranking data. Malo 'aupito, brother. 🍍

<!-- M7-FIREWALL-EXEMPT: internal-handoff -->
