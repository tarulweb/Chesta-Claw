# 🚀 CHESTA CLAW v1.0: Comprehensive Tutorial & Guide

Welcome to the future of agentic computing. This guide will take you from zero to running your own fleet of autonomous agents.

---

## 🛠 Step 1: Installation

### Prerequisites
- **Python 3.11+**: The orchestration heart.
- **Rust**: For the high-speed execution engine.
- **Node.js**: Powers the Next.js Dashboard.

### Single-Command Setup
Clone the repo and run the magic command:
```bash
git clone https://github.com/your-username/chesta-claw.git
cd chesta-claw
python chesta_cli.py install
```
*This command installs all dependencies, builds the Rust engine, and initializes your local memory.*

---

## 🧠 Step 2: Your First Agentic Goal

1. **Start the Engine**:
   ```bash
   python -m chesta.ui.api
   ```
2. **Access the Dashboard**: Open `http://localhost:3000` in your browser.
3. **Go to the Terminal**: Click the "Terminal" icon in the sidebar.
4. **Enter your Goal**:
   > "Research the top 5 AI startups in 2024, generate a comparison report in Markdown, and save it to a file named research_report.md"

### What happens under the hood?
- **The CEO Brain** receives the goal.
- It **decomposes** it into 3 sub-tasks:
  1. `web_research`: Search for startups.
  2. `content_gen`: Summarize findings.
  3. `system_ops`: Create the `.md` file.
- The **Multi-Model Router** picks the best LLM (e.g., Claude 3 for research, GPT-4o for generation).
- **Infinite Loop Detection** ensures the agent doesn't get stuck searching forever.

---

## 🛠 Step 3: Customizing Skills

### Adding a New Skill
1. Create a Python file in `chesta/skills/custom/my_skill.py`.
2. Define a `Skill` class with an `async def run` method.
3. Restart CHESTA, and your skill is instantly available to the CEO Brain.

### Self-Improvement (Hermes Style)
Every time CHESTA completes a complex task, check the `chesta/skills/custom/` directory. You'll find `SKILL.md` files where the CEO Brain has documented the most efficient path it found.

---

## 📱 Step 4: Messenger Integration

Control your OS from anywhere!
1. Go to the **Integrations** tab in the Dashboard.
2. Add your Telegram Bot Token or Discord Webhook.
3. Message your bot: `/goal "Check my system status and report back."`

---

## 🔒 Step 5: Security & Whitelisting

CHESTA is powerful but safe.
- If an agent tries to run a dangerous command (like `rm`), it will be blocked.
- Go to **Settings > Security** to whitelist specific commands for trusted workflows.

---

## 📈 Next Steps
- Explore the **Marketplace** for 100+ prebuilt skills.
- Set up **Workflows** for recurring tasks.
- Join the community and build the future of AI!
