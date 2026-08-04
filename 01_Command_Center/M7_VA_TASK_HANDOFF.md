---
title: M7 Virtual Assistant Task Handoff — Daily / Weekly / Monthly
type: operational_sop
status: active
for: Virtual Assistant · Saia · Naa Sione (owner oversight)
last_updated: 2026-08-04
brand_rules: CPPA (never "free") · IKO Certified (never "GAF") · RCAT #03-0637 · zero green · Outbox Shield
purpose: Free the brothers to run field operations. Every task below is tedious, repeatable, and does NOT require field expertise.
---

# 🍍 M7 VIRTUAL ASSISTANT — TASK HANDOFF

**Rule of the handoff:** the VA drafts, the brothers approve. Nothing goes live without a "GO" from Saia or Naa Sione. Every draft lands in `01_Command_Center/Outbox_Drafts/` first.

**Skills the VA needs:** English writing, Google Business Profile access, Gmail, Excel/Sheets, phone politeness. No SEO experience needed — the vault does the thinking; the VA does the doing.

---

## 🌅 DAILY TASKS (Monday–Saturday, ~90 min total)

### 1. Lead intake sweep (15 min, first thing AM)
- Open Gmail, GBP Messages, Facebook DMs, Instagram DMs, website contact form, LSA inbox.
- For every new inquiry, log the following in the CRM sheet within 15 minutes of receipt:
  - Name · Phone · Address/city · Source (GBP / LSA / Facebook / Site / Referral) · Type (Storm / Repair / Replacement / Insurance / Other) · Timestamp received
- **If it's a hot lead** (storm damage, active leak, insurance claim), immediately text or call Saia/Naa Sione so a brother can dial back within 5 minutes.
- Non-urgent leads: send the standard first-touch reply within 15 minutes (template in `01_Command_Center/Outbox_Drafts/Scripts/`).

### 2. Google Business Profile review responses (15 min)
- Check GBP for new reviews.
- For 4-5 star reviews: use `03_Knowledge_Mat/active_context/skills/gbp_review_responder.md` — paste the review into the AI tool, get the reply, drop into `Outbox_Drafts/Reviews/` as a dated file, ping Saia in Slack/text for GO, then post.
- For 1-3 star reviews: **do NOT reply.** Text Saia immediately with the full review text and reviewer name. Brothers handle negative reviews personally.

### 3. Photo intake from the field (10 min)
- Check the "Field Photos" folder in Google Drive (crews upload here from job sites).
- Rename each folder using the pattern: `YYYY-MM-DD_City_ServiceType_LastName` (e.g., `2026-08-04_Frisco_HailInspection_Nguyen`).
- Move unusable photos (blurry, no context, personal identifiers visible) to `_TRASH/` subfolder.
- Add a one-line note per job to `02_Media_Vault/PHOTO_LOG.md`: date, city, service, whether it's ready for social use.

### 4. Speed-to-lead audit log (5 min, end of day)
- Open the CRM sheet, look at every lead received today.
- For each: enter the actual first-response time (in minutes). Flag any over 5 minutes in red so brothers can debug tomorrow.

### 5. Calendar prep (10 min, end of day)
- Confirm tomorrow's CPPA appointments via text: "Hi [Name], confirming Pineapple Roofing will be at [address] tomorrow at [time] for your Complimentary Professional Photo Audit. Reply YES to confirm or call (972) 928-0788 to reschedule."

---

## 📅 WEEKLY TASKS (specific day, ~3-4 hours total)

### Monday morning — Lead scorecard (30 min)
- Tally last week from the CRM sheet: total leads by source · average response time · appointments booked · jobs closed.
- Email Saia and Naa Sione the one-page scorecard by 9:00 AM Monday.

### Monday afternoon — GBP post drafting (45 min)
- Pick 2 approved photos from last week's job log.
- Use `03_Knowledge_Mat/active_context/skills/blog_to_gbp.md` — paste an existing blog or job description, get 2 GBP posts back.
- Drop drafts in `01_Command_Center/Outbox_Drafts/` marked `STATUS: PAUSED`, ping Saia for GO.

### Tuesday — Photo upload to GBP (30 min)
- Once Saia approves, upload 5-10 approved photos to the Google Business Profile (goal: 100+ real photos on GBP over time).
- Geotag if not already geotagged. Add short caption using neighborhood name when known.

### Wednesday — Review request sweep (45 min)
- Pull the list of jobs completed 3-7 days ago from the CRM.
- For each satisfied customer (crew flagged them 👍), send the review request text:
  - "Hi [Name] — this is [VA Name] with Pineapple Roofing. Thank you for trusting us with your roof! If you have 60 seconds, we'd love a Google review: [SHORT LINK]. Every honest review helps our family business. — Saia & Naa Sione"
