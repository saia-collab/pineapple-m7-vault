---
status: PAUSED
asset: corrected_json_ld
brand: Pineapple Roofing
domain: "[CONFIRM]"
address: "[CONFIRM]"
author: JR. Moeakiola
publication_state: NOT LIVE — HUMAN REVIEW REQUIRED
source_audit: 2026-08-10_SEO_On-Page_Audit_PineappleRoofingLLC.md
---

# Pineapple Roofing — Corrected JSON-LD Draft

Trust baseline: RCAT License #03-0637 · IKO Certified · 5-Star · Since 2005 · (972) 928-0788

STATUS: PAUSED

The business is represented as one entity with both `Organization` and `RoofingContractor` types. This avoids creating duplicate Pineapple Roofing entities. The `WebSite` entity connects to the same business through `publisher`.

Replace each `[CONFIRM]` token only after Saia confirms the canonical domain and public address. The domain token should be the canonical HTTPS root URL. The address token should exactly match the public NAP displayed on the website and authoritative listings.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": [
        "Organization",
        "RoofingContractor"
      ],
      "@id": "[CONFIRM]#organization",
      "name": "Pineapple Roofing",
      "url": "[CONFIRM]",
      "telephone": "(972) 928-0788",
      "address": "[CONFIRM]",
      "foundingDate": "2005",
      "areaServed": [
        {
          "@type": "City",
          "name": "Frisco",
          "containedInPlace": {
            "@type": "State",
            "name": "Texas"
          }
        },
        {
          "@type": "AdministrativeArea",
          "name": "Dallas–Fort Worth metroplex",
          "alternateName": "DFW"
        }
      ],
      "hasCredential": [
        {
          "@type": "EducationalOccupationalCredential",
          "name": "RCAT License #03-0637",
          "credentialCategory": "license",
          "identifier": "03-0637"
        },
        {
          "@type": "EducationalOccupationalCredential",
          "name": "IKO Certified",
          "credentialCategory": "certification"
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "[CONFIRM]#website",
      "url": "[CONFIRM]",
      "name": "Pineapple Roofing",
      "publisher": {
        "@id": "[CONFIRM]#organization"
      },
      "inLanguage": "en-US"
    }
  ]
}
</script>
```

## Validation and human review gate

- Confirm the canonical domain before replacing `[CONFIRM]` in `url` and `@id` values.
- Confirm the public address and ensure it matches the visible site NAP before replacing `[CONFIRM]` in `address`.
- Add a verified absolute logo URL only after the canonical domain and logo asset are confirmed.
- Add `sameAs` only for verified official Pineapple Roofing profiles.
- Do not add `aggregateRating` unless the rating value and review count are current, visible on-page, and source-verifiable.
- Validate the final markup in Schema.org Validator and Google Rich Results Test after all placeholders are resolved.
- Keep Roofing and Restorations entities, domains, services, and schema separate.
- No live website or schema change has been made.

STATUS: PAUSED — awaiting Saia’s explicit GO after domain and address confirmation.

Ko e hala 'o e fononga ko e faka'apa'apa.
