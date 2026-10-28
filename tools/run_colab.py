"""Command-line entry point for the Colab notebook.

Runs in its own Python process so it always sees freshly installed packages
(no "restart runtime" needed). Writes the list of new clips to made.json.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import tts  # noqa: E402

parser = argparse.ArgumentParser()
parser.add_argument("--repo", required=True)
parser.add_argument("--lessons", default="")
parser.add_argument("--overwrite", action="store_true")
args = parser.parse_args()

lessons = [x.strip() for x in args.lessons.split(",") if x.strip()] or None
made, problems = tts.run(args.repo, lessons=lessons, overwrite=args.overwrite)
json.dump({"made": made, "problems": problems}, open(os.path.join(args.repo, "made.json"), "w"))
print(f"\nMade {len(made)} clip(s).")
if problems:
    print("⚠️ Please listen to these. They may be cut off or rambling:")
    for path, issue in problems:
        print("  ", path, "→", issue)
