---
type: research
status: active
date: "2026-04-08"
tags: [pi, openrouter, setup, auth, config]
related:
  - "[[PI]]"
  - "[[OpenRouter]]"
  - "[[PI Harness Architecture for EMAI]]"
  - "[[2026-04-08 – PI Agent Teams Video Breakdown]]"
---

# PI + OpenRouter Local Auth Setup

Source:
- shared setup gist from David Ondrej workflow discussion

## Why this matters

This is the cleanest "first practical step" into [[PI]] for someone who wants:
- model flexibility
- provider control
- no system-wide env var requirement
- local config scoped to [[PI]]

That makes it strategically important because it lowers the barrier between:
- "PI seems interesting"
- and
- "I can actually try this today"

## Claimed setup flow

### 1. Create PI config directory

```bash
mkdir -p ~/.pi/agent
```

### 2. Store OpenRouter auth in `auth.json`

Path:

```bash
~/.pi/agent/auth.json
```

Example:

```json
{
  "openrouter": {
    "type": "api_key",
    "key": "sk-or-your-key-here"
  }
}
```

Claimed behavior:
- [[PI]] reads this before environment variables
- auth stays scoped inside the PI config folder

### 3. Optional macOS Keychain pattern

Store key:

```bash
security add-generic-password -a "openrouter" -s "openrouter" -w "sk-or-your-key-here"
```

Reference from `auth.json`:

```json
{
  "openrouter": {
    "type": "api_key",
    "key": "!security find-generic-password -ws 'openrouter'"
  }
}
```

Claimed behavior:
- `!` prefix executes the command
- command output is used as the key

### 4. Set default provider/model in `settings.json`

Path:

```bash
~/.pi/agent/settings.json
```

Example:

```json
{
  "defaultProvider": "openrouter",
  "defaultModel": "anthropic/claude-sonnet-4"
}
```

Claimed result:
- running `pi` uses [[OpenRouter]] by default
- no provider/model flags needed on every launch

### 5. Launch

```bash
pi
```

## Claimed quick commands

- switch models mid-session: `Ctrl+L` or `/model`
- cycle favorite models: `Ctrl+P`
- change thinking level: `Shift+Tab`
- continue last session: `pi -c`
- browse past sessions: `pi -r`

## Strategic takeaway

This matters less as a "setup tutorial" and more as proof of the broader point:

> the moment you can choose the harness, the provider, and the model independently, you are already less trapped by vendor product decisions.

That is the real value.

## Important note

Treat the exact config keys and behaviors above as **claimed setup details to verify before presenting on camera as fact**.

Specific things to verify:
- config path: `~/.pi/agent/`
- auth file format
- command substitution with `!`
- `defaultProvider`
- `defaultModel`
- shortcuts and session commands

## Best use in content

Use this as:
- the practical bridge from theory to exploration
- "here's how you start"
- not "here's my fully mature PI system"

That keeps the whole thing honest.
