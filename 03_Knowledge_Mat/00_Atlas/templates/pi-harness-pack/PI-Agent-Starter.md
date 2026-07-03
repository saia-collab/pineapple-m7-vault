This the clean setup of **Pi** on OpenRouter by default

## 0) Install Pi

```bash
npm install -g @mariozechner/pi-coding-agent
```

Check that it installed:

```bash
pi --version
```

### Windows note

Pi needs a **bash shell** on Windows.
For most people, installing **Git for Windows** is enough:
https://git-scm.com/download/win

---

## 1) Create Pi’s config folder

### Mac / Linux

```bash
mkdir -p ~/.pi/agent
```

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME/.pi/agent"
```

On Windows, that usually lives here:

```text
C:\Users\YOUR_NAME\.pi\agent\
```

---

## 2) Add your OpenRouter API key

Pi supports credentials in `auth.json`, and that takes priority over environment variables.
That’s the cleanest move here.

### Mac / Linux

```bash
nano ~/.pi/agent/auth.json
```

### Windows PowerShell

```powershell
notepad $HOME\.pi\agent\auth.json
```

Paste this in:

```json
{
  "openrouter": {
    "type": "api_key",
    "key": "sk-or-your-key-here"
  }
}
```

Get your key here:

https://openrouter.ai/keys

A couple things matter:

- keep `"type": "api_key"`
- keep `"key"`
- do **not** rename it to `apiKey`

---

## 3) Set OpenRouter as the default provider

Now tell Pi to boot into OpenRouter automatically.

### Mac / Linux

```bash
nano ~/.pi/agent/settings.json
```

### Windows PowerShell

```powershell
notepad $HOME\.pi\agent\settings.json
```

Paste this in:

```json
{
  "defaultProvider": "openrouter",
  "defaultModel": "anthropic/claude-sonnet-4"
}
```

That gives you:

- **OpenRouter** as the default provider
- **Claude Sonnet 4** as the default model through OpenRouter

If you want a different model, swap this line:

```json
"defaultModel": "anthropic/claude-sonnet-4"
```

for any OpenRouter-supported model in this format:

```text
author/model-name
```

Browse models here:

https://openrouter.ai/models

---

## 4) Run Pi

### Mac / Linux

```bash
pi
```

### Windows

Start with:

```powershell
pi
```

If PowerShell complains, use:

```powershell
pi.cmd
```

If everything worked, Pi should open using OpenRouter by default.

---

## 5) Windows fallback if Pi can’t find bash

Pi needs bash on Windows.
If Git for Windows is installed and Pi still doesn’t detect it, add `shellPath` to `settings.json`.

Use this:

```json
{
  "defaultProvider": "openrouter",
  "defaultModel": "anthropic/claude-sonnet-4",
  "shellPath": "C:\\Program Files\\Git\\bin\\bash.exe"
}
```

Only do this if Pi isn’t picking up Git Bash automatically.

---

## Useful shortcuts after setup

- switch models: `Ctrl+L` or `/model`
- cycle scoped models: `Ctrl+P`
- change thinking level: `Shift+Tab`
- continue last session: `pi -c`
- browse older sessions: `pi -r`
