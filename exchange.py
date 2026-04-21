"""Alpaca API wrapper. All broker interactions live here."""
import os

import pandas as pd
from alpaca_trade_api.rest import REST, APIError, TimeFrame, TimeFrameUnit


def _client() -> REST:
    key = os.environ["ALPACA_KEY_ID"]
    secret = os.environ["ALPACA_SECRET_KEY"]
    paper = os.environ.get("PAPER_TRADING", "true").lower() == "true"
    base_url = "https://paper-api.alpaca.markets" if paper else "https://api.alpaca.markets"
    return REST(key, secret, base_url)


def get_account():
    """Return the Alpaca account object (equity, cash, buying_power, ...)."""
    return _client().get_account()


def is_market_open() -> bool:
    return bool(_client().get_clock().is_open)


def get_position(symbol: str):
    """Return the open Position for `symbol`, or None if none is held."""
    try:
        return _client().get_position(symbol)
    except APIError:
        return None


def get_bars(symbol: str, limit: int = 100) -> pd.DataFrame:
    """Fetch 15-minute bars for `symbol` as a DataFrame (open/high/low/close/volume)."""
    return _client().get_bars(
        symbol, TimeFrame(15, TimeFrameUnit.Minute), limit=limit
    ).df


def submit_market_buy(symbol: str, qty: int):
    """Submit a cash-only, day-good market buy."""
    return _client().submit_order(
        symbol=symbol, qty=qty, side="buy", type="market", time_in_force="day"
    )


def submit_stop_loss(symbol: str, qty: int, stop_price: float):
    """Attach a GTC stop-loss sell order."""
    return _client().submit_order(
        symbol=symbol,
        qty=qty,
        side="sell",
        type="stop",
        time_in_force="gtc",
        stop_price=round(stop_price, 2),
    )


def list_open_orders(symbol: str):
    return _client().list_orders(status="open", symbols=[symbol])


def cancel_order(order_id: str) -> None:
    _client().cancel_order(order_id)


def close_position(symbol: str):
    """Liquidate any open position in `symbol` at market."""
    return _client().close_position(symbol)
