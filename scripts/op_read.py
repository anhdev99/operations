#!/usr/bin/env python3
"""Read open work packages assigned to me from a role's OpenProject. Read-only.

Usage: python3 scripts/op_read.py <role>
Writes units/<role>/snapshot/op.json and prints the same JSON.
"""
import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

from common import credentials, load_sources, not_configured, ssl_context, write_snapshot

PAGE_SIZE = 100
RELATIONS = ("assignee", "responsible", "author", "watcher")


def api_get(base, token, path, params=None):
    url = base.rstrip("/") + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    auth = base64.b64encode(f"apikey:{token}".encode()).decode()
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    with urllib.request.urlopen(req, timeout=30, context=ssl_context()) as resp:
        return json.load(resp)


def fetch_relation(base, token, project, relation):
    filters = [
        {"status": {"operator": "o", "values": []}},
        {relation: {"operator": "=", "values": ["me"]}},
    ]
    items, offset = [], 1
    while True:
        data = api_get(
            base, token, (f"/api/v3/projects/{project}/work_packages" if project else "/api/v3/work_packages"),
            {"filters": json.dumps(filters), "pageSize": PAGE_SIZE, "offset": offset,
             "sortBy": json.dumps([["dueDate", "asc"]])},
        )
        for wp in data["_embedded"]["elements"]:
            items.append({
                "id": wp["id"],
                "subject": wp["subject"],
                "type": wp["_links"]["type"]["title"],
                "status": wp["_links"]["status"]["title"],
                "project": project or wp["_links"]["project"]["title"],
                "relation": relation,
                "dueDate": wp.get("dueDate"),
                "updatedAt": wp.get("updatedAt"),
                "url": f"{base.rstrip('/')}/work_packages/{wp['id']}",
            })
        if offset * PAGE_SIZE >= data["total"]:
            return items
        offset += 1


def fetch_project(base, token, project):
    """Open work packages related to me, merged by id; 'relations' lists why each one is here."""
    merged = {}
    for relation in RELATIONS:
        for item in fetch_relation(base, token, project, relation):
            entry = merged.setdefault(item["id"], {**item, "relations": []})
            entry["relations"].append(relation)
    for entry in merged.values():
        del entry["relation"]
    return list(merged.values())


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    role = sys.argv[1]
    src = load_sources(role)
    cfg = src.get("openproject") or {}
    creds = credentials(src, ("OP_BASE_URL", "OP_TOKEN"))
    if not creds:
        print(json.dumps(not_configured(role, "openproject"), ensure_ascii=False, indent=2))
        return
    try:
        base, token = creds["OP_BASE_URL"], creds["OP_TOKEN"]
        items = []
        for project in cfg.get("projects") or [None]:
            items += fetch_project(base, token, project)
        items.sort(key=lambda i: (i["dueDate"] is None, i["dueDate"] or ""))
        result = {"role": role, "source": "openproject", "status": "ok", "items": items}
    except (urllib.error.URLError, KeyError, OSError) as exc:
        result = {"role": role, "source": "openproject", "status": "error",
                  "error": type(exc).__name__ + ": " + str(exc), "items": []}
    write_snapshot(role, "op.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "error":
        sys.exit(1)


if __name__ == "__main__":
    main()
