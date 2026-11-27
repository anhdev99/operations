#!/usr/bin/env python3
"""Render a summary JSON as Slack blocks and post it: one message per role to its channel, one overview to #00-tong-hop.

Usage: python3 scripts/post_summary.py <summary.json> [--role <role>] [--dry-run]
       python3 scripts/post_summary.py --overview [--dry-run]   (joins reports/summary-<role>.json into #00-tong-hop)
The model only fills the content; layout is fixed here so every report looks the same.
Tables use Slack's native table block; if Slack rejects it, falls back to a monospace text table.

summary.json:
{"roles": [{"role": "digital-transformation",
            "needs_you": ["..."],                       # empty list = nothing needs the user
            "highlights": [{"channel": "#operations", "text": "..."}],
            "people": [{"name": "tuansang753", "channel": "#operations", "doing": "...", "reported": "..."}],
            "agents": "7 agent, 0 đang chạy, 0 lỗi",
            "links": [{"label": "...", "url": "https://..."}],
            "tickets": [{"id": 46, "summary": "tóm tắt 1-2 câu nội dung ticket OpenProject"}],
            "warnings": ["nguồn X lỗi"]}]}             # optional
"""
import datetime
import json
import sys

import common  # noqa: F401  (UTF-8 stdio)
from report import ROLES
from slack_post import post

LIMIT = 2800  # Slack section text limit is 3000


def _clip(text):
    return text if len(text) <= LIMIT else text[:LIMIT - 1] + "…"


def link_cell(text, url):
    """Table cell holding one clickable link (raw_text cells cannot hold links)."""
    return {"type": "rich_text", "elements": [{"type": "rich_text_section",
            "elements": [{"type": "link", "url": url, "text": text}]}]}


def _cell(text, bold=False):
    if isinstance(text, dict):  # already a ready-made cell (e.g. link_cell)
        return text
    if not bold:
        return {"type": "raw_text", "text": text or "—"}
    return {"type": "rich_text", "elements": [{"type": "rich_text_section",
            "elements": [{"type": "text", "text": text, "style": {"bold": True}}]}]}


def table_block(headers, rows, wrap):
    """Slack native table block: first row is the header. At most one table per message."""
    return {"type": "table",
            "rows": [[_cell(h, bold=True) for h in headers]] + [[_cell(c) for c in r] for r in rows],
            "column_settings": [{"is_wrapped": w} for w in wrap]}


def text_table(headers, rows, widths):
    """Fallback: monospace table inside a code block."""
    def fit(text, width):
        text = (text or "—").replace("\n", " ")
        return (text if len(text) <= width else text[:width - 1] + "…").ljust(width)

    def line(cells):
        return " | ".join(fit(c, w) for c, w in zip(cells, widths))

    body = [line(headers), "-+-".join("-" * w for w in widths)] + [line(r) for r in rows]
    return {"type": "section", "text": {"type": "mrkdwn", "text": "```" + "\n".join(body) + "```"}}


def table(native, headers, rows, wrap, widths):
    return table_block(headers, rows, wrap) if native else text_table(headers, rows, widths)


def role_blocks(item, stamp, native=True):
    title = ROLES[item["role"]][2]
    needs = item.get("needs_you") or []
    blocks = [{"type": "header", "text": {"type": "plain_text", "text": "📋 %s · %s" % (title, stamp)}}]
    if needs:
        body = "\n".join("• " + n for n in needs)
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": _clip("🔴 *Cần bạn xử lý*\n" + body)}})
    else:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": "✅ *Không có việc cần bạn xử lý*"}})
    blocks.append({"type": "divider"})
    hl = item.get("highlights") or []
    grouped = {}  # nhóm chủ đề -> các kênh nguồn, giữ thứ tự xuất hiện
    for h in hl:
        grouped.setdefault(h.get("group") or "Khác", []).append(h)
    parts = []
    for group, items in grouped.items():
        parts.append("📂 *%s*\n%s" % (group, "\n".join("      • `%s` %s" % (h["channel"], h["text"]) for h in items)))
    body = "\n\n".join(parts) or "_Không có tin mới._"
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": _clip("📌 *Tình hình chung theo nhóm*\n\n" + body)}})
    people = item.get("people") or []
    if people:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": "👥 *Ai làm gì, ai báo cáo gì*"}})
        rows = [[x["name"], x.get("channel") or "—", x.get("doing") or "—", x.get("reported") or "—"] for x in people]
        blocks.append(table(native, ["Người", "Kênh", "Đang làm", "Báo cáo"], rows, [False, False, True, True], [16, 14, 34, 34]))
    if item.get("warnings"):
        warn = "\n".join("• " + w for w in item["warnings"])
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": _clip("⚠️ *Lưu ý nguồn dữ liệu*\n" + warn)}})
    blocks.append({"type": "divider"})
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": "🤖 *Agent*   " + (item.get("agents") or "_không có dữ liệu_")}})
    links = item.get("links") or []
    if links:
        text = "🔗 " + "  ·  ".join("<%s|%s>" % (l["url"], l["label"]) for l in links[:5])
        blocks.append({"type": "context", "elements": [{"type": "mrkdwn", "text": text}]})
    return blocks


