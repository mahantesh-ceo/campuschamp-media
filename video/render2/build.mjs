// Episode timeline: groups narration lines into scenes, adds the brand sting, quiz countdown
// and end card, and records voice loudness per frame (for the voice mark).
// Usage: node build.mjs <episode.json> <clipsDir> <out.json>
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { createRequire } from 'node:module';

const QRCode = createRequire('/home/user/test/package.json')('qrcode');
const FPS = 25;
const GAP = 0.45; // pause between sentences (beginners need room to think)
const LEAD = 0.7;
const TAIL = 0.6;

const [epPath, clipsDir, outPath] = process.argv.slice(2);
const E = JSON.parse(readFileSync(epPath, 'utf8'));

const duration = (f) => Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).toString().trim());
function envelope(f) {
  const raw = execFileSync('ffmpeg', ['-loglevel', 'error', '-i', f, '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], { maxBuffer: 1 << 26 });
  const s = new Int16Array(raw.buffer, raw.byteOffset, raw.length / 2);
  const per = 8000 / FPS;
  const out = [];
  for (let i = 0; i < s.length; i += per) {
    let a = 0;
    const end = Math.min(s.length, i + per);
    for (let j = i; j < end; j++) a += s[j] * s[j];
    out.push(Math.sqrt(a / Math.max(1, end - i)) / 32768);
  }
  const peak = Math.max(0.0001, ...[...out].sort((a, b) => a - b).slice(Math.floor(out.length * 0.95)));
  return out.map((v) => Math.round(Math.min(1, v / peak) * 100) / 100);
}

// Scenes in order; quiz-answer joins the quiz scene after a 5 s countdown
const ORDER = ['cold', 'sting', 'rx', 'unclear', 'chip', 'program', 'exact', 'around', 'quiz', 'recap', 'teaser', 'end'];
const HOLD = { cold: 3.2, sting: 2.8, rx: 0.8, unclear: 0.6, chip: 1.6, program: 1.2, exact: 0.6, around: 1.0, quiz: 1.2, recap: 1.4, teaser: 0.4, end: 6 };
const CHAPTER = { cold: 'Intro', rx: 'ಒಂದು prescription', unclear: 'Clear ಆಗಿರದಿದ್ರೆ?', chip: 'Computer ಅನ್ನು ಭೇಟಿ ಮಾಡಿ', program: 'Program', exact: 'Exactly ಅಂದ್ರೆ exactly', around: 'ನಿಮ್ಮ ಸುತ್ತಾ programs', quiz: 'Quick check', recap: 'Recap', teaser: 'ಮುಂದೆ ಏನು?', end: 'Practise free' };

let t = 0;
const scenes = [];
const audio = [];
for (const type of ORDER) {
  const start = t;
  const lines = [];
  const mine = E.lines.filter((l) => l.scene === type || (type === 'quiz' && l.scene === 'quiz-answer'));
  if (mine.length) t += LEAD;
  for (const l of mine) {
    if (l.scene === 'quiz-answer') {
      lines.push({ id: 'countdown', start: t, dur: 5, text: '' });
      t += 5 + GAP;
    }
    const file = join(clipsDir, `${l.id}.mp3`);
    const dur = duration(file);
    lines.push({ id: l.id, start: t, dur, text: l.say, env: envelope(file) });
    audio.push({ file, at: t });
    t += dur + GAP;
  }
  t += HOLD[type] + (mine.length ? TAIL : 0);
  scenes.push({ type, chapter: CHAPTER[type] || '', start, end: t, lines });
}

const qrUrl = `https://www.campuschamp.in/learn/${E.course}/${E.lesson}?utm_source=youtube&utm_medium=video&utm_campaign=${E.course}-${E.lesson}-ep${E.episode}-${E.lang}`;
const timeline = {
  fps: FPS,
  duration: t,
  episode: E.episode,
  lessonNumber: E.lesson.replace('-', '.'),
  lang: E.lang,
  qr: await QRCode.toDataURL(qrUrl, { margin: 1, width: 600, color: { dark: '#1d1d1f', light: '#ffffff' } }),
  scenes,
  audio,
};
writeFileSync(outPath, JSON.stringify(timeline));
const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
console.log(`timeline ${fmt(t)} · ${scenes.length} scenes · ${audio.length} clips`);
scenes.forEach((s) => console.log(fmt(s.start), s.type));
