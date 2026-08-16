# PM7-002 Storage Triage (READ-ONLY)

- Run: 20260816-125807
- C: free: 12.69 GB of 455.77 GB (2.78 %)
- Docker VHDX total on disk: 68.72 GB
- Downloads total: 33.62 GB

## Docker system df (summary)
```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          8         4         15.97GB   2.186GB (13%)
Containers      4         4         49.27MB   0B (0%)
Local Volumes   5         3         11.05GB   73.71MB (0%)
Build Cache     0         0         0B        0B
```

## Docker VHDX files
- 68.63 GB  C:\Users\estim\AppData\Local\Docker\wsl\disk\docker_data.vhdx
- 0.09 GB  C:\Users\estim\AppData\Local\Docker\wsl\main\ext4.vhdx

## WSL distros
```
  NAME              STATE           VERSION
* Ubuntu            Stopped         2
  docker-desktop    Running         2
```

## PM7 / Local Studio / Hermes / Agent OS linkage
- Image: mcp/playwright:<none>  [1.43GB]
- Image: ollama/ollama:latest  [10.1GB]
- Image: mcp/brave-search:<none>  [294MB]
- Image: mcp/google-maps-comprehensive:<none>  [252MB]
- Image: mcp/obsidian:<none>  [215MB]
- Container: pineapplehq-db-1  [20.5kB (virtual 469MB)]
- Container: pineapple-local-worker  [16.4kB (virtual 6.31GB)]
- Volume: pineapple-marketing_postgres_data  [(see df -v)]
- Volume: pineapplehq_ollama_data  [(see df -v)]
- Volume: pineapplehq_pineapple_data  [(see df -v)]

Containers mounting a PM7-related host path:
- /pineapplehq-db-1|postgres:15|/var/lib/docker/volumes/pineapplehq_pineapple_data/_data;
- /pineapple-local-worker|ollama/ollama:latest|/var/lib/docker/volumes/pineapplehq_ollama_data/_data;

## Top 10 Downloads items
- 4.476 GB  [Folder]  agent-os-pack-extracted
- 1.406 GB  [File]  OneDrive_2023-08-24.zip
- 1.012 GB  [File]  Ant - Reels-20260325T160923Z-1-001.zip
- 0.995 GB  [File]  Ulta _94 - The Shops at North East Mall - Hurst, TX.zip
- 0.751 GB  [File]  QbkkykEtCOWx_1697463095.zip
- 0.692 GB  [File]  Duwest Retail.zip
- 0.681 GB  [File]  PLANO ISD_WILLIAMS HIGH SCHOOL ___INVITATION TO BID___.zip
- 0.619 GB  [File]  CROWLEY ISD - CROWLEY ES _17  - CMAR BID.zip
- 0.579 GB  [File]  BidFiles_1702410507798.zip
- 0.55 GB  [File]  Melissa ISD Middle School _2 - 100_ CD_s.zip

---

# THREE RANKED CLEANUP OPTIONS (proposal only — no changes made)

## 🥇 Option A — Compact the Docker virtual disk (RECOVER EMPTY SPACE, NOT DATA)
- **What is affected:** `docker_data.vhdx` is 68.6 GB on disk but only ~27 GB is actually used inside (Images 15.97 GB + Volumes 11.05 GB). ~40 GB is trapped EMPTY space. Compacting shrinks the file; it deletes NO containers, images, or volumes.
- **Estimated space recovered:** ~40 GB.
- **Risk level:** LOW. Nothing is deleted. Requires a brief Docker restart (or an Administrator compact).
- **PM7 / Agent OS affected?** NO. The Pineapple DB + Ollama containers/volumes are preserved and restart automatically.
- **Human approval required?** YES — because Docker restarts briefly (this session is not Administrator, so it is a Docker Desktop restart, not a forced compact).

## 🥈 Option B — Delete regenerable installers + the redundant extracted pack (Downloads)
- **What is affected:** Re-downloadable app installers in Downloads (OllamaSetup, LM-Studio, Chrome, Dropbox, 6× ChatGPT Installer, Codex, Manus, VSCode, Git, Acrobat, Antigravity IDE, etc.) + the `agent-os-pack-extracted` folder (4.48 GB, redundant because the Studio is already installed in the vault) + optionally `OneDrive_2023-08-24.zip` (1.4 GB, old backup).
- **Estimated space recovered:** ~10–12 GB.
- **Risk level:** LOW. Installers re-download anytime; the extracted pack is a duplicate of the installed Studio. (Verify the OneDrive backup zip is not needed first.)
- **PM7 / Agent OS affected?** NO. The small `agent-os-pack-*.zip` files stay; only the redundant EXTRACTED copy is removed. The installed Agent OS in the vault is untouched.
- **Human approval required?** YES — deletion is a human action (the agent does not hard-delete).

## 🥉 Option C — Archive the construction-bid library to Google Drive (biggest Downloads reclaim)
- **What is affected:** Hundreds of construction estimating records in Downloads (ISD bid sets, Tesla/car-wash/retail plan sets, insurance-claim PDFs, EagleView/ITEL reports) — roughly ~15–20 GB of the 33.62 GB. These are REAL BUSINESS RECORDS, not junk.
- **Estimated space recovered:** ~15–20 GB.
- **Risk level:** MEDIUM — only because they must be MOVED to Google Drive first and sync-verified, then deleted locally. Never delete in place.
- **PM7 / Agent OS affected?** NO.
- **Human approval required?** YES + your judgment on which records to archive vs keep. This is the estimating business's data.

## ⛔ Docker resources that must NOT be touched (PM7-connected, active)
- Container `pineapplehq-db-1` (postgres:15) → volume `pineapplehq_pineapple_data`
- Container `pineapple-local-worker` (ollama/ollama) → volume `pineapplehq_ollama_data`
- Volume `pineapple-marketing_postgres_data`; image `ollama/ollama:latest` (in use)
- (Active tool) `open-seo` container/image/volume — the SEO pipeline; retire only on your call.

Deleting any of these would destroy Pineapple database or Ollama data. None are proposed for removal.
