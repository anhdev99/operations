#!/usr/bin/env python3
"""Show which sources are filled in and working. Never prints a token or its value.

Usage: python3 scripts/check_setup.py
"""
import json
import subprocess
import sys
from pathlib import Path

from common import credentials, list_roles, load_sources

HERE = Path(__file__).resolve().parent
KEYS = {"openproject": ("OP_BASE_URL", "OP_TOKEN"), "kimai": ("KIMAI_BASE_URL", "KIMAI_TOKEN"), "slack": ("SLACK_TOKEN",)}
SCRIPT = {"openproject": "op_read.py", "kimai": "kimai_read.py", "slack": "slack_read.py"}


def main():
    for role in list_roles():
        src = load_sources(role)
        print(f"\n{role}")
        for name, keys in KEYS.items():
            if not credentials(src, keys):
                print(f"  {name:<12} CHƯA ĐIỀN   điền {', '.join(keys)} vào {src.get('env_file', '(thiếu env_file trong sources.json)')}")
                continue
            proc = subprocess.run([sys.executable, str(HERE / SCRIPT[name]), role], capture_output=True, text=True)
            try:
                status = json.loads(proc.stdout).get("status", "?")
            except json.JSONDecodeError:
                status = "error"
            detail = "" if status == "ok" else "  xem lỗi: python3 scripts/" + SCRIPT[name] + " " + role
            print(f"  {name:<12} {'OK' if status == 'ok' else status.upper()}{detail}")
        owners = (src.get("github") or {}).get("owners", [])
        print(f"  {'github':<12} {'owners: ' + ', '.join(owners) if owners else 'CHƯA GÁN owner'}")


if __name__ == "__main__":
    main()
