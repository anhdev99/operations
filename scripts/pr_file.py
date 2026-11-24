#!/usr/bin/env python3
"""Read one file from a repo at a given ref (commit sha or branch) through the GitHub API. Read-only.

Usage: py -X utf8 scripts/pr_file.py owner/repo <ref> <path> [--max 60000]
Use the PR's `sha` for the proposed code and the base branch name (e.g. develop) for the current base,
instead of a local clone that may be out of date. Only repos in units/*/sources.json github.owners are allowed.
"""
import sys

from pr_common import gh, require_role


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    repo, ref, path = sys.argv[1:4]
    require_role(repo)
    limit = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 60000
    text = gh(["api", "repos/" + repo + "/contents/" + path + "?ref=" + ref, "-H", "Accept: application/vnd.github.raw"])
    sys.stdout.write(text[:limit])
    if len(text) > limit:
        sys.stdout.write("\n[truncated at " + str(limit) + " chars of " + str(len(text)) + "]\n")


if __name__ == "__main__":
    main()
