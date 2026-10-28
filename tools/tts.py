"""Generate Campus Champ narration audio from scripts/<course>/<lesson>.json.

Each script track becomes audio/<course>/<lesson>/<lang>/<prefix>NN.mp3.
Existing files are skipped unless overwrite=True, so re-running only fills gaps.
"""
import glob
import json
import os
import subprocess
import tempfile

import soundfile as sf
import torch

MODEL_ID = "ai4bharat/indic-parler-tts"
SEED = 7
STYLE = (
    "{voice} speaks in a calm, warm and soothing tone, like a kind teacher, "
    "at a slightly slow pace with natural pauses. Her voice is friendly and expressive. "
    "The recording is very high quality, close-sounding and clear, with no background noise."
)


def load_model():
    from parler_tts import ParlerTTSForConditionalGeneration
    from transformers import AutoTokenizer

    device = "cuda" if torch.cuda.is_available() else "cpu"
    # float32 everywhere: half precision can crash the audio decoder on T4 GPUs
    model = ParlerTTSForConditionalGeneration.from_pretrained(MODEL_ID).to(device).eval()
    print(f"Voice model loaded on {device.upper()}", flush=True)
    tok = AutoTokenizer.from_pretrained(MODEL_ID)
    desc_tok = AutoTokenizer.from_pretrained(model.config.text_encoder._name_or_path)
    return model, tok, desc_tok, device


def speak(bundle, voice, text):
    model, tok, desc_tok, device = bundle
    torch.manual_seed(SEED)
    d = desc_tok(STYLE.format(voice=voice), return_tensors="pt").to(device)
    p = tok(text, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(
            input_ids=d.input_ids,
            attention_mask=d.attention_mask,
            prompt_input_ids=p.input_ids,
            prompt_attention_mask=p.attention_mask,
        )
    return out.to(torch.float32).cpu().numpy().squeeze(), model.config.sampling_rate


def to_mp3(audio, rate, path):
    """Write a loudness-normalised 128 kbps mp3 (same settings as Lesson 1.1)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav") as wav:
        sf.write(wav.name, audio, rate)
        subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-y", "-i", wav.name,
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", "-b:a", "128k", path],
            check=True,
        )


def check(audio, rate, text):
    """Flag clips whose length doesn't fit the text (cut off, or rambling)."""
    seconds = len(audio) / rate
    words = len(text.split())
    if seconds < 1.0 or seconds < words / 5:
        return f"too short ({seconds:.1f}s for {words} words)"
    if seconds > words / 1.2 + 4:
        return f"too long ({seconds:.1f}s for {words} words)"
    return None


def pending(repo, lessons=None, overwrite=False):
    """List (script, track, index, text, out_path) still to generate."""
    jobs = []
    for script in sorted(glob.glob(os.path.join(repo, "scripts", "*", "*.json"))):
        doc = json.load(open(script, encoding="utf-8"))
        if lessons and doc["lesson"] not in lessons:
            continue
        for track in doc["tracks"]:
            for i, text in enumerate(track["tts"], 1):
                out = os.path.join(repo, "audio", doc["course"], doc["lesson"], track["lang"],
                                   f"{track['prefix']}{i:02d}.mp3")
                if overwrite or not os.path.exists(out):
                    jobs.append((doc, track, i, text, out))
    return jobs


def run(repo, lessons=None, overwrite=False, bundle=None, log=lambda m: print(m, flush=True)):
    jobs = pending(repo, lessons, overwrite)
    log(f"{len(jobs)} clip(s) to generate")
    if not jobs:
        return [], []
    bundle = bundle or load_model()
    made, problems = [], []
    for doc, track, i, text, out in jobs:
        voice = doc["voices"][track["lang"]]
        audio, rate = speak(bundle, voice, text)
        issue = check(audio, rate, text)
        if issue:
            # one retry with a different seed before flagging
            global SEED
            saved, SEED = SEED, SEED + 4
            audio, rate = speak(bundle, voice, text)
            SEED = saved
            issue = check(audio, rate, text)
        to_mp3(audio, rate, out)
        rel = os.path.relpath(out, repo)
        made.append(rel)
        log(f"{'⚠️ ' + issue if issue else '✅'}  {rel}  ({len(audio) / rate:.1f}s)")
        if issue:
            problems.append((rel, issue))
    return made, problems
