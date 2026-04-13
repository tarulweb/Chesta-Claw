# CHESTA CLAW v1.0 Usage Guide

## Core Concepts
CHESTA is an agentic OS where the **CEO Brain** supervises specialized agents.

## Running Goals
1. Start the system: `python -m chesta.ui.api`
2. Open `http://localhost:3000/terminal`.
3. Type a goal like: "Generate a full-stack Next.js app for a crypto tracker."

## Skill Management
- **Prebuilt Skills**: Located in `chesta/skills/prebuilt/`. These include file ops, web research, and system control.
- **Custom Skills**: You can add your own `.py` files to `chesta/skills/custom/`.
- **Self-Improvement**: After complex tasks, the CEO writes `SKILL.md` in `chesta/skills/custom/` to remember optimized workflows.

## Messenger Integration
Configure your tokens in `chesta/mcp/adapters/` to enable Telegram/Discord control.

## Security
Dangerous commands (like `rm -rf`) are blocked by default. Add them to the whitelist in the **Settings** tab if you trust the agent for specific tasks.
