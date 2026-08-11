---
source: "NotebookLM - PM7 SEO Mastery (Nico + Skool)"
notebook_id: 6039ce8a-a164-44a7-8abf-647d1157a871
note_id: fa7a22d0-f8f5-4dc9-aa22-5f370c4a7309
ingested: 2026-08-11
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing (Outbox Shield)
---

# Local MCP Integration and Strategic Roofing SEO Roadmap

STATUS: PAUSED

### Topic 1: Integrating Local Client Data into your Local MCP

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
An **MCP (Model Context Protocol) Connection for local data** is a secure digital pipeline that allows your offline terminal AI (**Claude Code** or **Hermes**) to read spreadsheet files (like customer lists or storm history tables) stored right on your computer.

*   *Jargon Gloss:* **JSON (JavaScript Object Notation)** is a simple, lightweight text format used to store and organize structured business data, like lists of clients.
*   *Jargon Gloss:* **Model Context Protocol (MCP)** is an open framework that lets your AI assistant safely use custom local files and tools on your computer as part of its reasoning brain.

**Why It Matters to Pineapple Roofing:**
Generic AI models on the internet don't know who your actual customers are, where they live, or when they last had their roof replaced. 

By feeding your private local client list into Claude Code via a custom MCP bridge, you can type a simple command in your terminal like: *"Which of our clients in Stonebriar haven't had their homes assessed since the May hail storm?"*. Claude will scan your local files, cross-reference them with local storm data, and draft personalized, license-compliant (**RCAT #03-0637**) follow-up messages instantly.

---

#### 2) The Exact Steps to Run This Week

##### Step A: Create Your Local Client Database File
Create a new file named `clients.json` in your local project root directory and paste your active customer records inside:

```json
[
  {
    "client_name": "Marcus Vance",
    "address": "4200 Legacy Dr, Frisco, TX 75034",
    "subdivision": "Stonebriar",
    "last_install_date": "2019-10-12",
    "shingle_type": "3-Tab Standard",
    "status": "Needs CPPA Audit"
  },
  {
    "client_name": "Deborah Sterling",
    "address": "1200 Newman Village Blvd, Frisco, TX 75033",
    "subdivision": "Newman Village",
    "last_install_date": "2024-05-01",
    "shingle_type": "IKO Certified Architectural Shingles",
    "status": "Monitor After Hail"
  }
]
```

##### Step B: Write the Local Python Query Script
Create a script named `client_search.py` in your project folder to query this client list:

```python
# client_search.py
import sys
import json

def find_subdivision_clients(subdivision_name):
    try:
        with open("clients.json", "r") as f:
            clients = json.load(f)
        matches = [c for c in clients if c["subdivision"].lower() == subdivision_name.lower()]
        return matches
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query_subdivision = sys.argv[1]
        print(json.dumps(find_subdivision_clients(query_subdivision), indent=2))
    else:
        print(json.dumps({"error": "Please provide a subdivision name (e.g., Stonebriar)"}))
```

##### Step C: Register the Local Tool in Your `.mcp.json`
Add this tool entry into your root `.mcp.json` file so Claude Code knows how to run it:

```json
{
  "mcpServers": {
    "pineapple-client-lookup": {
      "command": "python3",
      "args": [
        "client_search.py",
        "{{subdivision}}"
      ]
    }
  }
}
```

Now, launch Claude Code (`claude` in your terminal) and ask it to scan your clients by typing: 
> *"Use the local pineapple-client-lookup tool to find our active leads in Newman Village."*

---

#### 3) The Pineapple-Specific Example
When you run the tool for **Newman Village**, Claude Code will locate Deborah Sterling’s account and automatically output:

> 🔷 **Local Lead Found in Newman Village (ZIP 75033):**
> *Client:* Deborah Sterling  
> *Current Shingle:* IKO Certified Architectural Shingles  
> *Action:* Draft an outreach template notifying them that North Frisco's expansive clay-soil shifting, combined with recent seasonal hail, requires an attic rafter and roof surface check. Offer our signature **Complimentary Professional Property Assessment (CPPA)** under our **RCAT #03-0637** license guidelines.

---

### Topic 2: Strategic SEO/GEO Roadmap (Today, This Week, This Month)

To capture local search traffic during your WordPress migration, execute this structured, high-velocity plan built from your community's master playbook:

```
[ TODAY: Launch Core Assets ] ──> [ THIS WEEK: Bridge Trust ] ──> [ THIS MONTH: Scale Local Dominance ]
  - Paste WP CPPA Calculator        - Set cPanel 301 Redirects       - Build out 10 Suburb Pages
  - Deploy Reputation Firewall      - Upload root llm.txt file       - Schedule automated Reels
```

#### 🔷 EXECUTE TODAY: Immediate Lead Capture & Protection
1.  **Install your WordPress Lead Tool**: Copy the custom code inside your **`cppa-calculator-code.md`** file (located in your Studio panel) and paste it into a **Custom HTML Block** inside your new WordPress editor. This provides a lightning-fast, zero-slop interactive calculator on your site.
2.  **Activate Your Reputation Firewall**: Import your **`pably-gbp-responder.json`** file into Pably Connect. Add your Google Business Profile credentials and your OpenRouter API key. This will automatically publish positive reviews while intercepting negative reviews under 4 stars as private drafts.

#### 🔷 EXECUTE THIS WEEK: Authority Migration & Agentic Compliance
1.  **Deploy your 301 Redirect Script**: Download **`301-redirects-v2.conf`** from your Studio panel. Copy its redirection directives and paste them at the absolute top of the `.htaccess` file on your legacy site (`pineapplecontractors.com`). This instantly routes all established traffic and Google rankings to your new domain (`pineappleroofingllc.com`) without dropping a single call.
2.  **Upload Your AI Agent Map**: Upload your customized **`llm.txt`** file directly to your website’s root directory (`pineappleroofingllc.com/llm.txt`) so AI search bots from OpenAI and Perplexity can crawl and recommend your business credentials instantly.

#### 🔷 EXECUTE THIS MONTH: Local Suburb Scalability & Video Traffic
1.  **Complete Your Suburb Landers**: Use the **50% Unique Content Rule** to build dedicated pages for all your remaining DFW target neighborhoods (Starwood, Westside, Newman Village) using local soil shifting and neighborhood guidelines.
2.  **Run the Video Pipeline**: Set up **Repurpose.io** to automatically strip watermarks from your TikTok videos and drop them into your Google Drive root. Have your crews record simple 60-second job site videos explaining shingle damage, highlighting your **RCAT #03-0637** license, and guiding homeowners to book our high-converting **CPPA**.

---

### Topic 3: Setting up the "Shared Brain" in `claude.md`

#### 1) Plain-English "What It Is + Why It Matters for a Frisco Roofer"
A **`claude.md` file** is a plain text file placed in your local project folder that acts as a permanent, shared memory block. It contains all your brand rules, state licenses, visual designs, and terminology guardrails.

*   *Jargon Gloss:* **System Prompt / Shared Brain** is a core instruction set that is automatically read by your local AI engines before they write a single word, preventing errors or compliance slip-ups.

**Why It Matters to Pineapple Roofing:**
You don't want to waste time explaining your business constraints every time you open your terminal or draft an article. Placing **`claude.md`** in your root folder creates a shared memory. Claude Code, Hermes, and your local Ollama models will read it automatically, ensuring 100% of your content stays strictly brand-compliant without any manual editing.

---

#### 2) The Exact Steps to Run This Week

I have already generated, validated, and published your complete **`claude.md`** configuration file directly to your **Studio panel**.

To activate it:
1.  Download **`claude.md`** from your Studio panel.
2.  Save it directly to your local workspace project directory (e.g., `/projects/pineapple-roofing/`).
3.  **Claude Code Integration**: When you start Claude Code in your terminal, it will automatically crawl and read `claude.md` as context before generating any copy or layout assets.
4.  **Hermes / Local Ollama Integration**: When launching your offline models, use this exact command to link their system memory directly to your local file:
    ```bash
    ollama run hermes3:70b --system "You are the Lead Systems Architect for PM7. Read the brand parameters in the local 'claude.md' file before answering. Enforce the RCAT #03-0637 license, IKO Certified status, and the CPPA Brand Firewall across all generated copy."
    ```

---

#### 3) The Pineapple-Specific Example
Because `claude.md` contains our strict Brand Firewall rules, if you ask your local Hermes model in Goal Mode to write a Facebook post, it will read your local shared memory, bypass the word "free", and automatically generate this compliant copy:

> *"Protect your Frisco home before the next storm hits. Our IKO Certified and RCAT #03-0637 licensed roofing crews are out in Stonebriar today conducting specialized diagnostics. Contact us to schedule your custom **Complimentary Professional Property Assessment (CPPA)** today."*

---

⭐ **This week's one action:** Download **`claude.md`** from your Studio panel and save it directly in your local project folder so Claude Code and Hermes can start using your customized shared memory brain today!