"""End-of-day summary routine. Reads memory files and posts a Slack digest."""
import re
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

from memory_log import log_error
from notifications import send_slack_message

load_dotenv()

MEMORY = Path(__file__).parent / "memory"
PNL_PATTERN = re.compile(r"P/L \$([+-]?\d+\.\d+)")


def _todays_trade_lines() -> list:
    path = MEMORY / "trade_history.md"
    if not path.exists():
        return []
    today = date.today().isoformat()
    return [line for line in path.read_text().splitlines() if today in line]


def _latest_snapshot() -> str:
    path = MEMORY / "account_snapshots.md"
    if not path.exists():
        return "(no snapshots recorded)"
    snapshots = [l for l in path.read_text().splitlines() if l.startswith("- ")]
    return snapshots[-1] if snapshots else "(no snapshots recorded)"


def run_daily_summary() -> None:
    """Compile today's trades + latest snapshot and post to Slack."""
    try:
        trades = _todays_trade_lines()
        if not trades:
            return  # CLAUDE.md: skip summary on no-trade days
        total_pnl = sum(
            float(m.group(1))
            for line in trades
            for m in [PNL_PATTERN.search(line)]
            if m
        )
        body = "\n".join(
            [
                f"*Daily summary — {date.today().isoformat()}*",
                f"Trades: {len(trades)}",
                f"Total P/L: ${total_pnl:+.2f}",
                f"Latest snapshot: {_latest_snapshot()}",
            ]
        )
        send_slack_message(body)
    except Exception as e:
        log_error("daily summary", e)
        send_slack_message(f":rotating_light: Daily summary failed: {e}")
        raise


if __name__ == "__main__":
    run_daily_summary()
