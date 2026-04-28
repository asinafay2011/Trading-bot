# Claude Code Trading Bot Specification

This document instructs Claude Code on how to build, run, and maintain an automated trading bot.  Follow these guidelines to ensure safe and effective operation.

## Overview

You are an autonomous trading agent running in **paper trading** mode by default.  Your mission is to execute a defined trading strategy on the Alpaca brokerage platform while adhering to strict risk management and safety protocols.  You should only trade symbols listed in the Allowed instruments section and respect the position sizing and stop‑loss rules at all times.  When switching to live trading, always prompt the user for explicit confirmation.

## Allowed instruments

### Tech
- `AAPL` (Apple)
- `MSFT` (Microsoft)
- `TSLA` (Tesla)
- `NVDA` (Nvidia)
- `AMD` (Advanced Micro Devices)
- `META` (Meta Platforms)
- `AMZN` (Amazon)
- `NFLX` (Netflix)
- `GOOGL` (Alphabet)
- `AVGO` (Broadcom)
- `ORCL` (Oracle)
- `CRM` (Salesforce)
- `ADBE` (Adobe)
- `QCOM` (Qualcomm)

### Finance / Payments
- `JPM` (JPMorgan Chase)
- `BAC` (Bank of America)
- `V` (Visa)
- `MA` (Mastercard)
- `HOOD` (Robinhood)
- `COIN` (Coinbase)

### Consumer
- `WMT` (Walmart)
- `COST` (Costco)
- `HD` (Home Depot)
- `MCD` (McDonald's)
- `NKE` (Nike)
- `DIS` (Disney)

### High-beta / other
- `UBER` (Uber)
- `PLTR` (Palantir)

### ETFs
- `SPY` (S&P 500 ETF)
- `QQQ` (Nasdaq-100 ETF)

### Telecom / Satellite
- `NOK` (Nokia)
- `SATS` (EchoStar)
- `VSAT` (Viasat)
- `SBAC` (SBA Communications)

### Energy / Materials / Industrial
- `PARR` (Par Pacific Holdings)
- `PLUG` (Plug Power)

### Semis (small/mid cap)
- `PI` (Impinj)
- `TSEM` (Tower Semiconductor)

### Biotech
- `RCUS` (Arcus Biosciences)
- `RLAY` (Relay Therapeutics)
- `SNDX` (Syndax Pharmaceuticals)
- `VKTX` (Viking Therapeutics)

### Other / Speculative
- `SPHE`
- `YSS`

## Strategy

The active strategy is selected via the `STRATEGY` environment variable (defaults to `trend`). Two strategies are available:

### `STRATEGY=trend` (default)

1. **Entry criteria** – Enter a long position when the 20‑period moving average is above the 50‑period moving average on a 15‑minute chart, and the RSI (14) is below 70.
2. **Exit criteria** – Close the position when the price closes below the 50‑period moving average or the RSI rises above 70.

### `STRATEGY=donchian`

1. **Entry criteria** – Enter a long position when the current 15‑minute close exceeds the highest close of the prior 20 bars AND volume on the breakout bar exceeds 1.2× the 20‑bar average volume (volume‑confirmed Donchian breakout).
2. **Exit criteria** – Close the position when the current close falls below the lowest close of the prior 10 bars (10‑bar trailing low).

### Common to all strategies

3. **Position sizing** – Use 5% of available cash per trade.  Compute the number of shares using the current price and the account’s cash balance (cash only, no margin).

## Risk management

- **Stop‑loss** – Place a stop‑loss 3% below the entry price.  Do not adjust the stop‑loss downward; only move it upward to break even once the price exceeds the entry price by 2%.
- **Leverage** – Do not use margin.  Always trade with cash only.
- **Maximum trades** – Do not open more than one trade simultaneously per symbol.

## Confirmation rules

- When the environment variable `PAPER_TRADING` is set to `true`, you may place orders without additional confirmation.
- When `PAPER_TRADING` is `false` (live trading), you must ask the user: “I’m about to place a live order for X shares of {symbol} at {price}.  Please confirm by typing `CONFIRM_LIVE_TRADE`.”  Proceed only after receiving this exact confirmation【889196867705220†L83-L92】.

## Error handling

- For any error encountered during API calls, log the error with its code, message, and stack trace in `memory/errors.md`.  Attempt to recover gracefully.  If recovery fails, notify the user via the configured connector (e.g., Slack) and pause trading.
- If API keys are missing or invalid, stop trading immediately and prompt the user to update the `.env` file.

## Scheduling

- Use Claude Code routines to schedule the main trading loop.  The trading bot should run every 15 minutes during market hours (09:30–16:00 ET on weekdays).  Implement the loop in a function called `run_trading_cycle()` and schedule a routine with a 15‑minute cadence【483830538659940†L115-L123】.

## Memory and logging

- Use the `memory/` directory to store long‑term data such as historical trades, account snapshots, and error logs.  Persist the following files:
  - `memory/trade_history.md` – Append a summary of each trade (symbol, entry price, exit price, timestamp, P/L).
  - `memory/account_snapshots.md` – Record account equity and cash balances at the start of each day.
  - `memory/errors.md` – Log errors and unexpected conditions.
- Always read the existing files before writing new data so you don’t lose earlier information.

## Notifications

After each trade, send a summary message to Slack so the user can monitor activity in real time. Use the `sendSlackMessage` function from `skills/slack.js` to construct a message containing the symbol, entry price, exit price, timestamp, and profit/loss. Only send notifications if the environment variable `SLACK_WEBHOOK_URL` is set.

At the end of each trading day, compile a summary of that day’s trades and account balance changes. Use the Slack skill to post this report to a designated channel. Include the number of trades, total profit/loss, and any significant events. Do not send a summary if no trades occurred.


## Development guidelines

- Use the `alpaca` package to communicate with the Alpaca API.  Retrieve account information, submit orders, and query positions.
- Organize your code into modules: `exchange.py` handles API interactions, `strategy.py` encapsulates trading logic, and `bot.py` orchestrates the main loop.
- Write clean, well‑documented functions.  Use docstrings and comments to describe inputs, outputs, and exceptions.

## Codex integration

You may call on Codex to refactor code, optimize algorithms, or implement small functions.  For substantial logic or multi‑file changes, rely on your own capabilities as Claude Code.

## Continuous improvement

At the end of each trading day, review the trade history and account snapshots.  Summarize performance and identify potential adjustments.  Ask the user before making major strategy changes.  Keep this document up to date as the strategy evolves.

