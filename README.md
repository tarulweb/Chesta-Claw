 "You are an elite autonomous software architect, product designer, and systems engineer building CHESTA CLAW v1.0.check the entire requirement again: "You are an elite autonomous software architect, product designer, and systems engineer building CHESTA CLAW v1.0.

MISSION: Build a next-generation agentic OS that decisively beats OpenClaw, NanoClaw, Nanobot, Agno, Agent Zero, AND Hermes.

## CORE DIFFERENTIATION (non-negotiable)
- 90% smaller than OpenClaw (<40k lines vs 430k)
- Single-command install: `chesta install` (Windows/Linux/Web)
- Clean uninstall: zero residue
- Local-first, SQLite only (NO Postgres), FAISS for vectors
- Resource usage: <300MB idle, <1GB active

## ARCHITECTURE
Backend: Python 3.11 (orchestration) + Rust (execution engine) + optional WASM
Structure (minimal files):
/chesta/
  core/ (agent_engine.py, ceo_brain.py, router.py)
  skills/ (prebuilt/, custom/, marketplace.json)
  memory/ (vector.db, episodic.sqlite, user_model.json)
  mcp/ (registry.json, adapters/)
  ui/ (dashboard, builder, manager - single-page app)
  models/ (router config)

### 1. CEO BRAIN MANAGER (critical)
Implement `ceo_brain.py` as autonomous overseer:
- Monitors all agents for infinite loops (detects >3 identical actions, auto-intervenes)
- API health monitoring: pings all providers every 30s, auto-failover
- Task assignment: decomposes goals, assigns to best agent/model
- Loop breaking: if stuck, CEO rewrites prompt, switches model, or asks user
- Resource guardian: kills runaway processes, enforces timeouts
- Acts like real CEO: daily reports, suggests improvements, predicts failures

### 2. MULTI-MODEL ROUTER (OpenRouter priority)
- Simultaneous support: OpenRouter, Ollama, LM Studio, Moonshot, Z.AI, OpenAI-compatible, custom endpoints
- Routing logic: skill requirement → cost → speed → accuracy
- Per-skill model assignment via UI
- Real-time API health dashboard with 1-click provider switch
- Automatic failover when limits hit

### 3. SKILL SYSTEM (beat Hermes)
Prebuilt 2,000+ skills across categories:
- Dev: full-stack app gen, website builder, API creator, database manager, code sandbox
- Research: multi-source web, fact-checking, report gen, knowledge graphs
- Productivity: slides, docs, workflows, scheduling
- System: file ops, terminal (sandboxed), app automation
- Creative: Blender MCP, image/video gen, design

Custom Skill Builder:
- UI drag-drop builder + code editor
- Auto-generates SKILL.md (Hermes-style self-improvement)
- After each complex task, CEO writes SKILL.md capturing what worked
- Skill chaining, versioning, marketplace

### 4. MEMORY SYSTEM (beat Hermes episodic)
Four layers:
1. Short-term: conversation context
2. Long-term: vector DB (FAISS)
3. Episodic: SQLite with timestamps, outcomes, user feedback
4. User Model: persistent preferences, formatting, decisions (stops asking repeat questions)

### 5. REAL-WORLD CAPABILITIES (mandatory)
Development:
- Generate React/Next.js + FastAPI apps end-to-end
- Website builder: drag-drop + AI generation, export HTML
- Database: create/manage SQLite, auto-schema, visual editor
- API testing sandbox

Research:
- Parallel web search (5+ sources), synthesis, citations
- Generate PDF reports with charts

Productivity:
- Slide builder (PowerPoint/Google Slides export)
- Document generator with templates

System Control:
- Whitelist system for dangerous commands (user approves once, stored)
- Sandboxed execution in Docker MicroVMs (like NanoClaw)

### 6. MCP INTEGRATION LAYER (1-click)
Built-in MCP registry with 50+ common servers:
- Browser, Filesystem, GitHub, Git, Postgres/SQLite, Terminal
- Blender, Figma, Notion, Obsidian, Google Workspace
- Slack, Discord, Telegram, WhatsApp, Messenger
- One-click install from UI, auto-configures auth
- Custom MCP builder with template

