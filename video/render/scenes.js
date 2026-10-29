// Draws one frame of a lesson video for any time t (seconds). Deterministic: the renderer
// seeks to each frame time, calls renderAt(t), then screenshots the page.
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
  const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
  const prog = (t, a, d) => ease((t - a) / d);
  const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c]);
  // **bold** and `code` in lesson text
  const md = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/`(.+?)`/g, '<code style="font-family:var(--mono);background:#eef2ff;color:#4338ca;padding:0 .25em;border-radius:.25em">$1</code>');
  const enter = (el, p, dy = 40, scale = 0.96) => {
    if (!el) return;
    el.style.opacity = p;
    el.style.transform = `translateY(${(1 - p) * dy}px) scale(${scale + (1 - scale) * p})`;
  };

  let T = null; // timeline
  let current = null; // { scene, el }

  // ---------- characters ----------
  function setupCast() {
    $('#p-anu').insertAdjacentHTML('afterbegin', CHARACTERS.anu);
    $('#p-champ').insertAdjacentHTML('afterbegin', CHARACTERS.champ);
  }
  function speakingAt(t) {
    for (const s of T.scenes) for (const l of s.lines) if (l.who && t >= l.start && t < l.start + l.dur) return l;
    return null;
  }
  function animateCast(t, line) {
    for (const who of ['anu', 'champ']) {
      const card = $(`#p-${who}`);
      const on = line && line.who === who;
      const level = on && line.env ? line.env[Math.min(line.env.length - 1, Math.floor((t - line.start) * T.fps))] || 0 : 0;
      const mouth = $(`#${who}-mouth-open`);
      mouth.style.transform = `scaleY(${level > 0.12 ? clamp(0.35 + level * 0.9, 0, 1.1) : 0})`;
      $(`#${who}-mouth-closed`).style.opacity = level > 0.12 ? 0 : 1;
      // blink every ~3.7s (offset per character)
      const ph = (t + (who === 'anu' ? 0 : 1.6)) % 3.7;
      $(`#${who}-lids`).style.transform = `scaleY(${ph < 0.14 ? 1 : 0})`;
      const bob = Math.sin((t + (who === 'anu' ? 0 : 1)) * 2.2) * (on ? 4 : 2);
      $(`#${who}-body`).style.transform = `translateY(${bob}px)`;
      card.style.opacity = line && !on ? 0.72 : 1;
      card.style.transform = `scale(${on ? 1.02 : 1})`;
      $('.ring', card).style.opacity = on ? 1 : 0;
      const wave = $('.wave', card);
      wave.style.opacity = on ? 1 : 0;
      [...wave.children].forEach((b, i) => (b.style.height = `${8 + 20 * clamp(level * (0.6 + 0.4 * Math.sin(t * 18 + i * 1.7)))}px`));
    }
  }

  // ---------- subtitles ----------
  function chunks(text) {
    const parts = text.match(/[^,.?!:;]+[,.?!:;]*\s*/g) || [text];
    const out = [];
    let cur = '';
    for (const p of parts) {
      if ((cur + p).length > 64 && cur) {
        out.push(cur.trim());
        cur = p;
      } else cur += p;
    }
    if (cur.trim()) out.push(cur.trim());
    return out;
  }
  function subtitles(t, line) {
    const box = $('#subs');
    if (!line || !line.text) {
      box.innerHTML = '';
      return;
    }
    const cs = chunks(line.text);
    const total = cs.reduce((s, c) => s + c.length, 0);
    let acc = 0;
    let pick = cs[cs.length - 1];
    for (const c of cs) {
      acc += c.length;
      if ((t - line.start) / line.dur <= acc / total) {
        pick = c;
        break;
      }
    }
    const who = line.who === 'anu' ? 'Anu' : 'Champ';
    box.innerHTML = `<div class="box"><span class="who ${line.who}">${who}</span><span class="text">${esc(pick)}</span></div>`;
  }

  // ---------- scenes ----------
  const lineStart = (scene, id) => (scene.lines.find((l) => l.id === id) || {}).start ?? Infinity;
  const lineEnd = (scene, id) => {
    const l = scene.lines.find((x) => x.id === id);
    return l ? l.start + l.dur : Infinity;
  };

  const SCENES = {
    intro: {
      build: (s) => `
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;padding:0 40px">
          <p class="kicker pop" id="i1" style="color:#a5b4fc">BP101T · Lesson ${esc(T.lesson)} · ಕನ್ನಡ</p>
          <h1 class="h1 pop" id="i2" style="font-size:96px;margin-top:22px;max-width:1200px">${esc(T.title)}</h1>
          <p class="pop" id="i3" style="font-size:34px;margin-top:22px;color:#cbd5e1">${esc(T.lessonTitle)}</p>
          <div class="pop" id="i4" style="margin-top:40px;display:flex;gap:14px">
            ${['Voice lessons', 'ಕನ್ನಡ · हिन्दी · English', 'Free practice'].map((x) => `<span style="font-size:24px;font-weight:600;padding:10px 20px;border-radius:999px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.15)">${x}</span>`).join('')}
          </div>
        </div>`,
      update: (el, t, s) => {
        ['i1', 'i2', 'i3', 'i4'].forEach((id, i) => enter($(`#${id}`, el), prog(t, s.start + 0.2 + i * 0.35, 0.7)));
      },
    },

    hook: {
      build: (s) => `
        <div class="card" style="background:linear-gradient(160deg,#fff7ed,#ffffff 60%)">
          <div style="position:absolute;left:60px;top:70px;width:600px">
            <p class="kicker">Lesson ${esc(T.lesson)}</p>
            <h2 class="h1 pop" id="h1" style="font-size:64px;margin-top:18px">${esc(s.data.title)}</h2>
            <div id="h2" style="margin-top:44px;display:flex;flex-direction:column;gap:18px">
              ${['💻 Installation ಬೇಡ', '🧑‍🎓 Coding background ಬೇಡ', '📱 ನಿಮ್ಮ phone ಸಾಕು'].map((x, i) => `<div class="pop chip-h" data-i="${i}" style="font-size:34px;font-weight:600;background:#fff;border:2px solid #fed7aa;border-radius:22px;padding:16px 26px;width:fit-content;box-shadow:0 8px 24px rgba(249,115,22,.12)">${x}</div>`).join('')}
            </div>
          </div>
          <svg viewBox="0 0 560 620" style="position:absolute;right:30px;bottom:0;width:560px;height:620px">
            <rect x="40" y="40" width="480" height="380" rx="24" fill="#e0e7ff"/>
            ${[0, 1, 2].map((r) => `<rect x="60" y="${110 + r * 110}" width="440" height="12" rx="6" fill="#a5b4fc"/>` + [0, 1, 2, 3, 4, 5].map((c) => {
              const colors = ['#f87171', '#34d399', '#60a5fa', '#fbbf24', '#a78bfa', '#f472b6'];
              const h = 46 + ((r * 7 + c * 3) % 4) * 8;
              return `<rect x="${78 + c * 70}" y="${110 + r * 110 - h}" width="44" height="${h}" rx="10" fill="${colors[(c + r) % 6]}"/><rect x="${84 + c * 70}" y="${110 + r * 110 - h + 14}" width="32" height="12" rx="3" fill="#fff" opacity=".85"/>`;
            }).join('')).join('')}
            <rect x="0" y="430" width="560" height="190" rx="22" fill="#0f766e"/>
            <rect x="0" y="430" width="560" height="26" rx="12" fill="#14b8a6"/>
            <g id="rx" transform="translate(70 300) rotate(-6)">
              <rect width="210" height="250" rx="14" fill="#fff" stroke="#e2e8f0" stroke-width="3"/>
              <text x="22" y="48" font-family="Plus Jakarta Sans" font-weight="800" font-size="34" fill="#4f46e5">℞</text>
              ${[0, 1, 2, 3].map((i) => `<rect x="22" y="${80 + i * 36}" width="${150 - i * 18}" height="12" rx="6" fill="#cbd5e1"/>`).join('')}
            </g>
            <g id="phone" transform="translate(330 330) rotate(8)">
              <rect width="150" height="270" rx="26" fill="#0f172a"/><rect x="10" y="14" width="130" height="236" rx="18" fill="#111633"/>
              ${[0, 1, 2, 3].map((i) => `<rect x="24" y="${40 + i * 30}" width="${60 + (i % 2) * 30}" height="10" rx="5" fill="${['#64748b', '#93c5fd', '#86efac', '#fcd34d'][i]}"/>`).join('')}
              <rect x="22" y="180" width="106" height="44" rx="12" fill="#10b981"/><text x="75" y="209" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#fff">▶ Run</text>
            </g>
          </svg>
        </div>`,
      update: (el, t, s) => {
        enter($('#h1', el), prog(t, s.start + 0.3, 0.7));
        const a = lineStart(s, 'a-hook');
        const d = s.lines[1] ? s.lines[1].dur : 6;
        el.querySelectorAll('.chip-h').forEach((c, i) => enter(c, prog(t, a + d * (0.35 + i * 0.2), 0.5), 30));
        const ph = $('#phone', el);
        ph.setAttribute('transform', `translate(330 ${330 + Math.sin(t * 1.6) * 6}) rotate(8)`);
      },
    },

    prescription: {
      // Replays the lesson's own animation (actors + actions) at video size
      build: (s) => {
        const S = 1.5;
        const box = (a) => `left:${a.desktop.x * S + 50}px;top:${a.desktop.y * S + 70}px;width:${a.desktop.w * S}px;height:${a.desktop.h * S}px`;
        const color = { emerald: ['#ecfdf5', '#10b981'], indigo: ['#eef2ff', '#6366f1'], amber: ['#fffbeb', '#f59e0b'] };
        const actors = s.data.actors.map((a) => {
          if (a.type === 'card') {
            const [bg, fg] = color[a.color] || color.indigo;
            return `<div class="actor pop" data-id="${a.id}" style="position:absolute;${box(a)};background:${bg};border:3px solid ${fg};border-radius:28px;padding:22px 26px;opacity:0">
              <p style="font-family:var(--head);font-weight:800;font-size:30px;color:${fg}">${a.icon || ''} ${esc(a.title)}</p>
              <div style="margin-top:14px;display:flex;flex-direction:column;gap:8px">${a.lines.map((l, i) => `<div class="al" data-i="${i}" style="font-family:${a.mono ? 'var(--mono)' : 'var(--body)'};font-size:${a.mono ? 23 : 27}px;padding:8px 12px;border-radius:12px;color:#0f172a">${esc(l)}</div>`).join('')}</div>
            </div>`;
          }
          if (a.type === 'terminal') {
            return `<div class="actor pop term" data-id="${a.id}" style="position:absolute;${box(a)};opacity:0"><div class="bar"><span>&gt;_ ${esc(a.title)}</span><span>stdout</span></div><div class="out" style="font-size:24px;line-height:1.45;padding:12px 24px"></div></div>`;
          }
          if (a.type === 'pill') {
            return `<div class="actor pop" data-id="${a.id}" style="position:absolute;left:${a.desktop.x * S + 50}px;top:${a.desktop.y * S + 70}px;opacity:0;background:#fef3c7;border:2px solid #f59e0b;color:#92400e;font-weight:700;font-size:24px;border-radius:999px;padding:8px 20px;white-space:nowrap">🔍 ${esc(a.text)}</div>`;
          }
          return '';
        });
        return `<div class="card" style="background:#f8fafc"><p class="kicker" style="position:absolute;left:50px;top:28px">${esc(s.data.title)}</p>${actors.join('')}</div>`;
      },
      update: (el, t, s) => {
        const state = { shown: new Set(), hl: {}, out: {} };
        s.data.steps.forEach((actions, k) => {
          const st = lineStart(s, `anim:${k + 1}`);
          if (t < st) return;
          for (const a of actions) {
            if (a.do === 'show') state.shown.add(a.target);
            if (a.do === 'highlightLine') state.hl[a.target] = a.line;
            if (a.do === 'appendOutput') (state.out[a.target] = state.out[a.target] || []).push({ text: a.text, at: st + 0.8 });
            if (a.do === 'scanLines') {
              const i = Math.floor((t - st) / ((a.intervalMs || 800) / 1000));
              const card = s.data.actors.find((x) => x.id === a.target);
              state.hl[a.target] = i < card.lines.length ? i : null;
            }
          }
        });
        el.querySelectorAll('.actor').forEach((node) => {
          const id = node.dataset.id;
          let firstShow = Infinity;
          s.data.steps.forEach((actions, k) => {
            if (actions.some((a) => a.do === 'show' && a.target === id)) firstShow = Math.min(firstShow, lineStart(s, `anim:${k + 1}`));
          });
          enter(node, state.shown.has(id) ? prog(t, firstShow, 0.6) : 0, 30);
          node.querySelectorAll('.al').forEach((l) => {
            const on = state.hl[id] === Number(l.dataset.i);
            l.style.background = on ? '#fde68a' : 'transparent';
            l.style.fontWeight = on ? 700 : 400;
          });
          const out = $('.out', node);
          if (out) out.innerHTML = (state.out[id] || []).filter((o) => t >= o.at).map((o) => `<div class="ok">&gt; ${esc(o.text)}</div>`).join('');
        });
      },
    },

    why: {
      build: () => `
        <div class="card" style="background:linear-gradient(160deg,#eef2ff,#fff 55%)">
          <p class="kicker" style="position:absolute;left:60px;top:56px">Python ಯಾಕೆ?</p>
          <p class="muted" style="position:absolute;left:60px;top:96px;font-size:26px">Guido van Rossum · 1991 · ಪ್ರಪಂಚದ ಅತ್ಯಂತ popular languages ಗಳಲ್ಲಿ ಒಂದು</p>
          <div style="position:absolute;left:60px;right:60px;top:180px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
            ${[
              ['🔤', 'English ತರಹ ಓದಬಹುದು', 'Beginners ಗೆ ಸುಲಭ', '#e0e7ff'],
              ['🆓', 'ಎಲ್ಲರಿಗೂ free', 'Download, use, share', '#dcfce7'],
              ['📊', 'Data, graphs libraries', 'NumPy · Pandas · Matplotlib', '#fef3c7'],
              ['💊', 'Pharmacy ಯಲ್ಲಿ use', 'Clinical trials · PK curves · ADR reports', '#ffe4e6'],
            ].map(([ic, t1, t2, bg], i) => `<div class="pop tile" data-i="${i}" style="background:${bg};border-radius:30px;padding:34px 36px;opacity:0">
                <div style="font-size:64px">${ic}</div><p class="h1" style="font-size:40px;margin-top:14px">${t1}</p><p class="muted" style="font-size:26px;margin-top:8px">${t2}</p></div>`).join('')}
          </div>
        </div>`,
      update: (el, t, s) => {
        const l = s.lines[0];
        el.querySelectorAll('.tile').forEach((n, i) => enter(n, prog(t, l.start + l.dur * (i * 0.22), 0.6), 40));
      },
    },

    terms: {
      build: (s) => `
        <div class="card" style="background:linear-gradient(160deg,#f0fdfa,#fff 60%)">
          <p class="kicker" style="position:absolute;left:60px;top:56px;color:#0d9488">Key words · ಈ lesson ನ ಮುಖ್ಯ ಪದಗಳು</p>
          ${s.data.cards.map((c, i) => `<div class="pop term-card" data-i="${i}" style="position:absolute;left:120px;right:120px;top:180px;bottom:120px;background:#fff;border:3px solid #99f6e4;border-radius:36px;padding:60px 70px;box-shadow:0 30px 60px rgba(13,148,136,.15);opacity:0">
              <p style="font-family:var(--mono);font-weight:700;font-size:84px;color:#4f46e5">${esc(c.term)}</p>
              <p style="font-size:44px;line-height:1.45;margin-top:34px;color:#0f172a">${md(c.meaning)}</p>
              <p class="muted" style="position:absolute;right:50px;bottom:36px;font-family:var(--mono);font-size:26px">${i + 1} / ${s.data.cards.length}</p>
            </div>`).join('')}
        </div>`,
      update: (el, t, s) => {
        const start = lineEnd(s, 'a-terms') + 0.2;
        const each = 4.2;
        el.querySelectorAll('.term-card').forEach((n, i) => {
          const a = start + i * each;
          const p = t < a ? 0 : t < a + each - 0.35 || i === s.data.cards.length - 1 ? prog(t, a, 0.5) : 1 - prog(t, a + each - 0.35, 0.35);
          enter(n, p, 60, 0.92);
        });
      },
    },

    code: {
      build: (s) => {
        const tok = (line) => {
          if (line.trim().startsWith('#')) return `<span class="tok-c">${esc(line)}</span>`;
          return esc(line)
            .replace(/(&quot;|")(.*?)\1/g, '<span class="tok-s">"$2"</span>')
            .replace(/\b(print)\b/g, '<span class="tok-f">$1</span>')
            .replace(/(?<![\w">])(\d+)(?![\w<])/g, '<span class="tok-n">$1</span>');
        };
        const lines = s.data.code.split('\n');
        return `
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;gap:22px">
            <div class="editor" style="flex:none">
              <div class="bar"><i style="background:#f87171"></i><i style="background:#fbbf24"></i><i style="background:#34d399"></i><span class="file">${esc(s.data.filename)}</span><span class="ver">Python 3.11</span></div>
              <div class="code">${lines.map((l, i) => `<div class="ln" data-l="${i + 1}"><span class="n">${i + 1}</span><span>${tok(l)}</span></div>`).join('')}</div>
            </div>
            <div class="term" style="flex:1"><div class="bar"><span>&gt;_ Terminal output</span><span>stdout</span></div><div class="out" id="cout"></div></div>
          </div>`;
      },
      update: (el, t, s) => {
        let active = null;
        const outs = [];
        s.data.steps.forEach((st, k) => {
          const a = lineStart(s, `step:${k + 1}`);
          if (t >= a) {
            active = st.line;
            if (st.output && t >= a + 1.2) outs.push(st.output);
          }
        });
        el.querySelectorAll('.ln').forEach((l) => l.classList.toggle('on', Number(l.dataset.l) === active));
        $('#cout', el).innerHTML = outs.map((o) => `<div class="ok">${esc(o)}</div>`).join('') + (t >= lineStart(s, 'step:7') ? '<div style="color:#64748b;margin-top:6px">✓ Program finished</div>' : '');
      },
    },

    mistake: {
      build: () => `
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;gap:22px">
          <p class="kicker" style="color:#fda4af">ಸಾಮಾನ್ಯ ತಪ್ಪು · Common mistake</p>
          <div class="editor"><div class="bar"><i style="background:#f87171"></i><i style="background:#fbbf24"></i><i style="background:#34d399"></i><span class="file">mistake.py</span><span class="ver">Python 3.11</span></div>
            <div class="code" style="font-size:52px;padding:40px 0"><div class="ln"><span class="n">1</span><span><span id="pP" class="tok-f" style="display:inline-block">P</span><span class="tok-f">rint</span>(<span class="tok-s">"Paracetamol"</span>)</span></div></div>
          </div>
          <div class="term" style="flex:1"><div class="bar"><span>&gt;_ Terminal output</span><span id="mstate"></span></div><div class="out" id="mout" style="font-size:34px"></div></div>
          <div id="badge" class="pop" style="position:absolute;right:30px;top:120px;background:#fef3c7;color:#92400e;border:2px solid #f59e0b;border-radius:18px;padding:12px 22px;font-weight:700;font-size:28px;opacity:0">Python is case-sensitive: P ≠ p</div>
        </div>`,
      update: (el, t, s) => {
        const err = lineStart(s, 'c-mistake') + 2.6;
        const fix = lineStart(s, 'a-mistake') + 3.0;
        const P = $('#pP', el);
        const fixed = t >= fix;
        P.textContent = fixed ? 'p' : 'P';
        P.style.color = t >= err && !fixed ? '#fda4af' : fixed ? '#6ee7b7' : '';
        P.style.transform = `scale(${t >= err && t < fix ? 1.25 : 1})`;
        $('#mout', el).innerHTML = fixed
          ? '<div class="ok">Paracetamol</div>'
          : t >= err
            ? '<div class="err">Traceback (most recent call last):<br>  File "mistake.py", line 1<br>NameError: name \'Print\' is not defined</div>'
            : '';
        $('#mstate', el).innerHTML = fixed ? '<span style="color:#6ee7b7">✓ fixed</span>' : t >= err ? '<span style="color:#fda4af">✗ error</span>' : '';
        enter($('#badge', el), prog(t, lineStart(s, 'a-mistake') + 1.5, 0.5), 20);
      },
    },

    quiz: {
      build: (s) => `
        <div class="card" style="background:linear-gradient(160deg,#faf5ff,#fff 60%)">
          <p class="kicker" style="position:absolute;left:60px;top:56px;color:#7c3aed">Pause and answer · ನೀವೇ ಉತ್ತರಿಸಿ</p>
          <h2 class="h1" style="position:absolute;left:60px;right:300px;top:110px;font-size:50px">${esc(s.data.q)}</h2>
          <div style="position:absolute;left:60px;right:60px;top:330px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
            ${s.data.options.map((o, i) => `<div class="opt" data-i="${i}" style="display:flex;align-items:center;gap:22px;border:3px solid #e9d5ff;border-radius:26px;padding:26px 30px;font-size:36px;font-weight:600;background:#fff">
              <span style="flex:none;width:58px;height:58px;border-radius:16px;background:#f3e8ff;color:#7c3aed;display:grid;place-items:center;font-family:var(--head);font-weight:800">${'ABCD'[i]}</span><span>${esc(o)}</span></div>`).join('')}
          </div>
          <div id="ring" style="position:absolute;right:60px;top:90px;width:180px;height:180px;opacity:0">
            <svg viewBox="0 0 100 100" style="width:100%;height:100%;transform:rotate(-90deg)"><circle cx="50" cy="50" r="44" fill="#f3e8ff"/><circle id="arc" cx="50" cy="50" r="44" fill="none" stroke="#7c3aed" stroke-width="8" stroke-linecap="round" stroke-dasharray="276.5" stroke-dashoffset="0"/></svg>
            <span id="num" style="position:absolute;inset:0;display:grid;place-items:center;font-family:var(--head);font-weight:800;font-size:76px;color:#7c3aed"></span>
          </div>
        </div>`,
      update: (el, t, s) => {
        const cd = s.lines.find((l) => l.id === 'countdown');
        const reveal = lineStart(s, 'a-quiz-answer');
        const inCd = t >= cd.start && t < cd.start + cd.dur;
        $('#ring', el).style.opacity = inCd ? 1 : 0;
        if (inCd) {
          const left = cd.dur - (t - cd.start);
          $('#num', el).textContent = Math.ceil(left);
          $('#arc', el).setAttribute('stroke-dashoffset', String(276.5 * (1 - left / cd.dur)));
        }
        el.querySelectorAll('.opt').forEach((o) => {
          const i = Number(o.dataset.i);
          const right = i === s.data.answer;
          const shown = t >= reveal;
          o.style.borderColor = shown && right ? '#10b981' : '#e9d5ff';
          o.style.background = shown && right ? '#ecfdf5' : '#fff';
          o.style.opacity = shown && !right ? 0.45 : 1;
          o.style.transform = `scale(${shown && right ? 1.03 : 1})`;
        });
      },
    },

    exam: {
      build: (s) => `
        <div class="card" style="background:#fffdf5;background-image:repeating-linear-gradient(#fffdf5 0 58px,#dbeafe 58px 60px)">
          <div style="position:absolute;left:150px;top:0;bottom:0;width:3px;background:#fca5a5"></div>
          <p class="kicker" style="position:absolute;left:190px;top:28px;color:#b91c1c">Exam corner · Short answer · ${s.data.marks} marks</p>
          <p style="position:absolute;left:190px;right:70px;top:116px;font-family:var(--head);font-weight:800;font-size:44px;color:#0f172a">Q. ${esc(s.data.q)}</p>
          <p id="ans" style="position:absolute;left:190px;right:80px;top:236px;font-family:'Inter';font-size:38px;line-height:60px;color:#1e3a8a"></p>
          <div id="m1" style="position:absolute;left:28px;top:250px;font-family:var(--head);font-weight:800;font-size:40px;color:#dc2626;opacity:0">✓ 1</div>
          <div id="m2" style="position:absolute;left:28px;top:430px;font-family:var(--head);font-weight:800;font-size:40px;color:#dc2626;opacity:0">✓ 1</div>
          <p class="muted" style="position:absolute;left:190px;bottom:28px;font-size:22px">${esc(s.data.note)}</p>
        </div>`,
      update: (el, t, s) => {
        const a = lineStart(s, 'a-exam');
        const l = s.lines.find((x) => x.id === 'a-exam');
        const p = clamp((t - a) / (l.dur * 0.9));
        const text = s.data.answer;
        const shown = text.slice(0, Math.floor(text.length * p));
        $('#ans', el).innerHTML = esc(shown).replace(/(interpreter|statement by statement|interpreted language)/gi, '<b style="background:#fef08a">$1</b>') + (p < 1 && t >= a ? '<span style="color:#1e3a8a">|</span>' : '');
        $('#m1', el).style.opacity = p > 0.45 ? 1 : 0;
        $('#m2', el).style.opacity = p >= 1 ? 1 : 0;
      },
    },

    summary: {
      build: (s) => `
        <div class="card" style="background:linear-gradient(160deg,#ecfdf5,#fff 60%)">
          <p class="kicker" style="position:absolute;left:60px;top:56px;color:#059669">ನೆನಪಿಡಿ · Remember</p>
          <div style="position:absolute;left:60px;right:60px;top:140px;display:flex;flex-direction:column;gap:26px">
            ${s.data.points.map((p, i) => `<div class="pop pt" data-i="${i}" style="display:flex;gap:26px;align-items:flex-start;background:#fff;border:3px solid #a7f3d0;border-radius:28px;padding:30px 34px;opacity:0">
              <span style="flex:none;width:60px;height:60px;border-radius:50%;background:#10b981;color:#fff;display:grid;place-items:center;font-family:var(--head);font-weight:800;font-size:30px">${i + 1}</span>
              <p style="font-size:38px;line-height:1.4">${esc(p)}</p></div>`).join('')}
          </div>
        </div>`,
      update: (el, t, s) => {
        const l = s.lines[0];
        el.querySelectorAll('.pt').forEach((n, i) => enter(n, prog(t, l.start + i * (l.dur / 3), 0.6), 30));
      },
    },

    end: {
      build: (s) => `
        <div class="card" style="background:linear-gradient(150deg,#4f46e5,#6d28d9);color:#fff">
          <div style="position:absolute;left:70px;top:90px;width:700px">
            <p class="kicker" style="color:#c7d2fe">Practise this lesson free</p>
            <h2 class="h1 pop" id="e1" style="font-size:70px;margin-top:18px">ಈಗಲೇ ನಿಮ್ಮ phone ನಲ್ಲಿ practice ಮಾಡಿ</h2>
            <p class="pop" id="e2" style="margin-top:34px;font-family:var(--mono);font-size:34px;background:rgba(255,255,255,.12);border-radius:16px;padding:14px 22px;width:fit-content">${esc(s.data.url)}</p>
            <div class="pop" id="e3" style="margin-top:44px;display:flex;align-items:center;gap:18px;background:#fff;color:#0f172a;border-radius:24px;padding:20px 26px;width:fit-content">
              <span style="font-size:40px">▶</span><div><p class="muted" style="font-size:22px;font-weight:600">Next</p><p style="font-family:var(--head);font-weight:800;font-size:32px">Lesson 1.2</p></div>
            </div>
          </div>
          <div class="pop" id="e4" style="position:absolute;right:80px;top:150px;background:#fff;border-radius:36px;padding:26px;box-shadow:0 30px 60px rgba(0,0,0,.3)">
            <img src="${s.data.qrImage}" style="width:360px;height:360px;display:block" />
            <p style="text-align:center;color:#0f172a;font-weight:700;font-size:26px;margin-top:12px">Scan to practise</p>
          </div>
        </div>`,
      update: (el, t, s) => {
        ['e1', 'e2', 'e3', 'e4'].forEach((id, i) => enter($(`#${id}`, el), prog(t, s.start + 0.4 + i * 0.3, 0.6)));
      },
    },
  };

  // ---------- frame ----------
  window.setupVideo = (timeline) => {
    T = timeline;
    $('#lessonChip').textContent = `BP101T · Lesson ${T.lesson} · ಕನ್ನಡ`;
    setupCast();
    const bar = $('#progress');
    T.scenes.slice(1).forEach((s) => bar.insertAdjacentHTML('beforeend', `<div class="tick" style="left:${(s.start / T.duration) * 100}%"></div>`));
  };

  window.renderAt = (t) => {
    const scene = T.scenes.find((s) => t >= s.start && t < s.end) || T.scenes[T.scenes.length - 1];
    if (!current || current.scene !== scene) {
      $('#stage').innerHTML = SCENES[scene.type].build(scene);
      current = { scene, el: $('#stage') };
    }
    // scene crossfade
    const fadeIn = prog(t, scene.start, 0.45);
    const fadeOut = 1 - clamp((t - (scene.end - 0.3)) / 0.3);
    const stage = $('#stage');
    stage.style.opacity = scene.type === 'intro' ? 1 : Math.min(fadeIn, scene === T.scenes[T.scenes.length - 1] ? 1 : fadeOut);
    stage.style.transform = `translateY(${(1 - fadeIn) * 24}px)`;
    SCENES[scene.type].update(stage, t, scene);
    $('#chapter').textContent = scene.chapter;
    $('#chapter').style.opacity = scene.type === 'intro' ? 0 : 1;
    const line = speakingAt(t);
    animateCast(t, line);
    subtitles(t, line);
    // cast slides in during the intro
    const castIn = prog(t, 0.6, 0.9);
    $('#cast').style.transform = `translateX(${(1 - castIn) * 480}px)`;
    $('.fill', $('#progress')).style.width = `${(t / T.duration) * 100}%`;
  };
})();
