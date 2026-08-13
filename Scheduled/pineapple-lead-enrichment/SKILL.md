---
name: pineapple-lead-enrichment
description: Daily 7:35 AM — enrich new M7 CRM leads with property/roof-age context, drafted notes for Saia to review.
---

Daily 7:35 AM lead enrichment for Pineapple Contractors M7 (Frisco roofing). DRAFT ONLY — write enrichment notes for review; do not change the CRM's live data without flagging it.

DATA SOURCE — the new M7 CRM (Airtable is DECOMMISSIONED, do not use it):
C:\Pineapple Contractors M7\02_Workspaces\Pineapple_Mana_Master_CRM_M7.xlsx
Tabs: Google_LSA_Leads, Master_Lead_Tracker.

DO:
1. Read the CRM and find leads added in the last 24h that lack enrichment (no roof age, property type, or estimated job value).
2. For each, draft an enrichment note: likely property type, ZIP/neighborhood (Starwood / Newman Village / Stonebriar = luxury estate; multi-unit = property manager), estimated job-value band vs the $18K+ qualification floor, and which 1-3-12 avatar it maps to (Local Fan / Culture Seeker / Founder's Circle). If a property-data connector is available use it; otherwise infer from ZIP and note it's an estimate.

OUTPUT: save to C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\<YYYY-MM-DD>_Lead_Enrichment.md with a banner "STATUS: draft notes — Saia approves before any CRM edit."

BRAND RULES: never "Complimentary" (CPPA), no "GAF" (IKO), no "The Pineapple Standard/The Pineapple Standard", no green, phone 972-928-0788. End with: . Then a 3-line chat summary.