import json,subprocess,sys,time
def curl(*a):
    o=subprocess.run(["curl","-sS",*a],capture_output=True,text=True).stdout
    try: return json.loads(o)
    except Exception: return {"raw":o[:300]}
model,img,aud,out=sys.argv[1:5]; prompt=sys.argv[5] if len(sys.argv)>5 else ""
body={"model":model,"input":{"image_url":img,"audio_url":aud,"prompt":prompt}}
r=curl("-X","POST","https://api.kie.ai/api/v1/jobs/createTask","-H","Content-Type: application/json","-d",json.dumps(body)); print(r,flush=True)
t=r.get("data",{}).get("taskId")
for _ in range(120):
    if not t: break
    d=curl(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={t}").get("data",{})
    if d.get("state") in("success","fail"):
        print(d.get("state"),d.get("creditsConsumed"),d.get("failMsg"),flush=True)
        if d["state"]=="success":
            u=json.loads(d["resultJson"])["resultUrls"][0]
            dl=curl("-X","POST","https://api.kie.ai/api/v1/common/download-url","-H","Content-Type: application/json","-d",json.dumps({"url":u})).get("data",u)
            subprocess.run(["curl","-sSL",dl,"-o",out]); print("saved",out)
        break
    time.sleep(10)
