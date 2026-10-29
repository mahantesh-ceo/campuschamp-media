"""Moves YouTube ids from youtube_pending to youtube once the video is public, so the website
starts playing from YouTube. Run: python3 tools/promote_published.py"""
import json
import os
import urllib.error
import urllib.request

PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "bp101t", "videos.json")


def is_public(video_id):
    # YouTube's oEmbed answers only for public (and unlisted) videos
    try:
        with urllib.request.urlopen(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json") as r:
            return r.status == 200
    except urllib.error.HTTPError:
        return False


data = json.load(open(PATH, encoding="utf-8"))
moved = []
for lesson, episodes in data.items():
    if lesson.startswith("_"):
        continue
    for ep in episodes:
        for lang, src in ep["sources"].items():
            vid = src.get("youtube_pending")
            if vid and is_public(vid):
                src["youtube"] = vid
                src.pop("youtube_pending")
                moved.append(f"{lesson} ep{ep['episode']} {lang}: {vid}")
json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Now on YouTube:" if moved else "Nothing newly public.", *moved, sep="\n  ")