- Log which customers were asked in the CRM (avoid re-asking).

### Thursday — Social schedule (60 min)
- Pull 3-5 approved video clips or before/after carousels from `02_Media_Vault/`.
- Draft captions in Blotato using the approved Hormozi format (Dream Outcome → Obstacle → Mechanism/CPPA → Proof → CTA). Schedule for FB / IG / TikTok / LinkedIn.
- Everything stays PAUSED in Blotato until Saia approves the batch.

### Friday — Weekly close (30 min)
- Confirm every hot lead from the week has been dispositioned (booked / lost / pending).
- Reply to any unanswered DMs / emails older than 24 hours.
- Send Saia a short "week-in-review" text: leads received · booked · lost · biggest miss · one question for the brothers.

---

## 📆 MONTHLY TASKS (first week of each month, ~4-6 hours total)

### 1. NAP consistency audit (60 min)
- Open a checklist of directories (GBP, Bing Places, Yelp, BBB, Angi, Houzz, Nextdoor, Facebook page, LinkedIn page).
- Verify Name / Address / Phone match EXACTLY on every one. Flag mismatches for Saia — do not edit yourself.
- Verify RCAT #03-0637 and IKO Certified are present wherever credentials are shown.

### 2. Review request follow-up sweep (45 min)
- Pull all customers asked for a review 3+ weeks ago who haven't left one.
- Send ONE polite follow-up: "Hi [Name] — just checking in. If you have a spare minute, a quick Google review means the world to our family. If not, no worries at all — we appreciate you either way."
- Do not follow up a second time.

### 3. GBP insights export (30 min)
- Export GBP Insights (calls, direction requests, website clicks, photo views) as CSV.
- Save to `02_Workspaces/GBP_Insights/YYYY-MM.csv`.
- Add the monthly totals to the running scorecard.

### 4. Photo library cleanup (60 min)
- Audit `02_Media_Vault/` — archive anything older than 12 months to `_ARCHIVE/YYYY/`.
- Delete confirmed duplicates (same job, near-identical shot).
- Make sure `PHOTO_LOG.md` matches the folder reality.

### 5. Content batch prep (90 min)
- With Saia, pick 5-10 completed jobs worth turning into content (variety across storm / repair / replacement / commercial / heritage).
- Draft the raw material (job story, crew photo names, customer quote if available) into `Outbox_Drafts/Content/YYYY-MM_content_pool.md`.
- Brothers will approve the pool at the start of the next month.

### 6. Directory citation refresh (60 min, only if flagged)
- If any mismatches were found in Task #1, prepare a change-request checklist for Saia. Do not submit changes to directories directly — some require verification codes that only the owner should handle.

---

## 🚫 WHAT THE VA DOES NOT DO

To protect brand integrity and the family's voice, the VA does NOT:
- Reply to negative reviews (brothers only)
- Publish anything live — every draft is PAUSED until GO
- Handle insurance claim conversations (brothers only — legal and technical stakes too high)
- Quote prices or make service commitments to leads
- Change GBP settings, hours, service areas, or categories
- Post to Google LSA (that's Saia/Naa Sione)
- Speak on behalf of the brothers in DMs — always identify as VA
- Delete anything from the vault or Google Drive without written approval

---

## 📞 ESCALATION TREE

| Situation | Text who? |
|---|---|
| Storm hits DFW / hail event | Both brothers immediately |
| Insurance adjuster reaches out | Naa Sione |
| Negative review (1-3 stars) posted | Saia |
| Lead older than 5 min without callback | Saia (with lead's phone number) |
| Photo/video approval question | Saia |
| Anything about branding or wording | Wait for Naa Sione's brand markdown, then ask Saia |
| Tool broken / login won't work | Saia |

---

## ✅ ONBOARDING CHECKLIST FOR THE VA (first week)

- [ ] Read this document top-to-bottom
- [ ] Read `01_Command_Center/CLAUDE.md` for brand law (never "free" / no green / RCAT #03-0637)
- [ ] Get logins: Gmail (VA account), GBP manager access, Blotato, CRM sheet
- [ ] Shadow Saia on 3 lead intakes to see the tone
- [ ] Shadow Saia on 3 review responses
- [ ] Do the first week WITH Saia sitting next to you before running solo

**Goal by end of month 1:** the brothers stop touching daily lead intake, review responses, and GBP posts — they only touch the GO button.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
