import json,subprocess,os
D=os.path.dirname(os.path.abspath(__file__))+'/'
L=json.load(open(D+'script.json'))
dur=lambda i: float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+f'vo/l{i:02d}.mp3']))
LEAD={'hist':1.0,'good':0.5,'book':0.6}
HOLD={'hist':0.9,'search':0.6,'smiles':0.6,'fold':0.5,'abx':0.5,'data':0.5,'india':1.0,'syl':0.4,'sems':0.6,'wall':1.2,'good':0.4,'blend':0.6,'promise':0.6,'proof':0.8,'book':0.6,'cta':4.5}
GAP={(0,1):0.6,(3,4):0.4,(33,34):0.6,(34,35):0.6,(35,36):0.5}
t=0;scenes=[];lines=[];cur=None
for i,l in enumerate(L):
    sc=l[0]
    if sc!=cur:
        if cur: t+=HOLD[cur]; scenes[-1]['end']=t
        scenes.append({'id':sc,'start':t});cur=sc;t+=LEAD.get(sc,0.35)
    elif lines: t+=GAP.get((i-1,i),0.3)
    d=dur(i);lines.append({'i':i,'scene':sc,'start':round(t,3),'dur':round(d,3),'text':l[1]});t+=d
t+=HOLD[cur];scenes[-1]['end']=t
for s in scenes: s['start']=round(s['start'],3);s['end']=round(s['end'],3)
json.dump({'duration':round(t,3),'scenes':scenes,'lines':lines},open(D+'timeline.json','w'),indent=1)
print(round(t,1),'s');[print(s['id'],s['start'],s['end']) for s in scenes]
