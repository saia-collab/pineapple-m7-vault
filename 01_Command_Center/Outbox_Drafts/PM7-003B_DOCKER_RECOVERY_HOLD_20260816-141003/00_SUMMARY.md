# PM7-003B Docker Recovery Hold (READ-ONLY inspection)

- Run: 20260816-141003
- C: free now: 53.03 GB
- Trigger: Docker start failed (dockerInference listener/path error); "Factory reset of Docker Desktop completed" dialog observed.
- Overall: DATA PRESERVED ON DISK (volume remount UNVERIFIED - no Docker start performed)

## 1. VHDX inventory (under C:\Users\estim\AppData\Local\Docker)
- docker_data.vhdx : logical 29.18 GB | physical 29.18 GB | created 2026-04-11 22:51:10 | modified 2026-08-16 13:44:32 (= compact time; NOT modified after)
- wsl\main\ext4.vhdx : 0.10 GB (Docker Desktop VM system disk; normal) | modified 2026-08-16 13:41:07
- No .bak/.backup/.old/.tmp VHDX copies found. No second/new data VHDX found.

## 2/3. Original compacted data disk
- STILL EXISTS at C:\Users\estim\AppData\Local\Docker\wsl\disk\docker_data.vhdx, 29.18 GB, unchanged since the compact.
- A completed factory-reset data wipe would have shrunk this file or created a fresh small disk timestamped after 13:44 - neither happened.

## 4. New VHDX after reset?
- NO. Only the same 29.18 GB data disk + the normal small system disk. No fresh/empty data VHDX.

## 5. WSL state (wsl --list --verbose; nothing started)
- Ubuntu: Stopped | docker-desktop: Stopped (both still registered - not deleted)

## 6. Recovery / Compose sources
- open-seo: C:\Users\estim\open-seo\compose.yaml EXISTS (+ Dockerfile.selfhost, drizzle DB migrations) -> open-seo is recreatable from Compose.
- pineapplehq / pineapple-marketing: no local project folder or compose found (folders absent). Definitions recoverable from GitHub repos (PineappleHQ), not locally.
- No .sql / .dump / .tar database backups found in the PM7 vault.

## 7. Resource status
- pineapplehq_pineapple_data (Postgres)   : PRESERVED in original VHDX (unverified until mount)
- pineapplehq_ollama_data (Ollama models) : PRESERVED in original VHDX (unverified until mount)
- pineapple-marketing_postgres_data       : PRESERVED in original VHDX (unverified until mount)
- open-seo_open_seo_data                  : PRESERVED in original VHDX (unverified until mount)
- pineapplehq-db-1 (container)            : definition not local; recreatable (GitHub) - DATA in VHDX
- pineapple-local-worker (container)      : recreatable (ollama/ollama image) - DATA in VHDX
- open-seo-open-seo-1 (container)         : RECOVERABLE from Compose (open-seo\compose.yaml)

## SAFEST NEXT ACTION (recommendation only - not performed)
Before ANY Docker start: COPY (do not move/rename) docker_data.vhdx (29.18 GB) to a separate backup
location while Docker is stopped. This locks the data in even if Docker's next start tries a fresh init.
Only after that backup exists, do a controlled verification-only Docker start to check the volumes remount.
Do not allow Docker to complete a fresh initialization before the backup copy exists.
