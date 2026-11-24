#!/usr/bin/env python3
"""Write to a GitHub PR and tell me on Slack. The only script that writes to GitHub.

Usage:
  py -X utf8 scripts/pr_act.py comment owner/repo#N --sha <headSha> --base <baseSha> --review-file F [--notify-file F] [--dry-run]
  py -X utf8 scripts/pr_act.py ack owner/repo#N --sha <headSha> --base <baseSha>    (re-checked after base moved, nothing to say)
  py -X utf8 scripts/pr_act.py approve owner/repo#N --confirmed-by-user [--body-file F] [--dry-run]
  py -X utf8 scripts/pr_act.py request-changes owner/repo#N --confirmed-by-user --body-file F [--dry-run]

Policy (memory: github-pr-review-policy):
  comment          allowed autonomously, review text follows the fixed format, then Slack gets a summary
  approve / request-changes   ONLY after the user said so for that PR; --confirmed-by-user is that statement.
                   Agents must never pass it on their own.
Only repos whose owner is in units/*/sources.json github.owners are accepted; Slack goes to that role's channel only.
"""
import sys

from pr_common import gh, load_state, parse_ref, require_role, save_state, slack_notify


def arg(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip()


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("comment", "ack", "approve", "request-changes"):
        sys.exit(__doc__)
    action, (repo, number) = sys.argv[1], parse_ref(sys.argv[2])
    role = require_role(repo)
    dry = "--dry-run" in sys.argv
    key = repo + "#" + str(number)
    if action == "ack":  # reviewed again against the new base, nothing worth saying: record it, write nothing anywhere
        if not arg("--sha") or not arg("--base"):
            sys.exit("ack needs --sha and --base")
        state = load_state()
        if state is not None and not dry:
            rec = state["prs"].setdefault(key, {"role": role})
            rec["reviewed_sha"], rec["reviewed_base"] = arg("--sha"), arg("--base")
            save_state(state)
        print("ack " + key)
        return
    if action != "comment" and "--confirmed-by-user" not in sys.argv:
        sys.exit("refused: " + action + " needs the user's explicit go-ahead for this PR (--confirmed-by-user)")

    if action == "comment":
        sha, review_file = arg("--sha"), arg("--review-file")
        if not sha or not review_file:
            sys.exit("comment needs --sha and --review-file")
        body = read(review_file)
        if not body:
            sys.exit("review file is empty")
        flag, label = "--comment", "đã comment"
    else:
        body_file = arg("--body-file")
        body = read(body_file) if body_file else ""
        if action == "request-changes" and not body:
            sys.exit("request-changes needs --body-file")
        flag, label = ("--approve", "đã approve") if action == "approve" else ("--request-changes", "đã request changes")

    if dry:
        print("dry-run: gh pr review " + str(number) + " -R " + repo + " " + flag + " (" + str(len(body)) + " chars)")
        return
    cmd = ["pr", "review", str(number), "-R", repo, flag]
    if body:
        cmd += ["--body", body]
    gh(cmd)
    state = load_state()
    if state is not None:
        rec = state["prs"].setdefault(key, {"role": role})
        if action == "comment":
            rec["reviewed_sha"] = sha
            if arg("--base"):
                rec["reviewed_base"] = arg("--base")
        else:
            rec["approve_by_user" if action == "approve" else "changes_requested_by_user"] = True
        save_state(state)
    print(label + " " + key)

    notify = arg("--notify-file")
    if notify:
        ok, detail = slack_notify(role, read(notify))
        print("slack #" + ("ok" if ok else "FAILED") + ": " + detail)
    elif action != "comment":
        ok, detail = slack_notify(role, ":white_check_mark: " + label.capitalize() + " <https://github.com/" + repo + "/pull/"
                                  + str(number) + "|" + key + "> theo yêu cầu của bạn.")
        print("slack " + ("ok" if ok else "FAILED") + ": " + detail)


if __name__ == "__main__":
    main()
