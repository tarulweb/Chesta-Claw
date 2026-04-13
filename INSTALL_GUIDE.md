# CHESTA CLAW v1.0 Installation & Guide

## Prerequisites
- Python 3.11+
- Rust 1.75+
- Node.js 18+
- Docker (optional, for sandboxing)

## 1-Command Installation
```bash
python chesta_cli.py install
```
This will:
1. Install all Python dependencies.
2. Build the Rust execution engine.
3. Configure the local SQLite database.

## Usage Guide
### Starting the System
```bash
# Start the Backend & UI
python -m chesta.ui.api
```
Then visit `http://localhost:3000` to access the dashboard.

### Using the Terminal
1. Navigate to the **Terminal** tab.
2. Enter a high-level goal (e.g., "Research the latest AI agents and create a summary report").
3. Watch the CEO Brain decompose the task and assign skills in real-time.

### Adding Skills
Browse the **Skills Marketplace** and click "Install" to add prebuilt capabilities.

### Configuration
Update `chesta/models/router_config.json` to add your API keys for OpenRouter, OpenAI, etc.
