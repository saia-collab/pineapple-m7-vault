# workspace/ — generated state

This directory is empty by design.

On first use, run the setup gate to create `config.json` and `INDEX.md`:

```bash
python3 scripts/setup.py
```

Setup will:
- Ask which provider to use (Kie / FAL / both / prompt-only)
- Walk through API key entry (saved to `~/.shot-builder/.env` or `workspace/.env` — your choice)
- Set defaults for model, resolution, aspect, workflow mode, and output directory

After setup, create a project:

```bash
python3 scripts/project.py new "<project-name>" --switch
```

See `../SKILL.md` for the full workflow.
