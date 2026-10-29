"""Generates a soft, original background music bed (no licensing issues).
Usage: python3 make_bed.py <seconds> <out.wav>"""
import sys, wave
import numpy as np

SR = 44100
dur = float(sys.argv[1]); out = sys.argv[2]
n = int(SR * dur)
t = np.arange(n) / SR
bpm = 84; beat = 60 / bpm; bar = beat * 4

def note(m):  # MIDI -> Hz
    return 440 * 2 ** ((m - 69) / 12)

# Warm, hopeful loop: Cmaj7 - Am7 - Fmaj7 - G6
chords = [[48, 55, 64, 71], [45, 52, 60, 67], [41, 53, 57, 64], [43, 50, 59, 64]]
mix = np.zeros(n)

# Pads: soft sines with slow swell per bar
for i in range(int(dur / bar) + 1):
    c = chords[i % 4]; s = int(i * bar * SR); e = min(n, int((i + 1) * bar * SR + 0.6 * SR))
    if s >= n: break
    tt = np.arange(e - s) / SR
    env = np.minimum(1, tt / 0.8) * np.exp(-np.maximum(0, tt - bar) * 3)
    for m in c:
        f = note(m)
        mix[s:e] += 0.05 * env * (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(2 * np.pi * 2 * f * tt + 0.3))

# Gentle plucked arpeggio (eighth notes)
step = beat / 2
for k in range(int(dur / step)):
    c = chords[int(k * step / bar) % 4]
    m = c[[0, 2, 1, 3, 2, 1, 3, 2][k % 8]] + 12
    s = int(k * step * SR); e = min(n, s + int(1.2 * SR))
    tt = np.arange(e - s) / SR
    f = note(m)
    mix[s:e] += 0.035 * np.exp(-tt * 4.5) * (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt))

# Soft low pulse on beats 1 and 3
for k in range(int(dur / beat)):
    if k % 2: continue
    s = int(k * beat * SR); e = min(n, s + int(0.35 * SR))
    tt = np.arange(e - s) / SR
    mix[s:e] += 0.08 * np.exp(-tt * 12) * np.sin(2 * np.pi * (55 + 40 * np.exp(-tt * 30)) * tt)

# Fade in/out, normalise
fade = int(2.5 * SR)
mix[:fade] *= np.linspace(0, 1, fade); mix[-fade:] *= np.linspace(1, 0, fade)
mix /= np.max(np.abs(mix)) + 1e-9
stereo = np.stack([mix, np.roll(mix, int(0.012 * SR))], axis=1)
pcm = (stereo * 0.9 * 32767).astype(np.int16)
with wave.open(out, 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('music bed', dur, 's')
