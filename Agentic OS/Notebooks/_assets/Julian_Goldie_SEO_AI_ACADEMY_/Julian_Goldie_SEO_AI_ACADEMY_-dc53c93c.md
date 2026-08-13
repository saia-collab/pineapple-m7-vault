# SOP: Advanced AI Operations Plan for Pineapple Business Automation

### 1. Strategic Infrastructure Overview
This operation deploys a decentralized, hybrid "Paperclip + Hermes" architecture designed to weaponize agentic intelligence while ruthlessly optimizing inference costs. By utilizing Paperclip as a decentralized Agentic ERP (Enterprise Resource Planning) system and Hermes as the self-evolving intelligence layer, we ensure that the business logic is not just automated, but strategically improved at every compute node.

**The Three Pillars of Operation:**
*   **Paperclip (Orchestration):** The "Company Operating System." It functions as an agentic ERP, managing the organizational chart, departmental hierarchies, and strictly enforcing **Task Budgets** across the agent workforce.
*   **Hermes (Agent Intelligence):** The cognitive core. Unlike stateless LLMs, Hermes operates with a persistent learning loop, allowing agents to evolve their own capabilities through skill distillation.
*   **Hybrid Model Environment:** 
    *   **Local Inference:** Gemma 4 and Qwen 3.6 (Mixture of Experts) handle high-volume, data-sensitive logic at zero marginal API cost via Ollama.
    *   **Cloud Orchestration:** Claude Opus 4.7 provides "X-High" reasoning for mission-critical strategic decisions and cross-departmental supervision.

---

### 2. Phase I: Local Environment & Model Provisioning
Establishing the local hardware layer is the primary directive for ensuring "zero-cost" operational scalability.

1.  **Ollama Installation:** Deploy the Ollama backend to handle local inference. Verify the local server status via `ollama serve`. The system must be responsive at `localhost:11434` before proceeding.
2.  **Model Acquisition:** Provision the local model weights using the following terminal commands:
    *   `ollama run gemma4`: Deployed for brand marketing and iterative copy tasks.
    *   `ollama run qwen3.6`: A high-context Mixture of Experts (MoE) model utilized for 1M token research processing.
3.  **Hardware Verification:** Architect-level oversight requires a pre-flight check of GPU VRAM and system RAM. 

> **Warning:** Running Qwen 3.6 (MoE) at high context windows requires substantial VRAM. Ensure your local hardware nodes are provisioned with at least 24GB of VRAM to avoid high-latency bottlenecks in the automation pipeline.

---

### 3. Phase II: Hermes Agent & Paperclip Integration
The deployment of the agentic core requires a seamless link between local nodes and the "NASA-like" visual operating system.

1.  **Hermes Installation:** Execute the deployment of the Hermes Agent core and its associated environment:
    ```bash
    npm install hermes-agent-core
    ```
2.  **Paperclip Dashboard Setup:** Clone the React-based Paperclip dashboard. This provides the visual interface for the Agentic ERP. Map the pineapple business departments (Research, Marketing, Sales) within the UI.
3.  **Mission Control Configuration:** Access the browser-based Mission Control terminal. This visual OS provides total transparency into the agent's file system and logic.
    *   **Inference Routing:** Link the Anthropic API (for Opus 4.7) and the Localhost API (for Ollama nodes).
    *   **Gateway Setup:** Configure the **Gateway** for Telegram and Slack channels. This allows for mobile, "Zero-Downtime Oversight" where the Architect can monitor agent pings and intervene from any device.

---

### 4. Departmental Configurations: The Hermes Profiles
Profiles define the reasoning depth and model allocation for specific business nodes.

| Role Name | Business Function | AI Model Stack | Logic Configuration |
| :--- | :--- | :--- | :--- |
| **Ananas-CEO** | Strategic Coordinator | Claude Opus 4.7 | **X-High Effort**; manages **Task Budgets** to prioritize tokens on complex logistics; enforces budget compliance. |
| **Pina-Researcher** | Market Analyst | Qwen 3.6 (MoE) | **Mixture of Experts Efficiency**; 1M token context window for scanning global agriculture news and pricing trends. |
| **Gold-Copywriter** | Brand Marketer | Gemma 4 (Local) | **Zero-Cost Inference**; localized ad-copy and newsletter generation with persistent brand-voice memory. |
| **Maui-Outreach** | B2B Distributor | Gemma 4 + Opus 4.7 | **Routing Logic**; uses Gemma 4 for lead vetting and routes high-value contract negotiations to Opus 4.7. |

---

### 5. Activating the Learning Loop & Skill Generation
Hermes agents are designed for "Self-Evolution," transforming successful task outcomes into persistent business assets.

1.  **Task Execution:** The agent executes a directive (e.g., "Analyze competitor pineapple pricing in Maui").
2.  **Skill Distillation:** Upon success, the agent analyzes the session, identifies successful patterns, and writes a **Skill**. This is a **Markdown-formatted artifact** stored directly in the local file system.
3.  **Cross-Session Memory:** In future sessions, the agent reads these Markdown Skills from the file system. This ensures the agent "remembers" preferred negotiation tactics or formatting rules without needing a full re-prompt, creating an auditworthy evolution of business logic.

---

### 6. Operational Workflows & Orchestration
The Paperclip dashboard synchronizes departmental effort through automated hand-offs and token management.

**The Content-to-Conversion Workflow:**
*   **Data Acquisition:** **Pina-Researcher** utilizes its MoE architecture to ingest massive datasets on agricultural pricing, outputting a market intelligence report.
*   **Creative Production:** This report is handed to the **Gold-Copywriter**, who generates high-volume campaigns on zero-cost local nodes.
*   **Strategic Supervision:** The **Ananas-CEO** reviews the assets. Using **Task Budgets**, the CEO agent allocates higher reasoning tokens (Opus 4.7) only to the most critical "hard parts" of the campaign, ensuring the **Maui-Outreach** agent doesn't over-consume resources on low-value B2B leads.

---

### 7. Maintenance & Security Protocols
To maintain enterprise-grade integrity, all agentic behavior must be audited via the Mission Control analytics suite.

*   **Token Consumption Monitoring:** Real-time auditing of usage via the **Mission Control Analytics Dashboard**.
*   **Ultra Review (Pre-flight Safety):** Before any agent-generated code or complex logic is pushed to a live environment, the Architect must trigger the `/ultrareview` command. This dedicated review session forces the AI to audit its own changes, catching design flaws and logic bugs before they impact operations.
*   **Operational Security:** Ensure CSRF and CSP protections are active in Mission Control to secure the agent gateway.

> **Pro-Tip:** For extended workflows, enable **Auto Mode** for Max users. This reduces permission friction, allowing agents to make background decisions during long sessions, though the Architect should always run a final `/ultrareview` before execution.