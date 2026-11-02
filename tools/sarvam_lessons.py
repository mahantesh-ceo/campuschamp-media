"""Lesson narration with Sarvam (Bulbul): rebuilds the walkthrough and animation voices of lessons.

Reads scripts/bp101t/<lesson>.json (written by tools/translations/bp101t_<lesson>.py) and writes
audio/bp101t/<lesson>/<lang>/<prefix>NN.mp3, the files the lesson page plays.
Voices match the video lessons: Ritu (English, Hindi) and Chaitra (Kannada).

Usage: SARVAM_KEY_FROM_NETWORK=1 python3 tools/sarvam_lessons.py [lesson ids...]   (default: every script)
       add --missing to only fill files that don't exist yet.
"""
import glob
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sarvam_tts import client, speak  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SPEAKERS = {"en": "ritu_en_edtech", "hi": "ritu_hi_conversation", "kn": "chaitra_kn_conversation"}
VOICE_NAMES = {"en": "Ritu", "hi": "Ritu", "kn": "Chaitra"}


def jobs_for(script, missing_only):
    out = []
    for track in script["tracks"]:
        lang = track["lang"]
        for i, text in enumerate(track["tts"], 1):
            path = os.path.join(ROOT, "audio", script["course"], script["lesson"], lang, f"{track['prefix']}{i:02d}.mp3")
            if missing_only and os.path.exists(path):
                continue
            out.append((text, path, lang))
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    missing_only = "--missing" in sys.argv
    files = sorted(glob.glob(os.path.join(ROOT, "scripts", "bp101t", "*.json")))
    if args:
        files = [f for f in files if os.path.basename(f)[:-5] in args]
    c = client()
    jobs = []
    for f in files:
        script = json.load(open(f, encoding="utf-8"))
        jobs += jobs_for(script, missing_only)
        # record which voices the lesson now uses
        script["voices"] = VOICE_NAMES
        json.dump(script, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    def go(job):
        text, path, lang = job
        err = ""
        for attempt in range(6):
            try:
                speak(c, text, path, SPEAKERS[lang], lang=f"{lang}-IN")
                return None
            except Exception as e:  # rate limits and network blips: back off and retry
                err = str(e)[-160:]
                time.sleep(2 + attempt * 3)
        return f"{os.path.relpath(path, ROOT)}: {err}"

    with ThreadPoolExecutor(4) as pool:
        failed = [r for r in pool.map(go, jobs) if r]
    print(f"{len(jobs)} clips from {len(files)} lessons, {len(failed)} failed")
    for f in failed:
        print("  ", f)
