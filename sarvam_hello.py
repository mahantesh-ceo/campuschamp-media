"""One Sarvam AI chat call, to check the API key works. Run: python3 sarvam_hello.py"""
import os
import sys

from sarvamai import SarvamAI

# Read SARVAM_API_KEY from .env (if present) without overriding the environment
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(env_path):
    for line in open(env_path):
        name, sep, value = line.strip().partition("=")
        if sep and name and not name.startswith("#"):
            os.environ.setdefault(name.strip(), value.strip())

key = os.environ.get("SARVAM_API_KEY", "")
if not key:
    sys.exit("SARVAM_API_KEY is empty. Paste your key into .env and run again.")

client = SarvamAI(api_subscription_key=key)
response = client.chat.completions(
    model="sarvam-105b-conversations",
    messages=[{"role": "user", "content": "Say hello in Kannada in one short sentence."}],
)
print(response.choices[0].message.content)
