#!/usr/bin/env python3
"""Poll GitHub for PRs that need my review, per company, and hand new ones to Paperclip.

Usage: py -X utf8 scripts/pr_watch.py [--baseline] [--dry-run] [--no-trigger]

Scope per role (units/<role>/sources.json -> github):
  watch = review_requested : open PRs where review is requested from me, in the owners' repos
  watch = all_open         : every open PR by someone else (personal repos: nobody assigns review to yourself)
Bots (Dependabot...), drafts and my own PRs are tracked but never queued.
For each PR that is new, has new commits (headRefOid changed), or whose base branch moved on files the PR touches
(reason: new | updated | base_changed), and a separate warning when the PR starts to conflict with its base: one Slack message in the role's report
channel, an entry in reports/pr-queue-<role>.json, and the role's "Review PR được giao" routine is started.

--baseline : record everything open right now as already handled (no Slack, no routine). Required for the first run.
--dry-run  : print what would happen, change nothing.
Designed to run every ~10 minutes without an LLM; it is cheap and only calls out when something changed.
"""
import datetime
import json
import sys

from common import ROOT
from pr_common import (base_drift, gh_json, load_state, me, parse_ref, save_state, slack_notify, trigger_review_routine,
                       watch_config)

FIELDS = "repository,number,title,author,url,updatedAt,isDraft"
FIELDS_VIEW = "title,author,url,updatedAt,isDraft"


def search(owner, mode):
    args = ["search", "prs", "--owner", owner, "--state", "open", "--limit", "100", "--json", FIELDS]
    if mode == "review_requested":
        args.insert(2, "--review-requested=@me")
    return gh_json(args)


def search_own(owner):
    """Open PRs authored by my account (agents push with it); agent branches among them are reported to me."""
    return gh_json(["search", "prs", "--owner", owner, "--author=@me", "--state", "open", "--limit", "100", "--json", FIELDS])


def head_info(repo, number):
    return gh_json(["pr", "view", str(number), "-R", repo, "--json",
                    "headRefOid,headRefName,baseRefOid,baseRefName,mergeable,additions,deletions,changedFiles,isDraft,files"])


NL = "\n"


def slack_text(item, role, kind):
    link = "<" + item["url"] + "|" + item["repo"] + "#" + str(item["number"]) + ">"
    if kind == "base_changed":
        files = ", ".join("`" + f.rsplit("/", 1)[-1] + "`" for f in item["drift_files"][:5])
        return (":arrows_counterclockwise: *Nhánh gốc vừa đổi, chạm vào file của PR* — " + link + NL + item["title"] + NL
                + "File bị ảnh hưởng: " + files + NL + "Mình đang xem lại PR so với nhánh gốc mới trong Paperclip.")
    verb = "cập nhật thêm commit" if kind == "updated" else "mới"
    return (":inbox_tray: *PR " + verb + " cần review* — " + link + NL + item["title"] + NL
            + "Người tạo: `" + item["author"] + "` · +" + str(item["additions"]) + "/-" + str(item["deletions"])
            + " · " + str(item["changedFiles"]) + " file" + NL + "Mình đang review trong Paperclip, xong sẽ báo nội dung comment.")


def agent_pr_text(pr, info):
    base = info["baseRefName"]
    text = (":package: *Agent đã mở PR, chờ bạn duyệt merge vào `" + base + "`* — <" + pr["url"] + "|" + pr["repository"]["nameWithOwner"]
            + "#" + str(pr["number"]) + ">" + NL + pr["title"] + NL + "Nhánh `" + info["headRefName"] + "` → `" + base + "` · +"
            + str(info["additions"]) + "/-" + str(info["deletions"]) + " · " + str(info["changedFiles"]) + " file" + NL
            + "Chưa merge. Kiểm tra review độc lập của Reviewer trong ticket trước khi quyết định.")
    if base != "develop":
        text += NL + ":warning: PR nhắm vào `" + base + "`, không phải `develop`. Luật hiện hành: mọi PR của agent phải nhắm vào `develop`."
    return text


