// Lesson 1.1 · Episode 3 "Your first program": the walkthrough program run line by line, then two errors
// made on purpose, the beginner mistakes, and the call to practise on Campus Champ.
window.addScenes(({ $, $$, clamp, ap, lerp, show, pop, S, E, bg, T }) => {
  const STR = {
    en: {
      minutes: '⏱ 4 minutes', breakIt: '🔨 Then we break it', comment: '# comment → Python skips it', print: 'print = show on the screen',
      string: '"text in quotes" = a string', newline: 'every print → a new line', commas: 'commas → a space between items', star: '* = multiply',
      done: '✓ 4 instructions, top to bottom', neverRuns: 'never runs', unclear: '℞ Like an unclear line on a prescription',
      nothing: '(nothing printed)', checking: '🔍 Checking the whole program…', syntaxDef: '<b>Syntax</b> = the grammar rules of a language',
      mistakesT: '3 beginner mistakes', m1: 'Capital P', m2: 'Curly quotes from WhatsApp', m3: 'No quotes around text',
      pointing: 'Errors point to exactly where to look 👉', task: 'Make a medicine label', correct: '✓ Correct!', free: '₹0 · Free',
      instant: '⚡ Instant check', next: 'Next: Lesson 1.2 →',
    },
    kn: {
      minutes: '⏱ 4 ನಿಮಿಷ', breakIt: '🔨 ಆಮೇಲೆ ಹಾಳು ಮಾಡೋಣ', comment: '# comment → Python skip ಮಾಡುತ್ತೆ', print: 'print = screen ಮೇಲೆ ತೋರಿಸು',
      string: '"quotes ಒಳಗಿನ text" = string', newline: 'ಪ್ರತಿ print → ಹೊಸ line', commas: 'commas → items ಮಧ್ಯೆ space', star: '* = multiply',
      done: '✓ 4 instructions, ಮೇಲಿಂದ ಕೆಳಗೆ', neverRuns: 'run ಆಗಲ್ಲ', unclear: '℞ Clear ಇಲ್ಲದ prescription line ತರಹ',
      nothing: '(ಏನೂ print ಆಗಿಲ್ಲ)', checking: '🔍 ಪೂರ್ತಿ program check…', syntaxDef: '<b>Syntax</b> = language ನ grammar rules',
      mistakesT: 'Beginners ಮಾಡೋ 3 ತಪ್ಪುಗಳು', m1: 'Capital P', m2: 'WhatsApp ನ curly quotes', m3: 'Text ಸುತ್ತ quotes ಇಲ್ಲ',
      pointing: 'ಎಲ್ಲಿ ನೋಡಬೇಕು ಅಂತ error ತೋರಿಸುತ್ತೆ 👉', task: 'ಒಂದು medicine label ಮಾಡಿ', correct: '✓ ಸರಿ!', free: '₹0 · Free',
      instant: '⚡ ತಕ್ಷಣ check', next: 'ಮುಂದೆ: Lesson 1.2 →',
    },
    hi: {
      minutes: '⏱ 4 मिनट', breakIt: '🔨 फिर इसे तोड़ेंगे', comment: '# comment → Python skip करता है', print: 'print = screen पर दिखाओ',
      string: '"quotes वाला text" = string', newline: 'हर print → नई line', commas: 'commas → items के बीच space', star: '* = multiply',
      done: '✓ 4 instructions, ऊपर से नीचे', neverRuns: 'run नहीं होती', unclear: '℞ Prescription की unclear line की तरह',
      nothing: '(कुछ भी print नहीं हुआ)', checking: '🔍 पूरा program check…', syntaxDef: '<b>Syntax</b> = language के grammar rules',
      mistakesT: 'Beginners की 3 गलतियाँ', m1: 'Capital P', m2: 'WhatsApp के curly quotes', m3: 'Text पर quotes नहीं',
      pointing: 'Error बताती है कि कहाँ देखना है 👉', task: 'एक medicine label बनाइए', correct: '✓ सही!', free: '₹0 · Free',
      instant: '⚡ तुरंत check', next: 'आगे: Lesson 1.2 →',
    },
  };
  const tx = (k) => (STR[T().lang] || STR.en)[k];
  const dur = (s, k) => (s.lines[k] || {}).dur || 1;
  // syntax colours
  const K = (x, cls = '') => `<span class="${cls}" style="color:#7dd3fc;border-radius:8px">${x}</span>`;
  const Q = (x, cls = '') => `<span class="${cls}" style="color:#86efac;border-radius:8px">${x}</span>`;
  const N = (x, cls = '') => `<span class="${cls}" style="color:#fdba74;border-radius:8px">${x}</span>`;
  const C = (x) => `<span style="color:#64748b;font-style:italic">${x}</span>`;
  const editor = (id, x, y, w, file, rows) => `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;opacity:0;border-radius:28px;background:#0b1023;border:1.5px solid #2b3466;box-shadow:0 30px 70px rgba(0,0,0,.5);overflow:hidden">
      <div style="display:flex;align-items:center;gap:10px;padding:16px 24px;background:#111633;border-bottom:1.5px solid #1e293b"><i style="width:14px;height:14px;border-radius:50%;background:#fb7185"></i><i style="width:14px;height:14px;border-radius:50%;background:#fbbf24"></i><i style="width:14px;height:14px;border-radius:50%;background:#34d399"></i><span style="margin-left:12px;color:#94a3b8;font-family:var(--mono);font-size:22px">${file}</span></div>
      <div style="padding:20px 0">${rows.map((r, i) => `<div class="row" data-i="${i}" style="position:relative;height:70px;display:flex;align-items:center;padding:0 30px;font-family:var(--mono);font-size:36px;color:#e2e8f0;white-space:pre"><span style="width:44px;color:#475569">${i + 1}</span>${r}<span class="tick" style="margin-left:auto;color:#34d399;opacity:0">✓</span></div>`).join('')}</div></div>`;
  const consoleBox = (id, x, y, w, h = 330) => `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;opacity:0;border-radius:28px;background:#020617;border:1.5px solid #1e293b;overflow:hidden">
      <div style="padding:16px 24px;background:#0f172a;color:#94a3b8;font-family:var(--head);font-weight:700;font-size:24px">Output</div>
      <div class="out" style="padding:22px 26px;font-family:var(--mono);font-size:32px;line-height:1.7;color:#e2e8f0;min-height:${h}px;white-space:pre-wrap"></div></div>`;
  const pointer = (id) => `<div id="${id}" class="abs" style="left:58px;top:0;opacity:0;width:52px;height:52px;border-radius:50%;background:#fde68a;color:#1f2937;display:grid;place-items:center;font-weight:800;font-size:24px;box-shadow:0 10px 30px rgba(0,0,0,.35)">▶</div>`;
  const rowY = (top, i) => top + 64 + 20 + i * 70 + 9; // editor top + header + padding + row
  const glow = (n, p, rgb = '253,230,138') => { if (!n) return; n.style.background = `rgba(${rgb},${0.25 * p})`; n.style.boxShadow = `0 0 0 ${6 * p}px rgba(${rgb},${0.25 * p})`; };
  const note = (id, x, y) => `<div id="${id}" class="abs tag" style="left:${x}px;top:${y}px;opacity:0;font-size:36px;font-family:var(--mono);background:rgba(253,230,138,.14);border-color:#fde68a;color:#fef3c7"></div>`;

  return {
    hook: {
      build: () => `
        ${bg(['#3b2a12', '#1f160a', '#0b0804'])}
        <div class="abs" style="left:610px;top:170px;width:700px;height:150px;border-radius:40px;background:linear-gradient(#475569,#1e293b);box-shadow:0 30px 60px rgba(0,0,0,.5)">
          <div style="position:absolute;left:60px;right:60px;bottom:26px;height:16px;border-radius:8px;background:#020617"></div>
          <div style="position:absolute;right:40px;top:34px;width:18px;height:18px;border-radius:50%;background:#34d399;box-shadow:0 0 18px #34d399"></div>
        </div>
        <div class="abs" style="left:680px;top:300px;width:560px;height:620px;overflow:hidden">
          <div id="paper" style="width:560px;padding:40px 44px;background:#fffdf7;border-radius:0 0 18px 18px;box-shadow:0 30px 50px rgba(0,0,0,.45);font-family:var(--mono);font-size:30px;line-height:1.9;color:#1f2937;transform:translateY(-620px)">
            ${['Welcome to Campus Champ!', 'Drug: Paracetamol', 'Strength: 500 mg', 'Daily dose: 1500 mg'].map((l) => `<div class="pl" style="opacity:0">${l}</div>`).join('')}
            <div style="margin-top:20px;border-top:3px dashed #cbd5e1;padding-top:16px;font-size:24px;color:#64748b">first_program.py</div>
          </div>
        </div>
        <div id="min" class="abs tag" style="left:150px;top:300px;opacity:0;font-size:44px;background:rgba(251,191,36,.18);border-color:#fbbf24;color:#fef3c7">${tx('minutes')}</div>
        <div id="brk" class="abs tag" style="left:1330px;top:560px;opacity:0;font-size:40px;background:rgba(251,113,133,.2);border-color:#fb7185;color:#ffe4e6">${tx('breakIt')}</div>`,
      update: (el, t, s) => {
        pop($('#min', el), ap(t, S(s, 0) + 0.6, 0.5));
        const pp = clamp((t - S(s, 1) + 0.2) / Math.max(1, dur(s, 1)));
        $('#paper', el).style.transform = `translateY(${-620 + pp * 620}px)`;
        $$('.pl', el).forEach((l, i) => (l.style.opacity = ap(t, S(s, 1) + (i * dur(s, 1)) / 4, 0.3)));
        const shake = t > S(s, 2) + dur(s, 2) * 0.4 ? Math.sin(t * 40) * 6 * (1 - ap(t, S(s, 2) + dur(s, 2) * 0.4, 0.6)) : 0;
        $('#paper', el).style.transform += ` translateX(${shake}px) rotate(${shake * 0.2}deg)`;
        pop($('#brk', el), ap(t, S(s, 2) + 0.4, 0.5));
      },
    },

    walk: {
      build: () => `
        ${bg(['#1e1b4b', '#12103a', '#06051a'])}
        ${pointer('ptr')}
        ${editor('ed', 120, 190, 1040, 'first_program.py', [
          C('# My first Python program'),
          `${K('print', 'pk')}(${Q('"Welcome to Campus Champ!"', 'st')})`,
          `${K('print')}(${Q('"Drug: Paracetamol"')})`,
          `${K('print')}(${Q('"Strength:"')}<b class="cma" style="color:#fde68a">,</b> ${N('500')}<b class="cma" style="color:#fde68a">,</b> ${Q('"mg"')})`,
          `${K('print')}(${Q('"Daily dose:"')}, ${N('500')} <b class="star" style="color:#f472b6;border-radius:8px">*</b> ${N('3')}, ${Q('"mg"')})`,
        ])}
        ${consoleBox('con', 1220, 190, 600)}
        <div id="calc" class="abs h" style="left:1000px;top:640px;opacity:0;padding:16px 26px;border-radius:20px;background:#f472b6;color:#fff;font-size:44px;box-shadow:0 20px 40px rgba(0,0,0,.4)">500 × 3 = 1500</div>
        ${note('note', 120, 780)}`,
      update: (el, t, s) => {
        show($('#ed', el), ap(t, s.start + 0.1, 0.6), 30, 0.96);
        show($('#con', el), ap(t, s.start + 0.4, 0.6), 30, 0.96);
        // which row Python is on, for each sentence
        const rowFor = [null, 0, 1, 1, 2, 3, 4, 4, null];
        let k = -1;
        for (let i = 0; i < 9; i++) if (t >= S(s, i)) k = i;
        let row = k >= 0 ? rowFor[k] : null;
        if (k === 0) row = Math.min(4, Math.floor(clamp((t - S(s, 0) - 1.5) / Math.max(1, dur(s, 0) - 1.5)) * 5));
        const ptr = $('#ptr', el);
        ptr.style.opacity = row === null || row < 0 ? 0 : 1;
        ptr.style.transform = `translateY(${rowY(190, Math.max(0, row || 0))}px)`;
        $$('#ed .row', el).forEach((r, i) => {
          const on = row === i && k > 0;
          r.style.background = on ? 'rgba(165,180,252,.14)' : 'transparent';
          r.style.opacity = i === 0 && k >= 1 ? 1 - 0.55 * ap(t, S(s, 1) + 1.2, 0.6) : 1;
          $('.tick', r).style.opacity = i > 0 ? ap(t, S(s, 8) + 0.3 + i * 0.2, 0.3) : 0;
        });
        glow($('.pk', el), ap(t, S(s, 2) + 0.3, 0.4) * (1 - ap(t, S(s, 3), 0.3)));
        glow($('.st', el), ap(t, S(s, 3) + 0.2, 0.4) * (1 - ap(t, S(s, 4), 0.3)));
        $$('.cma', el).forEach((c) => glow(c, ap(t, S(s, 5) + dur(s, 5) * 0.2, 0.4) * (1 - ap(t, S(s, 6), 0.3))));
        glow($('.star', el), ap(t, S(s, 6) + dur(s, 6) * 0.5, 0.4) * (1 - ap(t, S(s, 8), 0.3)), '244,114,182');
        pop($('#calc', el), ap(t, S(s, 7) + 0.3, 0.5) * (1 - ap(t, S(s, 8), 0.4)));
        // output appears as each print runs
        const outs = ['Welcome to Campus Champ!', 'Drug: Paracetamol', 'Strength: 500 mg', 'Daily dose: 1500 mg'];
        const when = [S(s, 2) + dur(s, 2) * 0.7, S(s, 4) + 0.6, S(s, 5) + dur(s, 5) * 0.65, S(s, 7) + dur(s, 7) * 0.7];
        $('#con .out', el).innerHTML = outs.filter((_, i) => t >= when[i]).map((o, i, a) => `<div style="color:${i === a.length - 1 ? '#fde68a' : '#e2e8f0'}">${o}</div>`).join('');
        const notes = [null, 'comment', 'print', 'string', 'newline', 'commas', 'star', 'star', 'done'];
        const n = $('#note', el);
        if (k >= 0 && notes[k]) {
          n.textContent = tx(notes[k]);
          show(n, ap(t, S(s, k) + 0.4, 0.4), 15, 0.95);
        } else n.style.opacity = 0;
      },
    },

    errors: {
      build: () => `
        ${bg(['#4c0519', '#2a0410', '#120207'])}
        ${pointer('ptr')}
        ${editor('ed', 120, 220, 1040, 'patient.py', [
          `${K('print')}(${Q('"Patient: Ravi"')})`,
          `${K('print')}(${Q('"Weight:"')}, <span class="w" style="color:#e2e8f0;border-radius:8px;text-decoration:underline wavy #fb7185 0px">weight</span>)`,
          `${K('print')}(${Q('"Dose calculated"')})`,
        ])}
        ${consoleBox('con', 1220, 220, 600, 250)}
        <div id="nr" class="abs tag" style="left:860px;top:${rowY(220, 2) - 4}px;opacity:0;font-size:28px;padding:8px 18px;background:rgba(148,163,184,.15);border-color:#64748b;color:#cbd5e1">${tx('neverRuns')}</div>
        <div id="rx" class="abs tag" style="left:120px;top:640px;opacity:0;font-size:38px;background:rgba(255,250,240,.12);border-color:#fde68a;color:#fef3c7">${tx('unclear')}</div>`,
      update: (el, t, s) => {
        show($('#ed', el), ap(t, s.start + 0.1, 0.6), 30, 0.96);
        show($('#con', el), ap(t, s.start + 0.4, 0.6), 30, 0.96);
        const w = $('.w', el);
        const wp = ap(t, S(s, 1) + dur(s, 1) * 0.6, 0.4);
        glow(w, wp, '251,113,133');
        w.style.textDecorationThickness = `${4 * wp}px`;
        // run: line 1, then stop at line 2
        let row = null;
        if (t >= S(s, 2)) row = t < S(s, 2) + dur(s, 2) * 0.45 ? 0 : 1;
        const ptr = $('#ptr', el);
        ptr.style.opacity = row === null ? 0 : 1;
        ptr.style.transform = `translateY(${rowY(220, row || 0)}px)`;
        ptr.style.background = row === 1 ? '#fb7185' : '#fde68a';
        $$('#ed .row', el).forEach((r, i) => {
          r.style.background = row === i ? (i === 1 ? 'rgba(251,113,133,.18)' : 'rgba(165,180,252,.14)') : 'transparent';
          r.style.opacity = i === 2 && t >= S(s, 3) ? 1 - 0.6 * ap(t, S(s, 3) + dur(s, 3) * 0.6, 0.5) : 1;
        });
        let out = '';
        if (t >= S(s, 2) + dur(s, 2) * 0.3) out += '<div>Patient: Ravi</div>';
        if (t >= S(s, 3)) out += `<div style="color:#fb7185;opacity:${ap(t, S(s, 3), 0.4)}">NameError: name 'weight' is not defined</div>`;
        $('#con .out', el).innerHTML = out;
        pop($('#nr', el), ap(t, S(s, 3) + dur(s, 3) * 0.6, 0.5));
        show($('#rx', el), ap(t, S(s, 4) + 0.3, 0.5), 20, 0.92);
      },
    },

    syntax: {
      build: () => `
        ${bg(['#172554', '#0f1a3d', '#060b1c'])}
        ${editor('ed', 120, 220, 1040, 'lines.py', [
          `${K('print')}(${Q('"Line 1"')})`,
          `${K('print')}(${Q('"Line 2"')}<span id="gap" style="display:inline-block;width:30px;height:46px;margin-left:4px;border:3px dashed #fb7185;border-radius:8px;vertical-align:middle"></span>`,
          `${K('print')}(${Q('"Line 3"')})`,
        ])}
        <div id="scan" class="abs" style="left:120px;top:0;width:1040px;height:70px;opacity:0;background:linear-gradient(90deg,rgba(94,234,212,0),rgba(94,234,212,.28),rgba(94,234,212,0));border-top:2px solid #5eead4;border-bottom:2px solid #5eead4"></div>
        ${consoleBox('con', 1220, 220, 600, 250)}
        <div id="chk" class="abs tag" style="left:120px;top:620px;opacity:0;font-size:34px">${tx('checking')}</div>
        <div id="def" class="abs" style="left:120px;top:720px;opacity:0;padding:24px 34px;border-radius:24px;background:#fffaf0;color:#1d1d1f;font-size:40px;box-shadow:0 20px 50px rgba(0,0,0,.4)">${tx('syntaxDef')}</div>`,
      update: (el, t, s) => {
        show($('#ed', el), ap(t, s.start + 0.1, 0.6), 30, 0.96);
        show($('#con', el), ap(t, s.start + 0.4, 0.6), 30, 0.96);
        const g = $('#gap', el);
        g.style.opacity = ap(t, S(s, 0) + dur(s, 0) * 0.5, 0.4) * (0.6 + 0.4 * Math.sin(t * 6));
        $$('#ed .row', el).forEach((r, i) => (r.style.background = i === 1 && t >= S(s, 0) + dur(s, 0) * 0.5 ? 'rgba(251,113,133,.14)' : 'transparent'));
        let out = '';
        if (t >= S(s, 1) && t < S(s, 3)) out = `<div style="color:#64748b;opacity:${ap(t, S(s, 1) + 0.3, 0.4)}">${tx('nothing')}</div>`;
        if (t >= S(s, 3)) out = `<div style="color:#fb7185;opacity:${ap(t, S(s, 3), 0.4)}">SyntaxError: '(' was never closed</div>`;
        $('#con .out', el).innerHTML = out;
        // Python reads the whole file before running: a scan bar sweeps every line
        const sc = $('#scan', el);
        const on = t >= S(s, 2) && t < S(s, 3) + 0.3;
        sc.style.opacity = on ? 1 : 0;
        const ph = ((t - S(s, 2)) % 1.6) / 1.6;
        sc.style.transform = `translateY(${rowY(220, 0) - 9 + ph * 3 * 70}px)`;
        show($('#chk', el), ap(t, S(s, 2) + 0.2, 0.4) * (1 - ap(t, S(s, 3), 0.4)), 15, 0.95);
        show($('#def', el), ap(t, S(s, 3) + dur(s, 3) * 0.45, 0.6), 20, 0.95);
      },
    },

    mistakes: {
      build: () => {
        const card = (i, x, title, bad, good) => `<div class="abs mk" data-i="${i}" style="left:${x}px;top:280px;width:540px;opacity:0;border-radius:34px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.16);padding:34px 34px">
            <p style="font-family:var(--head);font-weight:800;font-size:34px;color:#fff">${i + 1}. ${title}</p>
            <div style="margin-top:26px;padding:20px 22px;border-radius:18px;background:rgba(251,113,133,.14);border:2px solid #fb7185;font-family:var(--mono);font-size:32px;color:#ffe4e6;display:flex;justify-content:space-between"><span>${bad}</span><b style="color:#fb7185">✕</b></div>
            <div class="ok" style="margin-top:18px;opacity:0;padding:20px 22px;border-radius:18px;background:rgba(52,211,153,.14);border:2px solid #34d399;font-family:var(--mono);font-size:32px;color:#d1fae5;display:flex;justify-content:space-between"><span>${good}</span><b style="color:#34d399">✓</b></div></div>`;
        return `
          ${bg(['#422006', '#2a1505', '#120902'])}
          <p id="mt" class="abs h" style="left:0;right:0;top:140px;text-align:center;font-size:64px;color:#fff;opacity:0">${tx('mistakesT')}</p>
          ${card(0, 120, tx('m1'), '<b style="color:#fb7185">P</b>rint("Hi")', 'print("Hi")')}
          ${card(1, 690, tx('m2'), 'print(<b style="color:#fb7185">“</b>Hi<b style="color:#fb7185">”</b>)', 'print("Hi")')}
          ${card(2, 1260, tx('m3'), 'print(Paracetamol)', 'print("Paracetamol")')}
          <div id="pt" class="abs" style="left:0;right:0;margin:0 auto;top:740px;width:max-content;opacity:0;padding:26px 48px;border-radius:999px;background:#fffaf0;color:#1d1d1f;font-family:var(--head);font-weight:800;font-size:46px;box-shadow:0 30px 70px rgba(0,0,0,.5)">${tx('pointing')}</div>`;
      },
      update: (el, t, s) => {
        show($('#mt', el), ap(t, S(s, 0), 0.6), 20, 1);
        $$('.mk', el).forEach((c, i) => {
          show(c, ap(t, S(s, i + 1), 0.6), 40, 0.92);
          const on = t >= S(s, i + 1) && t < S(s, i + 2);
          c.style.borderColor = on ? '#fde68a' : 'rgba(255,255,255,.16)';
          $('.ok', c).style.opacity = ap(t, S(s, i + 1) + dur(s, i + 1) * 0.6, 0.4);
        });
        pop($('#pt', el), ap(t, S(s, 4) + 0.3, 0.6));
      },
    },

    cta: {
      build: () => `
        ${bg(['#134e4a', '#0b2e2c', '#041716'])}
        <div id="phone" class="abs" style="left:240px;top:150px;width:470px;height:840px;opacity:0;border-radius:64px;background:#f8fafc;border:14px solid #0f172a;box-shadow:0 40px 90px rgba(0,0,0,.55);padding:56px 30px;overflow:hidden">
          <p style="font-family:var(--head);font-weight:700;font-size:22px;color:#4f46e5">BP101T · Lesson 1.1 · Task 2</p>
          <p class="h" style="margin-top:6px;font-size:34px;color:#0f172a;line-height:1.15">${tx('task')}</p>
          <div style="margin-top:20px;border-radius:18px;background:#0b1023;padding:18px;font-family:var(--mono);font-size:19px;line-height:1.7;color:#e2e8f0;min-height:250px"><span id="ty"></span><span style="color:#a5b4fc">|</span></div>
          <div style="margin-top:18px;display:flex;justify-content:center"><span style="padding:14px 38px;border-radius:999px;background:#4f46e5;color:#fff;font-family:var(--head);font-weight:800;font-size:22px">▶ Run</span></div>
          <div id="ok" style="margin-top:20px;opacity:0;padding:18px;border-radius:18px;background:#d1fae5;color:#065f46;font-family:var(--head);font-weight:800;font-size:30px;text-align:center">${tx('correct')}</div>
        </div>
        <div id="t1" class="abs tag" style="left:860px;top:330px;opacity:0;font-size:44px;background:rgba(45,212,191,.16);border-color:#2dd4bf;color:#ccfbf1">${tx('instant')}</div>
        <div id="t2" class="abs tag" style="left:860px;top:450px;opacity:0;font-size:44px;background:rgba(253,230,138,.16);border-color:#fde68a;color:#fef3c7">${tx('free')}</div>
        <div id="t3" class="abs h" style="left:860px;top:180px;opacity:0;font-size:60px;color:#fff">campuschamp.in</div>
        <div id="nx" class="abs" style="left:860px;top:600px;opacity:0;padding:30px 40px;border-radius:30px;background:#fffaf0;box-shadow:0 30px 70px rgba(0,0,0,.45)">
          <p style="font-family:var(--head);font-weight:700;font-size:30px;color:#6e6e73">${tx('next')}</p>
          <p class="h" style="margin-top:8px;font-size:56px;color:#1d1d1f">${T().next ? T().next.title : ''}</p>
        </div>`,
      update: (el, t, s) => {
        show($('#phone', el), ap(t, S(s, 0) + 0.2, 0.7), 40, 0.94);
        show($('#t3', el), ap(t, S(s, 0) + dur(s, 0) * 0.5, 0.5), 20, 0.95);
        const code = '# Prescription label\nprint("== CAMPUS CHAMP ==")\nprint("Drug : Amoxicillin")\nprint("Strength:", 250, "mg")\nprint("Daily:", 250 * 4, "mg")';
        $('#ty', el).innerHTML = code.slice(0, Math.floor(clamp((t - S(s, 1)) / Math.max(1, dur(s, 1) * 0.9)) * code.length)).replace(/\n/g, '<br>');
        pop($('#ok', el), ap(t, S(s, 2) + 0.2, 0.5));
        show($('#t1', el), ap(t, S(s, 2) + 0.4, 0.5), 20, 0.9);
        show($('#t2', el), ap(t, S(s, 2) + dur(s, 2) * 0.6, 0.5), 20, 0.9);
        show($('#nx', el), ap(t, S(s, 3) + 0.3, 0.6), 30, 0.95);
      },
    },
  };
});
