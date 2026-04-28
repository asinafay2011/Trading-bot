"""Trading strategies. Selected via the STRATEGY env var; defaults to "trend".

  STRATEGY=trend     SMA20 > SMA50 + RSI < 70 (trend in place + not overbought)
  STRATEGY=donchian  Close > 20-bar high + volume > 1.2x avg (breakout momentum)
"""
import os

import pandas as pd

# --- Trend strategy params ---
SHORT_WINDOW = 20
LONG_WINDOW = 50
RSI_PERIOD = 14
RSI_ENTRY_MAX = 70
RSI_EXIT_MIN = 70

# --- Donchian breakout params ---
DONCHIAN_LOOKBACK = 20
DONCHIAN_EXIT_LOOKBACK = 10
VOLUME_MULTIPLIER = 1.2


def _active_strategy() -> str:
    name = os.environ.get("STRATEGY", "trend").strip().lower()
    return name if name in ("trend", "donchian") else "trend"


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


# ----- Trend strategy -----

def _trend_entry_filters(bars: pd.DataFrame) -> dict:
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


def _trend_exit_signal(bars: pd.DataFrame) -> bool:
    if len(bars) < LONG_WINDOW:
        return False
    close = bars["close"]
    long_ = sma(close, LONG_WINDOW)
    r = rsi(close)
    return bool(close.iloc[-1] < long_.iloc[-1] or r.iloc[-1] > RSI_EXIT_MIN)


def _trend_trigger_description(bars: pd.DataFrame) -> str:
    rsi_val = float(rsi(bars["close"]).iloc[-1])
    return f"SMA20 > SMA50, RSI={rsi_val:.1f}"


# ----- Donchian breakout strategy -----

def _donchian_entry_filters(bars: pd.DataFrame) -> dict:
    result = {"sufficient_data": False, "breakout": False, "volume_pass": False}
    if len(bars) < DONCHIAN_LOOKBACK + 1:
        return result
    close = bars["close"]
    volume = bars["volume"]
    prior_close = close.iloc[-(DONCHIAN_LOOKBACK + 1):-1]
    prior_volume = volume.iloc[-(DONCHIAN_LOOKBACK + 1):-1]
    prior_high = float(prior_close.max())
    avg_volume = float(prior_volume.mean()) if len(prior_volume) else 0.0
    result["sufficient_data"] = True
    result["breakout"] = bool(close.iloc[-1] > prior_high)
    result["volume_pass"] = bool(
        avg_volume > 0 and volume.iloc[-1] > VOLUME_MULTIPLIER * avg_volume
    )
    return result


def _donchian_exit_signal(bars: pd.DataFrame) -> bool:
    if len(bars) < DONCHIAN_EXIT_LOOKBACK + 1:
        return False
    close = bars["close"]
    prior_low = float(close.iloc[-(DONCHIAN_EXIT_LOOKBACK + 1):-1].min())
    return bool(close.iloc[-1] < prior_low)


def _donchian_trigger_description(bars: pd.DataFrame) -> str:
    close = bars["close"]
    volume = bars["volume"]
    prior_close = close.iloc[-(DONCHIAN_LOOKBACK + 1):-1]
    prior_volume = volume.iloc[-(DONCHIAN_LOOKBACK + 1):-1]
    prior_high = float(prior_close.max())
    avg_volume = float(prior_volume.mean()) if len(prior_volume) else 0.0
    vol_mult = float(volume.iloc[-1]) / avg_volume if avg_volume > 0 else 0.0
    return (
        f"Breakout above {DONCHIAN_LOOKBACK}-bar high ${prior_high:.2f}, "
        f"vol={vol_mult:.1f}x avg"
    )


# ----- Public dispatchers -----

def entry_filters(bars: pd.DataFrame) -> dict:
    """Compute filter state for the active strategy. Each strategy returns a
    `sufficient_data` flag plus its own named filters (uptrend/rsi_pass for
    trend; breakout/volume_pass for donchian)."""
    if _active_strategy() == "donchian":
        return _donchian_entry_filters(bars)
    return _trend_entry_filters(bars)


def entry_signal(bars: pd.DataFrame) -> bool:
    flags = entry_filters(bars)
    if not flags["sufficient_data"]:
        return False
    return all(v for k, v in flags.items() if k != "sufficient_data")


def exit_signal(bars: pd.DataFrame) -> bool:
    if _active_strategy() == "donchian":
        return _donchian_exit_signal(bars)
    return _trend_exit_signal(bars)


def trigger_description(bars: pd.DataFrame) -> str:
    if _active_strategy() == "donchian":
        return _donchian_trigger_description(bars)
    return _trend_trigger_description(bars)


def active_strategy_name() -> str:
    return _active_strategy()
