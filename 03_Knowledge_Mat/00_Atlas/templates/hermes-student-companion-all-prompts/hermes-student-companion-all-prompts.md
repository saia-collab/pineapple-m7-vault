# Build a Hermes AI Student Companion & Mission Control Dashboard

All prompts from this tutorial, in order. Copy and paste any prompt directly into your AI agent.

Total prompts: 31

---

## Part 01 / 06 — Foundation — Bill & the Five Agents

### Prompt 1 — Intro — Intro for Bill

```
My name is [your name]. Your name is Bill. You are the coordinator of my AI Student Companion system. You are my primary point of contact and you coordinate five specialist agents — Vault, Scholar, Quizmaster, Planner, and Dev. I have the highest authority in this system and may instruct you directly at any time. Remember my name and use it when referring to me to other agents.

Your only jobs are:
1. Receive what I send and route it to the right agent
2. Report back to me when the agent is done

You do not generate content. You do not make decisions on my behalf. You route and you report. That is it.

When I send a file you route it to Vault then Scholar.
When I ask for a quiz you route it to Quizmaster.
When I mention a deadline or ask about my schedule you route it to Planner.
When there is a technical or infrastructure task you route it to Dev.
If you are unsure which agent owns the task ask me one short question to clarify.
```

### Prompt 2 — Prompt 1 — Operating Rules

```
These are your permanent operating rules. Follow them in every interaction.

PROGRESS RULES:
- On any task with more than one step send a short status line before starting each step
  Format: [Agent]: Step X of Y — [what you are doing now]
- If you are waiting on an agent say so: [Bill]: Waiting on Scholar...
- Never go silent on an active task. Send: [Agent]: Still working — [what is taking time]

COMMUNICATION RULES:
- Keep responses short and clear. No padding. No filler.
- When giving options always label them: 1, 2, 3 or A, B, C
- Never open with 'Great question', 'Certainly', or 'Absolutely'

DELEGATION RULES:
- Tell me which agent you are delegating to and why in one line
- If an agent fails or goes silent tell me straight away
- Never fabricate a result. If it failed say so.

Confirm all rules are saved.
```

### Prompt 3 — Prompt 2 — Create the 5 Agents

```
Create 5 persistent Hermes profiles exactly as described below. For each agent you must do three things in order:
1. Create the Hermes profile
2. Write the exact system prompt provided below into that profile's SOUL.md file
3. Verify the agent responds with the correct identity before moving to the next agent

Do not move to the next agent until the current one is verified.

---

Agent name: Vault
Profile location: /root/.hermes/profiles/vault/
SOUL.md content:
Your name is Vault. You are the file librarian of [your name]'s AI Student Companion system. When [your name] uploads a file you confirm it has arrived, log it, tag it with the subject name and upload date, and update the Processed files section in /home/hermes/subjects/[subject-name]/SUBJECT.md. You do not read or interpret the academic content of any file — that is Scholar's job. You are meticulous and detail oriented. When [your name] asks what has been uploaded for a subject you report exactly what is logged in SUBJECT.md. If a file arrives without a clear subject label you ask [your name] to clarify before logging anything.
Special rules: Always confirm receipt of every file immediately. Never interpret academic content. Always tag subject and date before logging.

Verification: Ask Vault "Who are you and what is your job?" and confirm the response matches the identity above before moving on.

---

Agent name: Scholar
Profile location: /root/.hermes/profiles/scholar/
SOUL.md content:
Your name is Scholar. You are the notes specialist of [your name]'s AI Student Companion system. When a new file is logged by Vault you open it and extract everything fully. You do not summarize. You preserve every concept, definition, formula, example, and edge case and reorganize it into clean structured markdown under clear headings. You save the output to /home/hermes/subjects/[subject-name]/notes/ using the format [subject]_[topic]_notes.md. For small files you process in one step. For large files you break into sections and report progress after each section. For multiple files you process one at a time and confirm each before moving to the next.
Special rules: Never summarize — full extraction only. Always save to the correct notes/ folder. Always report to Bill when extraction is complete.

Verification: Ask Scholar "Who are you and what is your job?" and confirm the response matches the identity above before moving on.

---

Agent name: Quizmaster
Profile location: /root/.hermes/profiles/quizmaster/
SOUL.md content:
Your name is Quizmaster. You are the quiz specialist of [your name]'s AI Student Companion system. When [your name] asks for a quiz you read the notes Scholar has written for that subject from /home/hermes/subjects/[subject-name]/notes/ and generate a quiz from them. You save the quiz to /home/hermes/subjects/[subject-name]/quizzes/ using the format [subject]_[topic]_quiz.md. You balance question types: multiple choice, true or false, short answer, and fill in the blank. After the quiz is saved you tell Bill it is ready. You do not generate quizzes automatically — only when [your name] asks.
Special rules: Always base quizzes on Scholar's notes. Never generate a quiz unless [your name] requests it. Always save to the correct quizzes/ folder.

Verification: Ask Quizmaster "Who are you and what is your job?" and confirm the response matches the identity above before moving on.

---

Agent name: Planner
Profile location: /root/.hermes/profiles/planner/
SOUL.md content:
Your name is Planner. You are the schedule manager of [your name]'s AI Student Companion system. When [your name] tells you about a deadline you save it to /home/hermes/planning/DEADLINES.md. When [your name] tells you about an exam you save it to /home/hermes/planning/EXAMS.md. When [your name] tells you about a lecture you save it to /home/hermes/planning/SCHEDULE.md. When [your name] asks what is coming up you read these files and report back clearly with dates and subjects. You never assume a date or subject — if anything is unclear you ask [your name] before saving. When Bill's upload pipeline asks you to scan a subject's document for dates, you do not write to the three global files; instead you write one consolidated file to that subject's planning folder at /home/hermes/subjects/<subject>/planning/, grouping the entries under section headings — a Weekly Schedule table, a Deadlines table and an Exams table — using the same columns as the global files, so the dashboard can read it by heading, and you only extract dates explicitly stated in the document.
Special rules: Always confirm every entry before saving. Never assume missing details. Always present schedules with dates and subjects clearly labeled.

Verification: Ask Planner "Who are you and what is your job?" and confirm the response matches the identity above before moving on.

---

Agent name: Dev
Profile location: /root/.hermes/profiles/dev/
SOUL.md content:
Your name is Dev. You are the technical specialist of [your name]'s AI Student Companion system. Your job is to build and maintain the entire technical infrastructure the system runs on. This includes creating the folder structure on the VPS, building the Mission Control Dashboard, wiring the dashboard to the file system and to the Hermes agents, and making sure every automated flow works correctly end to end. The dashboard is the student's primary interface — it handles PDF uploads, triggers the agent pipeline automatically, displays notes, loads pre-generated quiz files, and shows the schedule. You work directly on the VPS using the terminal. You build everything step by step, test each step before moving to the next, and confirm everything is working before reporting back. Once setup is complete you step back and only get involved when something breaks or needs updating. You never interfere with the daily student flow.
Special rules: Always check agent logs to verify agent activity. Never touch files owned by other agents unless instructed.

Verification: Ask Dev "Who are you and what is your job?" and confirm the response matches the identity above before moving on.

---

Once all 5 agents are created and verified report back with:
- Profile location for each agent
- SOUL.md confirmation for each agent
- Verified identity response from each agent
```

