import json,subprocess,time,sys
OUT="/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video/stills/"
TAIL=(" seated at a candlelit private dining table in an upscale London restaurant at night, mid-conversation, "
"speaking with a relaxed, genuine expression, turned slightly toward a guest just out of frame, chest-up, "
"subject in the upper two-thirds of the frame, warm low candle light, dark wood and deep green walls, "
"wine glasses and white linen softly out of focus in the foreground, shallow depth of field, 50mm lens, "
"candid editorial photograph, natural skin texture, subtle film grain. No text, no logos, no name badges, no lanyards.")
PEOPLE=[
 "A British woman in her early 50s with a short silver bob, wearing a navy blazer,",
 "An American man in his mid 40s with a short dark beard, wearing an open-collar white shirt and charcoal jacket,",
 "A Black woman in her mid 40s with natural hair pulled back, wearing a black roll-neck and small gold earrings,",
 "A British man in his 60s with a neat grey beard, wearing a tweed jacket and tie-less blue shirt,",
 "A South Asian woman in her late 30s with shoulder-length dark hair, wearing a cream silk blouse,",
]
only=[int(a) for a in sys.argv[1:]] or range(1,6)
def curl(*a): return json.loads(subprocess.run(["curl","-sS",*a],capture_output=True,text=True).stdout)
tasks={}
for i in only:
    body={"model":"nano-banana-2","input":{"prompt":PEOPLE[i-1]+TAIL,"aspect_ratio":"9:16","resolution":"1K","output_format":"png"}}
    r=curl("-X","POST","https://api.kie.ai/api/v1/jobs/createTask","-H","Content-Type: application/json","-d",json.dumps(body))
    print(i,r); tasks[i]=r.get("data",{}).get("taskId"); time.sleep(1)
done={}
for _ in range(40):
    for i,t in tasks.items():
        if i in done or not t: continue
        d=curl(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={t}").get("data",{})
        if d.get("state")=="success":
            u=json.loads(d["resultJson"])["resultUrls"][0]
            dl=curl("-X","POST","https://api.kie.ai/api/v1/common/download-url","-H","Content-Type: application/json","-d",json.dumps({"url":u}))["data"]; subprocess.run(["curl","-sSL",dl,"-o",f"{OUT}exec{i}_raw.png"])
            done[i]=d.get("creditsConsumed"); print("done",i,"credits",done[i],u)
        elif d.get("state")=="fail": done[i]="FAIL"; print("fail",i,d)
    if len(done)==len(tasks): break
    time.sleep(10)
