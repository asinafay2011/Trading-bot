"""End-of-day summary routine. Reads memory files and posts a Discord digest."""
import re
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

import exchange
from memory_log import log_error
from notifications import send_discord_message

load_dotenv()

MEMORY = Path(__file__).parent / "memory"
PNL_PATTERN = re.compile(r"P/L \$([+-]?\d+\.\d+)")
SNAPSHOT_EQUITY_PATTERN = re.compile(r"equity \$([\d,\.]+)")


def _todays_trade_lines() -> list:
    path = MEMORY / "trade_history.md"
    if not path.exists():
        return []
    today = datetime.utcnow().date().isoformat()
    return [line for line in path.read_text().splitlines() if today in line]


def _start_of_day_equity() -> float | None:
    path = MEMORY / "account_snapshots.md"
    if not path.exists():
        return None
    today = datetime.utcnow().date().isoformat()
    for line in path.read_text().splitlines():
        if today in line:
            m = SNAPSHOT_EQUITY_PATTERN.search(line)
            if m:
                return float(m.group(1).replace(",", ""))
    return None


def _current_equity() -> float | None:
    try:
        return float(exchange.get_account().equity)
    except Exception:
        return None


def run_daily_summary() -> None:
    """Compile today's trades + account performance and post to Discord."""
    try:
        all_lines = _todays_trade_lines()
        entries = sum(1 for line in all_lines if " BUY " in line)
        exits = sum(1 for line in all_lines if " SELL " in line)
        pnls = [
            float(m.group(1))
            for line in all_lines
            for m in [PNL_PATTERN.search(line)]
            if m
        ]

        if entries == 0 and exits == 0:
            return  # CLAUDE.md: skip summary on no-activity days

        wins = sum(1 for p in pnls if p > 0)
        losses = exits - wins
        total_pnl = sum(pnls)

        today = datetime.utcnow().date().isoformat()
        lines = [f"**Daily summary — {today}**"]
        if exits > 0:
            lines.append(
                f"Completed trades: {exits}  |  Wins: {wins}  |  Losses: {losses}"
            )
            lines.append(f"Realized P/L: ${total_pnl:+.2f}")
        if entries > exits:
            lines.append(f"Open positions: {entries - exits}")

        current = _current_equity()
        sod = _start_of_day_equity()
        if current is not None and sod is not None:
            lines.append(
                f"Equity: ${current:,.2f}  (start of day: ${sod:,.2f})"
            )
        elif current is not None:
            lines.append(f"Equity: ${current:,.2f}")

        send_discord_message("\n".join(lines))
    except Exception as e:
        log_error("daily summary", e)
        send_discord_message(f"**ERROR** — daily summary failed\n{e}")
        raise


if __name__ == "__main__":
    run_daily_summary()
