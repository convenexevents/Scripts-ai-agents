"""Generate HTML for the 16-22 Nov 2026 LinkedIn visuals (copy = FINAL (Felix), word for word)."""
import base64, html, sys, pathlib

OUT = pathlib.Path(sys.argv[1])
LOGO = base64.b64encode(pathlib.Path(sys.argv[2]).read_bytes()).decode()

BG, TXT, GREY, PINK, YEL, INK = "#0A0A0A", "#F5F5F5", "#A3A3A3", "#FF1FA9", "#FCD500", "#0A0A0A"

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300;1,9..144,400&family=Libre+Franklin:wght@400;500&family=IBM+Plex+Mono:wght@500;600&display=block');
@page {{ size: 1080px 1350px; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{ background: {BG}; }}
.page {{ width:1080px; height:1350px; position:relative; overflow:hidden; background:{BG}; color:{TXT};
  page-break-after: always; break-after: page; font-family:'Libre Franklin', sans-serif; }}
.page:last-child {{ page-break-after:auto; break-after:auto; }}
.mono {{ font-family:'IBM Plex Mono', monospace; font-weight:500; letter-spacing:0.08em; text-transform:uppercase; }}
.pill {{ display:inline-block; font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:28px; letter-spacing:0.1em;
  text-transform:uppercase; padding:12px 26px; border-radius:999px; line-height:1; }}
.pill.pink {{ background:{PINK}; color:{INK}; }}
.pill.yellow {{ background:{YEL}; color:{INK}; }}
.top {{ position:absolute; left:96px; right:96px; top:96px; }}
.content {{ position:absolute; left:96px; right:96px; top:300px; }}
.hero {{ position:absolute; left:96px; right:96px; top:0; bottom:260px; display:flex; flex-direction:column; justify-content:center; }}
h1 {{ font-family:'Fraunces', serif; font-weight:300; font-size:92px; line-height:1.08; letter-spacing:-0.01em; color:{TXT}; }}
h1.xl {{ font-size:104px; line-height:1.04; }}
.em {{ color:{YEL}; font-style:italic; }}
.body {{ font-size:46px; line-height:1.32; color:{TXT}; margin-top:44px; max-width:860px; }}
.num {{ display:inline-flex; align-items:center; justify-content:center; width:96px; height:96px; border-radius:999px;
  background:{PINK}; color:{INK}; font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:48px; margin-bottom:48px; }}
.rule-y {{ width:160px; height:6px; background:{YEL}; margin-bottom:48px; }}
.footer {{ position:absolute; left:96px; right:96px; bottom:84px; height:90px; display:flex; align-items:flex-end; justify-content:space-between; }}
.footer .url {{ font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:30px; letter-spacing:0.04em; color:{TXT}; }}
.logo {{ height:112px; display:block; }}
.tag {{ font-family:'Fraunces', serif; font-style:italic; font-weight:300; font-size:46px; color:{TXT}; line-height:1.1; }}
.strip {{ position:absolute; left:96px; right:96px; bottom:84px; border-top:3px solid {PINK}; padding-top:36px;
  display:flex; align-items:flex-end; justify-content:space-between; }}
/* timeline */
.tl {{ position:relative; height:60px; }}
.tl .line {{ position:absolute; left:0; right:0; top:29px; height:2px; background:#3A3A3A; }}
.tl .line.done {{ background:{PINK}; right:auto; }}
.tl .stops {{ position:absolute; inset:0; display:flex; justify-content:space-between; align-items:center; }}
.tl .stop {{ font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:24px; letter-spacing:0.06em; text-transform:uppercase;
  background:{BG}; color:{GREY}; padding:8px 12px; border-radius:999px; line-height:1; white-space:nowrap; }}
.tl .stop.on {{ background:{PINK}; color:{INK}; padding:12px 18px; }}
.tl .stop.hidden {{ color:transparent; background:transparent; }}
.tl .stop.hidden::after {{ content:''; }}
.dot {{ display:inline-block; width:14px; height:14px; border-radius:50%; background:#3A3A3A; }}
"""

def doc(title, pages):
    return f"<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"

LOGO_IMG = f"<img class='logo' src='data:image/png;base64,{LOGO}' alt='Convene X Events'>"

def footer(left=""):
    return f"<div class='footer'><div class='url'>{left}</div>{LOGO_IMG}</div>"

def e(s):
    return html.escape(s, quote=False)

# ---------------- Monday carousel (7) ----------------
def mon():
    p = []
    p.append(f"""<section class='page'><div class='hero'>
      <h1 class='xl'>Before a senior leader gives up an evening, they check <span class='em'>4</span> things.</h1>
      <p class='body'>The menu isn&#8217;t one of them.</p></div>{footer()}</section>""")
    checks = [
        ("1", "Who else is coming", "By role and seniority, not by name. A room of peers is the reason to say yes."),
        ("2", "Whether anyone will pitch", "Senior guests have sat through the dinner that became a demo. Once is enough."),
        ("3", "The question on the table", "A topic is vague. One sharp question is a reason to come."),
        ("4", "The terms of the room", "Chatham House Rule. How many seats. What time it ends."),
    ]
    for n, h, b in checks:
        p.append(f"""<section class='page'><div class='top'><span class='pill pink'>CHECK {n} OF 4</span></div>
          <div class='content' style='top:360px'><div class='num'>{n}</div><h1>{e(h)}</h1><p class='body'>{e(b)}</p></div>{footer()}</section>""")
    p.append(f"""<section class='page'><div class='top'><span class='pill pink'>IF YOU&#8217;RE HOSTING</span></div>
      <div class='content' style='top:360px'><div class='rule-y'></div><h1>Answer all 4 in the invitation</h1>
      <p class='body'>If the guest has to ask, it reads like it could have gone to anyone.</p></div>{footer()}</section>""")
    p.append(f"""<section class='page'><div class='top'><span class='pill pink'>SAVE THIS</span></div>
      <div class='content' style='top:360px'><h1 class='xl'>Who&#8217;s in the room is the event.</h1>
      <p class='body'>Save this for the next invitation you write.</p></div>{footer('convenexevents.com')}</section>""")
    return doc("Convene X LinkedIn Mon 16 Nov carousel", p)

# ---------------- Thursday carousel (8) ----------------
STAGES = ["BEFORE", "THE NIGHT", "WEEK 1", "WEEKS 2 TO 4", "WEEK 6"]

def timeline(cur):
    stops = []
    for i, s in enumerate(STAGES):
        if i == cur:
            stops.append(f"<span class='stop on'>{s}</span>")
        elif i < cur:
            stops.append(f"<span class='stop'>{s}</span>")
        else:
            stops.append("<span class='dot'></span>")
    return f"<div class='tl'><div class='line'></div><div class='stops'>{''.join(stops)}</div></div>"

def thu():
    p = []
    p.append(f"""<section class='page'><div class='hero'>
      <h1 class='xl'>Judge an executive dinner <span class='em'>6 weeks</span> after it ends.</h1>
      <p class='body'>Not on the night.</p></div>{footer()}</section>""")
    p.append(f"""<section class='page'><div class='top'><span class='pill pink'>THE GAP</span></div>
      <div class='content' style='top:300px'>
        <div style="font-family:'Fraunces',serif;font-weight:300;font-size:300px;line-height:0.95;color:{PINK};letter-spacing:-0.02em">38%</div>
        <p class='body' style='margin-top:40px'>of CMOs agree their events perform well. About half of organisations say they do.</p>
      </div>
      <div class='footer'><div class='mono' style='font-size:24px;color:{GREY};max-width:680px;line-height:1.4;letter-spacing:0.02em;text-transform:none'>Source: Forrester, The Next Era of B2B Events, 25 Jun 2026</div>{LOGO_IMG}</div></section>""")
    steps = [
        ("Agree what to look at first", "3 or 4 signals, chosen with the host before any invitation goes out."),
        ("Check the room against the list", "The right guests from the signed-off list. A conversation that went somewhere."),
        ("Follow up like a conversation", "Carry on what the table discussed. Something useful, not a deck."),
        ("Look at who leaned in", "Who replied. Who asked for a next conversation. Who introduced a colleague."),
        ("Take stock of the relationships", "Where each one stands, and whether guests would come again."),
    ]
    for i, (h, b) in enumerate(steps):
        p.append(f"""<section class='page'><div class='top'>{timeline(i)}</div>
          <div class='content' style='top:360px'><h1>{e(h)}</h1><p class='body'>{e(b)}</p></div>{footer()}</section>""")
    p.append(f"""<section class='page'><div class='top'><span class='pill pink'>WHAT WE WON&#8217;T PROMISE</span></div>
      <div class='content' style='top:300px'><h1 class='xl'>Leads, meetings or ROI.</h1>
      <p class='body'>These are things to look at, not outcomes anyone can guarantee.</p>
      <p class='tag' style='margin-top:96px;font-size:56px'>Who&#8217;s in the room is the event.</p>
      <p class='mono' style='margin-top:36px;font-size:26px;color:{TXT}'>SAVE THIS FOR YOUR NEXT POST-EVENT REPORT</p></div>
      {footer('convenexevents.com')}</section>""")
    return doc("Convene X LinkedIn Thu 19 Nov carousel", p)

# ---------------- Wednesday stat card ----------------
def wed():
    arrow = f"""<svg width='120' height='40' viewBox='0 0 120 40' style='margin:0 28px'><path d='M2 20 H112 M96 6 L114 20 L96 34' stroke='{TXT}' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"""
    p = [f"""<section class='page'><div class='top'><span class='pill pink'>NETWORKING, RATED BY ORGANISERS</span></div>
      <div class='content' style='top:300px;text-align:center'>
        <div style="display:flex;align-items:center;justify-content:center;font-family:'Fraunces',serif;font-weight:300;letter-spacing:-0.02em">
          <span style='font-size:200px;color:{GREY}'>46%</span>{arrow}<span style='font-size:250px;color:{YEL}'>15%</span></div>
        <p class='body' style='margin:40px auto 0;font-weight:500;max-width:820px'>Organisers who rate their networking &#8216;very effective&#8217;, 2025 to 2026.</p>
        <p class='mono' style='margin-top:48px;font-size:26px;color:{GREY};text-transform:none;letter-spacing:0.02em'>Source: Bizzabo 2026 State of Events Benchmark<br>(vendor survey)</p>
      </div>
      <p class='mono' style='position:absolute;left:96px;bottom:300px;font-size:26px;color:{TXT}'>SAVE THIS FOR YOUR NEXT GUEST LIST</p>
      <div class='strip'><span class='tag'>Who&#8217;s in the room is the event.</span>{LOGO_IMG}</div></section>"""]
    return doc("Convene X LinkedIn Wed 18 Nov stat card", p)

# ---------------- Saturday checklist card ----------------
def sat():
    items = ["One table, one conversation", "A door that shuts", "The quietest voice carries",
             "Close to the main stations", "Staff who serve around the talk"]
    rows = "".join(
        f"<li style='display:flex;align-items:center;gap:32px;margin-bottom:34px'><span class='num' style='width:72px;height:72px;font-size:36px;margin:0;flex:none'>{i}</span>"
        f"<span style='font-size:44px;line-height:1.2'>{e(t)}</span></li>" for i, t in enumerate(items, 1))
    streak = f"""<svg width='420' height='260' viewBox='0 0 420 260' style='position:absolute;left:0;top:0'>
      <defs><filter id='g' x='-50%' y='-50%' width='200%' height='200%'><feGaussianBlur stdDeviation='6'/></filter></defs>
      <path d='M-20 230 L330 -20' stroke='{PINK}' stroke-width='10' opacity='0.55' filter='url(#g)'/>
      <path d='M-20 230 L330 -20' stroke='{PINK}' stroke-width='3'/></svg>"""
    p = [f"""<section class='page'>{streak}<div class='top' style='top:200px'><span class='pill yellow'>THE LONDON ROOM</span></div>
      <div class='content' style='top:360px'><h1 style='font-size:92px'>5 things before the menu</h1>
      <ol style='list-style:none;margin-top:64px'>{rows}</ol></div>
      <div class='strip'><span class='tag'>Who&#8217;s in the room is the event.</span>{LOGO_IMG}</div></section>"""]
    return doc("Convene X LinkedIn Sat 21 Nov checklist card", p)

for name, fn in [("mon", mon), ("thu", thu), ("wed", wed), ("sat", sat)]:
    (OUT / f"{name}.html").write_text(fn(), encoding="utf-8")
print("ok")
