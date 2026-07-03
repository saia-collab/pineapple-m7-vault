---
name: pineapple-daily-performance-brief
description: Daily 6 AM brief — Meta ad spend + lead count vs 7-day average, from the new M7 CRM (Google Sheets / xlsx).
---

Daily 6:00 AM performance brief for Pineapple Contractors M7 (Frisco roofing). DRAFT ONLY — never change live spend or publish anything.

DATA SOURCE — the new M7 CRM (Airtable is DECOMMISSIONED, do not use it):
C:\Pineapple Contractors M7\02_Workspaces\Pineapple_Mana_Master_CRM_M7.xlsx
Tabs: Google_LSA_Leads, Master_Lead_Tracker, Attribution, Meta_Ads, Assets.

DO:
1. Read the CRM. From Meta_Ads + Google_LSA_Leads, compute yesterday's: total leads, leads by source, ad spend, and cost-per-lead. Compare each to the trailing 7-day average from the same tabs.
2. Flag anything notable: leads not contacted within 5 minutes (speed-to-lead miss), cost-per-lead over $50, or a day-over-day swing > 30%.
3. If a Meta Ads connector is available, pull live spend to cross-check; if not, use the Meta_Ads tab and note the source.

OUTPUT: a short one-page brief saved to C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\<YYYY-MM-DD>_Daily_Brief.md with a "STATUS: informational — no action taken automatically" banner. Track cost per SIGNED JOB where data allows, not just per click.

BRAND RULES: never "Complimentary" (use CPPA), no "GAF" (use IKO Certified), no "The Pineapple Standard/The Pineapple Standard", no green, phone 972-928-0788. End with: Ko e hala 'o e fononga ko e faka'apa'apa. Then give me a 3-line chat summary.