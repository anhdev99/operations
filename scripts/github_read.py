#!/usr/bin/env python3
"""Read PRs and issues that concern me from GitHub via the gh CLI. Read-only.

Usage: python3 scripts/github_read.py [<role>]
Items are assigned to a role by repository owner (github.owners in sources.json);
anything else is reported under role "unassigned". With <role>, only that role is printed.
"""
import json
import subprocess
import sys

from common import list_roles, load_sources, write_snapshot

QUERIES = {
    "review_requested": ["search", "prs", "--review-requested=@me", "--state=open"],
    "my_prs": ["search", "prs", "--author=@me", "--state=open"],
    "assigned_issues": ["search", "issues", "--assignee=@me", "--state=open"],
}
FIELDS = "repository,title,url,updatedAt,number"


def gh_json(args):
    out = subprocess.run(["gh", *args, "--json", FIELDS, "--limit", "100"],
                         capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    owners = {}
    for role in list_roles():
        for owner in (load_sources(role).get("github") or {}).get("owners", []):
            owners[owner.lower()] = role
    result = {r: {"source": "github", "status": "ok", **{k: [] for k in QUERIES}} for r in [*list_roles(), "unassigned"]}
    try:
        for kind, args in QUERIES.items():
            for item in gh_json(args):
                owner = item["repository"]["nameWithOwner"].split("/")[0].lower()
                role = owners.get(owner, "unassigned")
                result[role][kind].append({
                    "repo": item["repository"]["nameWithOwner"], "number": item["number"],
                    "title": item["title"], "url": item["url"], "updatedAt": item["updatedAt"],
                })
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        detail = getattr(exc, "stderr", "") or str(exc)
        for role in result:
            result[role]["status"] = "error: " + detail.strip()[:200]
    for role, data in result.items():
        if role != "unassigned":
            write_snapshot(role, "github.json", data)
    print(json.dumps(result if only is None else {only: result[only]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
