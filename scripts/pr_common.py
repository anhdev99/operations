"""Shared helpers for the PR watcher (pr_watch.py), reader (pr_fetch.py) and actor (pr_act.py).

Role <-> GitHub owner mapping comes from units/<role>/sources.json (github.owners, github.watch).
State lives in reports/pr-state.json (outside git). Each company keeps its own PRs and Slack channel.
"""
import json
import subprocess
import sys
import urllib.request

from common import ROOT, list_roles, load_sources

STATE = ROOT / "reports" / "pr-state.json"
REVIEW_ROUTINE_TITLE = "Review PR được giao"

# Report channel in the personal Slack workspace, and the Paperclip company prefix, per role.
CHANNELS = {
    "digital-transformation": "dthu-bao-cao",
    "phd-group": "phd-group-bao-cao",
    "lucidtech": "lucidtech-bao-cao",
    "homelab": "homelab-bao-cao",
}
COMPANY_PREFIX = {
    "digital-transformation": "TCH",
    "phd-group": "PHD",
    "lucidtech": "LUC",
    "homelab": "HOMA",
}
PAPERCLIP = "http://127.0.0.1:3100/api"


def watch_config():
    """{role: {"owners": [...], "watch": "review_requested"|"all_open"}} for roles with a GitHub owner."""
    out = {}
    for role in list_roles():
        gh = load_sources(role).get("github") or {}
        if gh.get("owners") and role in CHANNELS:
            out[role] = {"owners": gh["owners"], "watch": gh.get("watch", "review_requested")}
    return out


def role_for_repo(name_with_owner):
    owner = name_with_owner.split("/")[0].lower()
    for role, cfg in watch_config().items():
        if owner in [o.lower() for o in cfg["owners"]]:
            return role
    return None


def gh(args, check=True):
    out = subprocess.run(["gh", *args], capture_output=True, text=True, encoding="utf-8")
    if check and out.returncode != 0:
        raise RuntimeError("gh " + " ".join(args[:3]) + ": " + (out.stderr or "").strip()[:300])
    return out.stdout


def gh_json(args):
    return json.loads(gh(args))


def base_drift(repo, old, new, pr_files, max_commits=15, max_files=60):
    """What landed between two refs (PR head vs base branch, or the base at last review vs now), restricted to files the PR touches.

    The compare API caps its file list at 300 files, which a big merge can fill with unrelated files, so each PR file is
    asked for its own commits since the merge base instead.
    Returns {"behind_by": n, "overlapping_files": [...], "commits": [{"sha","message","author"}]}.
    """
    import urllib.parse
    cmp = gh_json(["api", "repos/" + repo + "/compare/" + old + "..." + new])
    merge_base = cmp["merge_base_commit"]
    since = merge_base["commit"]["committer"]["date"]
    overlap, commits, seen = [], [], set()
    for path in pr_files[:max_files]:
        found = gh_json(["api", "repos/" + repo + "/commits?sha=" + new + "&since=" + since + "&per_page=5&path="
                         + urllib.parse.quote(path)])
        fresh = [c for c in found if c["sha"] != merge_base["sha"]]
        if not fresh:
            continue
        overlap.append(path)
        for c in fresh:
            if c["sha"] not in seen and len(commits) < max_commits:
                seen.add(c["sha"])
                commits.append({"sha": c["sha"][:10], "message": c["commit"]["message"].splitlines()[0][:160],
                                "author": (c.get("author") or {}).get("login") or c["commit"]["author"]["name"]})
    return {"behind_by": cmp.get("ahead_by", 0), "overlapping_files": sorted(overlap), "commits": commits}


def me():
    return gh(["api", "user", "-q", ".login"]).strip()


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return None


def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_ref(ref):
    """'owner/repo#12' or 'owner/repo 12' -> ('owner/repo', 12)."""
    ref = ref.strip().replace(" ", "#")
    repo, _, num = ref.partition("#")
    if repo.count("/") != 1 or not num.isdigit():
        sys.exit("expected owner/repo#number, got: " + ref)
    return repo, int(num)


def require_role(repo):
    role = role_for_repo(repo)
    if not role:
        sys.exit("refused: " + repo + " is not in a configured github.owners")
    return role


def paperclip(method, path, body=None):
    req = urllib.request.Request(
        PAPERCLIP + path, method=method,
        data=json.dumps(body).encode("utf-8") if body is not None else None,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def trigger_review_routine(role):
    """Start the role's review routine in Paperclip. Returns a short status string."""
    try:
        companies = paperclip("GET", "/companies")
        company = next(c for c in companies if c.get("issuePrefix") == COMPANY_PREFIX[role])
        routines = paperclip("GET", "/companies/" + company["id"] + "/routines")
        routine = next(r for r in routines if r["title"].startswith(REVIEW_ROUTINE_TITLE))
        run = paperclip("POST", "/routines/" + routine["id"] + "/run", {})
        return "routine run " + str(run.get("status"))
    except StopIteration:
        return "routine not found for " + role
    except OSError as exc:
        return "paperclip unreachable: " + str(exc)[:120]


def slack_notify(role, text, dry_run=False):
    from slack_post import post
    return post(CHANNELS[role], text, dry_run)
