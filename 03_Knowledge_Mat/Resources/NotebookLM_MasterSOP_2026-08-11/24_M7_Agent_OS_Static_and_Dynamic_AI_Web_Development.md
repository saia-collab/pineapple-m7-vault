---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 9bbad442-b8d4-43f6-ab22-31cc100afb46
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# M7 Agent OS: Static and Dynamic AI Web Development

### 🌐 THE MODERN PARADIGMS OF AI WEBSITE DEVELOPMENT

AI website development has transitioned from static, lifeless templates to highly interactive, automated, and context-aware digital assets [cite: 296, 334]. In your local **M7 Agent OS**, you have two distinct, high-performance paths to build and manage your sites [cite: 240, 241, 332]:

1. **The Static Paradigm** — High-speed, luxury landing pages utilizing the **One-Take Website Engine** (Claude Code + Seedance 2.5) hosted on Netlify [cite: 293, 297, 305].
2. **The Dynamic Paradigm** — Direct, headless content and database automation over your secure WordPress server via **WP MCP Ultimate** [cite: 248, 323, 326].

---

### 🎨 1. THE STATIC PATH: THE ONE-TAKE WEBSITE ENGINE (SEEdANCE 2.5 + CLAUDE CODE)

Until recently, premium websites featuring rotating products, interactive depth, and fluid scroll animations required a full agency, weeks of motion design work, and heavy JavaScript frameworks [cite: 296, 297]. 

The **One-Take Website Engine** collapses this process into a single afternoon conversation [cite: 297]. It relies on a simple technical "cheat": **most high-end interactive motion is actually a single video file, and the user's scrollbar acts as the remote playhead** [cite: 298].

```
  Visitor Scrolls Down ──► Video Plays Forward
  Visitor Scrolls Up   ──► Video Plays Backward
  (Motion is responsive and tied entirely to the user's focus)
``` [cite: 298, 304, 307]

#### 🚀 How You Build It (The Step-by-Step Flow) [cite: 300]:
1.  **Connect the Video MCP:** You link ByteDance's **Seedance 2.5** (housed inside Higgsfield) directly to your Claude Code workspace using the Higgsfield Model Context Protocol (MCP) [cite: 293, 301]. This lets Claude generate high-fidelity videos straight inside your terminal session [cite: 301].
2.  **Generate "The Take":** You prompt the camera directly to record one continuous, 30-second, high-resolution visual shot (such as a slow, golden-hour rotation of a premium roof shingle) [cite: 300, 307, 308].
3.  **Design the Code Structure:** You take screenshots of layouts you admire [cite: 302]. Claude studies their typography, margins, and hierarchy, and builds the raw HTML around your newly generated video [cite: 303].
4.  **Wire the Scroll Position:** With one plain-English command (*"Tie this video to the scroll position"*), Claude writes the underlying scroll-scrubbing parameters [cite: 304].
5.  **Direct Netlify Publish:** You type *"Push this live"* [cite: 300]. The local Netlify CLI compiles your clean assets, hosts the site, and deploys it to your custom domain without you ever touching a hosting dashboard [cite: 222, 237, 305].

#### 🛑 The 3 Non-Negotiable Rules of Premium AI Design [cite: 307, 308]:
*   **Rule 1: Restraint:** Use only one or two motion effects per page [cite: 307]. The stillness around an effect is what gives it premium weight [cite: 307].
*   **Rule 2: Name the Camera:** Avoid generic vibes like "cinematic" [cite: 307]. Explicitly instruct the model on lens moves (*"slow push-in, static"*), lighting (*"single window golden hour"*), and pace (*"slow motion"*)[cite: 307].
*   **Rule 3: Kill the Auto-Loop:** Endless background video loops scream "cheap AI template" [cite: 307]. Ensure video motion only triggers when a user scrolls, hovers, or interacts with the cursor [cite: 307].

---

### 🔌 2. THE DYNAMIC PATH: HEADLESS WP WITH "WP MCP ULTIMATE"

For your active CRM and large content clusters (like your **33-page Frisco and regional city pages**), self-hosted WordPress is your operational powerhouse [cite: 175, 200, 201]. Historically, managing WordPress with AI required complex, brittle chains of different plugins that constantly broke during core updates [cite: 318, 319].

**WP MCP Ultimate** solves this by consolidating the entire interface into a single, self-contained **Streamable HTTP** server plug [cite: 318, 320, 322].

```
  Your Local AI  ───────►  WP MCP Ultimate  ───────►  58 Native WordPress
  (Claude / Cursor)        (Basic Auth / HTTPS)       Abilities Across 13 Domains
``` [cite: 320, 321, 328]

#### 🛠️ What the AI Can Do Natively in Your Terminal [cite: 321]:
*   **Manage Content:** List, create, patch, and publish posts, pages, and categories in seconds [cite: 321].
*   **Handle Media Assets:** Upload, crop, delete, and dynamically inject optimized Alt tags into your media library [cite: 321, 322].
*   **System Controls:** List active users, modify system configurations, moderate incoming spam comments, and even install or activate core plugins (like Yoast SEO or Redirection) on the fly [cite: 251, 321].

#### 🔐 Quick-Connect Settings (Under 2 Minutes) [cite: 323]:
1.  Download the plugin zip file and upload it to your WordPress admin console [cite: 323].
2.  Navigate to **Tools \\(\rightarrow\\) MCP Ultimate** and click **Generate** to secure your WordPress Application Password (looks like `xxxx xxxx xxxx xxxx xxxx xxxx`) [cite: 259, 323].
3.  Add the generated Streamable HTTP snippet directly to your local **`~/.claude/settings.json`** file [cite: 260, 324]:
    ```json
    {
      "mcpServers": {
        "wordpress": {
          "type": "streamable-http",
          "url": "https://pineappleroofingllc.com/wp-json/mcp/wp-mcp-ultimate",
          "headers": {
            "Authorization": "Basic BASE64_CREDENTIALS"
          }
        }
      }
    }
    ``` [cite: 260, 324]

Now, your terminal-based agents can write high-authority local landing pages (completely conforming to your **0% green / CPPA brand laws**), compile your schemas, and publish them directly to your WordPress backend in one seamless command sequence [cite: 176, 243, 327]!

---


📂 **Next Step Suggestion:**  
I can configure a custom **`one_take_builder.py`** script inside your `04_Tech_Lab/scripts/` folder to help guide your local Claude Code interface when structuring its first Scroll-Rotation landing page project [cite: 181, 304]. Would you like me to map out this visual generation script?