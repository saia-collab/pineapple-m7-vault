# Pineapple Roofing & Restoration Agentic OS Playbook & SOP Core

## SYSTEM PARAMETERS & RULES
- **Primary Root Directory:** All operations, files, scripts, and terminal sessions must be strictly locked to `C:\Pineapple Contractors M7\` to prevent context leakage and directory entropy.
- **Brand Identity & Mission:** Focus exclusively on high-value storm restorations with an $18,000+ average project size across the Frisco/DFW market. Executive Leader: Tatafu Veehala. Core differentiation is anchored in heritage-driven, non-corporate storytelling that protects the brand’s "Mana". Any deviation from this high-ticket baseline is considered an architectural failure.
- **Authority Credentials:** All generated copy must strictly cite RCAT Licensed #03-0637, 5-star ratings, and IKO Certified RoofPro Team status.
- **Visual Design Sovereignty (The 140/95 Rule):**
  - **Gold Law:** All top-of-frame text overlays/banners must use Pineapple Gold (#FBC02D) at a height of 140px for action-oriented hooks (e.g., "Storm Alert" in Royal Navy Impact font).
  - **Navy Law:** All bottom-of-frame trust credentials must use Royal Navy (#1A365D) at a height of 95px, explicitly displaying: "Pineapple Contractors | RCAT Licensed #03-0637 | IKO Certified RoofPro Team" in Yellow Arial Bold font.
- **Banned Visuals & Elements:** Heritage Green (#2D7D46) is strictly banned and must NEVER be used in any corporate graphics, visual outputs, landing pages, or CSS templates.
- **The Navy Photo Moat:** All before/after project photos must include a 10px solid Royal Navy (#1A365D) border to signal official engineering documentation rather than casual snapshots.
- **Audio-First Caption Rule:** Text captions must sync directly to the loudest audio peaks, appearing exactly 2 frames before the spoken word and holding for a minimum of 18 frames (0.6s).
- **The Money Shield (Negative Filter):** Strictly prohibit and hard-block terms that attract low-value leads, price shoppers, or irrelevant traffic: "FREE", "cheap", "discount", "$0 Down", "$0 Out of Pocket", "repair patch", "shingle repair cost", "DIY", "GAF", "discount code", "job openings", or "salary".
- **Elite Language Swaps:**
  - Replace "Free" with "Complimentary Professional Photo Audit" (CPPA).
  - Replace "$0 out of pocket" or "$0 Down" with "Full restoration coverage evaluation".
  - Replace "GAF Certified" exclusively with "IKO Certified".
  - Replace "Adjusters miss damage" with "Comprehensive documentation for a successful claim".
  - Replace "Save Money" with "Protecting your family's investment".
- **Platform Separation Mandate:** Content generated under the corporate business playbook must ONLY be published to official business assets. Personal platform content architectures must remain strictly isolated to separate personal profiles. Audiences must never be mixed.
- **Operational Priority Hierarchy:** Priority 1 is the Personal Social Media Moat (Tatafu Veehala); Priority 2 is Business Scale Operations.
- **Cultural Grounding:** All copy, breakthrough announcements, scripts, and communications must honor a high-performance Polynesian family work ethic, weaving in the Fā‘ī Kaveikoula (Four Golden Pillars) and anchoring interactions with Faka'apa'apa (Respect) and Tauhi Vā (Maintaining Relationships). Eliminate generic corporate robot talk (e.g., hard-block "leverage" or "synergize"). Major breakthroughs or milestone announcements must conclude with the Tongan proverb anchor: "" (The path of the journey is respect).
- **Safety Execution State (DEC-005 Gate):** Every single campaign, ad set, and creative payload pushed via CLI, Claude Code, or Meta Ads MCP must deterministically land in the ad manager in a locked, strictly `PAUSED` state pending manual human review. Unattended live budget activation or expenditure of family resources without verification is strictly prohibited.
- **12-Month Safety Rule:** All automated social media posts must be pushed to Blotato as drafts scheduled exactly 12 months into the future to allow for a manual audit before being dragged to 'Today' for publication.
- **Outbox Shield (DEC-005):** No AI-drafted ad, social post, SMS, or carousel payload is permitted to go live until Saia gives explicit GO. All outputs land PAUSED in `01_Command_Center/Outbox_Drafts/`. No Airtable — decommissioned 2026-06-30.
- **Automated Kill & Scale Rules:** Automatically deactivate any creative with a Click-Through Rate (CTR) below 1.0% after 48 hours or 1,000 impressions. Scale campaign budgets by 20% every 48–72 hours for winning ad sets maintaining a 1.5%+ CTR and a Cost-Per-Lead (CPL) under $40.
- **Meta Pixel Conditioning Rule:** Never fire the Meta Pixel for top-of-funnel actions like clicks or DMs. Only fire the conversion pixel when a highly qualified prospect completes a high-friction action or books a call.
- **AI Setter Vocabulary Guardrails:** AI setter models must explicitly utilize high-equity phrases such as "home equity protection," "property value increase," and "architectural upgrades" to systematically condition the ad platform algorithm. The AI must respectfully push back against price-shoppers and never offer a discount.
- **Anti-Spike Bidding Rule:** Never use Auto Bidding when CPM costs spike, as it sends bad signals to the algorithm; instead, lower the daily budget to force a cost reset.
- **Messaging Refresh Frequency:** Creative volume must shift from minor variations of a single ad to 15 highly diverse, distinct messaging angles generated per month to prevent audience fatigue.
- **Retargeting Boundary Guardrail:** Paid retargeting audiences must be strictly limited to users who engaged with social media assets or visited the website within the last 30 days. Only deploy propaganda-style authority content.
- **Terminal Velocity Speed-to-Lead SLAs:** Response time must be under 5 minutes. Field reps must dial inbound leads within 120 seconds of an SMS alert. If unanswered, leave a voicemail, dispatch an immediate follow-up text, and set a task reminder to retry execution in exactly 10 minutes.
- **Lead Follow-Up Constraint:** Contact a lead a maximum of 7 times across a strict cadence (Minute 0 SMS/Email, Hour 1 Phone Call, Day 1 SMS, Day 3 Email, Day 5 SMS, Day 7 Email). Cease execution immediately if the target replies "Stop" or "Not interested".
- **Sovereign Local Core Security:** High-volume batch processing exceeding 50 data units or highly sensitive property/financial analytics must be routed locally to your on-premise Gemma model infrastructure via port `11434` to ensure absolute data privacy.
- **Sales Funnel & Recruiting Guardrail:** Top-of-funnel resume screening must be completely automated to eliminate bottlenecks. Never hire an inbound closer without routing them through a high-friction application funnel. Booking confirmation pages must be optimized using an urgency script, an FAQ video strategy, and heavy testimonials to pre-sell the candidate and lift show-up rates by 19% to 30%.
- **B2B ABM Mandate:** Eradicate generic, high-volume spam. All commercial contract outreach (property managers,developers) must execute a 1-to-1, hyper-personalized Account-Based Marketing strategy on LinkedIn.

## OPERATIONAL WORKFLOWS
### 1. Sovereign Infrastructure Provisioning (Oracle Cloud)
1. **Deployment:** Deploy on Oracle Cloud Free Tier using ARM-powered Ampere A1 Compute running Ubuntu 24.04 Minimal.
2. **Hardware Allocation:** Assign exactly 4 vCPUs, 24GB RAM, and 200GB Block Storage.
3. **Capacity Hardening:** Upgrade instance status to "Pay-As-You-Go" (PAYG) and attach a strict $1.00 budget limit to prevent oracle instance reclamation and secure priority server access.
4. **Firewall Security:** Enforce strict local UFW rules for ports 22 (SSH), 80/443 (Web Layouts), 8000 (Coolify Interface), and 6001-6002 (Real-time tracking protocols).
5. **VPS Cloud Persistence:** Deploy agent foundations exclusively on a Hostinger VPS ($5 environment) for 24/7 cloud persistence using Node.js v24 and NPM v11 to support ESM/CJS interop. 
6. **Session Collisions Prevention:** Ensure the Base URL configuration in `settings.json` maps explicitly to `https://opencode.ai/zen` (MiniMax-2.5) with an empty `oauth_token`. Connect the local Obsidian environment via MCP to prevent context resets.

