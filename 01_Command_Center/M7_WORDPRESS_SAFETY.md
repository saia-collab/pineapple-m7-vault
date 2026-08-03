---
type: website_safety_sop
title: M7 WordPress Safety — agents never touch the live site
status: active
last_updated: 2026-08-03
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🛡️ WORDPRESS SAFETY — THE OUTBOX SHIELD APPLIES TO THE WEBSITE TOO

**Site:** `pineappleroofingllc.com` (in-house WordPress) · Reference: `pineapplecontractors.com` (Scorpion-built)
**Phone:** 972-928-0788 · RCAT #03-0637 · IKO Certified

## What went wrong (2026-08-03)
An AI agent was told to make `pineappleroofingllc.com` look like the Scorpion site.
It over-edited the live homepage and the **header and footer disappeared site-wide** —
the classic result of a page template being switched to **Canvas / Blank / Full-Width**,
which strips the theme's header/footer for a page builder that never rebuilt them.
The pages and data survived; only the site "frame" was knocked off.

**This is the reason breaking off from Scorpion felt unsafe: the agent had direct
write-access to the live site and did too much.** The fix is not a better agent — it
is the same rule the rest of M7 already runs on.

## THE HARD RULE (non-negotiable, like the Outbox Shield)
> **No AI agent edits the live website directly. Ever.**
> Agents produce a *draft change* → a human reviews it → a human applies it in WP Admin.

Concretely:
1. **Revoke standing write access.** If an agent/MCP/plugin holds a WordPress
   **Application Password** or admin login, remove it (WP Admin → Users → your user →
   Application Passwords → Revoke). Agents get access only for a supervised, one-off task.
2. **Always work on staging, never production.** Most hosts offer a 1-click **staging**
   site. Changes get made and reviewed there, then pushed live by a human.
3. **Back up before any change.** Install **UpdraftPlus** (free) → set daily backups →
   take a manual backup immediately before touching anything. This turns any future
   mistake into a 10-minute restore.
4. **Website drafts land PAUSED**, same as content: the agent writes the copy/layout
   change to `01_Command_Center/Outbox_Drafts/` and says exactly what to click. Saia applies it.

## RECOVERY PLAYBOOK (header/footer gone, or site broken)
In order — stop at the first one that works:
1. **Restore from host backup.** Host control panel → Backups → Restore a point
   *before* the edit. Fastest, safest.
2. **Restore from UpdraftPlus** (if installed): Settings → UpdraftPlus → Restore.
3. **Reset the page template:** WP Admin → Pages → Home → sidebar **Template** →
   change from Canvas/Blank/Full-Width back to **Default Template** → Update.
4. **Re-select the theme:** Appearance → Themes → activate the correct theme; then
   Appearance → Editor/Customize → confirm Header and Footer template parts are assigned.
5. **If a page builder (Elementor/Divi) was used:** check its Theme Builder →
   Header and Footer templates are still "published" and set to display site-wide.

## BRAND NOTE (fix while you're in there)
The current homepage says **"FREE Quote"** repeatedly. "Free" is banned lexicon.
Replace with **Complimentary Professional Photo Audit (CPPA)** wording (see
`M7_WEBSITE_SEO_FIXLIST.md`). Do this as a *human edit*, not an agent free-run.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
