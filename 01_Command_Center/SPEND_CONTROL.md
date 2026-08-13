---
type: spend_control_policy
status: active
last_updated: 2026-06-18
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 — AD SPEND CONTROL & DOUBLE-DOWN POLICY

You launch manually, with a hard cap, then let the data decide where money goes.

## Hard rules (never automated)
- **Human pulls the trigger.** No agent sets a campaign to ACTIVE. You publish in Meta yourself.
- **Weekly cap:** $250 CBO. Absolute max CPL $250; target CPL < $50.
- **Advantage+ creative:** OFF (protects palette + brand).

## The data loop (track → double down)
Run every Monday (or let the daily sync surface it):
1. Pull last-7-day CTR + CPL per creative/avatar from Meta.
2. Feed into the scorer: `python 04_Tech_Lab\Scripts\m7_scoring.py --campaign <export>.json`.
3. Apply the rules the engine returns:
   - **1% Kill** — CTR < 1.0% after 48h or 1,000 impressions → PAUSE it.
   - **1.5% Scale** — CTR > 1.5% AND CPL < $50 → increase budget weighting +15%.
4. **Double-down:** shift the freed budget to the winning avatar/angle. The dashboard sparklines
   show the trend; the avatar with the steepest CTR climb gets the next $ first.
5. Log the week to `04_Tech_Lab\logs\` so the daily sync charts it over time.

## What "winning" looks like
- Cost per CPPA booked, not just clicks. A $40 CPL that books $18k+ jobs beats a $20 CPL that doesn't.
- Track booked-CPPA → signed-job rate per avatar. Double down on the avatar that converts to signed restoration work.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
