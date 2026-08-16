# PM7 Windows Storage and Installer Audit

- Run: 20260816-124512
- Computer: ESTIMATES
- Windows: Microsoft Windows 11 Home 10.0.26200
- Processor/system: Inspiron 16 7635 2-in-1
- Installed RAM: 15.28 GB
- C: capacity: 455.77 GB
- C: free: 12.49 GB (2.74%)
- Storage status: **CRITICAL_LOW_SPACE**
- Mode: READ-ONLY AUDIT

## Key counts

- OpenAI installer candidates in Downloads: 7
- Agent OS ZIPs in Downloads: 14
- Exact SHA-256 duplicate groups: 2
- Installed desktop app records found: 1
- Installed AppX package records found: 1
- August 14 audited Agent OS pack hash match: 1
- Files sent to Recycle Bin: 0

## Automatic decision boundary

This audit never uninstalls applications, stops services, edits PM7, changes launchers, deletes Agent OS versions, or removes files with different hashes. Cleanup mode can send only exact SHA-256 duplicate installer/ZIP copies from Downloads to the Windows Recycle Bin.

Review the CSV files in this receipt folder before approving any installed-app uninstall, old Agent OS version retirement, Ollama-model removal, Docker cleanup, or PM7 folder migration.
