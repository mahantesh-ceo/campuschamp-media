"""Shared writer for lesson translations (Unit II onwards).

A lesson file defines T (hi / hinglish / kn section texts), NARR and ANIM (narration lines per
language) and calls build(). Lists keep the English order because the website merges by position.
"""
import json
import os
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SECTIONS = ["hook", "learn", "explanation", "walkthrough", "errors", "mistakes", "tasks",
            "quiz", "exam", "mindmap", "summary", "animations"]
NATIVE_PY = {"hi": "पाइथन", "kn": "ಪೈಥಾನ್"}


def say_native(text, lang):
    """Sarvam reads English words inside Hindi/Kannada text; only 'Python' needs native spelling."""
    return text.replace("Python", NATIVE_PY[lang])


def build(lesson, anim_id, T, NARR, ANIM, say_en=lambda s: s):
    en = json.load(open(os.path.join(ROOT, "content", "bp101t", lesson, "en.json"), encoding="utf-8"))
    n_steps, n_anim = len(en["walkthrough"]["steps"]), len(en["animations"][0]["steps"])
    for lang, data in T.items():
        assert len(NARR[lang]) == n_steps, (lang, "narration", len(NARR[lang]), n_steps)
        assert len(ANIM[lang]) == n_anim, (lang, "animation", len(ANIM[lang]), n_anim)
        for key in ("explanation", "tasks", "quiz", "mistakes", "learn", "summary"):
            assert len(data[key]) == len(en[key]), (lang, key)
        assert len(data["errors"]["examples"]) == len(en["errors"]["examples"]), (lang, "errors")
        assert len(data["walkthrough"]["keyTerms"]) == len(en["walkthrough"]["keyTerms"]), (lang, "keyTerms")
        assert len(data["mindmap"]["children"]) == len(en["mindmap"]["children"]), (lang, "mindmap")
        for a, b in zip(data["mindmap"]["children"], en["mindmap"]["children"]):
            assert len(a["children"]) == len(b["children"]), (lang, "mindmap child", a["label"])
        for a, b in zip(data["tasks"], en["tasks"]):
            assert len(a["hints"]) == len(b["hints"]), (lang, "hints", b["id"])
            assert ("solutionNote" in a) == ("solutionNote" in b), (lang, "solutionNote", b["id"])
        for a, b in zip(data["explanation"], en["explanation"]):
            assert ("callout" in a) == ("callout" in b), (lang, "callout", b["heading"])
        doc = dict(data)
        doc["walkthrough"] = dict(doc["walkthrough"], steps=[{"say": s} for s in NARR[lang]])
        doc["animations"] = [{"steps": [{"say": s} for s in ANIM[lang]]}]
        doc["translatedSections"] = SECTIONS
        path = os.path.join(ROOT, "content", "bp101t", lesson, f"{lang}.json")
        json.dump(doc, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("wrote", os.path.relpath(path, ROOT))

    narr_en = [s["say"] for s in en["walkthrough"]["steps"]]
    anim_en = [s["say"] for s in en["animations"][0]["steps"]]
    tracks = []
    for tid, prefix, en_lines, native in (("narrator", "step-", narr_en, NARR), (anim_id, anim_id + "-", anim_en, ANIM)):
        tracks.append({"id": tid, "prefix": prefix, "lang": "en", "tts": [say_en(t) for t in en_lines], "display": en_lines})
        tracks.append({"id": tid, "prefix": prefix, "lang": "hi", "tts": [say_native(t, "hi") for t in native["hi"]],
                       "display": native["hi"], "displayHinglish": native["hinglish"]})
        tracks.append({"id": tid, "prefix": prefix, "lang": "kn", "tts": [say_native(t, "kn") for t in native["kn"]], "display": native["kn"]})
    script = {"course": "bp101t", "lesson": lesson, "voices": {"en": "Ritu", "hi": "Ritu", "kn": "Chaitra"}, "tracks": tracks}
    path = os.path.join(ROOT, "scripts", "bp101t", f"{lesson}.json")
    json.dump(script, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote", os.path.relpath(path, ROOT))
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "glossary_bp101t.py")], check=True)
