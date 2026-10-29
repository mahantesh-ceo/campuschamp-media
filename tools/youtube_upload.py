"""Publishes one episode to YouTube, at most once, and keeps the course playlist in order.

- Already on YouTube (id in content/bp101t/videos.json)? No new upload: the title/description are
  refreshed and the video is made sure to be in the playlist. So the same episode is never uploaded twice.
- New episode: uploaded (public by default), numbered "#N" in course order for its language,
  added to the course playlist (created automatically), id saved for the website.

Runs in GitHub Actions with secrets YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN
(the refresh token needs the https://www.googleapis.com/auth/youtube scope for playlists).
Usage: python tools/youtube_upload.py video/meta/<episode>.json
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS = os.path.join(ROOT, "content", "bp101t", "videos.json")
PLAYLISTS = os.path.join(ROOT, "video", "playlists.json")
API = "https://www.googleapis.com/youtube/v3"
# public (default) · private · or a scheduled time like 2026-11-02T18:30:00+05:30 (private until then)
WHEN = os.environ.get("PUBLISH", "public").strip() or "public"
PUBLISH_AT = WHEN if WHEN not in ("private", "public") else ""
PRIVACY = "public" if WHEN == "public" else "private"
LANG_NAME = {"kn": "ಕನ್ನಡ", "hi": "हिन्दी", "en": "English"}


def load(path, default):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else default


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def access_token():
    data = urllib.parse.urlencode({
        "client_id": os.environ["YT_CLIENT_ID"].strip(),
        "client_secret": os.environ["YT_CLIENT_SECRET"].strip(),
        "refresh_token": os.environ["YT_REFRESH_TOKEN"].strip(),
        "grant_type": "refresh_token",
    }).encode()
    try:
        with urllib.request.urlopen("https://oauth2.googleapis.com/token", data) as r:
            return json.load(r)["access_token"]
    except urllib.error.HTTPError as e:
        why = {}
        try:
            why = json.loads(e.read().decode())
        except Exception:
            pass
        sys.exit(f"Google refused the YouTube credentials ({e.code} {why.get('error')}: {why.get('error_description', '')}). Check the three YT_ secrets.")


def call(method, url, token, body=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8"})
    try:
        with urllib.request.urlopen(req) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode()[:400]
        if e.code == 403 and "insufficient" in detail.lower():
            sys.exit("YouTube says the sign-in can only upload, not manage playlists. Make a new refresh token with the "
                     "https://www.googleapis.com/auth/youtube scope and update YT_REFRESH_TOKEN.")
        sys.exit(f"YouTube API error {e.code} on {url.split('?')[0]}: {detail}")


def find_episode(videos, meta):
    for ep in videos.get(meta["lesson"], []):
        if ep["episode"] == meta["episode"]:
            return ep
    sys.exit(f"Lesson {meta['lesson']} episode {meta['episode']} isn't in content/bp101t/videos.json yet.")


def episode_number(videos, meta):
    """#N: this episode's place in the course for this language (lessons in order, then episodes)."""
    order = sorted((k for k in videos if not k.startswith("_")), key=lambda k: [int(x) for x in k.split("-")])
    n = 0
    for lesson in order:
        for ep in sorted(videos[lesson], key=lambda e: e["episode"]):
            if meta["language"] in ep["sources"]:
                n += 1
            if lesson == meta["lesson"] and ep["episode"] == meta["episode"]:
                return n
    return n


def snippet(meta, number):
    chapters = open(os.path.join(ROOT, meta["chapters"]), encoding="utf-8").read().strip() if meta.get("chapters") else ""
    lang = meta["language"]
    title = f"{meta['topic']} | BP101T Python {LANG_NAME.get(lang, lang)} #{number} | Lesson {meta['lesson'].replace('-', '.')} · Episode {meta['episode']}"
    return {
        "title": title[:100],
        "description": meta["description"].replace("{{CHAPTERS}}", chapters),
        "tags": meta.get("tags", []),
        "categoryId": "27",  # Education
        "defaultLanguage": lang,
        "defaultAudioLanguage": lang,
    }


