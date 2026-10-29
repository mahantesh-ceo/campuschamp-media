"""Kannada narration for BP101T 1.1 Episode 1. Writes bp101t-1-1-ep1.kn.json:
display text (subtitles) and TTS text (English words spelt in Kannada for the voice)."""
import json, re, os

LINES = [
  ("cold", "ಸೋಮವಾರ ಬೆಳಿಗ್ಗೆ. ಬಾಗಲಕೋಟೆಯ ಒಂದು pharmacy."),
  ("cold", "ಇನ್ನೂರು prescriptions ಕಾಯ್ತಾ ಇವೆ."),
  ("cold", "ಪ್ರತಿಯೊಂದೂ instructions ನ ಒಂದು ಚಿಕ್ಕ set. Pharmacist ಪ್ರತಿಯೊಂದನ್ನೂ step by step follow ಮಾಡ್ತಾರೆ."),
  ("rx", "ಬನ್ನಿ, ಒಂದು prescription ಅನ್ನು ಹತ್ತಿರದಿಂದ ನೋಡೋಣ."),
  ("rx", "ಇದರಲ್ಲಿ ಮೂರು lines ಇವೆ."),
  ("rx", "Paracetamol ಐನೂರು milligram."),
  ("rx", "ಒಂದು tablet ತಗೊಳ್ಳಿ."),
  ("rx", "ದಿನಕ್ಕೆ ಮೂರು ಸಲ, ಊಟದ ನಂತರ."),
  ("rx", "ಇಲ್ಲಿ ಮೂರು ವಿಷಯ ಗಮನಿಸಿ."),
  ("rx", "ಮೊದಲನೆಯದು, ಪ್ರತಿ line ಒಂದು clear instruction."),
  ("rx", "ಎರಡನೆಯದು, ಅವು ಒಂದು ಕ್ರಮದಲ್ಲಿ, ಅಂದ್ರೆ order ನಲ್ಲಿ ಬರೆದಿವೆ."),
  ("rx", "ಮೂರನೆಯದು, patient ಅವನ್ನು ಬರೆದ ಹಾಗೆಯೇ, exactly follow ಮಾಡ್ತಾರೆ."),
  ("rx", "ಈ ಮೂರು ಪದಗಳನ್ನು ನೆನಪಿಟ್ಟುಕೊಳ್ಳಿ. Clear. In order. Followed exactly."),
  ("rx", "ಈ ಇಡೀ lesson ಇವುಗಳ ಸುತ್ತಾನೇ ಇದೆ."),
  ("unclear", "ಈಗ, ಎರಡನೇ line ಬರೀ tablet ತಗೊಳ್ಳಿ ಅಂತ ಇದ್ರೆ?"),
  ("unclear", "ಯಾವ tablet? ಎಷ್ಟು tablets?"),
  ("unclear", "ಒಬ್ಬ ಮನುಷ್ಯ ಆದ್ರೆ, doctor ಗೆ call ಮಾಡಿ ಕೇಳ್ತಾರೆ."),
  ("unclear", "ಮತ್ತೆ lines ಎಲ್ಲಾ ಉಲ್ಟಾಪಲ್ಟಾ ಆದ್ರೆ, ಅರ್ಥಾನೇ ಬದಲಾಗಬಹುದು."),
  ("unclear", "ಔಷಧಿಗಳ ವಿಷಯದಲ್ಲಿ, ಒಂದು ಚಿಕ್ಕ confusion ಕೂಡ ಅಪಾಯ."),
  ("unclear", "ಅದಕ್ಕೇ prescriptions ಅನ್ನು clear ಆಗಿ, order ನಲ್ಲಿ ಬರೀತಾರೆ."),
  ("chip", "ಈಗ computer ಅನ್ನು ಭೇಟಿ ಮಾಡೋಣ."),
  ("chip", "ಇದು ತುಂಬಾ fast. ಒಂದು second ನಲ್ಲಿ ಲಕ್ಷಾಂತರ steps ಮಾಡುತ್ತೆ."),
  ("chip", "ಮತ್ತು ಇದು ಯಾವತ್ತೂ ಸುಸ್ತಾಗಲ್ಲ."),
  ("chip", "ಆದ್ರೆ ಒಂದು surprise ಇದೆ. ಇದಕ್ಕೆ common sense ಸ್ವಲ್ಪನೂ ಇಲ್ಲ."),
  ("chip", "ನೀವು ಏನು ಅಂದ್ಕೊಂಡಿದ್ದೀರಿ ಅಂತ ಇದು guess ಮಾಡಲ್ಲ."),
  ("chip", "Computer ಗೆ ಹೇಳಿ: tablets count ಮಾಡು."),
  ("chip", "ಅದು ಅಲ್ಲೇ ನಿಂತುಬಿಡುತ್ತೆ. ಯಾವ tablets? ಎಲ್ಲಿ? ಹೇಗೆ count ಮಾಡೋದು?"),
  ("chip", "ಆದ್ರೆ clear steps ಕೊಡಿ, order ನಲ್ಲಿ."),
  ("chip", "Strip ನೋಡು. Zero ಇಂದ ಶುರು ಮಾಡು. ಪ್ರತಿ tablet ಗೆ ಒಂದು ಸೇರಿಸು. Total ತೋರಿಸು."),
  ("chip", "ಈಗ ಅದು ಕೆಲಸವನ್ನ perfect ಆಗಿ ಮಾಡುತ್ತೆ, ಪ್ರತಿ ಸಲ."),
  ("program", "Order ನಲ್ಲಿ ಬರೆದ, computer exactly follow ಮಾಡುವ, clear instructions ನ list."),
  ("program", "ಇದಕ್ಕೆ ಒಂದು ಹೆಸರಿದೆ."),
  ("program", "ಇದನ್ನು program ಅಂತಾರೆ."),
  ("program", "ಹಾಗಾಗಿ program ಅಂದ್ರೆ, prescription ತರಹನೇ."),
  ("program", "Prescription patient ಗಾಗಿ ಬರೆದದ್ದು. Program computer ಗಾಗಿ ಬರೆದದ್ದು."),
  ("exact", "ನೆನಪಿಡಿ, computer instructions ಅನ್ನು exactly follow ಮಾಡುತ್ತೆ."),
  ("exact", "ನೀವು ತಪ್ಪಾಗಿ ಒಂದು ಬದಲು ಹತ್ತು ಅಂತ ಬರೆದ್ರೆ, ಅದು ನಿಮ್ಮನ್ನ ಕೇಳಲ್ಲ."),
  ("exact", "ಖುಷಿಯಾಗಿ ಹತ್ತು ಅಂತಾನೇ ತೋರಿಸುತ್ತೆ."),
  ("exact", "ಅದಕ್ಕೇ programming ನಲ್ಲೂ, pharmacy ತರಹನೇ, ಚಿಕ್ಕ details ತುಂಬಾ ಮುಖ್ಯ."),
  ("exact", "ಚಿಂತೆ ಬೇಡ. Computer ಗೆ ಏನಾದ್ರೂ ಅರ್ಥ ಆಗದಿದ್ರೆ, ಅದು ನಮಗೆ ಹೇಳುತ್ತೆ."),
  ("exact", "ಅದನ್ನ ಮೂರನೇ episode ನಲ್ಲಿ ನೋಡೋಣ."),
  ("around", "ನಿಮ್ಮ phone ನಲ್ಲಿರುವ ಪ್ರತಿ app ಒಂದು program."),
  ("around", "Medical shop ನ billing software."),
  ("around", "Sugar reading ತೋರಿಸುವ glucometer."),
  ("around", "Patient records ಇಡುವ hospital system."),
  ("around", "ಇವೆಲ್ಲಾ ಯಾರೋ ಬರೆದ instructions ನ lists."),
  ("around", "ಸ್ವಲ್ಪ ದಿನದಲ್ಲೇ, ನೀವೂ ಇಂಥವನ್ನ ಬರೀತೀರಿ."),
  ("quiz", "ಒಂದು quick check. ಇವುಗಳಲ್ಲಿ program ಯಾವುದು?"),
  ("quiz", "ಬೇಕಾದ್ರೆ video pause ಮಾಡಿ ಯೋಚಿಸಿ."),
  ("quiz-answer", "ಉತ್ತರ B. Computer order ನಲ್ಲಿ follow ಮಾಡುವ, clear instructions ನ list. Super!"),
  ("recap", "ಒಮ್ಮೆ recap ಮಾಡೋಣ."),
  ("recap", "Program ಅಂದ್ರೆ, computer ಗಾಗಿ ಬರೆದ instructions ನ list."),
  ("recap", "ಅವು clear ಆಗಿರಬೇಕು, order ನಲ್ಲಿರಬೇಕು."),
  ("recap", "Computer ಅವನ್ನು exactly follow ಮಾಡುತ್ತೆ."),
  ("teaser", "ಆದ್ರೆ ಒಂದು problem ಇದೆ. Computer ಗೆ English ಆಗಲಿ, ಕನ್ನಡ ಆಗಲಿ ಅರ್ಥ ಆಗಲ್ಲ."),
  ("teaser", "ಹಾಗಾದ್ರೆ ಅದಕ್ಕೆ ಅರ್ಥ ಆಗುವ instructions ಹೇಗೆ ಬರೆಯೋದು?"),
  ("teaser", "ಅದೇ ಮುಂದಿನ episode. Python ಯಾಕೆ? ಅಲ್ಲಿ ಸಿಗೋಣ!"),
]

