---
type: seo_pipeline_output
title: Goldie SEO Pipeline — Week 1 & 2 (GBP Audit · Reviews · Schema)
status: PAUSED — review, then apply to GBP + WordPress
brand_check: free roof inspection (no "free") · IKO Certified · The Pineapple Standard · RCAT #03-0637 · zero green
last_updated: 2026-07-14
verify_before_publish: HQ address (The Star), geo-coordinates, final website URL
---

# 🏆 Goldie Pipeline — Week 1 & 2

Business brain: **Pineapple Contractors** · (972) 928-0788 · RCAT #03-0637 · IKO Certified ·
HQ The Star, 1 Cowboys Way Ste 270W, Frisco TX 75034 *(verify)* · Site: pineappleroofingllc.com

---

## 📅 WEEK 1 — GBP Category & Attribute Audit

### Prompt 1 — Category Audit (set these in Google Business Profile)
- **Primary category:** **Roofing Contractor** (highest-intent, must be primary)
- **Secondary categories** (add all that apply — each opens new searches):
  - Construction Company
  - Commercial Roofing
  - Water Damage Restoration Service
  - Gutter Cleaning Service
  - Siding Contractor
  - Metal Roofing Manufacturer *(only if accurate — else skip)*
- **Do NOT** over-add unrelated categories — it dilutes relevance.

### Prompt 2 — Attributes Audit (toggle these ON in GBP)
- **From the business:** Locally owned & operated · Family-owned
- **Service options:** Online estimates · On-site services · Emergency service
- **Accessibility / planning:** Appointment required (if true)
- **Payments:** Accepts cards · Financing available (if true)
- **Highlights:** Licensed (RCAT #03-0637) · Insured · IKO Certified
- **Add a booking/CTA link** → your free roof inspection request page.

**Action:** apply in business.google.com → Edit profile → Categories / Attributes.

---

## 📅 WEEK 2 — Review Velocity + Response Templates

**Goal:** 10+ new reviews/month. Send the review texts in `Outbox_Drafts/Content/`.
**Reply to EVERY review** — Google rewards it. Keywords woven in naturally below.

### ⭐⭐⭐⭐⭐ 5-Star responses (3)
1. "Thank you, [Name]! We're proud to have earned your trust on your **roof replacement in [City]**. Our IKO Certified crew loves hearing this — enjoy that new roof, and we're one call away at (972) 928-0788. — The Pineapple team 🍍"
2. "[Name], this means the world to our family business. So glad the **storm damage repair** went smoothly and the insurance side felt easy with us in your corner. Thank you for choosing Pineapple Contractors!"
3. "We appreciate you, [Name]! Reviews like yours help other **[City] homeowners** find a licensed (RCAT #03-0637), IKO Certified team they can trust. Thank you for the 5 stars."

### ⭐⭐⭐⭐ 4-Star responses (3)
1. "Thanks for the honest feedback, [Name] — glad you were happy overall with your **roof repair**. We're always improving; if there's anything that would've made it 5 stars, we'd love to hear it at (972) 928-0788."
2. "Appreciate the review, [Name]! We're grateful you trusted us with your **[City] roofing** project. Please reach out directly if we can make anything right — The Pineapple Standard means we follow through."
3. "Thank you, [Name]. Four stars is a great start and we want to earn that fifth — tell us what we can do better. We're committed to every North Texas homeowner we serve."

### ⭐/⭐⭐ 1–2 Star responses (3) — calm, accountable, offline
1. "[Name], thank you for the feedback and we're sorry your experience fell short of The Pineapple Standard. That's not who we are. Please call me directly at (972) 928-0788 so we can make this right."
2. "We take this seriously, [Name]. As a licensed (RCAT #03-0637) family business, your experience matters to us. I'd like to understand what happened and resolve it — please reach me at (972) 928-0788."
3. "We're sorry, [Name]. We'd rather fix a problem than defend one. Please give us the chance to make it right — (972) 928-0788, ask for the owner."

---

## 🧩 LocalBusiness JSON-LD Schema (paste into WordPress site <head> or an HTML block)
> Boosts Google understanding of who/where you are. Verify address + geo before publishing.
```json
{
  "@context": "https://schema.org",
  "@type": "RoofingContractor",
  "name": "Pineapple Contractors",
  "image": "https://www.pineappleroofingllc.com/logo.png",
  "@id": "https://www.pineappleroofingllc.com",
  "url": "https://www.pineappleroofingllc.com",
  "telephone": "+1-972-928-0788",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1 Cowboys Way, Ste 270W",
    "addressLocality": "Frisco",
    "addressRegion": "TX",
    "postalCode": "75034",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 33.0972, "longitude": -96.8352 },
  "areaServed": ["Frisco TX","Lewisville TX","Plano TX","McKinney TX","Denton TX","Allen TX","Dallas–Fort Worth"],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "08:00", "closes": "18:00"
  }],
  "founder": "Pineapple Contractors (Polynesian-owned, family-run)",
  "foundingDate": "2005",
  "hasCredential": ["RCAT License #03-0637","IKO Certified"],
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "400" },
  "sameAs": [
    "https://www.google.com/maps/place/Pineapple+Contractors",
    "https://www.facebook.com/pineapplecontractors"
  ]
}
```
*(Swap URL to pineapplecontractors.com if you place it there first; update geo + reviewCount to real values.)*

<!-- M7-FIREWALL-EXEMPT: seo-pipeline -->
