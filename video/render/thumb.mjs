// Renders the YouTube thumbnail (1280×720). Usage: node thumb.mjs <out.png>
import { createRequire } from 'node:module';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const { chromium } = createRequire(import.meta.url)('playwright');
const HERE = dirname(fileURLToPath(import.meta.url));
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
await p.goto(pathToFileURL(join(HERE, 'thumbnail.html')).href);
await p.evaluate(() => window.setupThumb({ tag: 'BP101T · Lesson 1.1', title: 'Python <em>ಅಂದ್ರೆ</em> ಏನು?', sub: 'ನಿಮ್ಮ ಮೊದಲ program, 10 ನಿಮಿಷದಲ್ಲಿ', lang: ['ಕನ್ನಡ', 'B.Pharm Sem I'] }));
await p.evaluate(async () => { await document.fonts.load('800 100px "Plus Jakarta Sans"', 'ಅ'); await document.fonts.load('800 100px "Noto Sans Kannada"', 'ಕ'); await document.fonts.ready; });
await p.screenshot({ path: process.argv[2] });
await b.close();
