"""Append a lesson's glossary block (text file with a  "lesson": [...],  entry) to glossary_bp101t.py."""
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
p = os.path.join(ROOT, "tools", "glossary_bp101t.py")
s = open(p, encoding="utf-8").read()
add = open(sys.argv[1], encoding="utf-8").read().rstrip("\n")
key = add.strip().split(":")[0]
if key in s:
    sys.exit(f"{key} already in glossary")
i = s.index("\n}\n\n\ndef apply")
open(p, "w", encoding="utf-8").write(s[:i] + "\n" + add + s[i:])
print("added", key)
