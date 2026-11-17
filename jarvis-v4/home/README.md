# Convene X agents on your phone: free, in-house

Everything runs on your Windows PC. Your phone chats to the agents through the
Rocket.Chat app. Nothing new to pay for:

| Part | Cost |
|---|---|
| Ubuntu inside Windows (WSL) | Free |
| Docker Engine | Free (open source) |
| Rocket.Chat Community edition | Free (self-hosted) |
| JARVIS v4 | Free (MIT licence) |
| Tailscale (secure link to your phone) | Free personal plan |
| Agents' AI | **Claude Code on your existing Claude plan**, instead of a Cursor subscription |

**Trade-offs:** agents only run while the PC is on and awake. Each agent uses
your Claude plan's allowance while it works (idle agents use nothing). Start
with 3 agents.

---

## Step 1: Ubuntu on Windows (5 min, once)
Open **PowerShell as administrator** and run:
```
wsl --install -d Ubuntu
```
Restart if asked, open **Ubuntu** from the Start menu, and pick a username and password.

## Step 2: Get this repo into Ubuntu
```
git clone https://github.com/convenexevents/Scripts-ai-agents.git ~/Scripts-ai-agents
```
(If GitHub asks you to sign in, use your GitHub account; the repo is private.)

## Step 3: Run the setup script (10–15 min, mostly waiting)
```
bash ~/Scripts-ai-agents/jarvis-v4/home/setup-wsl.sh
```
It installs Docker, starts Rocket.Chat, installs Claude Code and JARVIS v4,
switches JARVIS to Claude Code, and installs all 22 Convene X agents.
Afterwards, close Ubuntu and open it again (so Docker permissions apply).

## Step 4: Finish setup (10 min)
1. In Windows, open **http://localhost:3000** and complete the Rocket.Chat wizard
   (this creates your admin login). When it offers to **register the workspace**,
   say yes: it's free and is what makes phone notifications work.
2. In Rocket.Chat: **Administration → Users → New**, create a user `jarvis-bot`
   with a password (this is the account the agents post as).
3. In Ubuntu, log Claude Code in once:
   ```
   claude
   ```
   Follow the login link, then type `/exit`.
4. Connect JARVIS to Rocket.Chat (enter the admin and jarvis-bot logins when asked):
   ```
   cd ~/jarvis-v4 && python3 apps/master-rocketchat.py setup
   ```
5. Start your first 3 agents:
   ```
   python3 deploy.py cx-theo --no-attach
   python3 deploy.py cx-jordan --no-attach
   python3 deploy.py cx-andrew --no-attach
   ```
   Each one gets its own private channel: `#cx-theo`, `#cx-jordan`, `#cx-andrew`.

## Step 5: Your phone
**Option A: in the house only (simplest).** Find your PC's address (in
PowerShell: `ipconfig`, look for IPv4, for example 192.168.1.20). In the
Rocket.Chat phone app, add the workspace `http://192.168.1.20:3000`. Some app
versions insist on https; if it refuses, use option B.

**Option B: in the house and out (recommended).** Install **Tailscale** (free)
on the PC (Windows installer from tailscale.com) and on your phone, signing in
with the same account on both. Then in Ubuntu:
```
sudo tailscale serve --bg 3000        # if Tailscale is installed inside Ubuntu
```
or in Windows PowerShell: `tailscale serve --bg 3000`. It prints an https
address like `https://your-pc.your-tailnet.ts.net`. Add that in the Rocket.Chat
phone app. Only your own devices can reach it.

## Using it
- Message an agent in its channel, for example in `#cx-theo`: *"Draft three
  LinkedIn posts about the CFO dinner."* It replies in the same channel.
- Everything is draft only: agents never send, post or sign anything without
  your OK.
- Post **STOP** in a channel to halt that agent immediately.
- Dashboard: in Ubuntu run `cd ~/jarvis-v4 && python3 app.py`, then open
  http://localhost:5112 on the PC.
- Add more agents later: `python3 deploy.py cx-<name> --no-attach`
  (names in `jarvis-v4/agents.json`).

## Keeping it running
- Leave the PC on and stop it sleeping (Windows Settings → Power → Sleep: Never).
- After a restart: open Ubuntu, then `cd ~/Scripts-ai-agents/jarvis-v4/home && docker compose up -d`
  and re-run the `deploy.py` lines for your agents.

## Undo
`docker compose down` (in this folder) stops Rocket.Chat. `tmux kill-server`
stops all agents. To remove everything: `wsl --unregister Ubuntu` in PowerShell
(this deletes the Ubuntu install).
