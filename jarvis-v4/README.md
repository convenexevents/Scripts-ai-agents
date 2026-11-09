# Convene X on JARVIS v4

[JARVIS v4](https://github.com/sw7ft/jarvis-v4) (MIT) runs each agent in its own
tmux session with a Cursor CLI worker, and gives each one a private Rocket.Chat
channel you can message from your phone. This folder installs the 22 Convene X
agents into it as `cx-<firstname>` (channel `#cx-amara`, session `cx-amara`, …).

## Free, in-house option (recommended to start)
Run it all on your Windows PC with Claude Code as the engine (no Cursor subscription) and chat from your phone: see **[home/README.md](home/README.md)**.

## What you need (cloud or Mac option)
- A Mac or Linux machine to host it (JARVIS v4 is not built for Windows; WSL may work but is untested).
- A Rocket.Chat server (self-hosted or Rocket.Chat Cloud), with an admin account and a bot account.
- Cursor with the CLI agent (`cursor agent`), plus `tmux` and Python 3.

## Install
```bash
git clone https://github.com/sw7ft/jarvis-v4.git ~/jarvis-v4
cd ~/jarvis-v4 && ./scripts/check-prerequisites.sh
python3 apps/master-rocketchat.py setup          # Rocket.Chat admin + bot credentials
bash ~/Scripts-ai-agents/jarvis-v4/install.sh ~/jarvis-v4            # writes the 22 agents
bash ~/Scripts-ai-agents/jarvis-v4/install.sh ~/jarvis-v4 --deploy   # optional: launch all 22
python3 app.py                                   # dashboard on http://localhost:5112
```
Start with one agent (`python3 deploy.py cx-theo`) before launching all 22.

## What the installer does
- Builds `agents/cx-*/context.md` from JARVIS v4's own template plus the agent's
  full Convene X role (from `.claude/agents/cx-*.md` in this repo). `deploy.py`
  keeps an existing `context.md`, so redeploying never overwrites it.
- Writes `tags.json` (Convene X, department, reports to) for the dashboard.
- Appends the Convene X fleet rules (`MASTER-CONTEXT-convenex.md`) to
  `MASTER-CONTEXT.md` once: draft only, STOP means stop, log jobs in the Agent
  Jobs sheet, Convene X CRM / Finance Control / Prospecting Machine as systems of
  record, brand rules, no SSH needed, how to hand off between agents.

Re-run `install.sh` after an agent changes in this repo, then redeploy that agent
(delete its `context.md` first if you want the new version picked up).

## What JARVIS v4 adds that Convene X didn't have
| JARVIS v4 feature | Gap it fills |
|---|---|
| One Rocket.Chat channel per agent | Message any agent directly from your phone |
| `logs/dispatch.log` per agent | Full audit trail of every request and reply |
| STOP / HALT / ABORT | Emergency stop for a running agent |
| Routines in pane 2 | Recurring jobs that stop when the agent stops (replacement for the paused scheduled jobs) |
| Dashboard on :5112 | Live view of every agent's session |

Not used: the `contact-form` module (your forms already go to the CRM through
Make) and SSH hosts (agents work through connectors, not servers).
