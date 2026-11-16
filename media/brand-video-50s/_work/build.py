import subprocess,os
B="/home/user/Scripts-ai-agents/media/brand-video-50s/"; W=B+"_work/edit/"; S=B+"stills/"
FPS=24; FONT="/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
GRADE="vignette=PI/5,noise=alls=5:allf=t,format=yuv420p"
def ff(args): subprocess.run(["ffmpeg","-v","error","-y"]+args,check=True)
# (start,end,type,src,params)
T=[
(0.0,3.6,"clip","01-conference-chaos.mp4",dict(ss=0.5,crop="1160:652:300:430")),
(3.6,7.4,"still","13-conference-crowd",dict(z=(1.35,1.45),f=(0.5,0.78),f2=(0.5,0.8))),
(7.4,11.9,"still","14-bored-watch",dict(z=(1.0,1.12),f=(0.55,0.55))),
(11.9,15.8,"clip","02-banquet-boredom.mp4",dict(ss=0.0)),
(15.8,20.0,"still","15-banquet-rows",dict(z=(1.0,1.1),f=(0.5,0.5))),
(20.0,24.0,"clip","03-sommelier-pour.mp4",dict(ss=0.5)),
(24.0,27.9,"still","03-projector-pitch",dict(z=(1.0,1.12),f=(0.6,0.45))),
(27.9,32.9,"still","16-sommelier-detail",dict(z=(1.12,1.0),f=(0.5,0.5))),
(32.9,36.6,"still","09-dining-room-empty",dict(z=(1.0,1.12),f=(0.5,0.6))),
(36.6,39.8,"still","17-city-night-arrival",dict(z=(1.0,1.1),f=(0.7,0.5))),
(39.8,43.2,"still","10-host-welcome",dict(z=(1.05,1.15),f=(0.4,0.45))),
(43.2,46.6,"still","08-place-setting",dict(z=(1.15,1.0),f=(0.5,0.5))),
(46.6,53.2,"clip","05a-round-table.mp4",dict(ss=1.0)),
(53.2,58.4,"still","04-diverse-round-table",dict(z=(1.25,1.35),f=(0.45,0.62))),
(58.4,62.0,"still","01-close-woman-nodding",dict(z=(1.0,1.1),f=(0.55,0.4))),
(62.0,64.4,"still","02-close-notebook",dict(z=(1.15,1.25),f=(0.6,0.6))),
(64.4,66.9,"still","07-glass-toast",dict(z=(1.0,1.1),f=(0.5,0.5))),
(66.9,71.0,"clip","05b-round-table.mp4",dict(ss=2.0)),
(71.0,73.4,"still","12-listener-profile",dict(z=(1.0,1.08),f=(0.6,0.45))),
(73.4,75.8,"still","11-woman-speaking",dict(z=(1.0,1.1),f=(0.5,0.4))),
(75.8,78.3,"still","05-two-execs-laughing",dict(z=(1.08,1.0),f=(0.5,0.5))),
(78.3,86.0,"ring","07-neon-ring.mp4",dict(ss=1.0)),
(86.0,96.0,"end",None,{}),
]
segs=[]
for i,(a,b,typ,src,p) in enumerate(T):
    d=round(b-a,3); n=round(d*FPS); out=f"{W}seg{i:02d}.mp4"; segs.append(out)
    if i not in (1,21): continue
    d=round(b-a,3); n=round(d*FPS); out=f"{W}seg{i:02d}.mp4"; segs.append(out)
    if typ=="clip":
        crop=f"crop={p['crop']}," if 'crop' in p else "crop=1920:1080:0:4,"
        ff(["-ss",str(p['ss']),"-i",B+src,"-t",str(d),"-vf",f"{crop}scale=1920:1080:flags=lanczos,fps={FPS},{GRADE}","-an","-c:v","libx264","-crf","17","-preset","medium",out])
    elif typ=="still":
        z0,z1=p['z']; fx,fy=p['f']; fx2,fy2=p.get('f2',p['f'])
        z=f"({z0}+({z1}-{z0})*on/{n})"
        cx=f"({fx}+({fx2}-{fx})*on/{n})"; cy=f"({fy}+({fy2}-{fy})*on/{n})"
        x=f"max(0,min(iw-iw/zoom,{cx}*iw-iw/zoom/2))"; y=f"max(0,min(ih-ih/zoom,{cy}*ih-ih/zoom/2))"
        vf=f"scale=5504:3072:flags=lanczos,zoompan=z='{z}':x='{x}':y='{y}':d={n}:s=1920x1080:fps={FPS},{GRADE}"
        ff(["-i",S+src+".jpg","-vf",vf,"-frames:v",str(n),"-c:v","libx264","-crf","17","-preset","medium",out])
    elif typ=="ring":
        # neon ring + logo fading in (screen blend, logo has black bg)
        fc=(f"[0]crop=1920:1080:0:4,fps={FPS},format=gbrp[v];[1]scale=1100:-2,pad=1920:1080:(ow-iw)/2:(oh-ih)/2-30:black,fps={FPS},format=gbrp,fade=in:st=0.4:d=1.2[l];"
            f"[v][l]blend=all_mode=screen,{GRADE}")
        ff(["-ss",str(p['ss']),"-i",B+src,"-loop","1","-t",str(d),"-i",B+"logo-endcard.png","-t",str(d),"-filter_complex",fc,"-an","-c:v","libx264","-crf","17",out])
    elif typ=="end":
        fc=(f"color=black:s=1920x1080:r={FPS}:d={d}[bg];"
            f"[0]scale=1100:-2[l];[bg][l]overlay=110:(H-h)/2-90[a];"
            f"[1]scale=-2:980,format=rgba,split[e][g];"
            f"[g]alphaextract,format=gray,geq=lum='p(X,Y)',boxblur=18:2,format=gray[m];"
            f"color=0xFF1FA9:s=345x980:d={d},format=rgba[pc];[pc][m]scale2ref[pc2][m2];[pc2][m2]alphamerge,colorchannelmixer=aa=0.55[glow];"
            f"[glow]fade=in:st=1.6:d=1.4:alpha=1[glow2];[e]fade=in:st=1.4:d=1.4:alpha=1[e2];"
            f"[a][glow2]overlay=1395:70[a2];[a2][e2]overlay=1395:70[a3];"
            f"[a3]drawtext=fontfile={FONT}:text='Book a 15-minute intro call':fontsize=56:fontcolor=white:x=110+(1100-tw)/2:y=840:alpha='min(1,max(0,(t-0.6)/0.8))',"
            f"drawtext=fontfile={FONT}:text='convenexevents.com':fontsize=42:fontcolor=0xFCD500:x=110+(1100-tw)/2:y=920:alpha='min(1,max(0,(t-1.0)/0.8))',"
            f"fade=out:st={d-1.2}:d=1.2,{GRADE}")
        ff(["-loop","1","-t",str(d),"-i",B+"logo-endcard.png","-loop","1","-t",str(d),"-i",B+"eva-upscaled.png","-filter_complex",fc,"-frames:v",str(n),"-c:v","libx264","-crf","17",out])
    print("built",i,typ,src,d,flush=True)
open(W+"list.txt","w").write("".join(f"file '{s}'\n" for s in segs))
ff(["-f","concat","-safe","0","-i",W+"list.txt","-c","copy",W+"video.mp4"])
ff(["-i",W+"video.mp4","-i",B+"vo-georgia.mp3","-filter_complex","[1]apad,atrim=0:96,afade=t=out:st=94.5:d=1.5,loudnorm=I=-14:TP=-1.5:LRA=11[a];[0]fade=in:st=0:d=0.6[v]",
    "-map","[v]","-map","[a]","-c:v","libx264","-crf","21","-preset","slow","-maxrate","12M","-bufsize","24M","-c:a","aac","-b:a","192k","-movflags","+faststart","-t","96",B+"convenex-brand-film-draft-v1.mp4"])
print("done")
