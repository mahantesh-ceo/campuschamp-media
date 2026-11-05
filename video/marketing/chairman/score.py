import json, subprocess, numpy as np, wave
D='/tmp/claude-0/-home-user/9ed5ad7e-b576-5f9e-8769-1c9b95945112/scratchpad/chair/'
TL=json.load(open(D+'timeline.json')); SR=44100; T=TL['duration']+0.5; n=int(SR*T); t=np.arange(n)/SR
SC={s['id']:s for s in TL['scenes']}; LN=TL['lines']
def L(sc,k): return [l for l in LN if l['scene']==sc][k]['start']
def env(a,b,fa=1.0,fb=1.0):
    e=np.zeros(n); e[(t>=a)&(t<b)]=1
    up=np.clip((t-a)/fa,0,1); dn=np.clip((b-t)/fb,0,1); return e*up*dn
def note(f,start,dur,amp=0.3,harm=(1,.5,.25,.12),dec=2.5):
    s=int(start*SR); m=min(n-s,int(dur*SR)); 
    if m<=0: return
    tt=np.arange(m)/SR; w=sum(h*np.sin(2*np.pi*f*(k+1)*tt) for k,h in enumerate(harm))
    mix[s:s+m]+=amp*w*np.exp(-tt*dec)*np.minimum(1,tt/0.008)
def pad(freqs,a,b,amp,fa=1.5,fb=1.5,bright=4):
    e=env(a,b,fa,fb); w=np.zeros(n)
    for f in freqs:
        for k in range(1,bright+1): w+=np.sin(2*np.pi*f*k*t*(1+0.0007*k)+k)/k**1.6
    return amp*e*w*(0.85+0.15*np.sin(2*np.pi*0.2*t))
def lp(x,k=40): return np.convolve(x,np.ones(k)/k,'same')
mix=np.zeros(n)
black0=SC['black']['start']; turn0=SC['turn']['start']; fame0=SC['fame']['start']; lead=L('fame',4); chair=L('teacher',2)
# Act 1-2: dark drone (D minor), tension rising
mix+=pad([73.42,110.0],0,black0,0.05,3,0.4,2)
mix+=pad([87.31],SC['insp']['start'],black0,0.05,4,0.4,3)
mix+=pad([116.54],SC['teacher']['start'],chair,0.04,3,0.5,2)
# heartbeat from "Six new papers" to the empty chair, accelerating; one heavy beat on the chair
hb=L('shift',2); tb=hb
while tb<chair-0.3:
    bpm=58+18*(tb-hb)/(chair-hb)
    for off,a in ((0,0.33),(0.18,0.2)): note(48,tb+off,0.25,a,(1,.3),14); note(70,tb+off,0.1,a*0.4,(1,),30)
    tb+=60/bpm
note(42,chair,1.4,0.9,(1,.4),3.5); note(30,chair,1.6,0.6,(1,),2.5)
# sparse low piano in the fear
for k,tt0 in enumerate(np.arange(SC['insp']['start'],black0-1,4.2)):
    note([293.66,349.23,220.0,261.63][k%4],tt0,3.5,0.14,(1,.45,.2,.1),1.1)
# black: near silence, a single high bell at the question
note(587.33,L('black',0),3,0.05,(1,.3),1.2)
# Turn: sunrise swell
rise=env(turn0,turn0+3.5,2.5,0.8); mix+=0.06*rise*lp(np.random.default_rng(1).standard_normal(n),12)*np.clip((t-turn0)/2.5,0,1)
# Act 3-4: warm progression D - Bm - G - A, 76 bpm, piano arpeggios
bpm=76; bar=4*60/bpm; prog=[[146.83,185.0,220.0],[123.47,146.83,185.0],[98.0,123.47,146.83],[110.0,138.59,164.81]]
k=0; tt0=turn0+0.4
while tt0<T-3:
    ch=prog[k%4]
    big = 1.0 if tt0<fame0 else (1.35 if tt0<lead-bar else 1.0)
    mix+=pad([c/2 for c in ch]+ch,tt0,tt0+bar+0.3,0.035*big*min(1,(tt0-turn0)/12+0.4),0.6,0.6,4)
    if tt0>SC['tongue']['start']-0.5:
        for j in range(8): note(ch[j%3]*(2 if j>=3 else 1),tt0+j*bar/8,1.4,0.09 if tt0<fame0 else 0.11,(1,.4,.15),2.6)
    k+=1; tt0+=bar
# Fame: riser into "Leading.", impact, big chord
r0=lead-4; ramp=np.clip((t-r0)/4,0,1)*(t<lead)
noise=np.random.default_rng(2).standard_normal(n); mix+=0.10*ramp**2*(noise-lp(noise,6))
for f in (220,330,440,660): mix+=0.03*ramp**2*np.sin(2*np.pi*f*(1+ramp*0.06)*t)
note(55,lead,3,0.9,(1,.5,.2),1.6); note(41,lead,3,0.7,(1,),1.2)
burst=env(lead,lead+1.8,0.005,1.6)*noise; mix+=0.07*lp(burst,3)
mix+=pad([73.42,146.83,185.0,220.0,293.66],lead,SC['proof']['end'],0.05,0.05,2,5)
# end: gentle resolve
mix+=pad([146.83,220.0,293.66],SC['cta']['start'],T,0.04,2,3,3)
mix*=np.clip((T-t)/3,0,1)
# voice
voice=np.zeros(n)
for l in LN:
    raw=subprocess.check_output(['ffmpeg','-loglevel','error','-i',D+f"vo/l{l['i']:02d}.mp3",'-f','s16le','-ac','1','-ar',str(SR),'-'])
    a=np.frombuffer(raw,np.int16)/32768; s=int(l['start']*SR); voice[s:s+len(a)]+=a[:n-s]
venv=lp(np.abs(voice),SR//6); duck=1-0.55*np.clip(venv*10,0,1)
music=mix/np.max(np.abs(mix))*0.5
out=voice*1.0+music*duck
out=np.clip(out/np.max(np.abs(out))*0.95,-1,1)
w=wave.open(D+'mix.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
print('mixed',round(T,1))
