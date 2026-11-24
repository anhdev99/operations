#!/usr/bin/env python3
"""Create and inspect Paperclip tickets through the REST API.

Why: `paperclipai issue create` on Windows cuts multi-line arguments at the first newline, so descriptions,
assignee and project were silently lost. This script sends the description from a file as JSON.

Usage:
  py -X utf8 scripts/pc_task.py new --company HOMA --project anhdev99 --assignee Friday --title "..." --file desc.md
        [--parent HOMA-28] [--blocked-by HOMA-29,HOMA-30] [--status todo|backlog] [--priority medium]
  py -X utf8 scripts/pc_task.py show HOMA-28          (ticket, children, who holds what, what blocks what)

Company is the issue prefix (TCH, PHD, LUC, HOMA). Agents and projects are matched by name, case-insensitive.
Only writes tickets in the local Paperclip; it never touches GitHub, Slack or OpenProject.
"""
import json
import sys
import urllib.request

import common  # noqa: F401  (UTF-8 stdout on Windows)

API = "http://127.0.0.1:3100/api"


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode("utf-8") if body is not None else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def company_by_prefix(prefix):
    for c in call("GET", "/companies"):
        if c.get("issuePrefix", "").upper() == prefix.upper():
            return c
    sys.exit("no company with prefix " + prefix)


def issues_of(company_id):
    data = call("GET", "/companies/" + company_id + "/issues?limit=200")
    return data if isinstance(data, list) else data.get("issues", data)


def find_issue(identifier):
    prefix = identifier.split("-")[0]
    company = company_by_prefix(prefix)
    for i in issues_of(company["id"]):
        if i["identifier"].upper() == identifier.upper():
            return company, i
    sys.exit("issue not found: " + identifier)


def new():
    company = company_by_prefix(arg("--company", ""))
    cid = company["id"]
    agents = {a["name"].lower(): a["id"] for a in call("GET", "/companies/" + cid + "/agents")}
    projects = {p["name"].lower(): p["id"] for p in call("GET", "/companies/" + cid + "/projects")}
    assignee, project = arg("--assignee", "").lower(), arg("--project", "").lower()
    if assignee not in agents:
        sys.exit("agent not found: " + assignee + " (have: " + ", ".join(sorted(agents)) + ")")
    if project and project not in projects:
        sys.exit("project not found: " + project + " (have: " + ", ".join(sorted(projects)) + ")")
    with open(arg("--file"), encoding="utf-8") as fh:
        description = fh.read().strip()
    body = {"title": arg("--title"), "description": description, "assigneeAgentId": agents[assignee],
            "status": arg("--status", "todo"), "priority": arg("--priority", "medium")}
    if project:
        body["projectId"] = projects[project]
    if arg("--parent"):
        body["parentId"] = find_issue(arg("--parent"))[1]["id"]
    if arg("--blocked-by"):
        body["blockedByIssueIds"] = [find_issue(x.strip())[1]["id"] for x in arg("--blocked-by").split(",") if x.strip()]
    issue = call("POST", "/companies/" + cid + "/issues", body)
    chk = call("GET", "/issues/" + issue["id"])
    ok = (chk.get("assigneeAgentId") == agents[assignee] and len(chk.get("description") or "") >= len(description) - 2
          and (not project or chk.get("projectId") == projects[project]))
    print(chk["identifier"], chk["status"], "->", assignee, "| verified:", ok,
          "| blockedBy:", [b["identifier"] for b in chk.get("blockedBy", [])])
    if not ok:
        sys.exit("created, but the saved ticket does not match what was sent; check it in the dashboard")


def show():
    company, top = find_issue(sys.argv[2])
    cid = company["id"]
    names = {a["id"]: a["name"] for a in call("GET", "/companies/" + cid + "/agents")}
    everything = issues_of(cid)

    def line(i, indent):
        full = call("GET", "/issues/" + i["id"])
        waits = ", ".join(b["identifier"] + "(" + b["status"] + ")" for b in full.get("blockedBy", []))
        print("  " * indent + i["identifier"] + " [" + i["status"] + "] " + names.get(i.get("assigneeAgentId"), "-") + " | "
              + i["title"][:70] + (" | waits for " + waits if waits else ""))

    line(top, 0)
    for child in sorted((x for x in everything if x.get("parentId") == top["id"]), key=lambda x: int(x["identifier"].split("-")[1])):
        line(child, 1)


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("new", "show"):
        sys.exit(__doc__)
    new() if sys.argv[1] == "new" else show()