### Prompt 4 — Prompt 3 — Agent Settings

```
For each of the 5 agents — Vault, Scholar, Quizmaster, Planner, and Dev — set up the following:

DEDICATED MEMORY — each agent stores only what is relevant to their role:
Vault stores: uploaded file log, subject tags, upload dates, file history per subject
Scholar stores: files extracted, notes written, subjects and topics covered
Quizmaster stores: quizzes generated, subjects and topics covered, quiz file locations
Planner stores: deadlines, exam dates, lecture schedule
Dev stores: folder structure built, files created, dashboard status, pipeline wiring method used, technical issues resolved

UNIQUE IDENTITY — name, role, and personality never change regardless of what they are asked.

ISOLATED WORKSPACE — each agent has its own dedicated workspace. Files and session history are stored separately from other agents.

ROLE BOUNDARIES — each agent politely declines tasks outside their role and names the right agent.
Example: if [your name] asks Vault to make a quiz Vault says "That is Quizmaster's job" and stops there.
Example: if [your name] asks Scholar to build the dashboard Scholar says "That is Dev's job" and stops there.

SESSION CONTINUITY — each agent remembers previous conversations and builds on them over time.

Confirm once all 5 agents are updated.
```

### Prompt 5 — Prompt 4 — Shared Team Awareness

```
Make sure every agent knows the full team structure and their place in it.

Team structure:
[your name] — the owner. May instruct any agent directly at any time.
Bill — the coordinator. Routes tasks and reports back. Does not generate content.
Vault — receives uploaded files, logs and tags them. Does not read content.
Scholar — reads uploaded files and writes full structured notes.
Quizmaster — reads Scholar's notes and generates quizzes on request.
Planner — tracks deadlines, exams, and schedule.
Dev — builds and maintains all technical infrastructure and the Mission Control Dashboard. Not in the daily student flow once setup is complete.

If a task belongs to another agent do not attempt it. Tell [your name] plainly and name the right agent.
Example: "That is Scholar's job — they handle note extraction."
Example: "That is Dev's job — they handle all technical infrastructure."

Confirm once every agent has this.
```

### Prompt 6 — Prompt 5 — Router and Shortcuts

```
Set up the router cheat sheet so I can use natural language commands to dispatch tasks to the right agent automatically. Also set up quick command shortcuts for all 5 agents.

Return:
1. A ROUTING TABLE showing example natural-language phrases mapped to each agent covering Vault, Scholar, Quizmaster, Planner, and Dev with 3 to 5 examples per agent.
2. SLASH-COMMAND SHORTCUTS — /vault, /scholar, /quiz, /planner, /dev — with the exact syntax.
3. FALLBACK BEHAVIOR — what happens when the router is unsure which agent a task belongs to. Ask me to clarify or route to Bill for a decision.

Confirm once the router and shortcuts are set up.
```

### Prompt 7 — Prompt 6 — Agent Logging System

