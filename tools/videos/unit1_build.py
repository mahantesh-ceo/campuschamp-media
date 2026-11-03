"""Write the episode scripts and plans for the Unit I lesson videos (1.2-1.7), and voice the new lines.

For each lesson L and language: video/episodes/bp101t-L-ep1.<lang>.json and bp101t-L-ep1.plan.json.
New narration is voiced into audio/bp101t/L/<lang>/ep1/; the animation and walkthrough reuse the
lesson's existing clips (ids like ../step-01). Usage:
  SARVAM_KEY_FROM_NETWORK=1 python3 tools/videos/unit1_build.py [1-2 1-3 ...] [--no-tts]
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))
from unit1_text import EP, ICON, TITLE, WORDS  # noqa: E402

LANGS = ["en", "hi", "kn"]
SPEAKERS = {"en": "ritu_en_edtech", "hi": "ritu_hi_conversation", "kn": "chaitra_kn_conversation"}
VOICE = {"en": "Ritu", "hi": "Ritu", "kn": "Chaitra"}
NEXT = {"1-2": "1-3", "1-3": "1-4", "1-4": "1-5", "1-5": "1-6", "1-6": "1-7", "1-7": "2-1"}
NATIVE_PY = {"hi": "पाइथन", "kn": "ಪೈಥಾನ್"}


def plain(md):
    s = md.replace("\\*", "\x00")
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"(?<!\w)\*(\S.*?)\*(?!\w)", r"\1", s)
    return s.replace("\x00", "*").strip()


def run(code):
    p = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=20)
    return p.stdout.rstrip("\n")


def load(lesson, lang):
    return json.load(open(os.path.join(ROOT, "content", "bp101t", lesson, f"{lang}.json"), encoding="utf-8"))


def episode(lesson, lang):
    cfg = EP[lesson]
    en, tr = load(lesson, "en"), load(lesson, lang)
    say = cfg["say"][lang]
    W = WORDS[lang]
    script = json.load(open(os.path.join(ROOT, "scripts", "bp101t", f"{lesson}.json"), encoding="utf-8"))
    track = {t["id"]: t for t in script["tracks"] if t["lang"] == lang}
    narr = track["narrator"]
    anim_id = next(k for k in track if k != "narrator")
    anim = track[anim_id]
    lines, data = [], {}
    add = lambda i, scene, text, reuse=False: lines.append({"id": i, "scene": scene, "say": text, "tts": text, "reuse": reuse})

    # hook
    for k, s in enumerate(say["hook"]):
        add(f"h{k + 1}", "lhook", s)
    data["hook"] = {"icon": ICON[lesson], "title": plain(tr["hook"]["title"]), "learn": [plain(x) for x in tr["learn"][:3]],
                    "label": f"BP101T · {W['lesson']} {lesson.replace('-', '.')}", "learnT": W["learn"]}

    # the lesson's animation, with its own narration clips
    a = en["animations"][0]
    for k, s in enumerate(anim["display"]):
        add(f"../{anim['prefix']}{k + 1:02d}", "lanim", s, True)
    data["lanim"] = {"title": a["title"], "actors": a["actors"], "steps": [{"actions": st["actions"]} for st in a["steps"]]}

    # three key ideas
    for k, (ix, code, out, mode) in enumerate(cfg["concepts"]):
        sid = f"c{k + 1}"
        add(sid, sid, say["c"][k])
        ex = tr["explanation"][ix]
        c = {"heading": plain(ex["heading"]), "mode": mode, "idea": W["idea"]}
        if mode == "points":
            c["points"] = cfg["points"][lang][k]
        else:
            c["code"] = code
            c["output"] = "" if mode == "terminal" else (out if out is not None else run(code))
            c["file"] = W["terminal"] if mode == "terminal" else "example.py"
        if ex.get("callout") and len(plain(ex["callout"]["md"])) <= 110:
            c["callout"] = plain(ex["callout"]["md"])
        data[sid] = c

    # walkthrough, with its own narration clips
    w = en["walkthrough"]
    for k, s in enumerate(narr["display"]):
        add(f"../step-{k + 1:02d}", "lwalk", s, True)
    data["lwalk"] = {"file": w["filename"], "code": w["code"], "steps": [{"line": s.get("line"), "vars": s.get("vars", {}), "output": s.get("output")} for s in w["steps"]],
                     "varsT": W["vars"], "outT": W["output"]}

    # two errors
    for k, ex in enumerate(en["errors"]["examples"][:2]):
        sid = f"e{k + 1}"
        add(sid, sid, say["e"][k])
        data[sid] = {"title": plain(tr["errors"]["examples"][k]["title"]), "code": ex["code"], "errorLine": ex["errorLine"], "output": ex["output"]}

    # quiz (three options) and recap
    qi, pick = cfg["quiz"]
    q = en["quiz"][qi]
    options = [q["options"][i] for i in pick]
    ans = pick.index(q["answer"])
    qtext = plain(tr["quiz"][qi]["q"])
    add("q1", "quiz", qtext)
    add("q2", "quiz-answer", W["answer"].format(L="ABC"[ans], opt=options[ans], why=plain(tr["quiz"][qi]["why"])))
    recap = [plain(x) for x in tr["summary"][:4]]
    add("r0", "lrecap", W["recapIntro"])
    for k, s in enumerate(recap):
        add(f"r{k + 1}", "lrecap", s)
    data["lrecap"] = {"items": recap, "title": W["recap"]}
    data["output"] = W["output"]
    return {"course": "bp101t", "lesson": lesson, "episode": 1, "lang": lang, "engine": "sarvam", "speaker": SPEAKERS[lang],
            "voiceName": VOICE[lang], "lines": lines, "data": data,
            "quiz": {"q": qtext, "options": options, "answer": ans}, "recap": recap}


def plan(lesson, eps):
    chapters, title, quiz, recap, nxt = {}, {}, {}, {}, {}
    for lang, E in eps.items():
        W = WORDS[lang]
        d = E["data"]
        chapters[lang] = {"lhook": W["intro"], "lanim": d["lanim"]["title"] if lang == "en" else W["idea"], "c1": d["c1"]["heading"],
                          "c2": d["c2"]["heading"], "c3": d["c3"]["heading"], "lwalk": W["walk"], "e1": W["errors"],
                          "quiz": W["quiz"], "lrecap": W["recap"], "end": W["end"]}
        title[lang] = TITLE[lesson][lang]
        quiz[lang] = E.pop("quiz")
        recap[lang] = E.pop("recap")
        n = NEXT[lesson]
        nxt[lang] = {"label": W["next"].format(n=n.replace("-", ".")), "title": TITLE[n][lang], "desc": W["desc"]}
    return {"order": ["lhook", "sting", "lanim", "c1", "c2", "c3", "lwalk", "e1", "e2", "quiz", "lrecap", "end"],
            "hold": {"lhook": 1.2, "sting": 2.8, "lanim": 1.2, "c1": 1.8, "c2": 1.8, "c3": 1.8, "lwalk": 1.4, "e1": 1.4, "e2": 1.4,
                     "quiz": 1.4, "lrecap": 1.4, "end": 6},
            "chapters": chapters, "title": title, "quiz": quiz, "recap": recap, "next": nxt}


def tts_jobs(lesson, E):
    out = []
    for l in E["lines"]:
        if l["reuse"]:
            continue
        path = os.path.join(ROOT, "audio", "bp101t", lesson, E["lang"], "ep1", f"{l['id']}.mp3")
        text = l["tts"] if E["lang"] == "en" else l["tts"].replace("Python", NATIVE_PY[E["lang"]])
        out.append((text, path, E["lang"]))
    return out


if __name__ == "__main__":
    lessons = [a for a in sys.argv[1:] if not a.startswith("--")] or list(EP)
    jobs = []
    for lesson in lessons:
        eps = {lang: episode(lesson, lang) for lang in LANGS}
        P = plan(lesson, eps)
        base = os.path.join(ROOT, "video", "episodes", f"bp101t-{lesson}-ep1")
        json.dump(P, open(base + ".plan.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for lang, E in eps.items():
            json.dump(E, open(f"{base}.{lang}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            jobs += tts_jobs(lesson, E)
        print(lesson, {lang: len(E["lines"]) for lang, E in eps.items()})
    if "--no-tts" in sys.argv:
        sys.exit()
    from sarvam_tts import client, speak
    c = client()
    todo = [j for j in jobs if "--all" in sys.argv or not os.path.exists(j[1])]

    def go(j):
        text, path, lang = j
        for attempt in range(6):
            try:
                speak(c, text, path, SPEAKERS[lang], lang=f"{lang}-IN")
                return None
            except Exception as e:  # rate limits: back off
                err = str(e)[-120:]
                import time
                time.sleep(2 + attempt * 3)
        return f"{path}: {err}"

    with ThreadPoolExecutor(4) as pool:
        failed = [r for r in pool.map(go, todo) if r]
    print(f"{len(todo)} clips voiced, {len(failed)} failed", *failed, sep="\n")
