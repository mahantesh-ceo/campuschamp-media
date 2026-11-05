import json,subprocess
D='/tmp/claude-0/-home-user/9ed5ad7e-b576-5f9e-8769-1c9b95945112/scratchpad/chair/'
L=json.load(open(D+'script.json'))
dur=lambda i: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo/l{i:02d}.mp3']))
LEAD={'open':1.2,'black':0.9,'turn':0.6}
HOLD={'open':0.6,'shift':0.8,'insp':1.0,'parent':0.9,'student':0.9,'teacher':0.6,'black':1.1,'turn':0.9,'tongue':0.7,'teacher2':0.7,'naac':0.7,'parents':0.9,'fame':1.6,'proof':0.8,'cta':4.5}
GAP={(6,7):1.1,(28,29):0.55,(2,3):0.5}
t=0;scenes=[];lines=[];cur=None
for i,l in enumerate(L):
    sc=l[0]
    if sc!=cur:
        if cur: t+=HOLD[cur]; scenes[-1]['end']=t
        scenes.append({'id':sc,'start':t});cur=sc;t+=LEAD.get(sc,0.4)
    elif lines: t+=GAP.get((i-1,i),0.32)
    d=dur(i);lines.append({'i':i,'scene':sc,'start':round(t,3),'dur':round(d,3),'text':l[1]});t+=d
t+=HOLD[cur];scenes[-1]['end']=t
for s in scenes: s['start']=round(s['start'],3);s['end']=round(s['end'],3)
json.dump({'duration':round(t,3),'scenes':scenes,'lines':lines},open(D+'timeline.json','w'),indent=1)
print(round(t,1),'s');[print(s['id'],s['start'],s['end']) for s in scenes]
