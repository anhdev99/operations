#!/usr/bin/env python3
"""Print everything a reviewer needs about one PR. Read-only.

Usage: py -X utf8 scripts/pr_fetch.py owner/repo#number [--max-diff 150000]
Output: JSON with metadata, files, CI checks, existing reviews/comments and the diff (truncated if huge).
`sha`/`base_sha` are the commits that were read; pass them to pr_act.py comment --sha/--base so a later push or a base change is noticed.
base_drift lists commits that landed on the base branch since the PR branched and touch the PR's files.
Only repos whose owner is configured in units/*/sources.json are allowed.
"""
import json
import sys

from pr_common import base_drift, gh, gh_json, parse_ref, require_role

MAX_BODY = 4000
MAX_COMMENT = 800


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    repo, number = parse_ref(sys.argv[1])
    role = require_role(repo)
    max_diff = int(sys.argv[sys.argv.index("--max-diff") + 1]) if "--max-diff" in sys.argv else 150000
    pr = gh_json(["pr", "view", str(number), "-R", repo, "--json",
                  "title,author,body,baseRefName,headRefName,headRefOid,additions,deletions,changedFiles,files,"
                  "statusCheckRollup,reviews,comments,isDraft,mergeable,mergeStateStatus,baseRefOid,state,url"])
    diff = gh(["pr", "diff", str(number), "-R", repo])
    drift = base_drift(repo, pr["headRefOid"], pr["baseRefName"], [f["path"] for f in pr["files"]])
    out = {
        "role": role, "repo": repo, "number": number, "url": pr["url"], "state": pr["state"], "draft": pr["isDraft"],
        "title": pr["title"], "author": pr["author"]["login"], "base": pr["baseRefName"], "head": pr["headRefName"],
        "sha": pr["headRefOid"], "base_sha": pr["baseRefOid"], "mergeable": pr["mergeable"],
        "merge_state": pr["mergeStateStatus"], "base_drift": drift,
        "size": {"additions": pr["additions"], "deletions": pr["deletions"], "files": pr["changedFiles"]},
        "body": (pr["body"] or "")[:MAX_BODY],
        "files": [{"path": f["path"], "additions": f["additions"], "deletions": f["deletions"]} for f in pr["files"]],
        "checks": [{"name": c.get("name") or c.get("context"), "result": c.get("conclusion") or c.get("state")}
                   for c in pr["statusCheckRollup"]],
        "reviews": [{"by": r["author"]["login"], "state": r["state"], "body": (r.get("body") or "")[:MAX_COMMENT]}
                    for r in pr["reviews"]],
        "comments": [{"by": c["author"]["login"], "body": (c.get("body") or "")[:MAX_COMMENT]} for c in pr["comments"]],
        "diff_truncated": len(diff) > max_diff,
        "diff": diff[:max_diff],
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
