#!/usr/bin/env python3
"""Read my timesheet entries of the last 7 days from a role's Kimai. Read-only.

Usage: python3 scripts/kimai_read.py <role>
Writes units/<role>/snapshot/kimai.json. Not yet verified against a real Kimai instance.
"""
import datetime
import json
import sys
import urllib.error

from common import credentials, http_json, load_sources, not_configured, write_snapshot

DAYS = 7


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    role = sys.argv[1]
    creds = credentials(load_sources(role), ("KIMAI_BASE_URL", "KIMAI_TOKEN"))
    if not creds:
        print(json.dumps(not_configured(role, "kimai"), ensure_ascii=False, indent=2))
        return
    today = datetime.date.today()
    start = today - datetime.timedelta(days=DAYS - 1)
    try:
        rows = http_json(
            creds["KIMAI_BASE_URL"].rstrip("/") + "/api/timesheets",
            {"Authorization": "Bearer " + creds["KIMAI_TOKEN"]},
            {"begin": start.isoformat() + "T00:00:00", "end": today.isoformat() + "T23:59:59", "size": 200, "full": "true"},
        )
        hours = {(start + datetime.timedelta(days=i)).isoformat(): 0.0 for i in range(DAYS)}
        items = []
        for r in rows:
            day = r["begin"][:10]
            h = round((r.get("duration") or 0) / 3600, 2)
            hours[day] = round(hours.get(day, 0) + h, 2)
            items.append({"id": r["id"], "date": day, "hours": h,
                          "project": (r.get("project") or {}).get("name"),
                          "activity": (r.get("activity") or {}).get("name")})
        missing = [d for d, h in hours.items() if h == 0 and datetime.date.fromisoformat(d).weekday() < 5]
        result = {"role": role, "source": "kimai", "status": "ok", "hours_by_day": hours,
                  "missing_weekdays": missing, "items": items}
    except (urllib.error.URLError, KeyError, OSError, ValueError) as exc:
        result = {"role": role, "source": "kimai", "status": "error",
                  "error": type(exc).__name__ + ": " + str(exc), "items": []}
    write_snapshot(role, "kimai.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "error":
        sys.exit(1)


if __name__ == "__main__":
    main()
