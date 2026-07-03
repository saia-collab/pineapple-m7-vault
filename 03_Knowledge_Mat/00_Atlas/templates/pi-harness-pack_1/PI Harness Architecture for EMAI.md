---
type: research
status: active
date: "2026-04-08"
tags: [pi, harness, architecture, ui, agents, workflow]
related:
  - "[[PI]]"
  - "[[Claude Code]]"
  - "[[Codex]]"
  - "[[Obsidian]]"
  - "[[Google Workspace]]"
---

# PI Harness Architecture for EMAI

## The goal

Do **not** try to build a general-purpose AI operating system first.

Build a narrow harness for **your actual operator workflows**:
- planning
- content
- client follow-up
- context retrieval
- review / approval

The point of [[PI]] is not "replace [[Claude Code]] immediately."

The point is:
- own the harness
- own the commands
- own the context rules
- own the UI around decisions

## The simplest mental model

- [[Claude Code]] = production appliance
- [[PI]] = harness workshop
- [[Codex]] = worker engine

That means:
- keep using [[Claude Code]] for the stuff that already works
- use [[PI]] to build the custom layer you wish existed
- use [[Codex]] later as a delegated worker where useful

## What the harness actually is

The harness is not the model.

The harness is:
- what context gets loaded
- which commands exist
- which tools are available
- what UI appears before risky actions
- how outputs get logged back into the vault
- how work gets routed between tools

That is the real product.

## The 5 layers

### 1. Context layer

This decides what the agent sees.

Inputs:
- `AGENTS.md`
- active daily note
- recent daily notes
- selected project note
- relevant people / client notes
- content pipeline notes
- reusable system prompts / skill files

What it should do:
- inject only the right files for the task
- avoid blind whole-vault dumping
- surface "carry-over" work
- pull recent business state automatically

This is where your "memory" becomes operational.

### 2. Command layer

These are the workflows the user can trigger fast.

Good v1 commands:
- `/today`
- `/content`
- `/client-context`
- `/followup`
- `/review`

Each command should:
- gather specific context
- run a predictable workflow
- return a structured output
- optionally write back to the vault

### 3. Tool layer

These are the actions the harness can take.

Good v1 tools:
- read / write files in the vault
- search notes
- git status / diff
- queue an email draft
- pull calendar / email metadata
- open a review screen before sending or writing

Do not try to rebuild everything at once.

### 4. UI layer

This is the part most people skip.

The UI is what turns "agent chaos" into a usable system.

Good v1 UI pieces:
- command picker
- context preview panel
- approval screen
- diff / write review
- status bar

What the UI should answer:
- what is this command about to read?
- what is it about to change?
- what model is running?
- what workflow am I in?
- what still needs my approval?

### 5. Orchestration layer

This is where "agent teams" eventually live.

But v1 should be simple:
- one orchestrator command
- one or two specialized worker routines
- no giant team graph yet

Do not start with:
- multi-tier lead / worker / manager architecture
- autonomous loops
- generic background swarm

Start with:
- one workflow
- one delegator
- one visible review step

## The first harness to build

Name:
- `EMAI Operator Harness`

Purpose:
- make business/operator workflows faster and more reliable inside the vault

V1 workflows:

### `/today`
Goal:
- build the day from daily note + carry-overs + active projects + calendar

Output:
- prioritized plan
- carry-over cleanup
- optional note updates

### `/content`
Goal:
- pull current pipeline, relevant research, and recent ideas

Output:
- best next video angle
- hook options
- packaging notes
- optional draft note

### `/client-context`
Goal:
- gather everything relevant for one client / person / project

Output:
- briefing
- open loops
- last actions
- next recommended move

### `/followup`
Goal:
- draft a follow-up based on actual history and current context

Output:
- draft message
- review screen
- optional vault log

### `/review`
Goal:
- show pending file changes / generated text / email draft before action

Output:
- approve
- reject
- revise

## What the UI should look like

### UI 1: command palette

Simple list:
- Today
- Content
- Client Context
- Follow-up
- Review

This gives the harness a "front door."

### UI 2: context preview

Before a run, show:
- files loaded
- project selected
- people / notes included
- external sources included

This is critical.
It builds trust and reduces mystery.

### UI 3: approval screen

Before writing or sending:
- show exact file changes
- show exact draft text
- show target note or email destination

Buttons / actions:
- approve
- revise
- cancel

### UI 4: session status bar

Show:
- current command
- current model
- selected workspace / project
- pending approvals
- last sync / write state

## What not to build first

Avoid these in v1:
- full web app
- giant package ecosystem
- complete custom agent marketplace
- generalized multi-agent architecture
- your own MCP replacement
- every command you can imagine

That is how this turns into infrastructure theater.

## The right build order

### Phase 1: narrow proof
- build `/today`
- add context preview
- add approval before writes

### Phase 2: operator workflows
- add `/content`
- add `/client-context`
- add `/followup`

### Phase 3: external tool integration
- add [[Google Workspace]]-related actions
- add email / calendar reads
- add logging back into the vault

### Phase 4: delegation
- add one worker-style routine
- use [[Codex]] or another model for bounded execution tasks

### Phase 5: packaging
- clean up extensions
- extract skills
- package reusable commands

## What success looks like

V1 is successful if:
- one workflow is clearly better than doing it manually
- the UI makes the workflow feel safe and legible
- the harness writes back to the vault cleanly
- you can run it repeatedly without re-explaining context

It does **not** need:
- full autonomy
- 10 agents
- a web dashboard
- every integration under the sun

## The actual product opportunity

The opportunity is not "I use [[PI]]."

The opportunity is:

> I built a harness for business operators that actually remembers context, routes work cleanly, and gives approvals before it does dumb shit.

That is far more valuable than a tool switch.

## Recommended next step

If building this for real, the next artifact should be:

`PI Harness Spec v1`

That spec should define:
- exact folder structure
- exact commands
- exact UI components
- exact tools
- exact approval points
- exact writeback behavior

That is the point where this becomes buildable.
