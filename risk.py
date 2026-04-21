"""Position sizing and stop-loss rules, per CLAUDE.md risk management section."""

POSITION_PCT = 0.05
STOP_LOSS_PCT = 0.03
BREAKEVEN_TRIGGER_PCT = 0.02


def position_size(buying_power: float, price: float) -> int:
    """Whole-share quantity using 5% of buying power at `price`."""
    if price <= 0:
        return 0
    return int((buying_power * POSITION_PCT) // price)


def stop_price(entry_price: float) -> float:
    return entry_price * (1 - STOP_LOSS_PCT)


def should_move_to_breakeven(
    current_price: float, entry_price: float, current_stop: float
) -> bool:
    """True when price is +2% above entry and the stop is still below breakeven."""
    return (
        current_price >= entry_price * (1 + BREAKEVEN_TRIGGER_PCT)
        and current_stop < entry_price
    )
