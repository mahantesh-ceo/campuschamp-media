// Screenshots the style frames. Usage: node shoot.mjs <outDir>
import { createRequire } from 'node:module';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const req = createRequire(import.meta.url);
const { chromium } = req('playwright');
const QR = createRequire('/home/user/test/package.json')('qrcode');
const HERE = dirname(fileURLToPath(import.meta.url));
const out = process.argv[2];
const qr = await QR.toDataURL('https://www.campuschamp.in/learn/bp101t/1-1?utm_source=youtube', { margin: 1, width: 600, color: { dark: '#1d1d1f', light: '#ffffff' } });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
p.on('pageerror', (e) => console.error(e.message));
await p.goto(pathToFileURL(join(HERE, 'frames.html')).href);
await p.evaluate(async () => { for (const f of ['800 80px "Plus Jakarta Sans"', '700 40px "Noto Sans Kannada"', '500 40px Inter', '400 30px "JetBrains Mono"']) await document.fonts.load(f, 'ಕAa'); await document.fonts.ready; });
for (const id of ['cold', 'sting', 'rx', 'chip', 'program', 'end']) {
  await p.evaluate(([i, q]) => window.show(i, q), [id, qr]);
  await p.screenshot({ path: join(out, `${id}.png`) });
}
await b.close();
console.log('ok');
