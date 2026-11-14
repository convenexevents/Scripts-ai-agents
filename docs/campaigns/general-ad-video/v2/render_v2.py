import sys, subprocess, numpy as np, cv2
sys.path.insert(0,"/tmp/claude-0/ls")
from lipsync import Face, envelope
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
BLACK=(10,10,10); PINK=(255,31,169); YEL=(252,213,0); OFF=(245,245,245); MID=(163,163,163)
F="/usr/share/fonts/opentype/inter/"; font=lambda n,s: ImageFont.truetype(F+n,s)
CAP=font("Inter-ExtraBold.otf",78); TAG=font("Inter-SemiBold.otf",30); SMALL=font("Inter-Medium.otf",34)
LINES=[("Most events fill the room. Not many fill it with the right people.","right"),
 ("I've sat through dinners that turned into a sales demo before the starters arrived.","demo"),
 ("Here, every guest is Director level or above, and every seat is by invitation.","Director"),
 ("The host signs off the guest list. And nobody pitches at the table.","nobody"),
 ("You just get a proper conversation, with people who do what you do.","proper")]
LEAD=0.15; TAIL=0.35
durs=[float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video/v2/voices/exec{i}.mp3"],capture_output=True,text=True).stdout) for i in range(1,6)]
shots=[]; t=0
for i,d in enumerate(durs): shots.append((t,t+LEAD+d+TAIL,i+1)); t+=LEAD+d+TAIL
END=(t,t+3.5); TOTAL=END[1]
open(sys.argv[2],"w").write(" ".join(f"{s[0]+LEAD:.3f}" for s in shots))
grad=Image.new("L",(1,H))
for y in range(H): grad.putpixel((0,y),int(min(215,max(0,(y-H*0.52)/(H*0.48))*240)) if y>H*0.52 else int(max(0,(H*0.12-y)/(H*0.12))*140))
grad=grad.resize((W,H))
def caption(d,line,hl,alpha):
    words=line.split(" "); lines=[];cur=[]
    for w in words:
        if cur and d.textlength(" ".join(cur+[w]),font=CAP)>940: lines.append(cur);cur=[w]
        else: cur.append(w)
    lines.append(cur); y=int(H*0.70)
    for ln in lines:
        x=(W-d.textlength(" ".join(ln),font=CAP))/2
        for w in ln:
            col=PINK if w.strip(".,").startswith(hl) else OFF
            col=tuple(int(c*alpha+BLACK[i]*(1-alpha)) for i,c in enumerate(col))
            d.text((x+3,y+4),w,font=CAP,fill=(0,0,0)); d.text((x,y),w,font=CAP,fill=col)
            x+=d.textlength(w+" ",font=CAP)
        y+=96
def endcard(t):
    im=Image.new("RGB",(W,H),BLACK); d=ImageDraw.Draw(im)
    def c(col,k):
        a=max(0,min(1,(t-k*0.25)/0.35)); return tuple(int(v*a+BLACK[i]*(1-a)) for i,v in enumerate(col))
    d.rectangle([60,620,60+int(160*min(1,t/0.4)),628],fill=PINK)
    d.text((60,660),"CONVENE X",font=font("Inter-ExtraBold.otf",150),fill=c(OFF,0))
    d.text((60,830),"EVENTS",font=font("Inter-ExtraBold.otf",150),fill=c(PINK,0))
    d.text((60,1040),"Executive dinners, roundtables",font=font("Inter-Medium.otf",54),fill=c(OFF,1))
    d.text((60,1110),"and webinars for senior leaders.",font=font("Inter-Medium.otf",54),fill=c(OFF,1))
    bc=c(YEL,2); d.rounded_rectangle([60,1290,840,1410],radius=60,fill=bc)
    d.text((110,1318),"Book a 15-minute call",font=font("Inter-Bold.otf",56),fill=BLACK if t>0.6 else bc)
    d.text((60,1480),"convenexevents.com",font=font("Inter-SemiBold.otf",50),fill=c(MID,3))
    return im
faces={}; envs={}
for s0,s1,n in shots:
    faces[n]=Face(n); nf=int((s1-s0)*FPS)+2
    e=envelope(n,nf); envs[n]=np.concatenate([np.zeros(int(LEAD*FPS)),e])[:nf]
cmd=["ffmpeg","-y","-v","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",sys.argv[1]]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for i in range(int(TOTAL*FPS)):
    t=i/FPS; sh=[s for s in shots if s[0]<=t<s[1]]
    if sh:
        s0,s1,n=sh[0]; k=int((t-s0)*FPS); f=faces[n]; prog=(t-s0)/(s1-s0)
        src=Image.fromarray(cv2.cvtColor(f.frame(float(envs[n][min(k,len(envs[n])-1)])),cv2.COLOR_BGR2RGB))
        z=1.0+0.05*prog; sc=max(W/src.width,H/src.height)*1.06*z
        big=src.resize((round(src.width*sc),round(src.height*sc)),Image.BILINEAR)
        cx=big.width/2+(prog-0.5)*16; cy=big.height*0.46
        l=int(min(max(cx-W/2,0),big.width-W)); tp=int(min(max(cy-H/2,0),big.height-H))
        im=Image.composite(Image.new("RGB",(W,H),BLACK),big.crop((l,tp,l+W,tp+H)),grad)
        d=ImageDraw.Draw(im)
        caption(d,*LINES[n-1],min(1,max(0,(t-s0-0.1)/0.2)))
        d.text((60,80),"CONVENE X",font=TAG,fill=OFF); d.rectangle([60,124,140,128],fill=PINK)
        d.text((W-60-d.textlength("AI-generated",font=SMALL),84),"AI-generated",font=SMALL,fill=MID)
        if t-s0<2/FPS and s0>0: im=Image.blend(im,Image.new("RGB",(W,H),OFF),0.5)
    else: im=endcard(t-END[0])
    p.stdin.write(im.tobytes())
p.stdin.close(); p.wait(); print("total",round(TOTAL,2))
