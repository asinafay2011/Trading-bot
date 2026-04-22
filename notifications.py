"""Discord notifications via incoming webhook. Silent no-op when unconfigured."""
import os
import sys

import requests

from memory_log import log_error

_warned_missing_webhook = False


def send_discord_message(text: str) -> None:
    global _warned_missing_webhook
    webhook = (os.environ.get("DISCORD_WEBHOOK_URL") or "").strip()
    if not webhook:
        if not _warned_missing_webhook:
            print(
                "[discord] DISCORD_WEBHOOK_URL not set — notifications disabled",
                file=sys.stderr,
            )
            _warned_missing_webhook = True
        return
    try:
        response = requests.post(webhook, json={"content": text}, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        # Never let notification failures break trading, but record them so
        # silent delivery problems (expired webhook, rate limits, 4xx payload
        # errors) are visible instead of vanishing.
        log_error("discord webhook post failed", e)