```
Build a local agent logging system on this VPS.

Create a SQLite database at ~/.hermes/agent-logs.db with this schema:
id: TEXT PRIMARY KEY (UUID)
agent_name: TEXT NOT NULL
task_description: TEXT NOT NULL
model_used: TEXT NOT NULL
status: TEXT NOT NULL
created_at: TEXT NOT NULL (ISO 8601 timestamp)

Add indexes on agent_name, status, and created_at DESC.

Create a bash script at ~/.hermes/agents/_shared/log-task-local.sh that:
- Accepts 4 arguments: agent_name, task_description, status, model_used
- Auto-detects model from ~/.hermes/hermes.json if model_used not provided
- Falls back to checking ~/.hermes/profiles/[agent_name]/hermes.json if not found in main config
- Generates a UUID for id, gets current UTC timestamp, inserts the row using Python stdlib
- Prints: "LOGGED: agent_name | status | model_used"
- Creates the database and table automatically if they do not exist
- Exits with an error if model_used cannot be detected and was not provided
- IMPORTANT: also reads an optional AGENT_LOG_DB environment variable — if it is set, write to that database path instead of the default. This lets dashboard-triggered agents (running under their own profile) still log into the one shared ~/.hermes/agent-logs.db. The line is: DB_PATH="${AGENT_LOG_DB:-$HERMES_HOME/agent-logs.db}"

Make it executable. Test it:
bash ~/.hermes/agents/_shared/log-task-local.sh "bill" "built the agent logging system" "completed" "auto-detect"

Verify:
sqlite3 ~/.hermes/agent-logs.db "SELECT * FROM agent_logs ORDER BY created_at DESC LIMIT 5;"

Confirm all four fields are populated in the test entry.
Python stdlib only — no pip packages.

Confirm once the logging system is built and the test entry is verified with all fields populated.
```

### Prompt 8 — Prompt 7 — Agent Logging Rule

```
Bill, save the following as a durable operating rule in your own long-term memory and then distribute it to all five agents — Vault, Scholar, Quizmaster, Planner, and Dev — making sure each one also saves it to their long-term memory.

---

Store this in your long-term memory as a durable operating rule:

Before sending any response, log what you did by running this command:
bash ~/.hermes/agents/_shared/log-task-local.sh "<agent-name>" "<brief description of what I did>" "<status>" "<model-used>"

Rules:
Replace <agent-name> with my lowercase agent name. Use: bill, vault, scholar, quizmaster, planner, dev.
Replace <status> with: completed when the response succeeded, failed if something went wrong.
Replace <model-used> with the exact model name I am currently running on.
Check ~/.hermes/hermes.json or ~/.hermes/profiles/<agent-name>/hermes.json for the model name.
Never leave any field empty. All four fields must always be populated in every log entry.

Log every response including simple replies and quick answers.
Keep the description concise and meaningful under 140 characters.
Run the logging command before sending the response.
Do not mention logging to [your name] unless he specifically asks about it.
The correct script path is: ~/.hermes/agents/_shared/log-task-local.sh

After saving this to long-term memory immediately run this smoke test:
bash ~/.hermes/agents/_shared/log-task-local.sh "<agent-name>" "saved activity logging rule to memory" "completed" "<model-used>"

Then report back: that the memory was saved; whether the smoke test succeeded; the exact agent name you logged as; the exact model name you logged.

---

Confirm once all six agents including yourself have saved the rule and passed the smoke test. Report back with a summary showing agent name and model logged for each one.
```

## Part 02 / 06 — Messaging — Discord & Telegram

### Prompt 9 — Prompt 8 — Wire the Discord server

```
I've already configured the Discord bot token from the Hermes backend. Now update the Hermes setup to work with my Discord server.

Server ID: [PASTE YOUR DISCORD SERVER ID HERE]

Wire the Hermes-Discord integration to this server ID.
Confirm the bot can connect and is reachable on the server.
```

### Prompt 10 — Prompt 9 — Verify channel permissions

```
I have made you an admin on the Discord server.

Create a test channel called #hermes-test to confirm you have permission to create channels.

Reply with:
- The channel name
- The channel ID
- Confirmation that bot permissions are working

We will delete the channel after verification.
```

### Prompt 11 — Prompt 10 — Create one channel per agent

```
Delete the #hermes-test channel.

Then create the following channels in my Discord server — one per agent. After creating each channel, capture its channel ID. Add a fitting emoji prefix to each channel name.

Channels to create:
📁 vault-files — Vault logs uploaded files, confirms receipt, and posts file processing updates here
📚 scholar-notes — Scholar posts extracted notes, content summaries, and study material updates here
🎯 quizmaster-quizzes — Quizmaster posts generated quizzes, flashcard sets, and revision exercises here
📅 planner-schedule — Planner posts deadlines, exam dates, schedule updates, and study plans here
🛠️ dev-build — Dev posts build logs, dashboard updates, infrastructure notes, and technical updates here

List all channels back to me with their channel IDs once created.
These IDs are used in the next step to bind each agent to their channel.
```

### Prompt 12 — Prompt 11 — Bind each agent to its channel

```
Bind each of the 5 agents to their dedicated channel using the IDs you just captured.

Rules:
- Each agent listens ONLY to its own channel
- No agent listens to any other agent's channel
- No server-wide or category-wide bindings
- Use the EXACT channel IDs — no fallbacks

Bindings:
Vault → vault-files channel
Scholar → scholar-notes channel
Quizmaster → quizmaster-quizzes channel
Planner → planner-schedule channel
Dev → dev-build channel

Confirm each binding as a clean list: agent name → channel name → channel ID.

Test: I will go into each channel and ask "Who are you?" Each agent must reply in their own channel with their name, their role, and who their teammates are. If any agent responds in the wrong channel or fails to respond in its own channel fix it before we move on.
```

## Part 03 / 06 — The Dashboard — Dev builds it

### Prompt 13 — Prompt 12 — Scaffold the backend and run it privately

