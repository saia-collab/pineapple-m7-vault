# Agent Initialization Instruction

## Direct Instruction Block: Initializing Your Agent in the 4‑Fala System

Whenever you start a terminal session with an AI agent (such as Claude Code or Hermes), copy and paste the following command block directly into the console. This completely bypasses human operational error and forces the AI to fix any layout discrepancies immediately:

```bash
claude --commands "Read claw.md first, verify that no legacy M7 folders or loose root files exist, run the self‑correction cleanup block inside claw.md if any layout errors are found, and confirm alignment to the 4‑Fala system."
```

**How this works:**
1. The agent reads `claw.md` at the repository root.
2. It verifies the directory layout and checks for duplicate or legacy files.
3. If any issues are detected, it runs the self‑correction script defined in `claw.md`.
4. Once the workspace is clean, the agent proceeds with the requested command.

---

*Save this file as `01_Command_Center/AGENT_INIT_INSTRUCTION.md`.*
