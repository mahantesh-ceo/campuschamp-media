// Builds the video timeline for one lesson + language: scenes, who speaks when, subtitles,
// mouth movement (loudness per frame) and the audio placements for the final mix.
// Usage: node build_timeline.mjs <script.json> <newClipsDir> <out.json>
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
const QRCode = createRequire('/home/user/test/package.json')('qrcode');

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
const FPS = 25;
const GAP = 0.4; // pause between two lines
const LEAD = 0.6; // pause when a scene starts
const TAIL = 0.6; // pause before the next scene

const [scriptPath, newDir, outPath] = process.argv.slice(2);
const S = JSON.parse(readFileSync(scriptPath, 'utf8'));
const { course, lesson, lang } = S;
const content = JSON.parse(readFileSync(join(ROOT, 'content', course, lesson, `${lang}.json`), 'utf8'));
const en = JSON.parse(readFileSync(join(ROOT, 'content', course, lesson, 'en.json'), 'utf8'));
const lessonAudio = join(ROOT, 'audio', course, lesson, lang);

const duration = (f) => Number(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).toString().trim());

// Loudness per video frame, 0..1, used to open the speaking character's mouth
function envelope(f) {
  const raw = execFileSync('ffmpeg', ['-loglevel', 'error', '-i', f, '-ac', '1', '-ar', '8000', '-f', 's16le', '-'], { maxBuffer: 1 << 26 });
  const samples = new Int16Array(raw.buffer, raw.byteOffset, raw.length / 2);
  const per = 8000 / FPS;
  const out = [];
  for (let i = 0; i < samples.length; i += per) {
    let s = 0;
    const end = Math.min(samples.length, i + per);
    for (let j = i; j < end; j++) s += samples[j] * samples[j];
    out.push(Math.sqrt(s / Math.max(1, end - i)) / 32768);
  }
  const peak = Math.max(0.0001, ...out.slice().sort((a, b) => a - b).slice(Math.floor(out.length * 0.95)));
  return out.map((v) => Math.round(Math.min(1, v / peak) * 100) / 100);
}

// A line is either new narration (S.lines) or an existing lesson clip (walkthrough / animation)
const walk = content.walkthrough.steps;
const anim = content.animations[0].steps;
function clip(ref) {
  if (S.lines[ref]) {
    const L = S.lines[ref];
    return { id: ref, who: L.who, text: L.say, file: join(newDir, `${ref}.mp3`) };
  }
  const [kind, n] = ref.split(':');
  const i = Number(n) - 1;
  if (kind === 'step') return { id: ref, who: 'anu', text: walk[i].say, file: join(lessonAudio, en.walkthrough.steps[i].audio) };
  if (kind === 'anim') return { id: ref, who: 'anu', text: anim[i].say, file: join(lessonAudio, en.animations[0].steps[i].audio) };
  throw new Error(`unknown line ${ref}`);
}

const glossary = (term) => {
  const i = en.glossary.findIndex((g) => g.term === term);
  return { term, meaning: content.glossary[i]?.meaning || en.glossary[i].meaning };
};
const strip = (md) => md.replace(/\*\*/g, '').replace(/`/g, '');

// The plan for this lesson: scene type, its lines, and silent holds (seconds)
const PLAN = [
  { type: 'intro', chapter: 'Intro', hold: 3.6 },
  { type: 'hook', chapter: 'ಯಾಕೆ Python?', lines: ['c-hook', 'a-hook'], data: { title: content.hook.title } },
  { type: 'prescription', chapter: 'Program ಅಂದ್ರೆ ಏನು', lines: ['c-what', 'anim:1', 'anim:2', 'anim:3', 'anim:4', 'anim:5', 'anim:6', 'anim:7'], data: { title: 'Program ಅಂದ್ರೆ ಏನು?', actors: en.animations[0].actors, steps: en.animations[0].steps.map((s) => s.actions) } },
  { type: 'why', chapter: 'Python ಯಾಕೆ', lines: ['a-why'] },
  { type: 'terms', chapter: 'Key words', lines: ['a-terms'], hold: 4 * 4.2, data: { cards: ['Program', 'Interpreter', 'print()', 'Comment'].map(glossary) } },
  { type: 'code', chapter: 'ಮೊದಲ program', lines: ['c-code', 'step:1', 'step:2', 'step:3', 'step:4', 'step:5', 'step:6', 'step:7'], data: { code: en.walkthrough.code, filename: en.walkthrough.filename, steps: en.walkthrough.steps.map((s) => ({ line: s.line, output: s.output })) } },
  { type: 'mistake', chapter: 'ಸಾಮಾನ್ಯ ತಪ್ಪು', lines: ['c-mistake', 'a-mistake'], hold: 1.2 },
  { type: 'quiz', chapter: 'Quiz', lines: ['a-quiz', '@countdown', 'a-quiz-answer'], hold: 1.2, data: { q: content.quiz[1].q, options: content.quiz[1].options, answer: en.quiz[1].answer } },
  { type: 'exam', chapter: 'Exam corner', lines: ['c-exam', 'a-exam'], hold: 2.5, data: { q: en.exam.short[1].q, marks: en.exam.short[1].marks, answer: strip(en.exam.short[1].md), note: 'Practice question. University questions may differ.' } },
  { type: 'summary', chapter: 'Summary', lines: ['a-summary'], hold: 2.5, data: { points: [0, 2, 3].map((i) => strip(content.summary[i])) } },
  { type: 'end', chapter: 'Practise free', lines: ['c-end'], hold: 6, data: { url: `campuschamp.in/learn/${course}/${lesson}`, qr: `https://www.campuschamp.in/learn/${course}/${lesson}?utm_source=youtube&utm_medium=video&utm_campaign=${course}-${lesson}-${lang}` } },
];

let t = 0;
const scenes = [];
const audio = [];
for (const p of PLAN) {
  const start = t;
  const lines = [];
  t += p.type === 'intro' ? 0 : LEAD;
  for (const ref of p.lines || []) {
    if (ref === '@countdown') {
      lines.push({ id: 'countdown', who: null, start: t, dur: 5, text: '' });
      t += 5 + GAP;
      continue;
    }
    const c = clip(ref);
    const dur = duration(c.file);
    lines.push({ id: c.id, who: c.who, start: t, dur, text: c.text, env: envelope(c.file) });
    audio.push({ file: c.file, at: t });
    t += dur + GAP;
  }
  t += (p.hold || 0) + (p.type === 'intro' ? 0 : TAIL);
  scenes.push({ type: p.type, chapter: p.chapter, start, end: t, lines, data: p.data || {} });
}

const end = scenes.find((s) => s.type === 'end');
end.data.qrImage = await QRCode.toDataURL(end.data.qr, { margin: 1, width: 600, color: { dark: '#0f172a', light: '#ffffff' } });
const timeline = { fps: FPS, duration: t, title: S.title, lesson: en.number, lessonTitle: en.title, lang, scenes, audio };
writeFileSync(outPath, JSON.stringify(timeline));
const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
console.log(`timeline ${fmt(t)} · ${scenes.length} scenes · ${audio.length} clips`);
scenes.forEach((s) => console.log(fmt(s.start), s.chapter));