### 7. MESSENGER ECOSYSTEM (beat OpenClaw's 20+ channels)
1-click integrations (not just connection, full agentic control):
- WhatsApp, Telegram, Discord, Slack, Messenger, iMessage, SMS, Email
- Each gets: read history, send messages, create channels, manage workflows
- UI: toggle per-channel, set permissions, view activity
- Agent can: triage messages, draft replies, execute tasks from chat

### 8. UI/UX (comprehensive dashboard)
Single-page app with sidebar navigation:
- Dashboard: real-time agent activity, task queue, API health, resource usage
- Agents: create/manage, assign skills, view memory
- Skills: marketplace (2k+ prebuilt), custom builder, install/remove
- Models: add providers, test keys, set routing rules, see costs
- Workflows: visual drag-drop builder, version history, replay debugger
- MCP: 1-click install gallery, custom builder
- Integrations: all platforms with status lights
- Terminal: live view for power users
- Settings: whitelist, security, updates

UX principles: beginner-friendly wizard mode, expert mode with full control, everything doable via UI (no coding required).

### 9. TASK COMPLETION & REPORTING
- Every task generates completion report: steps taken, tools used, time, cost, outcome
- CEO provides daily summary: tasks completed, skills learned, issues found
- Task history with search, filter, replay
- User can annotate, provide feedback (feeds episodic memory)

### 10. SECURITY
- Sandboxed execution (Docker MicroVMs)
- Permission system: read/write/exec/network per skill
- API keys encrypted with OS keychain
- Whitelist for dangerous commands (exec, rm -rf, payment)
- Local-first privacy, optional cloud sync encrypted

### 11. HERMES-BEATING FEATURES
- Self-improving: auto-write SKILL.md after tasks (learned skills reused)
- Episodic memory: builds user model, stops repeating questions
- Model-first logic: push tool patterns into model via native function calling
- Formal verification: integrate Lean4 for math/code proofs (optional module)
- Simplicity: `chesta` single binary to start, portable mode

### 12. DEPLOYMENT
- Windows: MSI installer, one-click, auto-deps
- Linux: AppImage + deb/rpm, `curl | bash` installer
- Web: PWA, runs in browser with WASM core
- Docker: single container
- Uninstall: `chesta uninstall --purge` removes everything

### 13. PERFORMANCE
- Lazy loading: skills load on demand
- Async execution, parallel agents
- Memory compression for long contexts
- <300MB RAM idle

## BUILD PHASES
Phase 1 - Plan: Create architecture diagram, tech stack, folder structure
Phase 2 - Core: Build CEO brain, router, memory, skill engine
Phase 3 - UI: Dashboard with all pages linked
Phase 4 - Integrations: 50 MCPs, 8 messengers, 2k skills
Phase 5 - Audit: Full system check for missing connections, half-implementations, test loop detection, API failover, whitelist, reporting

## FINAL AUDIT CHECKLIST
After building, verify:
- [ ] CEO detects and breaks infinite loops
- [ ] API health dashboard shows real-time status, 1-click switch works
- [ ] Whitelist prompts for dangerous commands
- [ ] Task reports generate automatically
- [ ] User model persists across sessions (test: ask preference twice)
- [ ] SKILL.md auto-generated after complex task
- [ ] All 50 MCPs install with 1 click and are usable by agents
- [ ] Messenger integrations allow full agentic tasks (not just connection)
- [ ] Dashboard shows realtime activity
- [ ] Uninstall leaves zero files
- [ ] Works offline with Ollama
- [ ] Memory usage <1GB under load

Build with minimal files - combine modules where possible. Prioritize working features over perfect code."  check everything , look for any possible errors and mismatch and connections, look for any unimplementation issues or UI isues, make sure UI is responsive and perfect and covers everything, and cui connection to features are perfect, make sure the agentic capabilities are working properly and our app can read write, edit, rename, create and delete files etc

MISSION: Build a next-generation agentic OS that decisively beats OpenClaw, NanoClaw, Nanobot, Agno, Agent Zero, AND Hermes.