# English words → how the Kannada voice should say them
SAY = {
  "pharmacy": "ಫಾರ್ಮಸಿ", "prescriptions": "ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ಸ್", "prescription": "ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್",
  "instructions": "ಇನ್ಸ್ಟ್ರಕ್ಷನ್ಸ್", "instruction": "ಇನ್ಸ್ಟ್ರಕ್ಷನ್", "set": "ಸೆಟ್", "pharmacist": "ಫಾರ್ಮಸಿಸ್ಟ್",
  "step": "ಸ್ಟೆಪ್", "steps": "ಸ್ಟೆಪ್ಸ್", "by": "ಬೈ", "follow": "ಫಾಲೋ", "followed": "ಫಾಲೋಡ್", "lines": "ಲೈನ್ಸ್",
  "line": "ಲೈನ್", "paracetamol": "ಪ್ಯಾರಸಿಟಮಾಲ್", "milligram": "ಮಿಲಿಗ್ರಾಮ್", "tablet": "ಟ್ಯಾಬ್ಲೆಟ್",
  "tablets": "ಟ್ಯಾಬ್ಲೆಟ್ಸ್", "clear": "ಕ್ಲಿಯರ್", "order": "ಆರ್ಡರ್", "in": "ಇನ್", "patient": "ಪೇಷಂಟ್",
  "exactly": "ಎಕ್ಸಾಕ್ಟ್ಲಿ", "lesson": "ಲೆಸನ್", "doctor": "ಡಾಕ್ಟರ್", "call": "ಕಾಲ್", "confusion": "ಕನ್ಫ್ಯೂಷನ್",
  "computer": "ಕಂಪ್ಯೂಟರ್", "fast": "ಫಾಸ್ಟ್", "second": "ಸೆಕೆಂಡ್", "surprise": "ಸರ್ಪ್ರೈಸ್", "common": "ಕಾಮನ್",
  "sense": "ಸೆನ್ಸ್", "guess": "ಗೆಸ್", "count": "ಕೌಂಟ್", "strip": "ಸ್ಟ್ರಿಪ್", "zero": "ಜೀರೋ", "total": "ಟೋಟಲ್",
  "perfect": "ಪರ್ಫೆಕ್ಟ್", "list": "ಲಿಸ್ಟ್", "lists": "ಲಿಸ್ಟ್ಸ್", "program": "ಪ್ರೋಗ್ರಾಮ್",
  "programming": "ಪ್ರೋಗ್ರಾಮಿಂಗ್", "details": "ಡೀಟೇಲ್ಸ್", "episode": "ಎಪಿಸೋಡ್", "phone": "ಫೋನ್", "app": "ಆ್ಯಪ್",
  "medical": "ಮೆಡಿಕಲ್", "shop": "ಶಾಪ್", "billing": "ಬಿಲ್ಲಿಂಗ್", "software": "ಸಾಫ್ಟ್‌ವೇರ್", "sugar": "ಶುಗರ್",
  "reading": "ರೀಡಿಂಗ್", "glucometer": "ಗ್ಲೂಕೋಮೀಟರ್", "records": "ರೆಕಾರ್ಡ್ಸ್", "hospital": "ಹಾಸ್ಪಿಟಲ್",
  "system": "ಸಿಸ್ಟಮ್", "quick": "ಕ್ವಿಕ್", "check": "ಚೆಕ್", "video": "ವಿಡಿಯೋ", "pause": "ಪಾಸ್", "b": "ಬಿ",
  "super": "ಸೂಪರ್", "recap": "ರೀಕ್ಯಾಪ್", "problem": "ಪ್ರಾಬ್ಲಮ್", "english": "ಇಂಗ್ಲಿಷ್", "python": "ಪೈಥಾನ್",
}

def tts(text):
    def rep(m):
        w = m.group(0)
        if w.lower() not in SAY:
            raise SystemExit(f"no Kannada spelling for '{w}'")
        return SAY[w.lower()]
    return re.sub(r"[A-Za-z]+", rep, text)

out = {"course": "bp101t", "lesson": "1-1", "episode": 1, "lang": "kn", "voice": "Anu",
       "lines": [{"id": f"l{i + 1:02d}", "scene": s, "say": t, "tts": tts(t)} for i, (s, t) in enumerate(LINES)]}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bp101t-1-1-ep1.kn.json")
json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
print(len(LINES), "lines →", path)
