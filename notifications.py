"""Slack notifications via incoming webhook. Silent no-op when unconfigured."""
import os

import requests


def send_slack_message(text: str) -> None:
    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook:
        return
    try:
        requests.post(webhook, json={"text": text}, timeout=10)
    except requests.RequestException:
        # Never let notification failures break trading.
        pass
