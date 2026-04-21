"""Discord notifications via incoming webhook. Silent no-op when unconfigured."""
import os

import requests


def send_discord_message(text: str) -> None:
    webhook = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook:
        return
    try:
        requests.post(webhook, json={"content": text}, timeout=10)
    except requests.RequestException:
        # Never let notification failures break trading.
        pass
