# Trading routine description

This markdown file describes the schedule and triggers for the trading bot routine.  It’s not a program but a documentation file to remind you how to configure the routine in Claude Code.

- **Schedule**: Run every 15 minutes on weekdays between 09:30 and 16:00 ET.
- **Prompt**: Use the `CLAUDE.md` file as the session prompt.  The routine should run the `run_trading_cycle()` function from `bot.py`.
- **Repositories**: This repository (trading_bot_project) should be added.  Make sure your `.env` file is configured.
- **Environment**: Use an environment with network access enabled (so that API calls to Alpaca succeed).  Ensure the correct values for `ALPACA_KEY_ID`, `ALPACA_SECRET_KEY`, and `PAPER_TRADING` are present.
- **Connectors**: Add Slack connector or email to receive notifications after each cycle.

To create this routine via the CLI, open a Claude Code session and run:

```bash
/schedule every 15 minutes run trading bot
```

Claude Code will guide you through selecting the repository, environment, and connectors.  After creation, the routine will appear in your routines dashboard【483830538659940†L164-L175】.

