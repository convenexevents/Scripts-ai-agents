import subprocess
V="/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video"
WH="/tmp/claude-0/-home-user-Scripts-ai-agents/d4f372cf-6872-5ec2-bb2c-03d8d867aa4b/scratchpad/ad/wh.wav"
S=[float(x) for x in open("starts3.txt").read().split()]
TOT=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","v3.mp4"],capture_output=True,text=True).stdout)
ins=[]; 
for i in range(1,6): ins+=["-i",f"{V}/v2/voices/exec{i}.mp3"]
ins+=["-stream_loop","1","-i",f"{V}/voices/ambience.mp3"]+["-i",WH]*4
f=[]
for i,s in enumerate(S): ms=int(s*1000); f.append(f"[{i}]adelay={ms}|{ms}[v{i}]")
f.append("".join(f"[v{i}]" for i in range(5))+"amix=inputs=5:normalize=0[vox]")
f.append(f"[5]atrim=0:{TOT},volume=0.16,afade=t=in:d=0.5,afade=t=out:st={TOT-1.2}:d=1.2[amb]")
for k in range(4): ms=max(0,int(S[k+1]*1000)-150); f.append(f"[{6+k}]volume=0.22,adelay={ms}|{ms}[w{k}]")
f.append(f"[vox][amb][w0][w1][w2][w3]amix=inputs=6:normalize=0,apad,atrim=0:{TOT},loudnorm=I=-14:TP=-1.5:LRA=11")
subprocess.run(["ffmpeg","-y","-v","error",*ins,"-filter_complex",";".join(f),"-ar","48000","-ac","2","mix3.wav"],check=True)
OUT=f"{V}/convene-x-ad-v3-kling-9x16.mp4"
subprocess.run(["ffmpeg","-y","-v","error","-i","v3.mp4","-i","mix3.wav","-c:v","copy","-c:a","aac","-b:a","192k","-shortest",OUT],check=True)
print(OUT,TOT,S)
