# 38 · SEO → Parasite SEO — One Keyword, Every Platform (Optional)

> 🛑 **Already built.** This sub-tab ships working inside the **SEO** tab — don't ask an AI to build it. If you don't see it, update your pack (`Update Agent OS.command`).

**Parasite SEO** is keyword arbitrage across platforms: find a search query you (or one platform) already rank for, then recreate that content **platform-native everywhere else** — a thread on X, a Reel on Instagram, a Short on TikTok/YouTube — so you own more of page 1 with the same idea.

It sits on top of your own Google Search Console data (same one-time connection as the Research tab).

## How to use it
1. **Connect your Search Console** once — exactly the same setup as the Research tab: `install/36-SEO-RESEARCH.md`. Already connected? You're done.
2. Open **SEO → Parasite SEO**.
3. Pick a winning query — the tab surfaces queries your sites already rank for.
4. For each platform it hands you a ready **play**: the format (thread / Reel / Short / video) and a **Claude-ready prompt**. Posts and threads route to the **Claude** tab; video formats route to the **Video Director** (Claude writes the script in-pipeline). You create everything inside your Agent OS.

## About Google's "platform properties" (honest note)
In July 2026 Google added **platform properties** to Search Console (Instagram / TikTok / X / YouTube performance on Google Search) — but as of 31 July 2026 they're visible in the GSC **website UI only**, not the API. The moment Google ships API access, this tab **auto-detects** your platform properties and lights them up. Until then it runs the full arbitrage engine off your **website** queries, which works today.

Add your platform accounts as properties in Search Console now (<https://search.google.com/search-console>) so the data's accruing when the API opens.

## Good to know
- **Read-only + private** — same read-only GSC token as the Research tab; nothing posts automatically. You always create + publish yourself.
- **No extra keys** — if Research works, Parasite SEO works.
