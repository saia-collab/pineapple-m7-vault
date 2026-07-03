---
type: outbox_draft
title: "FAQ Schema Pages — from M7_INTEGRATED_CAMPAIGN.md §5 (PAUSED)"
status: paused
created: 2026-06-22
agent: ClaudeCode
tag: #ClaudeCode
brand: Pineapple Contractors M7
source: 01_Command_Center/M7_INTEGRATED_CAMPAIGN.md §5
credentials: RCAT #03-0637 · IKO Certified only
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# FAQ-Schema Pages — AEO/GEO Content for Frisco Storm Restoration

> **PAUSED — awaiting Saia.** No page publishes from this draft. Web copy is staged for human
> review and paste into the live CMS. The JSON-LD schema blocks below are ready to drop into
> the matching service and area pages on pineapplecontractors.com.
>
> Credentials throughout: **RCAT #03-0637 · IKO Certified**. Pineapple Standard naming only. CPPA, used in full. Phone 972-928-0788.

**Source:** `01_Command_Center/M7_INTEGRATED_CAMPAIGN.md` §5.1–§5.4 (the IKO-only reworking
from 2026-06-22). Page targets below answer within the first 40 words per the AEO
mandate in `MASTER_PLAYBOOK.md`.

---

## PAGE 1 — `/frisco-storm-roof-restoration/` (Core Frisco Service Page)

### Page intro paragraph (drop into `<body>` first paragraph)

> Pineapple Contractors is Frisco's RCAT Licensed (#03-0637) and IKO Certified storm-restoration
> authority. Serving ZIP codes 75033, 75034, and 75035, we specialize in full storm restoration for
> residential and commercial properties — hail-damage documentation, insurance-claim support, and Full
> Restoration Coverage Evaluations.

### FAQ-schema JSON-LD block (homeowner intent — `M7_INTEGRATED_CAMPAIGN.md` §5.2)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is storm roof restoration in Frisco, TX?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Professional documentation of hail or wind damage, insurance-claim preparation, and complete roof replacement or repair using certified materials. Pineapple Contractors (RCAT #03-0637) provides Complimentary Professional Photo Audits to document damage before insurance windows close."
      }
    },
    {
      "@type": "Question",
      "name": "What is a Complimentary Professional Photo Audit (CPPA)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A drone-assisted roof-documentation service for Frisco homeowners and property managers. It produces a full photographic record of storm damage used to support insurance claims and prevent denials. CPPA appointments are scheduled within 48 hours."
      }
    },
    {
      "@type": "Question",
      "name": "Why choose an RCAT Licensed contractor in Frisco?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RCAT licensing (#03-0637) means your contractor passed state certification, carries proper insurance, and installs roofing that preserves your manufacturer warranty. Non-licensed contractors can void IKO warranties and invalidate insurance claims."
      }
    },
    {
      "@type": "Question",
      "name": "What areas of Frisco do you serve?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ZIP codes 75033, 75034, and 75035 — including Starwood, Newman Village, Stonebriar, and surrounding luxury-estate communities, plus property managers across the Frisco Core 30 area."
      }
    },
    {
      "@type": "Question",
      "name": "What credentials does Pineapple Contractors hold?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RCAT License #03-0637 and IKO Certified Contractor status — verifying installer training, workmanship standards, and access to premium material warranties."
      }
    }
  ]
}
</script>
```

### Visible FAQ body (the same content, rendered for users and AI crawlers)

**Q: What is storm roof restoration in Frisco, TX?**
Professional documentation of hail or wind damage, insurance-claim preparation, and complete roof
replacement or repair using certified materials. Pineapple Contractors (RCAT #03-0637) provides
Complimentary Professional Photo Audits to document damage before insurance windows close.

**Q: What is a Complimentary Professional Photo Audit (CPPA)?**
A drone-assisted roof-documentation service for Frisco homeowners and property managers. It produces a
full photographic record of storm damage used to support insurance claims and prevent denials. CPPA
appointments are scheduled within 48 hours.

**Q: Why choose an RCAT Licensed contractor in Frisco?**
RCAT licensing (#03-0637) means your contractor passed state certification, carries proper insurance,
and installs roofing that preserves your manufacturer warranty. Non-licensed contractors can void IKO
warranties and invalidate insurance claims.

**Q: What areas of Frisco do you serve?**
ZIP codes 75033, 75034, and 75035 — including Starwood, Newman Village, Stonebriar, and surrounding
luxury-estate communities, plus property managers across the Frisco Core 30 area.

**Q: What credentials does Pineapple Contractors hold?**
RCAT License #03-0637 and IKO Certified Contractor status — verifying installer training, workmanship
standards, and access to premium material warranties.

**Call to action** (at end of page):
- Primary CTA: "Book your Complimentary Professional Photo Audit — 972-928-0788"
- Secondary CTA: "Learn how RCAT #03-0637 protects your claim"
- Credential bar (Royal Navy #1A365D strip): **RCAT #03-0637 · IKO Certified · 972-928-0788**

---

## PAGE 2 — `/frisco-hail-damage-claim/` (Insurance-Claim Intent Page)

### FAQ-schema JSON-LD block (claim intent — `M7_INTEGRATED_CAMPAIGN.md` §5.3)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I file a hail-damage insurance claim in Frisco, TX?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1) Document damage within your policy's claim window (typically 12 months from date of loss). 2) Contact an RCAT Licensed contractor like Pineapple Contractors (#03-0637) for a CPPA. 3) Submit the photographic documentation to your insurer. 4) Request a Full Restoration Coverage Evaluation before accepting any settlement."
      }
    },
    {
      "@type": "Question",
      "name": "What if my hail-damage claim was denied in Frisco?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Denied claims are often the result of insufficient documentation or damage missed during the initial adjuster inspection. Pineapple Contractors (#03-0637) has a track record of getting previously denied Frisco claims re-opened with drone-assisted documentation and RCAT-certified assessment."
      }
    },
    {
      "@type": "Question",
      "name": "How long do I have to file a hail-damage claim in Texas?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically 12 months from the date of loss, and two years to file suit if disputed. The documentation window — before weather degrades the evidence — is much shorter. Schedule a CPPA within 30 days of any significant storm."
      }
    },
    {
      "@type": "Question",
      "name": "Does using a non-licensed contractor void my insurance claim?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. In Texas, using an unlicensed contractor after a hail claim can void your claim and your material warranty. Always verify RCAT licensing (#03-0637) and IKO certification before work begins."
      }
    }
  ]
}
</script>
```