def op_cell(op):
    """One-line OpenProject status for the overview table."""
    if not op:
        return "—"
    if op.get("status") == "not_configured":
        return "Chưa cấu hình"
    if op.get("status") != "ok":
        return "⚠ lỗi đọc"
    if not op["overdue"] and not op["soon"]:
        return "✅ %d việc mở, không quá hạn" % op["total"]
    return "🔴 %d quá hạn · 🟡 %d sắp đến hạn · %d việc mở" % (op["overdue"], op["soon"], op["total"])


def op_blocks(title, op, stamp, native=True, summaries=None):
    """Second message of a company: OpenProject workload. Layout is fixed here, numbers come from report.op_summary()."""
    blocks = [{"type": "header", "text": {"type": "plain_text", "text": "🗂 OpenProject · %s · %s" % (title, stamp)}}]
    if op.get("status") == "not_configured":
        text = "⚠️ OpenProject chưa cấu hình cho nơi này (thiếu OP_BASE_URL hoặc OP_TOKEN)."
        return blocks + [{"type": "section", "text": {"type": "mrkdwn", "text": text}}]
    if op.get("status") != "ok":
        text = "⚠️ Không đọc được OpenProject: %s" % (op.get("error") or op.get("status"))
        return blocks + [{"type": "section", "text": {"type": "mrkdwn", "text": _clip(text)}}]
    head = "🔴 *%d quá hạn*   🟡 *%d đến hạn trong %d ngày*   ⚪ %d việc mở (%d chưa có hạn)" % (
        op["overdue"], op["soon"], op["soon_days"], op["total"], op["no_due"])
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": head}})
    per_project = "\n".join("• %s: %d mở · 🔴 %d quá hạn · 🟡 %d sắp đến hạn" % (p["name"], p["total"], p["overdue"], p["soon"])
                            for p in op["projects"])
    blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": _clip("📁 *Theo dự án*\n" + per_project)}})
    if op["attention"]:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": "⏰ *Cần chú ý (gấp nhất trước)*"}})
        native_rows, text_rows = [], []
        for a in op["attention"]:
            if a["days"] < 0:
                state = "🔴 quá hạn %d ngày" % -a["days"]
            elif a["days"] == 0:
                state = "🟡 hết hạn hôm nay"
            else:
                state = "🟡 còn %d ngày" % a["days"]
            due = a["due"][8:10] + "/" + a["due"][5:7]
            label = "#%s %s" % (a["id"], a["subject"])
            note = (summaries or {}).get(str(a["id"])) or "—"
            state = "%s (%s)" % (state, due)
            holder = a.get("assignee") or "(chưa giao)"
            author = a.get("author") or "—"
            native_rows.append([link_cell(label, a["url"]), state, holder, author, a["project"], note])
            text_rows.append([label, state, holder, author, a["project"], note])
        heads = ["Việc", "Tình trạng (hạn)", "Đang giữ", "Người tạo", "Dự án", "Nội dung"]
        if native:
            blocks.append(table_block(heads, native_rows, [True, True, True, True, True, True]))
        else:
            blocks.append(text_table(heads, text_rows, [30, 26, 18, 18, 22, 36]))
        more = op["attention_total"] - len(op["attention"])
        if more > 0:
            blocks.append({"type": "context", "elements": [{"type": "mrkdwn", "text": "… và %d việc nữa." % more}]})
    return blocks


