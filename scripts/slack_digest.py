#!/usr/bin/env python3
"""Daily digest of a role's Slack: every message from the last 24h in channels the user can see. Read-only.

Usage: python3 scripts/slack_digest.py <role>
Needs SLACK_TOKEN (user token xoxp-, search:read) in the role's env file.
Per channel: message count, who spoke, a short snippet of each of the latest messages and a link.
"""
import datetime
import json
import sys
import time
import urllib.error

from common import credentials, http_json, load_sources, not_configured

API = "https://slack.com/api/"
WINDOW_HOURS = 24
PAGES = 3          # 100 messages per page
SNIPPET = 140
PER_CHANNEL = 4
FULL_TEXT = 700     # --full: enough text for a model to summarise


def _search(token, query, page):
    data = http_json(API + "search.messages", {"Authorization": "Bearer " + token},
                     {"query": query, "count": 100, "page": page, "sort": "timestamp", "sort_dir": "desc"})
    if not data.get("ok"):
        raise OSError("slack search.messages: " + str(data.get("error")))
    return data["messages"]


def digest(role, full=False):
    creds = credentials(load_sources(role), ("SLACK_TOKEN",))
    if not creds:
        return not_configured(role, "slack")
    token = creds["SLACK_TOKEN"]
    since = time.time() - WINDOW_HOURS * 3600
    day = (datetime.date.today() - datetime.timedelta(days=2)).isoformat()
    try:
        auth = http_json(API + "auth.test", {"Authorization": "Bearer " + token})
        if not auth.get("ok"):
            raise OSError("slack auth.test: " + str(auth.get("error")))
        found = []
        for page in range(1, PAGES + 1):
            block = _search(token, "after:" + day, page)
            found += [m for m in block["matches"] if float(m.get("ts", 0)) >= since]
            if page >= block["paging"]["pages"]:
                break
    except (urllib.error.URLError, KeyError, OSError) as exc:
        return {"role": role, "source": "slack", "status": "error",
                "error": type(exc).__name__ + ": " + str(exc), "channels": []}

    by_channel = {}
    for m in found:
        ch = m.get("channel") or {}
        key = ("DM" if ch.get("is_im") else "#" + str(ch.get("name")))
        by_channel.setdefault(key, []).append(m)
    channels = []
    for name, msgs in sorted(by_channel.items(), key=lambda kv: -len(kv[1])):
        msgs.sort(key=lambda m: float(m["ts"]))
        channels.append({
            "channel": name,
            "count": len(msgs),
            "people": sorted({m.get("username") or "?" for m in msgs}),
            "latest": [{"from": m.get("username") or "?",
                        "time": datetime.datetime.fromtimestamp(float(m["ts"])).strftime("%d/%m %H:%M"),
                        "text": (m.get("text") or "").replace("\n", " ")[:(FULL_TEXT if full else SNIPPET)],
                        "url": m.get("permalink")} for m in (msgs if full else msgs[-PER_CHANNEL:])],
        })
    return {"role": role, "source": "slack", "status": "ok", "workspace": auth.get("team"),
            "window_hours": WINDOW_HOURS, "total": len(found), "channels": channels}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    result = digest(sys.argv[1], full="--full" in sys.argv)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(1 if result["status"] == "error" else 0)


if __name__ == "__main__":
    main()
