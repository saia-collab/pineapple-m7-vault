# Hermes Model Router & Orchestrator Configuration

This directory contains the configurations and model routing weights for the Hermes local orchestration engine.

## Model Routing & Orchestration Setup

Hermes acts as the primary task planner and local routing orchestrator, mapping tasks to specialized subagents.

1. **Routing Weights Configuration**:
   - Define model endpoints and provider fallback configurations.
   - Default primary provider: `gemini` (`gemini-3.1-flash-lite-preview`)
   - Default secondary provider: `claude` (`claude-3-5-sonnet`)
   - Fallback routing for complex logical tasks: redirect to Claude.

2. **Integration into Script Paths**:
   - Import Hermes configurations into `04_Tech_Lab/agent_runtime_app.py`.
   - Ensure the local runtime loops query the orchestrator prior to initiating subagent tasks.
   - Run verification via the agent runtime tests:
     ```powershell
     python 04_Tech_Lab/test_agent_runtime_app.py
     ```

3. **Orchestrator Weight Tuning**:
   - Save custom weights mapping under `config/hermes/weights.json` to assign target complexity parameters for GEO validation and copy atomization tasks.
