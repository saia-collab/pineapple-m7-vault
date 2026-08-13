---
type: content_factory_sop
title: M7 Content Factory — 39GB Media → Viral Hooks → Lead Ads
status: active
last_updated: 2026-06-19
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 CONTENT FACTORY — TURN MEDIA INTO LEADS

You have drone footage, before/afters, a VSL, and client testimonials. This turns them into a
steady stream of short, hooky ads. Tools: **Higgsfield** (AI video — clipping, virality scoring,
reframe), your **shot-builder / clip skills**, `video-multiplier.py`, the **50/5/3 engine**, and the
**brand firewall**. Everything outputs PAUSED → you post.

## THE PIPELINE (raw → ad)
```
01_RAW_INTAKE → m7_media_index.py (know what you have)
   → IDENTIFY viral moments (Higgsfield virality predictor + the hook rubric below)
   → CLIP to 8-15s vertical (Higgsfield auto-clipper / personal_clipper, reframe 9:16)
   → 50/5/3 assembly (hook 0-15 frames · body · 3s end card)
   → HOOK + caption + Navy/Gold overlay + CPPA CTA + 972-928-0788 (NO green)
   → brand_firewall.py --fix on captions
   → 04_READY_TO_POST → Outbox_Drafts (PAUSED) → you post 4 ways
```

## STEP 1 — FIND THE VIRAL PARTS (don't post whole videos)
**For drone/before-after:** the wow moment is the *reveal* — the cut from damaged → restored. Clip 3s before + 5s after.
**For the VSL + testimonials:** run each through **Higgsfield's virality/analysis** to score segments,
then keep the highest-energy 8-15s. If doing it by eye, use this rubric — a clip is ad-worthy if it has:
- **Pattern interrupt in first 1.5s** (motion, bold claim, a face mid-sentence).
- **An emotional/relatable line** ("I thought my claim would be denied…").
- **A specific number** ("$0 out of pocket" → say "Full Restoration Coverage"; "47 hail hits"; "2 days").
- **A transformation** (stress → relief; old roof → new roof).
- **A quotable objection-handler** ("two other roofers said it wouldn't qualify — they were wrong").

## STEP 2 — MINE TESTIMONIALS FOR "MONEY QUOTES" (copy-paste prompt)
Feed a testimonial transcript to your AI (NotebookLM/Gemini/Higgsfield analysis):
```
Here is a client testimonial transcript. Extract the 5 strongest 8-15 second clips for a roofing
ad. For each: the exact quote, start/end timestamp, why it converts (emotion/proof/objection), and a
3-5 word on-screen hook. Brand rules: never use "free"→ say CPPA; never "$0 down"→ "Full Restoration
Coverage"; no green. Output a table.
```
Save the output to `02_SORTED_PROJECTS/Testimonials/<name>_clips.md`.

## STEP 3 — BULK EDIT (Higgsfield + skills)
- **Higgsfield:** auto-clip the scored segments, reframe to 9:16, captions on.
- **shot-builder skill / video-multiplier.py:** batch the cuts into the 50/5/3 format and stamp the
  brand overlay (Pineapple Gold top hook, Royal Navy bottom credential bar, CPPA + phone end card).
- One source video → many cuts (different hooks) for A/B testing.

## STEP 4 — THE HOOK BANK (reuse what works)
Keep a running list in `10_STRATEGY/hook_bank.md`. Start it from your winners:
- "Your roof has damage you can't see from the driveway."
- "Same storm. Two houses. One filed a claim."
- "I thought my claim would be denied. They proved me wrong." (testimonial)
- "29 days left on your Frisco claim window."
- "We treat your home like family — that's Tauhi Vā."
When an ad wins (>1.5% CTR), add its hook here. When one flops, retire it.

## STEP 5 — DEPLOY EACH ASSET 4 WAYS
GBP photo/video post · Reel/TikTok · YouTube Short · Meta ad creative (Storm Launch campaign).
Log which hook + clip drove leads in the CRM → that's your data for the weekly_review skill.

## WEEKLY CADENCE (realistic, ADHD-friendly)
- Pick **5 clips/week** (don't touch all 39GB). 1 testimonial + 2 before/after + 1 drone + 1 culture.
- Batch-edit in one Higgsfield session. Caption + firewall. Stage PAUSED.
- Post across the 4 surfaces. Done.

## GUARDRAIL
Higgsfield "Advantage+"-style auto-enhancements OFF for brand control. No green, no banned terms —
the firewall checks every caption. All ad spend stays human-approved (Outbox Shield).


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
