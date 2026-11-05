"""Shared helpers for the read-only connectors."""
import json
import os
import ssl
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_sources(role):
    path = ROOT / "units" / role / "sources.json"
    if not path.exists():
        sys.exit(f"unknown role '{role}': {path} not found")
    return json.loads(path.read_text(encoding="utf-8"))


def list_roles():
    return sorted(p.name for p in (ROOT / "units").iterdir() if (p / "sources.json").exists())


def load_env_file(path):
    """Parse KEY=VALUE lines. Values never leave this process."""
    env = {}
    for line in Path(os.path.expanduser(path)).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def write_snapshot(role, name, data):
    out = ROOT / "units" / role / "snapshot"
    out.mkdir(parents=True, exist_ok=True)
    (out / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def ssl_context():
    """Verify certificates. python.org builds on macOS ship without a CA bundle, so fall back to the system one."""
    for cafile in ("/etc/ssl/cert.pem", "/opt/homebrew/etc/ca-certificates/cert.pem"):
        if os.path.exists(cafile):
            return ssl.create_default_context(cafile=cafile)
    return ssl.create_default_context()


def credentials(src, keys):
    """Return {key: value} from the role's env_file, or None if unconfigured (no file, or any value empty)."""
    if not src.get("env_file"):
        return None
    try:
        env = load_env_file(src["env_file"])
    except OSError:
        return None
    if any(not env.get(k) for k in keys):
        return None
    return {k: env[k] for k in keys}


def http_json(url, headers, params=None, timeout=30):
    """GET a JSON document, verifying certificates."""
    import urllib.parse
    import urllib.request
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout, context=ssl_context()) as resp:
        return json.load(resp)


def not_configured(role, source):
    return {"role": role, "source": source, "status": "not_configured", "items": []}
