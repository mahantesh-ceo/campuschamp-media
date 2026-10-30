"""Generates an original product-launch music track (no licensing issues): a quiet ticking build,
a riser into an impact at the reveal, then a full, hopeful groove that resolves at the end.
Usage: python3 make_launch.py <seconds> <reveal seconds> <out.wav>"""
import sys, wave
import numpy as np

SR = 44100
dur, reveal, out = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
n = int(SR * dur)
mix = np.zeros(n)
bpm = 100; beat = 60 / bpm; bar = beat * 4
rng = np.random.default_rng(7)

def note(m):
    return 440 * 2 ** ((m - 69) / 12)

def add(start, sig, gain=1.0):
    s = int(start * SR)
    if s >= n or s + len(sig) <= 0:
        return
    e = min(n, s + len(sig))
    mix[max(0, s):e] += gain * sig[max(0, -s):e - s]

def tone(f, length, decay, harm=(1, 0.3, 0.12)):
    tt = np.arange(int(length * SR)) / SR
    env = np.exp(-tt * decay) * np.minimum(1, tt / 0.004)
    return env * sum(a * np.sin(2 * np.pi * f * (k + 1) * tt) for k, a in enumerate(harm))

# Am - F - C - G: hopeful, cinematic
chords = [[57, 60, 64], [53, 57, 60], [48, 55, 64], [55, 59, 62]]
roots = [45, 41, 48, 43]
def chord_at(t):
    return int(t / bar) % 4

# 1) pad, always there, swelling after the reveal
for i in range(int(dur / bar) + 1):
    t0 = i * bar
    c = chords[i % 4]
    length = bar + 0.8
    tt = np.arange(int(length * SR)) / SR
    env = np.minimum(1, tt / 0.9) * np.exp(-np.maximum(0, tt - bar) * 4)
    level = 0.035 if t0 < reveal else 0.05
    for m in c:
        f = note(m)
        add(t0, env * (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(2 * np.pi * f * 1.003 * tt) + 0.2 * np.sin(2 * np.pi * 2 * f * tt)), level)

# 2) the build: a soft tick on every eighth, getting brighter towards the reveal
step = beat / 2
k = 0
while k * step < min(reveal, dur):
    t0 = k * step
    p = t0 / max(reveal, 0.1)
    click = rng.standard_normal(int(0.03 * SR)) * np.exp(-np.arange(int(0.03 * SR)) / SR * 160)
    add(t0, np.diff(click, prepend=0), 0.05 + 0.08 * p)
    if k % 2 == 0:  # heartbeat-like low pulse
        add(t0, tone(note(33), 0.35, 9, (1, 0.2)), 0.12 + 0.15 * p)
    k += 1

# 3) riser into the reveal (filtered noise + rising tone, last two bars)
r0 = max(0, reveal - 2 * bar)
length = reveal - r0
if length > 0.2:
    tt = np.arange(int(length * SR)) / SR
    noise = rng.standard_normal(len(tt))
    noise = np.convolve(noise, np.ones(8) / 8, mode='same')
    sweep = np.sin(2 * np.pi * np.cumsum(np.linspace(200, 1400, len(tt))) / SR)
    env = (tt / length) ** 2
    add(r0, env * (0.06 * noise + 0.05 * sweep), 1.0)

# 4) impact at the reveal: sub boom + bright shimmer
tt = np.arange(int(2.5 * SR)) / SR
boom = np.sin(2 * np.pi * (55 * np.exp(-tt * 1.5) + 30) * tt) * np.exp(-tt * 1.8)
shimmer = sum(np.sin(2 * np.pi * note(m) * tt) for m in (69, 76, 81, 88)) * np.exp(-tt * 1.2)
add(reveal, 0.55 * boom + 0.03 * shimmer, 1.0)

# 5) after the reveal: kick, bass ostinato, bright arpeggio
t0 = reveal
end_groove = dur - 2.5
k = 0
while t0 + k * step < end_groove:
    t = t0 + k * step
    c = chord_at(t)
    if k % 2 == 0:  # kick on every beat
        kt = np.arange(int(0.3 * SR)) / SR
        add(t, np.sin(2 * np.pi * (110 * np.exp(-kt * 25) + 45) * kt) * np.exp(-kt * 12), 0.22)
    if k % 4 == 2:  # off-beat snap
        sn = rng.standard_normal(int(0.12 * SR)) * np.exp(-np.arange(int(0.12 * SR)) / SR * 35)
        add(t, sn, 0.035)
    add(t, tone(note(roots[c] - 12 + (12 if k % 4 == 3 else 0)), step * 0.95, 6, (1, 0.5, 0.2)), 0.09)
    arp = chords[c][[0, 1, 2, 1][k % 4]] + 12
    add(t, tone(note(arp), 0.5, 7, (1, 0.25, 0.1)), 0.045)
    k += 1

# 6) final chord rings out
tt = np.arange(int(3 * SR)) / SR
final = sum(np.sin(2 * np.pi * note(m) * tt) for m in (57, 64, 69, 72)) * np.exp(-tt * 0.9) * np.minimum(1, tt / 0.05)
add(max(0, end_groove), final, 0.06)

# fade in/out, normalise
fade = int(1.2 * SR)
mix[:fade] *= np.linspace(0, 1, fade)
mix[-fade:] *= np.linspace(1, 0, fade)
mix /= max(1e-6, np.abs(mix).max()) / 0.8
stereo = np.stack([mix, np.roll(mix, int(0.012 * SR))], axis=1)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((stereo * 32767).astype(np.int16).tobytes())