def overview_blocks(items, stamp, native=True, ops=None):
    blocks = [{"type": "header", "text": {"type": "plain_text", "text": "🗞 Báo cáo · " + stamp}}]
    rows = []
    for it in items:
        channel, _, title = ROLES[it["role"]]
        needs = it.get("needs_you") or []
        if needs:
            todo = "🔴 %d: %s" % (len(needs), "; ".join(needs[:3]))
        else:
            todo = "✅ Không có"
        rows.append([title, todo, op_cell((ops or {}).get(it["role"])), it.get("agents") or "—", "#" + channel])
    heads = ["Nơi", "Việc cần bạn", "OpenProject", "Agent", "Kênh chi tiết"]
    blocks.append(table(native, heads, rows, [False, True, True, True, False], [20, 34, 34, 26, 12]))
    blocks.append({"type": "context", "elements": [{"type": "mrkdwn", "text": "Chi tiết ở kênh riêng của từng nơi."}]})
    return blocks


def load_overview_items(max_age_hours=8):
    """Latest summary-<role>.json of every role; a missing or stale file becomes a 'no report' row."""
    import time
    from common import ROOT
    items = []
    for role in ROLES:
        path = ROOT / "reports" / ("summary-%s.json" % role)
        item = {"role": role, "needs_you": [], "agents": "⚠ chưa có báo cáo gần đây"}
        if path.exists() and time.time() - path.stat().st_mtime <= max_age_hours * 3600:
            try:
                item = json.loads(path.read_text(encoding="utf-8"))["roles"][0]
            except (ValueError, KeyError, IndexError):
                item["agents"] = "⚠ tệp báo cáo hỏng"
        items.append(item)
    return items


def load_overview_ops(max_age_hours=8):
    import time
    from common import ROOT
    ops = {}
    for role in ROLES:
        path = ROOT / "reports" / ("op-%s.json" % role)
        if path.exists() and time.time() - path.stat().st_mtime <= max_age_hours * 3600:
            try:
                ops[role] = json.loads(path.read_text(encoding="utf-8"))
            except ValueError:
                pass
    return ops


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    dry = "--dry-run" in sys.argv
    stamp = datetime.datetime.now().strftime("%H:%M · %d/%m")

    def send(channel, text, build):
        ok, detail = post(channel, text, dry, build(True))
        if not ok and "invalid_blocks" in detail:  # Slack rejected the table block
            ok, detail = post(channel, text, dry, build(False))
            detail += " (bảng chữ)"
        print("#%s: %s" % (channel, detail))
        return ok

    failed = False
    if "--overview" in sys.argv:  # only joins existing per-company summaries; reads no source system
        items, ops = load_overview_items(), load_overview_ops()
        failed |= not send("00-tong-hop", "Báo cáo " + stamp, lambda native: overview_blocks(items, stamp, native, ops))
        sys.exit(1 if failed else 0)

    data = json.load(open(sys.argv[1], encoding="utf-8"))
    only = sys.argv[sys.argv.index("--role") + 1] if "--role" in sys.argv else None
    roles = [r for r in data["roles"] if not only or r["role"] == only]
    if only and not roles:
        sys.exit("khong co role '%s' trong %s" % (only, sys.argv[1]))
    from common import ROOT
    from report import op_summary
    ops = {}
    for item in roles:
        channel, _, title = ROLES[item["role"]]
        failed |= not send(channel, "Báo cáo %s %s" % (title, stamp),
                           lambda native, item=item: role_blocks(item, stamp, native))
        op = ops[item["role"]] = op_summary(item["role"])  # deterministic, read-only
        if not dry:
            (ROOT / "reports" / ("op-%s.json" % item["role"])).write_text(json.dumps(op, ensure_ascii=False), encoding="utf-8")
        failed |= not send(channel, "OpenProject %s %s" % (title, stamp),
                           lambda native, title=title, op=op, item=item: op_blocks(
                               title, op, stamp, native,
                               {str(t["id"]): t.get("summary") for t in item.get("tickets") or [] if t.get("summary")}))
    if not only:
        failed |= not send("00-tong-hop", "Báo cáo " + stamp, lambda native: overview_blocks(roles, stamp, native, ops))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
