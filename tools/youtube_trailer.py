"""Publishes the brand film on a language channel and makes it that channel's trailer (what
non-subscribers see first). Uploads at most once per channel: the id is kept in video/trailers.json.
Usage: python tools/youtube_trailer.py video/trailer-<lang>.json
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from youtube_upload import API, ROOT, access_token, call, load, save, set_thumbnail, upload  # noqa: E402

TRAILERS = os.path.join(ROOT, "video", "trailers.json")

if __name__ == "__main__":
    meta = json.load(open(os.path.join(ROOT, sys.argv[1]), encoding="utf-8"))
    lang = meta["language"]
    token = access_token(lang)
    trailers = load(TRAILERS, {})
    snippet = {"title": meta["title"][:100], "description": meta["description"], "tags": meta.get("tags", []),
               "categoryId": "27", "defaultLanguage": lang, "defaultAudioLanguage": "en"}
    video_id = trailers.get(lang)
    if video_id:
        call("PUT", f"{API}/videos?part=snippet", token, {"id": video_id, "snippet": snippet})
        print(f"Already on YouTube, updated title/description: https://youtu.be/{video_id}")
    else:
        body = {"snippet": snippet, "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}}
        video_id = upload(meta, body, token)
        print(f"Uploaded (public): https://youtu.be/{video_id}")
        if meta.get("thumbnail"):
            set_thumbnail(video_id, meta["thumbnail"], token)
        trailers[lang] = video_id
        save(TRAILERS, trailers)
    # Channel trailer: brandingSettings must be sent whole, or YouTube clears the fields left out
    ch = call("GET", f"{API}/channels?part=brandingSettings&mine=true", token)["items"][0]
    branding = ch.get("brandingSettings", {})
    branding.setdefault("channel", {})["unsubscribedTrailer"] = video_id
    call("PUT", f"{API}/channels?part=brandingSettings", token, {"id": ch["id"], "brandingSettings": branding})
    print(f"Channel trailer set: {video_id}")
