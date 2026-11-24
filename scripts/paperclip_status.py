#!/usr/bin/env python3
"""Agent status per Paperclip company (local API, read-only).

Usage: python3 scripts/paperclip_status.py [PREFIX ...]   e.g. TCH HOMA   (default: all companies)
"""
import json
import sys
import urllib.error
import urllib.request

import common  # noqa: F401  (sets UTF-8 stdio)

BASE = "http://127.0.0.1:3100/api"


def _get(path):
    with urllib.request.urlopen(BASE + path, timeout=10) as resp:
        return json.load(resp)


def status(prefixes=None):
    try:
        companies = _get("/companies")
        out = []
        for c in companies:
            if prefixes and c["issuePrefix"] not in prefixes:
                continue
            agents = _get("/companies/%s/agents" % c["id"])
            agents = agents if isinstance(agents, list) else agents.get("agents", [])
            out.append({"company": c["name"], "prefix": c["issuePrefix"], "status": c["status"],
                        "spent_cents": c.get("spentMonthlyCents"),
                        "agents": [{"name": a["name"], "role": a.get("role"), "status": a.get("status"),
                                    "last_heartbeat": a.get("lastHeartbeatAt")} for a in agents]})
        return {"source": "paperclip", "status": "ok", "companies": out}
    except (urllib.error.URLError, OSError, KeyError) as exc:
        return {"source": "paperclip", "status": "error",
                "error": "Paperclip khong tra loi (" + type(exc).__name__ + ")", "companies": []}


if __name__ == "__main__":
    r = status(sys.argv[1:] or None)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    sys.exit(1 if r["status"] == "error" else 0)