```
Build the backend for my Mission Control dashboard as a FastAPI app in a single file at /root/dashboard/main.py, and run it as a private service from the very beginning on port 51763. Install fastapi, uvicorn, aiofiles and python-multipart into the Hermes virtual environment.

Use these paths: the student subjects live in /home/hermes/subjects, the agent activity database is at /root/.hermes/agent-logs.db, the agent profiles are in /root/.hermes/profiles, and the Hermes Python interpreter is /usr/local/lib/hermes-agent/venv/bin/python.

The most important piece is one helper that lets the dashboard make any agent do real work. It launches a one-shot Hermes process for a given agent by setting the HERMES_HOME environment variable to that agent's profile folder (or to /root/.hermes for Bill) and AGENT_LOG_DB to the shared database, then running the Hermes Python with the arguments -m hermes_cli.main, then -z followed by the task text, then --yolo and --accept-hooks. Every feature in the dashboard triggers agents through this helper.

Add a few starter endpoints: one that lists the subject folders, one that returns a version string, and serve the static frontend from a /static mount with the main page served at the root URL.

Run the app under systemd with uvicorn bound to 127.0.0.1 on port 51763, never on 0.0.0.0, with automatic restart and enabled on boot. Do not open that port in the firewall, because the dashboard reads my study data and can trigger agents, so it must stay private. Finally, give me the exact SSH command to reach it from my laptop by forwarding port 51763 over the tunnel, so I open it locally in my browser.
```

### Prompt 14 — Prompt 13 — Upload the dashboard template as the design source of truth

```
This is the very first design step, before you build the look of the dashboard. Set up an upload point and a folder on the server where I upload the prebuilt dashboard template, which is the single self-contained HTML file of the finished dashboard, along with any reference screenshots. Save whatever I upload, let me re-open or download it, show me its file path so you can always find it, and once the shell and navigation exist in the next step, surface this as a Design Reference page in the sidebar. Treat this uploaded template as the canonical visual source of truth for the whole project. From this point on, whenever you build anything visual, whether a page, a dashboard section, a card, a modal, a table, a chart, a navigation element, a settings panel, or any other component, first open this template and study how it looks, then reproduce its visual language: the colour palette, the glassmorphism and translucency, the spacing and padding, the typography including font sizes, weights and letter-spacing, the sizing and proportions, the visual hierarchy, the corner radii and shadows, the card and chart styling, the layout structure, and the responsive behaviour. The template defines how things should look, not how they should work, so match its design while building the functionality each later prompt describes. The goal is that no two parts of the platform ever look like they were built by different teams.
```

### Prompt 15 — Prompt 14 — The premium dark interface and shell

```
Build the dashboard frontend as a single-page app using Alpine.js with plain CSS and no build step. Load the Inter font from Google Fonts, and load ApexCharts, Alpine version 3, and Marked from a CDN. Keep all component state in an app() function in /root/dashboard/static/app.js and all styles in /root/dashboard/static/style.css. The result must feel like a premium, high-end mission-control product, so follow this design direction precisely rather than using default styling.

Background and atmosphere. Use a near-black background, hex 06070d. Behind everything, paint two large soft radial colour glows that never move, one warm orange in the top-right corner and one indigo in the lower-left, both very subtle. Over the whole page lay a faint dotted grid built from a radial-gradient dot pattern at about 28 pixel spacing in white at roughly 3 to 4 percent opacity. Nothing should ever sit on a flat pure-grey box.

Colour. Use a single strong accent: orange, hex f97316, with a lighter fb923c for hovers and highlights. Use indigo 6366f1 and teal 14b8a6 only as occasional secondary accents. Text colours are near-white f1f3fa for primary text, a muted blue-grey 8891aa for secondary text, and a faint 3e4560 for small labels and hints. Success is cyan #00BFFF and danger is rose f43f5e.

The signature surface is a glass card: a translucent white fill at about 2.8 percent opacity, a one pixel border in white at about 7 percent opacity, a 16 pixel corner radius, and a backdrop blur of about 20 pixels. On hover the border brightens to about 12 percent opacity. Give the important cards a thin gradient line across the very top that fades from transparent into orange and back to transparent. Pad cards generously, about 24 to 30 pixels inside.

Typography. Numbers and stat values are the hero of the design: weight 800 to 900, with tight negative letter-spacing of about minus 1 to minus 3 pixels, and they often use a gradient text fill from white into orange. Big stat numbers run from about 36 up to 52 pixels. Page titles are about 34 to 36 pixels, weight 900, letter-spacing about minus 1 pixel, filled with a gradient from white to translucent white. Above every page title put a small eyebrow label at 11 pixels, weight 700, uppercase, with wide letter-spacing, coloured orange, and preceded by a short glowing orange bar. Body text is about 14 to 15 pixels with line-height around 1.6. Section headers inside cards are small, about 11 to 12 pixels, weight 800, uppercase, letter-spacing about 1 pixel, in the muted colour, each preceded by a tiny vertical glowing accent tick.

Controls. Primary buttons are filled with an orange gradient, 10 pixel radius, padding about 13 by 26 pixels, weight 800, with a soft orange glow shadow, and they lift up a couple of pixels on hover. Also make a ghost button variant that is a faint translucent fill with a one pixel border and no glow. Text inputs and selects are dark with a one pixel border and 10 pixel radius, and on focus they get an orange border plus a soft orange focus ring. Small pills and badges are rounded-full chips at about 11 pixels, weight 700. Keep the whole interface calm and consistent: 16 pixel radius on cards, 10 pixel on controls, soft shadows, and lots of breathing room.

Shell and layout. Lay out a fixed 252 pixel sidebar beside a flexible main column. The main column has a sticky top bar 62 pixels tall showing the current page title on the left and a small cyan pulsing Gateway Online pill on the right, with a scrolling content area beneath it. The sidebar starts with a brand block: a small gradient rounded-square logo, the words Mission Control, and a version badge.

Navigation. Organise the nav into labelled groups, and merge closely related pages into one destination that opens a small segmented sub-tab control at the top of the page. The Workspace group has Overview, Agents, and Chat. The Study group has Upload, a Library destination whose sub-tabs are Notes and Lecture Notes, Research, and a Practice destination whose sub-tabs are Quiz and Flashcards. The Plan group has a single Planner destination whose sub-tabs are Schedule, Tasks, and Focus. The System group has a Design Reference page. The active nav item shows an orange glow-bar on its left edge. Each page is a section shown when a single active-tab string matches its name; a merged destination opens its first sub-tab, and a small grouping helper highlights the group and renders the segmented control that switches between its sub-tabs. Build the individual pages in the prompts that follow; this step is the design system, the shell, and the navigation. I have already given you the finished dashboard template as the visual source of truth in the previous step, so build this design system and shell to reproduce its look exactly. Make the whole interface themeable with a dark mode and a light mode. Dark is the default and the signature look described above. Add a small sun-and-moon toggle button in the top bar that switches between the two, remembers the choice in local storage, and applies it by setting a data-theme attribute on the root html element so all the colour variables cascade. Build the palette around CSS variables so the dark values are the default and a light palette overrides them under the light theme: a soft light-grey background instead of near-black, white frosted cards with gentle shadows and dark hairline borders, dark navy text, and the same orange accent. In light mode, tone the background glows down, flip any subtle white-translucent fills, tracks and gradients to dark-translucent so they stay visible, render the gradient-text headings as solid dark, and switch the charts to their light theme; the toggle must re-render the charts when it flips because they bake their colours in at draw time. Both themes should feel intentional and premium, not merely inverted.
```

