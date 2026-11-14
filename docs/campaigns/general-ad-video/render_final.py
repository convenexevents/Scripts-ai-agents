import subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
BLACK=(10,10,10); PINK=(255,31,169); YEL=(252,213,0); OFF=(245,245,245); GREY=(58,58,58); MID=(163,163,163)
F="/usr/share/fonts/opentype/inter/"
def font(n,s): return ImageFont.truetype(F+n,s)
BOLD=font("Inter-Bold.otf",96); XB=font("Inter-ExtraBold.otf",104); SMALL=font("Inter-Medium.otf",34); TAG=font("Inter-SemiBold.otf",30)
SHOTS=[ # (start,end, line, highlight word, placeholder note, bg tint)
 (0.0,2.2,"Real conversations.","Real","EXEC 1 · UK · woman, 50s · warm, measured",(40,20,32)),
 (2.2,4.2,"With genuine peers.","peers.","EXEC 2 · US · man, 40s · relaxed, direct",(22,26,40)),
 (4.2,6.4,"Director level and above.","Director","EXEC 3 · Germany · woman, 40s · crisp",(36,30,16)),
 (6.4,8.4,"Invitation only.","only.","EXEC 4 · UK · man, 60s · dry, low",(18,34,30)),
 (8.4,10.4,"And nobody sells.","nobody","EXEC 5 · France · woman, 30s · half-smile",(40,18,22)),
]
END=(10.4,14.0)
TOTAL=END[1]
STILL="/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video/stills/exec{}_raw.png"
_cache={}
def base(n):
    if n not in _cache:
        im=Image.open(STILL.format(n)).convert("RGB")
        s=max(W/im.width,H/im.height)*1.08
        im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,60,2))
        g=Image.new("L",(1,H))
        for y in range(H): g.putpixel((0,y),int(max(0,(y-H*0.55)/(H*0.45))*215) if y>H*0.55 else int(max(0,(H*0.12-y)/(H*0.12))*140))
        _cache[n]=(im,g.resize((W,H)))
    return _cache[n]
def photo(n,p):
    im,g=base(n); z=1.0+0.06*p            # slow push-in over the shot
    w2=im.width/(1.08*z); h2=im.height/(1.08*z)
    cx=im.width/2+(p-0.5)*20; cy=im.height*0.46
    l=min(max(cx-w2/2,0),im.width-w2); t=min(max(cy-h2/2,0),im.height-h2)
    fr=im.crop((int(l),int(t),int(l+w2),int(t+h2))).resize((W,H),Image.BILINEAR)
    return Image.composite(Image.new("RGB",(W,H),BLACK),fr,g)
def bg(tint,zoom):
    im=Image.new("RGB",(W,H),BLACK); d=ImageDraw.Draw(im)
    for y in range(0,H,8):
        t=y/H; c=tuple(int(BLACK[i]+(tint[i]-BLACK[i])*(1-abs(t-0.4)*1.4 if abs(t-0.4)<0.7 else 0)) for i in range(3))
        d.rectangle([0,y,W,y+8],fill=c)
    # silhouette placeholder, scaled by zoom
    cx,cy=W//2,int(H*0.43); s=zoom
    d.ellipse([cx-150*s,cy-330*s,cx+150*s,cy+20*s],fill=GREY)
    d.rounded_rectangle([cx-330*s,cy+70*s,cx+330*s,cy+700*s],radius=int(260*s),fill=GREY)
    return im
def text_w(d,t,f): return d.textlength(t,font=f)
def caption(d,line,hl,alpha):
    words=line.split(" "); f=XB
    # wrap into lines max width 900
    lines=[];cur=[]
    for w in words:
        if cur and text_w(d," ".join(cur+[w]),f)>900: lines.append(cur);cur=[w]
        else: cur.append(w)
    lines.append(cur)
    y=int(H*0.76)
    for ln in lines:
        tw=text_w(d," ".join(ln),f); x=(W-tw)/2
        for w in ln:
            col=PINK if w==hl else OFF
            col=tuple(int(c*alpha+BLACK[i]*(1-alpha)) for i,c in enumerate(col))
            d.text((x+3,y+4),w,font=f,fill=(0,0,0)); d.text((x,y),w,font=f,fill=col)
            x+=text_w(d,w+" ",f)
        y+=125
def chrome(d,note):
    d.text((60,80),"CONVENE X",font=TAG,fill=OFF)
    d.rectangle([60,124,140,128],fill=PINK)
    d.text((W-60-text_w(d,"AI-generated",SMALL),84),"AI-generated",font=SMALL,fill=MID)

def endcard(t):
    im=Image.new("RGB",(W,H),BLACK); d=ImageDraw.Draw(im)
    a=min(1,t/0.4)
    def c(col,k=1): 
        aa=max(0,min(1,(t-k*0.25)/0.35)); return tuple(int(v*aa) + int(BLACK[i]*(1-aa)) for i,v in enumerate(col))
    d.rectangle([60,620,60+int(160*a),628],fill=PINK)
    d.text((60,660),"CONVENE X",font=font("Inter-ExtraBold.otf",150),fill=c(OFF,0))
    d.text((60,830),"EVENTS",font=font("Inter-ExtraBold.otf",150),fill=c(PINK,0))
    d.text((60,1040),"Executive dinners, roundtables",font=font("Inter-Medium.otf",54),fill=c(OFF,1))
    d.text((60,1110),"and webinars for senior leaders.",font=font("Inter-Medium.otf",54),fill=c(OFF,1))
    # button
    bc=c(YEL,2); d.rounded_rectangle([60,1290,840,1410],radius=60,fill=bc)
    d.text((110,1318),"Book a 15-minute call",font=font("Inter-Bold.otf",56),fill=BLACK if t>0.6 else bc)
    d.text((60,1480),"convenexevents.com",font=font("Inter-SemiBold.otf",50),fill=c(MID,3))
    return im
cmd=["ffmpeg","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",sys.argv[1]]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
n=int(TOTAL*FPS)
for i in range(n):
    t=i/FPS
    sh=[s for s in SHOTS if s[0]<=t<s[1]]
    if sh:
        s0,s1,line,hl,note,tint=sh[0]; lt=t-s0
        idx=[x[0] for x in SHOTS].index(s0)+1
        im=photo(idx,lt/(s1-s0)); d=ImageDraw.Draw(im)
        caption(d,line,hl,min(1,max(0,(lt-0.1)/0.2))); chrome(d,note)
        if lt<2/FPS: im=Image.blend(im,Image.new("RGB",(W,H),OFF),0.6)  # cut flash
    else:
        im=endcard(t-END[0])
    p.stdin.write(im.tobytes())
p.stdin.close(); p.wait()
