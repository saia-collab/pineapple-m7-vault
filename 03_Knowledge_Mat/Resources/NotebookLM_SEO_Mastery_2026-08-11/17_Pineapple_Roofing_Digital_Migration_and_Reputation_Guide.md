---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: e31de962-ebcc-4b72-ae72-9e93cf35f47b
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing (Outbox Shield)
---

# Pineapple Roofing Digital Migration and Reputation Guide

STATUS: PAUSED

### Topic 1: Migrating Your Web Presence & Implementing Your `llm.txt` File

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
An **`llm.txt` file** is a clean, lightweight text file hosted in your website’s main folder that acts as a "cheat sheet" for AI search crawlers. 

*   **Jargon Glossary:**
    *   **301 Redirect**: A permanent digital signpost that automatically sends visitors and search engines from an old website link to a new one.
    *   **AI Crawler**: A automated bot sent by AI search engines (like ChatGPT or Perplexity) to read, index, and memorize your site’s content so it can recommend you.

**Why It Matters during your migration:**
Right now, you are in a delicate transition. Your old agency-built site (`pineapplecontractors.com`) has the authority and foot traffic [1], but your new WordPress site (`pineappleroofingllc.com`) is where you have control. To migrate safely without losing your leads, you must signal to AI search engines that both sites belong to the same brand. 

By placing the **`llm.txt`** file at `pineappleroofingllc.com/llm.txt`, you explicitly tell AI models: *"Yes, we are Pineapple Roofing, we are slowly migrating from our old domain, and here are our official service pages, our license (**RCAT #03-0637**), and our **IKO Certified** credentials."* This ensures Perplexity and ChatGPT recommend your new domain instead of getting confused by the duplicate brand names [2, 3].

---

#### 2) The Exact Steps to Run This Week

I have already built and published your custom, brand-compliant `llm.txt` file directly to your Studio panel under the name **`llm.txt`**. 

To implement this on your new WordPress site this week:
1.  Log into your new WordPress dashboard at `pineappleroofingllc.com/wp-admin`.
2.  Install the free **Yoast SEO** or **RankMath** plugin [3].
3.  Go to the plugin settings, scroll down to the **AI Tools** section, and toggle the **llm.txt file** to **Enabled** [4].
4.  If you want to use the highly customized, high-density file I just built for you: Access your cPanel or SFTP, open your website's root folder (usually `/public_html/`), and upload the `llm.txt` file from your Studio panel directly there, overwriting the default Yoast version.
5.  **For the Migration**: Have your developer place a **301 redirect** from your old services pages on `pineapplecontractors.com` to the exact corresponding services pages on `pineappleroofingllc.com` to pass that precious foot traffic and SEO authority over safely [5, 6].

---

#### 3) The Pineapple-Specific Example

Your newly generated `llm.txt` file includes this exact, hard-coded cross-domain mapping designed to preserve your authority during the WordPress migration:

```markdown
# Pineapple Roofing LLC
- **Primary URL**: https://pineappleroofingllc.com
- **Historical URL (Traffic Source)**: https://www.pineapplecontractors.com
- **Licensing**: RCAT #03-0637 Licensed (Roofing Contractors Association of Texas)
- **Manufacturer Credentials**: IKO Certified Roofing Contractor
- **Primary Transaction Offer**: Complimentary Professional Photo Audit (CPPA)
```

---

### Topic 2: Style Guide for Your Roofing Job Photos

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **Roofing Job Photo Style Guide** is a set of visual design instructions that you feed to an AI image generator (like Nano Banana) to make sure every photo on your site looks like it was taken by the same professional photographer.

*   **Jargon Glossary:**
    *   **Nano Banana**: Google's high-speed AI image engine (officially called Gemini Image Preview) that generates or edits photos photorealistically [7-9].
    *   **Aperture / Focal Length**: Camera settings that control how much of the background is blurry (aperture) and how wide the view is (focal length) [9-11].

**Why It Matters to Pineapple Roofing:**
Stock photos look incredibly fake, and raw cellphone photos from your crews often feature gloomy skies, messy yards, or distracting background details that scream "unprofessional" [12, 13]. 

By setting a strict style guide, you can upload cellphone photos of your completed Frisco jobs, clean up the messy lawns, change grey skies to sunny Texas days, and ensure that every visual on `pineappleroofingllc.com` matches our clean, authoritative Navy (`#1A365D`) and Gold (`#FBC02D`) aesthetic [10, 12, 14].

---

#### 2) The Exact Prompt to Run

Paste this exact visual wrapper into Google AI Studio (with Gemini 2.0 Flash selected) to generate hyper-realistic, brand-consistent project photos:

