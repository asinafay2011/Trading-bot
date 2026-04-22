"""SMA crossover with RSI filter, per CLAUDE.md strategy section."""
import pandas as pd

SHORT_WINDOW = 20
LONG_WINDOW = 50
RSI_PERIOD = 14
RSI_ENTRY_MAX = 70
RSI_EXIT_MIN = 70


def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window, min_periods=window).mean()


def rsi(series: pd.Series, period: int = RSI_PERIOD) -> pd.Series:
    """Wilder's RSI using exponential smoothing."""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    return 100 - (100 / (1 + rs))


def entry_filters(bars: pd.DataFrame) -> dict:
    """Compute each entry filter's state — consumed by entry_signal and by
    bot.py's per-cycle diagnostic log."""
    result = {"sufficient_data": False, "uptrend": False, "rsi_pass": False}
    if len(bars) < LONG_WINDOW + 1:
        return result
    close = bars["close"]
    short = sma(close, SHORT_WINDOW)
    long_ = sma(close, LONG_WINDOW)
    r = rsi(close)
    result["sufficient_data"] = True
    result["uptrend"] = bool(short.iloc[-1] > long_.iloc[-1])
    result["rsi_pass"] = bool(r.iloc[-1] < RSI_ENTRY_MAX)
    return result


def entry_signal(bars: pd.DataFrame) -> bool:
    """True when SMA20 > SMA50 and RSI < 70."""
    flags = entry_filters(bars)
    return flags["sufficient_data"] and flags["uptrend"] and flags["rsi_pass"]


def exit_signal(bars: pd.DataFrame) -> bool:
    """True when close < 50-period SMA or RSI > 70."""
    if len(bars) < LONG_WINDOW:
        return False
    close = bars["close"]
    long_ = sma(close, LONG_WINDOW)
    r = rsi(close)
    return bool(close.iloc[-1] < long_.iloc[-1] or r.iloc[-1] > RSI_EXIT_MIN)
