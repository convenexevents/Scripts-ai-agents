#!/usr/bin/env bash
# Install the Convene X agent team into a JARVIS v4 checkout.
# Usage: bash jarvis-v4/install.sh /path/to/jarvis-v4 [--deploy]
#   JARVIS_ENGINE=claude  run agents on Claude Code instead of Cursor (needs patch-claude-engine.py)
#   --deploy  also runs `python3 deploy.py cx-<name> --no-attach` for every agent
#             (needs Rocket.Chat set up first: python3 apps/master-rocketchat.py setup)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
V4="${1:?Usage: install.sh /path/to/jarvis-v4 [--deploy]}"
DEPLOY="${2:-}"
[ -f "$V4/deploy.py" ] && [ -f "$V4/templates/agent-context.md" ] || { echo "Not a JARVIS v4 checkout: $V4"; exit 1; }

python3 - "$REPO" "$V4" <<'PY'
import json, os, re, sys, shutil
from pathlib import Path
repo, v4 = Path(sys.argv[1]), Path(sys.argv[2])
meta = json.loads((repo/"jarvis-v4/agents.json").read_text(encoding="utf-8"))
tpl = (v4/"templates/agent-context.md").read_text(encoding="utf-8")
for slug, m in meta.items():
    src = repo/".claude/agents"/f"{slug}.md"
    body = src.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n", "", body, count=1, flags=re.S).strip()
    d = v4/"agents"/slug
    for sub in ("apps", "logs", "docs", "utilities", "routines", "uploads", "downloads"):
        (d/sub).mkdir(parents=True, exist_ok=True)
    ctx = (tpl.replace("{{name}}", slug).replace("{{channel}}", slug)
              .replace("{{ssh_host}}", slug).replace("{{session}}", slug))
    ctx += ("\n\n---\n\n# Convene X role: " + m["name"] + "\n\n"
            f"**Department:** {m['department']}  \n**Reports to:** {m['reports_to']}  \n"
            "**Fleet rules:** see the Convene X addendum at the end of `../../MASTER-CONTEXT.md`.\n\n" + body + "\n")
    (d/"context.md").write_text(ctx, encoding="utf-8")   # deploy.py keeps an existing context.md
    if os.environ.get("JARVIS_ENGINE") == "claude":
        (d/".jarvis-engine").write_text("claude\n", encoding="utf-8")
    (d/"tags.json").write_text(json.dumps(["Convene X", m["department"], "reports to " + m["reports_to"]]), encoding="utf-8")
    for sub in ("routines", "utilities", "docs"):
        t = v4/"templates"/sub/"README.md"
        dst = d/sub/"README.md"
        if t.exists() and not dst.exists():
            dst.write_text(t.read_text(encoding="utf-8").replace("{{name}}", slug).replace("{{channel}}", slug).replace("{{session}}", slug), encoding="utf-8")
    print("installed", slug)
mc = v4/"MASTER-CONTEXT.md"
s = mc.read_text(encoding="utf-8")
if "<!-- convenex-addendum -->" not in s:
    mc.write_text(s.rstrip() + "\n" + (repo/"jarvis-v4/MASTER-CONTEXT-convenex.md").read_text(encoding="utf-8"), encoding="utf-8")
    print("MASTER-CONTEXT.md: Convene X rules appended")
PY

if [ "$DEPLOY" = "--deploy" ]; then
  cd "$V4"
  for a in $(python3 -c "import json;print(' '.join(json.load(open('$HERE/agents.json'))))"); do
    python3 deploy.py "$a" --no-attach
  done
else
  echo "Done. Next: cd $V4 && python3 apps/master-rocketchat.py setup, then python3 deploy.py cx-amara (or re-run with --deploy for all 22)."
fi
