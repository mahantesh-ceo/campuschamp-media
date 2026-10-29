"""Sarvam Bulbul text-to-speech for Campus Champ narration.

Key: SARVAM_API_KEY from the environment/.env, or a network secret that adds it to api.sarvam.ai
requests (then set SARVAM_KEY_FROM_NETWORK=1).
"""
import base64
import os
import subprocess
import tempfile

from sarvamai import SarvamAI


def client():
    env = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    if os.path.exists(env):
        for line in open(env):
            name, sep, value = line.strip().partition("=")
            if sep and name and not name.startswith("#"):
                os.environ.setdefault(name.strip(), value.strip())
    key = os.environ.get("SARVAM_API_KEY", "")
    if not key and not os.environ.get("SARVAM_KEY_FROM_NETWORK"):
        raise SystemExit("SARVAM_API_KEY is empty (or set SARVAM_KEY_FROM_NETWORK=1 with a network secret).")
    return SarvamAI(api_subscription_key=key or "set-by-network-secret")


def speak(c, text, out_mp3, speaker, model="bulbul:v4-flash", lang="kn-IN", pace=1.0, temperature=0.6):
    """Narrate text (native script; English words may stay in Latin script) to a loudness-normalised mp3."""
    r = c.text_to_speech.convert(text=text, model=model, language_code=lang, speaker=speaker,
                                 pace=pace, temperature=temperature, speech_sample_rate=48000)
    wav = base64.b64decode("".join(r.audios))
    os.makedirs(os.path.dirname(out_mp3) or ".", exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        w.write(wav)
        w.flush()
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", w.name, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                        "-ar", "44100", "-b:a", "160k", out_mp3], check=True)
    return out_mp3