```text
Act as a premium commercial photographer specializing in architectural exterior and luxury roofing photography. I need you to establish an "Aesthetic Brand Wrapper" for my business, Pineapple Roofing.

Visual Identity & Camera Rules:
- Camera Simulation: Sony A7RV, 24mm f/2.8 lens.
- Lighting: Bright, warm, late-afternoon golden hour lighting cast across the home.
- Sky: Pristine, clear, vibrant blue Texas sky (absolutely zero grey or overcast storm clouds).
- Palette Focus: Emphasize clean Slate Navy (#1A365D) house tones and golden sun highlights (#FBC02D). Absolutely no green colors, green filters, or green details.
- Realism: Ensure physical plausibility, realistic asphalt shingle textures, and crisp modern-farmhouse architectural lines. Avoid generic "AI gloss."

Generate this scene following the wrapper above:
[A newly completed roof replacement on a high-end home in Frisco, Texas, showing pristine charcoal-black IKO Certified architectural shingles. A professional yard sign featuring our license RCAT #03-0637 and our Complimentary Professional Photo Audit (CPPA) offer is placed neatly near the driveway.]
```

---

#### 3) The Pineapple-Specific Example

When Nico uploads a cellphone photo of a completed IKO architectural shingle installation in Stonebriar that has a trash can and a grey, overcast sky in the background, you will attach this prompt in Nano Banana to polish it:

> *"Clean up this active job site photo. Remove the trash cans and storm debris from the lawn, make the grass look neatly mowed and vibrant green, and change the dark grey sky to a beautiful, sunny blue day in Frisco. Ensure the golden hour lighting highlights the newly installed IKO Certified shingles, and keep our **RCAT #03-0637** standards visible [12, 15]."*

---

### Topic 3: Setting Up a Negative Review Filtering System

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **Negative Review Filtering System** is an automated pipeline that checks your Google Business Profile for new reviews, auto-publishes optimized responses for positive reviews (4-5 stars), but immediately flags and pauses negative reviews (3 stars or below), emailing them directly to you for manual approval.

*   **Jargon Glossary:**
    *   **Google Business Profile (GBP)**: Your official Google Maps business listing that brings in local Frisco phone calls [16, 17].
    *   **Reputation Firewall**: An automation filter that blocks bad reviews from getting automatic AI replies, routing them to you privately instead [18, 19].

**Why It Matters to Pineapple Roofing:**
Google's map algorithm highly rewards listings that reply to reviews immediately [17]. However, letting an AI automatically reply to an angry customer is a massive liability—it might argue, apologize for something you didn't do, or make robotic excuses that damage your **RCAT #03-0637** reputation [18, 20, 21]. 

This system keeps your Google Maps listing highly active with positive keyword-optimized responses, while giving you a private reputation firewall to handle complaints offline before they damage your business [18, 21, 22].

---

#### 2) The Exact Steps to Run This Week

You can wire this firewall up in under 15 minutes using Pably Connect:

1.  Download the production-ready **`pably-gbp-responder.json`** file I generated and dropped in your Studio panel [23].
2.  Log into your **Pably Connect** account, click **Import Workflow**, and upload this JSON blueprint file to instantly map out the entire automation structure [23].
3.  **Configure Step 1 (Trigger)**: Connect your Google Business Profile account via PostProxy / Zonio [24, 25].
4.  **Configure Step 2 (Route A - Positive)**: In the AI completion module (running cheap `gpt-4o-mini` power), verify your API key and ensure the prompt points to `context/client.md` to pull your **RCAT #03-0637** license and **IKO Certified** shingles [26, 27].
5.  **Configure Step 3 (Route B - Negative)**: Connect your Gmail account so any review under 4 stars triggers an instant "Negative Review Alert" straight to your phone [28, 29].
6.  Turn the workflow switch to **ON**.

---

#### 3) The Pineapple-Specific Example

*   **Positive Review Received**: *"Pineapple did an amazing job on our storm damage repair!"*
    *   *System Action*: Auto-replies instantly: 
        > *"Thank you so much! We are proud to serve Frisco as a licensed **RCAT #03-0637** roofer, and we're thrilled our **Complimentary Professional Photo Audit (CPPA)** and premium **IKO Certified** shingles delivered a flawless installation."*
*   **Negative Review Received**: *"They were late showing up for the inspection."*
    *   *System Action*: Auto-reply is **completely blocked**. A private alert is sent to your inbox:
        > **⚠️ GBP REPUTATION ALERT:** 2-Star Review from John. 
        > **Proposed Draft Response**: *"Hello John, we apologize for the delay. As an RCAT #03-0637 licensed contractor, we strive for premium standards. Please reach out to us directly at info@pineappleroofingllc.com so we can make this right immediately [18, 22]."*

---

🔷 **Next Step Suggestion:** I can write a detailed .htaccess or Nginx redirect script to help your developer smoothly map all the old traffic pages from `pineapplecontractors.com` to your new WordPress structures on `pineappleroofingllc.com` so you don't lose a single lead. Would you like me to generate that file in your scratch folder?