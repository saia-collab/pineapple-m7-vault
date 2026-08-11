---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: 0a649af3-2786-4907-a9f8-fe918f338c65
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing (Outbox Shield)
---

# AI-Driven Digital Marketing for Frisco Roofing Professionals

### Topic 1: Nano Banana for Local Business Imagery

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**Nano Banana** (Google's state-of-the-art AI image generator, officially named **Gemini Image Preview**) is a tool that allows you to generate photorealistic business imagery and edit existing photos with incredible precision [1-3]. 

*   **Jargon Glossary:**
    *   **Vibe Coding:** Building apps or generating content using conversational, natural language instead of writing lines of code [4, 5].
    *   **Image Style Guide:** A set of strict camera parameters (like focal length and lighting) given to an AI so every image it generates looks like it was shot by the same professional photographer [6, 7].

**Why it matters to a Frisco Roofer:** 
Roofing is a highly visual business. Homeowners want to see beautiful, clean, completed jobs. However, hiring a professional photographer to follow your crew around Frisco is expensive. On the flip side, stock photos look fake, and raw cellphone photos of job sites often feature messy yards, discarded shingles, and grey, overcast skies. 

With **Nano Banana**, you can upload a messy cellphone photo of an active job site, clean up the lawn, change the gloomy grey sky to a perfect Texas blue, and generate consistent, high-end visual assets for your website and social media—all for fractions of a cent per run [8-10].

---

#### 2) The Exact Steps and Prompt to Run
To generate hyper-realistic, brand-consistent project photos, you will first define an **Image Style Guide** so your photos look uniform [7, 11]. Run this exact prompt in Google AI Studio or ChatGPT:

```text
Act as a world-class commercial photographer specializing in luxury home exterior and construction photography. I want to build a highly consistent brand image gallery for my business. 

First, establish a "Style Guide Wrapper" that defines the photographic style. Every image we generate must simulate being shot with a Sony A7RV camera, using a 24mm f/2.8 lens, with bright, natural, late-afternoon golden hour lighting, clean compositions, and razor-sharp textures showing actual physical plausibility. Do not make the images look like glossy AI art; they must look like real, high-end photography.

Now, use this style guide to generate the following scene:
[A pristine, luxury modern-farmhouse home in Frisco, Texas, with a newly installed high-contrast charcoal asphalt shingle roof. In the driveway, a neat, wrapped pallet of premium IKO shingles is visible. The lawn is neatly mown, the sky is a bright, clear blue, and the image is shot from a low-angle perspective to emphasize the beauty and lines of the new roof.]
```

---

#### 3) The Pineapple-Specific Example
Suppose a tenant or homeowner sends you a low-quality, cluttered photo of a completed roof replacement, but there is storm debris, a trash can, and a dark overcast sky in the background [8, 12]. 

Instead of discarding it, upload the photo to Google AI Studio with **Nano Banana** selected and type this exact refinement [1, 4]:

> *"Clean up the yard in this photo [8]. Remove the trash cans and storm debris from the lawn, make the grass look neatly mowed and vibrant green, and change the dark grey sky to a beautiful, sunny blue day in Frisco [8]. Ensure the lighting on the house matches the new sunny sky, and make the newly installed shingles look pristine [8]."*

---

### Topic 2: The Reverse Interview Prompt for Site Schema

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **Reverse Interview** is a prompting technique where, instead of you trying to write a complex prompt, you instruct the AI to "interview" you by asking targeted questions to extract the exact data it needs to generate a perfect output [13, 14].

*   **Jargon Glossary:**
    *   **Schema Markup (Structured Data):** A specialized block of code injected into your website's header that acts as a "machine-readable directory" for search engines to instantly understand who you are, your license, and what you offer [15-18].
    *   **JSON-LD:** The specific, clean code format that Google prefers for reading schema markup [19-21].

**Why it matters to a Frisco Roofer:** 
AI search engines (like ChatGPT Search and Perplexity) are lazy—they look for machine-readable schema code to verify your business credentials before recommending you [16, 22]. If a homeowner asks an AI, *"Who is a licensed roofer in Frisco?"* and your website has verified **RoofingContractor** schema, the AI can instantly read your license number (**RCAT #03-0637**) and confidently recommend you [23-25]. 

By using the **Reverse Interview**, you don't have to guess what technical schema details to include; the AI extracts your specific business rules and outputs perfect code on the first try [13].

---

#### 2) The Exact Prompt to Run
Paste this exact prompt into your AI assistant to start your custom schema interview [26]:

```text
Act as an expert Local SEO technical architect. I need to generate a perfect, error-free JSON-LD Schema markup block for my local business homepage to make us highly discoverable by AI search engines like ChatGPT and Perplexity.

To ensure the schema is 100% accurate, I want you to run a "Reverse Interview." Do not generate any code yet. Ask me exactly 5 targeted, one-by-one questions about my business (including credentials, service areas, and license numbers) so you have all the context you need. 

Once I answer your questions, you will output a single, fully populated JSON-LD block combining 'LocalBusiness', 'RoofingContractor', and 'Service' schemas, verified to pass Google's Rich Results Test.
```

---

#### 3) The Pineapple-Specific Example
When the AI asks you its interview questions, you will feed it your exact business facts:

1.  **Business Name:** Pineapple Roofing [27]
2.  **License:** RCAT #03-0637 Licensed [28]
3.  **Certifications:** IKO Certified [28]
4.  **Primary Offer/Service:** CPPA (Comprehensive Professional Property Assessment) [28]
5.  **Service Area:** Frisco, Texas [29]

The AI will then output a flawless schema block that you copy and paste directly into your website header [19, 30]. It will look like this:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "RoofingContractor",
      "@id": "https://pineapple-roofing.com/#business",
      "name": "Pineapple Roofing",
      "areaServed": "Frisco, TX",
      "license": "RCAT #03-0637",
      "hasCredential": {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "IKO Certified Roofing Contractor"
      }
    },
    {
      "@type": "Service",
      "serviceType": "CPPA (Comprehensive Professional Property Assessment)",
      "provider": {
        "@id": "https://pineapple-roofing.com/#business"
      }
    }
  ]
}
```

---

### Topic 3: Automating GBP Review Replies

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**Google Business Profile (GBP) Review Reply Automation** is a system that monitors your Google Maps listing and uses AI to reply to customers [31-33]. 

*   **Jargon Glossary:**
    *   **GBP (Google Business Profile):** Your business listing on Google Maps that shows your reviews, hours, and photos [34, 35].
    *   **Zonio / Postroxy:** Secure connector tools that allow local AI tools to securely talk to your live Google Maps account [33, 36, 37].
    *   **Review Gating:** The practice of sending happy customers to public review sites while keeping unhappy customers in a private feedback loop (Technically discouraged by Google, but highly effective when managed carefully) [38].

**Why it matters to a Frisco Roofer:** 
The plumber or roofer down the street isn't outranking you because of luck—it's because their Google Maps profile is highly active [31, 39]. Google's map algorithm highly rewards profiles that reply to reviews immediately [31]. 

Automating this keeps your profile highly active 24/7 [33]. However, to protect your hard-earned reputation, you must use a **split-logic system**: positive reviews are replied to instantly, while negative reviews are privately drafted and paused for your manual approval before posting [40-42].

---

#### 2) The Exact Steps to Run This Week
You can set up this workflow in under an hour using **Pably Connect** or **Make** combined with **Open Router** [43, 44]:

1.  Create a free account on **Pably Connect** or **Make** [43, 45].
2.  Set up your trigger module: Select **Google Business Profile** and set the event to **New Review** [46].
3.  Add a **Router/Filter** module to split the traffic based on the review rating [47]:
    *   **Path A (Positive):** If rating is **4 or 5 stars**, route to Open Router/ChatGPT [47, 48].
    *   **Path B (Negative):** If rating is **3 stars or below**, route to your email or Slack [40, 49].
4.  Configure the **Positive Review Reply** prompt in your Open Router/ChatGPT module [44, 48]:

```text
Act as the Owner of Pineapple Roofing in Frisco, Texas. Write a warm, 2-sentence response to this 5-star review left by [Customer Name]. 

