// Lesson 1.1 · Episode 2 "Why Python?": its own illustrated scenes, added to the shared renderer.
// The sting, quiz, recap and end card come from scenes.js and read their words from the episode plan.
window.addScenes(({ $, $$, clamp, ap, lerp, show, pop, S, E, prescription, chipSvg, chipFace, bg, T }) => {
  const STR = {
    en: {
      namaste: 'Namaste!', count: 'Count the tablets', show500: 'Show 500', impossible: '😵 Impossible to write',
      common: 'A common language', human: 'People', plTitle: 'Programming language', plSub: 'People can write it. Computers understand it.',
      many: 'Many programming languages', syllabus: 'In your syllabus', creator: 'Created by', first: 'First released',
      named: 'Named after a comedy show 🎭', notSnake: 'not the snake 🐍', whyQ: 'Why Python for pharmacy?', reason: 'Reason',
      r1: 'Reads like English', lines5: '5 lines', lines1: '1 line', fewer: '✓ Fewer mistakes',
      free: 'Free', freeSub: 'Download it, use it. No fees.', libs: 'Ready-made libraries', libsSub: 'Like ready-made tablets 💊',
      libCalc: 'Calculations', libData: 'Data tables', libGraph: 'Graphs', pharma: 'Used in pharmacy', pharmaSub: 'Every single day',
      p1: 'Clinical trial data', p2: 'Drug concentration over time', p3: 'Adverse drug reaction reports', p4: 'Designing new drugs',
      skill: 'Python is a <span style="color:#fde68a">pharmacy skill</span> 💊', patients: 'patients', time: 'time', conc: 'concentration',
      signal: '⚠ Pattern spotted early', reads: 'Read line by line', interp: 'Interpreter', output: 'Output', turn: 'Your turn',
      friend: 'Errors are your friend 🤝',
    },
    kn: {
      namaste: 'ನಮಸ್ಕಾರ!', count: 'Tablets count ಮಾಡು', show500: '500 ತೋರಿಸು', impossible: '😵 ಹೀಗೆ ಬರೆಯೋಕೆ ಸಾಧ್ಯನೇ ಇಲ್ಲ',
      common: 'ಒಂದು common ಭಾಷೆ', human: 'ಮನುಷ್ಯರು', plTitle: 'Programming language', plSub: 'ಮನುಷ್ಯರು ಬರೆಯಬಹುದು. Computer ಗೆ ಅರ್ಥ ಆಗುತ್ತೆ.',
      many: 'ತುಂಬಾ programming languages', syllabus: 'ನಿಮ್ಮ syllabus ನಲ್ಲಿ', creator: 'ಮಾಡಿದ್ದು', first: 'ಮೊದಲ release',
      named: 'ಒಂದು comedy show ಹೆಸರು 🎭', notSnake: 'ಹಾವಿನ ಹೆಸರಲ್ಲ 🐍', whyQ: 'Pharmacy ಗೆ Python ಯಾಕೆ?', reason: 'ಕಾರಣ',
      r1: 'English ತರಹ ಓದಬಹುದು', lines5: '5 lines', lines1: '1 line', fewer: '✓ ಕಡಿಮೆ ತಪ್ಪುಗಳು',
      free: 'Free', freeSub: 'Download ಮಾಡಿ, use ಮಾಡಿ. Fees ಇಲ್ಲ.', libs: 'Ready-made libraries', libsSub: 'Ready-made tablets ತರಹ 💊',
      libCalc: 'Calculations', libData: 'Data tables', libGraph: 'Graphs', pharma: 'Pharmacy ಯಲ್ಲಿ use', pharmaSub: 'ಪ್ರತಿದಿನ',
      p1: 'Clinical trial data', p2: 'Drug concentration, time ಜೊತೆ', p3: 'Adverse drug reaction reports', p4: 'ಹೊಸ drugs design',
      skill: 'Python ಒಂದು <span style="color:#fde68a">pharmacy skill</span> 💊', patients: 'patients', time: 'time', conc: 'concentration',
      signal: '⚠ Pattern ಬೇಗ ಸಿಕ್ತು', reads: 'ಒಂದೊಂದೇ line ಓದ್ತಾರೆ', interp: 'Interpreter', output: 'Output', turn: 'ನಿಮ್ಮ turn',
      friend: 'Error ನಿಮ್ಮ friend 🤝',
    },
    hi: {
      namaste: 'नमस्ते!', count: 'Tablets count करो', show500: '500 दिखाओ', impossible: '😵 ऐसे लिखना नामुमकिन',
      common: 'एक common भाषा', human: 'इंसान', plTitle: 'Programming language', plSub: 'इंसान लिख सकें. Computer समझ सके.',
      many: 'बहुत सारी programming languages', syllabus: 'आपके syllabus में', creator: 'बनाई', first: 'पहली release',
      named: 'एक comedy show पर नाम 🎭', notSnake: 'साँप पर नहीं 🐍', whyQ: 'Pharmacy के लिए Python क्यों?', reason: 'कारण',
      r1: 'English जैसी आसान', lines5: '5 lines', lines1: '1 line', fewer: '✓ कम गलतियाँ',
      free: 'Free', freeSub: 'Download करो, use करो. कोई fee नहीं.', libs: 'Ready-made libraries', libsSub: 'Ready-made tablets की तरह 💊',
      libCalc: 'Calculations', libData: 'Data tables', libGraph: 'Graphs', pharma: 'Pharmacy में use', pharmaSub: 'हर दिन',
      p1: 'Clinical trial data', p2: 'समय के साथ drug concentration', p3: 'Adverse drug reaction reports', p4: 'नई drugs का design',
      skill: 'Python एक <span style="color:#fde68a">pharmacy skill</span> है 💊', patients: 'patients', time: 'time', conc: 'concentration',
      signal: '⚠ Pattern जल्दी पकड़ा', reads: 'एक-एक line पढ़ते हैं', interp: 'Interpreter', output: 'Output', turn: 'आपकी बारी',
      friend: 'Error आपकी दोस्त है 🤝',
    },
  };
  const tx = (k) => (STR[T().lang] || STR.en)[k];
  const rnd = (i) => { const x = Math.sin(i * 12.9898) * 43758.5453; return x - Math.floor(x); };
  const dur = (s, k) => (s.lines[k] || {}).dur || 1;
  const bubble = (cls, x, y, text, tail = 'left') => `<div class="abs ${cls}" style="left:${x}px;top:${y}px;opacity:0;background:#fff;color:#0f172a;border-radius:${tail === 'left' ? '28px 28px 28px 6px' : '28px 28px 6px 28px'};padding:22px 32px;font-size:42px;font-weight:700;white-space:nowrap;box-shadow:0 20px 40px rgba(0,0,0,.35)">${text}</div>`;
  const win = (id, x, y, w, title, body) => `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;opacity:0;border-radius:28px;background:#0b1023;border:1.5px solid #2b3466;box-shadow:0 30px 70px rgba(0,0,0,.5);overflow:hidden">
      <div style="display:flex;align-items:center;gap:10px;padding:16px 24px;background:#111633;border-bottom:1.5px solid #1e293b"><i style="width:14px;height:14px;border-radius:50%;background:#fb7185"></i><i style="width:14px;height:14px;border-radius:50%;background:#fbbf24"></i><i style="width:14px;height:14px;border-radius:50%;background:#34d399"></i><span style="margin-left:12px;color:#94a3b8;font-family:var(--mono);font-size:22px">${title}</span></div>
      <div style="padding:30px 32px;font-family:var(--mono);font-size:34px;line-height:1.7;color:#e2e8f0;white-space:pre">${body}</div></div>`;
  const py = (s) => `<span style="color:#7dd3fc">print</span>(<span style="color:#86efac">"${s}"</span>)`;

  return {
    binary: {
      build: () => {
        let rain = '';
        for (let i = 0; i < 26; i++) {
          const col = Array.from({ length: 40 }, (_, j) => (rnd(i * 97 + j) > 0.5 ? '1' : '0')).join('<br>');
          rain += `<div class="rc" data-s="${40 + rnd(i) * 70}" data-o="${rnd(i + 7) * 1400}" style="position:absolute;left:${i * 75 + 10}px;top:-1400px;font-family:var(--mono);font-size:30px;line-height:1.2;color:#2dd4bf;opacity:${0.15 + rnd(i + 3) * 0.3}">${col}</div>`;
        }
        const bin = '00110101 00110000 00110000';
        return `
          ${bg(['#1e1b4b', '#0f0c2e', '#05040f'])}
          <div id="rain" class="abs" style="inset:0;opacity:0;overflow:hidden">${rain}</div>
          <div id="chip" class="abs" style="left:1180px;top:300px;opacity:0">${chipSvg('x')}</div>
          ${bubble('b0', 170, 250, 'Hello! 👋')}${bubble('b1', 300, 420, tx('namaste') + ' 🙏')}${bubble('b2', 170, 590, tx('count'))}
          <div id="qm" class="abs h" style="left:1340px;top:200px;width:96px;height:96px;border-radius:50%;background:#fb7185;color:#fff;font-size:60px;display:grid;place-items:center;opacity:0">?</div>
          <div id="bits" class="abs" style="left:0;right:0;top:330px;display:flex;justify-content:center;gap:60px">
            ${['0', '1'].map((b) => `<div class="bit h" style="opacity:0;width:260px;height:260px;border-radius:48px;background:rgba(45,212,191,.14);border:3px solid #2dd4bf;color:#fff;font-family:var(--mono);font-size:180px;display:grid;place-items:center;box-shadow:0 0 80px rgba(45,212,191,.35)">${b}</div>`).join('')}
          </div>
          <div id="conv" class="abs" style="left:0;right:0;top:380px;display:flex;align-items:center;justify-content:center;gap:50px;opacity:0">
            <div style="background:#fde68a;color:#1f2937;border-radius:16px;padding:30px 40px;font-size:56px;font-weight:800;transform:rotate(-3deg);box-shadow:0 24px 50px rgba(0,0,0,.4)">${tx('show500')}</div>
            <div class="h" style="font-size:80px;color:#a5b4fc">→</div>
            <div style="min-width:900px;padding:34px 40px;border-radius:24px;background:#0b1023;border:2px solid #2dd4bf;font-family:var(--mono);font-size:56px;color:#5eead4;letter-spacing:.04em"><span id="typed" data-full="${bin}"></span><span style="color:#a5b4fc">|</span></div>
          </div>
          <div id="paper" class="abs" style="left:560px;top:1080px;width:800px;border-radius:28px;background:#fffaf0;padding:40px 48px;box-shadow:0 30px 70px rgba(0,0,0,.5)">
            <div class="h" style="font-size:64px;color:#4f46e5">℞</div>
            ${Array.from({ length: 12 }, (_, r) => `<div style="font-family:var(--mono);font-size:30px;line-height:1.6;color:#475569">${Array.from({ length: 4 }, (_, k) => Array.from({ length: 8 }, (_, j) => (rnd(r * 50 + k * 9 + j) > 0.5 ? 1 : 0)).join('')).join(' ')}</div>`).join('')}
          </div>
          <div id="imp" class="abs tag" style="left:1300px;top:300px;opacity:0;background:rgba(251,113,133,.2);border-color:#fb7185;color:#ffe4e6;font-size:40px">${tx('impossible')}</div>`;
      },
      update: (el, t, s) => {
        const chip = $('#chip', el);
        const off = ap(t, S(s, 3), 0.5);
        chip.style.opacity = ap(t, s.start + 0.3, 0.8) * (1 - ap(t, S(s, 2) + 0.2, 0.5));
        chip.style.transform = `translateY(${Math.sin(t * 1.6) * 6}px)`;
        chipFace(el, t, t >= S(s, 1) + 0.8 && t < S(s, 2) + 0.4 ? 'confused' : 'happy');
        const gone = ap(t, S(s, 2), 0.5);
        ['b0', 'b1', 'b2'].forEach((c, i) => {
          const n = $(`.${c}`, el);
          const p = ap(t, S(s, 1) + 0.2 + i * 0.45, 0.5);
          show(n, p * (1 - gone), 30, 0.85);
          // each bubble drifts toward the chip and bounces off
          n.style.transform += ` translateX(${p * 60}px)`;
        });
        pop($('#qm', el), ap(t, S(s, 1) + 1.2, 0.5) * (1 - gone));
        $('#rain', el).style.opacity = ap(t, S(s, 2), 0.8) * (1 - 0.6 * off);
        $$('.rc', el).forEach((c) => (c.style.transform = `translateY(${(t * Number(c.dataset.s) + Number(c.dataset.o)) % 1400}px)`));
        $$('.bit', el).forEach((b, i) => pop(b, ap(t, S(s, 2) + 0.6 + i * 0.3, 0.5) * (1 - off)));
        const conv = $('#conv', el);
        conv.style.opacity = ap(t, S(s, 3) + 0.3, 0.5) * (1 - ap(t, S(s, 4), 0.4));
        const full = $('#typed', el).dataset.full;
        $('#typed', el).textContent = full.slice(0, Math.floor(clamp((t - S(s, 3) - 0.8) / Math.max(1, dur(s, 3) - 0.8)) * full.length));
        const pp = ap(t, S(s, 4), 1.4);
        $('#paper', el).style.transform = `translateY(${-pp * 900}px) rotate(${lerp(6, -2, pp)}deg)`;
        pop($('#imp', el), ap(t, S(s, 4) + 1.4, 0.5));
      },
    },

    bridge: {
      build: () => `
        ${bg(['#134e4a', '#0b2e2c', '#041716'])}
        <svg class="art" viewBox="0 0 1920 1080"><path id="arch" d="M520 600 C 760 330, 1160 330, 1400 600" fill="none" stroke="#5eead4" stroke-width="10" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1" pathLength="1"/></svg>
        <div id="pa" class="abs" style="inset:0">
          <div class="abs who" style="left:250px;top:470px;width:260px;height:260px;border-radius:50%;background:rgba(255,255,255,.1);border:3px solid rgba(255,255,255,.25);display:grid;place-items:center;font-size:150px">🧓</div>
          <div class="abs who" style="left:1410px;top:470px;width:260px;height:260px;border-radius:50%;background:rgba(255,255,255,.1);border:3px solid rgba(255,255,255,.25);display:grid;place-items:center;font-size:150px">🧑‍⚕️</div>
          ${bubble('q1', 230, 300, '? ¿ ؟ ?!')}${bubble('q2', 1440, 300, '🤔 ?', 'right')}
        </div>
        <div id="pb" class="abs" style="inset:0;opacity:0">
          <div class="abs" style="left:250px;top:470px;width:260px;height:260px;border-radius:50%;background:rgba(255,255,255,.1);border:3px solid rgba(255,255,255,.25);display:grid;place-items:center;font-size:150px">🧑‍🎓</div>
          <p class="abs h nm" style="left:200px;width:360px;top:760px;text-align:center;font-size:40px;color:#ccfbf1">${tx('human')}</p>
          <div class="abs" style="left:1340px;top:400px;transform:scale(.7)">${chipSvg('y')}</div>
          <p class="abs h nm" style="left:1360px;width:360px;top:760px;text-align:center;font-size:40px;color:#ccfbf1">Computer</p>
        </div>
        <div id="mid" class="abs tag" style="left:0;right:0;margin:0 auto;width:max-content;top:300px;opacity:0;font-size:40px;background:rgba(45,212,191,.16);border-color:#2dd4bf;color:#ccfbf1">${tx('common')}</div>
        <div id="code" class="abs" style="left:0;right:0;margin:0 auto;width:max-content;top:280px;opacity:0;padding:22px 34px;border-radius:22px;background:#0b1023;border:2px solid #5eead4;font-family:var(--mono);font-size:46px;color:#e2e8f0">${py('Hello')}</div>
        <div id="title" class="abs" style="left:0;right:0;top:620px;text-align:center;opacity:0">
          <h1 class="h" style="font-size:96px;color:#fff;text-shadow:0 0 60px rgba(94,234,212,.5)">${tx('plTitle')}</h1>
          <p style="margin-top:18px;font-size:40px;color:#99f6e4">${tx('plSub')}</p>
        </div>`,
      update: (el, t, s) => {
        const swap = ap(t, S(s, 2), 0.7);
        const pa = $('#pa', el);
        pa.style.opacity = ap(t, s.start + 0.1, 0.6) * (1 - swap);
        $$('.who', el).forEach((w, i) => (w.style.transform = `translateY(${Math.sin(t * 1.5 + i) * 6}px)`));
        show($('.q1', el), ap(t, S(s, 0) + 0.8, 0.5), 20, 0.85);
        show($('.q2', el), ap(t, S(s, 0) + 1.6, 0.5), 20, 0.85);
        $('#pb', el).style.opacity = swap;
        $('#arch', el).setAttribute('stroke-dashoffset', String(1 - ap(t, S(s, 1) + 0.2, 1.2)));
        show($('#mid', el), ap(t, S(s, 1) + 1.0, 0.5) * (1 - ap(t, S(s, 3), 0.4)), 20, 0.9);
        show($('#code', el), ap(t, S(s, 3) + 0.4, 0.6), 20, 0.85);
        show($('#title', el), ap(t, S(s, 4), 0.7), 30, 0.94);
        $('#pb', el).style.transform = `translateY(${-ap(t, S(s, 4), 0.7) * 150}px)`;
        $$('.nm', el).forEach((n) => (n.style.opacity = 1 - ap(t, S(s, 4), 0.4)));
      },
    },

    langs: {
      build: () => {
        const card = (cls, x, label, mark, bgc, fg) => `<div class="abs ${cls}" style="left:${x}px;top:360px;width:340px;height:240px;opacity:0;border-radius:34px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.16);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
            <div style="width:110px;height:110px;border-radius:28px;background:${bgc};color:${fg};display:grid;place-items:center;font-family:var(--head);font-weight:800;font-size:52px">${mark}</div>
            <span class="h" style="font-size:42px;color:#fff">${label}</span></div>`;
        return `
          ${bg(['#312e81', '#1e1b4b', '#0b0a24'])}
          <p id="kick" class="abs h" style="left:0;right:0;top:170px;text-align:center;font-size:56px;color:#e0e7ff;opacity:0">${tx('many')}</p>
          ${card('c0', 330, 'C', 'C', '#a8b9cc', '#1e293b')}${card('c1', 790, 'Java', '☕', '#f97316', '#fff')}${card('c2', 1250, 'JavaScript', 'JS', '#facc15', '#1f2937')}
          <div id="pyc" class="abs" style="left:640px;top:330px;width:640px;height:330px;opacity:0;border-radius:44px;background:linear-gradient(140deg,rgba(55,118,171,.35),rgba(255,212,59,.18));border:3px solid #ffd43b;box-shadow:0 0 90px rgba(255,212,59,.3);display:flex;align-items:center;justify-content:center;gap:40px">
            <svg viewBox="0 0 120 120" style="width:170px;height:170px"><rect x="10" y="10" width="62" height="62" rx="18" fill="#3776ab"/><rect x="48" y="48" width="62" height="62" rx="18" fill="#ffd43b"/><circle cx="30" cy="28" r="6" fill="#fff"/><circle cx="90" cy="92" r="6" fill="#fff"/></svg>
            <div><div class="h" style="font-size:104px;color:#fff;line-height:1">Python</div><div id="syl" style="margin-top:14px;font-family:var(--head);font-weight:700;font-size:32px;color:#fde68a">⭐ ${tx('syllabus')}</div></div>
          </div>
          <div id="info" class="abs" style="left:1060px;top:300px;width:720px;opacity:0">
            <p style="font-family:var(--head);font-weight:700;font-size:32px;color:#a5b4fc">${tx('creator')}</p>
            <p class="h" style="margin-top:6px;font-size:64px;color:#fff">Guido van Rossum</p>
            <p style="margin-top:34px;font-family:var(--head);font-weight:700;font-size:32px;color:#a5b4fc">${tx('first')}</p>
            <p id="year" class="h" style="font-size:140px;line-height:1;color:#fde68a;font-variant-numeric:tabular-nums">1991</p>
          </div>
          <div id="fun" class="abs" style="left:250px;top:780px;opacity:0;display:flex;gap:24px;align-items:center">
            <span class="tag" style="font-size:38px;background:rgba(251,191,36,.18);border-color:#fbbf24;color:#fef3c7">${tx('named')}</span>
            <span class="tag" style="font-size:34px;background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.2);color:#cbd5e1;text-decoration:line-through;text-decoration-color:#fb7185;text-decoration-thickness:4px">${tx('notSnake')}</span>
          </div>`;
      },
      update: (el, t, s) => {
        show($('#kick', el), ap(t, S(s, 0), 0.6), 20, 1);
        const d1 = dur(s, 1), out = ap(t, S(s, 2), 0.6);
        ['c0', 'c1', 'c2'].forEach((c, i) => {
          const n = $(`.${c}`, el);
          show(n, ap(t, S(s, 1) + (d1 * i) / 3, 0.5), 30, 0.8);
          n.style.opacity = Number(n.style.opacity) * (1 - 0.75 * out);
          n.style.transform += ` translateY(${-out * 200}px) scale(${1 - out * 0.35})`;
        });
        const pyc = $('#pyc', el);
        const pin = ap(t, S(s, 2) + 0.2, 0.7), side = ap(t, S(s, 3), 0.7);
        pyc.style.opacity = pin;
        pyc.style.transform = `translate(${-side * 400}px, ${(1 - pin) * 60}px) scale(${lerp(0.8, 1, pin) - side * 0.12})`;
        show($('#syl', el), ap(t, S(s, 2) + 0.9, 0.5), 10, 1);
        show($('#info', el), ap(t, S(s, 3) + 0.4, 0.6), 20, 0.96);
        $('#year', el).textContent = Math.round(lerp(1970, 1991, ap(t, S(s, 3) + 0.8, 1.6)));
        show($('#fun', el), ap(t, S(s, 4) + 0.3, 0.6), 20, 0.95);
        $('#kick', el).style.opacity = Number($('#kick', el).style.opacity) * (1 - out);
      },
    },

    compare: {
      build: () => {
        const c = ['<span style="color:#c084fc">#include</span> <span style="color:#86efac">&lt;stdio.h&gt;</span>', '<span style="color:#7dd3fc">int</span> main() {', `    <span style="color:#7dd3fc">printf</span>(<span style="color:#86efac">"Paracetamol 500 mg\\n"</span>);`, '    <span style="color:#c084fc">return</span> 0;', '}'];
        return `
          ${bg(['#0f172a', '#0b1224', '#050814'])}
          <p id="q" class="abs h" style="left:0;right:0;top:130px;text-align:center;font-size:60px;color:#fff;opacity:0">${tx('whyQ')}</p>
          <div id="r1" class="abs" style="left:0;right:0;margin:0 auto;width:max-content;top:225px;opacity:0;display:flex;align-items:center;gap:16px">
            <span class="tag" style="font-size:34px;background:rgba(45,212,191,.16);border-color:#2dd4bf;color:#ccfbf1">${tx('reason')} 1 · ${tx('r1')}</span></div>
          ${win('cw', 120, 330, 820, 'label.c', c.map((l, i) => `<div class="cl" style="opacity:0">${l}</div>`).join(''))}
          ${win('pw', 1000, 330, 800, 'label.py', `<div id="pyl"><span id="pk" style="color:#7dd3fc;border-radius:8px">print</span>(<span id="ps" style="color:#86efac;border-radius:8px">"Paracetamol 500 mg"</span>)</div>`)}
          <div id="n5" class="abs tag" style="left:400px;top:780px;opacity:0;font-size:36px;background:rgba(251,113,133,.16);border-color:#fb7185;color:#ffe4e6">C · ${tx('lines5')}</div>
          <div id="n1" class="abs tag" style="left:1180px;top:640px;opacity:0;font-size:36px;background:rgba(52,211,153,.18);border-color:#34d399;color:#d1fae5">Python · ${tx('lines1')}</div>
          <div id="few" class="abs tag" style="left:1180px;top:740px;opacity:0;font-size:36px;background:rgba(52,211,153,.18);border-color:#34d399;color:#d1fae5">${tx('fewer')}</div>`;
      },
      update: (el, t, s) => {
        show($('#q', el), ap(t, S(s, 0), 0.6), 20, 1);
        show($('#r1', el), ap(t, S(s, 1) + 0.2, 0.5), 15, 0.9);
        show($('#cw', el), ap(t, S(s, 2), 0.5), 30, 0.96);
        $$('.cl', el).forEach((l, i) => (l.style.opacity = ap(t, S(s, 2) + 0.4 + (i * dur(s, 2)) / 6, 0.3)));
        show($('#pw', el), ap(t, S(s, 3), 0.5), 30, 0.96);
        const pin = ap(t, S(s, 3) + 0.5, 0.8);
        $('#pyl', el).style.clipPath = `inset(0 ${100 - pin * 100}% 0 0)`;
        const glow = (n, a) => { const p = ap(t, a, 0.4) * (1 - ap(t, S(s, 5), 0.5)); n.style.background = `rgba(253,230,138,${0.22 * p})`; n.style.boxShadow = `0 0 0 ${6 * p}px rgba(253,230,138,${0.22 * p})`; };
        glow($('#pk', el), S(s, 4));
        glow($('#ps', el), S(s, 4) + dur(s, 4) * 0.35);
        show($('#n5', el), ap(t, S(s, 5), 0.5), 15, 0.9);
        show($('#n1', el), ap(t, S(s, 5) + 0.3, 0.5), 15, 0.9);
        show($('#few', el), ap(t, S(s, 5) + 1.0, 0.5), 15, 0.9);
      },
    },

    reasons: {
      build: () => {
        const card = (cls, x, n, title, inner, sub) => `<div class="abs ${cls}" style="left:${x}px;top:200px;width:520px;height:620px;opacity:0;border-radius:40px;background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.16);padding:40px 40px;display:flex;flex-direction:column">
            <span style="font-family:var(--head);font-weight:700;font-size:28px;color:#99f6e4">${tx('reason')} ${n}</span>
            <span class="h" style="margin-top:8px;font-size:48px;color:#fff;line-height:1.1">${title}</span>
            <div style="flex:1;display:grid;place-items:center">${inner}</div>
            <span class="sub" style="font-size:32px;color:#ccfbf1;font-weight:600">${sub}</span></div>`;
        const lib = (i, icon, name, what) => `<div class="lib" style="display:flex;align-items:center;gap:18px;padding:14px 18px;border-radius:20px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);width:420px">
            <span style="width:62px;height:62px;border-radius:16px;background:rgba(45,212,191,.2);display:grid;place-items:center;font-size:32px;color:#5eead4;font-weight:800;flex:none">${icon}</span>
            <span><b style="display:block;font-family:var(--mono);font-size:28px;color:#fff">${name}</b><span style="font-size:24px;color:#a7f3d0">${what}</span></span></div>`;
        return `
          ${bg(['#164e63', '#0c2d3a', '#06151c'])}
          ${card('k2', 120, 2, tx('free'), '<div class="h" style="font-size:190px;color:#5eead4;text-shadow:0 0 60px rgba(94,234,212,.4)">₹0</div>', tx('freeSub'))}
          ${card('k3', 700, 3, tx('libs'), `<div style="display:flex;flex-direction:column;gap:16px">${lib(0, 'Σ', 'NumPy', tx('libCalc'))}${lib(1, '▦', 'Pandas', tx('libData'))}${lib(2, '📈', 'Matplotlib', tx('libGraph'))}</div>`, `<span id="tabs">${tx('libsSub')}</span>`)}
          ${card('k4', 1280, 4, tx('pharma'), '<div style="font-size:120px;display:flex;gap:10px">💊🩺<br>🧪📊</div>', tx('pharmaSub'))}`;
      },
      update: (el, t, s) => {
        show($('.k2', el), ap(t, S(s, 0), 0.6), 40, 0.92);
        show($('.k3', el), ap(t, S(s, 1), 0.6), 40, 0.92);
        $('#tabs', el).style.opacity = ap(t, S(s, 2) + 0.4, 0.5);
        const d3 = dur(s, 3);
        $$('.lib', el).forEach((n, i) => {
          const on = t >= S(s, 3) + (d3 * i) / 3 && t < E(s, 3) + 0.4;
          n.style.opacity = t < S(s, 1) + 0.6 ? 0 : 1;
          n.style.background = on ? 'rgba(45,212,191,.22)' : 'rgba(255,255,255,.06)';
          n.style.borderColor = on ? '#2dd4bf' : 'rgba(255,255,255,.14)';
          n.style.transform = `scale(${on ? 1.04 : 1})`;
        });
        const k4 = $('.k4', el);
        show(k4, ap(t, S(s, 4), 0.6), 40, 0.92);
        const g = ap(t, S(s, 4) + 0.5, 0.6);
        k4.style.borderColor = `rgba(251,191,36,${0.16 + g * 0.84})`;
        k4.style.boxShadow = `0 0 ${80 * g}px rgba(251,191,36,${0.3 * g})`;
        // the first two cards step back when the best reason arrives
        ['.k2', '.k3'].forEach((c) => { const n = $(c, el); n.style.opacity = Number(n.style.opacity) * (1 - 0.45 * g); });
      },
    },

    pharma: {
      build: () => {
        const panel = (i, x, y, title, inner) => `<div class="abs pan" data-i="${i}" style="left:${x}px;top:${y}px;width:800px;height:380px;opacity:0;border-radius:34px;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.14);padding:28px 34px;overflow:hidden">
            <p class="h" style="font-size:36px;color:#fff">${title}</p><div style="position:relative;height:280px">${inner}</div></div>`;
        const dots = Array.from({ length: 60 }, (_, i) => `<span class="pt" style="width:26px;height:26px;border-radius:50%;background:#475569"></span>`).join('');
        // one-compartment oral dose: C(t) = 10(e^-0.25t - e^-1.6t)
        const pts = Array.from({ length: 61 }, (_, i) => { const h = i * 0.4, c = 10 * (Math.exp(-0.25 * h) - Math.exp(-1.6 * h)); return `${40 + i * 10},${230 - c * 26}`; });
        const rows = [0, 1, 2, 3, 4].map((r) => `<div class="ad" style="display:flex;align-items:center;gap:14px;height:44px;padding:0 14px;border-radius:12px;margin-bottom:8px;background:rgba(255,255,255,.05)"><span style="width:22px;height:22px;border-radius:6px;background:#64748b"></span><span style="height:12px;border-radius:6px;background:#475569;width:${240 + rnd(r) * 260}px"></span></div>`).join('');
        const ring = Array.from({ length: 6 }, (_, k) => { const a = (k / 6) * Math.PI * 2; return [Math.cos(a) * 80, Math.sin(a) * 80]; });
        const mol = `<svg viewBox="-200 -150 400 300" style="position:absolute;left:180px;top:-10px;width:400px;height:300px"><g id="mol">
            ${ring.map(([x, y], k) => { const [x2, y2] = ring[(k + 1) % 6]; return `<line x1="${x}" y1="${y}" x2="${x2}" y2="${y2}" stroke="#c4b5fd" stroke-width="8"/>`; }).join('')}
            <line x1="80" y1="0" x2="160" y2="0" stroke="#c4b5fd" stroke-width="8"/><line x1="-40" y1="-69" x2="-80" y2="-138" stroke="#c4b5fd" stroke-width="8"/>
            ${ring.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="18" fill="#a78bfa"/>`).join('')}<circle cx="160" cy="0" r="24" fill="#fb7185"/><circle cx="-80" cy="-138" r="24" fill="#60a5fa"/></g></svg>`;
        return `
          ${bg(['#3b0764', '#1e0b3b', '#0b0418'])}
          ${panel(0, 120, 120, tx('p1'), `<div style="display:grid;grid-template-columns:repeat(15,26px);gap:14px;margin-top:22px">${dots}</div><p id="np" class="h" style="position:absolute;right:0;bottom:6px;font-size:44px;color:#5eead4">0 ${tx('patients')}</p>`)}
          ${panel(1, 1000, 120, tx('p2'), `<svg viewBox="0 0 680 260" style="width:680px;height:260px"><line x1="40" y1="230" x2="660" y2="230" stroke="#64748b" stroke-width="3"/><line x1="40" y1="10" x2="40" y2="230" stroke="#64748b" stroke-width="3"/><text x="560" y="256" fill="#94a3b8" font-size="22" font-family="Inter">${tx('time')} →</text><polyline id="pk" points="${pts.join(' ')}" fill="none" stroke="#fbbf24" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><g id="cmax" opacity="0"><circle cx="${pts[5].split(',')[0]}" cy="${pts[5].split(',')[1]}" r="11" fill="#fff"/><text x="${Number(pts[5].split(',')[0]) + 22}" y="${Number(pts[5].split(',')[1]) - 6}" fill="#fff" font-size="26" font-family="Plus Jakarta Sans" font-weight="800">Cmax</text></g></svg>`)}
          ${panel(2, 120, 560, tx('p3'), `<div style="margin-top:16px">${rows}</div><span id="sig" class="tag" style="position:absolute;right:0;top:96px;opacity:0;font-size:28px;padding:10px 18px;background:rgba(251,113,133,.2);border-color:#fb7185;color:#ffe4e6">${tx('signal')}</span>`)}
          ${panel(3, 1000, 560, tx('p4'), mol)}
          <div id="skill" class="abs" style="left:0;right:0;margin:0 auto;top:430px;width:max-content;opacity:0;padding:34px 60px;border-radius:40px;background:#fffaf0;box-shadow:0 40px 100px rgba(0,0,0,.55)"><span class="h" style="font-size:68px;color:#1d1d1f">${tx('skill').replace('#fde68a', '#7c3aed')}</span></div>`;
      },
      update: (el, t, s) => {
        const fin = ap(t, S(s, 4), 0.6);
        $$('.pan', el).forEach((p, i) => {
          const on = t >= S(s, i) && t < S(s, i + 1);
          show(p, ap(t, S(s, i), 0.6), 30, 0.95);
          if (t >= S(s, i)) p.style.opacity = (on ? 1 : 0.55) * (1 - 0.6 * fin);
          p.style.borderColor = on ? 'rgba(196,181,253,.9)' : 'rgba(255,255,255,.14)';
        });
        const p0 = clamp((t - S(s, 0) - 0.3) / Math.max(1, dur(s, 0)));
        $$('.pt', el).forEach((d, i) => (d.style.background = i < p0 * 60 ? (i % 7 === 3 ? '#fbbf24' : '#2dd4bf') : '#475569'));
        $('#np', el).textContent = `${Math.round(p0 * 2400).toLocaleString('en-IN')} ${tx('patients')}`;
        $('#pk', el).setAttribute('stroke-dashoffset', String(1 - clamp((t - S(s, 1) - 0.3) / Math.max(1, dur(s, 1) - 0.3))));
        $('#cmax', el).setAttribute('opacity', ap(t, S(s, 1) + dur(s, 1) * 0.45, 0.4));
        const bad = ap(t, S(s, 2) + dur(s, 2) * 0.5, 0.4);
        $$('.ad', el).forEach((r, i) => (r.style.background = i === 2 ? `rgba(251,113,133,${0.05 + bad * 0.3})` : 'rgba(255,255,255,.05)'));
        pop($('#sig', el), bad);
        $('#mol', el).setAttribute('transform', `rotate(${t * 25}) scale(${0.9 + 0.1 * ap(t, S(s, 3), 0.6)})`);
        pop($('#skill', el), fin);
      },
    },

    interp: {
      build: () => {
        const code = ['Paracetamol', '500 mg', 'After food'];
        return `
          ${bg(['#1e3a8a', '#14215a', '#090f2c'])}
          <div id="rxw" class="abs" style="left:100px;top:250px;opacity:0;transform:rotate(-3deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.45))">${prescription(470)}</div>
          <div id="reads" class="abs tag" style="left:170px;top:760px;opacity:0;font-size:32px">📖 ${tx('reads')}</div>
          ${win('ed', 690, 250, 640, 'label.py', code.map((c, i) => `<div class="ln" data-i="${i}" style="position:relative;height:58px"><span style="color:#64748b">${i + 1}</span>&nbsp; ${py(c)}</div>`).join(''))}
          <div id="ptr" class="abs" style="left:618px;top:0;opacity:0;display:flex;align-items:center;gap:8px;padding:10px 18px;border-radius:999px;background:#fde68a;color:#1f2937;font-family:var(--head);font-weight:800;font-size:26px;box-shadow:0 10px 30px rgba(0,0,0,.35)">▶</div>
          <div id="itag" class="abs tag" style="left:780px;top:600px;opacity:0;font-size:34px;background:rgba(253,230,138,.16);border-color:#fde68a;color:#fef3c7">⚙️ ${tx('interp')}: ↓ 1 → 2 → 3</div>
          <div id="con" class="abs" style="left:1400px;top:250px;width:420px;opacity:0;border-radius:28px;background:#020617;border:1.5px solid #1e293b;overflow:hidden">
            <div style="padding:16px 24px;background:#0f172a;color:#94a3b8;font-family:var(--head);font-weight:700;font-size:24px">${tx('output')}</div>
            <div id="out" style="padding:24px 28px;font-family:var(--mono);font-size:34px;line-height:1.75;color:#e2e8f0;min-height:250px"></div>
          </div>`;
      },
      update: (el, t, s) => {
        show($('#rxw', el), ap(t, s.start + 0.1, 0.6), 30, 0.95);
        const d1 = dur(s, 1);
        $$('.rxl', el).forEach((g, i) => {
          const on = t >= S(s, 1) + (d1 * i) / 3 && t < S(s, 1) + (d1 * (i + 1)) / 3 + 0.2;
          $('.hl', g).setAttribute('opacity', on ? 1 : 0);
          $('.dot', g).setAttribute('fill', on ? '#f59e0b' : t >= S(s, 1) + (d1 * i) / 3 ? '#2dd4bf' : '#e2e8f0');
          $('.num', g).setAttribute('fill', t >= S(s, 1) + (d1 * i) / 3 ? '#fff' : '#64748b');
        });
        show($('#reads', el), ap(t, S(s, 1) + 0.3, 0.5), 15, 0.9);
        show($('#ed', el), ap(t, S(s, 2), 0.6), 30, 0.96);
        show($('#con', el), ap(t, S(s, 2) + 0.3, 0.6), 30, 0.96);
        // line order: swapped at k5 so "After food" moves to the top
        const sw = ap(t, S(s, 5) + 0.3, 0.8);
        const pos = [lerp(0, 1, sw), lerp(1, 2, sw), lerp(2, 0, sw)];
        $$('.ln', el).forEach((l, i) => (l.style.transform = `translateY(${(pos[i] - i) * 58}px)`));
        // pointer: one sweep while the interpreter is introduced, then a step per line at k4
        const d4 = dur(s, 4);
        let row = -1;
        if (t >= S(s, 3) && t < S(s, 4)) row = clamp((t - S(s, 3) - 0.5) / Math.max(1, dur(s, 3) - 0.5)) * 2;
        else if (t >= S(s, 4) && t < S(s, 5)) row = Math.min(2, Math.floor((t - S(s, 4)) / (d4 / 3)));
        else if (t >= S(s, 5) + 1.1) row = Math.min(2, Math.floor((t - S(s, 5) - 1.1) / 0.55));
        const ptr = $('#ptr', el);
        ptr.style.opacity = row >= 0 ? 1 : 0;
        ptr.style.transform = `translateY(${250 + 30 + 78 + Math.max(0, row) * 58}px)`;
        show($('#itag', el), ap(t, S(s, 3) + 0.6, 0.5), 15, 0.9);
        // output: grows a line at a time at k4; after the swap it reruns in the new order
        const first = ['Paracetamol', '500 mg', 'After food'], second = ['After food', 'Paracetamol', '500 mg'];
        let lines = [];
        if (t >= S(s, 5) + 1.1) lines = second.slice(0, Math.min(3, Math.floor((t - S(s, 5) - 1.1) / 0.55) + 1));
        else if (t >= S(s, 4)) lines = first.slice(0, Math.min(3, Math.floor((t - S(s, 4)) / (d4 / 3)) + 1));
        $('#out', el).innerHTML = lines.map((x, i) => `<div style="color:${t >= S(s, 5) + 1.1 && i === 0 ? '#fde68a' : '#e2e8f0'}">${x}</div>`).join('');
      },
    },

    teaser2: {
      build: () => `
        ${bg(['#2a2370', '#141038', '#07061a'])}
        <p id="turn" class="abs h" style="left:0;right:0;top:110px;text-align:center;font-size:84px;color:#fff;opacity:0">${tx('turn')} ✍️</p>
        <div id="phone" class="abs" style="left:300px;top:250px;width:420px;height:760px;opacity:0;border-radius:60px;background:#0f172a;border:14px solid #1e293b;box-shadow:0 40px 90px rgba(0,0,0,.55);padding:60px 26px">
          <div style="border-radius:20px;background:#0b1023;border:1.5px solid #2b3466;padding:20px;font-family:var(--mono);font-size:22px;color:#e2e8f0;min-height:140px"><span id="pt"></span><span style="color:#a5b4fc">|</span></div>
          <div id="po" style="margin-top:22px;border-radius:20px;background:#020617;padding:20px;font-family:var(--mono);font-size:24px;color:#5eead4;opacity:0">Paracetamol 500 mg</div>
          <div style="margin-top:22px;display:flex;justify-content:center"><span style="padding:14px 34px;border-radius:999px;background:#34d399;color:#03201d;font-family:var(--head);font-weight:800;font-size:24px">▶ Run</span></div>
        </div>
        <div id="err" class="abs" style="left:880px;top:330px;width:880px;opacity:0;border-radius:30px;background:#1a0b14;border:2px solid #fb7185;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.5)">
          <div style="padding:18px 28px;background:rgba(251,113,133,.18);color:#fecdd3;font-family:var(--mono);font-weight:700;font-size:30px">SyntaxError</div>
          <div style="padding:26px 30px;font-family:var(--mono);font-size:34px;line-height:1.6;color:#e2e8f0;white-space:pre">${'print("Paracetamol 500 mg"'}<br><span style="color:#fb7185">                          ^</span></div>
        </div>
        <div id="fr" class="abs tag" style="left:1100px;top:640px;opacity:0;font-size:38px;background:rgba(52,211,153,.18);border-color:#34d399;color:#d1fae5">${tx('friend')}</div>
        <div id="ep3" class="abs h" style="left:880px;top:780px;opacity:0;font-size:64px;color:#fff">Episode 3 · <span style="color:#fde68a">${T().next ? T().next.title.replace(/<[^>]+>/g, '') : ''}</span></div>`,
      update: (el, t, s) => {
        show($('#turn', el), ap(t, S(s, 0), 0.6), 20, 0.95);
        show($('#phone', el), ap(t, S(s, 0) + 0.4, 0.7), 40, 0.94);
        const full = 'print("Paracetamol 500 mg")';
        $('#pt', el).textContent = full.slice(0, Math.floor(clamp((t - S(s, 1) - 0.3) / Math.max(1, dur(s, 1) * 0.6)) * full.length));
        $('#po', el).style.opacity = ap(t, S(s, 1) + dur(s, 1) * 0.75, 0.4);
        show($('#err', el), ap(t, S(s, 2), 0.6), 30, 0.95);
        pop($('#fr', el), ap(t, S(s, 2) + dur(s, 2) * 0.55, 0.5));
        show($('#ep3', el), ap(t, S(s, 3), 0.6), 20, 0.95);
      },
    },
  };
});
