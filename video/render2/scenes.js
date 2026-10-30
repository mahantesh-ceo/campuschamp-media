// Episode renderer: draws any frame at time t. Teaching scenes are illustrated, full-bleed
// worlds (Kurzgesagt-style); the sting and end card are clean brand moments (Apple-style).
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const clamp = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
  const ease = (x) => { x = clamp(x); return 1 - Math.pow(1 - x, 3); };
  const easeIO = (x) => { x = clamp(x); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  const ap = (t, a, d = 0.6) => ease((t - a) / d);
  const lerp = (a, b, p) => a + (b - a) * p;
  const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c]);
  const show = (el, p, dy = 30, sc = 0.94) => {
    if (!el) return;
    el.style.opacity = p;
    el.style.transform = `translateY(${(1 - p) * dy}px) scale(${lerp(sc, 1, p)})`;
  };
  const pop = (el, p) => { if (!el) return; el.style.opacity = clamp(p * 1.4); el.style.transform = `scale(${p < 1 ? lerp(0.4, 1.08, p) - (p > 0.8 ? (p - 0.8) * 0.4 : 0) : 1})`; };

  let T;
  // on-screen words per language (the narration lives in video/episodes/*.<lang>.json)
  const STR = {
    "kn": {
      "kick": "ಸೋಮವಾರ · 9:00 AM · ಬಾಗಲಕೋಟೆ",
      "head": "ನೀವು ಈಗಾಗಲೇ <span style=\"color:#fbbf24\">programmer</span> ತರಹ ಯೋಚಿಸ್ತೀರಿ.",
      "head2": "ಅದು ನಿಮಗೆ ಇನ್ನೂ ಗೊತ್ತಿಲ್ಲ ಅಷ್ಟೇ.",
      "clinic": "City Clinic · Bagalkot",
      "title": "Program <span class=\"grad\">ಅಂದ್ರೆ ಏನು?</span>",
      "langName": "ಕನ್ನಡ",
      "labels": [
        "ಸ್ಪಷ್ಟವಾಗಿ",
        "ಕ್ರಮವಾಗಿ",
        "ಬರೆದ ಹಾಗೆಯೇ"
      ],
      "call": "📞 Doctor ಗೆ call ಮಾಡಿ ಕೇಳ್ತಾರೆ",
      "danger": "⚠️ ಚಿಕ್ಕ confusion ಕೂಡ ಅಪಾಯ",
      "okSub": "ಅದಕ್ಕೇ prescriptions ಹೀಗೆ ಬರೀತಾರೆ.",
      "note": "Tablets count ಮಾಡು",
      "steps": [
        "Strip ನೋಡು",
        "Zero ಇಂದ ಶುರು ಮಾಡು",
        "ಪ್ರತಿ tablet ಗೆ 1 ಸೇರಿಸು",
        "Total ತೋರಿಸು"
      ],
      "named": "ಇದಕ್ಕೆ ಒಂದು ಹೆಸರಿದೆ",
      "def": "Order ನಲ್ಲಿ ಬರೆದ, computer <b style=\"color:#fde68a\">exactly</b> follow ಮಾಡುವ, <b style=\"color:#fde68a\">clear instructions</b> ನ list.",
      "dose": "Dose ತೋರಿಸು:",
      "meant": "ಬರೆಯಬೇಕಿತ್ತು: 1",
      "shown": "Computer ತೋರಿಸಿದ್ದು",
      "detail": "🔍 ಚಿಕ್ಕ details ತುಂಬಾ ಮುಖ್ಯ",
      "err": "ಈ line ನನಗೆ ಅರ್ಥ ಆಗಲಿಲ್ಲ.",
      "you": "ಸ್ವಲ್ಪ ದಿನದಲ್ಲೇ, <span style=\"color:#2dd4bf\">ನೀವೂ</span> ಬರೀತೀರಿ ✍️",
      "quizQ": "ಇವುಗಳಲ್ಲಿ program ಯಾವುದು?",
      "quizB": "Computer order ನಲ್ಲಿ follow ಮಾಡುವ clear instructions ನ list",
      "recap": [
        "Program ಅಂದ್ರೆ, computer ಗಾಗಿ ಬರೆದ instructions ನ list.",
        "Instructions clear ಆಗಿರಬೇಕು, order ನಲ್ಲಿರಬೇಕು.",
        "Computer ಅವನ್ನು exactly follow ಮಾಡುತ್ತೆ. Guess ಮಾಡಲ್ಲ."
      ],
      "hello2": "ನಮಸ್ಕಾರ computer! 🙏",
      "why": "Python <span style=\"color:#fde68a\">ಯಾಕೆ?</span>",
      "whyBrand": "Python <span class=\"grad\">ಯಾಕೆ?</span>",
      "nextEp": "ಮುಂದಿನ episode",
      "nextDesc": "Computer ಗೆ ಅರ್ಥ ಆಗುವ ಭಾಷೆಯಲ್ಲಿ instructions ಹೇಗೆ ಬರೆಯೋದು."
    },
    "hi": {
      "kick": "सोमवार · 9:00 AM · लखनऊ",
      "head": "आप पहले से ही <span style=\"color:#fbbf24\">programmer</span> की तरह सोचते हैं.",
      "head2": "बस अभी आपको इसका पता नहीं है.",
      "clinic": "City Clinic · Lucknow",
      "title": "Program <span class=\"grad\">क्या है?</span>",
      "langName": "हिन्दी",
      "labels": [
        "साफ़-साफ़",
        "क्रम से",
        "जैसा लिखा, वैसा ही"
      ],
      "call": "📞 Doctor को call करके पूछेंगे",
      "danger": "⚠️ छोटी सी confusion भी ख़तरनाक",
      "okSub": "इसीलिए prescriptions ऐसे लिखे जाते हैं.",
      "note": "Tablets count करो",
      "steps": [
        "Strip देखो",
        "Zero से शुरू करो",
        "हर tablet पर 1 जोड़ो",
        "Total दिखाओ"
      ],
      "named": "इसका एक नाम है",
      "def": "Order में लिखी, <b style=\"color:#fde68a\">clear instructions</b> की list, जिसे computer <b style=\"color:#fde68a\">exactly</b> follow करता है.",
      "dose": "Dose दिखाओ:",
      "meant": "लिखना था: 1",
      "shown": "Computer ने दिखाया",
      "detail": "🔍 छोटी details बहुत ज़रूरी",
      "err": "ये line मुझे समझ नहीं आई.",
      "you": "बहुत जल्द, <span style=\"color:#2dd4bf\">आप भी</span> लिखेंगे ✍️",
      "quizQ": "इनमें से program कौन सा है?",
      "quizB": "Clear instructions की list, जिसे computer order में follow करता है",
      "recap": [
        "Program मतलब, computer के लिए लिखी instructions की list.",
        "Instructions clear होनी चाहिए, order में होनी चाहिए.",
        "Computer उन्हें exactly follow करता है. Guess नहीं करता."
      ],
      "hello2": "नमस्ते computer! 🙏",
      "why": "Python <span style=\"color:#fde68a\">क्यों?</span>",
      "whyBrand": "Python <span class=\"grad\">क्यों?</span>",
      "nextEp": "अगला episode",
      "nextDesc": "Computer को समझ आने वाली भाषा में instructions कैसे लिखें."
    },
    "en": {
      "kick": "Monday · 9:00 AM · Bagalkot",
      "head": "You already think like a <span style=\"color:#fbbf24\">programmer</span>.",
      "head2": "You just don't know it yet.",
      "clinic": "City Clinic · Bagalkot",
      "title": "What is a <span class=\"grad\">program?</span>",
      "langName": "English",
      "labels": [
        "Nothing left to guess",
        "One step after another",
        "No changes, no guessing"
      ],
      "call": "📞 Call the doctor and ask",
      "danger": "⚠️ Even a small confusion is dangerous",
      "okSub": "That's why prescriptions are written this way.",
      "note": "Count the tablets",
      "steps": [
        "Look at the strip",
        "Start from zero",
        "Add 1 for each tablet",
        "Show the total"
      ],
      "named": "This has a name",
      "def": "A list of <b style=\"color:#fde68a\">clear instructions</b>, written in order, that the computer follows <b style=\"color:#fde68a\">exactly</b>.",
      "dose": "Show dose:",
      "meant": "Meant: 1",
      "shown": "Computer shows",
      "detail": "🔍 Small details matter",
      "err": "I don't understand this line.",
      "you": "Soon, <span style=\"color:#2dd4bf\">you</span> will write them too ✍️",
      "quizQ": "Which of these is a program?",
      "quizB": "A list of clear instructions the computer follows in order",
      "recap": [
        "A program is a list of instructions written for a computer.",
        "The instructions must be clear, and in order.",
        "The computer follows them exactly. It doesn't guess."
      ],
      "hello2": "Namaste computer! 🙏",
      "why": "<span style=\"color:#fde68a\">Why</span> Python?",
      "whyBrand": "<span class=\"grad\">Why</span> Python?",
      "nextEp": "Next episode",
      "nextDesc": "How to write instructions in a language the computer understands."
    }
  };
  const tx = (k) => (STR[T.lang] || STR.kn)[k];
  let cur = null;
  // line helpers for the current scene: start / end of the k-th sentence
  const S = (s, k) => (s.lines[k] ? s.lines[k].start : Infinity);
  const E = (s, k) => (s.lines[k] ? s.lines[k].start + s.lines[k].dur : Infinity);
  const byId = (s, id) => s.lines.find((l) => l.id === id);

  // ---------- reusable art ----------
  const prescription = (w = 820) => `
    <svg viewBox="0 0 820 760" style="width:${w}px;height:${(w * 760) / 820}px;overflow:visible">
      <rect width="820" height="760" rx="28" fill="#fffaf0"/>
      <rect width="820" height="120" rx="28" fill="#e6fffa"/><rect y="92" width="820" height="28" fill="#e6fffa"/>
      <text x="48" y="74" font-family="Plus Jakarta Sans" font-weight="800" font-size="34" fill="#0f766e">${tx('clinic')}</text>
      <text x="48" y="230" font-family="Plus Jakarta Sans" font-weight="800" font-size="96" fill="#4f46e5">℞</text>
      ${[0, 1, 2].map((i) => `
        <g class="rxl" data-i="${i}">
          <rect class="hl" x="40" y="${276 + i * 120}" width="740" height="96" rx="18" fill="#fef3c7" opacity="0"/>
          <circle class="dot" cx="96" cy="${324 + i * 120}" r="30" fill="#e2e8f0"/>
          <text class="num" x="96" y="${336 + i * 120}" text-anchor="middle" font-family="Plus Jakarta Sans" font-weight="800" font-size="32" fill="#64748b">${i + 1}</text>
          <text class="txt" x="150" y="${338 + i * 120}" font-family="Inter" font-weight="600" font-size="42" fill="#334155">${['Paracetamol 500 mg', 'Take 1 tablet', '3 times a day, after food'][i]}</text>
        </g>`).join('')}
      <path d="M560 690 C 600 660, 640 700, 690 670 S 760 690, 780 664" fill="none" stroke="#334155" stroke-width="4" stroke-linecap="round"/>
    </svg>`;

  const chipSvg = (id) => `
    <svg viewBox="-200 -200 400 400" style="width:400px;height:400px;overflow:visible">
      <defs>
        <linearGradient id="ce${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a5b4fc"/><stop offset=".5" stop-color="#7c5cff"/><stop offset="1" stop-color="#2dd4bf"/></linearGradient>
        <linearGradient id="cf${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2b2f6b"/><stop offset="1" stop-color="#161a44"/></linearGradient>
        <filter id="cg${id}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        <filter id="cs${id}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      </defs>
      ${[-110, -55, 0, 55, 110].map((p) => `<rect x="${p - 10}" y="-200" width="20" height="40" rx="6" fill="#4c4fa8"/><rect x="${p - 10}" y="160" width="20" height="40" rx="6" fill="#4c4fa8"/><rect x="-200" y="${p - 10}" width="40" height="20" rx="6" fill="#4c4fa8"/><rect x="160" y="${p - 10}" width="40" height="20" rx="6" fill="#4c4fa8"/>`).join('')}
      <g class="edge" filter="url(#cg${id})"><rect x="-170" y="-170" width="340" height="340" rx="56" fill="url(#ce${id})"/></g>
      <rect x="-158" y="-158" width="316" height="316" rx="48" fill="url(#cf${id})"/>
      <g class="eyes" filter="url(#cs${id})"><rect class="eye" x="-70" y="-40" width="34" height="56" rx="17" fill="#e0e7ff"/><rect class="eye" x="36" y="-40" width="34" height="56" rx="17" fill="#e0e7ff"/></g>
      <path class="smile" d="M-40 70 Q 0 96 40 70" stroke="#e0e7ff" stroke-width="10" fill="none" stroke-linecap="round"/>
      <path class="flat" d="M-36 80 L 36 76" stroke="#e0e7ff" stroke-width="10" fill="none" stroke-linecap="round" opacity="0"/>
    </svg>`;
  function chipFace(root, t, mood) {
    // blink every ~3.4 s; mood: 'happy' | 'confused'
    const ph = t % 3.4;
    $$('.eye', root).forEach((e, i) => {
      const blink = ph < 0.12 ? 0.12 : 1;
      e.setAttribute('transform', mood === 'confused' ? `translate(${i ? 52 : -52} 12) rotate(${i ? 12 : -12}) scale(1 ${blink}) translate(${i ? -52 : 52} -12)` : `translate(0 ${(1 - blink) * 28}) scale(1 ${blink})`);
    });
    $('.smile', root).style.opacity = mood === 'confused' ? 0 : 1;
    $('.flat', root).style.opacity = mood === 'confused' ? 1 : 0;
  }

  const bg = (stops, extra = '') => `<svg class="art" viewBox="0 0 1920 1080"><defs><radialGradient id="g${stops[0].slice(1)}" cx=".5" cy=".42" r=".8">${stops.map((c, i) => `<stop offset="${i / (stops.length - 1)}" stop-color="${c}"/>`).join('')}</radialGradient><pattern id="dt" width="34" height="34" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="2" fill="#fff" opacity=".05"/></pattern></defs><rect width="1920" height="1080" fill="url(#g${stops[0].slice(1)})"/><rect width="1920" height="1080" fill="url(#dt)"/>${extra}</svg>`;

  // ---------- scenes ----------
  const SCENES = {
    cold: {
      build: () => `
        <div class="layer" id="cam">
          <svg class="art" viewBox="0 0 1920 1080">
            <defs>
              <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1330"/><stop offset="1" stop-color="#1b2150"/></linearGradient>
              <linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#26357f"/><stop offset=".55" stop-color="#8b6fd6"/><stop offset="1" stop-color="#ffb38a"/></linearGradient>
              <linearGradient id="cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd27a" stop-opacity=".55"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></linearGradient>
              <radialGradient id="pool" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd27a" stop-opacity=".45"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>
              <linearGradient id="counter" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f3b5c"/><stop offset="1" stop-color="#0d1a2e"/></linearGradient>
              <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="18" stdDeviation="16" flood-color="#000" flood-opacity=".45"/></filter>
            </defs>
            <rect width="1920" height="1080" fill="url(#wall)"/>
            <g transform="translate(1100 110)">
              <rect width="460" height="400" rx="30" fill="url(#dawn)"/>
              <circle id="sun" cx="300" cy="300" r="70" fill="#ffd9a0" opacity=".85"/>
              <path d="M0 330 C 80 300, 150 320, 220 300 C 290 280, 360 310, 460 290 L460 400 L0 400 Z" fill="#3a2f6e" opacity=".9"/>
              <path d="M0 360 C 100 340, 200 360, 300 345 C 380 335, 420 350, 460 345 L460 400 L0 400 Z" fill="#2a2257"/>
              <rect x="222" width="16" height="400" fill="#0b1330"/><rect y="192" width="460" height="16" fill="#0b1330"/>
              <rect width="460" height="400" rx="30" fill="none" stroke="#0b1330" stroke-width="18"/>
            </g>
            <g transform="translate(1680 210)">
              <circle r="78" fill="#f8fafc"/><circle r="78" fill="none" stroke="#334155" stroke-width="10"/>
              <line x1="0" y1="0" x2="-44" y2="0" stroke="#0f172a" stroke-width="9" stroke-linecap="round"/>
              <line id="minute" x1="0" y1="0" x2="0" y2="-58" stroke="#0f172a" stroke-width="6" stroke-linecap="round"/>
              <circle r="8" fill="#fb7185"/>
            </g>
            <g transform="translate(1560 340)">${(() => {
              const cols = ['#fb7185', '#2dd4bf', '#60a5fa', '#fbbf24', '#a78bfa', '#f472b6', '#34d399'];
              let h = '<rect width="380" height="420" fill="#101a3f"/>';
              for (let r = 0; r < 4; r++) {
                const y = 90 + r * 100;
                h += `<rect y="${y}" width="380" height="10" fill="#2a356e"/>`;
                for (let c = 0; c < 6; c++) {
                  const bh = 42 + ((r * 5 + c * 3) % 4) * 9, x = 22 + c * 60;
                  h += `<rect x="${x}" y="${y - bh}" width="40" height="${bh}" rx="8" fill="${cols[(r + c) % 7]}" opacity=".55"/><rect x="${x + 7}" y="${y - bh + 12}" width="26" height="10" rx="3" fill="#fff" opacity=".35"/>`;
                }
              }
              return h;
            })()}</g>
            <path d="M930 0 L930 150 L1000 300" stroke="#2b3566" stroke-width="16" fill="none" stroke-linecap="round"/>
            <path d="M920 290 L1080 300 L1050 345 L950 338 Z" fill="#3b4680"/>
            <polygon id="cone" points="950,340 1050,346 1330,800 690,800" fill="url(#cone)"/>
            <rect x="0" y="790" width="1920" height="290" fill="url(#counter)"/>
            <rect x="0" y="782" width="1920" height="14" fill="#2c5282"/>
            <ellipse id="pool" cx="1050" cy="800" rx="420" ry="60" fill="url(#pool)"/>
            <g id="pile">${Array.from({ length: 14 }, (_, i) => {
              const x = 1240 + (i % 5) * 26 - 40, y = 700 - Math.floor(i / 5) * 18 - (i % 3) * 6, r = ((i * 37) % 17) - 8;
              return `<rect class="pp" x="${x}" y="${y}" width="160" height="96" rx="8" fill="${['#e9e2d0', '#f2ecdc', '#fffaf0'][i % 3]}" transform="rotate(${r} ${x + 80} ${y + 48})" opacity="0"/>`;
            }).join('')}</g>
            <g filter="url(#shadow)">
              <g transform="translate(820 610) rotate(-9)"><rect width="300" height="220" rx="14" fill="#e9e2d0"/></g>
              <g transform="translate(860 600) rotate(5)"><rect width="300" height="220" rx="14" fill="#f2ecdc"/></g>
              <g transform="translate(900 580) rotate(-3)">
                <rect width="300" height="230" rx="14" fill="#fffaf0"/>
                <text x="26" y="62" font-family="Plus Jakarta Sans" font-weight="800" font-size="52" fill="#4f46e5">℞</text>
                <rect x="26" y="96" width="210" height="12" rx="6" fill="#cbd5e1"/><rect x="26" y="128" width="170" height="12" rx="6" fill="#cbd5e1"/><rect x="26" y="160" width="230" height="12" rx="6" fill="#cbd5e1"/>
              </g>
            </g>
          </svg>
        </div>
        <div class="abs" style="left:120px;top:250px;width:760px">
          <p id="kick" style="font-family:var(--head);font-weight:700;font-size:32px;color:#fbbf24">${tx('kick')}</p>
          <h1 id="head" class="h" style="margin-top:26px;font-size:76px;line-height:1.15;color:#fff6e5">${tx('head')}</h1>
          <p id="head2" style="margin-top:24px;font-size:40px;color:#c7cdf5">${tx('head2')}</p>
        </div>`,
      update: (el, t, s) => {
        const p = clamp((t - s.start) / (s.end - s.start));
        $('#cam', el).style.transform = `scale(${1 + p * 0.07}) translate(${-p * 30}px, ${-p * 12}px)`;
        show($('#kick', el), ap(t, s.start + 0.6, 0.8), 20, 1);
        $('#minute', el).setAttribute('transform', `rotate(${p * 30})`);
        $('#cone', el).style.opacity = 0.85 + Math.sin(t * 7) * 0.04;
        // prescriptions keep arriving while "200 prescriptions" is said
        $$('.pp', el).forEach((n, i) => (n.style.opacity = ap(t, S(s, 1) + i * 0.22, 0.4)));
        const h = E(s, 2) - 0.2;
        show($('#head', el), ap(t, h, 0.8), 30, 0.98);
        show($('#head2', el), ap(t, h + 0.6, 0.8), 20, 1);
      },
    },

    sting: {
      brand: true,
      build: () => `
        <div class="layer brand"></div>
        <div class="abs" style="inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center">
          <div id="g" style="width:132px;height:132px;border-radius:36px;background:linear-gradient(140deg,#6366f1,#7c3aed 55%,#2dd4bf);display:grid;place-items:center;color:#fff;font-family:var(--mono);font-weight:700;font-size:48px;box-shadow:0 30px 80px rgba(99,102,241,.35)">&lt;/&gt;</div>
          <p id="e" style="margin-top:54px;font-family:var(--head);font-weight:600;font-size:28px;color:#6e6e73">BP101T · Lesson ${T.lessonNumber} · Episode ${T.episode}</p>
          <h1 id="h" class="h" style="margin-top:14px;font-size:112px;letter-spacing:-.035em;line-height:1.05;color:#1d1d1f">${T.title || tx('title')}</h1>
          <p id="f" style="margin-top:26px;font-size:30px;color:#6e6e73">Campus Champ · ${tx('langName')}</p>
        </div>`,
      update: (el, t, s) => {
        const g = $('#g', el);
        const pg = ap(t, s.start + 0.1, 0.7);
        g.style.opacity = pg;
        g.style.transform = `scale(${lerp(0.7, 1, pg)}) rotate(${(1 - pg) * -8}deg)`;
        show($('#e', el), ap(t, s.start + 0.5, 0.6), 18, 1);
        show($('#h', el), ap(t, s.start + 0.7, 0.7), 24, 1);
        show($('#f', el), ap(t, s.start + 1.1, 0.6), 12, 1);
      },
    },

    rx: {
      build: () => `
        ${bg(['#0f6e69', '#0b4549', '#06222c'])}
        <div id="paper" class="abs" style="left:250px;top:150px;filter:drop-shadow(0 30px 40px rgba(2,26,31,.55))">${prescription(820)}</div>
        <svg class="art" id="links" viewBox="0 0 1920 1080" style="pointer-events:none">
          ${[300, 470, 640].map((y, i) => `<path class="lk" d="M1090 ${y + 30} C 1170 ${y + 30}, 1180 ${y}, 1250 ${y}" stroke="#5eead4" stroke-width="3" stroke-dasharray="4 12" fill="none" opacity="0"/>`).join('')}
        </svg>
        <div id="labels" class="abs" style="left:1260px;top:250px;display:flex;flex-direction:column;gap:64px">
          ${['Clear', 'In order', 'Followed exactly'].map((a, i) => [a, tx('labels')[i]]).map(([a, b], i) => `<div class="lbl" style="opacity:0"><span class="n">${i + 1}</span><span class="t">${a}<span class="k">${b}</span></span></div>`).join('')}
        </div>`,
      update: (el, t, s) => {
        const paper = $('#paper', el);
        const pin = ap(t, s.start + 0.2, 1.0);
        paper.style.opacity = pin;
        paper.style.transform = `translateY(${(1 - pin) * 120}px) rotate(${lerp(-10, -3, pin)}deg) scale(${lerp(0.9, 1, pin)})`;
        const linesIn = ap(t, S(s, 1), 0.6);
        // reading lines: k2,k3,k4 → line 1,2,3
        let active = -1;
        [2, 3, 4].forEach((k, i) => { if (t >= S(s, k) && t < S(s, 5)) active = i; });
        $$('.rxl', el).forEach((g, i) => {
          g.style.opacity = clamp(linesIn * 1.2 - i * 0.15);
          const on = i === active;
          $('.hl', g).setAttribute('opacity', on ? 1 : 0);
          $('.dot', g).setAttribute('fill', on ? '#f59e0b' : t >= S(s, 2 + i) ? '#2dd4bf' : '#e2e8f0');
          $('.num', g).setAttribute('fill', on || t >= S(s, 2 + i) ? '#fff' : '#64748b');
          $('.txt', g).setAttribute('fill', on ? '#0f172a' : '#334155');
        });
        $$('.lbl', el).forEach((n, i) => {
          const p = ap(t, S(s, 6 + i) + 0.3, 0.6);
          show(n, p, 0, 0.8);
          n.style.transform += ` translateX(${(1 - p) * 40}px)`;
          // "Clear. In order. Followed exactly." pulses each label in turn
          const k9 = S(s, 9), d9 = (s.lines[9] || {}).dur || 0;
          const beat = k9 + d9 * (0.45 + i * 0.18);
          const pulse = t > beat && t < beat + 0.5 ? Math.sin(((t - beat) / 0.5) * Math.PI) : 0;
          $('.n', n).style.transform = `scale(${1 + pulse * 0.25})`;
        });
        $$('.lk', el).forEach((l, i) => (l.style.opacity = ap(t, S(s, 6 + i), 0.5)));
      },
    },

    unclear: {
      build: () => `
        ${bg(['#16336b', '#101d45', '#070c22'])}
        <div id="paper" class="abs" style="left:140px;top:190px;transform:rotate(-2deg);filter:drop-shadow(0 30px 40px rgba(0,0,0,.5))">${prescription(640)}</div>
        <div id="warn" class="abs" style="left:120px;top:170px;width:680px;height:640px;border-radius:36px;box-shadow:0 0 0 8px #fb7185, 0 0 80px rgba(251,113,133,.6);opacity:0"></div>
        <div id="strips" class="abs" style="left:980px;top:230px;display:flex;gap:40px">
          ${['#60a5fa', '#f472b6', '#fbbf24'].map((c, i) => `<div class="strip" style="opacity:0;position:relative;width:220px;height:300px;border-radius:26px;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.18);display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:28px">
            ${Array.from({ length: 6 }, () => `<span style="border-radius:50%;background:${c};box-shadow:inset 0 -6px 0 rgba(0,0,0,.18)"></span>`).join('')}
            <span class="q" style="position:absolute;right:-18px;top:-22px;width:60px;height:60px;border-radius:50%;background:#fb7185;color:#fff;font-family:var(--head);font-weight:800;font-size:38px;display:grid;place-items:center">?</span></div>`).join('')}
        </div>
        <div id="call" class="abs tag" style="left:1100px;top:640px;opacity:0;background:rgba(45,212,191,.16);border-color:#2dd4bf;color:#ccfbf1">${tx('call')}</div>
        <div id="danger" class="abs tag" style="left:1100px;top:640px;opacity:0;background:rgba(251,113,133,.18);border-color:#fb7185;color:#ffe4e6">${tx('danger')}</div>
        <div id="ok" class="abs" style="left:1020px;top:330px;width:720px;opacity:0;text-align:left">
          <div style="width:120px;height:120px;border-radius:50%;background:#34d399;color:#03201d;display:grid;place-items:center;font-size:70px;font-weight:800;box-shadow:0 0 0 18px rgba(52,211,153,.18)">✓</div>
          <p class="h" style="margin-top:40px;font-size:72px;color:#fff;line-height:1.1">Clear <span style="color:#6ee7b7">+</span> In order</p>
          <p style="margin-top:18px;font-size:38px;color:#a7f3d0">${tx('okSub')}</p>
        </div>`,
      update: (el, t, s) => {
        show($('#paper', el), ap(t, s.start, 0.6), 30, 0.96);
        const lines = $$('.rxl', el);
        // line 2 loses its "1" while k0 is said, and comes back at k5
        const vague = t >= S(s, 0) + 0.8 && t < S(s, 5) + 0.4;
        const t2 = $('.txt', lines[1]);
        t2.textContent = vague ? 'Take tablet' : 'Take 1 tablet';
        t2.setAttribute('fill', vague ? '#e11d48' : '#334155');
        $('.hl', lines[1]).setAttribute('opacity', vague ? 1 : 0);
        $('.hl', lines[1]).setAttribute('fill', '#ffe4e6');
        $$('.strip', el).forEach((n, i) => show(n, ap(t, S(s, 1) + i * 0.25, 0.5) * (1 - ap(t, S(s, 3), 0.4)), 30, 0.9));
        $$('.q', el).forEach((q, i) => { const b = Math.sin(t * 4 + i) * 6; q.style.transform = `translateY(${b}px)`; });
        // k3: lines jumble; k5: back in order
        const jumble = ap(t, S(s, 3), 0.7) * (1 - ap(t, S(s, 5), 0.7));
        const order = [2, 0, 1];
        lines.forEach((g, i) => g.setAttribute('transform', `translate(${Math.sin(i * 2) * 30 * jumble} ${(order[i] - i) * 120 * jumble}) rotate(${(i - 1) * 3 * jumble} 410 ${324 + i * 120})`));
        $('#warn', el).style.opacity = ap(t, S(s, 4), 0.4) * (1 - ap(t, S(s, 5), 0.4)) * (0.75 + Math.sin(t * 6) * 0.25);
        show($('#call', el), ap(t, S(s, 2), 0.5) * (1 - ap(t, S(s, 3), 0.3)), 20, 0.9);
        show($('#danger', el), ap(t, S(s, 4), 0.5) * (1 - ap(t, S(s, 5), 0.3)), 20, 0.9);
        show($('#ok', el), ap(t, S(s, 5) + 0.5, 0.5), 20, 0.9);
      },
    },

    chip: {
      build: () => {
        let traces = '';
        for (let i = 0; i < 16; i++) {
          const a = (i / 16) * Math.PI * 2 + 0.2, r1 = 210, r2 = 560 + (i % 3) * 140;
          const x1 = 700 + Math.cos(a) * r1, y1 = 480 + Math.sin(a) * r1, x2 = 700 + Math.cos(a) * r2, y2 = 480 + Math.sin(a) * r2 * 0.75;
          const mx = (x1 + x2) / 2;
          traces += `<path class="tr" d="M${x1} ${y1} L${mx} ${y1} L${x2} ${y2}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/><circle class="tp" cx="${x2}" cy="${y2}" r="9" fill="#2dd4bf" stroke="none" opacity="0"/>`;
        }
        return `
          ${bg(['#2a2370', '#141038', '#07061a'], `<g stroke="#6d63ff" stroke-width="4" fill="none" opacity=".55" stroke-linecap="round">${traces}</g><g id="sparks"></g>`)}
          <div id="chip" class="abs" style="left:500px;top:280px">${chipSvg('a')}</div>
          <div class="abs tag t1" style="left:250px;top:200px;opacity:0">⚡ Super fast</div>
          <div class="abs tag t2" style="left:820px;top:170px;opacity:0">🔋 Never tired</div>
          <div class="abs tag t3" style="left:200px;top:760px;opacity:0;background:rgba(251,113,133,.18);border-color:#fb7185;color:#ffe4e6">🤷 Common sense: 0</div>
          <div class="abs tag t4" style="left:640px;top:820px;opacity:0">🎯 Does exactly what it's told</div>
          <div id="note" class="abs" style="left:1240px;top:330px;opacity:0;background:#fde68a;color:#1f2937;border-radius:12px;padding:30px 36px;font-size:40px;font-weight:700;box-shadow:0 24px 50px rgba(0,0,0,.4);transform:rotate(3deg)">${tx('note')}
            <div id="qm" style="position:absolute;right:-30px;top:-46px;width:80px;height:80px;border-radius:50%;background:#fb7185;color:#fff;font-family:var(--head);font-weight:800;font-size:48px;display:grid;place-items:center;opacity:0">?</div>
          </div>
          <div id="steps" class="abs" style="left:1180px;top:200px;width:640px;display:flex;flex-direction:column;gap:18px">
            ${tx('steps').map((x, i) => `<div class="step" style="opacity:0"><span class="n">${i + 1}</span>${x}</div>`).join('')}
          </div>
          <div id="count" class="abs" style="left:1180px;top:740px;width:640px;opacity:0;display:flex;align-items:center;gap:26px">
            <div style="display:flex;gap:10px;padding:18px 20px;border-radius:24px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.18)">
              ${Array.from({ length: 10 }, () => '<span class="tab" style="width:30px;height:30px;border-radius:50%;background:#475569"></span>').join('')}
            </div>
            <div class="h" style="font-size:72px;color:#fff;font-variant-numeric:tabular-nums"><span id="num">0</span></div>
          </div>`;
      },
      update: (el, t, s) => {
        const chip = $('#chip', el);
        const pin = ap(t, s.start + 0.2, 1.0);
        chip.style.opacity = pin;
        chip.style.transform = `scale(${lerp(0.5, 1, easeIO(pin))}) translateY(${Math.sin(t * 1.6) * 6}px)`;
        $$('.tr', el).forEach((p, i) => p.setAttribute('stroke-dashoffset', String(1 - ap(t, s.start + 0.6 + i * 0.05, 1.2))));
        $$('.tp', el).forEach((p, i) => p.setAttribute('opacity', ap(t, s.start + 1.2 + i * 0.05, 0.4)));
        [1, 2, 3, 4].forEach((n) => {
          const k = [1, 2, 3, 4][n - 1];
          const out = n >= 3 ? 1 - ap(t, S(s, 7), 0.4) : 1 - ap(t, S(s, 5), 0.4);
          const node = $(`.t${n}`, el);
          show(node, ap(t, S(s, k) + (n === 2 ? 0 : 0.2), 0.5) * out, 20, 0.85);
          node.style.transform += ` translateY(${Math.sin(t * 1.3 + n) * 5}px)`;
        });
        const confused = t >= S(s, 6) && t < S(s, 7) + 0.5;
        chipFace(el, t, confused ? 'confused' : 'happy');
        show($('#note', el), ap(t, S(s, 5), 0.5) * (1 - ap(t, S(s, 7), 0.4)), 30, 0.9);
        pop($('#qm', el), ap(t, S(s, 6), 0.5));
        const steps = $$('.step', el);
        const k8 = S(s, 8), d8 = (s.lines[8] || {}).dur || 1;
        steps.forEach((n, i) => {
          show(n, ap(t, S(s, 7) + 0.2 + i * 0.15, 0.5), 20, 0.95);
          n.classList.toggle('on', t >= k8 + (d8 * i) / 4);
        });
        // k9: the computer counts the strip, 0 → 10
        show($('#count', el), ap(t, S(s, 9) - 0.3, 0.5), 20, 0.95);
        const c = Math.floor(clamp((t - S(s, 9)) / Math.max(0.5, ((s.lines[9] || {}).dur || 2) * 0.8)) * 10);
        $$('.tab', el).forEach((n, i) => (n.style.background = i < c ? '#2dd4bf' : '#475569'));
        $('#num', el).textContent = c;
      },
    },

    program: {
      build: () => `
        ${bg(['#4338ca', '#25207a', '#0d0b2e'])}
        <div id="mini" class="abs" style="left:660px;top:250px;width:600px;display:flex;flex-direction:column;gap:14px">
          ${tx('steps').map((x, i) => `<div class="step on" style="font-size:30px;padding:16px 22px"><span class="n" style="width:46px;height:46px">${i + 1}</span>${x}</div>`).join('')}
        </div>
        <div class="abs" style="left:0;right:0;top:170px;text-align:center">
          <p id="kick" style="font-family:var(--head);font-weight:700;font-size:36px;color:#c7d2fe;opacity:0">${tx('named')}</p>
          <div id="word" class="h" style="margin-top:6px;font-size:270px;letter-spacing:.06em;line-height:1;color:#fff;text-shadow:0 0 80px rgba(165,180,252,.65)">${'PROGRAM'.split('').map((c) => `<span class="ch" style="display:inline-block;opacity:0">${c}</span>`).join('')}</div>
          <p id="def" style="margin:34px auto 0;width:1240px;font-size:42px;line-height:1.45;color:#e0e7ff;opacity:0">${tx('def')}</p>
        </div>
        <div class="abs" style="left:0;right:0;top:740px;display:flex;justify-content:center;gap:40px">
          <div class="cmp c1" style="opacity:0"><span class="ic" style="background:#fef3c7;color:#b45309">℞</span><span>Prescription</span><span style="color:#a5b4fc">→</span><span class="ic" style="background:#ccfbf1">🧑</span><span>Patient</span></div>
          <div class="cmp c2" style="opacity:0"><span class="ic" style="background:#e0e7ff;color:#4338ca;font-family:var(--mono);font-size:30px">{ }</span><span>Program</span><span style="color:#a5b4fc">→</span><span class="ic" style="background:#ede9fe">💻</span><span>Computer</span></div>
        </div>`,
      update: (el, t, s) => {
        const mini = $('#mini', el);
        const away = ap(t, S(s, 1), 0.7);
        mini.style.opacity = ap(t, s.start + 0.1, 0.5) * (1 - away);
        mini.style.transform = `scale(${lerp(1, 0.3, away)}) translateY(${-away * 200}px)`;
        show($('#kick', el), ap(t, S(s, 1) + 0.2, 0.5), 15, 1);
        $$('.ch', el).forEach((c, i) => {
          const p = ap(t, S(s, 2) + 0.15 + i * 0.07, 0.5);
          c.style.opacity = p;
          c.style.transform = `translateY(${(1 - p) * 60}px) scale(${lerp(1.3, 1, p)})`;
        });
        show($('#def', el), ap(t, S(s, 2) + 1.1, 0.7), 20, 1);
        show($('.c1', el), ap(t, S(s, 3) + 0.3, 0.6), 30, 0.9);
        show($('.c2', el), ap(t, S(s, 4) + 0.9, 0.6), 30, 0.9);
      },
    },

    exact: {
      build: () => `
        ${bg(['#3b1d5e', '#1d1240', '#0a0820'])}
        <div id="prog" class="abs" style="left:150px;top:240px;width:760px;border-radius:30px;background:#0b1023;border:1.5px solid #2b3466;box-shadow:0 30px 70px rgba(0,0,0,.5);overflow:hidden">
          <div style="padding:18px 26px;background:#111633;color:#94a3b8;font-family:var(--mono);font-size:22px;border-bottom:1.5px solid #1e293b">program</div>
          <div style="padding:36px 34px;font-family:var(--mono);font-size:40px;line-height:1.8;color:#e2e8f0">
            <div><span style="color:#64748b">1</span>&nbsp; ${tx('dose')}</div>
            <div><span style="color:#64748b">2</span>&nbsp; <span id="typed"></span><span id="caret" style="color:#a5b4fc">|</span><span style="color:#86efac"> tablet</span></div>
          </div>
        </div>
        <div id="meant" class="abs" style="left:620px;top:205px;opacity:0;background:#fde68a;color:#1f2937;border-radius:14px;padding:12px 20px;font-size:28px;font-weight:700;transform:rotate(4deg)">${tx('meant')}</div>
        <div id="screen" class="abs" style="left:1110px;top:220px;width:640px;height:420px;border-radius:34px;background:#0f172a;border:12px solid #1e293b;box-shadow:0 30px 70px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0">
          <p style="color:#94a3b8;font-size:30px;font-family:var(--head);font-weight:700">${tx('shown')}</p>
          <p id="out" class="h" style="margin-top:12px;font-size:120px;color:#fff">10 tablets</p>
        </div>
        <div id="lens" class="abs" style="left:300px;top:380px;width:220px;height:220px;border-radius:50%;border:12px solid #e0e7ff;box-shadow:0 0 0 6px rgba(0,0,0,.25), inset 0 0 40px rgba(255,255,255,.25);opacity:0">
          <span style="position:absolute;right:-70px;bottom:-60px;width:110px;height:24px;background:#e0e7ff;border-radius:12px;transform:rotate(45deg)"></span>
        </div>
        <div id="detail" class="abs tag" style="left:150px;top:720px;opacity:0;background:rgba(251,191,36,.16);border-color:#fbbf24;color:#fef3c7">${tx('detail')}</div>
        <div id="err" class="abs" style="left:1110px;top:690px;width:640px;opacity:0;border-radius:24px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.18);padding:24px 28px;color:#e2e8f0;font-size:30px;line-height:1.4">
          <b style="color:#fda4af">Computer:</b> ${tx('err')} 🙋<br><span style="color:#a5b4fc;font-size:26px;font-weight:700">Errors → Episode 3</span>
        </div>`,
      update: (el, t, s) => {
        show($('#prog', el), ap(t, s.start + 0.1, 0.6), 30, 0.95);
        const tp = clamp((t - S(s, 1)) / 1.2);
        $('#typed', el).textContent = tp <= 0 ? '' : tp < 0.5 ? '1' : '10';
        $('#typed', el).style.color = tp >= 0.5 ? '#fda4af' : '#fcd34d';
        $('#caret', el).style.opacity = Math.floor(t * 2) % 2 ? 0 : 1;
        show($('#meant', el), ap(t, S(s, 1) + 1.6, 0.5), 15, 0.9);
        const scr = $('#screen', el);
        const ps = ap(t, S(s, 2), 0.5);
        scr.style.opacity = ps;
        scr.style.transform = `scale(${lerp(0.9, 1, ps)})`;
        scr.style.boxShadow = `0 30px 70px rgba(0,0,0,.5), 0 0 ${60 + Math.sin(t * 5) * 20}px rgba(251,113,133,${0.55 * ps})`;
        $('#out', el).style.color = '#fda4af';
        const pl = ap(t, S(s, 3), 0.6);
        const lens = $('#lens', el);
        lens.style.opacity = pl * (1 - ap(t, S(s, 4), 0.4));
        lens.style.transform = `translate(${lerp(-80, 0, pl)}px, ${lerp(60, 0, pl)}px) scale(${lerp(0.7, 1, pl)})`;
        show($('#detail', el), ap(t, S(s, 3) + 0.4, 0.5), 20, 0.9);
        show($('#err', el), ap(t, S(s, 4) + 0.3, 0.6), 20, 0.95);
      },
    },

    around: {
      build: () => {
        const item = (cls, x, y, inner, label) => `<div class="abs dev ${cls}" style="left:${x}px;top:${y}px;opacity:0;text-align:center">
            <div style="width:300px;height:250px;border-radius:34px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.16);display:grid;place-items:center;position:relative">${inner}
              <div class="code" style="position:absolute;right:18px;bottom:18px;display:flex;flex-direction:column;gap:6px;opacity:0">${[50, 34, 44].map((w) => `<span style="width:${w}px;height:8px;border-radius:4px;background:#2dd4bf"></span>`).join('')}</div>
            </div>
            <p style="margin-top:16px;color:#e0e7ff;font-size:30px;font-weight:600">${label}</p></div>`;
        return `
          ${bg(['#0e4f6b', '#0a2b44', '#06121f'])}
          ${item('d0', 150, 230, `<div style="width:110px;height:190px;border-radius:24px;background:#0f172a;border:6px solid #334155;display:grid;place-items:center;gap:8px;padding:18px">${['#60a5fa', '#f472b6', '#fbbf24', '#34d399'].map((c) => `<span style="width:56px;height:16px;border-radius:8px;background:${c}"></span>`).join('')}</div>`, 'Phone apps')}
          ${item('d1', 560, 230, `<div style="width:200px;height:150px;border-radius:16px;background:#f8fafc;padding:16px;display:flex;flex-direction:column;gap:10px;font-family:var(--mono);font-size:18px;color:#0f172a;text-align:left"><b>BILL</b><span>Paracetamol ₹22</span><span>ORS ₹19</span><b style="color:#0d9488">Total ₹41</b></div>`, 'Medical shop billing')}
          ${item('d2', 970, 230, `<div style="width:140px;height:190px;border-radius:30px;background:#e2e8f0;padding:18px;display:flex;flex-direction:column;align-items:center;gap:12px"><div style="width:104px;height:70px;border-radius:12px;background:#0f172a;color:#5eead4;font-family:var(--mono);font-weight:700;font-size:34px;display:grid;place-items:center">110</div><span style="width:30px;height:30px;border-radius:50%;background:#94a3b8"></span></div>`, 'Glucometer')}
          ${item('d3', 1380, 230, `<div style="width:220px;height:150px;border-radius:16px;background:#0f172a;border:5px solid #334155;padding:16px;display:flex;flex-direction:column;gap:10px">${[1, 2, 3].map(() => '<div style="display:flex;gap:8px"><span style="width:26px;height:26px;border-radius:50%;background:#a78bfa"></span><span style="flex:1;height:12px;margin-top:7px;border-radius:6px;background:#475569"></span></div>').join('')}</div>`, 'Hospital records')}
          <div id="you" class="abs h" style="left:0;right:0;top:700px;text-align:center;font-size:76px;color:#fff;opacity:0">${tx('you')}</div>`;
      },
      update: (el, t, s) => {
        [0, 1, 2, 3].forEach((i) => {
          const n = $(`.d${i}`, el);
          show(n, ap(t, S(s, i) + 0.1, 0.6), 40, 0.85);
          n.style.transform += ` translateY(${Math.sin(t * 1.4 + i) * 6}px)`;
          $('.code', n).style.opacity = ap(t, S(s, 4) + i * 0.2, 0.4);
        });
        show($('#you', el), ap(t, S(s, 5), 0.7), 30, 0.95);
      },
    },

    quiz: {
      build: () => `
        ${bg(['#4c1d95', '#2e1065', '#0f0727'])}
        <h2 class="abs h" style="left:150px;top:170px;font-size:64px;color:#fff">${T.quiz ? T.quiz.q : tx('quizQ')}</h2>
        <div class="abs" style="left:150px;right:420px;top:330px;display:flex;flex-direction:column;gap:24px">
          ${(T.quiz ? T.quiz.options : ['Computer screen', tx('quizB'), 'Internet']).map((o, i) => `<div class="opt" data-i="${i}" style="opacity:0"><span class="l">${'ABC'[i]}</span><span>${o}</span></div>`).join('')}
        </div>
        <div id="ring" class="abs" style="right:150px;top:340px;width:240px;height:240px;opacity:0">
          <svg viewBox="0 0 100 100" style="width:100%;height:100%;transform:rotate(-90deg)"><circle cx="50" cy="50" r="44" fill="rgba(255,255,255,.08)"/><circle id="arc" cx="50" cy="50" r="44" fill="none" stroke="#c4b5fd" stroke-width="7" stroke-linecap="round" stroke-dasharray="276.5"/></svg>
          <span id="num" class="h" style="position:absolute;inset:0;display:grid;place-items:center;font-size:110px;color:#fff"></span>
        </div>`,
      update: (el, t, s) => {
        const cd = byId(s, 'countdown');
        const ans = s.lines[s.lines.length - 1];
        $$('.opt', el).forEach((o, i) => {
          show(o, ap(t, S(s, 0) + 0.5 + i * 0.2, 0.5), 20, 0.97);
          const right = i === (T.quiz ? T.quiz.answer : 1), shown = t >= ans.start;
          o.style.background = shown && right ? 'rgba(52,211,153,.2)' : 'rgba(255,255,255,.07)';
          o.style.borderColor = shown && right ? '#34d399' : 'rgba(255,255,255,.16)';
          o.style.opacity = shown && !right ? 0.4 : o.style.opacity;
          if (shown && right) o.style.transform = `scale(${1 + 0.03 * ap(t, ans.start, 0.4)})`;
        });
        const inCd = t >= cd.start && t < cd.start + cd.dur;
        $('#ring', el).style.opacity = inCd ? 1 : 0;
        if (inCd) {
          const left = cd.dur - (t - cd.start);
          $('#num', el).textContent = Math.ceil(left);
          $('#arc', el).setAttribute('stroke-dashoffset', String(276.5 * (1 - left / cd.dur)));
        }
      },
    },

    recap: {
      build: () => `
        ${bg(['#065f46', '#053b33', '#03201d'])}
        <p class="abs h" id="rt" style="left:150px;top:160px;font-size:64px;color:#fff;opacity:0">Recap</p>
        <div class="abs" style="left:150px;right:150px;top:300px;display:flex;flex-direction:column;gap:30px">
          ${(T.recap || tx('recap')).map((p, i) => `<div class="rp" style="opacity:0;display:flex;gap:28px;align-items:center;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.16);border-radius:30px;padding:30px 36px">
            <span style="flex:none;width:70px;height:70px;border-radius:50%;background:#34d399;color:#03201d;display:grid;place-items:center;font-family:var(--head);font-weight:800;font-size:34px">${i + 1}</span>
            <span style="font-size:44px;color:#fff;font-weight:600">${p}</span></div>`).join('')}
        </div>`,
      update: (el, t, s) => {
        show($('#rt', el), ap(t, s.start + 0.2, 0.5), 20, 1);
        $$('.rp', el).forEach((n, i) => show(n, ap(t, S(s, i + 1), 0.6), 30, 0.96));
      },
    },

    teaser: {
      build: () => `
        ${bg(['#2a2370', '#141038', '#07061a'])}
        <div id="chip" class="abs" style="left:760px;top:250px">${chipSvg('b')}</div>
        <div id="b1" class="abs" style="left:170px;top:300px;opacity:0;background:#fff;color:#0f172a;border-radius:28px 28px 28px 6px;padding:24px 32px;font-size:44px;font-weight:700">Hello computer! 👋</div>
        <div id="b2" class="abs" style="left:1260px;top:540px;opacity:0;background:#fff;color:#0f172a;border-radius:28px 28px 6px 28px;padding:24px 32px;font-size:44px;font-weight:700">${tx('hello2')}</div>
        <div id="q" class="abs h" style="left:900px;top:130px;width:120px;height:120px;border-radius:50%;background:#fb7185;color:#fff;font-size:76px;display:grid;place-items:center;opacity:0">?</div>
        <div id="next" class="abs h" style="left:0;right:0;top:760px;text-align:center;font-size:84px;color:#fff;opacity:0">${tx('why')}</div>`,
      update: (el, t, s) => {
        const c = $('#chip', el);
        c.style.opacity = ap(t, s.start, 0.5);
        c.style.transform = `translateY(${Math.sin(t * 1.6) * 6}px)`;
        chipFace(el, t, t >= S(s, 0) + 1.2 && t < S(s, 2) ? 'confused' : 'happy');
        const b1 = ap(t, S(s, 0) + 0.3, 0.6), b2 = ap(t, S(s, 0) + 1.0, 0.6);
        const gone = ap(t, S(s, 2), 0.5);
        show($('#b1', el), b1 * (1 - gone), 30, 0.9);
        show($('#b2', el), b2 * (1 - gone), 30, 0.9);
        pop($('#q', el), ap(t, S(s, 0) + 1.6, 0.5) * (1 - gone));
        show($('#next', el), ap(t, S(s, 2) + 0.3, 0.7), 30, 0.95);
      },
    },

    end: {
      brand: true,
      build: () => `
        <div class="layer brand"></div>
        <div class="abs" style="left:150px;top:0;bottom:0;width:900px;display:flex;flex-direction:column;justify-content:center">
          <p id="e1" style="font-family:var(--head);font-weight:600;font-size:30px;color:#6e6e73">${tx('nextEp')}</p>
          <h1 id="e2" class="h" style="margin-top:12px;font-size:110px;letter-spacing:-.035em;line-height:1.05;color:#1d1d1f">${T.next ? T.next.title : tx('whyBrand')}</h1>
          <p id="e3" style="margin-top:30px;font-size:34px;line-height:1.45;color:#424245">${T.next ? T.next.desc : tx('nextDesc')}</p>
          <div id="e4" style="margin-top:56px;display:flex;gap:16px;align-items:center">
            <span style="font-family:var(--head);font-weight:700;font-size:30px;background:#1d1d1f;color:#fff;border-radius:999px;padding:20px 36px">Practise free →</span>
            <span style="font-family:var(--head);font-weight:600;font-size:30px;color:#4f46e5;padding:0 10px">campuschamp.in</span>
          </div>
        </div>
        <div id="e5" class="abs" style="right:170px;top:280px;width:520px;height:520px;border-radius:56px;background:#fff;box-shadow:0 40px 100px rgba(0,0,0,.08),0 0 0 1px rgba(0,0,0,.04);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">
          <img src="${T.qr}" style="width:360px;height:360px" />
          <p style="font-family:var(--head);font-weight:700;font-size:26px;color:#1d1d1f">Scan to practise Lesson ${T.lessonNumber}</p>
        </div>`,
      update: (el, t, s) => {
        ['e1', 'e2', 'e3', 'e4', 'e5'].forEach((id, i) => show($(`#${id}`, el), ap(t, s.start + 0.2 + i * 0.18, 0.7), 24, 0.98));
      },
    },
  };

  // Later episodes add their own scenes (scenes-ep2.js …) and reuse these helpers and the shared
  // sting, quiz, recap and end card, which read the episode's words from the timeline.
  window.addScenes = (make) => Object.assign(SCENES, make({ $, $$, clamp, ease, easeIO, ap, lerp, esc, show, pop, S, E, byId, prescription, chipSvg, chipFace, bg, T: () => T }));

  // ---------- frame ----------
  function speaking(t) {
    for (const s of T.scenes) for (const l of s.lines) if (l.env && t >= l.start && t < l.start + l.dur) return l;
    return null;
  }
  function chunk(text) {
    const parts = text.match(/[^,.?!:;]+[,.?!:;]*\s*/g) || [text];
    const out = [];
    let c = '';
    for (const p of parts) {
      if ((c + p).length > 62 && c) { out.push(c.trim()); c = p; } else c += p;
    }
    if (c.trim()) out.push(c.trim());
    return out;
  }

  window.setupVideo = (timeline) => { T = timeline; };
  window.renderAt = (t) => {
    const idx = T.scenes.findIndex((s) => t >= s.start && t < s.end);
    const scene = T.scenes[idx === -1 ? T.scenes.length - 1 : idx];
    if (!cur || cur.scene !== scene) {
      $('#stage').innerHTML = `<div class="scene">${SCENES[scene.type].build(scene)}</div>`;
      cur = { scene };
    }
    const el = $('#stage .scene');
    SCENES[scene.type].update(el, t, scene);
    // dip through black between scenes (short, cinematic)
    const into = clamp((t - scene.start) / 0.35);
    const outof = scene === T.scenes[T.scenes.length - 1] ? 1 : clamp((scene.end - t) / 0.35);
    $('#fade').style.opacity = 1 - Math.min(into, outof);
    // overlays only on teaching scenes
    const brand = !!SCENES[scene.type].brand;
    $('#overlay').style.display = brand ? 'none' : 'block';
    $('#chapter').textContent = scene.chapter;
    const line = speaking(t);
    const p = $('#sub p');
    if (line) {
      const cs = chunk(line.text);
      const total = cs.reduce((a, c) => a + c.length, 0);
      let acc = 0, pick = cs[cs.length - 1];
      for (const c of cs) { acc += c.length; if ((t - line.start) / line.dur <= acc / total) { pick = c; break; } }
      p.textContent = pick;
    } else p.textContent = '';
    const lvl = line ? line.env[Math.min(line.env.length - 1, Math.floor((t - line.start) * T.fps))] || 0 : 0;
    $$('#voice b').forEach((b, i) => (b.style.height = `${6 + 24 * clamp(lvl * (0.55 + 0.45 * Math.sin(t * 17 + i * 1.9)))}px`));
    $('#voice').style.opacity = line ? 1 : 0.45;
  };
})();