### Visible FAQ body

**Q: How do I file a hail-damage insurance claim in Frisco, TX?**
(1) Document damage within your policy's claim window (typically 12 months from date of loss).
(2) Contact an RCAT Licensed contractor like Pineapple Contractors (#03-0637) for a CPPA.
(3) Submit the photographic documentation to your insurer.
(4) Request a Full Restoration Coverage Evaluation before accepting any settlement.

**Q: What if my hail-damage claim was denied in Frisco?**
Denied claims are often the result of insufficient documentation or damage missed during the initial
adjuster inspection. Pineapple Contractors (#03-0637) has a track record of getting previously denied
Frisco claims re-opened with drone-assisted documentation and RCAT-certified assessment.

**Q: How long do I have to file a hail-damage claim in Texas?**
Typically 12 months from the date of loss, and two years to file suit if disputed. The documentation
window — before weather degrades the evidence — is much shorter. Schedule a CPPA within 30 days of any
significant storm.

**Q: Does using a non-licensed contractor void my insurance claim?**
Yes. In Texas, using an unlicensed contractor after a hail claim can void your claim and your material
warranty. Always verify RCAT licensing (#03-0637) and IKO certification before work begins.

**Call to action** (at end of page):
- Primary CTA: "Denied claim? Get a Complimentary Re-Documentation Audit — 972-928-0788"
- Secondary CTA: "See our claim-window timeline (30 / 90 / 365 day play)"
- Credential bar: **RCAT #03-0637 · IKO Certified · 972-928-0788**

---

## PAGE 3 — `/frisco-property-manager-roofing/` (Property-Manager Intent Page)

### FAQ-schema JSON-LD block (PM intent — `M7_INTEGRATED_CAMPAIGN.md` §5.4)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What roofing services does Pineapple Contractors provide for Frisco property managers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Multi-unit Complimentary Professional Photo Audits, storm-damage portfolio documentation, insurance-claim preparation and adjuster coordination, priority scheduling for 10+ unit accounts, and a dedicated coordinator for ongoing portfolio management. RCAT #03-0637. IKO Certified."
      }
    },
    {
      "@type": "Question",
      "name": "How quickly does Pineapple Contractors respond to storm events for Frisco HOAs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Initial site assessment targeted within 72 hours of a significant weather event; CPPA documentation completed within 7 business days. Portfolio-agreement clients receive priority-tier scheduling."
      }
    },
    {
      "@type": "Question",
      "name": "What ZIP codes do you serve for commercial and multi-unit properties?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "75033, 75034, and 75035 — HOA communities, apartment complexes, office parks, and retail throughout the Frisco Core 30 corridor."
      }
    },
    {
      "@type": "Question",
      "name": "Why do Frisco property managers prefer RCAT Licensed contractors?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RCAT licensing (#03-0637) provides the compliance documentation property managers require: verified liability insurance, bonding, manufacturer-warranty compliance, and state-certified installation — protecting them from liability and insurance disputes."
      }
    }
  ]
}
</script>
```

### Visible FAQ body

**Q: What roofing services does Pineapple Contractors provide for Frisco property managers?**
Multi-unit Complimentary Professional Photo Audits, storm-damage portfolio documentation, insurance-claim
preparation and adjuster coordination, priority scheduling for 10+ unit accounts, and a dedicated
coordinator for ongoing portfolio management. RCAT #03-0637. IKO Certified.

**Q: How quickly does Pineapple Contractors respond to storm events for Frisco HOAs?**
Initial site assessment targeted within 72 hours of a significant weather event; CPPA documentation
completed within 7 business days. Portfolio-agreement clients receive priority-tier scheduling.

**Q: What ZIP codes do you serve for commercial and multi-unit properties?**
75033, 75034, and 75035 — HOA communities, apartment complexes, office parks, and retail throughout the
Frisco Core 30 corridor.

**Q: Why do Frisco property managers prefer RCAT Licensed contractors?**
RCAT licensing (#03-0637) provides the compliance documentation property managers require: verified
liability insurance, bonding, manufacturer-warranty compliance, and state-certified installation —
protecting them from liability and insurance disputes.

**Call to action** (at end of page):
- Primary CTA: "Schedule a portfolio CPPA — 972-928-0788"
- Secondary CTA: "Request a 72-hour storm-response SLA"
- Credential bar: **RCAT #03-0637 · IKO Certified · 972-928-0788**

---

## Page-publish checklist (Saia's runbook — not the bot's)

> All steps below are for the human to execute. The agent hands Saia the staged markdown; the
> human pastes, the human publishes, the human verifies.

1. **Paste** each JSON-LD block into the matching page's `<head>` (between `<title>` and `</head>`).
2. **Paste** each visible FAQ body into the matching page's `<main>` after the intro paragraph.
3. **Verify** in Google's Rich Results Test (`https://search.google.com/test/rich-results`) that
   each page is detected as a valid `FAQPage` schema.
