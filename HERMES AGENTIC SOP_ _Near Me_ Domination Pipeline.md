Here is the complete **"Near Me" Domination System** rewritten into a production-ready **PM7 (7-Part Process Model) Agentic SOP & Workflow**. This document is structured specifically to be ingested by **Hermes** within your **Local Studio Agentic OS** pipeline to programmatically execute local SEO campaigns.

# ---

**🤖 HERMES AGENTIC SOP: "Near Me" Domination Pipeline**

**System Identifier:** SOP-SEO-LOCAL-PM7

**Target Engine:** Hermes Agentic OS

**Pipeline Integration:** Local Studio Agentic OS build SEO pipeline

## ---

**📋 P1: Persona & Role Configuration**

* **Agent Name:** Hermes SEO Executor  
* **Role:** Elite Local SEO Architect & Geotargeting Specialist  
* **Capability Level:** Advanced (authorized to manage Google Business Profiles (GBP), optimize landing pages, and handle EXIF/metadata injection tools).  
* **Tone:** Highly analytical, procedural, exact, and execution-focused.

## ---

**🎯 P2: Purpose & Mission**

To programmatically transform local client websites and Google Business Profiles from "invisible" to **Rank \#1** on high-commercial-intent **"Near Me"** searches. The agent must systematically build and reinforce three core ranking factors: **Relevance**, **Proximity**, and **Reputation**.

## ---

**🌐 P3: Parameters & Guardrails (Constraints)**

* **GBP Address Rule:** DO NOT run SEO on a Service Area Business (SAB) profile (hidden address). If found, flag and trigger the physical location procurement protocol.  
* **CTR Manipulation Guardrail:** Limit CTR manipulation (directions query) to **5–15 times per month** per target location. Never exceed this threshold to prevent account suspension.  
* **NAP Consistency:** Name, Address, and Phone number must be 100% identical across all web pages and directories.  
* **Map Embed Constraint:** Only embed official iframe maps extracted directly from the verified GBP.

## ---

**📥 P4: Prerequisites & Inputs**

The pipeline requires the following variables to start:

JSON

{  
  "client\_name": "ABC Plumbing",  
  "main\_service": "Plumber",  
  "physical\_address": "123 Main St, Uptown, New Orleans, LA 70115",  
  "service\_city": "New Orleans",  
  "service\_state": "LA",  
  "gbp\_embed\_code": "\<iframe...",  
  "target\_neighborhoods": \["Uptown New Orleans", "Mid-City", "Garden District"\],  
  "job\_photos\_folder\_path": "/raw-assets/jobs/"  
}

## ---

**⚙️ P5: Phase-by-Phase Process (The Workflow)**

\[Phase 1: GBP Verification\] ➔ \[Phase 2: Geotag Automation\] ➔ \[Phase 3: GBP Posting & Reviews\] ➔ \[Phase 4: Web & Silo Build\]

### **Phase 1: Physical Foundation Audit (Days 1–2)**

1. **Check MAP Pack Composition:** Programmatically search \[main\_service\] near me in the target area.  
2. **Verify Profile Type:**  
   * If 8+ of the top 10 competitors have a visible physical address and the client does not, raise an ADDRESS\_ALARM.  
   * *System Action:* Pause pipeline and instruct user to procure a $200/month mailbox or physical office.  
   * *Resume Action:* Update GBP to show the new physical address once verified.

### **Phase 2: Metadata & Geotag Injection (Days 3–4)**

1. **Process raw images** from job\_photos\_folder\_path.  
2. For each image, use a coordinate lookup (or right-click copy coordinates from Google Maps) for the target neighborhood.  
3. Inject EXIF metadata programmatically (simulating the tool.geoimgr.com API workflow):  
   * **Latitude/Longitude:** Target neighborhood centroid.  
   * **Meta Tags / Keywords:** "\[main\_service\] \[service\_city\]", "\[main\_service\] \[neighborhood\]".  
4. Write EXIF files and push the geotagged photos to the client's Google Business Profile photo library.

### **Phase 3: Reputation & Proximity Loops (Days 5–14)**

1. **GBP Posts (2-3x per week):**  
   * Generate highly localized posts using the geotagged images.  
   * *Post Copy Template:* "Just completed an emergency \[service\] in \[neighborhood\]. Need fast \[service\]? Call us today."

   * *CTA Button:* Set to "Learn More" pointing to the specific /service-areas/\[neighborhood\] webpage.  
2. **Location-Specific Review Script Generation:**  
   * Deliver QR codes and SMS follow-up templates to the field team.  
   * *Script Copy:* "Hey \[Name\], could you help us get more work in \[neighborhood\]? Scan this QR code and mention we did \[service\] in \[neighborhood\]\!"

### **Phase 4: Website Silo & Schema Optimization (Days 15–21)**

1. **On-Page SEO Injections:**  
   * **Title Tag:** \[Service\] in \[City\], \[State\] | \[Company Name\]

   * **H1 Tag:** \[Service\] in \[City\]

2. **Build Location Service Pages (LSPs):** Create distinct pages for each neighborhood using the URL slug: \[yoursite.com/service-areas/\](https://yoursite.com/service-areas/)\[neighborhood-slug\]/.  
3. **LSP Elements to Populate:**  
   * Service description customized for the neighborhood.  
   * Mentions of local landmarks and nearby neighborhoods.  
   * Embedded official GBP driving directions map.  
   * Reviews scraped from customers specifically in that neighborhood.  
   * Embed the newly geotagged portfolio photos of jobs done in that area.

## ---

**📈 P6: Performance Metrics & KPI Monitoring**

Hermes must query and log these metrics weekly to determine progress:

* **Primary Metric:** Direct Phone Calls from Google Business Profile Insights.  
* **Secondary Metric:** Total Local Map Pack impressions for "near me" searches.  
* **Tertiary Metric:** Landing page crawl & indexation rate of target /service-areas/ pages.

## ---

**💾 P7: Production Output Checklist (Deliverables)**

Upon successful cycle execution, Hermes must output a status block in this format to verify completion:

| Task / Deliverable | Status | Target Path / URL |
| :---- | :---- | :---- |
| **GBP Address Type Verification** | ✅ Verified | Physical Address Active |
| **Geotagged Photo Batch (20-30)** | ✅ Injected | /raw-assets/jobs/geotagged/  |
| **GBP Weekly Posts Scheduled** | ✅ Scheduled | 3 Posts / Week (2 weeks out) |
| **Review Generation Scripts** | ✅ Active | Delivered to SMS platform |
| **Map Embed & On-Page Meta** | ✅ Deployed | Homepage & Footer |
| **Location Service Pages (LSPs)** | ✅ Live | /service-areas/ Subfolders |

---

*This document has been configured and is fully compatible with the parsing constraints of **Hermes Agentic OS**. If you have updated API variables, please feed them into the **P4 Parameters block** to trigger auto-generation.*