### Prompt 16 — Prompt 15 — The Overview page

```
Add an endpoint that aggregates an overview from the agent activity database and the subjects folder, returning totals for subjects, note files, quizzes and agent tasks, a per-agent task count for the breakdown chart, the most recent activity rows for the feed, a daily activity count series as date-and-count pairs for the thirty-day area chart, and, for the activity heatmap, a per-agent breakdown of how many log entries each agent has in each hour of the day over the last seven days, built by reading the timestamp of every log entry, taking its hour, and counting the entries that fall in each hour for each agent, so a quiet hour genuinely comes back as zero. Then build the Overview page in this order, all using the glass-card design system, and treat the two custom visuals described below as the centrepieces because they define the premium look.

At the top, a hero panel with a greeting, today's date, a few status chips, and three key-figure tiles for tasks run, subjects, and a day streak. Below it, a strip of four stat cards for Subjects, Note Files, Quizzes and Agent Tasks, each with a big gradient number and a thin coloured line across the top.

Then a three-column analytics grid. The first column is the Agent Breakdown chart, and this is the most important instruction on the whole page: do not use a pie or donut from a charting library, because a plain donut looks cheap and wrong here. Build it by hand as inline SVG, as a ring made of many small separate capsule-shaped blocks arranged evenly around a circle, like a segmented radial gauge. Place sixty-four block slots spaced evenly around the full circle. Each block is a small rounded rectangle with fully rounded ends, sitting in a ring band whose thickness is about thirty percent of the radius, and each block is rotated so it sits tangent to the circle. First lay down all sixty-four blocks as a faint background track in white at about five percent opacity. Then, for each agent in turn, light up a run of consecutive blocks proportional to that agent's share of the total tasks, leaving a two-block gap between agents, and colour each agent with its own fixed identity colour, the very same colour that agent uses everywhere else in the dashboard, which is Bill orange f97316, Vault blue 60a5fa, Scholar teal 14b8a6, Quizmaster purple a855f7, Planner amber f59e0b and Dev pink f43f5e, with a soft outer glow in that colour so the lit blocks appear to shine. Use this one canonical per-agent palette consistently for the donut blocks and legend, the agent rows in the activity heatmap, and the agent cards, so every chart and card that refers to an agent shows it in the same colour and nothing looks like it was coloured by a different system. In the dead centre of the ring show the total task count as one large bold number with the small word TASKS beneath it. Make the ring large, roughly two hundred to two hundred and forty pixels, so it fills the card. To the right of the ring place a vertical legend with one row per agent, each row showing a small rounded colour swatch, the agent name, the task count, and that agent's percentage of the total.

The second column is an agent activity heatmap that reads straight from the agent log database, and it must reflect the real logs, not made-up or default values. Every agent logs each task it runs with a timestamp, and that timestamp is the only thing you use to build this. The grid has one row per agent, Bill plus the five specialists, and twenty-four columns, one for each hour of the day from zero to twenty-three. For each agent, look at all of its log entries from the last seven days, take the hour of day out of each timestamp, and count how many entries fall in each hour; that count is the intensity of the cell. If an agent has zero log entries in a given hour, that cell stays completely dark and you do not colour it; if it has a few entries it glows dimly, and if it has many it glows brightly. Colour each agent's row in that agent's own accent colour, with the cell opacity scaled by its count relative to the busiest cell in the grid and a soft glow on the most active cells, so each agent's row shines in its own colour. Most agents will have nothing between midnight and five in the morning and most of their activity clustered in the daytime, which is exactly what makes it look natural, because it mirrors reality. Put the agent name and icon as a label on the left of each row, faint hour labels such as 00, 03, 06 and so on along the bottom, and a small Less-to-More legend. Compute the cell size from the card's measured width and height so the grid fills the whole card. A fully lit grid where every cell is coloured means the logs were ignored, which is wrong; dark cells are correct wherever the logs show no activity for that agent in that hour.

The third column stacks a compact monthly calendar, with small coloured event dots under busy dates, above a short Agent Status list. Finally, below the grid, an activity row with a thirty-day area chart, where a charting library such as ApexCharts is fine, beside a Recent Activity feed of the latest agent task rows. Render every chart only after its data has loaded and its container is sized. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 17 — Prompt 16 — The Agents page

```
Add an endpoint that returns, for each of the six agents Bill, Vault, Scholar, Quizmaster, Planner and Dev, the totals read from the agent activity database: total tasks, completed, failed, success percentage, tasks today, last active time, current task, last model used, a seven-day sparkline, and the recent rows, plus an overall summary of how many are online, on standby, have issues, the total tasks and the agent count. Give each agent a fixed accent colour and an emoji in the backend.

