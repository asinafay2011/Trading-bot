# Daily summary routine description

This file documents a routine that sends a daily performance summary after markets close.  It is separate from the 15‑minute trading loop and is intended to run once per day.

- **Schedule**: 16:05 ET every weekday after the market closes.  Adjust the time for your timezone if necessary.
- **Prompt**: Use `CLAUDE.md` plus a short instruction: “Compile a summary of today’s trades and account performance and send it to Slack.”
- **Repositories**: This repository.  Ensure the latest code and memory files are present.
- **Environment**: Same as the trading bot routine.  The `SLACK_WEBHOOK_URL` variable must be set.
- **Connectors**: Slack (via the Slack skill).  Optionally add email if you want to receive an email summary as well.

To set up this routine in Claude Code, open a session and run:

```bash
/schedule weekdays at 16:05 run daily summary routine
```

Claude will guide you through selecting the repository and connectors.  During execution, the routine should read `memory/trade_history.md` and `memory/account_snapshots.md`, aggregate the results, and call `sendSlackMessage` to post the summary.
