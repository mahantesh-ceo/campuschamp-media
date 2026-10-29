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
if not key and not os.environ.get("SARVAM_KEY_FROM_NETWORK"):
    sys.exit("SARVAM_API_KEY is empty. Paste your key into .env and run again "
             "(or set SARVAM_KEY_FROM_NETWORK=1 when a network secret adds the key to api.sarvam.ai requests).")

# With a network secret, the real key is added to every api.sarvam.ai request outside this program,
# so the SDK only needs a non-empty value to build the request.
client = SarvamAI(api_subscription_key=key or "set-by-network-secret")
response = client.chat.completions(
    model="sarvam-105b-conversations",
    messages=[{"role": "user", "content": "Say hello in Kannada in one short sentence."}],
)
print(response.choices[0].message.content)
