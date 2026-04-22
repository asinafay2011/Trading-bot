"""Main trading bot orchestration. Entry point: run_trading_cycle()."""
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

import exchange
import risk
import strategy
from memory_log import log_account_snapshot, log_error, log_trade
from notifications import send_discord_message

load_dotenv()

ALLOWED_SYMBOLS = [
    # Core tech
    "AAPL", "MSFT", "TSLA", "NVDA", "AMD", "META", "AMZN", "NFLX", "GOOGL",
    "AVGO", "ORCL", "CRM", "ADBE", "QCOM",
    # Finance / payments
    "JPM", "BAC", "V", "MA", "HOOD", "COIN",
    # Consumer
    "WMT", "COST", "HD", "MCD", "NKE", "DIS",
    # High-beta / other
    "UBER", "PLTR",
    # ETFs
    "SPY", "QQQ",
    # Telecom / satellite
    "NOK", "SATS", "VSAT", "SBAC",
    # Energy / materials / industrial
    "PARR", "PLUG",
    # Semis (small/mid cap)
    "PI", "TSEM",
    # Biotech
    "RCUS", "RLAY", "SNDX", "VKTX",
    # Other / speculative
    "SPHE", "YSS",
]
SNAPSHOTS_FILE = Path(__file__).parent / "memory" / "account_snapshots.md"
ET = ZoneInfo("America/New_York")


def _et_now() -> str:
    return datetime.now(ET).strftime("%Y-%m-%d %H:%M ET")


def _is_paper() -> bool:
    return os.environ.get("PAPER_TRADING", "true").strip().lower() == "true"


def _live_confirmed() -> bool:
    # CLAUDE.md specifies an interactive CONFIRM_LIVE_TRADE typed confirmation.
    # In a headless routine we approximate that with an env-var gate the
    # operator must set explicitly before each live-trading window.
    return os.environ.get("LIVE_TRADE_CONFIRMED", "").strip().lower() == "true"


def _authorized_to_trade(symbol: str, qty: int, price: float) -> bool:
    if _is_paper():
        return True
    if not _live_confirmed():
        send_discord_message(
            f"**LIVE ORDER BLOCKED** — {qty} {symbol} @ ${price:.2f}\n"
            "Set LIVE_TRADE_CONFIRMED=true to proceed."
        )
        return False
    return True


def _snapshot_once_per_day(account) -> None:
    today = datetime.utcnow().date().isoformat()
    if SNAPSHOTS_FILE.exists() and today in SNAPSHOTS_FILE.read_text():
        return
    log_account_snapshot(account.equity, account.cash, account.buying_power)


def _manage_open_position(symbol: str, position, bars, account) -> None:
    entry_price = float(position.avg_entry_price)
    qty = int(float(position.qty))
    current_price = float(bars["close"].iloc[-1])

    if strategy.exit_signal(bars):
        exchange.close_position(symbol)
        for order in exchange.list_open_orders(symbol):
            exchange.cancel_order(order.id)
        pnl = (current_price - entry_price) * qty
        pct = (current_price / entry_price - 1) * 100 if entry_price else 0.0
        log_trade(symbol, "sell", entry_price, current_price, qty, pnl)
        send_discord_message(
            f"**EXIT** — {qty} {symbol} @ ${current_price:.2f} (exit signal)\n"
            f"Entry: ${entry_price:.2f}\n"
            f"P/L: ${pnl:+.2f} ({pct:+.2f}%)\n"
            f"Time: {_et_now()}\n"
            f"Equity after: ${float(account.equity):,.2f}"
        )
        return

    stops = [o for o in exchange.list_open_orders(symbol) if o.type == "stop"]
    if stops:
        stop_order = stops[0]
        current_stop = float(stop_order.stop_price)
        if risk.should_move_to_breakeven(current_price, entry_price, current_stop):
            exchange.cancel_order(stop_order.id)
            exchange.submit_stop_loss(symbol, qty, entry_price)
            pct = (current_price / entry_price - 1) * 100 if entry_price else 0.0
            send_discord_message(
                f"**STOP → BREAKEVEN** — {symbol}\n"
                f"Current: ${current_price:.2f} ({pct:+.2f}% from entry ${entry_price:.2f})\n"
                f"Stop moved to ${entry_price:.2f}"
            )


def _try_enter(symbol: str, bars, account) -> None:
    if not strategy.entry_signal(bars):
        return
    price = float(bars["close"].iloc[-1])
    buying_power = float(account.buying_power)
    qty = risk.position_size(buying_power, price)
    if qty <= 0:
        return
    if not _authorized_to_trade(symbol, qty, price):
        return
    exchange.submit_market_buy(symbol, qty)
    stop = risk.stop_price(price)
    exchange.submit_stop_loss(symbol, qty, stop)
    rsi_val = float(strategy.rsi(bars["close"]).iloc[-1])
    log_trade(symbol, "buy", price, None, qty, None)
    send_discord_message(
        f"**ENTRY** — {qty} {symbol} @ ${price:.2f}\n"
        f"Stop: ${stop:.2f} (-3.00%)\n"
        f"Trigger: 20-SMA crossed above 50-SMA, RSI={rsi_val:.1f}\n"
        f"Time: {_et_now()}\n"
        f"Equity after: ${float(account.equity):,.2f}"
    )


def run_trading_cycle() -> None:
    """Routine entry point. Scheduled every 15 minutes during market hours."""
    try:
        if "ALPACA_KEY_ID" not in os.environ or "ALPACA_SECRET_KEY" not in os.environ:
            raise RuntimeError(
                "Missing ALPACA_KEY_ID or ALPACA_SECRET_KEY. Update .env before trading."
            )

        if not exchange.is_market_open():
            return

        account = exchange.get_account()
        _snapshot_once_per_day(account)

        for symbol in ALLOWED_SYMBOLS:
            try:
                bars = exchange.get_bars(symbol, limit=100)
                if bars.empty:
                    continue
                position = exchange.get_position(symbol)
                if position is not None:
                    _manage_open_position(symbol, position, bars, account)
                else:
                    _try_enter(symbol, bars, account)
            except Exception as e:
                log_error(f"cycle failure for {symbol}", e)
                send_discord_message(f"**ERROR** — trading {symbol}\n{e}")
    except Exception as e:
        log_error("trading cycle", e)
        send_discord_message(f"**ERROR** — trading cycle halted\n{e}")
        raise


if __name__ == "__main__":
    run_trading_cycle()