### 2. The Agentic OS Command Loop
1. **Context Initialization:** Load `soul.md` from the local directory path to anchor brand DNA values, the corporate tone (Polynesian-proud, friendly, hardworking, zero corporate jargon), and system "Super Goals".
2. **Orchestration Tooling:** Launch global agent foundations via `npm install -g @anthropic-ai/claude-code`. Initialize the Antigravity 2.0 CLI to command and track parallel running sub-agents.
3. **Grounding Protocols:** Spin up the local NotebookLM MCP Server (`npx -y notebooklm-mcp-server start`) or execute `npx notebooklm-mcp-server refresh_auth` to secure persistent browser session tokens, providing zero-hallucination data access to project vaults.
4. **Execution Phases:** Route commands through Claude Code using `/plan` mode for non-destructive engineering discovery before executing structural modifications via `/edit`.
5. **Memory & Dashboards Sync:** Run the `obsidian_sync` tool or execute the `/vault` command daily at 08:00 AM CT to pull progress logs and state updates into your local dashboard workspace.

### 3. Daily Performance Briefing & Morning Handshake
1. **Daily Operator Routine (6:00 AM CT):** Run `daily-performance-brief.md` to generate a Virtual VP summary comparing active Meta advertising expenditure and internal CRM lead acquisition curves directly against the running 7-day average.
2. **Morning Handshake & Enrichment (7:30 AM CT):** Run `morning-handshake.md` to scan incoming leads. Execute `lead-enrichment.ts` to autonomously scrape regional data via Firecrawl (Zillow metrics for Year Built, Square Footage, Roof Material Profiles) and generate a local DFW weather threat briefing.
3. **Storm Response & Ad Deployment:** Upon detection of National Weather Service (NWS) hail alerts exceeding 2.0" in priority DFW ZIP codes (75033, 75034, 75035, 75056), trigger `storm-response.md`. Utilize the `/pineapple-ad-architect` agent skill to instantly draft 3 brand-compliant ad variations focused on the 30-day Texas storm insurance filing deadline.
4. **Denial Sniper Operations:** When an internal CRM claim status shifts to "Denied", execute `denial-sniper.ts`. The script polls Firecrawl for localized NOAA storm verification data on the exact date of loss/ZIP code and drafts a rigorous reinspection demand citing IBC §1507.16, IRC §R908.3.1.1, and Texas Insurance Code § 541/542.

