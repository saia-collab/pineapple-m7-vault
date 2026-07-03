# Oracle Database Connectivity Config Guidelines

This directory houses the upcoming configuration scripts and database environment mapping keys for the Oracle DB replication pipeline.

## Cloud Database Integration Steps

To link the cloud-hosted postgres/database systems into the core M7 script execution paths, perform the following:

1. **Environment Mapping**: Ensure the workspace root `.env` includes:
   - `DATABASE_URL=postgresql://postgres:[PASSWORD]@[HOST]:5432/pineapple_db`
   - `DB_PASSWORD=[PASSWORD]`
   - `POSTGRES_PASSWORD=[PASSWORD]`

2. **Connection Provisioning**:
   - Use the internal Postgres driver client in Python or Node.js.
   - For scripts in `04_Tech_Lab/`, verify database connectivity via `C:\Pineapple Contractors M7\04_Tech_Lab\airtable.py` or equivalent modules.
   - Run a dry-run test using:
     ```powershell
     python -c "import os, psycopg2; psycopg2.connect(os.getenv('DATABASE_URL'))"
     ```

3. **Replication Guardrails**:
   - Outbound writes must comply with security filters (masking PII customer info).
   - Only sync verified lead contracts matching the premium portfolio threshold ($18,000+).
