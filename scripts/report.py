#!/usr/bin/env python3
"""Collect raw data for the daily Slack report of one role. Read-only, prints JSON, sends nothing.

Usage: py scripts/report.py --raw --role <role>
"""
import argparse
import datetime
import html
import json
import os
import re
import subprocess
import sys
import urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import credentials, http_json, load_sources, not_configured
from op_read import api_get

HOURS = 24
DUE_SOON_DAYS = 3
ATTENTION_LIMIT = 10
SLACK_API = "https://slack.com/api/"


def _sub(script, *args):
    """Run an existing read-only connector and return its JSON (or an error stub)."""
    # PYTHONUTF8 makes the child decode `gh`'s UTF-8 output correctly on Windows (cp1252 consoles).
    env = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}
    proc = subprocess.run([sys.executable, str(HERE / script), *args], capture_output=True, text=True,
                          encoding="utf-8", env=env)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"status": "error", "error": (proc.stderr or proc.stdout).strip()[:300]}


def _openproject(role):
    src = load_sources(role)
    creds = credentials(src, ("OP_BASE_URL", "OP_TOKEN"))
    if not creds:
        return not_configured(role, "openproject")
    try:
        base, token = creds["OP_BASE_URL"], creds["OP_TOKEN"]
        projects = (src.get("openproject") or {}).get("projects") or [None]
        items, offset = [], 1
        for project in projects:
            path = f"/api/v3/projects/{project}/work_packages" if project else "/api/v3/work_packages"
            while True:
                data = api_get(base, token, path, {
                    "filters": json.dumps([{"status": {"operator": "o", "values": []}}]),
                    "pageSize": 100, "offset": offset, "sortBy": json.dumps([["dueDate", "asc"]]),
                })
                for wp in data["_embedded"]["elements"]:
                    items.append({
                        "id": wp["id"], "subject": wp["subject"],
                        "status": wp["_links"]["status"]["title"],
                        "project": project or wp["_links"]["project"]["title"],
                        "dueDate": wp.get("dueDate"),
                        "url": f"{base.rstrip('/')}/work_packages/{wp['id']}",
                    })
                if offset * 100 >= data["total"]:
                    break
                offset += 1
        today = datetime.date.today()
        soon = (today + datetime.timedelta(days=DUE_SOON_DAYS)).isoformat()
        t = today.isoformat()
        overdue = [i for i in items if i["dueDate"] and i["dueDate"] < t]
        due_soon = [i for i in items if i["dueDate"] and t <= i["dueDate"] <= soon]
        attention = []
        for i in (overdue + due_soon)[:ATTENTION_LIMIT]:
            data = api_get(base, token, f"/api/v3/work_packages/{i['id']}")
            desc = html.unescape(re.sub(r"<[^>]+>", " ", data.get("description") or ""))
            desc = re.sub(r"\s+", " ", desc).strip()[:400]
            attention.append({**i, "description": desc})
        short = lambda lst: [{"id": i["id"], "subject": i["subject"], "dueDate": i["dueDate"]} for i in lst]
        return {"role": role, "source": "openproject", "status": "ok",
                "total": len(items), "overdue": short(overdue), "due_soon": short(due_soon),
                "attention": attention, "items": items}
    except (urllib.error.URLError, KeyError, OSError) as exc:
        return {"role": role, "source": "openproject", "status": "error",
                "error": type(exc).__name__ + ": " + str(exc), "items": []}


def _slack(role):
    src = load_sources(role)
    creds = credentials(src, ("SLACK_TOKEN",))
    if not creds:
        return not_configured(role, "slack")
    token = creds["SLACK_TOKEN"]

    def call(method, params=None):
        data = http_json(SLACK_API + method, {"Authorization": "Bearer " + token}, params)
        if not data.get("ok"):
            raise OSError("slack " + method + ": " + str(data.get("error")))
        return data

    try:
        now = datetime.datetime.now(datetime.timezone.utc)
        cutoff = (now - datetime.timedelta(hours=HOURS)).timestamp()
        after = (now - datetime.timedelta(hours=HOURS + 2)).strftime("%Y-%m-%d")
        matches = call("search.messages", {"query": f"after:{after}", "count": 200})["messages"]["matches"]
        chans, cursor = {}, None
        for _ in range(3):
            params = {"types": "public_channel,private_channel,mpim", "limit": 200}
            if cursor:
                params["cursor"] = cursor
            data = call("conversations.list", params)
            for c in data["channels"]:
                chans[c["id"]] = {"name": c.get("name") or c.get("id"), "group": role}
            cursor = data.get("response_metadata", {}).get("next_cursor")
            if not cursor:
                break
        messages = []
        for m in matches:
            if float(m.get("ts") or 0) < cutoff:
                continue
            cid = (m.get("channel") or {}).get("id")
            info = chans.get(cid, {})
            messages.append({
                "from": m.get("username"),
                "channel": info.get("name") or (m.get("channel") or {}).get("name"),
                "group": info.get("group", role),
                "ts": m.get("ts"),
                "text": (m.get("text") or "")[:400],
                "url": m.get("permalink"),
            })
        return {"role": role, "source": "slack", "status": "ok", "hours": HOURS, "messages": messages}
    except (urllib.error.URLError, KeyError, OSError) as exc:
        return {"role": role, "source": "slack", "status": "error",
                "error": type(exc).__name__ + ": " + str(exc), "messages": []}


def _paperclip(role):
    url, key, cid = os.environ.get("PAPERCLIP_API_URL"), os.environ.get("PAPERCLIP_API_KEY"), os.environ.get("PAPERCLIP_COMPANY_ID")
    if not (url and key and cid):
        return not_configured(role, "paperclip")
    try:
        data = http_json(url.rstrip("/") + f"/api/companies/{cid}/agents", {"Authorization": "Bearer " + key})
        agents = data.get("agents") if isinstance(data, dict) else data
        rows = []
        for a in agents or []:
            state = a.get("state") or a.get("status") or a.get("executionState") or "unknown"
            rows.append({"name": a.get("name") or a.get("agentNameKey") or a.get("id"), "state": state})
        running = sum(1 for r in rows if r["state"] in ("running", "active", "in_progress", "working"))
        errors = sum(1 for r in rows if r["state"] in ("error", "failed"))
        return {"role": role, "source": "paperclip", "status": "ok",
                "agents": rows, "running": running, "errors": errors}
    except (urllib.error.URLError, KeyError, OSError) as exc:
        return {"role": role, "source": "paperclip", "status": "error",
                "error": type(exc).__name__ + ": " + str(exc), "agents": []}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", action="store_true", help="print the raw JSON (only mode)")
    ap.add_argument("--role", required=True)
    args = ap.parse_args()
    role = args.role
    out = {
        "role": role,
        "generated_at": datetime.datetime.now().astimezone().isoformat(timespec="minutes"),
        "openproject": _openproject(role),
        "slack": _slack(role),
        "paperclip": _paperclip(role),
        "github": _sub("github_read.py", role).get(role, {"status": "error"}),
        "kimai": _sub("kimai_read.py", role),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