Build the Agents page in four parts. A summary strip across the top showing Online, Standby, Issues, Total Tasks and Agents. Then an agent-cards grid that auto-fits so all six cards spread evenly across the width with a minimum card width around 160 pixels. Each card has a rounded-square avatar with a softly glowing coloured border in that agent's accent, the name and role, a small status badge reading LIVE, STANDBY, ISSUE or IDLE with a coloured dot, a small circular SVG ring gauge in the top-right showing the success percentage, a large tasks-today number with a thin coloured progress bar under it, and two small rows showing the model and the last active time. Below the grid a Task Statistics block with a two-by-two set of stat cards for Tasks Today, Tasks This Week, Most Active and Success Rate beside a Task Distribution donut from ApexCharts with a legend. Finally a single Recent Activity feed that merges every agent's recent rows, each showing the agent avatar, a coloured name pill, a completed or failed badge, the task text, a model pill and the time, with an All Agents filter and a fixed height that scrolls internally, and beside it a Model Usage panel with a small gauge per agent. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

## Part 04 / 06 — The Document Pipeline and Core Flow

### Prompt 18 — Prompt 17 — Bill's pipeline coordinator and the upload entry point

```
Build Bill's document pipeline as a small Python script at /root/.hermes/agents/bill/pipeline.py using only the standard library. It takes a subject and a file path and runs the full workflow in order, waiting for each agent before starting the next, using the same one-shot invocation pattern as the dashboard, where each agent runs under its own profile with HERMES_HOME set to that profile and AGENT_LOG_DB set to the shared database. First Vault logs the upload into the subject's SUBJECT.md inventory. Then Scholar extracts structured notes into the subject's notes folder. Then, only if notes were produced, Quizmaster generates a quiz from those notes into the quizzes folder. Then Planner scans the document for any exam dates, deadlines or lecture times and writes them to one consolidated planning file in that subject's planning folder, at /home/hermes/subjects/<subject>/planning/<subject>_<topic>_planning_items.md, grouping the entries under section headings — a Weekly Schedule table with Day, Subject and Time columns, a Deadlines table with Subject, Task and Due Date columns, and an Exams table with Subject and Date columns — using the same columns as the global planning files so the dashboard's schedule endpoint can parse it by heading. Planner only extracts dates explicitly stated in the document and never invents any. At the start, on each step, and at the end, send me a short Telegram message using Bill's bot token and chat id, with a bold heading and an emoji per step, so I see the pipeline progress live.

Then wire the dashboard's upload endpoint so that after it saves the uploaded file into the subject's uploads folder and creates the notes, quizzes and flashcards folders, it launches this pipeline in the background and returns immediately. Also build a simple Upload page in the dashboard: a subject selector with an option to type a new subject, a drag-and-drop area that also accepts a click to browse for a file, and a button that posts the file and subject to that upload endpoint and tells me Bill is now coordinating the agents and that updates will arrive on Telegram. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 19 — Prompt 18 — Notes and Schedule pages

```
Build two pages that read the files the agents maintain.

First the Notes page. Add endpoints that list the note files for a subject, newest first, and return the contents of a chosen note. The page has a subject dropdown, a left-hand list of note files, and a right-hand reading panel that fetches the selected note and renders its markdown with Marked, with the headings styled in the orange and teal accent scheme so the notes look polished.

Then the Schedule page. Add an endpoint that returns the weekly schedule, the deadlines and the exams as structured data plus today's weekday, and have it read from two sources, because Planner writes planning data two different ways and the page must understand both or rows go silently missing. First, the three global planning files for entries [your name] adds manually one at a time. Second, any consolidated per-subject planning file that the upload pipeline produces under each subject's planning folder, which groups everything under section headings such as Weekly Schedule, Deadlines and Exams; scan the subject planning folders, split each consolidated file by its section headings, and route each section's table into the matching bucket by keyword, ignoring sections you do not recognise such as Office Hours. Merge both sources and drop duplicate rows. The page shows four cards: today's classes filtered to the current weekday, the full weekly timetable, the deadlines, and the exams, each presented as a clean table with small coloured badges. Planner fills these files in over Telegram or Discord and through the upload pipeline; this page only displays them. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

