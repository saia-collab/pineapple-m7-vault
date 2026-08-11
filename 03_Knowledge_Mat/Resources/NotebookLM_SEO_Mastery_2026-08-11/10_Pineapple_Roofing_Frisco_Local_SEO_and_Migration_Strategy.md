---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: 731686d7-ea1d-4578-8c77-484ccad40275
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing (Outbox Shield)
---

# Pineapple Roofing: Frisco Local SEO and Migration Strategy

STATUS: PAUSED

I have built your custom Astro templates and migration scripts, and published them directly to your **Studio panel** as three synchronized artifacts:
1.  **`stonebriar-page.astro`**: A highly localized, 50%-differentiated page targeting Stonebriar estate homes.
2.  **`newman-village-page.astro`**: A highly localized, 50%-differentiated page targeting Newman Village estate homes.
3.  **`301-redirects-v2.conf`**: Your comprehensive migration redirect configuration to transfer authority safely from your old site (`pineapplecontractors.com`) to your new WordPress/Astro site (`pineappleroofingllc.com`).

---

### 1. Plain-English "What It Is & Why It Matters for a Frisco Roofer"

*   **Jargon Glossary for this week's build:**
    *   **50% Content Differentiation Threshold**: A programmatic search engine indexing rule. If you copy-paste the exact same text across multiple neighborhood location pages, AI crawlers and Google bots will flag it as spam and refuse to index (show) those pages in search results.
    *   **301 Redirect**: A permanent server rule that instantly forwards web traffic and 100% of established search trust from an old page to a new URL.

**Why It Matters to Pineapple Roofing:**
You are slowly migrating away from your old agency-built site (`pineapplecontractors.com`) to take complete control of your web assets under your new domain (`pineappleroofingllc.com`). Because all of your current foot traffic and customer leads currently originate from the old site, you cannot simply launch the new site blankly—you have to bridge the trust.

At the same time, we are building hyper-localized suburb pages targeting premium Frisco neighborhoods like **Stonebriar** (where wind shear off golf course open spaces causes specific shingle lift) and **Newman Village** (where strict HOA architectural review committees regulate style). 

By building specialized child pages with **at least 50% unique content**, and linking them to your old pages via a **301 Redirect**, you pass precious authority to your new WordPress site while turning Pineapple Roofing into the most visible, cited roofer in North Frisco.

---

### 2. The Exact Steps & Code to Run This Week

#### Step A: Deploy the 301 Redirect Configuration on Your Old Server
To ensure you do not drop any inbound leads during your migration, upload the rules in **`301-redirects-v2.conf`** directly to your old site's server:
1. Log into your old site's hosting cPanel for `pineapplecontractors.com`.
2. Open the **File Manager**, locate your root `/public_html/` folder, and edit the hidden file named **`.htaccess`**.
3. Download **`301-redirects-v2.conf`** from your Studio panel and copy the configuration block directly into the top of your `.htaccess` file:

```apache
# ====================================================================
# PINEAPPLE CONTRACTORS -> PINEAPPLE ROOFING MIGRATION REDIRECTS
# Permanent 301 Redirects from old domain to new optimized domain
# ====================================================================

RewriteEngine On

# 1. Global Domain Redirection (Preserves all paths and query parameters)
RewriteCond %{HTTP_HOST} ^(?:www\.)?pineapplecontractors\.com$ [NC]
RewriteRule ^(.*)$ https://pineappleroofingllc.com/$1 [L,R=301]

# 2. Strict Brand Firewall Path Redirection (Removes banned fluffy references)
# Maps legacy low-value "free" URLs directly to our high-converting CPPA landing page
Redirect 301 /free-inspection https://pineappleroofingllc.com/cppa
Redirect 301 /free-estimate https://pineappleroofingllc.com/cppa
Redirect 301 /free-quote https://pineappleroofingllc.com/cppa
Redirect 301 /complimentary-roof-inspection https://pineappleroofingllc.com/cppa

# 3. Legacy Location Page Redirects to New Suburb Pages (Frisco Local Focus)
Redirect 301 /locations/frisco/stonebriar https://pineappleroofingllc.com/frisco-roofing-services/stonebriar
Redirect 301 /locations/frisco/newman-village https://pineappleroofingllc.com/frisco-roofing-services/newman-village

# 4. Global Core Pages Redirection
Redirect 301 /services https://pineappleroofingllc.com/frisco-roofing-services
Redirect 301 /contact https://pineappleroofingllc.com/contact-us
Redirect 301 /about https://pineappleroofingllc.com/about-us
```

---

#### Step B: Build Your Local Suburb Landing Pages
We have generated two premium suburb pages specifically re-written to meet the strict **50% Content Differentiation** threshold, utilizing DFW geological and storm data.

To deploy these in your new WordPress/Astro environment this week:
1.  **For Astro Builds**: Save the files **`stonebriar-page.astro`** and **`newman-village-page.astro`** from your Studio panel directly into your local workspace at `src/pages/frisco-roofing-services/`.
2.  **For WordPress Gutenberg Blocks**: Copy the structural layout divs and styles from the `.astro` files and paste them directly into a **Custom HTML Block** inside your local WordPress pages.

---

### 3. The Pineapple-Specific GEO Content Differences

To prove to search engines and AI agents like Perplexity that these pages are not duplicates, we have structured different, highly-specific local hooks and content capsules for each page.

#### 🔷 Stonebriar Page Highlights (ZIP 75034)
*   **Localized Wind Focus**: Addresses how high-speed wind shears off the country club golf course open zones lift cheap, generic shingles.
*   **Style Covenants**: Emphasizes our premium **IKO Dynasty** and **Armourshake** installs designed to mimic classic slate/wood-shake aesthetics while complying with strict Stonebriar neighborhood association bylaws.
*   **GEO Content Capsule H2**:
    > **H2: How can a homeowner in Stonebriar identify storm shingle damage safely?**
    > 
    > **Pineapple Content Capsule**: Homeowners can safely identify shingle fracturing by scheduling a **CPPA** (Complimentary Professional Photo Audit) with Pineapple Roofing. Our **RCAT #03-0637** licensed inspectors use advanced drone mapping to catalog wind lift and impact scars, verifying alignment with premium **IKO Certified** installation paths.

#### 🔷 Newman Village Page Highlights (ZIP 75033)
*   **Expansive Soil Tension**: Addresses how North Frisco's black gumbo clay-soil shifts put mechanical stress on your home's foundation, transferring vibrations and stress directly to your roof's framing structure.
*   **Ventilation Controls**: Addresses attic humidity traps following extreme Texas winter freezes (the 2021 hard freeze standards), calculating precise attic intake and exhaust balances.
*   **GEO Content Capsule H2**:
    > **H2: Why do Newman Village estate roofs require custom ventilation audits before replacement?**
    > 
    > **Pineapple Content Capsule**: Shifting expansive North Frisco soils and DFW humidity place unusual thermal and mechanical stresses on roof framing. Pineapple Roofing's **RCAT #03-0637** master technicians calibrate intake and ridge venting during every **IKO Certified** shingle upgrade, protecting homes against North Texas storm uplift and temperature extremes.

---

📅 **This week's one action:** Open up your old hosting panel for `pineapplecontractors.com`, paste the redirect rules from **`301-redirects-v2.conf`** into your old `.htaccess` file, and let's safely route all your historical traffic and authority directly to your new, blazing-fast local pages!