#!/usr/bin/env python3
"""Post the daily report for one role to its Slack channel. Two messages:
1) the filled summary, 2) the OpenProject table (per project + urgent list).

Usage: py scripts/post_summary.py <summary.json> --role <role>
"""
import argparse
import datetime
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import credentials, load_sources, ssl_context

SLACK_API = "https://slack.com/api/"


def post(token, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(SLACK_API + "chat.postMessage", data=body, method="POST",
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30, context=ssl_context()) as resp:
        return json.load(resp)


def render_summary(role, s, now):
    lines = [f"*Báo cáo {role} · {now.strftime('%d/%m/%Y %H:%M')}*", ""]
    if s.get("needs_you"):
        lines += ["*Cần bạn:*"] + [f"• {t}" for t in s["needs_you"]] + [""]
    if s.get("highlights"):
        lines += ["*Điểm nổi bật:*"]
        lines += [f"• #{h.get('channel', '')} ({h.get('group', '')}): {h.get('text', '')}" for h in s["highlights"]]
        lines.append("")
    if s.get("people"):
        lines += ["*Mọi người:*"]
        for p in s["people"]:
            lines.append(f"• *{p.get('name', '')}* (#{p.get('channel', '')}) — đang làm: {p.get('doing', '—')} · đã báo: {p.get('reported', '—')}")
        lines.append("")
    if s.get("agents"):
        lines += [f"*Agents:* {s['agents']}", ""]
    if s.get("links"):
        lines += ["*Link:*"] + [f"• {l.get('label', 'link')} <{l.get('url', '')}>" for l in s["links"]] + [""]
    if s.get("warnings"):
        lines += ["*Cảnh báo:*"] + [f"• {w}" for w in s["warnings"]]
    return "\n".join(lines)


def render_openproject(role, op, tickets):
    notes = {t.get("id"): t.get("summary", "") for t in tickets or []}
    lines = [f"*OpenProject {role} · bảng theo dự án*", ""]
    if op.get("status") == "ok":
        by_project = {}
        for i in op.get("items", []):
            by_project.setdefault(i.get("project", "?"), 0)
            by_project[i.get("project", "?")] += 1
        for name in sorted(by_project):
            lines.append(f"• {name}: {by_project[name]} việc mở")
        lines.append("")
        lines.append(f"Tổng {op.get('total', 0)} việc mở · {len(op.get('overdue', []))} quá hạn · {len(op.get('due_soon', []))} sắp đến hạn")
        urgent = op.get("overdue", []) + op.get("due_soon", [])
        if urgent:
            today = datetime.date.today().isoformat()
            lines += ["", "*Việc gấp:*"]
            for i in sorted(urgent, key=lambda x: x["dueDate"] or ""):
                d = i["dueDate"]
                days = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(d)).days if d < today else 0
                tag = f"quá hạn {days} ngày" if d < today else f"hạn {d}"
                lines.append(f"• #{i['id']} {i.get('subject', '')} — {tag} <{i.get('url', '')}>")
                note = notes.get(i["id"])
                if note:
                    lines.append(f"  {note}")
        else:
            lines += ["", "Không có việc quá hạn hoặc sắp đến hạn."]
    else:
        lines.append(f"Lỗi nguồn OpenProject: {op.get('error', op.get('status'))}")
    return "\n".join(lines)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("summary")
    ap.add_argument("--role", required=True)
    args = ap.parse_args()
    role = args.role
    summary = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    s = next((r for r in summary.get("roles", []) if r.get("role") == role), None)
    if s is None:
        print(f"lỗi: tệp summary không có role '{role}'")
        sys.exit(1)
    creds = credentials(load_sources(role), ("SLACK_TOKEN",))
    if not creds:
        print(f"lỗi: SLACK_TOKEN chưa cấu hình cho role '{role}' (env_file trong sources.json)")
        sys.exit(1)
    channel = f"#{role}-bao-cao"  # ponytail: fixed per-role naming, add channel map when a role's channel differs
    from report import _openproject
    op = _openproject(role)
    now = datetime.datetime.now()
    for text in (render_summary(role, s, now), render_openproject(role, op, s.get("tickets"))):
        data = post(creds["SLACK_TOKEN"], {"channel": channel, "text": text})
        if not data.get("ok"):
            print(f"{channel}: lỗi {data.get('error')}")
            sys.exit(1)
        print(f"{channel}: ok")


if __name__ == "__main__":
    main()
