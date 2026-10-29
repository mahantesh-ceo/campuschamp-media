// Anu (teacher) and Champ (first-year B.Pharm student): flat illustrated busts.
// Each has #<id>-mouth-open (scaled by voice loudness), #<id>-lids (blink) and #<id>-body (idle bob).

window.CHARACTERS = {
  anu: `
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="anuKurta" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14b8a6"/><stop offset="1" stop-color="#0f766e"/></linearGradient>
    <linearGradient id="anuDupatta" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbbf24"/><stop offset="1" stop-color="#f97316"/></linearGradient>
  </defs>
  <g id="anu-body">
    <!-- hair behind -->
    <path d="M112 190 C 100 110, 150 62, 205 62 C 262 62, 304 108, 292 196 C 300 250, 286 292, 262 300 L 140 300 C 118 290, 104 250, 112 190 Z" fill="#1b1520"/>
    <!-- bun -->
    <circle cx="276" cy="92" r="34" fill="#1b1520"/>
    <circle cx="282" cy="80" r="8" fill="#f43f5e"/><circle cx="268" cy="72" r="6" fill="#fde68a"/><circle cx="292" cy="96" r="6" fill="#fde68a"/>
    <!-- body -->
    <path d="M70 400 C 74 320, 120 292, 200 290 C 280 292, 326 320, 330 400 Z" fill="url(#anuKurta)"/>
    <path d="M168 292 L 200 334 L 232 292" fill="none" stroke="#fde68a" stroke-width="5" stroke-linejoin="round"/>
    <path d="M250 300 C 300 316, 318 350, 324 400 L 286 400 C 280 360, 262 330, 232 312 Z" fill="url(#anuDupatta)"/>
    <!-- lanyard + ID -->
    <path d="M178 296 L 196 352 L 214 296" fill="none" stroke="#4f46e5" stroke-width="4"/>
    <rect x="182" y="350" width="30" height="38" rx="5" fill="#fff" stroke="#c7d2fe" stroke-width="2"/><rect x="188" y="358" width="18" height="6" rx="3" fill="#4f46e5"/>
    <!-- neck -->
    <path d="M178 250 L 178 296 C 190 306, 210 306, 222 296 L 222 250 Z" fill="#b5764f"/>
    <!-- ears -->
    <ellipse cx="124" cy="186" rx="13" ry="20" fill="#c4825b"/><ellipse cx="276" cy="186" rx="13" ry="20" fill="#c4825b"/>
    <circle cx="124" cy="212" r="6" fill="#fbbf24"/><circle cx="276" cy="212" r="6" fill="#fbbf24"/>
    <!-- face -->
    <path d="M128 170 C 128 112, 162 88, 200 88 C 238 88, 272 112, 272 170 C 272 232, 238 266, 200 266 C 162 266, 128 232, 128 170 Z" fill="#cf8d63"/>
    <!-- front hair with parting -->
    <path d="M126 168 C 122 112, 160 80, 200 82 C 196 104, 168 128, 132 150 Z" fill="#1b1520"/>
    <path d="M274 168 C 278 112, 240 80, 200 82 C 206 106, 238 128, 268 148 Z" fill="#1b1520"/>
    <!-- brows -->
    <path d="M150 150 Q 166 140 182 148" fill="none" stroke="#1b1520" stroke-width="5" stroke-linecap="round"/>
    <path d="M218 148 Q 234 140 250 150" fill="none" stroke="#1b1520" stroke-width="5" stroke-linecap="round"/>
    <!-- eyes -->
    <ellipse cx="166" cy="174" rx="13" ry="11" fill="#fff"/><circle cx="168" cy="175" r="7" fill="#2a1b14"/><circle cx="170" cy="172" r="2.2" fill="#fff"/>
    <ellipse cx="234" cy="174" rx="13" ry="11" fill="#fff"/><circle cx="236" cy="175" r="7" fill="#2a1b14"/><circle cx="238" cy="172" r="2.2" fill="#fff"/>
    <g id="anu-lids" style="transform-origin: 200px 163px; transform: scaleY(0)">
      <rect x="150" y="161" width="34" height="26" fill="#cf8d63"/><rect x="218" y="161" width="34" height="26" fill="#cf8d63"/>
    </g>
    <!-- glasses -->
    <circle cx="166" cy="175" r="22" fill="none" stroke="#3730a3" stroke-width="3.5"/><circle cx="234" cy="175" r="22" fill="none" stroke="#3730a3" stroke-width="3.5"/>
    <path d="M188 173 Q 200 166 212 173" fill="none" stroke="#3730a3" stroke-width="3.5"/>
    <!-- bindi, nose, cheeks -->
    <circle cx="200" cy="138" r="4.5" fill="#e11d48"/>
    <path d="M200 182 Q 194 204 200 210 Q 205 211 209 208" fill="none" stroke="#a96745" stroke-width="3.5" stroke-linecap="round"/>
    <ellipse cx="152" cy="212" rx="14" ry="8" fill="#e88f7a" opacity=".45"/><ellipse cx="248" cy="212" rx="14" ry="8" fill="#e88f7a" opacity=".45"/>
    <!-- mouth -->
    <path id="anu-mouth-closed" d="M180 228 Q 200 242 220 228" fill="none" stroke="#7c2d12" stroke-width="5" stroke-linecap="round"/>
    <g id="anu-mouth-open" style="transform-origin: 200px 228px; transform: scaleY(0)">
      <path d="M178 226 Q 200 222 222 226 Q 220 254 200 256 Q 180 254 178 226 Z" fill="#5b1a14"/>
      <path d="M186 246 Q 200 240 214 246 Q 208 255 200 255 Q 192 255 186 246 Z" fill="#f47c7c"/>
      <path d="M180 226 Q 200 223 220 226 L 219 231 Q 200 229 181 231 Z" fill="#fff"/>
    </g>
  </g>
</svg>`,

  champ: `
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="champCoat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e2e8f0"/></linearGradient>
  </defs>
  <g id="champ-body">
    <!-- body: indigo tee under white lab coat -->
    <path d="M66 400 C 70 318, 120 290, 200 288 C 280 290, 330 318, 334 400 Z" fill="#4f46e5"/>
    <path d="M66 400 C 70 318, 120 290, 168 288 L 186 400 Z" fill="url(#champCoat)"/>
    <path d="M334 400 C 330 318, 280 290, 232 288 L 214 400 Z" fill="url(#champCoat)"/>
    <path d="M168 288 L 196 340 L 186 400" fill="none" stroke="#cbd5e1" stroke-width="3"/>
    <path d="M232 288 L 204 340 L 214 400" fill="none" stroke="#cbd5e1" stroke-width="3"/>
    <rect x="252" y="340" width="34" height="8" rx="3" fill="#94a3b8"/><rect x="262" y="330" width="4" height="22" rx="2" fill="#f43f5e"/><rect x="272" y="330" width="4" height="22" rx="2" fill="#4f46e5"/>
    <!-- neck -->
    <path d="M178 248 L 178 294 C 190 304, 210 304, 222 294 L 222 248 Z" fill="#a8693f"/>
    <!-- ears -->
    <ellipse cx="128" cy="182" rx="14" ry="21" fill="#b9774a"/><ellipse cx="272" cy="182" rx="14" ry="21" fill="#b9774a"/>
    <!-- face -->
    <path d="M132 168 C 132 110, 164 86, 200 86 C 236 86, 268 110, 268 168 C 268 230, 236 262, 200 262 C 164 262, 132 230, 132 168 Z" fill="#c4834f"/>
    <!-- hair: short with a quiff -->
    <path d="M128 160 C 120 96, 160 60, 206 62 C 250 62, 284 92, 274 160 C 268 132, 250 118, 232 116 C 214 112, 190 120, 168 116 C 150 118, 136 132, 128 160 Z" fill="#231912"/>
    <path d="M170 70 C 196 44, 248 50, 258 86 C 234 72, 206 74, 184 92 Z" fill="#2f2219"/>
    <!-- brows -->
    <path d="M152 146 Q 168 136 184 144" fill="none" stroke="#231912" stroke-width="6" stroke-linecap="round"/>
    <path d="M216 144 Q 232 136 248 146" fill="none" stroke="#231912" stroke-width="6" stroke-linecap="round"/>
    <!-- eyes -->
    <ellipse cx="168" cy="172" rx="12" ry="12" fill="#fff"/><circle cx="170" cy="173" r="7.5" fill="#1e130c"/><circle cx="172" cy="170" r="2.4" fill="#fff"/>
    <ellipse cx="232" cy="172" rx="12" ry="12" fill="#fff"/><circle cx="234" cy="173" r="7.5" fill="#1e130c"/><circle cx="236" cy="170" r="2.4" fill="#fff"/>
    <g id="champ-lids" style="transform-origin: 200px 160px; transform: scaleY(0)">
      <rect x="154" y="158" width="30" height="28" fill="#c4834f"/><rect x="218" y="158" width="30" height="28" fill="#c4834f"/>
    </g>
    <!-- nose, cheeks -->
    <path d="M200 180 Q 193 202 200 208 Q 206 209 210 206" fill="none" stroke="#9a5b33" stroke-width="3.5" stroke-linecap="round"/>
    <ellipse cx="154" cy="210" rx="13" ry="7" fill="#e07a5f" opacity=".35"/><ellipse cx="246" cy="210" rx="13" ry="7" fill="#e07a5f" opacity=".35"/>
    <!-- mouth -->
    <path id="champ-mouth-closed" d="M176 224 Q 200 244 224 224" fill="none" stroke="#5a1f0e" stroke-width="5" stroke-linecap="round"/>
    <g id="champ-mouth-open" style="transform-origin: 200px 226px; transform: scaleY(0)">
      <path d="M176 224 Q 200 220 224 224 Q 222 256 200 258 Q 178 256 176 224 Z" fill="#4a160d"/>
      <path d="M186 246 Q 200 239 214 246 Q 208 257 200 257 Q 192 257 186 246 Z" fill="#f47c7c"/>
      <path d="M178 224 Q 200 221 222 224 L 221 230 Q 200 228 179 230 Z" fill="#fff"/>
    </g>
  </g>
</svg>`,
};