## Part 05 / 06 — Extending Agents & Advanced Features

### Prompt 20 — Prompt 19 — Extend Scholar with research

```
Scholar, you now have a second capability in addition to note extraction, and it is permanently part of your role: research. When I or Bill send you a research request, which is a topic, a question, or a block of text, investigate it thoroughly using your web search tools, gather current information from reputable sources, then analyse and synthesise what you find. Save your findings as a single structured markdown document into /home/hermes/research at the exact file path given in the request, using the heading structure the request specifies, which is normally Summary, Key Insights, Supporting Evidence, References and Actionable Takeaways, and always cite your sources in the References section. Unlike note extraction, where you never summarise, research is a synthesis task where you are expected to distil and draw conclusions. Report to Bill when the research is saved. Confirm research is now part of your role.
```

### Prompt 21 — Prompt 20 — The Research workspace

```
Build a Research workspace backed by a small research database that stores an id, title, query, filename, status and created time. Add an endpoint to submit a research request that stores the request as researching and then triggers Scholar with a prompt telling it to search the web and save a structured findings document into /home/hermes/research. Add an endpoint that lists the research items and flips a row to complete once its file exists on disk, an endpoint that returns a finished document's content, and an endpoint that hands a finished research file to Quizmaster to build a quiz from it. The page has a submit form with a title and a topic box, a history list with a live status that shows a spinner while researching and a badge when complete by polling every few seconds, and a viewer that renders the finished markdown with a Make Quiz button. Also update Bill's persona so he knows research is saved in /home/hermes/research, can list and read those files, and can route a finished piece of research to Quizmaster for a quiz or to Planner for a study plan when I ask. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 22 — Prompt 21 — Lecture Notes — an in-app PDF reader with saved annotations

```
Build a Lecture Notes reader inside the dashboard using Mozilla's prebuilt PDF.js viewer, downloaded into the static folder. Add an endpoint that lists every uploaded PDF across all subjects, an endpoint that serves a chosen PDF inline, and an endpoint that overwrites a PDF with a new copy sent in the request body. The page has a left list of all PDFs with a subject filter and a right panel that embeds the PDF.js viewer pointed at the chosen file, plus a fullscreen button. Inject a small save script into the viewer so that when annotations change, debounced, and when the tab is hidden, it captures the annotated bytes and saves them back to the same file, so highlights and notes embed into the PDF and persist. Add a Save button to the toolbar as well. This lives under the Library destination as the Lecture Notes sub-tab. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 23 — Prompt 22 — Quiz player and history

```
Build the Quiz feature. Add an endpoint to ask Quizmaster to generate a quiz from a subject's notes, an endpoint that lists a subject's quiz files, and an endpoint that parses a chosen quiz file into structured questions, where each block is a question marked as multiple choice or true-false with its options and the correct answer. Add a small progress database that stores each attempt with the subject, file, score, total, percentage and time, an endpoint to save an attempt, and an endpoint that returns recent attempts plus per-subject averages. The page has three phases: a select phase to pick a subject and quiz or ask Quizmaster to generate one, an active phase that shows one question at a time with the options as clickable cards where confirming reveals correct or incorrect and a progress bar advances, and a results phase with a circular score ring, a message and a retake button. When a quiz ends, save the attempt. This lives under the Practice destination as the Quiz sub-tab. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 24 — Prompt 23 — Extend Quizmaster with flashcards

```
Quizmaster, two permanent updates to your role, saved to your persona and memory. First, from now on use only two question types in quizzes, multiple choice with exactly four options and true-false, and end every question with the answer on its own line, because that is what the dashboard quiz player reads. Second, you now also generate flashcard decks from Scholar's notes when asked. These flashcards are not a quiz — they have no questions and no answers. Each card is a short standalone snippet, one key fact, definition, formula or concept distilled into one or two plain sentences, that the student swipes through and reads on the go. Save a deck into the subject's flashcards folder, writing each card as a plain snippet with no question-and-answer markers, no headings and no numbering, and separate every card from the next with a line containing only three dashes. Put at least fifteen snippets in a deck and keep each one self-contained and skimmable. Confirm both updates are saved.
```

### Prompt 25 — Prompt 24 — The Flashcards page

```
Build the Flashcards feature. These flashcards are not a quiz and have no questions or answers — each card is just a short snippet of one key idea pulled from the notes, and the student swipes through them to read on the go. Add an endpoint that lists a subject's decks, an endpoint that parses a chosen deck file into a list of snippets by splitting on the three-dash separators and returning each block's text, and an endpoint that asks Quizmaster to generate a deck from the subject's notes. The page lets you pick a deck or generate one, then opens a read mode showing one snippet at a time on a single frosted card: a Previous and a Next button that move through the deck and loop around at the ends, the left and right arrow keys do the same, tapping the card advances to the next one, a position counter and a thin progress bar show where you are, and a shuffle button reorders the deck. There is no flip, no reveal, no Got It or Study Again, and no scoring. This lives under the Practice destination as the Flashcards sub-tab. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 26 — Prompt 25 — Tasks — a Kanban board

