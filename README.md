# Campus Champ media

Audio and other media for campuschamp.in, served through jsDelivr:

`https://cdn.jsdelivr.net/gh/mahantesh-ceo/campuschamp-media@main/<path>`

## Layout

```
scripts/<course>/<lesson>.json                    what each clip says (English, Hindi, Kannada)
audio/<course>/<lesson>/<lang>/step-NN.mp3        narrator steps
audio/<course>/<lesson>/<lang>/anim-<id>-NN.mp3   animation steps
tools/tts.py                                      the generator
notebooks/generate_audio.ipynb                    run it on Google Colab
```

Languages: `en` (voice: Mary), `hi` (voice: Rani; also used for Hinglish), `kn` (voice: Anu).
Voices are generated with [Indic Parler-TTS](https://huggingface.co/ai4bharat/indic-parler-tts) (AI4Bharat, Apache-2.0).

## Make audio on Google Colab

**Open the notebook:**
https://colab.research.google.com/github/mahantesh-ceo/campuschamp-media/blob/main/notebooks/generate_audio.ipynb

### One-time setup (about 5 minutes)

**1. Hugging Face token**
1. Go to huggingface.co → your profile picture → **Settings** → **Access Tokens** → **Create new token**.
2. Token type: **Read**. Name: `colab`. Click **Create** and copy it.
   (You already accepted the Indic Parler-TTS terms with this account, so nothing else is needed.)

**2. GitHub token** (lets the notebook upload audio to this repository only)
1. Go to github.com → your profile picture → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**.
2. Name: `colab-audio`. Expiration: 90 days.
3. Repository access: **Only select repositories** → `campuschamp-media`.
4. Permissions → Repository permissions → **Contents: Read and write**.
5. Click **Generate token** and copy it.

**3. Add both tokens to Colab**
1. Open the notebook link above.
2. Click the 🔑 **key icon** (Secrets) in the left sidebar.
3. **Add new secret**: Name `HF_TOKEN`, Value = your Hugging Face token. Switch **Notebook access** on.
4. **Add new secret**: Name `GITHUB_TOKEN`, Value = your GitHub token. Switch **Notebook access** on.

**4. Turn on the free GPU**
`Runtime` → `Change runtime type` → **T4 GPU** → **Save**.

### Every time

`Runtime` → `Run all`. If Colab asks "Allow this notebook to access your secrets?", click **Grant access**.

The notebook only makes clips that are missing, uploads them, and prints any clip worth a listen.
