#!/usr/bin/env python3
"""Switch a JARVIS v4 checkout from the Cursor CLI to Claude Code.

Usage: python3 patch-claude-engine.py /path/to/jarvis-v4

What it changes (idempotent, keeps a .orig backup of each file):
  deploy.py               pane 1 runs `claude` instead of `cursor agent` when the
                          agent dir has a `.jarvis-engine` file containing "claude"
                          (the installer writes it), and writes the agent's
                          .claude/settings.json permission rules.
  apps/master-rocketchat.py  messages typed into pane 1 are flattened to one line
                          for Claude Code (a newline would submit early).
"""
import shutil, sys
from pathlib import Path

v4 = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
MARK = "# convenex-claude-engine"

def patch(rel, old, new):
    p = v4 / rel
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        print(f"{rel}: already patched"); return
    if s.count(old) != 1:
        sys.exit(f"{rel}: expected code not found; JARVIS v4 may have changed. Nothing patched.")
    shutil.copy2(p, p.with_suffix(p.suffix + ".orig"))
    p.write_text(s.replace(old, new), encoding="utf-8")
    print(f"{rel}: patched (backup: {p.name}.orig)")

patch("deploy.py",
"""    pane1 = (f'cd {agent_dir} && cursor agent --yolo --sandbox enabled '
             f'--model {model} "read context.md"')""",
"""    pane1 = (f'cd {agent_dir} && cursor agent --yolo --sandbox enabled '
             f'--model {model} "read context.md"')
    """ + MARK + """
    eng = agent_dir / ".jarvis-engine"
    if eng.exists() and eng.read_text().strip() == "claude":
        import json as _json
        (agent_dir / ".claude").mkdir(exist_ok=True)
        st = agent_dir / ".claude" / "settings.json"
        if not st.exists() and not dry:
            st.write_text(_json.dumps({"permissions": {
                "allow": ["Bash(python3 apps/rocketchat.py:*)", "Bash(python3 apps/mailinbox.py:*)",
                          "Bash(ls:*)", "Bash(cat:*)", "Bash(tail:*)", "Bash(grep:*)", "Bash(jq:*)",
                          "Read", "Edit", "Write", "WebSearch", "WebFetch"],
                "deny": ["Bash(rm -rf:*)", "Bash(ssh:*)", "Bash(curl:*)", "Bash(sudo:*)"]}}, indent=2))
        pane1 = f'cd {agent_dir} && claude --permission-mode acceptEdits "read context.md"'""")

patch("apps/master-rocketchat.py",
"""    target = f"{tmux_session}:main.1"
    subprocess.run(["tmux", "send-keys", "-t", target, "-l", prompt])""",
"""    target = f"{tmux_session}:main.1"
    """ + MARK + """
    try:
        if open(".jarvis-engine").read().strip() == "claude":
            prompt = " / ".join(l.strip() for l in prompt.splitlines() if l.strip())
    except OSError:
        pass
    subprocess.run(["tmux", "send-keys", "-t", target, "-l", prompt])""")
