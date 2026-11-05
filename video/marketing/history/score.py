import json, subprocess, numpy as np, wave, os
D=os.path.dirname(os.path.abspath(__file__))+'/'
TL=json.load(open(D+'timeline.json')); SR=44100; T=TL['duration']+0.5; n=int(SR*T); t=np.arange(n)/SR
SC={s['id']:s for s in TL['scenes']}; LN=TL['lines']
def L(sc,k): return [l for l in LN if l['scene']==sc][k]['start']
def env(a,b,fa=1.0,fb=1.0):
    e=np.zeros(n); e[(t>=a)&(t<b)]=1
    return e*np.clip((t-a)/fa,0,1)*np.clip((b-t)/fb,0,1)
mix=np.zeros(n)
def note(f,start,dur,amp=0.3,harm=(1,.5,.25,.12),dec=2.5):
    s=int(start*SR); m=min(n-s,int(dur*SR))
    if m<=0 or s<0: return
    tt=np.arange(m)/SR; w=sum(h*np.sin(2*np.pi*f*(k+1)*tt) for k,h in enumerate(harm))
    mix[s:s+m]+=amp*w*np.exp(-tt*dec)*np.minimum(1,tt/0.006)
def pad(freqs,a,b,amp,fa=1.5,fb=1.5,bright=4):
    e=env(a,b,fa,fb); w=np.zeros(n)
    for f in freqs:
        for k in range(1,bright+1): w+=np.sin(2*np.pi*f*k*t*(1+0.0007*k)+k)/k**1.6
    return amp*e*w*(0.85+0.15*np.sin(2*np.pi*0.2*t))
def lp(x,k=40): return np.convolve(x,np.ones(k)/k,'same')
rng=np.random.default_rng(3); noise=rng.standard_normal(n)
def riser(at,length=3.0,amp=0.08):
    global mix
    ramp=np.clip((t-(at-length))/length,0,1)*(t<at); mix+=amp*ramp**2*(noise-lp(noise,6))
    for f in (330,440,660): mix+=0.02*ramp**2*np.sin(2*np.pi*f*(1+ramp*0.05)*t)
def hit(at,amp=0.8):
    note(55,at,3,amp,(1,.5,.2),1.6); note(41,at,3,amp*0.7,(1,),1.2); global mix; mix+=0.06*lp(env(at,at+1.6,0.005,1.4)*noise,3)
# Opening: airy pad, single bells on each year
mix+=pad([146.83,220.0],0,SC['search']['start']+1,0.035,3,1,3)
h=LN[1]; [note(880*(1+0.25*i),h['start']+i*h['dur']/3,3,0.05,(1,.3),1.4) for i in range(3)]
note(1174.66,L('hist',2),3,0.05,(1,.3),1.2)
riser(L('hist',3)+0.4,3.2,0.09); hit(L('hist',3)+0.4,0.7)
# Main bed: hopeful D - A - Bm - G (I-V-vi-IV), tempo builds
prog=[[146.83,185.0,220.0],[110.0,138.59,164.81],[123.47,146.83,185.0],[98.0,123.47,146.83]]
def bpm_at(x): return 84 if x<SC['sems']['start'] else (92 if x<SC['good']['start'] else 96)
k=0; tt0=SC['search']['start']
while tt0<T-4:
    bar=4*60/bpm_at(tt0); ch=prog[k%4]
    lift=1.0+0.25*(tt0>SC['sems']['start'])+0.2*(tt0>SC['good']['start'])
    mix+=pad([c/2 for c in ch]+ch,tt0,tt0+bar+0.3,0.03*lift,0.5,0.6,4)
    for j in range(8): note(ch[j%3]*(2 if j>=3 else 1),tt0+j*bar/8,1.3,0.075*lift,(1,.4,.15),2.8)
    if tt0>SC['sems']['start']:
        for j in range(4): note(ch[0]/2,tt0+j*bar/4,0.4,0.12,(1,.3),9)   # soft pulse
    if tt0>SC['blend']['start']: note(ch[2]*4,tt0,2.2,0.035,(1,.2),1.6)  # sparkle
    k+=1; tt0+=bar
# Lifts at key turns
for at in (SC['syl']['start']+0.4, SC['wall']['start']+0.3, L('good',0)+1.3, SC['cta']['start']+0.3):
    riser(at,2.6,0.06); hit(at,0.5)
# Final: big open chord on "Let it remember your college."
end=L('cta',3); riser(end,3,0.08); hit(end,0.9)
mix+=pad([73.42,146.83,185.0,220.0,293.66],end,T,0.05,0.05,3,5)
mix*=np.clip((T-t)/3,0,1)*np.clip(t/1.5,0,1)
voice=np.zeros(n)
for l in LN:
    raw=subprocess.check_output(['ffmpeg','-loglevel','error','-i',D+f"vo/l{l['i']:02d}.mp3",'-f','s16le','-ac','1','-ar',str(SR),'-'])
    a=np.frombuffer(raw,np.int16)/32768; s=int(l['start']*SR); voice[s:s+len(a)]+=a[:n-s]
venv=lp(np.abs(voice),SR//6); duck=1-0.5*np.clip(venv*10,0,1)
music=mix/np.max(np.abs(mix))*0.45
out=voice+music*duck; out=np.clip(out/np.max(np.abs(out))*0.95,-1,1)
w=wave.open(D+'mix.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',round(T,1))
