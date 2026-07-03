---
name: pineapple-denial-sniper-monitor
description: Twice daily (9 AM / 4 PM) — watch the M7 CRM for Claim Denied leads and draft a Denial Sniper re-engagement (PAUSED).
---

Twice-daily (9 AM & 4 PM) Denial Sniper monitor for Pineapple Contractors M7 (Frisco roofing). DRAFT ONLY — never send.

DATA SOURCE — the new M7 CRM (Airtable is DECOMMISSIONED, do not use it):
C:\Pineapple Contractors M7\02_Workspaces\Pineapple_Mana_Master_CRM_M7.xlsx
Tabs: Master_Lead_Tracker, Google_LSA_Leads.

DO:
1. Read the CRM. Find any lead whose status changed to "Claim Denied" (or similar) since the last run. If none, do nothing and reply "No denials — no action." (no file needed).
2. For each denial, draft a Denial Sniper re-engagement message: empathetic, explains that denied hail claims are often reopened with proper drone-assisted RCAT-certified documentation (RCAT #03-0637), and offers a Complimentary Professional Photo Audit (CPPA) to rebuild the claim. Fill placeholders [Name], [phone].

OUTPUT (only if there are denials): save to C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\<YYYY-MM-DD>_Denial_Sniper.md, marked STATUS: PAUSED — Saia reviews and sends.

BRAND RULES: never "Complimentary" (CPPA), no "Full Restoration Coverage" (Full Restoration Coverage), no "GAF" (IKO Certified), no "The Pineapple Standard/The Pineapple Standard", no green, phone 972-928-0788. End with: Ko e hala 'o e fononga ko e faka'apa'apa. Then a 1-line chat summary.