### 4. AEO, GEO & Local Domination (Core 30 Strategy)
1. **Map Pack Audit:** Run a 169-point rank map grid (`/seo-audit`) to identify local pack visibility gaps across specific Frisco city blocks, mirroring Google Business Profile categories 1:1 on the website.
2. **Hub Construction:** Deploy 30 high-density service pages mapping specific restoration solutions to city-sector data. Mandate content generation exclusively for "Bottom of the Funnel" (BOFU) assets (local pricing guides, material comparisons, attribute-heavy FAQs).
3. **On-Page Compliance:** Delete generic adjectives like "Best" or "Top-rated" from H1 tags. Ensure all FAQ sections are uncollapsed for AI extraction. Embed YouTube project videos within the top 25% of the page to satisfy Gemini "Ask Maps" indexing requirements.
4. **AI-Extraction Formatting:** All pages must use a clear H1 header that matches the exact buyer question, answer the core query directly within the first 40 words (1-2 sentences), and present supporting details using short, scannable "CNBC-style" bullet points. Integrate unique business data (e.g., actual average project costs) to force LLMs to cite the brand as primary authority.
5. **Conversion Capture:** Build and embed a no-code "Free Tool" via v0 (e.g., "Roof Replacement ROI Estimator") on the generated pages to capture high-intent Answer Engine traffic, integrating a low-friction CTA (e.g., "Claim Your Complimentary 15-Point Winter Roof Vulnerability Audit").
6. **Review Attribute Extraction:** Replace generic "Leave us a review" prompts with "Can you tell us what happened?" to force customers to write attribute-heavy social proof that Google's algorithm rewards.

