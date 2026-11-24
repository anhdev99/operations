#!/usr/bin/env python3
"""Post a message to the personal Slack workspace (report destination).

Usage: python3 scripts/slack_post.py <channel-name> [--file path] [--dry-run]   (text from file or stdin)
Reads SLACK_BOT_TOKEN from ~/.claude/homelab.env. Only ever writes to that workspace.
"""
import json
import sys
import urllib.request

from common import load_env_file, ssl_context

ENV_FILE = "~/.claude/homelab.env"
API = "https://slack.com/api/"


def _call(token, method, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(API + method, data=data, headers={
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30, context=ssl_context()) as resp:
        return json.load(resp)


def post(channel_name, text, dry_run=False, blocks=None):
    """Post text (fallback/notification text) and optional Block Kit blocks to #channel_name. Returns (ok, detail)."""
    if dry_run:
        return True, "dry-run, " + str(len(text)) + " chars"
    token = load_env_file(ENV_FILE).get("SLACK_BOT_TOKEN")
    if not token:
        return False, "SLACK_BOT_TOKEN is empty in " + ENV_FILE
    listing = _call(token, "conversations.list?types=public_channel&exclude_archived=true&limit=500")
    if not listing.get("ok"):
        return False, "conversations.list: " + str(listing.get("error"))
    ids = {c["name"]: c["id"] for c in listing["channels"]}
    if channel_name not in ids:
        return False, "channel #" + channel_name + " not found"
    sent = _call(token, "chat.postMessage", {
        "channel": ids[channel_name], "text": text, "mrkdwn": True,
        "unfurl_links": False, "unfurl_media": False, **({"blocks": blocks} if blocks else {})})
    return bool(sent.get("ok")), "ok" if sent.get("ok") else str(sent.get("error"))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if "--file" in sys.argv:  # avoids shell-specific stdin redirection on Windows
        with open(sys.argv[sys.argv.index("--file") + 1], encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()
    ok, detail = post(sys.argv[1], text, "--dry-run" in sys.argv)
    print(("posted #" if ok else "FAILED #") + sys.argv[1] + ": " + detail)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
