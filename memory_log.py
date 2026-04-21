"""Append-only writers for the markdown state files under memory/."""
import traceback
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent / "memory"


def _append(filename: str, entry: str) -> None:
    ROOT.mkdir(exist_ok=True)
    path = ROOT / filename
    if not path.exists():
        title = filename[:-3].replace("_", " ").title()
        path.write_text(f"# {title}\n\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as f:
        f.write(entry + "\n")


def log_trade(symbol, side, entry_price, exit_price, qty, pnl, timestamp=None):
    ts = (timestamp or datetime.utcnow()).isoformat()
    exit_str = f"${exit_price:.2f}" if exit_price is not None else "—"
    pnl_str = f"{pnl:+.2f}" if pnl is not None else "—"
    _append(
        "trade_history.md",
        f"- **{ts}** | {side.upper()} {qty} {symbol} | entry ${entry_price:.2f} "
        f"→ exit {exit_str} | P/L ${pnl_str}",
    )


def log_account_snapshot(equity, cash, buying_power, timestamp=None):
    ts = (timestamp or datetime.utcnow()).isoformat()
    _append(
        "account_snapshots.md",
        f"- **{ts}** | equity ${float(equity):.2f} | "
        f"cash ${float(cash):.2f} | buying power ${float(buying_power):.2f}",
    )


def log_error(context: str, error: BaseException) -> None:
    ts = datetime.utcnow().isoformat()
    _append(
        "errors.md",
        f"### {ts} — {context}\n"
        f"```\n{type(error).__name__}: {error}\n{traceback.format_exc()}```",
    )
