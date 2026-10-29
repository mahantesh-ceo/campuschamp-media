"""Uploads one episode to YouTube as a PRIVATE video and records its id in content/bp101t/videos.json.

Runs in GitHub Actions with secrets YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN.
Usage: python tools/youtube_upload.py video/meta/<episode>.json
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def access_token():
    data = urllib.parse.urlencode({
        "client_id": os.environ["YT_CLIENT_ID"],
        "client_secret": os.environ["YT_CLIENT_SECRET"],
        "refresh_token": os.environ["YT_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }).encode()
    with urllib.request.urlopen("https://oauth2.googleapis.com/token", data) as r:
        return json.load(r)["access_token"]


def upload(meta, token):
    path = os.path.join(ROOT, meta["file"])
    size = os.path.getsize(path)
    chapters = open(os.path.join(ROOT, meta["chapters"])).read().strip() if meta.get("chapters") else ""
    body = {
        "snippet": {
            "title": meta["title"],
            "description": meta["description"].replace("{{CHAPTERS}}", chapters),
            "tags": meta.get("tags", []),
            "categoryId": "27",  # Education
            "defaultLanguage": meta.get("language", "kn"),
            "defaultAudioLanguage": meta.get("language", "kn"),
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
            "containsSyntheticMedia": True,  # AI voice: YouTube's disclosure
        },
    }
    # Resumable upload: start a session, then send the file
    req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
        method="POST",
    )
    with urllib.request.urlopen(req) as r:
        session = r.headers["Location"]
    with open(path, "rb") as f:
        put = urllib.request.Request(session, data=f.read(), method="PUT",
                                     headers={"Content-Type": "video/mp4", "Content-Length": str(size)})
        with urllib.request.urlopen(put) as r:
            return json.load(r)["id"]


def set_thumbnail(video_id, thumb, token):
    with open(os.path.join(ROOT, thumb), "rb") as f:
        req = urllib.request.Request(
            f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={video_id}",
            data=f.read(), method="POST", headers={"Authorization": f"Bearer {token}", "Content-Type": "image/png"})
    try:
        urllib.request.urlopen(req).read()
        print("Thumbnail set")
    except urllib.error.HTTPError as e:
        # Custom thumbnails need a phone-verified channel; the upload itself is fine without it
        print("Thumbnail not set (verify the channel by phone to allow custom thumbnails):", e.code)


def record(meta, video_id):
    path = os.path.join(ROOT, "content", "bp101t", "videos.json")
    data = json.load(open(path, encoding="utf-8"))
    for ep in data.get(meta["lesson"], []):
        if ep["episode"] == meta["episode"]:
            ep["sources"].setdefault(meta["language"], {})["youtube"] = video_id
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    meta = json.load(open(os.path.join(ROOT, sys.argv[1]), encoding="utf-8"))
    try:
        token = access_token()
    except urllib.error.HTTPError as e:
        sys.exit(f"Google refused the YouTube credentials ({e.code}). Check the three YT_ secrets.")
    try:
        video_id = upload(meta, token)
    except urllib.error.HTTPError as e:
        sys.exit(f"Upload failed ({e.code}): {e.read().decode()[:500]}")
    print(f"Uploaded as PRIVATE: https://youtu.be/{video_id}")
    if meta.get("thumbnail"):
        set_thumbnail(video_id, meta["thumbnail"], token)
    record(meta, video_id)
    with open(os.environ.get("GITHUB_OUTPUT", os.devnull), "a") as out:
        out.write(f"video_id={video_id}\n")
