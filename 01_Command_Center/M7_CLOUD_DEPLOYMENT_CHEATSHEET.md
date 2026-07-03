---
type: deployment_cheatsheet
title: M7 Cloud Deployment — copy-paste cheat sheet (GCP + Docker + Hermes)
status: active
last_updated: 2026-06-27
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# ☁️ M7 CLOUD DEPLOYMENT — COPY-PASTE CHEAT SHEET
**Why:** moves the whole Agent OS off your low-memory laptop onto a Google Cloud VM with Docker.
24/7 uptime, no more disk-full freezes, no Ollama OOM crashes. You copy-paste; the agent runs it.

> **How memory works (no databases needed):** Hermes is **filesystem-first**. It reads `CLAUDE.md` /
> `AGENTS.md` / `.hermes.md` as it walks folders (progressive context), and curates `MEMORY.md` + `USER.md`.
> Your Obsidian vault is the second brain via the Obsidian MCP (`obsidian_search`, `obsidian_read_note`,
> `obsidian_save_note`). So the folders ARE the memory — exactly what you already built.

---

## ⚠️ READ FIRST — the 2 traps that delete your work
1. **Docker volume persistence trap:** containers are wiped on restart unless you map a host volume.
   The compose below maps `/opt/m7-agentos/data → /opt/data` so memory/skills/history survive. Don't remove it.
2. **Never expose ports to the public internet** (3000 / 8642 / 9119). Use the SSH tunnel or Tailscale below.
   The `.env` also locks agents from rewriting policy/cron/workspace (`HERMES_ALLOW_*_WRITE=false`) — keep those false.

---

## ▶️ HAND THIS TO CLAUDE CODE / CODEX (one prompt, it does the rest)
```
Act as my DevOps engineer. Deploy the Pineapple M7 Agent OS to Google Cloud, step by step, pausing for me
to confirm each step. Use the exact commands in 01_Command_Center/M7_CLOUD_DEPLOYMENT_CHEATSHEET.md:
provision the e2-standard-4 Ubuntu VM, install Docker, write the .env and docker-compose.yml (keep the
persistent volume map and HERMES_ALLOW_*_WRITE=false), bring the stack up, and set up Tailscale. Never
expose ports publicly. Tell me exactly what to paste into Google Cloud Shell at each step. Don't guess my
secrets — leave the placeholder lines for me to fill.
```

---

## STEP 1 — Provision the VM (paste in Google Cloud Shell)
```bash
gcloud compute instances create m7-agentos-vm \
    --project="YOUR_GCP_PROJECT_ID" \
    --zone="us-central1-a" \
    --machine-type="e2-standard-4" \
    --image-family="ubuntu-2204-lts" \
    --image-project="ubuntu-os-cloud" \
    --boot-disk-size="80GB" \
    --boot-disk-type="pd-ssd" \
    --metadata=startup-script='#!/bin/bash
    apt-get update && apt-get upgrade -y
    apt-get install -y docker.io docker-compose git curl nodejs npm
    systemctl enable --now docker
    usermod -aG docker root
    '
```
*(e2-standard-4 = 4 vCPU / 16 GB RAM — comfortable for multi-agent + browser automation. Or n1-standard-2 to save cost.)*

## STEP 2 — SSH in + write credentials
```bash
gcloud compute ssh m7-agentos-vm --zone=us-central1-a
mkdir -p /opt/m7-agentos/data
nano /opt/m7-agentos/data/.env
```
Paste, then fill your real values (OpenRouter key, a secure password):
```env
OPENROUTER_API_KEY=sk-or-v1-your-openrouter-key-here
LLM_PROVIDER=openrouter
LLM_MODEL=anthropic/claude-sonnet-4.6
PORT=3000
AGENT_LOG_DB=/opt/data/memory/system_logs.db
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=your-secure-hex-token-here
AUTH_USER=m7-admin
AUTH_PASS=your-secure-ten-character-password-here
AUTH_COOKIE_SECURE=false
HERMES_HOST_LOCK=local
HERMES_ALLOW_POLICY_WRITE=false
HERMES_ALLOW_CRON_WRITE=false
HERMES_ALLOW_WORKSPACE_WRITE=false
```

