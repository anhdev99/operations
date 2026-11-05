#!/usr/bin/env python3
"""Render the data part of the morning brief from collect.py output.

Usage: python3 scripts/collect.py | python3 scripts/render_brief.py > shared/morning-brief.html
Only titles, due dates, labels and links are rendered. The calendar section is a marker
(<!-- CALENDAR -->) for the morning-brief skill to fill from the teaching/shared calendars.
"""
import datetime
import html
import json
import sys

SHOW = 5
STATUS_TEXT = {"not_configured": "chưa điền link/token"}
RELATION_TEXT = {"assignee": "giao cho tôi", "responsible": "tôi chịu trách nhiệm", "author": "tôi tạo", "watcher": "tôi theo dõi"}
KIND_TEXT = {"review_requested": "Chờ tôi review", "my_prs": "PR của tôi đang mở", "assigned_issues": "Issue giao cho tôi"}


def link(text, url):
    return f'<a href="{html.escape(url)}">{html.escape(text)}</a>'


def role_block(role, src):
    parts, warnings = [], []
    for name, data in src.items():
        status = data.get("status", "ok")
        if status != "ok":
            warnings.append((role, name, STATUS_TEXT.get(status, status)))
    op = src["openproject"]
    if op.get("status") == "ok":
        today = datetime.date.today().isoformat()
        rows = []
        for i in op["items"]:
            due = i["dueDate"] or "chưa có hạn"
            late = ' <b class="late">quá hạn</b>' if i["dueDate"] and i["dueDate"] < today else ""
            rel = ", ".join(RELATION_TEXT.get(r, r) for r in i["relations"])
            title = link("#%s %s" % (i["id"], i["subject"]), i["url"])
            rows.append(f"<li>{title} · {html.escape(i['status'])} · {html.escape(due)}{late} · <i>{html.escape(rel)}</i></li>")
        parts.append(f'<h4>OpenProject ({len(rows)})</h4><ul>{"".join(rows) or "<li>Không có</li>"}</ul>')
    gh = src["github"]
    if gh.get("status") == "ok":
        for kind, label in KIND_TEXT.items():
            items = gh[kind]
            if not items:
                continue
            rows = ["<li>%s</li>" % link("%s#%s %s" % (i["repo"], i["number"], i["title"]), i["url"]) for i in items[:SHOW]]
            more = f'<li><i>… và {len(items) - SHOW} mục nữa</i></li>' if len(items) > SHOW else ""
            parts.append(f'<h4>{label} ({len(items)})</h4><ul>{"".join(rows)}{more}</ul>')
    kimai = src["kimai"]
    if kimai.get("status") == "ok":
        total = round(sum(kimai["hours_by_day"].values()), 1)
        missing = ", ".join(kimai["missing_weekdays"]) or "không có"
        parts.append(f"<h4>Giờ Kimai 7 ngày qua</h4><p>Tổng {total} giờ. Ngày làm việc chưa ghi: {html.escape(missing)}</p>")
    slack = src["slack"]
    if slack.get("status") == "ok":
        for key, label in (("mentions", "Slack nhắc tên tôi"), ("direct", "Slack tin nhắn trực tiếp")):
            rows = ["<li>%s · %s · %s</li>" % (link(m["text"] or "(không có chữ)", m["url"]), html.escape(m["from"] or "?"), html.escape("#" + (m["channel"] or "dm"))) for m in slack[key][:SHOW]]
            if rows:
                parts.append(f"<h4>{label} ({len(slack[key])})</h4><ul>{''.join(rows)}</ul>")
    return "".join(parts) or "<p><i>Không có mục nào.</i></p>", warnings


def main():
    data = json.load(sys.stdin)
    blocks, warnings = [], []
    for role, src in data["roles"].items():
        body, warn = role_block(role, src)
        warnings += warn
        blocks.append(f"<section><h3>{html.escape(role)}</h3>{body}</section>")
    un = data.get("github_unassigned", {})
    counts = {}
    for kind in KIND_TEXT:
        for i in un.get(kind, []):
            owner = i["repo"].split("/")[0]
            counts[owner] = counts.get(owner, 0) + 1
    un_html = "".join(f"<li><code>{html.escape(o)}</code>: {n} mục</li>" for o, n in sorted(counts.items())) or "<li>Không có</li>"
    warn_html = "".join(f"<li><b>{html.escape(r)}</b> / {html.escape(n)}: {html.escape(t)}</li>" for r, n, t in warnings)
    print(f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark"><title>Tóm tắt sáng</title>
<style>body{{font:16px/1.6 system-ui,sans-serif;max-width:860px;margin:2rem auto;padding:0 16px}}
h4{{margin:1rem 0 .25rem}}section{{border-top:1px solid #8884;padding-top:.5rem}}.late{{color:#c0392b}}
.warn{{background:#f39c1222;border-left:4px solid #f39c12;padding:.5rem 1rem}}</style></head>
<body>
<h1>Tóm tắt sáng</h1>
<p>Tạo lúc {html.escape(data["generated_at"])}. Chỉ gồm tiêu đề, hạn và link.</p>
<h2>Cảnh báo nguồn</h2><div class="warn"><ul>{warn_html or "<li>Không có</li>"}</ul></div>
<h2>Lịch hôm nay và 7 ngày tới</h2>
<!-- CALENDAR -->
<h2>Theo từng nơi</h2>
{"".join(blocks)}
<h2>Chưa phân nơi (GitHub)</h2>
<p>Gán owner vào <code>units/&lt;nơi&gt;/sources.json</code> (mục <code>github.owners</code>) để chúng vào đúng nơi.</p>
<ul>{un_html}</ul>
</body></html>""")


if __name__ == "__main__":
    main()
