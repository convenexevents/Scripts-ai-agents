#!/usr/bin/env bash
# One-time setup of Convene X JARVIS v4 on your Windows PC (inside WSL Ubuntu).
# Run inside Ubuntu:  bash ~/Scripts-ai-agents/jarvis-v4/home/setup-wsl.sh
# Free: Ubuntu, Docker Engine, Rocket.Chat Community, JARVIS v4, Tailscale personal.
# Claude Code uses your existing Claude plan (no extra subscription).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK="$(cd "$HERE/.." && pwd)"
V4="${JARVIS_DIR:-$HOME/jarvis-v4}"

echo "== 1/6 System packages"
sudo apt-get update -y
sudo apt-get install -y git curl tmux jq python3 python3-pip python3-venv ca-certificates

echo "== 2/6 Docker Engine (free, open source)"
if ! command -v docker >/dev/null; then
  curl -fsSL https://get.docker.com | sudo sh
  sudo usermod -aG docker "$USER"
fi
sudo systemctl enable --now docker 2>/dev/null || sudo service docker start

echo "== 3/6 Rocket.Chat + MongoDB"
cd "$HERE" && sudo docker compose up -d
echo "   Rocket.Chat is starting on http://localhost:3000 (first start takes a few minutes)"

echo "== 4/6 Claude Code"
if ! command -v claude >/dev/null; then
  curl -fsSL https://claude.ai/install.sh | bash
  export PATH="$HOME/.local/bin:$PATH"
fi

echo "== 5/6 JARVIS v4"
[ -d "$V4/.git" ] || git clone https://github.com/sw7ft/jarvis-v4.git "$V4"
cd "$V4"
[ -f requirements.txt ] && python3 -m pip install --user --break-system-packages -r requirements.txt || true
python3 "$PACK/patch-claude-engine.py" "$V4"

echo "== 6/6 Convene X agents (Claude Code engine)"
JARVIS_ENGINE=claude bash "$PACK/install.sh" "$V4"

cat <<NEXT

Setup done. Now, by hand (about 15 minutes, see jarvis-v4/home/README.md):
  a) Open http://localhost:3000 in Windows, finish the Rocket.Chat wizard
     (admin account), then create a user called "jarvis-bot".
  b) Run:  claude            (log in with your Claude account once, then /exit)
  c) Run:  cd $V4 && python3 apps/master-rocketchat.py setup
  d) Start 3 agents:  python3 deploy.py cx-theo --no-attach
                      python3 deploy.py cx-jordan --no-attach
                      python3 deploy.py cx-andrew --no-attach
  e) Phone: install Tailscale + Rocket.Chat apps (README step 5).
NEXT
