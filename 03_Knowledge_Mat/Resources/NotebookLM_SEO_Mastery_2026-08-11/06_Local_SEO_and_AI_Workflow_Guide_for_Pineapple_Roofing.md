---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: 2b9ebb9e-6755-4030-b02e-805ed77e40af
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing (Outbox Shield)
---

# Local SEO and AI Workflow Guide for Pineapple Roofing

### Topic 1: Setting up the DataForSEO MCP in Claude Code

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**DataForSEO MCP** is a technical bridge that links your local terminal assistant (**Claude Code**) directly to a massive, real-time search engine database [1-3]. 

*   **Jargon Glossary:**
    *   **MCP (Model Context Protocol)**: An open standard that allows AI models to securely connect to external APIs and live databases [4].
    *   **API (Application Programming Interface)**: A secure channel that lets two different software applications talk and trade live data [5].

**Why It Matters to Pineapple Roofing:**
Natively, AI models are frozen in time and have zero access to live search metrics [3, 6]. If you ask Claude, *"What are homeowners in Frisco searching for after a hail storm?"*, it can only make educated guesses [6, 7]. 

By connecting the **DataForSEO MCP**, you give Claude live "X-ray vision" into search data [8]. It can immediately scan North Texas, analyze your local competitors, and tell you exactly how many Frisco residents are searching for storm repairs each month—along with how hard it is to rank for those terms [3, 9, 10].

---

#### 2) The Exact Steps to Run
To configure this connection in under five minutes, execute these commands in your local computer terminal [11]:

1.  Create a free account at **[DataForSEO](https://dataforseo.com/)** to receive \$1 in free trial credits (which covers hundreds of keyword lookups) [11].
2.  Retrieve your **API Login** (your registration email) and **API Password** (sent to you via email) from your DataForSEO dashboard [12].
3.  Open your terminal and save these credentials as environment variables by editing your shell profile [13, 14]:
    ```bash
    nano ~/.zshrc
    ```
4.  Paste these lines at the bottom of the file (replacing with your actual details) and save (`Ctrl+O`, then `Ctrl+X`):
    ```bash
    export DATAFORSEO_USERNAME="your_email@domain.com"
    export DATAFORSEO_PASSWORD="your_api_password_here"
    ```
5.  Reload your terminal configuration:
    ```bash
    source ~/.zshrc
    ```
6.  Open Claude Code in your project folder, type `/mcp`, and verify that the `dataforseo` connector is verified and active [15, 16]!

---

#### 3) The Pineapple-Specific Example
Once active, you can run this exact command in Claude Code to find immediate low-hanging keyword opportunities:

> *"Using the dataforseo MCP, pull the top 20 local keywords for 'roof repair Frisco TX'. Show me their exact monthly search volume and difficulty, and identify which terms we should target for our next **Complimentary Professional Property Assessment (CPPA)** page."* [2, 17]

---

### Topic 2: The "50% Unique Content Rule" for Suburb Pages

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
The **50% Unique Content Rule** is a structural guideline requiring that at least half of the text on your individual neighborhood landing pages (like Stonebriar or Newman Village) contains distinct, hyper-local information [18-20].

*   **Jargon Glossary:**
    *   **Content Duplication**: A search engine penalty where crawlers flag your site as spam because you copy-pasted the exact same template across multiple local pages [18, 19].
    *   **Programmatic SEO**: Automatically generating hundreds of local landing pages using structured templates and database variables [19, 21].

**Why It Matters to Pineapple Roofing:**
If you try to build location pages for every suburb in DFW but simply swap the name "Frisco" for "Stonebriar" while leaving the rest of the text identical, search engine crawlers will flag your site [19, 22]. They will only index one page and bury the rest as duplicate spam [22, 23]. 

By ensuring **at least 50% of the content is unique**, you prove to search engines that you are a genuine local expert in every community you service [24, 25].

---

#### 2) The Exact Steps or Prompt to Run
To write highly differentiated suburb pages that search engines love, use this prompt with Claude to generate local angles:

```text
Act as a hyper-local market researcher. I need you to find at least three highly specific, factual geographic and physical characteristics for [Suburb Name] in Frisco, Texas. 

Specifically, research:
1. Local subdivision covenants, HOA guidelines, or architectural review guidelines that affect roof styles (e.g., matching slate or wood-shake tiles).
2. Local geological parameters (such as expansive clay soils that shift house slabs and stress rafters) or historic storm weather paths.
3. Hyper-local neighborhood boundaries, parks, or school landmarks to prove authentic geographic presence.

Use these factual details to write an introductory copy block that is 100% unique to this neighborhood.
``` [23, 26]

---

#### 3) The Pineapple-Specific Example
*   **Stonebriar Page (ZIP 75034)**: Focuses on wind shear off the open golf course zones, noting how high-speed winds lift cheap shingles, and outlines how our premium **IKO Certified** shingles meet local HOA requirements [Stonebriar page, previous turn].
*   **Newman Village Page (ZIP 75033)**: Focuses on expansive clay soils shifting foundations and stressing attic rafters, calculating precise attic ventilation metrics to prevent shingle degradation [Newman Village page, previous turn].

---

### Topic 3: Generating a Podcast from a Blog Using NotebookLM

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**NotebookLM Audio Overviews** is a free Google feature that takes any text, PDF, or blog post and automatically generates a highly realistic, two-person podcast discussing your content [27-29].

*   **Jargon Glossary:**
    *   **Audio Overview**: A feature in Google NotebookLM that uses advanced voice models to simulate a natural, conversational podcast [29, 30].
    *   **Time-on-Page**: An SEO metric tracking how long a user stays on your website before leaving. Longer stays signal high-quality content to Google [31, 32].

**Why It Matters to Pineapple Roofing:**
Many homeowners researching storm damage are busy and don't want to read a 2,000-word blog post [33]. By turning your local roofing articles into engaging, realistic audio podcasts, you provide a frictionless way for clients to learn about your **CPPA** process while driving between jobs [28, 31, 33]. 

Embedding this podcast into your site dramatically boosts your **time-on-page metrics**, sending powerful positive ranking signals directly to Google [31, 32].

---

#### 2) The Exact Steps to Run This Week
1.  Go to **[Google NotebookLM](https://notebooklm.google.com/)** and click **New Notebook** [29, 34].
2.  Click **Website** or **Pasted Text** and add the URL or copy of your new roofing blog post [29, 34].
3.  Once the source is loaded, open the **Notebook Guide** on the bottom-right of your screen [28, 30, 35].
4.  Under the **Audio Overview** section, click **Customize** to set the focus (e.g., *"Focus on how local homeowners can protect their properties from hail storm damage using our Complimentary Professional Property Assessment (CPPA)"*) [36, 37].
5.  Click **Generate** [29, 30].
6.  Once generated, download the audio file, upload it to a free hosting platform like **SoundCloud**, and copy the embed code directly into your WordPress blog editor [28, 31, 38]!

---

#### 3) The Pineapple-Specific Example
Upload your blog post titled *"How Frisco Homeowners Can Safely Identify Storm Damage"* into NotebookLM. Under the custom audio settings, instruct the AI: 

> *"The hosts should discuss how local homeowners can document hail fractures using a formal **CPPA** assessment with Pineapple Roofing, emphasizing why verified licensing under **RCAT #03-0637** is critical for local trust."* [36, 37]

---

### Topic 4: Custom Prompts for the Studio Panel

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **Studio Prompt Wrapper** is a set of permanent operational rules and visual design constraints that you store in your local agent's settings so it always outputs code and content matching your exact brand [39, 40].

*   **Jargon Glossary:**
    *   **System Prompt**: The underlying, foundational instructions that govern how an AI assistant behaves, writes, and formats its outputs [41-43].

**Why It Matters to Pineapple Roofing:**
You don't want to type your license number, colors, and banned words every single time you generate a new piece of content [44-46]. Storing a single prompt wrapper in your local agentic environment guarantees that every suburb page, schema block, or GBP update is automatically compliant with your brand guidelines on the first run.

---

#### 2) The Exact Steps to Run
Paste this master prompt into your Claude Project instructions or your custom AI writing tool:

```text
Act as the Master Content Copywriter for Pineapple Roofing. Whenever I ask you to generate website pages, blog content, or social media updates, you must adhere to these absolute rules:

1. Always highlight our corporate license: RCAT #03-0637.
2. Always emphasize our manufacturer standard: IKO Certified Roofing Contractor.
3. The term "free" is strictly banned for all inspections, quotes, or services. All diagnostics must be written as a "Complimentary Professional Property Assessment" (CPPA).
4. For any front-end reports or design code, use our exact corporate color hex codes: Navy (#1A365D) and Gold (#FBC02D). Absolutely zero green elements are allowed.
```

---

#### 3) The Pineapple-Specific Example
If you ask your custom-configured agent: *"Write a quick 100-character description for our Stonebriar SEO page"*, it will automatically generate: 
> *"Get a premium IKO Certified shingle replacement from Stonebriar's trusted RCAT #03-0637 licensed specialists. Schedule your Complimentary Professional Property Assessment (CPPA) today."*

---

### Topic 5: Syncing Context to Your Local Studio Agentic OS

#### Yes, you can absolutely copy and paste all of these SOPs directly into your local Agentic OS!

To create a shared memory across all of your models (like Hermes, Claude Code, or Ollama) [13, 47]:

1.  **Create a single file** named `claude.md` in your main project folder [47, 48].
2.  Paste all of these SOPs, the brand rules, and your DataForSEO MCP credentials directly into that file [47, 48].
3.  When you start a session in Claude Code or boot up your local model in **Goal mode**, the system will read your `claude.md` file first [47, 49]. It instantly absorbs your exact business parameters as its **Shared Brain**, ensuring your AI agents never hallucinate, skip rules, or violate your brand firewall during executions [47, 48]!

---

📊 Would you like me to generate a fully populated, copy-paste-ready `claude.md` file designed for your local terminal project folder so you can sync these settings today?