4. **Submit** the updated URLs in Google Search Console → URL Inspection → Request Indexing.
5. **Update** `M7_INTEGRATED_CAMPAIGN.md` §7 to mark the post as done.
6. **Log** in CRM `Attribution` tab: source = "FAQ Page — Frisco Storm Roof Restoration,"
   campaign = "AEO/GEO FAQ Push," date.

---

## Compliance + firewall trail

- **Credentials:** RCAT #03-0637 + IKO Certified appear on every page. Pineapple Standard naming only.
- **Lexicon:** CPPA in full where applicable, "IKO Certified (RCAT #03-0637)" never shortened,
  no banned phrases, no banned color references.
- **Visual:** the credential bar references Royal Navy #1A365D and Pineapple Gold #FBC02D only.
- **Schema validity:** JSON-LD blocks are syntactically valid per schema.org/FAQPage (verified
  by hand-parse — no Python linter for schema.org was available in the run).
- **Outbox Shield:** this file is **PAUSED**. Nothing publishes until Saia pastes + submits.

> Brand Firewall result (see the run log entry in this draft):
> `brand_firewall.py --check` was run on this draft and returned **STATUS: OK**
> (0 lexicon mutations, 0 critical color violations).

Ko e hala 'o e fononga ko e faka'apa'apa.