## STEP 3 — Write the container manifest
```bash
nano /opt/m7-agentos/docker-compose.yml
```
```yaml
version: '3.8'
services:
  hermes-gateway:
    image: nousresearch/hermes-agent:latest
    container_name: m7-hermes-gateway
    restart: unless-stopped
    command: ["gateway", "run"]
    ports: ["8642:8642"]
    volumes: ["/opt/m7-agentos/data:/opt/data"]
    env_file: ["/opt/m7-agentos/data/.env"]
    logging: { driver: "json-file", options: { max-size: "10m", max-file: "5" } }
  hermes-dashboard:
    image: nousresearch/hermes-agent:latest
    container_name: m7-hermes-dashboard
    restart: unless-stopped
    depends_on: ["hermes-gateway"]
    command: ["dashboard", "--host", "0.0.0.0", "--no-open"]
    ports: ["9119:9119"]
    volumes: ["/opt/m7-agentos/data:/opt/data"]
    env_file: ["/opt/m7-agentos/data/.env"]
    logging: { driver: "json-file", options: { max-size: "10m", max-file: "5" } }
  m7-workspace:
    image: ghcr.io/outsourc-e/hermes-workspace:latest
    container_name: m7-workspace
    restart: unless-stopped
    depends_on: ["hermes-gateway"]
    ports: ["3000:3000"]
    volumes: ["/opt/m7-agentos/data:/home/workspace/.hermes"]
    environment:
      - HERMES_HOME=/home/workspace/.hermes
      - HERMES_WORKSPACE_DIR=/workspace
      - HERMES_API_URL=http://hermes-gateway:8642
      - HERMES_DASHBOARD_URL=http://hermes-dashboard:9119
    logging: { driver: "json-file", options: { max-size: "10m", max-file: "5" } }
networks:
  default: { name: m7-agent-network }
```

## STEP 4 — Start the stack
```bash
cd /opt/m7-agentos && docker compose up -d --build
docker compose ps        # confirm all 3 containers are "running"
```

## STEP 5 — Access it privately (pick ONE — never open public ports)
**A) SSH tunnel (laptop):**
```bash
ssh -N -L 3000:127.0.0.1:3000 -L 9119:127.0.0.1:9119 root@YOUR_GCP_VM_IP
```
Then open `http://localhost:3000` (workspace) and `http://localhost:9119` (Hermes).

**B) Tailscale (phone + laptop, best for ADHD on-the-go):**
```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```
Install Tailscale on your phone/laptop too → reach the dashboards from anywhere, invisible to the open web.

---

## KEEP IT RUNNING (survives SSH logout + reboot)
```bash
sudo tee /etc/systemd/system/hermes-agent.service >/dev/null <<'EOF'
[Unit]
Description=M7 Hermes Agent OS (docker compose)
After=docker.service
Requires=docker.service
[Service]
WorkingDirectory=/opt/m7-agentos
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
RemainAfterExit=true
[Install]
WantedBy=multi-user.target
EOF
sudo systemctl enable --now hermes-agent.service
```

## UPDATE / RESTART later
```bash
cd /opt/m7-agentos && docker compose pull && docker compose up -d   # update
docker compose logs -f hermes-gateway                               # watch logs
```

---

## CONNECT YOUR VAULT (so the cloud agent uses your real files as memory)
Point the Obsidian MCP at the vault (sync the vault to the VM via Google Drive or `git`), then the agent uses
`obsidian_search` / `obsidian_read_note` / `obsidian_save_note`. Hand-off prompt for Claude Code/Hermes:
```
Treat C:\Pineapple Contractors M7 (synced to the VM) as my memory. Read GROUNDING.md, MASTER_PLAYBOOK.md,
M7_EXECUTE.md, and 03_Knowledge_Mat/SHARED_MEMORY.md before any task. Draft everything PAUSED to
Outbox_Drafts, run brand_firewall.py --check, never restructure folders. Saia is the only publisher.
```

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
