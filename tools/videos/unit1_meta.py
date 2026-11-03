"""YouTube metadata (video/meta/*.json), chapters and thumbnails for the Unit I lesson videos 1.2-1.7.
Masters are copied from the render folder given as argv[1] into video/out/."""
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, HERE)
from unit1_text import TITLE  # noqa: E402

MASTERS = sys.argv[1]
NAME = {"en": "English", "hi": "Hindi", "kn": "Kannada"}
KW = {"1-2": ["install python", "python IDE", "jupyter notebook", "vs code python"],
      "1-3": ["python variables", "python data types", "int float string bool"],
      "1-4": ["python type casting", "python operators", "floor division modulus"],
      "1-5": ["python input output", "python f-string", "python input function"],
      "1-6": ["python string operations", "string slicing python", "python string methods"],
      "1-7": ["python libraries", "pip install", "python modules import"]}
INTRO = {"en": "B.Pharm Sem I, BP101T Basics of Python Programming for Pharmaceutical Sciences, explained simply in English.",
         "hi": "B.Pharm Sem I, BP101T Basics of Python Programming for Pharmaceutical Sciences, हिंदी में.",
         "kn": "B.Pharm Sem I, BP101T Basics of Python Programming for Pharmaceutical Sciences, ಕನ್ನಡದಲ್ಲಿ."}
EPI = {"en": "In this episode: {a}, {b} and {c}. Then two common errors ({e}), a quick check and a recap.",
       "hi": "इस episode में: {a}, {b} और {c}. फिर दो आम errors ({e}), एक quick check और recap.",
       "kn": "ಈ episode ನಲ್ಲಿ: {a}, {b} ಮತ್ತು {c}. ಆಮೇಲೆ ಎರಡು ಸಾಮಾನ್ಯ errors ({e}), ಒಂದು quick check ಮತ್ತು recap."}
PRAC = {"en": "▶ Practise this lesson free on your phone:", "hi": "▶ इस lesson को अपने phone पर free practise कीजिए:",
        "kn": "▶ ಈ lesson ಅನ್ನು ನಿಮ್ಮ phone ನಲ್ಲಿ free ಆಗಿ practise ಮಾಡಿ:"}
IQ = {"en": "", "hi": "hi/", "kn": "kn/"}
HASH = {"en": "#BP101T #BPharm #Python #PCI", "hi": "#BP101T #BPharm #PythonInHindi #PCI", "kn": "#BP101T #BPharm #PythonInKannada #PCI"}

os.makedirs(os.path.join(ROOT, "video", "out"), exist_ok=True)
for lesson in ["1-2", "1-3", "1-4", "1-5", "1-6", "1-7"]:
    for lang in ["en", "hi", "kn"]:
        base = f"bp101t-{lesson}-ep1-{lang}"
        E = json.load(open(os.path.join(ROOT, "video", "episodes", f"bp101t-{lesson}-ep1.{lang}.json"), encoding="utf-8"))
        d = E["data"]
        out = os.path.join(ROOT, "video", "out", base)
        shutil.copy(os.path.join(MASTERS, base + ".mp4"), out + ".mp4")
        shutil.copy(os.path.join(MASTERS, base + ".chapters.txt"), out + ".chapters.txt")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "4.5", "-i", out + ".mp4", "-frames:v", "1", "-vf", "scale=1280:720", out + ".png"], check=True)
        errs = " / ".join(d[k]["output"].split(":")[0] for k in ("e1", "e2"))
        utm = f"utm_source=youtube&utm_medium=video&utm_campaign={base}"
        desc = "\n\n".join([
            INTRO[lang],
            EPI[lang].format(a=d["c1"]["heading"], b=d["c2"]["heading"], c=d["c3"]["heading"], e=errs),
            f"{PRAC[lang]}\nhttps://www.campuschamp.in/learn/bp101t/{lesson}?{utm}",
            f"📄 BP101T Unit 1 important questions (free PDF):\nhttps://www.campuschamp.in/{IQ[lang]}bp101t/important-questions/unit-1?{utm}",
            "Chapters\n{{CHAPTERS}}",
            "Narration uses an AI voice. Practice questions only; university questions may differ.",
            HASH[lang]])
        tags = ["BP101T", "B.Pharm Python", f"Python in {NAME[lang]}" if lang != "en" else "Python for pharmacy students"] + \
               [k + ("" if lang == "en" else f" {NAME[lang].lower()}") for k in KW[lesson]] + \
               ["Basics of Python Programming for Pharmaceutical Sciences", "PCI syllabus", "B.Pharm Sem 1", "pharmacy students", "Campus Champ"]
        meta = {"lesson": lesson, "episode": 1, "language": lang, "file": f"video/out/{base}.mp4",
                "chapters": f"video/out/{base}.chapters.txt", "thumbnail": f"video/out/{base}.png",
                "description": desc, "tags": tags, "topic": TITLE[lesson][lang]}
        json.dump(meta, open(os.path.join(ROOT, "video", "meta", base + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(base, len(desc))
