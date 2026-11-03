// Data-driven lesson episodes (Unit I lessons 1.2 onwards). Every scene reads its words, code and
// animation from T().data, written by tools/videos/unit1_build.py, so one set of scenes serves
// every lesson and language. Shared sting, quiz and end card come from scenes.js.
window.addScenes(({ $, $$, clamp, ap, lerp, esc, show, pop, S, E, bg, T }) => {
  const D = (k) => (T().data || {})[k] || {};
  const dur = (s, k) => (s.lines[k] || {}).dur || 1;
  const COL = { amber: '#fbbf24', emerald: '#34d399', indigo: '#818cf8', rose: '#fb7185' };
  const KW = /\b(print|input|int|float|str|bool|type|len|range|import|from|as|def|return|if|elif|else|for|while|in|and|or|not|True|False|None|round)\b/g;

  // light syntax colouring: strings, numbers, keywords, comments
  const hl = (line) => {
    const out = [];
    let i = 0;
    const src = line;
    const push = (txt, c) => out.push(c ? `<span style="color:${c}">${esc(txt)}</span>` : esc(txt));
    while (i < src.length) {
      const ch = src[i];
      if (ch === '#') { push(src.slice(i), '#64748b'); break; }
      if (ch === '"' || ch === "'") {
        let j = i + 1;
        while (j < src.length && src[j] !== ch) j++;
        push(src.slice(i, j + 1), '#86efac'); i = j + 1; continue;
      }
      const m = /^[A-Za-z_]\w*|^\d+(\.\d+)?/.exec(src.slice(i));
      if (m) {
        const w = m[0];
        if (/^\d/.test(w)) push(w, '#fdba74');
        else if (w.match(KW) && w.match(KW)[0] === w) push(w, '#7dd3fc');
        else push(w, '');
        i += w.length; continue;
      }
      push(ch, ''); i++;
    }
    return out.join('');
  };
  const fontFor = (lines, width, max = 34) => Math.max(20, Math.min(max, Math.floor((width - 120) / (Math.max(...lines.map((l) => l.length), 10) * 0.61))));
  const editor = (id, x, y, w, file, code, opts = {}) => {
    const rows = code.split('\n');
    const fs = fontFor(rows, w, opts.max || 34);
    const rh = Math.round(fs * 1.9);
    return { rh, top: y, html: `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;opacity:0;border-radius:28px;background:#0b1023;border:1.5px solid #2b3466;box-shadow:0 30px 70px rgba(0,0,0,.5);overflow:hidden">
      <div style="display:flex;align-items:center;gap:10px;padding:16px 24px;background:#111633;border-bottom:1.5px solid #1e293b"><i style="width:14px;height:14px;border-radius:50%;background:#fb7185"></i><i style="width:14px;height:14px;border-radius:50%;background:#fbbf24"></i><i style="width:14px;height:14px;border-radius:50%;background:#34d399"></i><span style="margin-left:12px;color:#94a3b8;font-family:var(--mono);font-variant-ligatures:none;font-size:22px">${esc(file)}</span></div>
      <div style="padding:16px 0">${rows.map((r, i) => `<div class="row" data-i="${i}" style="height:${rh}px;display:flex;align-items:center;padding:0 26px;font-family:var(--mono);font-variant-ligatures:none;font-size:${fs}px;color:#e2e8f0;white-space:pre">${opts.prompt ? '<span style="color:#34d399">$ </span>' : `<span style="width:${fs * 1.4}px;flex:none;color:#475569">${i + 1}</span>`}${opts.prompt ? esc(r) : hl(r)}</div>`).join('')}</div></div>` };
  };
  const consoleBox = (id, x, y, w, h, title) => `<div id="${id}" class="abs" style="left:${x}px;top:${y}px;width:${w}px;opacity:0;border-radius:28px;background:#020617;border:1.5px solid #1e293b;overflow:hidden">
      <div style="padding:16px 24px;background:#0f172a;color:#94a3b8;font-family:var(--head);font-weight:700;font-size:24px">${esc(title || D('output') || 'Output')}</div>
      <div class="out" style="padding:20px 24px;font-family:var(--mono);font-variant-ligatures:none;font-size:30px;line-height:1.6;color:#e2e8f0;height:${h}px;white-space:pre-wrap;overflow:hidden"></div></div>`;
  const glowRow = (n, p, rgb) => { if (!n) return; n.style.background = `rgba(${rgb},${0.22 * p})`; n.style.boxShadow = p > 0 ? `inset 6px 0 0 rgba(${rgb},${p})` : 'none'; };
  const voiceName = () => { const v = document.querySelector('#voice'); if (v && T().voiceName && v.lastChild.nodeType === 3) v.lastChild.textContent = T().voiceName; };

  // ---------- hook ----------
  const hook = {
    build: () => {
      voiceName();
      const d = D('hook');
      return `${bg(['#1e1b4b', '#12103a', '#06051a'])}
        <div id="ic" class="abs" style="left:150px;top:190px;width:150px;height:150px;border-radius:40px;background:linear-gradient(140deg,#6366f1,#7c3aed 55%,#2dd4bf);display:grid;place-items:center;font-size:84px;opacity:0;box-shadow:0 30px 80px rgba(99,102,241,.35)">${d.icon || ''}</div>
        <p id="lb" class="abs" style="left:340px;top:205px;font-family:var(--head);font-weight:700;font-size:30px;color:#a5b4fc;opacity:0">${esc(d.label || '')}</p>
        <h1 id="ti" class="abs h" style="left:340px;top:250px;width:1420px;font-size:76px;line-height:1.1;color:#fff;opacity:0">${esc(d.title || '')}</h1>
        <p id="lt" class="abs" style="left:150px;top:470px;font-family:var(--head);font-weight:700;font-size:30px;color:#99f6e4;opacity:0">${esc(d.learnT || '')}</p>
        <div class="abs" style="left:150px;right:150px;top:530px;display:flex;flex-direction:column;gap:18px">
          ${(d.learn || []).map((x, i) => `<div class="step ln" data-i="${i}" style="opacity:0;font-size:34px"><span class="n">${i + 1}</span><span>${esc(x)}</span></div>`).join('')}
        </div>`;
    },
    update: (el, t, s) => {
      pop($('#ic', el), ap(t, s.start + 0.2, 0.6));
      show($('#lb', el), ap(t, s.start + 0.4, 0.5), 14, 1);
      show($('#ti', el), ap(t, s.start + 0.5, 0.7), 24, 1);
      show($('#lt', el), ap(t, S(s, 1) - 0.2, 0.5), 14, 1);
      $$('.ln', el).forEach((n, i) => show(n, ap(t, S(s, 1) + i * dur(s, 1) * 0.28, 0.5), 24, 0.97));
    },
  };

  // ---------- the lesson's own animation, replayed from its actors and steps ----------
  const lanim = {
    build: () => {
      voiceName();
      const d = D('lanim');
      const actor = (a) => {
        const p = a.desktop, c = COL[a.color] || '#818cf8';
        const base = `position:absolute;left:${p.x}px;top:${p.y}px;width:${p.w}px;height:${p.h}px;opacity:0`;
        if (a.type === 'box') return `<div class="act" data-id="${a.id}" style="${base};border-radius:16px;background:rgba(255,255,255,.06);border:2px solid ${c};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px">
            <span style="font-family:var(--head);font-weight:700;font-size:15px;color:${c}">${esc(a.label || '')}</span>
            <span class="val" style="font-family:var(--mono);font-variant-ligatures:none;font-weight:700;font-size:${Math.min(30, p.h * 0.3)}px;color:#fff;white-space:nowrap">${esc(a.value || '')}</span></div>`;
        if (a.type === 'pill') return `<div class="act" data-id="${a.id}" style="${base};border-radius:999px;background:${c}2e;border:1.5px solid ${c};display:grid;place-items:center;font-family:var(--head);font-weight:700;font-size:${Math.min(16, p.h * 0.55)}px;color:#fff;white-space:nowrap">${esc(a.text || '')}</div>`;
        if (a.type === 'text') return `<div class="act" data-id="${a.id}" style="${base};display:flex;align-items:center;justify-content:center;text-align:center;font-family:var(--mono);font-variant-ligatures:none;font-size:${(a.size || 18) * 0.95}px;color:#e2e8f0">${esc(a.text || '')}</div>`;
        if (a.type === 'terminal') return `<div class="act" data-id="${a.id}" style="${base};border-radius:14px;background:#020617;border:1.5px solid #1e293b;overflow:hidden">
            <div style="padding:6px 12px;background:#0f172a;color:#94a3b8;font-family:var(--head);font-weight:700;font-size:13px">${esc(a.title || 'Output')}</div>
            <div class="tout" style="padding:8px 12px;font-family:var(--mono);font-variant-ligatures:none;font-size:16px;line-height:1.5;color:#e2e8f0;white-space:pre-wrap"></div></div>`;
        // card
        const lines = a.lines || [];
        const lh = Math.max(16, Math.min(34, (p.h - 46) / Math.max(1, lines.length)));
        return `<div class="act" data-id="${a.id}" style="${base};border-radius:16px;background:#0b1023;border:1.5px solid ${c};overflow:hidden">
            <div style="display:flex;align-items:center;gap:8px;padding:8px 12px;background:${c}26;color:#fff;font-family:var(--head);font-weight:700;font-size:15px"><span>${a.icon || ''}</span>${esc(a.title || '')}</div>
            <div style="padding:6px 0">${lines.map((l, i) => `<div class="cl" data-i="${i}" style="height:${lh}px;display:flex;align-items:center;padding:0 12px;font-family:${a.mono ? 'var(--mono)' : 'var(--body)'};font-variant-ligatures:none;font-size:${Math.min(16, lh * 0.62)}px;color:#e2e8f0;white-space:pre">${a.mono ? hl(l) : esc(l)}</div>`).join('')}</div></div>`;
      };
      return `${bg(['#0f2a4a', '#0a1a33', '#040b18'])}
        <svg id="wires" class="abs" style="left:320px;top:120px;width:1280px;height:736px;overflow:visible" viewBox="0 0 800 460"></svg>
        <div id="cv" class="abs" style="left:320px;top:120px;width:800px;height:460px;transform:scale(1.6);transform-origin:0 0">${d.actors.map(actor).join('')}</div>`;
    },
    update: (el, t, s) => {
      const d = D('lanim');
      const st = {};
      d.actors.forEach((a) => (st[a.id] = { show: 0, value: a.value, out: [], hl: -1, pulse: 0 }));
      const shownEver = new Set();
      d.steps.forEach((x) => x.actions.forEach((a) => a.do === 'show' && shownEver.add(a.target)));
      d.actors.forEach((a) => { if (!shownEver.has(a.id)) st[a.id].show = ap(t, s.start + 0.2, 0.5); });
      const wires = [];
      d.steps.forEach((step, k) => {
        const a0 = S(s, k);
        if (t < a0 - 0.1) return;
        const dt = t - a0, dd = dur(s, k);
        step.actions.forEach((a) => {
          const x = st[a.target];
          if (a.do === 'show' && x) x.show = Math.max(x.show, ap(t, a0 + 0.1, 0.5));
          if (a.do === 'hide' && x) x.show = Math.min(x.show, 1 - ap(t, a0 + 0.1, 0.4));
          if (a.do === 'setValue' && x && dt > 0.35) x.value = a.value;
          if (a.do === 'appendOutput' && x && dt > dd * 0.45) x.out.push(a.text);
          if (a.do === 'highlightLine' && x) x.hl = a.line;
          if (a.do === 'scanLines' && x) {
            const n = (d.actors.find((q) => q.id === a.target).lines || []).length;
            x.hl = Math.min(n - 1, Math.floor(dt / ((a.intervalMs || 800) / 1000)));
          }
          if (a.do === 'pulse' && x) x.pulse = Math.max(x.pulse, dt < 1 ? Math.sin(clamp(dt / 0.8) * Math.PI) : 0);
          if (a.do === 'connect') wires.push({ ...a, p: ap(t, a0 + 0.2, 0.7) });
        });
      });
      $$('.act', el).forEach((n) => {
        const x = st[n.dataset.id];
        n.style.opacity = x.show;
        n.style.transform = `translateY(${(1 - x.show) * 12}px) scale(${1 + 0.06 * x.pulse})`;
        const v = $('.val', n);
        if (v) v.textContent = x.value;
        const o = $('.tout', n);
        if (o) o.textContent = x.out.join('\n');
        $$('.cl', n).forEach((r, i) => glowRow(r, i === x.hl ? 1 : 0, '253,230,138'));
      });
      const pos = (id) => { const a = d.actors.find((q) => q.id === id); return a ? a.desktop : null; };
      $('#wires', el).innerHTML = wires.map((w) => {
        const a = pos(w.from), b = pos(w.to);
        if (!a || !b) return '';
        const x1 = a.x + a.w, y1 = a.y + a.h / 2, x2 = b.x, y2 = b.y + b.h / 2;
        const ax = b.x > a.x + a.w ? [x1, y1, x2, y2] : [a.x + a.w / 2, a.y + a.h, b.x + b.w / 2, b.y];
        const L = Math.hypot(ax[2] - ax[0], ax[3] - ax[1]);
        const c = COL[w.color] || '#a5b4fc';
        return `<line x1="${ax[0]}" y1="${ax[1]}" x2="${ax[2]}" y2="${ax[3]}" stroke="${c}" stroke-width="3" stroke-dasharray="${L}" stroke-dashoffset="${L * (1 - w.p)}"/>` +
          (w.label ? `<text x="${(ax[0] + ax[2]) / 2}" y="${(ax[1] + ax[3]) / 2 - 8}" fill="#fff" font-size="14" font-family="Plus Jakarta Sans" text-anchor="middle" opacity="${w.p}">${esc(w.label)}</text>` : '');
      }).join('');
    },
  };

  // ---------- a key idea: heading, code and its output (or points) ----------
  const concept = (key) => ({
    build: () => {
      voiceName();
      const d = D(key);
      let body = '';
      if (d.mode === 'points') {
        body = `<div class="abs" style="left:150px;right:150px;top:330px;display:flex;flex-direction:column;gap:24px">
          ${d.points.map((p, i) => `<div class="step pt" data-i="${i}" style="opacity:0;font-size:40px"><span class="n">${i + 1}</span><span>${esc(p)}</span></div>`).join('')}</div>`;
      } else if (d.mode === 'terminal') {
        const ed = editor('ed', 150, 320, 1100, d.file, d.code, { prompt: true, max: 40 });
        body = ed.html;
      } else {
        const ed = editor('ed', 120, 300, 1060, d.file, d.code);
        body = ed.html + consoleBox('con', 1230, 300, 570, Math.max(200, d.code.split('\n').length * 58));
      }
      return `${bg(['#123a5c', '#0b2440', '#050f1f'])}
        <p id="kk" class="abs" style="left:150px;top:150px;font-family:var(--head);font-weight:700;font-size:28px;color:#7dd3fc;opacity:0">${esc(d.idea || '')}</p>
        <h2 id="hh" class="abs h" style="left:150px;top:190px;width:1620px;font-size:62px;line-height:1.1;color:#fff;opacity:0">${esc(d.heading || '')}</h2>
        ${body}
        ${d.callout ? `<div id="co" class="abs tag" style="left:150px;top:${d.mode === 'points' ? 700 : 740}px;max-width:1620px;white-space:normal;font-size:28px;opacity:0;background:rgba(253,230,138,.12);border-color:#fde68a;color:#fef3c7">💡 ${esc(d.callout)}</div>` : ''}`;
    },
    update: (el, t, s) => {
      const d = D(key);
      show($('#kk', el), ap(t, s.start + 0.15, 0.5), 12, 1);
      show($('#hh', el), ap(t, s.start + 0.25, 0.6), 20, 1);
      const a0 = S(s, 0), dd = dur(s, 0);
      if (d.mode === 'points') $$('.pt', el).forEach((n, i) => show(n, ap(t, a0 + (i * dd) / Math.max(1, d.points.length) * 0.85, 0.5), 24, 0.97));
      else {
        show($('#ed', el), ap(t, s.start + 0.4, 0.6), 24, 0.98);
        const rows = $$('.row', el);
        const per = (dd * 0.7) / Math.max(1, rows.length);
        rows.forEach((r, i) => glowRow(r, t > a0 + i * per && t < a0 + (i + 1) * per + 0.2 ? 1 : 0, '253,230,138'));
        if ($('#con', el)) {
          show($('#con', el), ap(t, s.start + 0.6, 0.6), 24, 0.98);
          const outs = (d.output || '').split('\n');
          const n = Math.floor(clamp((t - a0 - dd * 0.25) / (dd * 0.55)) * outs.length + (t > a0 + dd * 0.25 ? 1 : 0));
          $('#con .out', el).textContent = outs.slice(0, Math.min(outs.length, n)).join('\n');
        }
      }
      if ($('#co', el)) show($('#co', el), ap(t, a0 + dd * 0.6, 0.6), 16, 1);
    },
  });

  // ---------- the walkthrough: the program runs line by line ----------
  const lwalk = {
    build: () => {
      voiceName();
      const d = D('lwalk');
      const ed = editor('ed', 110, 140, 1110, d.file, d.code);
      return `${bg(['#1e1b4b', '#12103a', '#06051a'])}
        ${ed.html}
        <div id="vars" class="abs" style="left:1260px;top:140px;width:550px;opacity:0;border-radius:28px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14);overflow:hidden">
          <div style="padding:16px 24px;background:rgba(255,255,255,.06);color:#c7d2fe;font-family:var(--head);font-weight:700;font-size:24px">${esc(d.varsT || 'Variables')}</div>
          <div class="vl" style="padding:14px 24px;min-height:200px;display:flex;flex-direction:column;gap:10px"></div></div>
        ${consoleBox('con', 1260, 470, 550, 290, d.outT)}
        <div id="ptr" class="abs" style="left:66px;top:0;opacity:0;width:40px;height:40px;border-radius:50%;background:#fde68a;color:#1f2937;display:grid;place-items:center;font-weight:800;font-size:18px;box-shadow:0 10px 30px rgba(0,0,0,.35)">▶</div>`;
    },
    update: (el, t, s) => {
      const d = D('lwalk');
      show($('#ed', el), ap(t, s.start + 0.2, 0.6), 24, 0.98);
      show($('#vars', el), ap(t, s.start + 0.4, 0.6), 24, 0.98);
      show($('#con', el), ap(t, s.start + 0.5, 0.6), 24, 0.98);
      const rows = $$('.row', el);
      const rh = rows.length ? rows[0].offsetHeight : 60;
      let cur = -1;
      const vars = {}, outs = [];
      d.steps.forEach((st, k) => {
        const a0 = S(s, k);
        if (t < a0) return;
        if (st.line) cur = st.line - 1;
        Object.assign(vars, st.vars || {});
        if (st.output && t > a0 + dur(s, k) * 0.5) outs.push(st.output);
      });
      rows.forEach((r, i) => glowRow(r, i === cur ? 1 : 0, '253,230,138'));
      const ptr = $('#ptr', el);
      ptr.style.opacity = cur >= 0 ? 1 : 0;
      ptr.style.top = `${140 + 64 + 16 + cur * rh + (rh - 40) / 2}px`;
      $('#vars .vl', el).innerHTML = Object.entries(vars).map(([k, v]) => `<div style="display:flex;gap:14px;align-items:baseline;font-family:var(--mono);font-variant-ligatures:none;font-size:${String(v).length > 22 ? 22 : 28}px;color:#e2e8f0"><span style="color:#a5b4fc">${esc(k)}</span><span style="color:#64748b">=</span><span style="color:#fef3c7;white-space:pre">${esc(v)}</span></div>`).join('');
      const o = $('#con .out', el);
      o.textContent = outs.join('\n');
      o.style.fontSize = outs.length > 7 ? '22px' : '28px';
    },
  };

  // ---------- an error: the line that breaks, and Python's message ----------
  const error = (key) => ({
    build: () => {
      voiceName();
      const d = D(key);
      const ed = editor('ed', 150, 280, 1620, 'error.py', d.code, { max: 38 });
      return `${bg(['#4a1430', '#2a0b1c', '#12040c'])}
        <h2 id="hh" class="abs h" style="left:150px;top:150px;width:1620px;font-size:56px;line-height:1.1;color:#fff;opacity:0">⚠️ ${esc(d.title || '')}</h2>
        ${ed.html}
        <div id="msg" class="abs" style="left:150px;top:${280 + 64 + 32 + d.code.split('\n').length * ed.rh + 30}px;width:1620px;opacity:0;border-radius:24px;background:#2a0712;border:2px solid #fb7185;padding:22px 30px;font-family:var(--mono);font-variant-ligatures:none;font-size:${d.output.length > 70 ? 26 : 32}px;color:#fecdd3">${esc(d.output)}</div>`;
    },
    update: (el, t, s) => {
      const d = D(key);
      show($('#hh', el), ap(t, s.start + 0.2, 0.6), 20, 1);
      show($('#ed', el), ap(t, s.start + 0.4, 0.6), 24, 0.98);
      const a0 = S(s, 0), dd = dur(s, 0);
      const on = ap(t, a0 + dd * 0.15, 0.5);
      $$('.row', el).forEach((r, i) => glowRow(r, i === d.errorLine - 1 ? on : 0, '251,113,133'));
      show($('#msg', el), ap(t, a0 + dd * 0.25, 0.5), 16, 0.98);
    },
  });

  // ---------- recap ----------
  const lrecap = {
    build: () => {
      voiceName();
      const d = D('lrecap');
      return `${bg(['#065f46', '#053b33', '#03201d'])}
        <p class="abs h" id="rt" style="left:150px;top:140px;font-size:60px;color:#fff;opacity:0">${esc(d.title || 'Recap')}</p>
        <div class="abs" style="left:150px;right:150px;top:250px;display:flex;flex-direction:column;gap:20px">
          ${(d.items || []).map((p, i) => `<div class="rp" style="opacity:0;display:flex;gap:24px;align-items:center;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.16);border-radius:26px;padding:20px 30px">
            <span style="flex:none;width:58px;height:58px;border-radius:50%;background:#34d399;color:#03201d;display:grid;place-items:center;font-family:var(--head);font-weight:800;font-size:28px">${i + 1}</span>
            <span style="font-size:${p.length > 110 ? 28 : 32}px;line-height:1.3;color:#fff;font-weight:600">${esc(p)}</span></div>`).join('')}
        </div>`;
    },
    update: (el, t, s) => {
      show($('#rt', el), ap(t, s.start + 0.2, 0.5), 20, 1);
      $$('.rp', el).forEach((n, i) => show(n, ap(t, S(s, i + 1), 0.6), 30, 0.96));
    },
  };

  return { lhook: hook, lanim, c1: concept('c1'), c2: concept('c2'), c3: concept('c3'), lwalk, e1: error('e1'), e2: error('e2'), lrecap };
});
