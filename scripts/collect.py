#!/usr/bin/env python3
"""Run every read-only connector and print one JSON document for the morning brief.

Usage: python3 scripts/collect.py
A source that is missing or failing is reported with its status, never skipped silently.
"""
import datetime
import json
import subprocess
import sys
from pathlib import Path

from common import list_roles, load_sources

HERE = Path(__file__).resolve().parent


def run(script, *args):
    proc = subprocess.run([sys.executable, str(HERE / script), *args], capture_output=True, text=True)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"status": "error", "error": (proc.stderr or proc.stdout).strip()[:300]}


def main():
    roles = list_roles()
    github = run("github_read.py")
    out = {"generated_at": datetime.datetime.now().astimezone().isoformat(timespec="minutes"), "roles": {}}
    for role in roles:
        src = load_sources(role)
        out["roles"][role] = {
            "openproject": run("op_read.py", role),
            "github": github.get(role, {"status": "error: no github data"}),
            "kimai": run("kimai_read.py", role),
            "slack": run("slack_read.py", role),
        }
    out["github_unassigned"] = github.get("unassigned", {})
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