### 5. Media Asset Processing & The Multiplier Engine
1. **Asset Ingestion:** Field crews upload raw project, drone, and founder media files into `\02_Media_Vault\raw_photos\` and `\02_Media_Vault\raw_reels\`. Enforce the strict naming convention: `YEAR_MONTH_CAMPAIGN_ASSET-TYPE`.
2. **Photo Optimization Scripting:** Trigger `python optimize_photos.py` locally within the Tech Lab to programmatically process and validate compliance, sorting assets into three output buckets: raw unedited crops (`lsa`), branded banners with Royal Navy accents and transparent corner RCAT watermarks (`google_ads`), and ultra-compressed WebP format landing page assets at 75% quality (`landing_pages`).
3. **The Multiplier Slicing Trick:** Execute `node ASSET_ANALYZER.js` or the `/multiplier` command in the Tech Lab terminal. The script will ingest 33 core raw brand assets from the Media Vault, utilize FFmpeg/Remotion to slice drone footage into 15-second loops, attach the 140px Gold top banner and 95px Navy bottom banner, and interface with the Blotato API to generate 100+ unique ad variations distributed across three core templates: Angle 1 (Insurance), Angle 2 (Complimentary), and Angle 3 (Heritage).
4. **Faceless Distribution:** Route static property imagery through Veo3 within the local pipeline to generate high-VFX "simulated drone shows" for faceless YouTube niche distribution.
5. **Lindy Voice-to-Text Constraints:** Process daily job-site voice memos via Lindy. Format transcripts to start with a strong scroll-stopping hook, maintain professional authority, and extract specific proprietary material costs and customer pain points to instantly output formatted LinkedIn posts.

### 6. Paid Media Deployment, Scaling & Leads Nurture
1. **The "Deal Reviver" Hook Lifecycle:** Securely connect the Claude Co-Work environment to the CRM sheet layout using Model Context Protocols (MCPs). The exact second an inbound lead populates a row via Meta Ads Instant Forms, trigger the "Deal Reviver" Agent. Read row data, classify user intent (Roofing vs. Restoration), deduplicate phone numbers against the master records, and instantly dispatch an automated WhatsApp text/SMS follow-up within 60 seconds pitching a personalized CPPA tracking link.
2. **Andromeda 1 Ad Testing Deployment:** Eliminate campaign fragmentation by condensing budgets into a unified campaign to hit the 50-conversion learning threshold rapidly. Build out one Control Ad Set (proven stable assets) and two Testing Ad Sets. Enforce the **3-2-2 Testing Method**: each testing ad set must contain exactly 3 creatives, 2 primary text assets, and 2 headlines. Set a strict 7-day minimum budget at the ad set level equal to 1x your target CPA. After 7 days, eliminate the minimum floor, calculate Gross Profit per Transaction (GPT) relative to the campaign baseline, and replace the worst player in the Control set with the winner of the testing block.
3. **Native Meta Instant Forms Architecture:** Optimize forms for "More Volume" but enforce strict manual qualifier filtering using conditional routing logic:
   - *Question:* "Are you a homeowner?"
   - *Yes:* Route natively to "Submit Form" (Request Full Name, Email, and Phone using work email filters).
   - *No:* Route natively to "Close Form" (Disqualification screen).
4. **The 21 Google Ads Skills Execution:** Run the Google Agent CLI on a rigid cadence: Run Skill 10 (Budget Allocation Optimizer) daily to scale spend in storm-hit Frisco ZIPs. Run Skill 5 (Search Term Mining) and Negative Keyword Discovery every 48 hours to scrub low-intent queries. Run Skill 2 (Wasted Spend Finder) and Skill 17 (Auction Insights Analyzer) weekly to track regional competitor changes.
5. **Python CLI "Surfing" Scale Optimization:** Deploy the "Surfing" scaling rule via Python CLI: When a creative asset sustains a >1.5% CTR and generates leads below target CPA over a 48-hour window, automatically push an API payload to scale the daily budget by 10% to 30%. Implement cost caps and bid caps to protect backend margins.
6. **Wednesday Forensic Audit & Kill Execution:** Execute the Wednesday Forensic Audit via the Meta Ads CLI to run a full account spend audit. Enforce the 1% Kill Rule: automatically deactivate any creative with a CTR below 1.0% after 48 hours or 1,000 impressions.
7. **"Hammer Them" Propaganda Retargeting Loop:** Batch-record short propaganda video assets focused strictly on testimonials (D2D success stories), code compliance (local material codes exceeded), and objection handling (why premium quality costs more). Build a dedicated retargeting campaign with small daily budgets allocated to multiple individual ad sets. Optimize exclusively for "thru-play" performance to force the algorithm to prioritize users who watch videos to completion.
8. **The Overnight Heartbeat Loop:** Point the local terminal to `overnight_ad_loop.py` and fire the `/goal` and `/loop` commands before closing the environment. The local model must autonomously generate 50 Meta Ad variations, run them through the 90-point scoring rubric, discard failures, and save winners to a `MORNING_REVIEW.md` file in `01_Command_Center`.
9. **LSA Review Engine Automation:** Trigger the "Customer Success Subagent" to monitor the CRM "Project Status" column. The exact second a status transitions to "Job Complete," the agent drafts and stages a localized LSA 5-star review request sequence utilizing the Principle of Reciprocity and Community Identity.
10. **3-Segment Lead Activation:** Run automated follow-up sequences via the Loop Agent for stalled leads: send a "Value Drop" to Ghost Users (0 purchases), cross-sell sequences to One-and-Done buyers, and Referral Offers to Power Users.
11. **B2B Commercial Execution:** Deploy the "Partnership Scout" agent to continuously scrape local directories and LinkedIn to build a targeted list of Frisco-based commercial developers and multi-family property managers. Pass data to the "ABM Orchestrator" agent integrated via the Karrot API to automatically transmit tailored, 1-to-1 personalized outreach payloads.
12. **AI Recruiting Funnel Integration:** Integrate Lindy with the Juicebox platform. Configure the AI to automatically screen inbound applications, evaluate past construction experience, and auto-schedule calendar interviews with top-tier candidates.

## DELIVERABLE FRAMEWORKS
- **WAT Architecture (Workflows → Agents → Tools):** The core deterministic execution layer. Workflows establish the structural SOP files, specialized Agents manage distinct domains (Media Buyer, Forensic Scout, Growth Engineer), and local Tools manipulate raw data without fragile cloud dependencies.
- **The 4-Room Fala Architecture Layout:**
  - *Room 1 (The Scout):* Continuous automated directory scanning and weather payload collection identifying high-demand storm niches.
  - *Room 2 (The Architect):* Engineering premium "Grand Slam Offers" mapped to the $18,000+ transaction floor.
  - *Room 3 (The Megaphone):* Scaling execution via the "Rule of 100" (enforcing 100 physical or digital touchpoints daily per target territory).
  - *Room 4 (The Closer & The Loop):* Operating sales scripts, multi-agent pipelines, and 24/7 autonomous nurture sequences.
- **The "Open Jaw" AEO Model:** Simultaneous dominance of traditional Search and AI engines using structured metadata, high-velocity BOFU pricing guides, and integrated no-code tools (e.g., V0 estimators) to capture and convert citation traffic.
- **50/5/3 Lego Video Matrix Engine:** Programmatic content compilation assembly establishing a 50-second maximum duration, opening with a 5-second aggressive scroll-stopping hook pattern interrupt, and closing with 3-second (90-frame) CTA end cards displaying a Pineapple Gold action asset and the corporate contact link (972-928-0788). Stitched together, these yield 150-750 variations tracking the "Hidden Asset Decay" model.
- **1-3-12 Meta Ads Strategy Matrix:** Paid traffic infrastructure deploying 1 Centralized Campaign (CBO set to $250/week initial), 3 targeted Avatar sets (The Local Fan [Frisco 35-65], The Culture Seeker, The Founder’s Circle), and 12 modular variations per set utilizing Advantage+ Flex Media for automatic Feed/Reel deployment. Generates a 30-post caption grid containing explicit Tongan heliaki structural components.
- **Strategic Content Pillars:** Three-tier structural marketing blueprint:
  - *Pillar 1 (Storm Integrity):* Event-driven content using "Independent property storm audit" and "Certified roof damage assessment".
  - *Pillar 2 (Credential Authority):* Premium vertical positioning using "Premium shingle replacement experts" and "Professional slate and tile restoration".
  - *Pillar 3 (Heritage/Trust):* Cultural alignment emphasizing family values and absolute contract integrity.
- **H-CAMP (Autonomous Media) Protocol:** Background cron architectures monitoring local directories for raw media. The Hermes agent categorizes media by mission parameters, handing files to Hyperframes for automated "Video-as-Code" rendering under strict 140/95 brand spatial filters.
- **Hormozi 3-Angle Ad Matrix:** Campaign briefing architecture forcing three distinct psychological positioning hooks: 
  - *Angle 1 (Problem Reveal):* "The Insurance Deadline" highlighting the ticking clock on 30-day Texas claims.
  - *Angle 2 (Dream Outcome):* "Stress-Free Claim" emphasizing bulletproof engineering documentation and zero sales pressure.
  - *Angle 3 (Social Proof):* "Local Trust" citing 350+ DFW families, Polynesian heritage, and active RCAT licensing.
- **The Lead Bridge (Phone Script):** Mandatory 5-minute sales conversion cadence. Instantly confirm the scheduled appointment, eliminate friction by framing the visit as a "photo report rather than a sales pitch," and anchor familiarity by promising an SMS alert exactly 20 minutes before arriving on-site.
- **Google Ads Money Shield & 21 Skills Matrix:** Analytical script core to defend Google Ads traffic. Execute Weekly (Account Audit, Wasted Spend Finder, CPA Spike Diagnosis), 48-Hours (Search Term Mining, Negative Keywords), Monthly (Quality Score Audit), Daily (Budget Allocation Optimizer), and Monitor (Auction Insights Analyzer).
- **Sabri Suby Hyperdopamine Formula:** Construct all video scripts and static copy using a three-part rhythm: a striking Pattern Interrupt, Burning Intrigue, and a Big Specific Benefit, written cleanly at a 5th-grade reading level to instantly capture attention and convert prospects.
- **CARPARK Closing Framework:** Structured closing logic mapping out Circumstances (Confirm structural state), Agitation (Highlight dynamic risks & loss aversion), Resolve (Present permanent high-ticket solution), Proof (Show peer success), Agreement (Confirm desire for permanent fix), Review (Walkthrough engineering timeline), and Kickoff (Secure deposit authorization).
- **Birds of a Feather Persona Framework:** Specialized setter screening protocol utilizing specific "IQ Questions" (e.g., "Are you looking for a temporary cosmetic patch or a permanent structural solution?") to immediately filter out low-ticket leads in the conversational inbox.
- **Skeptic Repellent Framework:** Disqualification setter prompt instructing the AI framework to directly state to price-shoppers that the organization is "rarely the cheapest option" and requires an absolute commitment to structural longevity and elite quality.
- **Amplifier & Supported Claims Framework:** Specialized data repository feeding setter models deep third-party technical data, regional engineering codes exceeded, and historic restoration metrics to seamlessly justify premium value placement.
- **The Fox Tag Protocol:** Systematized labeling protocol used across all tracking parameters to isolate exactly which hooks, asset designs, or copy elements are driving front-end conversion bottlenecks or performance breakthroughs.
- **Propaganda Content Matrix:** Structured three-tiered retargeting system delivering hyper-focused content: D2D Homeowner Success Stories (Testimonials), Premium Core Justification Assets (Objection Handling), and Local Building Code Walkthroughs (Education).
- **Confirmation Page Accelerator:** Operational recruitment funnel architecture integrating an automated Urgency Script, an FAQ Video Strategy, and deep Testimonials directly on the booking confirmation page to lift conversion parameters by 19% to 30%.
- **Low-to-High Ticket Upsell Matrix:** Funnel layout mapping 3-4 strategic micro-upsells within the lead capture architecture, priced mathematically to optimize Average Order Value (AOV) and completely liquidate customer acquisition cost before the high-ticket pitch occurs.
- **Facebook Stars Monetization Sequence:** Focused three-part distribution: Post 1 (Educational breakdown of how Stars back the mission to shield local DFW families), Post 2 (High-stakes video walkthrough of complex $18,000+ slate/tile engineering installations), and Post 3 (Testimonial-driven conversion CTA prompting users to send Stars).
- **Toa Lead Scoring Matrix:** Deterministic inbound qualification routing:
  - *Score 80+ (TOA TIER):* Flag for same-day personal high-ticket outreach directly by Saia.
  - *Score 60-79 (QUALIFIED):* Route to standard 24-hour field rep assignment follow-up sequence.
  - *Score <60 (NURTURE):* Drop into the 7-day automated email/text brand tracking sequence.
- **10 Key Maintenance CLI Commands:** Intercept model health using `/model` (Verify core engine state), `/plan` (Non-destructive engineering exploration), `/stats` (Monitor system tokens), `/token` (Assess active window parameters), `/config`, `/history`, `/clear`, `/export`, `/search` (Execute Firecrawl discovery), and `/vault` (Enforce local Obsidian hard-sync).
- **Claude Knowledge Base (LLM Wiki Layout):**
  - `master/root/`: Contains `claw.md` (active system prompt architecture).
  - `inputs/raw/`: Dedicated structural dump directory for raw text, un-vetted transcripts, and links.
  - `wiki/00_Atlas/`: Highly structured persistent directory containing `index.md`, `log.md`, and `processed.md`.
  - `outputs/`: Output bucket containing production-ready scripts, assets, and JSON payload configurations.
- **The "Hivemind" Slack Architecture:** Operational orchestration deployment moving autonomous agent workflows directly into specialized internal Slack channels (`#lead-followup`, `#seo-generation`), transforming the physical workforce from manual task-doers into a real-time fleet of supervisor managers (The 100x Operator Deployment Model managed by the AI Czar).
- **Multi-Model Self-Critique Loop:** Draft the initial content asset, then command the agent to score its own output (1-10) against Elite Compliance criteria. Demand the agent implement its own suggestions until the score plateaus at 9.5+, then cross-check the output with a secondary model family to eliminate blind spots.
- **4-Agent Pipeline:**
  - *Orchestrator:* Traffic controller routing requests via intent and the `CLAUDE.md` map.
  - *Researcher:* BOFU intelligence gatherer scraping Voice of Customer (VOC) quotes, outputting `audience-profile.json`.
  - *Strategist:* Campaign architect converting research into actionable SOPs, outputting `creative-brief.json`.
  - *Copywriter:* Execution engine finalizing compliant copy using 6 core hook formulas (e.g., Harsh Reality, Contrarian Challenge).
- **IDEA File System (Obsidian Memory):** Karpathy-style persistent organization for `03_Knowledge_Mat`: I (Insights - strategic breakthroughs), D (Data - raw sheets/specs), E (Execution - SOPs/logs), A (Assets - brand kits/creative).
- **TCCA Prompt Stack:** A rigid prompting framework consisting of Task (desired action), Context (who/what/why), Constraints (rules/word counts/exclusions), and Ask (require AI to ask clarifying questions before execution).
- **B.L.A.S.T. Protocol:** 1. Blueprint (Vision/schema definition), 2. Link (API Connectivity handshake), 3. Architect (Separate SOPs from Tools/CLIs), 4. Stylize (Refinement/formatting payloads), 5. Trigger (Deployment and activating the Self-Annealing Repair Loop).

---

*End of Master Playbook.*