Review Text: [Paste Review Comment]

Rules:
1. Thank them warmly by name.
2. Naturally mention our primary service "CPPA" (Comprehensive Professional Property Assessment), our "RCAT #03-0637" license, or our "IKO Certified" shingles.
3. Keep the tone professional, local, and polite. Do not use AI fluff.
```

5.  Configure the **Negative Review Reply** to send an alert email directly to your inbox with a pre-drafted response so you can review it before replying [41, 49]:

```text
ALERT: Negative Review received from [Customer Name] ([Star Rating] Stars). 
Review: [Review Text]

Proposed Private Draft Response (Review & Approve before public reply):
"Hello [Customer Name], we take your feedback seriously. Pineapple Roofing is an RCAT #03-0637 licensed contractor, and we strive to hit premium standards on every project. Please contact us directly at info@pineapple-roofing.com so we can make this right immediately."
```

---

#### 3) The Pineapple-Specific Example
If a Frisco homeowner named Sarah leaves a 5-star review saying: *"Loved the team, they inspected our roof after the hail storm and handled the repairs so quickly!"* 

The automated system will capture her review, pass it through your filter, and instantly post this highly optimized response back to your Google Maps listing [50, 51]:

> *"Thank you so much for the kind words, Sarah! We are proud to support Frisco homeowners with our licensed **RCAT #03-0637** standards, and we are thrilled our signature **CPPA** assessment helped document your hail storm damage quickly and safely."* [48, 52, 53]

---

📊 **This week's one action:** Open up your free Google AI Studio account, select **Gemini 2.0 Flash**, and run the **Style Guide Prompt** from Topic 1 to generate three gorgeous, customized roofing images of your active Frisco job sites to post on your website. Let's make Pineapple Roofing look like a million bucks!