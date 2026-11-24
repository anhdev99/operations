#!/usr/bin/env python3
"""Build the daily report and post it to the personal Slack workspace.

Usage: python3 scripts/report.py [--dry-run] [--role digital-transformation]
       python3 scripts/report.py --raw [--role <role>]   (full JSON for a model to summarise; posts nothing)
Now: Slack digest + agent status for the digital-transformation role.
Posts the detail to the role's channel and a one-screen summary to #bao-cao.
"""
import datetime
import sys

from common import load_sources
from paperclip_status import status as paperclip_status
from slack_digest import digest
from slack_post import post

ROLES = {  # role -> (channel in the personal workspace, Paperclip prefix, display name)
    "digital-transformation": ("dthu-bao-cao", "TCH", "Tổ chuyển đổi số"),
    "lucidtech": ("lucidtech-bao-cao", "LUC", "LucidTech"),
    "phd-group": ("phd-group-bao-cao", "PHD", "PHD Group"),
}
STATUS_ICON = {"idle": "🟢 rảnh", "running": "🔵 đang chạy", "paused": "⏸ tạm dừng", "error": "🔴 lỗi"}


def role_block(role):
    channel, prefix, title = ROLES[role]
    now = datetime.datetime.now().strftime("%d/%m %H:%M")
    lines = ["*%s* · báo cáo %s" % (title, now), ""]

    d = digest(role)
    lines.append("*Slack (24h qua)*")
    if d["status"] == "not_configured":
        lines.append("• Chưa cấu hình (thiếu SLACK_TOKEN).")
    elif d["status"] == "error":
        lines.append("• ⚠ Lỗi đọc Slack: " + d["error"])
    elif not d["channels"]:
        lines.append("• Không có tin nhắn mới.")
    else:
        lines.append("• %d tin ở %d kênh" % (d["total"], len(d["channels"])))
        for ch in d["channels"]:
            lines.append("")
            lines.append("*%s* — %d tin (%s)" % (ch["channel"], ch["count"], ", ".join(ch["people"][:5])))
            for m in ch["latest"]:
                link = " <%s|mở>" % m["url"] if m.get("url") else ""
                lines.append("   ◦ _%s_: %s%s" % (m["from"], m["text"], link))

    lines += ["", "*Agent trong Paperclip*"]
    p = paperclip_status([prefix])
    if p["status"] == "error":
        lines.append("• ⚠ " + p["error"])
    for c in p["companies"]:
        for a in c["agents"]:
            lines.append("• %s (%s): %s" % (a["name"], a["role"], STATUS_ICON.get(a["status"], a["status"])))
    return channel, title, d, "\n".join(lines)


SOON_DAYS = 3
ATTENTION_MAX = 10


def op_summary(role):
    """Deterministic OpenProject digest: counts per project plus the overdue / due-soon items. Read-only."""
    import collections
    import op_read
    result = op_read.read(role)
    if result["status"] != "ok":
        return {"status": result["status"], "error": result.get("error")}
    today = datetime.date.today()
    projects = collections.OrderedDict()
    attention, no_due = [], 0
    for it in result["items"]:
        p = projects.setdefault(it["project"], {"name": it["project"], "total": 0, "overdue": 0, "soon": 0})
        p["total"] += 1
        if not it.get("dueDate"):
            no_due += 1
            continue
        days = (datetime.date.fromisoformat(it["dueDate"]) - today).days
        if days < 0:
            p["overdue"] += 1
        elif days <= SOON_DAYS:
            p["soon"] += 1
        else:
            continue
        attention.append({"id": it["id"], "subject": it["subject"], "project": it["project"], "due": it["dueDate"],
                          "days": days, "url": it["url"], "relations": it["relations"],
                          "assignee": it.get("assignee"), "responsible": it.get("responsible"), "author": it.get("author"),
                          "description": " ".join((it.get("description") or "").split())[:600]})
    attention.sort(key=lambda a: a["days"])  # most overdue first
    return {"status": "ok", "total": len(result["items"]), "no_due": no_due,
            "overdue": sum(p["overdue"] for p in projects.values()),
            "soon": sum(p["soon"] for p in projects.values()),
            "soon_days": SOON_DAYS,
            "projects": sorted(projects.values(), key=lambda p: (-p["overdue"], -p["soon"], -p["total"])),
            "attention": attention[:ATTENTION_MAX], "attention_total": len(attention)}


def raw():
    """Full data for a model to summarise. Prints JSON only; posts nothing."""
    import json
    out = {"generated_at": datetime.datetime.now().isoformat(timespec="minutes"), "roles": []}
    only = sys.argv[sys.argv.index("--role") + 1] if "--role" in sys.argv else None
    for role, (channel, prefix, title) in ROLES.items():
        if only and role != only:
            continue  # one company's agent must only see that company's data
        slack = digest(role, full=True)
        # Topic groups come from units/<role>/sources.json -> slack_groups, so group names stay stable between runs.
        groups = load_sources(role).get("slack_groups", {})
        by_channel = {c: g for g, members in groups.items() for c in members}
        for ch in slack.get("channels", []):
            ch["group"] = by_channel.get(ch["channel"], "Khác")
        out["roles"].append({"role": role, "title": title, "post_to": channel,
                             "slack": slack, "paperclip": paperclip_status([prefix]),
                             "openproject": op_summary(role)})
    print(json.dumps(out, ensure_ascii=False, indent=1))


def main():
    if "--raw" in sys.argv:
        return raw()
    dry = "--dry-run" in sys.argv
    roles = [sys.argv[sys.argv.index("--role") + 1]] if "--role" in sys.argv else list(ROLES)
    failed = False
    for role in roles:
        channel, title, d, text = role_block(role)
        ok, detail = post(channel, text, dry)
        print("#%s: %s" % (channel, detail)); failed |= not ok
        n = d.get("total", "?")
        summary = "*Tóm tắt %s*: %s tin Slack trong 24h qua. Chi tiết ở #%s." % (title, n, channel)
        if d["status"] != "ok":
            summary += " ⚠ Nguồn Slack: " + d["status"]
        ok, detail = post("00-tong-hop", summary, dry)
        print("#00-tong-hop: %s" % detail); failed |= not ok
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
