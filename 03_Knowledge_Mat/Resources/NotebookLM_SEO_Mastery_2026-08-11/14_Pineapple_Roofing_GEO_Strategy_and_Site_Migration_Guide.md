---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: b81f4eff-fd97-4eca-9642-160bcc3f58b9
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing (Outbox Shield)
---

# Pineapple Roofing GEO Strategy and Site Migration Guide

### Topic 1: Finding Roofing "Fan-Out Queries" with Datawise

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**Fan-out queries** are the hidden, parallel questions that AI search engines (like ChatGPT Search or Perplexity) automatically generate behind the scenes to research, verify, and compile a final answer for a user [1-3]. 

*   **Jargon Glossary:**
    *   **Fan-Out Queries**: The subsequent, hidden search queries that an AI engine automatically executes in parallel to fully answer a user's initial question [1-3].
    *   **GEO (Generative Engine Optimization)**: The process of structuring and optimizing website content specifically so AI search engines can easily find, cite, and recommend your business [4, 5].

**Why it matters to Pineapple Roofing:**
Homeowners in Frisco don't just type keywords into search boxes anymore; they type full conversational questions into AI engines (e.g., *"Who should I hire to check my roof after a hail storm in Frisco?"*) [1, 6, 7]. To answer this, ChatGPT's brain "fans out" into parallel queries like *"Is Pineapple Roofing licensed in Texas?"* or *"What roofing certifications does Pineapple Roofing have?"* [1, 2, 6]. 

If your website doesn't explicitly answer these hidden fan-out queries in tight, direct paragraphs, the AI will recommend your competitor instead [6]. By capturing these queries, you ensure your site is the absolute source of truth for the AI's research [8].

---

#### 2) The Exact Steps to Run This Week
To discover these hidden AI search queries for your roofing services:
1.  Go to the free search intelligence tool **Datawise** (sign up with the promo code `keyword 48` to get 48 hours of unlimited free access) [6, 9, 10].
2.  Navigate to the keyword research dashboard and click on the **Fan-out queries** tab [1, 4, 11].
3.  Enter your seed keyword: **`hail damage roof repair`** or **`metal roofing contractor`** [4, 11, 12].
4.  Set your target country to **United States** and language to **English** (the dataset is so new that AI search data is currently tracked here first) [4].
5.  Click **Explore**, select the questions that align with your actual services, and click **Export to CSV** to hand off to your writing template [13, 14].

---

#### 3) The Pineapple-Specific Example
*   **Seed Keyword Searched**: "Frisco hail damage" [11]
*   **Fan-Out Query Discovered**: *"Does homeowner insurance cover IKO shingle roof replacement after hail?"* [15]
*   **How to optimize your page**: Place an H2 question header at the bottom of your **Stonebriar** landing page and answer it instantly using a **30-to-60-word Content Capsule** [16-18]:

> **H2: Does homeowner insurance cover IKO shingle roof replacement after a Frisco storm?**
> 
> **Pineapple Content Capsule:** Yes. Most Texas homeowners' insurance policies cover full roof replacements for storm damage. Pineapple Roofing is an **RCAT #03-0637** licensed contractor that provides a **Complimentary Professional Photo Audit (CPPA)** to document structural shingle damage, ensuring your claim meets premium **IKO Certified** installation guidelines [16-18].

---

### Topic 2: Setting Up 301 Redirects to Keep Your Migration Traffic

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **301 redirect** is a permanent digital redirect rule placed on your server that automatically forwards visitors and search engine bots from an old website link to a new address [previous turn].

*   **Jargon Glossary:**
    *   **301 Redirect**: A permanent redirect method that tells search engines a web page has moved forever, transferring 100% of its ranking power (trust) to the new link [previous turn].
    *   **.htaccess File**: A simple configuration file on Apache-based web hosting servers that acts as the traffic controller for your web domains [previous turn].
    *   **Link Juice (SEO Authority)**: The ranking trust and power a webpage accumulates over time from search engines and external links [19, 20].

**Why it matters to Pineapple Roofing:**
Your old agency-built site (`pineapplecontractors.com`) currently holds all your organic foot traffic and search authority, but you have no control over it [User request]. You are migrating to WordPress on `pineappleroofingllc.com` to take the steering wheel [User request]. 

