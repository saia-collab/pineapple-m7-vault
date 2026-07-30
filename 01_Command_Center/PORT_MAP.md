# 🔌 M7 PORT MAP — read before changing any port

Every local service and the port it owns. Changing one of these without
checking here is how the SEO Office tab broke.

| Port | Service | Started by | Hardcoded? |
|------|---------|-----------|-----------|
| 3000 | **SEO Office** (`~/seo-office`, `pnpm dev`) | you, manually | ✅ **yes** — Agentic OS iframes `localhost:3000/office` |
| 3001 | **OpenSEO** (Docker, `~/open-seo`) | `docker compose up -d` | ✅ yes |
| 3100 | **Paperclip** daemon | `npx paperclipai run` | env `PAPERCLIP_API` |
| 3737 | **Agentic OS** (Next.js pack) | `LAUNCH_ALL.bat` | ✅ **yes** — pack's start script sets `PORT=3737` |
| 3939 | **M7 Command Center** (`server.js`) | `RUN_AGENT_OS.bat` | env `PORT` |
| 7455/7456 | OpenDesign daemon / web | OpenDesign | ✅ yes |
| 8082 | FCC proxy | `npx fcc-server` | flag |
| 9119 | Hermes dashboard (FastAPI) | Agentic OS auto-spawns | ✅ yes |
| 11434 | Ollama | Ollama service | env `OLLAMA_HOST` |
| 20128/20129 | OmniRoute / 9Router | OmniRoute | ✅ yes |

## ⚠️ The two rules

1. **Never put the Agentic OS on port 3000.** Port 3000 belongs to SEO Office.
   The Agentic OS hardcodes `localhost:3000/office` in `SEOView.tsx` and in
   `api/seooffice/status`. If the Agentic OS sits on 3000 it pings *itself*,
   gets a 404, shows "SEO Office isn't responding", and the iframe embeds the
   Agentic OS inside the Agentic OS.

2. **The Command Center is 3939, not 3737.** The Agentic OS pack claims 3737
   for itself (its own start script hardcodes it), so `server.js` moved to
   3939 to end the collision.

## Where API keys go

Not in the vault `.env` — the Agentic OS reads them from the Hermes profile:

```
~/.hermes/profiles/main/.env      →      OPENROUTER_API_KEY=...
```

One key feeds Hermes, Fusion, Loop and Hy3-Coder. Don't repeat it per-tab.

> ⚠️ **Never create a `.env.local` containing an empty `ANTHROPIC_API_KEY=`.**
> An empty value overrides `claude login` and breaks the Claude tab.
> The Claude tab uses subscription OAuth (`claude login`), not an API key.

## Keep the pack version current

`LAUNCH_ALL.bat` starts the Agentic OS from an explicit dated path:

```
03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-<DATE>/source
```

Currently `agent-os-pack-2026-07-30`. **When you unzip a newer pack, update
that path** — otherwise you keep booting the old build while believing you're
on the new one.
