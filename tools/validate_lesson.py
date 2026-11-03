"""Run every program in a lesson and check its printed output.

Checks the walkthrough, each task solution (against expectedOutput, and that the starter code
does NOT already pass), each error example (the last line of the error must match), and the
mustContain hints. Usage: python3 tools/validate_lesson.py 2-1 [2-2 ...]
"""
import json
import os
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def run(code, stdin=""):
    p = subprocess.run([sys.executable, "-c", code], input=stdin, capture_output=True, text=True, timeout=20)
    return p.stdout.rstrip("\n"), (p.stderr.strip().splitlines() or [""])[-1]


def check(lesson):
    d = json.load(open(os.path.join(ROOT, "content", "bp101t", lesson, "en.json"), encoding="utf-8"))
    bad = []
    w = d["walkthrough"]
    out, err = run(w["code"], w.get("stdin", ""))
    if out != w["output"].rstrip("\n"):
        bad.append(f"walkthrough output:\n  got  {out!r}\n  want {w['output']!r}\n  {err}")
    said = [s["output"] for s in w["steps"] if s.get("output")]
    if "\n".join(said) != w["output"] and not w.get("stdin"):
        bad.append(f"walkthrough step outputs {said!r} != output")
    for t in d["tasks"]:
        out, err = run(t["solution"], t.get("stdin", ""))
        if out != t["expectedOutput"]:
            bad.append(f"task {t['id']} solution: got {out!r} want {t['expectedOutput']!r} {err}")
        for m in t["check"].get("mustContain", []):
            if m not in t["solution"]:
                bad.append(f"task {t['id']}: solution lacks {m!r}")
        sout, _ = run(t["starterCode"], t.get("stdin", ""))
        if sout == t["expectedOutput"] and all(m in t["starterCode"] for m in t["check"].get("mustContain", [])):
            bad.append(f"task {t['id']}: starter code already passes")
    for e in d["errors"]["examples"]:
        out, err = run(e["code"])
        if err != e["output"]:
            bad.append(f"error example {e['title']!r}: got {err!r} want {e['output']!r}")
    for q in d["quiz"]:
        if not 0 <= q["answer"] < len(q["options"]):
            bad.append(f"quiz answer index out of range: {q['q'][:40]}")
    print(f"{lesson}: {'OK' if not bad else str(len(bad)) + ' problem(s)'}")
    for b in bad:
        print("  -", b)
    return not bad


if __name__ == "__main__":
    ok = all([check(x) for x in sys.argv[1:]])
    sys.exit(0 if ok else 1)
