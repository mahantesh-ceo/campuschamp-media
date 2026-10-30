"""Applies a language channel's branding: banner image, About description, keywords, country.
(YouTube's API can't set the profile picture or the link buttons; those are set in YouTube Studio.)
Usage: python tools/youtube_branding.py video/channel-<lang>.json
"""
import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from youtube_upload import API, ROOT, access_token, call  # noqa: E402


def upload_banner(path, token):
    with open(os.path.join(ROOT, path), "rb") as f:
        req = urllib.request.Request("https://www.googleapis.com/upload/youtube/v3/channelBanners/insert",
                                     data=f.read(), method="POST",
                                     headers={"Authorization": f"Bearer {token}", "Content-Type": "image/png"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)["url"]
    except urllib.error.HTTPError as e:
        print("Banner not set:", e.code, e.read().decode()[:200])
        return None


if __name__ == "__main__":
    meta = json.load(open(os.path.join(ROOT, sys.argv[1]), encoding="utf-8"))
    token = access_token(meta["language"])
    ch = call("GET", f"{API}/channels?part=brandingSettings&mine=true", token)["items"][0]
    branding = ch.get("brandingSettings", {})
    c = branding.setdefault("channel", {})
    c["description"] = meta["description"][:1000]
    c["keywords"] = " ".join(f'"{k}"' if " " in k else k for k in meta.get("keywords", []))
    c["country"] = meta.get("country", "IN")
    c["defaultLanguage"] = meta["language"]
    if meta.get("banner"):
        url = upload_banner(meta["banner"], token)
        if url:
            branding.setdefault("image", {})["bannerExternalUrl"] = url
    # brandingSettings is replaced whole, so everything already set (like the trailer) is sent back
    call("PUT", f"{API}/channels?part=brandingSettings", token, {"id": ch["id"], "brandingSettings": branding})
    print(f"Branding applied to channel {ch['id']}")
