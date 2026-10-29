// Renders a lesson video from a timeline: draws every frame in Chromium, mixes the narration,
// and encodes a 1080p MP4. Usage:
//   node render.mjs <timeline.json> <out.mp4>                 full video
//   node render.mjs <timeline.json> <outDir> --stills 3,40,95  PNG frames at those seconds
import { spawn, execFileSync } from 'node:child_process';
import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const HERE = dirname(fileURLToPath(import.meta.url));
const [timelinePath, out, flag, list] = process.argv.slice(2);
const T = JSON.parse(readFileSync(timelinePath, 'utf8'));

async function openPage() {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', (e) => console.error('page error:', e.message));
  await page.goto(pathToFileURL(join(HERE, 'index.html')).href);
  await page.evaluate((t) => window.setupVideo(t), T);
  // load every font face that appears in the video before the first frame
  await page.evaluate(async () => {
    window.renderAt(0);
    await document.fonts.load('700 40px "Noto Sans Kannada"', 'ಕನ್ನಡ');
    await document.fonts.load('800 40px "Plus Jakarta Sans"', 'Aa');
    await document.fonts.load('400 40px "JetBrains Mono"', 'Aa');
    await document.fonts.load('500 40px "Inter"', 'Aa');
    await document.fonts.ready;
  });
  return { browser, page };
}

if (flag === '--stills') {
  mkdirSync(out, { recursive: true });
  const { browser, page } = await openPage();
  for (const s of list.split(',').map(Number)) {
    await page.evaluate((t) => window.renderAt(t), s);
    await page.screenshot({ path: join(out, `still-${String(s).padStart(4, '0')}.png`) });
  }
  await browser.close();
  console.log('stills done');
} else {
  // 1) narration mix
  const audioPath = out.replace(/\.mp4$/, '.m4a');
  const inputs = T.audio.flatMap((a) => ['-i', a.file]);
  const delays = T.audio.map((a, i) => `[${i}]adelay=${Math.round(a.at * 1000)}|${Math.round(a.at * 1000)}[a${i}]`).join(';');
  const mix = `${delays};${T.audio.map((_, i) => `[a${i}]`).join('')}amix=inputs=${T.audio.length}:normalize=0,apad=whole_dur=${T.duration.toFixed(2)},atrim=0:${T.duration.toFixed(2)}[mix]`;
  execFileSync('ffmpeg', ['-loglevel', 'error', '-y', ...inputs, '-filter_complex', mix, '-map', '[mix]', '-ac', '2', '-ar', '44100', '-c:a', 'aac', '-b:a', '160k', audioPath]);
  // soft original music bed, ducked under the voices
  const bed = out.replace(/\.mp4$/, '.bed.wav');
  const voices = out.replace(/\.mp4$/, '.voices.m4a');
  execFileSync('python3', [join(HERE, 'music', 'make_bed.py'), String(Math.ceil(T.duration)), bed]);
  execFileSync('mv', [audioPath, voices]);
  execFileSync('ffmpeg', ['-loglevel', 'error', '-y', '-i', voices, '-i', bed, '-filter_complex',
    '[1:a]volume=0.2[m];[m][0:a]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[duck];[0:a][duck]amix=inputs=2:normalize=0[out]',
    '-map', '[out]', '-c:a', 'aac', '-b:a', '160k', audioPath]);
  console.log('audio mixed');

  // 2) frames → ffmpeg
  const frames = Math.ceil(T.duration * T.fps);
  const ff = spawn('ffmpeg', ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(T.fps), '-i', '-', '-i', audioPath,
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const { browser, page } = await openPage();
  const t0 = Date.now();
  for (let f = 0; f < frames; f++) {
    await page.evaluate((t) => window.renderAt(t), f / T.fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
    if (f % 250 === 0) console.log(`frame ${f}/${frames} · ${Math.round((Date.now() - t0) / 1000)}s`);
  }
  ff.stdin.end();
  await new Promise((r) => ff.on('close', r));
  await browser.close();

  // 3) YouTube chapters
  const fmt = (s) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
  writeFileSync(out.replace(/\.mp4$/, '.chapters.txt'), T.scenes.map((s) => s.chapter ? `${fmt(s.start)} ${s.chapter}` : '').filter(Boolean).join('\n') + '\n');
  console.log('video done', out);
}