def upload(meta, body, token):
    path = os.path.join(ROOT, meta["file"])
    size = os.path.getsize(path)
    req = urllib.request.Request(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json; charset=UTF-8",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
    with urllib.request.urlopen(req) as r:
        session = r.headers["Location"]
    with open(path, "rb") as f:
        put = urllib.request.Request(session, data=f.read(), method="PUT",
                                     headers={"Content-Type": "video/mp4", "Content-Length": str(size)})
        with urllib.request.urlopen(put) as r:
            return json.load(r)["id"]


def set_thumbnail(video_id, thumb, token):
    with open(os.path.join(ROOT, thumb), "rb") as f:
        req = urllib.request.Request(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={video_id}",
                                     data=f.read(), method="POST",
                                     headers={"Authorization": f"Bearer {token}", "Content-Type": "image/png"})
    try:
        urllib.request.urlopen(req).read()
        print("Thumbnail set")
    except urllib.error.HTTPError as e:
        print("Thumbnail not set:", e.code)


def playlist_id(meta, token):
    """The course playlist for this language, created on first use and remembered in video/playlists.json."""
    lists = load(PLAYLISTS, {})
    key = f"bp101t-{meta['language']}"
    if lists.get(key):
        return lists[key]
    lang = LANG_NAME.get(meta["language"], meta["language"])
    created = call("POST", f"{API}/playlists?part=snippet,status", token, {
        "snippet": {
            "title": f"BP101T Python in {lang} | B.Pharm Sem I | Campus Champ",
            "description": "BP101T Basics of Python Programming for Pharmaceutical Sciences (PCI, B.Pharm Sem I), "
                           f"every lesson in order, in {lang}. Practise free: https://www.campuschamp.in/learn/bp101t",
            "defaultLanguage": meta["language"],
        },
        "status": {"privacyStatus": "public"},
    })
    lists[key] = created["id"]
    save(PLAYLISTS, lists)
    print("Created playlist:", f"https://www.youtube.com/playlist?list={created['id']}")
    return created["id"]


def ensure_in_playlist(pl, video_id, number, token):
    items, page = [], ""
    while True:
        r = call("GET", f"{API}/playlistItems?part=snippet&maxResults=50&playlistId={pl}{'&pageToken=' + page if page else ''}", token)
        items += r.get("items", [])
        page = r.get("nextPageToken", "")
        if not page:
            break
    if any(i["snippet"]["resourceId"].get("videoId") == video_id for i in items):
        print("Already in the playlist")
        return
    body = {"snippet": {"playlistId": pl, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}
    if number - 1 <= len(items):
        body["snippet"]["position"] = number - 1  # keep course order
    call("POST", f"{API}/playlistItems?part=snippet", token, body)
    print(f"Added to the playlist at #{number}")


if __name__ == "__main__":
    meta = json.load(open(os.path.join(ROOT, sys.argv[1]), encoding="utf-8"))
    videos = load(VIDEOS, {})
    ep = find_episode(videos, meta)
    src = ep["sources"].setdefault(meta["language"], {})
    number = episode_number(videos, meta)
    token = access_token()
    snip = snippet(meta, number)
    existing = src.get("youtube") or src.get("youtube_pending")

    if existing:
        # Never upload the same episode twice: refresh its title/description instead
        call("PUT", f"{API}/videos?part=snippet", token, {"id": existing, "snippet": snip})
        print(f"Already on YouTube, updated title/description: https://youtu.be/{existing}")
        video_id = existing
    else:
        body = {"snippet": snip, "status": {"privacyStatus": PRIVACY, "selfDeclaredMadeForKids": False,
                                            "containsSyntheticMedia": True}}  # AI voice disclosure
        if PUBLISH_AT:
            body["status"]["publishAt"] = PUBLISH_AT
        try:
            video_id = upload(meta, body, token)
        except urllib.error.HTTPError as e:
            sys.exit(f"Upload failed ({e.code}): {e.read().decode()[:500]}")
        print(f"Uploaded ({'public' if PRIVACY == 'public' else 'scheduled ' + PUBLISH_AT if PUBLISH_AT else 'private'}): https://youtu.be/{video_id}")
        if meta.get("thumbnail"):
            set_thumbnail(video_id, meta["thumbnail"], token)
        # Public now → the website plays it from YouTube; otherwise pending until promote_published.py sees it public
        src["youtube" if PRIVACY == "public" else "youtube_pending"] = video_id
        save(VIDEOS, videos)

    ensure_in_playlist(playlist_id(meta, token), video_id, number, token)
