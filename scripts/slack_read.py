#!/usr/bin/env python3
"""Read recent mentions of me and direct messages to me from a role's Slack. Read-only.

Usage: python3 scripts/slack_read.py <role>
Needs a user token (xoxp-...) with search:read. Stores sender, channel, the first 100
characters and a permalink only. Not yet verified against a real workspace.
"""
import datetime
import json
import sys
import urllib.error

from common import credentials, http_json, load_sources, not_configured, write_snapshot

HOURS = 48
API = "https://slack.com/api/"


def call(token, method, params=None):
    data = http_json(API + method, {"Authorization": "Bearer " + token}, params)
    if not data.get("ok"):
        raise OSError("slack " + method + ": " + str(data.get("error")))
    return data


def search(token, query):
    data = call(token, "search.messages", {"query": query, "count": 20, "sort": "timestamp"})
    return [{
        "from": m.get("username"),
        "channel": (m.get("channel") or {}).get("name"),
        "text": (m.get("text") or "").split("\n")[0][:100],
        "url": m.get("permalink"),
        "ts": m.get("ts"),
    } for m in data["messages"]["matches"]]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    role = sys.argv[1]
    creds = credentials(load_sources(role), ("SLACK_TOKEN",))
    if not creds:
        print(json.dumps(not_configured(role, "slack"), ensure_ascii=False, indent=2))
        return
    token = creds["SLACK_TOKEN"]
    after = (datetime.date.today() - datetime.timedelta(days=HOURS // 24)).isoformat()
    try:
        uid = call(token, "auth.test")["user_id"]
        result = {"role": role, "source": "slack", "status": "ok",
                  "mentions": search(token, f"<@{uid}> after:{after}"),
                  "direct": search(token, f"to:me after:{after}")}
    except (urllib.error.URLError, KeyError, OSError) as exc:
        result = {"role": role, "source": "slack", "status": "error",
                  "error": type(exc).__name__ + ": " + str(exc), "mentions": [], "direct": []}
    write_snapshot(role, "slack.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "error":
        sys.exit(1)


if __name__ == "__main__":
    main()
