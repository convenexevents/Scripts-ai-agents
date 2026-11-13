import sys, pathlib
SRC = pathlib.Path(sys.argv[1]); LOGO = sys.argv[2]; OUTD = pathlib.Path(sys.argv[3])
src = SRC.read_text().split("# ---------------- Monday carousel")[0]
sys.argv = ["gen.py", str(OUTD), LOGO]
exec(src)

def li(items, size=40):
    r = "".join(f"<li style='display:flex;gap:28px;align-items:flex-start;margin-bottom:26px'><span class='num' style='width:64px;height:64px;font-size:32px;margin:0;flex:none'>{i}</span><span style='font-size:{size}px;line-height:1.25;padding-top:8px'>{e(t)}</span></li>" for i, t in enumerate(items, 1))
    return f"<ol style='list-style:none;margin-top:44px'>{r}</ol>"

def fmt(items):
    r = "".join(f"<div style='border-left:6px solid {PINK};padding:4px 0 4px 28px;margin-bottom:18px'><div style=\"font-family:'Fraunces',serif;font-weight:400;font-size:46px;line-height:1.1\">{e(a)}</div><div style='font-size:34px;line-height:1.3;color:{TXT};margin-top:8px'>{e(b)}</div></div>" for a, b in items)
    return f"<div style='margin-top:44px'>{r}</div>"

def card(pill, h1, mid, pillcls="pink", h1size=76, topc=270):
    return f"""<section class='page'><div class='top'><span class='pill {pillcls}'>{e(pill)}</span></div>
      <div class='content' style='top:{topc}px'><h1 style='font-size:{h1size}px'>{h1}</h1>{mid}</div>{footer('convenexevents.com')}</section>"""

cards = {
"1-fri13-1200-three-formats": card("3 FORMATS", "3 ways to meet the senior leaders you actually want to meet.",
  fmt([("Executive dinners","6 to 20 guests, one moderated conversation."),("Virtual roundtables","6 to 12 senior leaders, about an hour."),("Executive webinars","A larger audience, gated to the titles you choose.")])
  + f"<p class='body' style='font-size:36px;margin-top:8px'>We find the guests and check every one against your brief.</p>", h1size=60, topc=232),
"2-fri13-1600-why-small-rooms": card("SMALL ROOMS", "A conference gives you reach. A small room gives you depth.",
  "<p class='body' style='font-size:38px;margin-top:36px'>At a table of 10, everyone hears everyone.</p><p class='body' style='font-size:38px;margin-top:28px'>3 things change in a small room:</p>"
  + li(["Everyone gets to speak.","The question on the invitation shapes the evening.","Peers compare notes instead of trading pitches."], 38), h1size=72, topc=250),
"3-sun15-1100-chatham-house": card("THE CHATHAM HOUSE RULE", "You can use what you hear, but you can&#8217;t say who said it or which company they work for.",
  "<p class='body' style='font-size:44px;margin-top:56px'>We design every room around it: no names, no attributed quotes, no public list of who was there afterwards.</p>", h1size=68, topc=290),
"4-mon16-1500-guest-list": card("THE GUEST LIST", "For a sponsor, the guest list is the whole point.",
  li(["You tell us who you want to meet.","We check every guest against that brief.","If someone doesn&#8217;t fit the conversation, they don&#8217;t get the seat.","For dinners and roundtables, you sign off the final list."], 40).replace("&amp;#8217;","&#8217;"), h1size=80, topc=290),
"5-tue17-1500-virtual-roundtables": card("VIRTUAL ROUNDTABLES", "10 executives, 10 cities, one table.",
  "<p class='body' style='font-size:40px;margin-top:32px'>6 to 12 senior leaders. About an hour.</p>"
  + li(["One question, sent with the invitation.","A guest list checked against a brief and signed off by the host.","A moderator who makes sure the quietest person is heard."], 38), h1size=84, topc=270),
"6-wed18-1500-best-question": card("THE BEST QUESTION", "Every room we plan starts with one question. We&#8217;re collecting good ones.",
  "<p class='body' style='font-size:42px;margin-top:52px'>What&#8217;s the best question you&#8217;ve been asked at an event, or wish someone had asked?</p><p class='body' style='font-size:38px;margin-top:36px;color:#F5F5F5'>Reply with it. We read every one.</p>", h1size=76, topc=290),
}
for k, v in cards.items():
    (OUTD / f"{k}.html").write_text(doc(k, [v]), encoding="utf-8")
print("ok")
