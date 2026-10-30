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
      build: () => {
        const F = [['In your language, with voice.', 'f-narrator.png'], ['Animated explanations.', 'f-animate.png'], ['Video lessons.', 'VIDEO'], ['Real code. Instant feedback.', 'f-check.png'], ['A quiz after every lesson.', 'f-quiz.png'], ['Important questions, every unit.', 'f-iq.png']];
        return `${glowBg('rgba(99,102,241,.22)', 'rgba(236,72,153,.12)')}
          ${F.map(([n], i) => `<p class="fn abs" style="${H}left:150px;width:860px;top:50%;transform:translateY(-50%);font-size:96px;line-height:1.05;color:#fff;opacity:0">${n}</p>`).join('')}
          <div id="ph" class="abs" style="left:1180px;top:110px;perspective:2400px">
            <div id="dev" style="width:400px;height:864px;border-radius:64px;background:#0b0b0f;padding:14px;box-shadow:0 60px 120px rgba(0,0,0,.6),0 0 0 2px #2a2a33 inset">
              <div style="position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background:#fff">
                ${F.map(([, img], i) => (img === 'VIDEO'
                  ? `<div class="scr" style="position:absolute;inset:0;opacity:0;background:#0f172a;display:flex;flex-direction:column;justify-content:center;padding:20px"><img src="../../media/bp101t/1-1/kn/ep1.jpg" style="width:100%;border-radius:14px"/><p style="margin-top:16px;font-family:var(--head);font-weight:800;font-size:22px;color:#fff">Episode 1 · Program ಅಂದ್ರೆ ಏನು?</p></div>`
                  : `<img class="scr" src="${SHOT(img)}" style="position:absolute;inset:0;width:100%;opacity:0"/>`)).join('')}
                <div style="position:absolute;left:50%;top:12px;width:120px;height:30px;border-radius:99px;background:#000;transform:translateX(-50%)"></div>
              </div>
            </div>
          </div>
          <h1 id="xr" class="abs" style="${H}left:0;right:0;top:360px;text-align:center;font-size:230px;line-height:1;opacity:0"><span class="gl">Exam-ready.</span></h1>`;
      },
      update: (el, t, s) => {
        // four features over the first sentence, two over the second, then "Exam-ready."
        let k = -1;
        if (t >= S(s, 0) - 0.2) k = Math.min(3, Math.floor(((t - S(s, 0) + 0.2) / dur(s, 0)) * 4));
        if (t >= S(s, 1) - 0.2) k = 4 + Math.min(1, Math.floor(((t - S(s, 1) + 0.2) / dur(s, 1)) * 2));
        const fin = ap(t, E(s, 1) - 0.1, 0.6);
        $$('.fn', el).forEach((f, i) => { f.style.opacity = i === k ? 1 - fin : 0; f.style.filter = `blur(${i === k ? 0 : 12}px)`; });
        $$('.scr', el).forEach((sc, i) => (sc.style.opacity = i === k ? 1 : 0));
        const p = ap(t, s.start, 1.2);
        $('#ph', el).style.opacity = ap(t, s.start, 0.5) * (1 - fin);
        $('#dev', el).style.transform = `rotateY(${lerp(-30, -12, p) + Math.sin(t * 0.8) * 3}deg) rotateX(${lerp(12, 4, p)}deg) translateY(${(1 - p) * 100 + Math.sin(t * 1.2) * 8}px)`;
        const x = $('#xr', el);
        x.style.opacity = fin;
        x.style.filter = `blur(${(1 - fin) * 16}px)`;
        x.style.transform = `scale(${lerp(1.12, 1, fin)})`;
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
      build: () => endCard('Campus Champ', 'Pharmacy, in your language.', 'Start with Python →', 'campuschamp.in', 'Scan to start'),
      update: endUpdate,
    },

    // ================= colleges film =================
    'c-hook': {
      subsOnly: true,
      build: () => {
        const SUB = [['BP101T', 'Sem I', 'Basics of Python Programming'], ['BP201T', 'Sem II', 'Biostatistics & Data Analytics'], ['BP212P', 'Sem II', 'Fundamentals of Computer Operations'], ['BP301T', 'Sem III', 'Machine Learning'], ['BP604T', 'Sem VI', 'AI Applications'], ['BP610P', 'Sem VI', 'Computer-Aided Drug Design'], ['BP703T', 'Sem VII', 'AI in Clinical Applications'], ['BP801T', 'Sem VIII', 'Ethical AI in Pharmacy']];
        return `${glowBg()}
          <p id="k" class="abs" style="left:0;right:0;top:300px;text-align:center;font-family:var(--head);font-weight:700;font-size:34px;color:#a5b4fc;opacity:0">PCI · NEP 2020 · from 2026-27</p>
          <h1 id="h1" class="abs" style="${H}left:0;right:0;top:380px;text-align:center;font-size:124px;line-height:1.08;color:#fff;transform-origin:50% 0">${words('AI is now in every year of B.Pharm.')}</h1>
          <div class="abs" style="left:150px;right:150px;top:330px;display:grid;grid-template-columns:repeat(4,1fr);gap:22px">
            ${SUB.map(([c, sem, name]) => `<div class="sc" style="opacity:0;height:200px;border-radius:28px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);padding:24px 26px;display:flex;flex-direction:column">
              <div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:var(--mono);font-weight:700;font-size:26px;background:linear-gradient(90deg,#a5b4fc,#5eead4);-webkit-background-clip:text;color:transparent">${c}</span><span style="font-family:var(--head);font-weight:700;font-size:22px;color:#a1a1aa">${sem}</span></div>
              <p style="margin-top:auto;${H}letter-spacing:-.01em;font-size:31px;line-height:1.15;color:#fff">${name}</p></div>`).join('')}
          </div>`;
      },
      update: (el, t, s) => {
        show($('#k', el), ap(t, S(s, 0), 0.6) * (1 - ap(t, S(s, 1), 0.4)), 10, 1);
        reveal($('#h1', el), t, S(s, 0) + 0.3, 0.16);
        const up = ap(t, S(s, 1), 0.7);
        $('#h1', el).style.transform = `translateY(${-up * 250}px) scale(${1 - up * 0.5})`;
        $$('.sc', el).forEach((c, i) => {
          const q = ap(t, S(s, 1) + 0.4 + (i * (dur(s, 1) - 0.6)) / 8, 0.45);
          c.style.opacity = q;
          c.style.transform = `translateY(${(1 - q) * 40}px) scale(${lerp(0.94, 1, q)})`;
        });
      },
    },

    'c-pains': {
      subsOnly: true,
      build: () => {
        const Q = [['👩‍🏫', 'Who will teach it?', 'Faculty trained in pharmaceutics, not programming'], ['🖥️', 'Where will they practise?', '30 hours a semester. Limited labs.'], ['🧑‍🎓', 'Will they keep up?', 'Biology background. Second language.'], ['📋', 'How will you show it to NAAC?', 'Evidence that real learning happened']];
        return `<div class="abs" style="inset:0;background:radial-gradient(circle at 50% 40%,#2a1030,#000 70%)"></div>
          <h1 id="h" class="abs" style="${H}left:0;right:0;top:400px;text-align:center;font-size:120px;color:#fff;transform-origin:50% 0">${words('Hard questions.')}</h1>
          <div class="abs" style="left:150px;right:150px;top:250px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
            ${Q.map(([ic, q, f]) => `<div class="pq" style="opacity:0;height:260px;border-radius:34px;background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.12);padding:34px 40px;display:flex;flex-direction:column">
              <div style="display:flex;align-items:center;gap:22px"><span style="font-size:56px">${ic}</span><span style="${H}font-size:54px;color:#fff;line-height:1.05">${q}</span></div>
              <p style="margin-top:auto;font-family:var(--head);font-weight:600;font-size:34px;color:#a1a1aa">${f}</p></div>`).join('')}
          </div>`;
      },
      update: (el, t, s) => {
        reveal($('#h', el), t, S(s, 0) + 0.2, 0.2);
        const up = ap(t, S(s, 1) - 0.2, 0.6);
        $('#h', el).style.transform = `translateY(${-up * 300}px) scale(${1 - up * 0.55})`;
        $$('.pq', el).forEach((c, i) => {
          const q = ap(t, S(s, i + 1) - 0.1, 0.5);
          const on = t >= S(s, i + 1) - 0.1 && t < S(s, i + 2) - 0.1;
          c.style.opacity = q * (on ? 1 : 0.45);
          c.style.borderColor = on ? '#fb7185' : 'rgba(255,255,255,.12)';
          c.style.boxShadow = on ? '0 0 60px rgba(251,113,133,.25)' : 'none';
          c.style.transform = `scale(${on ? 1.02 : 1}) translateY(${(1 - q) * 30}px)`;
        });
      },
    },

    'c-book': {
      subsOnly: true,
      build: () => {
        const code = ['def dose(w):', '    return w * 15', '', 'for i in range(3):', '    print(dose(60))', '', '# Bateman equation', 'c = d*ka/(v*(ka-k))'];
        return `${glowBg('rgba(120,113,108,.25)', 'rgba(251,113,133,.12)')}
          <h1 id="h" class="abs" style="${H}left:0;right:0;top:110px;text-align:center;font-size:84px;color:#fff">${words("Coding can't be learned by reading.")}</h1>
          <div id="bk" class="abs" style="left:460px;top:290px;width:1000px;height:560px;display:flex;filter:drop-shadow(0 40px 60px rgba(0,0,0,.6))">
            ${[0, 1].map((p) => `<div style="flex:1;background:#f5efe0;border-radius:${p ? '6px 22px 22px 6px' : '22px 6px 6px 22px'};padding:44px 46px;font-family:var(--mono);font-size:28px;line-height:1.75;color:#44403c;box-shadow:inset ${p ? 18 : -18}px 0 30px rgba(0,0,0,.12)">
              <p style="font-family:var(--head);font-weight:800;font-size:26px;color:#78716c;margin-bottom:18px">Chapter ${p + 3} · ${p ? 'Pharmacokinetics' : 'Functions'}</p>${code.slice(p * 4, p * 4 + 4).map((l) => `<div style="white-space:pre">${l || '&nbsp;'}</div>`).join('')}</div>`).join('')}
          </div>
          <div id="s1" class="abs stamp" style="left:520px;top:420px;transform:rotate(-8deg)">✕ Can't run code</div>
          <div id="s2" class="abs stamp" style="left:1000px;top:520px;transform:rotate(6deg)">✕ No feedback</div>
          <div id="s3" class="abs" style="left:0;right:0;top:880px;text-align:center;opacity:0;${H}font-size:56px;color:#fda4af">Memorise → Exam → Forget</div>
          <div id="s4" class="abs stamp" style="left:740px;top:330px;transform:rotate(-4deg);color:#fbbf24;border-color:#fbbf24">⌛ Outdated</div>
          <style>.stamp{opacity:0;padding:14px 30px;border:5px solid #fb7185;border-radius:14px;color:#fb7185;font-family:var(--head);font-weight:800;font-size:48px;background:rgba(0,0,0,.55)}</style>`;
      },
      update: (el, t, s) => {
        reveal($('#h', el), t, S(s, 0) + dur(s, 0) * 0.45, 0.14);
        show($('#bk', el), ap(t, S(s, 0) - 0.2, 0.7), 40, 0.95);
        pop($('#s1', el), ap(t, S(s, 1) + dur(s, 1) * 0.12, 0.35));
        pop($('#s2', el), ap(t, S(s, 1) + dur(s, 1) * 0.35, 0.35));
        show($('#s3', el), ap(t, S(s, 1) + dur(s, 1) * 0.62, 0.5), 15, 1);
        const old = ap(t, S(s, 2), 1.2);
        $('#bk', el).style.filter = `drop-shadow(0 40px 60px rgba(0,0,0,.6)) sepia(${old * 0.8}) brightness(${1 - old * 0.35})`;
        pop($('#s4', el), ap(t, S(s, 2) + dur(s, 2) * 0.5, 0.35));
      },
    },

    'c-blend': {
      subsOnly: true,
      build: () => {
        const N = [['👩‍🏫', 'Classroom'], ['📱', 'Practice'], ['✓', 'Instant feedback'], ['📊', 'Teacher insight']];
        const cx = 1300, cy = 560, r = 270;
        return `<div class="layer brand"></div>
          <div class="abs" style="left:130px;top:300px;width:700px">
            <h1 id="h" style="${H}font-size:120px;line-height:1"><span class="grad">Blended</span><br><span style="color:#1d1d1f">learning.</span></h1>
            <p id="sb" style="${H}margin-top:30px;font-size:46px;line-height:1.2;color:#6e6e73;opacity:0">Teacher in class.<br>Guided practice in between.</p>
            <p id="nep" style="margin-top:40px;opacity:0;width:max-content;font-family:var(--head);font-weight:800;font-size:32px;color:#4f46e5;padding:14px 28px;border-radius:999px;background:#eef2ff">NEP 2020 encourages blended learning</p>
          </div>
          <svg class="art" viewBox="0 0 1920 1080"><circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#e5e7eb" stroke-width="6"/><circle id="arc" cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="url(#bl)" stroke-width="10" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 ${cx} ${cy})"/><defs><linearGradient id="bl"><stop offset="0" stop-color="#6366f1"/><stop offset="1" stop-color="#2dd4bf"/></linearGradient></defs></svg>
          ${N.map(([ic, l], i) => { const a = -Math.PI / 2 + (i * Math.PI) / 2; return `<div class="abs nd" style="left:${cx + Math.cos(a) * r - 100}px;top:${cy + Math.sin(a) * r - 80}px;width:200px;text-align:center;opacity:0">
            <div style="width:120px;height:120px;margin:0 auto;border-radius:36px;background:#fff;box-shadow:0 20px 50px rgba(0,0,0,.1);display:grid;place-items:center;font-size:58px;color:#16a34a;font-weight:800">${ic}</div>
            <p style="margin-top:12px;font-family:var(--head);font-weight:800;font-size:28px;color:#1d1d1f">${l}</p></div>`; }).join('')}
          <div id="dot" class="abs" style="left:${cx - 16}px;top:${cy - r - 16}px;width:32px;height:32px;border-radius:50%;background:#6366f1;box-shadow:0 0 30px #6366f1;opacity:0"></div>`;
      },
      update: (el, t, s) => {
        show($('#h', el), ap(t, S(s, 0), 0.7), 30, 0.96);
        show($('#sb', el), ap(t, S(s, 0) + dur(s, 0) * 0.5, 0.6), 15, 1);
        $$('.nd', el).forEach((n, i) => show(n, ap(t, S(s, 0) + 0.6 + i * 0.3, 0.5), 20, 0.85));
        const p = clamp((t - S(s, 1)) / Math.max(1, dur(s, 1)));
        $('#arc', el).setAttribute('stroke-dashoffset', String(1 - p));
        const a = -Math.PI / 2 + p * Math.PI * 2;
        const d = $('#dot', el);
        d.style.opacity = t >= S(s, 1) ? 1 : 0;
        d.style.transform = `translate(${Math.cos(a) * 270}px,${Math.sin(a) * 270 + 270}px)`;
        show($('#nep', el), ap(t, S(s, 2), 0.5), 12, 0.95);
      },
    },

    'c-intro': {
      brand: true,
      build: () => introCard('', `<p id="i3" style="${H}margin-top:10px;font-size:110px;line-height:1;opacity:0"><span class="gl">for Colleges</span></p>`) + `
        <div id="first" class="abs" style="left:0;right:0;top:690px;text-align:center;opacity:0">
          <p style="${H}font-size:96px;line-height:1"><span class="gl">India's first</span></p>
          <p style="${H}margin-top:18px;font-size:44px;color:#e4e4e7;letter-spacing:-.01em">multilingual blended-learning platform for pharmacy's AI curriculum</p>
        </div>`,
      update: (el, t, s) => {
        introUpdate(el, t, s);
        const up = ap(t, S(s, 1) - 0.3, 0.7);
        $('#i1', el).parentElement.style.transform = `translateY(${-up * 170}px)`;
        const f = $('#first', el), q = ap(t, S(s, 1), 0.7);
        f.style.opacity = q;
        f.style.filter = `blur(${(1 - q) * 14}px)`;
        f.style.transform = `scale(${lerp(1.08, 1, q)})`;
      },
    },

    'c-trust': {
      subsOnly: true,
      build: () => `${glowBg('rgba(45,212,191,.18)', 'rgba(99,102,241,.25)')}
        <div id="p0" class="abs" style="inset:0">
          <h1 class="abs" style="${H}left:0;right:0;top:170px;text-align:center;font-size:88px;color:#fff">${words('Built by people who know both.')}</h1>
          <div class="abs" style="left:0;right:0;top:420px;display:flex;justify-content:center;align-items:center;gap:40px">
            <div class="cr" style="opacity:0;width:620px;padding:40px 44px;border-radius:36px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18)"><span style="font-size:70px">💊</span><p style="${H}margin-top:16px;font-size:52px;color:#fff;line-height:1.05">Pharmacy educators</p></div>
            <span class="cr" style="opacity:0;${H}font-size:90px;color:#71717a">+</span>
            <div class="cr" style="opacity:0;width:620px;padding:40px 44px;border-radius:36px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18)"><span style="font-size:70px">🤖</span><p style="${H}margin-top:16px;font-size:52px;color:#fff;line-height:1.05">Engineers from leading AI companies</p></div>
          </div>
        </div>
        <div id="p1" class="abs" style="inset:0;opacity:0">
          <p class="abs" style="left:150px;top:180px;font-family:var(--mono);font-weight:700;font-size:34px;color:#5eead4">BP101T · Official PCI syllabus</p>
          <div class="abs" style="left:150px;top:250px;width:860px;display:flex;flex-direction:column;gap:16px">
            ${['Introduction to Python programming', 'Control structures & functions', 'Data structures & file handling', 'Data handling with Pandas', 'Data visualisation with Matplotlib'].map((u, i) => `<div class="un" style="opacity:0;display:flex;align-items:center;gap:22px;padding:20px 28px;border-radius:22px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14)">
              <span style="font-family:var(--mono);font-weight:700;font-size:26px;color:#a1a1aa;width:90px">Unit ${['I', 'II', 'III', 'IV', 'V'][i]}</span><span style="flex:1;${H}letter-spacing:-.01em;font-size:34px;color:#fff">${u}</span><b class="tk" style="font-size:36px;color:#22c55e;opacity:0">✓</b></div>`).join('')}
          </div>
          <div class="abs" style="left:1100px;top:250px;width:680px">
            <p id="tp" style="${H}font-size:64px;line-height:1.05;color:#fff;opacity:0">Every concept,<br><span class="gl">taught through pharmacy.</span></p>
            <div style="margin-top:34px;display:flex;flex-wrap:wrap;gap:16px">${['℞ Prescriptions', '💊 Dosage calculations', '📈 Drug concentration curves', '⚠️ Adverse reaction data'].map((x) => `<span class="ex" style="opacity:0;font-family:var(--head);font-weight:700;font-size:32px;color:#fff;padding:14px 26px;border-radius:999px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.2)">${x}</span>`).join('')}</div>
          </div>
        </div>`,
      update: (el, t, s) => {
        const sw = ap(t, S(s, 1) - 0.3, 0.5);
        $('#p0', el).style.opacity = 1 - sw;
        reveal($('#p0', el), t, S(s, 0) - 0.2, 0.12);
        $$('.cr', el).forEach((c, i) => pop(c, ap(t, S(s, 0) + 0.4 + i * dur(s, 0) * 0.28, 0.5)));
        $('#p1', el).style.opacity = sw;
        const d = dur(s, 1);
        $$('.un', el).forEach((u, i) => {
          show(u, ap(t, S(s, 1) + i * 0.18, 0.4), 20, 0.97);
          $('.tk', u).style.opacity = ap(t, S(s, 1) + d * 0.2 + i * d * 0.07, 0.3);
        });
        show($('#tp', el), ap(t, S(s, 1) + d * 0.72, 0.5), 15, 1);
        $$('.ex', el).forEach((x, i) => pop(x, ap(t, S(s, 1) + d * 0.78 + i * 0.25, 0.4)));
      },
    },

    'c-features': {
      subsOnly: true,
      build: () => {
        const F = [['Champ Narrator', 'Voice, in their language', 'f-narrator.png'], ['Champ Animate', 'Animated explanations', 'f-animate.png'], ['Video lessons', 'Three short episodes per lesson', 'VIDEO'], ['Champ Lab', 'Real Python, in the browser', 'f-lab.png'], ['Champ Check', 'Instant checking', 'f-check.png'], ['Champ Quiz', 'A quiz after every lesson', 'f-quiz.png'], ['Champ Map', 'A mind map for revision', 'f-map.png'], ['Important Questions', 'Model answers · PCI exam pattern', 'f-iq.png']];
        return `${glowBg('rgba(124,92,255,.28)', 'rgba(45,212,191,.16)')}
          <div class="abs" style="left:150px;top:0;bottom:0;width:820px;display:flex;align-items:center">
            ${F.map(([n, d], i) => `<div class="fn abs" data-i="${i}" style="left:0;top:50%;transform:translateY(-50%);opacity:0"><p style="${H}font-size:${n.length > 14 ? 92 : 112}px;line-height:1"><span class="gl">${n}</span></p><p style="${H}margin-top:22px;font-size:50px;color:#d4d4d8;letter-spacing:-.01em">${d}</p></div>`).join('')}
          </div>
          <div id="ph" class="abs" style="left:1180px;top:110px;perspective:2400px">
            <div id="dev" style="width:400px;height:864px;border-radius:64px;background:#0b0b0f;padding:14px;box-shadow:0 60px 120px rgba(0,0,0,.6),0 0 0 2px #2a2a33 inset">
              <div style="position:relative;width:100%;height:100%;border-radius:52px;overflow:hidden;background:#fff">
                ${F.map(([, , img], i) => (img === 'VIDEO'
                  ? `<div class="scr" data-i="${i}" style="position:absolute;inset:0;opacity:0;background:#0f172a;display:flex;flex-direction:column;justify-content:center;padding:20px"><img src="../../media/bp101t/1-1/en/ep1.jpg" style="width:100%;border-radius:14px"/><p style="margin-top:16px;font-family:var(--head);font-weight:800;font-size:22px;color:#fff">Episode 1 · What is a program?</p><p style="margin-top:6px;font-size:18px;color:#94a3b8">ಕನ್ನಡ · हिन्दी · English</p></div>`
                  : `<img class="scr" data-i="${i}" src="${SHOT(img)}" style="position:absolute;inset:0;width:100%;opacity:0"/>`)).join('')}
                <div style="position:absolute;left:50%;top:12px;width:120px;height:30px;border-radius:99px;background:#000;transform:translateX(-50%)"></div>
              </div>
            </div>
          </div>
          <div id="live" class="abs" style="inset:0;opacity:0;background:#000">
            <h1 class="abs" style="${H}left:0;right:0;top:300px;text-align:center;font-size:120px;color:#fff">Python is <span style="color:#4ade80">live today.</span></h1>
            <p class="abs" style="${H}left:0;right:0;top:470px;text-align:center;font-size:54px;color:#a1a1aa">Each next subject arrives ahead of your batch.</p>
            <div class="abs" style="left:0;right:0;top:640px;display:flex;justify-content:center;gap:26px">${Array.from({ length: 8 }, (_, i) => `<div style="text-align:center"><div style="width:44px;height:44px;margin:0 auto;border-radius:50%;${i === 0 ? 'background:#22c55e;box-shadow:0 0 30px #22c55e' : 'border:3px solid #52525b'}"></div><p style="margin-top:12px;font-family:var(--head);font-weight:700;font-size:24px;color:${i === 0 ? '#fff' : '#71717a'}">Sem ${i + 1}</p></div>`).join('<div style="width:60px;height:3px;margin-top:21px;background:#3f3f46"></div>')}</div>
          </div>`;
      },
      update: (el, t, s) => {
        // the seven lesson features split the first sentence; Important Questions takes the second
        const d0 = dur(s, 0);
        let k = -1;
        if (t >= S(s, 0) - 0.2) k = Math.min(6, Math.floor(((t - S(s, 0) + 0.2) / d0) * 7));
        if (t >= S(s, 1) - 0.2) k = 7;
        $$('.fn', el).forEach((f, i) => {
          const on = i === k;
          f.style.opacity = on ? 1 : 0;
          f.style.filter = `blur(${on ? 0 : 12}px)`;
        });
        $$('.scr', el).forEach((sc) => (sc.style.opacity = Number(sc.dataset.i) === k ? 1 : 0));
        const p = ap(t, s.start, 1.2);
        $('#ph', el).style.opacity = ap(t, s.start, 0.5);
        $('#dev', el).style.transform = `rotateY(${lerp(-30, -12, p) + Math.sin(t * 0.8) * 3}deg) rotateX(${lerp(12, 4, p)}deg) translateY(${(1 - p) * 100 + Math.sin(t * 1.2) * 8}px)`;
        const lv = $('#live', el), q = ap(t, S(s, 2) - 0.2, 0.6);
        lv.style.opacity = q;
      },
    },

    'c-teacher': {
      subsOnly: true,
      build: () => `<div class="layer brand"></div>
        <div id="a" class="abs" style="inset:0">
          <div id="ph" class="abs" style="left:250px;top:110px;perspective:2400px">${phone('dev', SHOT('m-lesson.png'), 380)}</div>
          <div class="abs" style="left:860px;top:260px;width:900px">
            <p style="${H}font-size:84px;line-height:1.05;color:#1d1d1f">Your faculty lead.<br><span class="grad">Campus Champ powers the practice.</span></p>
            <div style="margin-top:36px;display:flex;gap:16px;flex-wrap:wrap">${['ಕನ್ನಡ', 'हिन्दी', 'English', 'Any phone', 'No lab needed'].map((l) => `<span class="lg" style="opacity:0;${H}letter-spacing:-.01em;font-size:40px;color:#1d1d1f;padding:14px 30px;border-radius:999px;background:#f2f2f7">${l}</span>`).join('')}</div>
          </div>
        </div>
        <div id="lp" class="abs" style="left:410px;top:160px;opacity:0;perspective:2400px">${laptop('lap', SHOT('dashboard.png'), 1100)}</div>
        <div id="wa" class="abs" style="left:1190px;top:560px;opacity:0;width:560px;border-radius:26px 26px 26px 8px;background:#dcf8c6;padding:24px 28px;box-shadow:0 30px 70px rgba(0,0,0,.25)">
          <p style="font-family:var(--head);font-weight:800;font-size:24px;color:#128c7e">WhatsApp · Section A</p>
          <p style="margin-top:8px;font-size:32px;line-height:1.35;color:#111b21">📚 Reminder: please finish Lesson 1.3 before Friday's class.</p>
        </div>`,
      update: (el, t, s) => {
        const out = ap(t, S(s, 1) - 0.3, 0.6);
        $('#a', el).style.opacity = ap(t, s.start, 0.5) * (1 - out);
        const p = ap(t, s.start, 1.2);
        $('#dev', el).style.transform = `rotateY(${lerp(28, 12, p)}deg) rotateX(${lerp(12, 4, p)}deg) translateY(${(1 - p) * 100 + Math.sin(t * 1.2) * 8}px)`;
        $$('.lg', el).forEach((g, i) => pop(g, ap(t, S(s, 0) + dur(s, 0) * (0.35 + i * 0.1), 0.4)));
        const q = ap(t, S(s, 1) - 0.2, 1.2);
        $('#lp', el).style.opacity = q;
        $('#lap', el).style.transform = `rotateX(${lerp(24, 6, q)}deg) translateY(${(1 - q) * 160}px)`;
        pop($('#wa', el), ap(t, S(s, 1) + dur(s, 1) * 0.6, 0.6));
      },
    },

    'c-principal': {
      subsOnly: true,
      build: () => `${glowBg('rgba(124,92,255,.3)', 'rgba(45,212,191,.14)')}
        <div id="rw" class="abs" style="left:230px;top:90px;perspective:2400px"><img id="rep" src="${SHOT('report.png')}" style="width:640px;border-radius:30px;box-shadow:0 60px 120px rgba(0,0,0,.6)"/></div>
        <div id="lab" class="abs" style="left:1050px;top:250px;display:flex;flex-direction:column;gap:18px">
          <p style="${H}font-size:80px;line-height:1.05;color:#fff">A clear report.<br><span class="gl">Every term.</span></p>
          ${['Participation', 'Progress, lesson by lesson', 'Quiz scores', '📄 PDF for your records'].map((x) => `<p class="ft" style="${H}letter-spacing:-.01em;font-size:44px;color:#d4d4d8;opacity:0">${x}</p>`).join('')}
        </div>
        <div id="naac" class="abs" style="left:980px;top:170px;width:800px;opacity:0;border-radius:40px;background:#fff;padding:48px 52px;box-shadow:0 50px 120px rgba(0,0,0,.6)">
          <p style="font-family:var(--head);font-weight:800;font-size:28px;color:#4f46e5;letter-spacing:.06em">NAAC EVIDENCE</p>
          <p style="${H}margin-top:8px;font-size:58px;line-height:1.05;color:#1d1d1f">Ready for your SSR and peer team visit</p>
          ${[['Criterion 2', 'ICT-enabled, student-centric teaching'], ['Criterion 2', 'Learning outcomes, measured'], ['Criterion 7', 'Blended learning as a best practice']].map(([c, x]) => `<div class="nc" style="margin-top:20px;display:flex;align-items:center;gap:20px;padding:20px 24px;border-radius:22px;background:#f5f5f7;opacity:0"><b style="flex:none;width:52px;height:52px;border-radius:50%;background:#22c55e;color:#fff;display:grid;place-items:center;font-size:30px">✓</b><div><p style="font-family:var(--head);font-weight:800;font-size:24px;color:#6e6e73">${c}</p><p style="${H}letter-spacing:-.01em;font-size:36px;color:#1d1d1f">${x}</p></div></div>`).join('')}
          <p style="margin-top:22px;font-size:22px;color:#8e8e93">Supports your documentation. Accreditation decisions rest with NAAC.</p>
        </div>`,
      update: (el, t, s) => {
        const p = ap(t, s.start + 0.1, 1.4), sw = ap(t, S(s, 1) - 0.3, 0.7);
        const r = $('#rep', el);
        r.style.opacity = p;
        r.style.transform = `rotateY(${lerp(-26, -10, p) - sw * 6}deg) rotateX(${lerp(14, 4, p)}deg) translateY(${(1 - p) * 120 + Math.sin(t * 1.1) * 8}px) scale(${1 - sw * 0.1})`;
        $('#rw', el).style.transform = `translateX(${-sw * 80}px)`;
        $('#lab', el).style.opacity = 1 - sw;
        $$('.ft', el).forEach((f, i) => {
          const q = ap(t, S(s, 0) + dur(s, 0) * (0.25 + i * 0.16), 0.45);
          f.style.opacity = q;
          f.style.filter = `blur(${(1 - q) * 10}px)`;
        });
        show($('#naac', el), sw, 40, 0.94);
        $$('.nc', el).forEach((n, i) => show(n, ap(t, S(s, 1) + dur(s, 1) * (0.25 + i * 0.17), 0.45), 15, 0.97));
      },
    },

    'c-cta': {
      subsOnly: true,
      build: () => `${glowBg()}
        <div class="abs" style="left:0;right:0;top:250px;text-align:center">
          <h1 id="h" style="${H}font-size:140px;line-height:1.02;color:#fff">${words('Make your college')}</h1>
          <h1 id="h2" style="${H}font-size:140px;line-height:1.1;opacity:0"><span class="gl">AI-ready.</span></h1>
          <p id="sb" style="${H}margin-top:18px;font-size:58px;color:#a1a1aa;opacity:0">One semester at a time.</p>
        </div>
        <div id="chips" class="abs" style="left:0;right:0;top:760px;display:flex;justify-content:center;gap:22px">
          <span class="ch" style="opacity:0;font-family:var(--head);font-weight:700;font-size:38px;color:#fef3c7;padding:18px 34px;border-radius:999px;background:rgba(251,191,36,.14);border:1.5px solid #fbbf24">Pilot 2026-27 · limited colleges</span>
          <span class="ch" style="opacity:0;font-family:var(--head);font-weight:800;font-size:38px;color:#000;padding:18px 34px;border-radius:999px;background:#fff">Book a 20-minute walkthrough →</span>
        </div>`,
      update: (el, t, s) => {
        reveal($('#h', el), t, S(s, 0) + 0.1, 0.18);
        show($('#h2', el), ap(t, S(s, 0) + 0.75, 0.6), 20, 0.96);
        show($('#sb', el), ap(t, S(s, 0) + dur(s, 0) * 0.55, 0.6), 14, 1);
        $$('.ch', el).forEach((c, i) => pop(c, ap(t, S(s, 1) + 0.3 + i * dur(s, 1) * 0.5, 0.5)));
      },
    },

    'c-end': {
      brand: true,
      build: () => endCard('Campus Champ for Colleges', "India's first multilingual blended-learning platform for pharmacy's AI curriculum.", 'Book a 20-minute walkthrough →', 'campuschamp.in/colleges', 'Scan to book'),
      update: endUpdate,
    },
  };
});