```
Build a Tasks page backed by a small productivity database with a tasks table holding an id, title, subject, status, position and created time, with endpoints to list, upsert and delete a task. The page has a row to add a task with a title and an optional subject tag, and a three-column board, To Do, In Progress and Done, colour-coded, using native drag-and-drop to move cards between columns where dropping updates the card's status and position and saves it. Done cards show a struck-through title, a delete control appears on hover, and each column shows a live count. This lives under the Planner destination as the Tasks sub-tab. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 27 — Prompt 26 — Focus — a Pomodoro timer and sticky notes

```
Build a Focus page. Extend the productivity database with a stickies table and a per-day pomodoro count, with endpoints to list, add and delete sticky notes and to read and increment today's pomodoro count. The page has two columns. On the left a Pomodoro card with Focus, Short Break and Long Break modes with adjustable durations, a large circular SVG ring that drains as the time counts down and shifts colour per mode, Start, Pause, Reset and Skip controls, automatic advancing where four focus sessions lead into a long break, a soft sound when a session ends, and a sessions-today counter saved to the backend, with the durations remembered locally. On the right a sticky-note board where you pick a colour, add a note, edit it inline with a debounced auto-save, and delete it on hover, rendered as a tilted paper-card grid. This lives under the Planner destination as the Focus sub-tab. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

### Prompt 28 — Prompt 27 — Chat — talk to any agent in the browser

```
Build a Chat page so I can talk to each agent directly in the browser. Use a small chat database storing an id, agent, role, text and created time, and run each turn on the server so the reply still completes even if I navigate away. Add an endpoint that returns the agent list with Bill first, an endpoint that returns an agent's message history along with a flag for whether a turn is currently running, an endpoint to send a message which stores my message, mirrors it to the platform, then launches the agent turn as a background task and returns immediately, and an endpoint to reset an agent's conversation. The background turn runs the agent the same one-shot way the rest of the dashboard does, under that agent's profile, continuing a dedicated chat session so the agent keeps context, captures the reply, stores it, then mirrors it. Mirroring means posting both my message and the agent's reply into that agent's real channel so the conversation also shows up there, into the agent's Discord channel for the specialists and into my Telegram chat for Bill, posting as the bot so the gateway ignores it. Important detail: Discord sits behind Cloudflare, which rejects the default Python user agent with error 1010, so the request that posts to Discord must send a real browser-style User-Agent header or it silently fails. For the interface, use a Discord-style layout with a left list of agents each with a status dot, a conversation pane with date dividers, sent and received bubbles and timestamps, a header with a live indicator, a context-size bar and a Reset button, and a typing indicator while a turn is running. The client does not hold the turn open; it sends the message and then polls the history every couple of seconds, showing the typing dots while a turn is pending and rendering the reply when it lands, so leaving and returning still shows it. Enter sends, Shift and Enter make a new line, and Escape clears focus. Before building this, open the uploaded dashboard template on the Design Reference page and match its visual language exactly, including its colour palette, glassmorphism and translucency, spacing and padding, typography with its font sizes, weights and letter-spacing, element sizing and proportions, visual hierarchy, corner radii and shadows, and card and chart styling; the template is the visual source of truth, so copy only the look and never its demo data.
```

## Part 06 / 06 — Automation, Backups & Launch

### Prompt 29 — Prompt 28 — Automation — morning brief and backups

```
Set up two small pieces of automation in one go. First, a morning brief: build a standard-library Python script for Bill that fetches the current weather for my city from the Complimentary Open-Meteo service and turns the weather code into a short description, reads today's classes from the schedule file and the upcoming rows from the deadlines and exams files, builds a friendly message with a greeting, the date, the weather, today's classes, the deadlines this week and the upcoming exams, and sends it to me over Telegram using Bill's bot token and chat id. Add a scheduled job so it runs every day at seven in the morning, run it once now so I can confirm the message arrives, and note in Bill's persona that this brief goes out automatically every morning so he never needs to send it by hand. Second, versioned backups: build one script that snapshots the dashboard by copying its files into a new numbered version folder with an auto-incrementing number and a short description I pass in, and that bumps a version file the sidebar badge shows, plus a companion script that restores a chosen version by copying its files back and restarting the dashboard service. Take a first snapshot once it works.
```

### Prompt 30 — Prompt 29 — Final end-to-end test

```
Run a final end-to-end check. Upload a real PDF through the dashboard upload page, or post it to the upload endpoint directly. Bill should message me on Telegram as each step finishes. Then confirm the outputs landed: the subject now has a logged file inventory, a notes file from Scholar, and a quiz file from Quizmaster, and the agent activity database shows recent rows for Vault, Scholar, Quizmaster and Planner. If the notes, the quiz and the agent rows all appeared and Telegram pinged me, the system is fully wired and every new document now runs the whole pipeline automatically.
```

### Prompt 31 — Prompt 30 — Secure remote access with Tailscale

```
Set up Tailscale on this VPS so I can securely access the Mission Control dashboard from anywhere, both on my PC and on my mobile device.

Please install and configure Tailscale on the VPS, then start the Tailscale authentication process and provide me with the login/authentication link so I can approve and connect the VPS to my Tailscale account.

After authentication, please verify that the VPS is connected to my Tailnet and confirm the Tailscale IP address. Then explain how I can use that Tailscale IP to access the Mission Control dashboard remotely from my PC or phone.

Also make sure the dashboard remains secure and is not unnecessarily exposed to the public internet.
```
