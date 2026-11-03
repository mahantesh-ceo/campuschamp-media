"""Add the rendered Unit I lesson videos (1.2-1.7, episode 1) to content/bp101t/videos.json, so the
lesson pages show them (self-hosted mp4 + poster). YouTube ids are added later, when published."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, HERE)
from unit1_text import TITLE  # noqa: E402

p = os.path.join(ROOT, "content", "bp101t", "videos.json")
V = json.load(open(p, encoding="utf-8"))
for lesson in ["1-2", "1-3", "1-4", "1-5", "1-6", "1-7"]:
    sources = {}
    for lang in ["kn", "hi", "en"]:
        mp4 = f"media/bp101t/{lesson}/{lang}/ep1.mp4"
        if not os.path.exists(os.path.join(ROOT, mp4)):
            continue
        secs = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(ROOT, mp4)]))
        sources[lang] = {"mp4": mp4, "poster": mp4.replace(".mp4", ".jpg"), "seconds": round(secs)}
    if not sources:
        continue
    V[lesson] = [{"episode": 1, "placement": "top", "title": TITLE[lesson], "sources": sources}]
    print(lesson, sorted(sources))
json.dump(V, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
