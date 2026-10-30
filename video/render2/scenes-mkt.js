// Marketing films (homepage brand film, colleges film): mostly Apple-launch style — one idea per frame,
// huge type, the real product on floating devices, an "Introducing" reveal — with illustrated moments
// only where the story is emotional. Product screens are captured from campuschamp.in (video/marketing/shots).
window.addScenes(({ $, $$, clamp, ease, ap, lerp, show, pop, S, E, T }) => {
  const SHOT = (f) => `../marketing/shots/${f}`;
  const dur = (s, k) => (s.lines[k] || {}).dur || 1;
  const H = 'font-family:var(--head);font-weight:800;letter-spacing:-.035em;';
  const words = (text, cls = 'w') => text.split(' ').map((w) => `<span class="${cls}" style="display:inline-block;opacity:0;margin-right:.24em">${w}</span>`).join('');
  // words land one by one (blur → sharp), Apple keynote style
  const reveal = (el, t, start, per = 0.16) => $$('.w', el).forEach((w, i) => {
    const p = ap(t, start + i * per, 0.5);
    w.style.opacity = p;
    w.style.filter = `blur(${(1 - p) * 14}px)`;
    w.style.transform = `translateY(${(1 - p) * 24}px)`;
  });
  const glowBg = (c1 = 'rgba(99,102,241,.28)', c2 = 'rgba(45,212,191,.16)') => `<div class="abs" style="inset:0;background:#000"></div>
    <div class="abs" style="left:50%;top:55%;width:1500px;height:900px;transform:translate(-50%,-50%);background:radial-gradient(closest-side,${c1},transparent 70%)"></div>
    <div class="abs" style="left:70%;top:30%;width:900px;height:700px;transform:translate(-50%,-50%);background:radial-gradient(closest-side,${c2},transparent 70%)"></div>`;
  const phone = (id, img, w = 400) => `<div id="${id}" class="abs" style="width:${w}px;height:${w * 2.16}px;border-radius:${w * 0.16}px;background:#0b0b0f;padding:${w * 0.035}px;box-shadow:0 60px 120px rgba(0,0,0,.6),0 0 0 2px #2a2a33 inset;transform-style:preserve-3d">
      <div style="position:relative;width:100%;height:100%;border-radius:${w * 0.13}px;overflow:hidden;background:#fff"><img src="${img}" style="width:100%;display:block"/>
      <div style="position:absolute;left:50%;top:${w * 0.03}px;width:${w * 0.3}px;height:${w * 0.075}px;border-radius:99px;background:#000;transform:translateX(-50%)"></div></div></div>`;
  const laptop = (id, img, w = 1100) => `<div id="${id}" class="abs" style="width:${w}px">
      <div style="border-radius:${w * 0.03}px ${w * 0.03}px 0 0;background:#0b0b0f;padding:${w * 0.018}px;box-shadow:0 50px 100px rgba(0,0,0,.35)"><div style="border-radius:8px;overflow:hidden;background:#f8fafc;aspect-ratio:16/10;display:grid;place-items:center;padding:3%"><img src="${img}" style="width:100%;display:block;border-radius:12px"/></div></div>
      <div style="height:${w * 0.025}px;margin:0 -4%;border-radius:0 0 ${w * 0.02}px ${w * 0.02}px;background:linear-gradient(#d4d4d8,#a1a1aa)"></div></div>`;
  const SEMS = [['Python', 'BP101T'], ['Statistics · Computers', 'BP201T · BP212P'], ['Machine learning', 'BP301T'], ['', ''], ['', ''], ['AI applications · CADD', 'BP604T · BP610P'], ['AI in the clinic', 'BP703T'], ['Ethical AI', 'BP801T']];
  const track = (y, big = false) => `<div class="abs trk" style="left:200px;right:200px;top:${y}px;height:4px;border-radius:2px;background:rgba(255,255,255,.12)"><div class="fill" style="height:100%;width:0;border-radius:2px;background:linear-gradient(90deg,#6366f1,#a855f7,#2dd4bf)"></div></div>
    ${Array.from({ length: 8 }, (_, i) => `<div class="abs sem" data-i="${i}" style="left:${200 + i * (1520 / 7) - 40}px;top:${y - 38}px;width:80px;text-align:center">
      <div class="dot" style="width:${big ? 40 : 30}px;height:${big ? 40 : 30}px;margin:${big ? 18 : 23}px auto 0;border-radius:50%;background:#18181b;border:3px solid #3f3f46"></div>
      <p style="margin-top:16px;font-family:var(--head);font-weight:700;font-size:24px;color:#71717a;white-space:nowrap;margin-left:-40px;margin-right:-40px">Sem ${i + 1}</p></div>`).join('')}`;
  const lightTrack = (el, t, start, d) => {
    const p = clamp((t - start) / Math.max(0.5, d));
    $('.fill', el).style.width = `${p * 100}%`;
    $$('.sem', el).forEach((n, i) => {
      const on = p >= i / 7 - 0.001;
      const dot = $('.dot', n);
      dot.style.background = on ? 'linear-gradient(135deg,#6366f1,#2dd4bf)' : '#18181b';
      dot.style.borderColor = on ? '#a5b4fc' : '#3f3f46';
      dot.style.boxShadow = on ? '0 0 30px rgba(129,140,248,.7)' : 'none';
      $('p', n).style.color = on ? '#fff' : '#71717a';
    });
  };
  const endCard = (title, tag, cta, url, scanLabel) => `
      <div class="layer brand"></div>
      <div class="abs" style="inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
        <div id="g" style="width:120px;height:120px;border-radius:34px;background:linear-gradient(140deg,#6366f1,#7c3aed 55%,#2dd4bf);display:grid;place-items:center;color:#fff;font-family:var(--mono);font-weight:700;font-size:44px;box-shadow:0 30px 80px rgba(99,102,241,.35)">&lt;/&gt;</div>
        <h1 id="e1" style="${H}margin-top:40px;font-size:118px;line-height:1;color:#1d1d1f">${title}</h1>
        <p id="e2" style="${H}margin-top:22px;font-size:58px;line-height:1.1"><span class="grad">${tag}</span></p>
        <div id="e3" style="margin-top:56px;display:flex;gap:22px;align-items:center">
          <span style="font-family:var(--head);font-weight:700;font-size:34px;background:#1d1d1f;color:#fff;border-radius:999px;padding:22px 44px">${cta}</span>
          <span style="font-family:var(--head);font-weight:600;font-size:34px;color:#4f46e5">${url}</span>
        </div>
      </div>
      <div id="e4" class="abs" style="right:90px;bottom:80px;text-align:center"><img src="${T().qr}" style="width:170px;height:170px;border-radius:16px;box-shadow:0 10px 40px rgba(0,0,0,.08)"/><p style="margin-top:8px;font-family:var(--head);font-weight:700;font-size:20px;color:#6e6e73">${scanLabel}</p></div>`;
  const endUpdate = (el, t, s) => {
    const g = $('#g', el), pg = ap(t, s.start + 0.1, 0.7);
    g.style.opacity = pg;
    g.style.transform = `scale(${lerp(0.7, 1, pg)})`;
    ['e1', 'e2', 'e3', 'e4'].forEach((id, i) => show($(`#${id}`, el), ap(t, s.start + 0.4 + i * 0.25, 0.7), 24, 0.98));
  };
  const introCard = (sub, extra = '') => `${glowBg('rgba(124,92,255,.32)', 'rgba(45,212,191,.2)')}
      <div class="abs" style="inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
        <p id="i0" style="${H}font-size:52px;color:#a1a1aa;letter-spacing:-.01em;opacity:0">Introducing</p>
        <div id="i1" style="margin-top:30px;display:flex;align-items:center;gap:36px;opacity:0">
          <div style="width:150px;height:150px;border-radius:42px;background:linear-gradient(140deg,#6366f1,#7c3aed 55%,#2dd4bf);display:grid;place-items:center;color:#fff;font-family:var(--mono);font-weight:700;font-size:56px;box-shadow:0 0 120px rgba(124,92,255,.6)">&lt;/&gt;</div>
          <h1 style="${H}font-size:170px;line-height:1;color:#fff">Campus Champ</h1>
        </div>
        ${extra}
        <p id="i2" style="${H}margin-top:34px;font-size:56px;color:#d4d4d8;opacity:0">${sub}</p>
      </div>`;
  const introUpdate = (el, t, s) => {
    const a = S(s, 0) - 0.3;
    show($('#i0', el), ap(t, a, 0.6), 10, 1);
    const p = ap(t, a + 0.7, 1.0);
    const i1 = $('#i1', el);
    i1.style.opacity = p;
    i1.style.filter = `blur(${(1 - p) * 20}px)`;
    i1.style.transform = `scale(${lerp(1.18, 1, ease(p))})`;
    if ($('#i3', el)) show($('#i3', el), ap(t, a + 1.3, 0.6), 14, 1);
    show($('#i2', el), ap(t, a + 1.7, 0.7), 16, 1);
  };

  return {
    // ================= homepage brand film =================
    'b-hook': {
      brand: true,
      build: (s) => `${glowBg()}
        <h1 id="h1" class="abs" style="${H}left:0;right:0;top:400px;text-align:center;font-size:150px;line-height:1.05;color:#fff;transform-origin:50% 0">${words(s.lines[0] ? 'AI is changing pharmacy.' : '')}</h1>
        <p id="yr" class="abs" style="${H}left:0;right:0;top:390px;text-align:center;font-size:64px;color:#d4d4d8;opacity:0">In every year of your B.Pharm.</p>
        <div id="trk" style="opacity:0">${track(640, true)}</div>
        ${[0, 1, 2, 5, 6].map((i, k) => `<div class="abs pill" style="left:${200 + i * (1520 / 7)}px;top:${k % 2 ? 470 : 520}px;opacity:0;transform:translateX(-50%);white-space:nowrap;${H}font-size:34px;letter-spacing:-.01em;color:#fff;padding:14px 26px;border-radius:999px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.22)">${['Python', 'Statistics', 'Machine learning', 'AI in drug design', 'AI in the clinic'][k]}</div>`).join('')}`,
      update: (el, t, s) => {
        reveal($('#h1', el), t, S(s, 0) + 0.1, 0.22);
        const up = ap(t, S(s, 1), 0.8);
        $('#h1', el).style.transform = `translateY(${-up * 240}px) scale(${1 - up * 0.45})`;
        show($('#yr', el), ap(t, S(s, 1) + 0.6, 0.6), 16, 1);
        $('#trk', el).style.opacity = ap(t, S(s, 1) + 0.4, 0.6);
        lightTrack(el, t, S(s, 1) + 0.8, dur(s, 1) - 0.6);
        $$('.pill', el).forEach((p, k) => {
          const q = ap(t, S(s, 2) + (k * dur(s, 2)) / 5, 0.4);
          p.style.opacity = q;
          p.style.transform = `translateX(-50%) translateY(${(1 - q) * 20}px) scale(${lerp(0.8, 1, q)})`;
        });
      },
    },

    'b-fear': {
      brand: true,
      build: () => {
        const J = ['syntax', 'interpreter', 'iteration', 'recursion', 'regression', 'overfitting', 'gradient descent', 'docking', 'pharmacophore', 'QSAR', 'p-value', 'ANOVA', 'neural network', 'hyperparameter', 'DataFrame', 'indentation', 'boolean', 'exception', 'virtual screening', 'ADMET', 'confusion matrix', 'null hypothesis', 'lambda', 'tokenisation'];
        const r = (i) => { const x = Math.sin(i * 91.7) * 1e4; return x - Math.floor(x); };
        return `<div class="abs" style="inset:0;background:radial-gradient(circle at 50% 50%,#1c1530,#000 70%)"></div>
          ${J.map((w, i) => `<span class="jw abs" data-x="${r(i) * 1700 + 60}" data-y="${(i % 2 ? 40 + r(i + 40) * 260 : 700 + r(i + 40) * 300)}" data-s="${0.4 + r(i + 9)}" style="left:0;top:0;${H}font-size:${34 + r(i + 3) * 46}px;color:rgba(255,255,255,${0.25 + r(i + 5) * 0.35});white-space:nowrap">${w}</span>`).join('')}
          <h1 id="q" class="abs" style="${H}left:0;right:0;top:390px;text-align:center;font-size:110px;line-height:1.12;color:#fff">${words('When every word is new,')}<br>${words('everything feels hard.')}</h1>`;
      },
      update: (el, t, s) => {
        $$('.jw', el).forEach((w, i) => {
          const sp = Number(w.dataset.s);
          const x = Number(w.dataset.x) + Math.sin(t * sp + i) * 60, y = Number(w.dataset.y) + Math.cos(t * sp * 0.8 + i) * 40;
          w.style.transform = `translate(${x}px,${y}px) rotate(${Math.sin(t * 0.5 + i) * 8}deg)`;
          w.style.filter = `blur(${2 + 4 * (0.5 + 0.5 * Math.sin(t * 1.3 + i))}px)`;
          w.style.opacity = ap(t, s.start + (i % 8) * 0.12, 0.6);
        });
        reveal($('#q', el), t, S(s, 0) + 0.1, 0.2);
      },
    },

    'b-tongue': {
      brand: true,
      build: (s) => `<div class="layer brand"></div>
        <div class="abs" style="left:0;right:0;top:250px;display:flex;justify-content:center;gap:18px">
          ${['English', 'ಕನ್ನಡ', 'हिन्दी'].map((l, i) => `<span class="lc" data-i="${i}" style="font-family:var(--head);font-weight:700;font-size:34px;padding:14px 32px;border-radius:999px;background:#f2f2f7;color:#6e6e73">${l}</span>`).join('')}
        </div>
        ${[0, 1, 2].map((k) => `<h1 class="ln abs" data-k="${k}" style="${H}left:120px;right:120px;top:420px;text-align:center;font-size:118px;line-height:1.08;color:#1d1d1f;opacity:0">${(s.lines[k] || {}).text || ''}</h1>`).join('')}
        <h1 id="ok" class="abs" style="${H}left:0;right:0;top:430px;text-align:center;font-size:150px;line-height:1;opacity:0"><span class="grad">Now, it makes sense.</span></h1>`,
      update: (el, t, s) => {
        let k = -1;
        for (let i = 0; i < 4; i++) if (t >= S(s, i) - 0.25) k = i;
        $$('.ln', el).forEach((h, i) => {
          const on = k === i;
          const p = on ? ap(t, S(s, i) - 0.25, 0.45) : 0;
          h.style.opacity = p;
          h.style.filter = `blur(${(1 - p) * 12}px)`;
          h.style.transform = `translateY(${(1 - p) * 26}px)`;
        });
        $$('.lc', el).forEach((c, i) => {
          const on = k === i || k === 3;
          c.style.background = on ? '#1d1d1f' : '#f2f2f7';
          c.style.color = on ? '#fff' : '#6e6e73';
          c.style.transform = `scale(${k === i ? 1.08 : 1})`;
        });
        const p = ap(t, S(s, 3) - 0.2, 0.6);
        $('#ok', el).style.opacity = p;
        $('#ok', el).style.transform = `scale(${lerp(0.92, 1, p)})`;
      },
    },

    'b-intro': { brand: true, build: () => introCard('Pharmacy, in your language.'), update: introUpdate },

    'b-proof': {
      brand: true,
      build: () => `${glowBg('rgba(99,102,241,.22)', 'rgba(236,72,153,.12)')}
        <div id="ph" class="abs" style="left:1010px;top:120px;perspective:2400px">${phone('dev', SHOT('m-lesson.png'), 400)}</div>
        <div class="abs" style="left:150px;top:300px;display:flex;flex-direction:column;gap:20px">
          ${['Read in your language.', 'Listen, with voice.', 'Practise on your phone.', 'Instant feedback.'].map((x) => `<p class="ft" style="${H}font-size:68px;line-height:1.05;color:#fff;opacity:0">${x}</p>`).join('')}
        </div>
        <div id="ok" class="abs" style="left:1450px;top:660px;opacity:0;padding:22px 34px;border-radius:24px;background:#dcfce7;color:#166534;${H}letter-spacing:-.01em;font-size:40px;box-shadow:0 30px 60px rgba(0,0,0,.4)">✓ Correct!</div>
        <div id="ls" class="abs" style="left:1440px;top:300px;opacity:0;padding:20px 30px;border-radius:24px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.25);color:#fff;${H}letter-spacing:-.01em;font-size:36px;backdrop-filter:blur(10px)">🎧 Listen in ಕನ್ನಡ · हिन्दी</div>
        <h1 id="free" class="abs" style="${H}left:1180px;top:330px;font-size:300px;line-height:1;opacity:0"><span class="gl">Free.</span></h1>`,
      update: (el, t, s) => {
        const p = ap(t, s.start, 1.4);
        const out = ap(t, S(s, 1) - 0.2, 0.8);
        $('#dev', el).style.transform = `rotateY(${lerp(-32, -8, p) - out * 10}deg) rotateX(${lerp(14, 4, p)}deg) translateY(${(1 - p) * 120 + Math.sin(t * 1.2) * 8}px)`;
        $('#ph', el).style.opacity = ap(t, s.start, 0.6);
        $('#ph', el).style.transform = `translateX(${-out * 660}px)`;
        $$('.ft', el).forEach((f, i) => {
          const q = ap(t, S(s, 0) + (i * dur(s, 0)) / 4, 0.45);
          f.style.opacity = q * (1 - out);
          f.style.filter = `blur(${(1 - q) * 10}px)`;
        });
        pop($('#ls', el), ap(t, S(s, 0) + dur(s, 0) * 0.25, 0.5) * (1 - out));
        pop($('#ok', el), ap(t, S(s, 0) + dur(s, 0) * 0.75, 0.5) * (1 - out));
        const f = $('#free', el), q = ap(t, S(s, 1), 0.6);
        f.style.opacity = q;
        f.style.transform = `scale(${lerp(1.15, 1, q)})`;
        f.style.filter = `blur(${(1 - q) * 16}px)`;
      },
    },

    'b-promise': {
      brand: true,
      build: () => `${glowBg('rgba(45,212,191,.18)', 'rgba(99,102,241,.22)')}
        <p id="hd" class="abs" style="${H}left:0;right:0;top:200px;text-align:center;font-size:84px;color:#fff">${words('Every semester. In your language.')}</p>
        ${track(560, true)}
        ${SEMS.map(([name, code], i) => (name ? `<div class="abs lbl2" data-i="${i}" style="left:${200 + i * (1520 / 7)}px;top:${i % 2 ? 660 : 400}px;transform:translateX(-50%);text-align:center;opacity:0;white-space:nowrap">
          <p style="${H}letter-spacing:-.01em;font-size:30px;color:#fff">${name}</p><p style="margin-top:4px;font-family:var(--mono);font-size:20px;color:#a1a1aa">${code}</p></div>` : '')).join('')}
        <div id="you" class="abs" style="left:${200 - 30}px;top:${560 - 32}px;width:60px;height:60px;border-radius:18px;background:linear-gradient(140deg,#6366f1,#2dd4bf);box-shadow:0 0 50px rgba(99,102,241,.8);display:grid;place-items:center;color:#fff;font-family:var(--mono);font-weight:700;font-size:22px">&lt;/&gt;</div>`,
      update: (el, t, s) => {
        const d = dur(s, 0);
        const p = clamp((t - S(s, 0) - 0.3) / Math.max(1, d - 0.6));
        lightTrack(el, t, S(s, 0) + 0.3, d - 0.6);
        $('#you', el).style.transform = `translateX(${p * 1520}px)`;
        $$('.lbl2', el).forEach((n) => {
          const i = Number(n.dataset.i);
          const q = clamp((p - i / 7) * 8 + 0.3);
          n.style.opacity = q;
        });
        reveal($('#hd', el), t, E(s, 0) - 0.6, 0.12);
      },
    },

    'b-end': {
      brand: true,
      build: () => endCard('Campus Champ', 'Pharmacy, in your language.', 'Start free with Python →', 'campuschamp.in', 'Scan to start'),
      update: endUpdate,
    },

    // ================= colleges film =================
    'c-hook': {
      subsOnly: true,
      build: () => {
        const SUB = [['BP101T', 'Sem I', 'Basics of Python Programming'], ['BP201T', 'Sem II', 'Biostatistics & Data Analytics'], ['BP212P', 'Sem II', 'Fundamentals of Computer Operations'], ['BP301T', 'Sem III', 'Machine Learning'], ['BP604T', 'Sem VI', 'AI Applications'], ['BP610P', 'Sem VI', 'Computer-Aided Drug Design'], ['BP703T', 'Sem VII', 'AI in Clinical Applications'], ['BP801T', 'Sem VIII', 'Ethical AI in Pharmacy']];
        return `${glowBg()}
          <h1 id="h1" class="abs" style="${H}left:0;right:0;top:380px;text-align:center;font-size:120px;line-height:1.08;color:#fff;transform-origin:50% 0">${words('AI is now part of every year of B.Pharm.')}</h1>
          <div class="abs" style="left:150px;right:150px;top:330px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">
            ${SUB.map(([c, sem, name]) => `<div class="sc" style="opacity:0;height:200px;border-radius:28px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);padding:24px 26px;display:flex;flex-direction:column">
              <div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-weight:700;font-size:26px;background:linear-gradient(90deg,#a5b4fc,#5eead4);-webkit-background-clip:text;color:transparent">${c}</span><span style="font-family:var(--head);font-weight:700;font-size:22px;color:#a1a1aa">${sem}</span></div>
              <p style="margin-top:auto;${H}letter-spacing:-.01em;font-size:31px;line-height:1.15;color:#fff">${name}</p></div>`).join('')}
          </div>
          <h1 id="q" class="abs" style="${H}left:150px;right:150px;top:400px;text-align:center;font-size:110px;line-height:1.08;color:#fff">${words('Is your department ready?', 'w2')}</h1>`;
      },
      update: (el, t, s) => {
        reveal($('#h1', el), t, S(s, 0) + 0.1, 0.16);
        const up = ap(t, S(s, 1), 0.7);
        $('#h1', el).style.transform = `translateY(${-up * 250}px) scale(${1 - up * 0.48})`;
        const qd = ap(t, S(s, 2), 0.6);
        $('#h1', el).style.opacity = 1 - qd;
        $$('.sc', el).forEach((c, i) => {
          const q = ap(t, S(s, 1) + 0.4 + (i * (dur(s, 1) - 0.6)) / 8, 0.45);
          c.style.opacity = q * (1 - 0.82 * qd);
          c.style.transform = `translateY(${(1 - q) * 40}px) scale(${lerp(0.94, 1, q)})`;
          c.style.filter = `blur(${qd * 6}px)`;
        });
        $$('.w2', el).forEach((w, i) => {
          const p = ap(t, S(s, 2) + 0.2 + i * 0.16, 0.5);
          w.style.opacity = p;
          w.style.filter = `blur(${(1 - p) * 14}px)`;
        });
      },
    },

    'c-gap': {
      subsOnly: true,
      build: () => `<div class="abs" style="inset:0;background:radial-gradient(circle at 30% 40%,#1e1b4b,#000 70%)"></div>
        <div id="fac" class="abs" style="left:170px;top:190px;width:700px;opacity:0;border-radius:36px;background:#fff;padding:44px 48px;box-shadow:0 40px 90px rgba(0,0,0,.5)">
          <div style="display:flex;align-items:center;gap:22px"><span style="width:96px;height:96px;border-radius:50%;background:#eef2ff;display:grid;place-items:center;font-size:56px">👩‍🏫</span><div><p style="${H}letter-spacing:-.01em;font-size:40px;color:#1d1d1f">Pharmacy faculty</p><p style="font-size:26px;color:#6e6e73">Trained for</p></div></div>
          ${['Pharmaceutics', 'Pharmacology', 'Pharmacognosy', 'Programming & AI'].map((x, i) => `<div class="sk" style="margin-top:${i ? 14 : 30}px;display:flex;justify-content:space-between;align-items:center;padding:18px 24px;border-radius:18px;background:${i === 3 ? '#fff1f2' : '#f5f5f7'};opacity:0"><span style="${H}letter-spacing:-.01em;font-size:34px;color:${i === 3 ? '#be123c' : '#1d1d1f'}">${x}</span><b style="font-size:38px;color:${i === 3 ? '#e11d48' : '#16a34a'}">${i === 3 ? '?' : '✓'}</b></div>`).join('')}
        </div>
        <div id="stu" class="abs" style="left:1040px;top:260px;width:720px;opacity:0;text-align:center">
          <span style="display:inline-grid;width:150px;height:150px;border-radius:50%;background:rgba(255,255,255,.1);place-items:center;font-size:90px">🧑‍🎓</span>
          <div style="margin-top:34px;display:flex;justify-content:center;gap:18px">${['ಕನ್ನಡ', 'हिन्दी', 'English'].map((l) => `<span class="lb" style="opacity:0;${H}letter-spacing:-.01em;font-size:44px;color:#1d1d1f;background:#fff;border-radius:26px 26px 26px 8px;padding:18px 30px">${l}</span>`).join('')}</div>
          <p style="margin-top:36px;${H}letter-spacing:-.01em;font-size:44px;color:#d4d4d8">Learns best in their own language</p>
        </div>`,
      update: (el, t, s) => {
        show($('#fac', el), ap(t, S(s, 0) - 0.2, 0.6), 40, 0.96);
        $$('.sk', el).forEach((k, i) => (k.style.opacity = ap(t, S(s, 0) + 0.3 + i * (dur(s, 0) / 5), 0.4)));
        const last = $$('.sk', el)[3];
        if (t > S(s, 0) + dur(s, 0) * 0.6) last.style.transform = `scale(${1 + 0.03 * Math.sin(t * 6)})`;
        show($('#stu', el), ap(t, S(s, 1) - 0.1, 0.6), 30, 0.96);
        $$('.lb', el).forEach((b, i) => pop(b, ap(t, S(s, 1) + 0.4 + i * 0.3, 0.5)));
      },
    },

    'c-intro': {
      brand: true,
      build: () => introCard('Your partner for the entire AI pathway.', `<p id="i3" style="${H}margin-top:10px;font-size:110px;line-height:1;opacity:0"><span class="gl">for Colleges</span></p>`),
      update: introUpdate,
    },

    'c-solve': {
      subsOnly: true,
      build: () => `${glowBg()}
        <div id="p0" class="abs" style="left:0;right:0;top:330px;text-align:center">
          <h1 style="${H}font-size:110px;line-height:1.05;color:#fff">${words('One partner.')}<br>${words('The entire AI pathway.')}</h1>
          <p id="only" style="margin:34px auto 0;width:max-content;opacity:0;font-family:var(--head);font-weight:700;font-size:36px;color:#fde68a;padding:14px 30px;border-radius:999px;border:1.5px solid rgba(253,230,138,.5);background:rgba(253,230,138,.1)">Built only for pharmacy</p>
        </div>
        <div id="p1" class="abs" style="inset:0;opacity:0">
          <p class="abs" style="${H}left:0;right:0;top:220px;text-align:center;font-size:72px;color:#fff">Mapped to the PCI syllabus, unit by unit.</p>
          ${track(560, true)}
          ${SEMS.map(([name, code], i) => (name ? `<div class="abs" style="left:${200 + i * (1520 / 7)}px;top:${i % 2 ? 660 : 400}px;transform:translateX(-50%);text-align:center;white-space:nowrap"><p style="font-family:var(--mono);font-weight:700;font-size:24px;color:${i === 0 ? '#5eead4' : '#a1a1aa'}">${code}</p></div>` : '')).join('')}
          <div id="live" class="abs" style="left:${200 - 60}px;top:330px;padding:10px 22px;border-radius:999px;background:#22c55e;color:#052e16;font-family:var(--head);font-weight:800;font-size:26px;box-shadow:0 0 40px rgba(34,197,94,.6)">● Live today</div>
          <p id="arr" class="abs" style="${H}left:0;right:0;top:800px;text-align:center;font-size:44px;color:#a1a1aa;opacity:0">Arriving semester by semester, as your batches move up.</p>
        </div>
        <div id="p2" class="abs" style="inset:0;opacity:0">
          <div id="ph" class="abs" style="left:250px;top:110px;perspective:2400px">${phone('dev', SHOT('m-lesson.png'), 380)}</div>
          <div class="abs" style="left:900px;top:250px;display:flex;flex-direction:column;gap:22px">
            <div style="display:flex;gap:16px">${['ಕನ್ನಡ', 'हिन्दी', 'English'].map((l) => `<span class="lg" style="opacity:0;${H}letter-spacing:-.01em;font-size:48px;color:#fff;padding:16px 34px;border-radius:999px;background:rgba(255,255,255,.1);border:1.5px solid rgba(255,255,255,.25)">${l}</span>`).join('')}</div>
            ${['Voice in every lesson', 'Video lessons', 'Practice on any phone', 'No lab needed'].map((x) => `<p class="ft" style="${H}font-size:66px;line-height:1.08;color:#fff;opacity:0">${x}</p>`).join('')}
          </div>
        </div>`,
      update: (el, t, s) => {
        const a = ap(t, S(s, 1) - 0.3, 0.5), b = ap(t, S(s, 2) - 0.3, 0.5);
        $('#p0', el).style.opacity = 1 - a;
        reveal($('#p0', el), t, S(s, 0) + 0.2, 0.16);
        show($('#only', el), ap(t, S(s, 0) + dur(s, 0) * 0.6, 0.5), 10, 0.95);
        $('#p1', el).style.opacity = a * (1 - b);
        lightTrack($('#p1', el), t, S(s, 1) + 0.6, dur(s, 1) - 1.2);
        $('#live', el).style.transform = `scale(${1 + 0.04 * Math.sin(t * 4)})`;
        show($('#arr', el), ap(t, S(s, 1) + dur(s, 1) * 0.45, 0.6), 12, 1);
        $('#p2', el).style.opacity = b;
        const p = ap(t, S(s, 2) - 0.3, 1.2);
        $('#dev', el).style.transform = `rotateY(${lerp(28, 10, p)}deg) rotateX(${lerp(12, 4, p)}deg) translateY(${(1 - p) * 100 + Math.sin(t * 1.2) * 8}px)`;
        $$('.lg', el).forEach((g, i) => pop(g, ap(t, S(s, 2) + 0.2 + i * 0.25, 0.4)));
        $$('.ft', el).forEach((f, i) => {
          const q = ap(t, S(s, 2) + dur(s, 2) * (0.3 + i * 0.16), 0.45);
          f.style.opacity = q;
          f.style.filter = `blur(${(1 - q) * 10}px)`;
        });
      },
    },

    'c-teacher': {
      subsOnly: true,
      build: () => `<div class="layer brand"></div>
        <div id="qr" class="abs" style="left:240px;top:200px;opacity:0;text-align:center">
          <div style="padding:30px;border-radius:40px;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.1)"><img src="${T().qr}" style="width:340px;height:340px"/></div>
          <p style="margin-top:26px;font-family:var(--mono);font-weight:700;font-size:30px;color:#4f46e5">campuschamp.in/join/BP1A7C</p>
        </div>
        <div id="h" class="abs" style="left:780px;top:280px;opacity:0">
          <p style="${H}font-size:96px;line-height:1.05;color:#1d1d1f">One class.<br>One link.</p>
          <p style="${H}margin-top:24px;font-size:52px;line-height:1.1"><span class="grad">Ready in a minute.</span></p>
        </div>
        <div id="lp" class="abs" style="left:410px;top:160px;opacity:0;perspective:2400px">${laptop('lap', SHOT('dashboard.png'), 1100)}</div>
        <div id="wa" class="abs" style="left:1190px;top:560px;opacity:0;width:560px;border-radius:26px 26px 26px 8px;background:#dcf8c6;padding:24px 28px;box-shadow:0 30px 70px rgba(0,0,0,.25)">
          <p style="font-family:var(--head);font-weight:800;font-size:24px;color:#128c7e">WhatsApp · Section A</p>
          <p style="margin-top:8px;font-size:32px;line-height:1.35;color:#111b21">📚 Reminder: please finish Lesson 1.3 before Friday's class.</p>
        </div>`,
      update: (el, t, s) => {
        const out = ap(t, S(s, 1) - 0.3, 0.6);
        show($('#qr', el), ap(t, S(s, 0) - 0.1, 0.6) * (1 - out), 30, 0.95);
        show($('#h', el), ap(t, S(s, 0) + 0.5, 0.6) * (1 - out), 20, 1);
        const p = ap(t, S(s, 1) - 0.2, 1.2);
        $('#lp', el).style.opacity = p;
        $('#lap', el).style.transform = `rotateX(${lerp(24, 6, p)}deg) translateY(${(1 - p) * 160}px) scale(${lerp(0.9, 1, p) + ap(t, S(s, 2), 3) * 0.04})`;
        pop($('#wa', el), ap(t, S(s, 2) + 0.2, 0.6));
      },
    },

    'c-principal': {
      subsOnly: true,
      build: () => `${glowBg('rgba(124,92,255,.3)', 'rgba(45,212,191,.14)')}
        <div class="abs" style="left:230px;top:90px;perspective:2400px"><img id="rep" src="${SHOT('report.png')}" style="width:640px;border-radius:30px;box-shadow:0 60px 120px rgba(0,0,0,.6)"/></div>
        <div class="abs" style="left:1050px;top:250px;display:flex;flex-direction:column;gap:18px">
          <p id="hd" style="${H}font-size:80px;line-height:1.05;color:#fff;opacity:0">A clear report.<br><span class="gl">Every term.</span></p>
          ${['Participation', 'Progress, lesson by lesson', 'Quiz scores', '📄 PDF for your records'].map((x) => `<p class="ft" style="${H}letter-spacing:-.01em;font-size:44px;color:#d4d4d8;opacity:0">${x}</p>`).join('')}
        </div>`,
      update: (el, t, s) => {
        const p = ap(t, s.start + 0.1, 1.4);
        const r = $('#rep', el);
        r.style.opacity = p;
        r.style.transform = `rotateY(${lerp(-26, -10, p)}deg) rotateX(${lerp(14, 4, p)}deg) translateY(${(1 - p) * 120 + Math.sin(t * 1.1) * 8}px)`;
        show($('#hd', el), ap(t, S(s, 0) - 0.2, 0.6), 20, 1);
        $$('.ft', el).forEach((f, i) => {
          const q = ap(t, S(s, 0) + dur(s, 0) * (0.25 + i * 0.16), 0.45);
          f.style.opacity = q;
          f.style.filter = `blur(${(1 - q) * 10}px)`;
        });
      },
    },

    'c-cta': {
      subsOnly: true,
      build: () => `${glowBg()}
        <div class="abs" style="left:0;right:0;top:260px;text-align:center">
          <h1 id="h" style="${H}font-size:140px;line-height:1.02;color:#fff">${words('Make your college')}</h1>
          <h1 id="h2" style="${H}font-size:140px;line-height:1.1;opacity:0"><span class="gl">AI-ready.</span></h1>
          <p id="sb" style="${H}margin-top:18px;font-size:58px;color:#a1a1aa;opacity:0">One semester at a time.</p>
        </div>
        <div id="chips" class="abs" style="left:0;right:0;top:720px;display:flex;justify-content:center;gap:22px">
          <span class="ch" style="opacity:0;font-family:var(--head);font-weight:700;font-size:38px;color:#d1fae5;padding:18px 34px;border-radius:999px;background:rgba(34,197,94,.15);border:1.5px solid #22c55e">Free for students &amp; teachers</span>
          <span class="ch" style="opacity:0;font-family:var(--head);font-weight:700;font-size:38px;color:#fef3c7;padding:18px 34px;border-radius:999px;background:rgba(251,191,36,.14);border:1.5px solid #fbbf24">Pilot 2026-27 · limited colleges</span>
        </div>`,
      update: (el, t, s) => {
        reveal($('#h', el), t, S(s, 0) + 0.1, 0.18);
        show($('#h2', el), ap(t, S(s, 0) + 0.75, 0.6), 20, 0.96);
        show($('#sb', el), ap(t, S(s, 0) + dur(s, 0) * 0.55, 0.6), 14, 1);
        $$('.ch', el).forEach((c, i) => pop(c, ap(t, S(s, 1) + 0.3 + i * dur(s, 1) * 0.5, 0.5)));
        const up = ap(t, S(s, 2), 0.6);
        $('#chips', el).style.transform = `translateY(${-up * 20}px)`;
      },
    },

    'c-end': {
      brand: true,
      build: () => endCard('Campus Champ for Colleges', 'Your AI pathway partner. Sem 1 to 8.', 'Book a 20-minute walkthrough →', 'campuschamp.in/colleges', 'Scan to book'),
      update: endUpdate,
    },
  };
});
