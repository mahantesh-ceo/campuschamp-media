import sys, json, time, os
sys.path.insert(0, '/home/user/campuschamp-media/tools')
from sarvam_tts import client, speak
from concurrent.futures import ThreadPoolExecutor
c = client(); D = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(D + '/script.json'))
os.makedirs(D + '/vo', exist_ok=True)
only = set(map(int, sys.argv[1:])) if len(sys.argv) > 1 else None
def go(i):
    l = L[i]; txt = l[2] if len(l) > 2 else l[1]
    for a in range(6):
        try:
            speak(c, txt, f"{D}/vo/l{i:02d}.mp3", 'girish_en_documentary', lang='en-IN', pace=1.22); return None
        except Exception as e:
            err = str(e)[-120:]; time.sleep(2 + a * 3)
    return f'{i} {err}'
with ThreadPoolExecutor(3) as p:
    bad = [r for r in p.map(go, [i for i in range(len(L)) if only is None or i in only]) if r]
print(len(L), 'lines,', len(bad), 'failed', bad)