If you just shut down the old site, you are committing SEO suicide—you will lose years of Google authority overnight [previous turn]. Setting up a **301 redirect script** ensures that all the "link juice" and customer foot traffic from the old site flow directly to your new WordPress pages without a single dropped call [previous turn].

---

#### 2) The Exact Steps to Run This Week
I have already generated and published your custom, brand-compliant redirect file in your Studio panel under **`301-redirects.conf`** [previous turn].

To apply these rules and protect your traffic:
1.  Log into the hosting control panel (cPanel) of your old site: `pineapplecontractors.com` [previous turn].
2.  Go to the **File Manager**, open the root folder (usually `/public_html/`), and look for the hidden file named **`.htaccess`** [previous turn].
3.  Download your **`301-redirects.conf`** file from your Studio panel [previous turn].
4.  Copy the code block inside it, paste it at the very top of your old site's `.htaccess` file, and click **Save** [previous turn].

---

#### 3) The Pineapple-Specific Example
The redirect script strictly maps the old agency's messy, generic links directly to your new premium brand terminology [SOP in previous turn]:

```apache
# Safely redirects old, fluffy traffic to your new signature CPPA framework
Redirect 301 /free-inspection https://pineappleroofingllc.com/cppa
Redirect 301 /free-estimate https://pineappleroofingllc.com/cppa
Redirect 301 /free-quote https://pineappleroofingllc.com/cppa
```
This forces any old search traffic looking for "free quotes" to land on your high-converting, licensed **RCAT #03-0637** and **IKO Certified** assessment page [SOP in previous turn].

---

### Topic 3: Consolidating Sources to Beat the 300-Source Limit

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
**File Consolidation** is the process of merging multiple small notes, checklists, and text documents into a single "master document" before uploading it to NotebookLM [previous turn].

*   **Jargon Glossary:**
    *   **NotebookLM Project**: A custom workspace where you upload business files so the AI can act as your personalized, source-grounded expert [21, 22].
    *   **File Consolidation**: Combining multiple short files into one formatted text file to bypass software upload count limits [previous turn].

**Why it matters to Pineapple Roofing:**
Google NotebookLM caps your uploads at **300 sources per notebook** [290, previous turn]. If you try to upload every single neighborhood checklist, daily task list, and roofing SOP as a separate document, you will hit that ceiling instantly. 

By consolidating your custom **SEO Playbook, SOPs, and tasks** into a single master Google Doc, you bypass the file-count limit and feed the AI massive amounts of brand context while only using up a single source slot [previous turn].

---

#### 2) The Exact Steps to Run This Week
To clear up slots in your notebook and import your new playbook:
1.  Open your Google Drive and create a new Google Doc named **`Pineapple Roofing - Master SOP & Playbook 2026`** [25, 26, previous turn].
2.  Open your current **SEO Playbook**, your **Review Responder SOP**, and your **Weekly Tasks** [9, 25, previous turn].
3.  Copy and paste the text of all three documents sequentially into this single Google Doc [25, previous turn].
4.  Organize them neatly using simple Markdown headers (use `#` for main titles, and `##` for sub-sections) [23].
5.  In your NotebookLM source panel, locate and **delete** the three smaller, individual files you just copied [previous turn].
6.  Import your newly compiled **Master Google Doc** as a single source [previous turn].

---

#### 3) The Pineapple-Specific Example
By combining your fragmented documents, your Master file will look like this:

```markdown
# PINEAPPLE ROOFING MASTER CONTEXT & SYSTEM RUNBOOK
- Primary Domain: https://pineappleroofingllc.com
- Authority License: RCAT #03-0637 Licensed
- Shingle Standard: IKO Certified Roofing Contractor

## SECTION 1: GBP Review Automation SOP
... [Paste your Positive and Negative review filter steps here] ...

## SECTION 2: Suburb SEO & Location Strategy
... [Paste your Stonebriar and Newman Village targeting guidelines here] ...

## SECTION 3: Transactional Offer Compliance (The Brand Firewall)
... [Enforce using CPPA (Complimentary Professional Photo Audit) terms] ...
```
By doing this, you instantly free up two source slots in your notebook while retaining 100% of your operational memory to write perfect, localized roofing content [previous turn]!

---

📊 I can map out your complete parent-child site structure for all 10 Frisco neighborhoods (like Newman Village, Starwood, and Westside) so your developer can build all these Astro pages out in one day. Want me to generate that file in your scratch folder?