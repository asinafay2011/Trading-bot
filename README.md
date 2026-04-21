# Trading Bot Project Setup

This project provides a skeleton for building an automated trading bot using **Claude Code** and **Codex**.  It includes a sample directory structure and placeholder files to guide you in setting up your own AI‑driven trading system.

## Directory structure

- `README.md` – This file.  Explains how to configure and run the project.
- `CLAUDE.md` – Prompt instructions for Claude Code (see below).
- `memory/` – Directory for long‑term memory files that store state between runs.  You can add additional `.md` files here to save your bot’s knowledge and conversation histories.
- `skills/` – Custom skill modules that extend Claude Code.  You can implement functions here to interact with external APIs (e.g., the Alpaca brokerage API) or perform custom computations.  A sample `alpaca.js` is provided.
- `routines/` – Scripts used to schedule recurring routines with Claude Code or Cron.  Add routine definitions here to run your bot automatically.
- `docs/` – Additional documentation or helper files.  You can store research or strategy documents in this folder.
- `.env.example` – Sample environment variables file.  Copy to `.env` and fill in your API keys.

## Getting started

1. **Create accounts**

   - **Claude Code** – Sign up at [Claude.ai](https://claude.ai) and enable Claude Code on your account.  Claude Code will be used to generate and refine the trading bot code and to run scheduled routines.
   - **Codex** – Ensure you have access to Codex via the OpenAI platform.  You will use Codex to quickly iterate on code, review logic, or supplement the work performed by Claude Code.
   - **Brokerage (Alpaca, ByBit, Binance, etc.)** – Create an account on a supported brokerage platform that offers a paper‑trading or test environment.  This skeleton is written for **Alpaca**.  Make sure you obtain your API key and secret and enable paper trading.
   - **Other services** – If you plan to connect Slack, email, or other connectors, create accounts and note any required API tokens.

2. **Clone this repository**

   Clone or copy this project to your local machine or a VPS where you will run Claude Code.  From your terminal:

   ```bash
   git clone <your_repo_url>.git
   cd trading_bot_project
   ```

3. **Install dependencies**

   Claude Code runs in the cloud, so you typically won’t install dependencies manually.  However, if your skills require external libraries (e.g., Node packages or Python modules), you can declare them in `package.json` or `requirements.txt` and use the appropriate package manager.  For example:

   ```bash
   # For Node JS skills
   npm install alpaca-trade-api

   # For Python skills
   pip install alpaca-trade-api
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your API keys and secrets.  Claude Code uses the `.env` file to access environment variables securely.

   ```bash
   cp .env.example .env
   echo "ALPACA_KEY_ID=your_key_id" >> .env
   echo "ALPACA_SECRET_KEY=your_secret_key" >> .env
   echo "PAPER_TRADING=true" >> .env
   ```

5. **Edit `CLAUDE.md`**

   The `CLAUDE.md` file contains the core instructions for Claude Code.  Describe the trading strategy, risk management rules, and guardrails here.  Claude Code will read this file and use it to generate the initial bot code and behaviours.  See the default template in this repository for guidance.

6. **Generate the bot code**

   Open a new Claude Code session and load this repository.  In the chat prompt, instruct Claude Code to read `CLAUDE.md` and build the trading bot accordingly.  Claude Code will produce source files under `skills/`, such as `bot.py`, `exchange.py`, `strategy.py`, etc.  Review and refine the generated code as needed.

   > **Tip:** The quality of `CLAUDE.md` is critical.  A detailed specification with risk parameters, allowed instruments, position sizing rules, and confirmation prompts will result in safer, more robust code【889196867705220†L45-L69】.

7. **Set up routines (scheduling)**

   To run the bot automatically, create a routine in Claude Code.  Routines are saved configurations that run on Anthropic‑managed cloud infrastructure.  They can be triggered on a schedule (hourly, daily, weekly), by an HTTP API call, or by GitHub events【483830538659940†L100-L118】.  Use the `/schedule` command in Claude Code or the web UI to create a new routine that runs your trading bot at the desired intervals.

   * Each routine can have multiple triggers (schedule, API, GitHub)【483830538659940†L115-L123】.
   * Routines run autonomously without prompting for confirmation during execution【483830538659940†L164-L174】.
   * When creating a routine, select this repository, choose the appropriate environment (paper trading vs. live), and add any connectors (Slack, email) for notifications.

8. **Use Codex for refinement**

   After Claude Code generates the initial code, you can open the same repository in a Codex workspace.  Use Codex to refactor functions, optimize performance, or add additional features.  Codex is fast and efficient for single‑file edits or small changes, whereas Claude Code excels at multi‑file reasoning and long‑term context【112159185290274†L94-L117】.

   You can alternate between Claude Code and Codex: run long sessions and schedule routines with Claude Code, and then ask Codex to review or refine the code.  This hybrid approach combines the strengths of both models for better overall results.

9. **Monitor and adjust**

   Once your bot is running, monitor its performance on the paper‑trading environment.  Adjust your strategy in `CLAUDE.md`, update the code, and revise your routines as necessary.  Only enable live trading after thorough backtesting and confirmation that the guardrails operate correctly.  Claude Code can enforce confirmation prompts for live trades as an extra safety measure【889196867705220†L83-L92】.

## Next steps

- Expand the sample `alpaca.js` skill in the `skills/` directory to implement order placement, account balance retrieval, and other API interactions.
- Develop more sophisticated strategies and risk management logic in `strategy.py` or other modules.
- Integrate additional connectors (e.g., Slack, email, ClickUp) through Claude Code’s connectors so that you receive alerts and daily summaries.
- Consider using version control (GitHub) to manage changes and collaborate with others.

This skeleton is only a starting point.  Use it as a foundation and adapt it to your own needs.  Happy building!
## Adding Slack notifications

To monitor bot activity in real time, you can connect a Slack incoming webhook and enable notification messages:

1. **Create a Slack webhook** – In your Slack workspace, go to **Apps → Manage** and add the **Incoming Webhooks** app.  Choose a channel and copy the webhook URL Slack provides.
2. **Configure the environment** – Open your `.env` file and set `SLACK_WEBHOOK_URL=<your_webhook_url>`.  This variable enables the Slack notification feature.
3. **Use the Slack skill** – The `skills/slack.js` module defines a `sendSlackMessage(text)` function.  Claude Code can import this skill and call it to send messages when trades occur or at the end of the day.  The `CLAUDE.md` file has been updated with guidance on when to send notifications.

If you prefer a different connector (e.g., Microsoft Teams, Telegram), create a new skill in `skills/` that wraps the corresponding API and update `CLAUDE.md` accordingly.

## Example daily summary routine

Besides the main 15‑minute trading loop, you might want a daily summary routine that runs after markets close.  Create a new routine that triggers at 16:05 ET on weekdays, reads the trade history and account snapshots, compiles a summary, and posts it to Slack using the Slack skill.  This helps you track performance and detect anomalies promptly.

