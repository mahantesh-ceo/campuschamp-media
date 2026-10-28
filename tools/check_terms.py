"""Flag technical words a lesson uses before they have been explained.

A word counts as explained once it appears in the "glossary" of the same lesson or any
earlier lesson. Code, program output and error messages are ignored, because students
copy those exactly rather than read them as explanations.

Usage: python3 tools/check_terms.py [lesson ids...]   (default: every available lesson)
"""
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONTENT = os.path.join(ROOT, "content", "bp101t")

# Technical words to watch for, with the patterns that count as a use of them.
JARGON = {
    "code": r"\bcode\b", "program": r"\bprograms?\b", "programming language": r"programming languages?",
    "interpreter": r"\binterpreter\b", "run": r"\b(run|runs|running|ran)\b", "output": r"\boutputs?\b",
    "print()": r"\bprint\b", "string": r"\bstrings?\b", "comment": r"\bcomments?\b",
    "syntax": r"\bsyntax\b", "error": r"\berrors?\b", "syntax error": r"\bsyntax errors?\b",
    "bug": r"\bbugs?\b", "debugging": r"\bdebug(ging|ger)?\b", "case-sensitive": r"case-sensitive",
    "library": r"\blibrar(y|ies)\b", "module": r"\bmodules?\b", "command prompt / terminal": r"\b(terminal|command prompt)\b",
    "command": r"\bcommands?\b", "PATH": r"\bPATH\b", "python prompt (>>>)": r">>>",
    "text editor": r"\btext editors?\b", "IDE": r"\bIDEs?\b", "file extension (.py)": r"\.py\b",
    "cell": r"\bcells?\b", "extension (add-on)": r"\bextensions?\b", "syntax highlighting": r"syntax highlighting",
    "auto-completion": r"auto-complet", "Anaconda": r"\bAnaconda\b",
    "variable": r"\bvariables?\b", "data type": r"\bdata types?\b", "integer": r"\bintegers?\b",
    "float": r"\bfloats?\b", "boolean": r"\bbooleans?\b", "operator": r"\boperators?\b",
    "function": r"\bfunctions?\b", "loop": r"\bloops?\b", "list": r"\b(a|the|python) lists?\b(?! of)",
    "dictionary": r"\bdictionar(y|ies)\b", "pip": r"\bpip\b", "dataset": r"\bdatasets?\b",
}
SKIP_KEYS = {"code", "output", "solution", "starterCode", "expectedOutput", "see", "audio", "id",
             "searchTerms", "videoUrl", "check", "actors", "canvas", "actions", "filename", "term"}


def texts(node, key=None):
    """Yield (field, text) for every human-readable string in a lesson."""
    if key in SKIP_KEYS:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            yield from ((f"{k}.{f}" if f else k, t) for f, t in texts(v, k))
    elif isinstance(node, list):
        for item in node:
            yield from texts(item, key)
    elif isinstance(node, str):
        yield "", re.sub(r"`[^`]*`", " ", node)  # inline code is copied, not read as prose


def glossary_terms(lesson):
    return {g["term"].lower() for g in lesson.get("glossary", [])}


def main(ids):
    course = json.load(open(os.path.join(CONTENT, "course.json"), encoding="utf-8"))
    order = [l["id"] for u in course["units"] for l in u["lessons"] if l["available"]]
    ids = ids or order
    known, problems = set(), 0
    for lid in order:
        lesson = json.load(open(os.path.join(CONTENT, lid, "en.json"), encoding="utf-8"))
        known |= glossary_terms(lesson)
        if lid not in ids:
            continue
        missing = {}
        for field, text in texts(lesson):
            for term, pattern in JARGON.items():
                if term.lower() not in known and re.search(pattern, text, re.IGNORECASE if term != "PATH" else 0):
                    missing.setdefault(term, field.split(".")[0])
        print(f"Lesson {lid}: glossary has {len(lesson.get('glossary', []))} words")
        for term, where in sorted(missing.items()):
            print(f"   ⚠️  '{term}' is used (first in {where}) but not explained yet")
        problems += len(missing)
    print("✅ Every technical word is explained" if not problems else f"\n{problems} word(s) to explain")
    return problems


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1:]) else 0)
