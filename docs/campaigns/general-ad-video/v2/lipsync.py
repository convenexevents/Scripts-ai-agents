import cv2, numpy as np, subprocess, mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions
STILLS="/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video/stills/exec{}_raw.png"
VOX="/home/user/Scripts-ai-agents/docs/campaigns/general-ad-video/v2/voices/exec{}.mp3"
FPS=30
_lm=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path="/tmp/claude-0/face_landmarker.task"),num_faces=3))
UP_IN=[78,191,80,81,82,13,312,311,310,415,308]
LO_IN=[78,95,88,178,87,14,317,402,318,324,308]
def landmarks(img):
    h,w=img.shape[:2]
    r=_lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)))
    # pick largest face (the subject)
    best=max(r.face_landmarks,key=lambda f:(max(p.x for p in f)-min(p.x for p in f)))
    return np.array([[p.x*w,p.y*h] for p in best],np.float32)
def envelope(n,frames):
    pcm=subprocess.run(["ffmpeg","-v","error","-i",VOX.format(n),"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    x=np.frombuffer(pcm,np.int16).astype(np.float32)/32768
    hop=16000//FPS; env=[]
    for i in range(frames):
        s=x[i*hop:(i+1)*hop]; env.append(np.sqrt(np.mean(s**2)) if len(s) else 0)
    env=np.array(env); ref=np.percentile(env[env>0.005],90) if (env>0.005).any() else 1
    a=np.clip((env-0.012)/(ref-0.012),0,1)**0.8
    out=np.zeros_like(a); v=0
    for i,t in enumerate(a):  # fast attack, slower release
        v = v+(t-v)*(0.7 if t>v else 0.35); out[i]=v
    return out
class Face:
    def __init__(s,n):
        s.img=cv2.imread(STILLS.format(n)); s.L=landmarks(s.img); L=s.L
        s.w=np.linalg.norm(L[61]-L[291]); s.cx=(L[61][0]+L[291][0])/2
        s.ytop=L[13][1]; s.ychin=L[152][1]
        h,w=s.img.shape[:2]; s.gx,s.gy=np.meshgrid(np.arange(w,dtype=np.float32),np.arange(h,dtype=np.float32))
        s.fx=np.exp(-((s.gx-s.cx)/(0.75*s.w))**2)
        fy=np.clip((s.gy-s.ytop)/(0.10*s.w),0,1)
        below=np.clip(1-(s.gy-s.ychin)/(0.45*s.w),0,1)
        s.field=(s.fx*fy*np.where(s.gy>s.ychin,below,1)).astype(np.float32)
    def frame(s,a):
        # jaw movement only: -0.06w (lips closer) .. +0.13w (open), real teeth and lips kept
        op=(a*0.24-0.06)*s.w
        return cv2.remap(s.img,s.gx,s.gy-op*s.field,cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT)
if __name__=="__main__":
    f=Face(1); print("mouth width px",f.w)
    tiles=[]
    for a in [0,0.3,0.6,1.0]:
        im=f.frame(a); L=f.L; x0,y0=int(f.cx-1.6*f.w),int(f.ytop-1.6*f.w)
        c=im[y0:y0+int(3.2*f.w),x0:x0+int(3.2*f.w)]; tiles.append(cv2.resize(c,(400,400)))
    cv2.imwrite("/tmp/claude-0/ls/test.png",np.hstack(tiles))
    print(envelope(1,120)[::6].round(2))
