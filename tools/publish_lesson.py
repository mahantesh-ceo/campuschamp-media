"""Mark a lesson available (with its translations) in content/bp101t/course.json."""
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
p = os.path.join(ROOT, "content", "bp101t", "course.json")
c = json.load(open(p, encoding="utf-8"))
for u in c["units"]:
    for l in u["lessons"]:
        if l["id"] in sys.argv[1:]:
            l["available"] = True
            l["translations"] = ["hi", "hinglish", "kn"]
            print("published", l["id"], l["title"])
json.dump(c, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