def merged_text(rec, view):
    who = (view.get("mergedBy") or {}).get("login") or "?"
    return (":information_source: *PR của agent đã được merge vào `" + view["baseRefName"] + "`* — <" + view["url"] + "|" + rec["key"] + ">"
            + NL + rec.get("title", "") + NL + "Tài khoản merge: `" + who + "` (tài khoản này dùng chung với agent)."
            + NL + "Nếu không phải bạn bấm merge thì một agent đã tự merge, trái với luật \"chỉ board được merge\".")


def conflict_text(item, base):
    return (":warning: *PR đang xung đột với `" + base + "`* — <" + item["url"] + "|" + item["repo"] + "#" + str(item["number"]) + ">"
            + NL + item["title"] + NL + "Người tạo: `" + item["author"] + "` cần cập nhật nhánh trước khi review tiếp.")


def main():
    baseline, dry, no_trigger = "--baseline" in sys.argv, "--dry-run" in sys.argv, "--no-trigger" in sys.argv
    state = load_state()
    if state is None and not baseline:
        sys.exit("no state yet: run once with --baseline so existing PRs are not all reviewed and announced")
    state = state or {"prs": {}}
    known = state["prs"]
    mine = me()
    seen, report = set(), []
    new_roles = {}

    for role, cfg in watch_config().items():
        queue = []
        prs = []
        for owner in cfg["owners"]:
            try:
                prs += search(owner, cfg["watch"])
            except RuntimeError as exc:
                report.append(role + ": ERROR " + str(exc))
        listed = {p["repository"]["nameWithOwner"] + "#" + str(p["number"]) for p in prs}
        if cfg["watch"] != "all_open":  # review_requested never lists my own PRs, so add them for agent-branch reports
            for owner in cfg["owners"]:
                try:
                    for p in search_own(owner):
                        k = p["repository"]["nameWithOwner"] + "#" + str(p["number"])
                        if k not in listed:
                            listed.add(k)
                            prs.append(p)
                except RuntimeError as exc:
                    report.append(role + ": ERROR (own PRs) " + str(exc))
        for key, rec in list(known.items()):  # a reviewed PR drops out of review-requested; keep following it while it is open
            if rec.get("role") != role or key in listed or rec.get("skip") or not rec.get("reviewed_sha") or rec.get("approve_by_user"):
                continue
            repo, number = parse_ref(key)
            try:
                view = gh_json(["pr", "view", str(number), "-R", repo, "--json", "state," + FIELDS_VIEW])
            except RuntimeError:
                continue
            if view["state"] == "OPEN":
                prs.append({"repository": {"nameWithOwner": repo}, "number": number, **{k: view[k] for k in FIELDS_VIEW.split(",")}})
        for pr in prs:
                repo = pr["repository"]["nameWithOwner"]
                key = repo + "#" + str(pr["number"])
                seen.add(key)
                rec = known.get(key, {})
                is_bot = bool(pr["author"].get("is_bot")) or pr["author"]["login"].endswith("[bot]")
                if is_bot or pr["author"]["login"] == mine:
                    rec = {**rec, "role": role, "skip": "bot" if is_bot else "own"}
                    known[key] = rec
                    if not is_bot:  # my account also opens PRs for agents: tell me once so I can decide on the merge
                        own = head_info(repo, pr["number"])
                        rec["agent_pr"] = own["headRefName"].startswith("agent/")
                        rec["key"], rec["title"] = key, pr["title"]
                        if baseline:
                            rec["notified_sha"] = own["headRefOid"]
                        elif own["headRefName"].startswith("agent/") and not own["isDraft"] and rec.get("notified_sha") != own["headRefOid"]:
                            ok, detail = slack_notify(role, agent_pr_text(pr, own), dry)
                            report.append(role + ": agent PR " + key + " -> slack " + detail)
                            if ok and not dry:
                                rec["notified_sha"] = own["headRefOid"]
                    continue
                info = head_info(repo, pr["number"])
                rec.update({"role": role, "sha": info["headRefOid"], "base_sha": info["baseRefOid"], "updatedAt": pr["updatedAt"],
                            "title": pr["title"], "additions": info["additions"], "deletions": info["deletions"],
                            "changedFiles": info["changedFiles"], "draft": info["isDraft"], "mergeable": info["mergeable"]})
                rec.pop("skip", None)
                known[key] = rec
                sha, base = rec["sha"], rec["base_sha"]
                if baseline:
                    rec["reviewed_sha"] = rec["notified_sha"] = sha
                    rec["reviewed_base"] = rec["notified_base"] = base
                    if info["mergeable"] == "CONFLICTING":
                        rec["conflict_notified"] = sha[:7] + base[:7]
                    continue
                if info["isDraft"]:
                    continue
                item = {"repo": repo, "number": pr["number"], "title": pr["title"], "url": pr["url"], "sha": sha, "base_sha": base,
                        "author": pr["author"]["login"], "additions": info["additions"], "deletions": info["deletions"],
                        "changedFiles": info["changedFiles"], "reason": None}
                kind = None
                if rec.get("reviewed_sha") != sha:
                    kind = "updated" if rec.get("notified_sha") else "new"
                elif not rec.get("reviewed_base"):
                    rec["reviewed_base"] = base  # state from before base tracking: start from now
                elif rec["reviewed_base"] != base:
                    drift = base_drift(repo, rec["reviewed_base"], base, [f["path"] for f in info["files"]])
                    if drift["overlapping_files"]:
                        kind = "base_changed"
                        item["drift_files"] = drift["overlapping_files"]
                    else:
                        rec["reviewed_base"] = base  # base moved but nothing the PR touches
                if kind:
                    item["reason"] = kind
                    queue.append(item)
                    marker = ("notified_base", base) if kind == "base_changed" else ("notified_sha", sha)
                    if rec.get(marker[0]) != marker[1]:
                        ok, detail = slack_notify(role, slack_text(item, role, kind), dry)
                        report.append(role + ": " + kind + " " + key + " -> slack " + detail)
                        if ok and not dry:
                            rec[marker[0]] = marker[1]
                        new_roles[role] = True
                if info["mergeable"] == "CONFLICTING":
                    tag = sha[:7] + base[:7]
                    if rec.get("conflict_notified") != tag:
                        ok, detail = slack_notify(role, conflict_text(item, info["baseRefName"]), dry)
                        report.append(role + ": conflict " + key + " -> slack " + detail)
                        if ok and not dry:
                            rec["conflict_notified"] = tag
                elif info["mergeable"] == "MERGEABLE":
                    rec.pop("conflict_notified", None)
        queue_path = ROOT / "reports" / ("pr-queue-" + role + ".json")
        if not dry:
            queue_path.parent.mkdir(parents=True, exist_ok=True)
            queue_path.write_text(json.dumps({"role": role, "generated_at": datetime.datetime.now().isoformat(timespec="seconds"),
                                              "items": queue}, ensure_ascii=False, indent=2), encoding="utf-8")
        report.append(role + ": " + str(len(queue)) + " PR chờ review")

    for key in [k for k in known if k not in seen]:  # closed or merged
        rec = known[key]
        if rec.get("agent_pr") and not baseline:  # tell me when an agent PR was merged, so an unauthorised merge is visible
            try:
                repo, number = parse_ref(key)
                view = gh_json(["pr", "view", str(number), "-R", repo, "--json", "state,mergedBy,baseRefName,url"])
                if view["state"] == "MERGED":
                    ok, detail = slack_notify(rec["role"], merged_text(rec, view), dry)
                    report.append(rec["role"] + ": agent PR merged " + key + " -> slack " + detail)
            except (RuntimeError, KeyError):
                pass
        if not dry:
            del known[key]
    if not dry:
        save_state(state)
    if baseline:
        report.append("baseline: " + str(len(seen)) + " PR ghi nhận là đã xử lý")
    elif new_roles and not no_trigger:
        for role in new_roles:
            report.append(role + ": " + ("(dry-run) would start routine" if dry else trigger_review_routine(role)))
    print("\n".join(report))


if __name__ == "__main__":
    main()
