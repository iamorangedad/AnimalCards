"""Small line icons for type chips and skill badges (self-drawn SVG)."""
INK = "#1f2328"
L = f'fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'


def _s(sz, body, vb=32):
    return f'<svg viewBox="0 0 {vb} {vb}" width="{sz}" height="{sz}">{body}</svg>'


CHIP = {
    "陆地": '<path d="M3 24 L11 12 L16 18 L21 10 L29 24 Z" fill="#e1efda" {L}/>',
    "水中": '<path d="M3 12 q4-4 8 0 t8 0 t10 0 M3 20 q4-4 8 0 t8 0 t10 0" {L}/>',
    "冰原": '<path d="M4 24 L10 10 L16 16 L20 8 L28 24 Z" fill="#dceafb" {L}/><path d="M4 27 H28" {L}/>',
    "两栖": '<path d="M3 20 q4-4 8 0 t8 0 t10 0" {L}/><path d="M8 14 L14 6 L18 11 L24 4 L29 14" fill="#e1efda" {L}/>',
    "天空": '<path d="M8 22 a6 6 0 0 1 2-11 a8 8 0 0 1 15 3 a4 4 0 0 1 -1 8 Z" fill="#dcf1f9" {L}/>',
    "草食": '<path d="M7 25 C7 13 15 6 26 6 C26 17 19 25 7 25 Z M7 25 L18 14" fill="#e1efda" {L}/>',
    "肉食": '<path d="M9 23 L23 9 M20 6 a3 3 0 1 1 6 6 M6 20 a3 3 0 1 0 6 6" {L}/>',
    "沙漠": '<path d="M3 24 Q10 14 17 22 Q23 16 29 24 Z" fill="#fbe9c8" {L}/><circle cx="23" cy="9" r="3.5" fill="#fff1c2" {L}/>',
    "林地": '<path d="M9 26 V20 M23 26 V20" {L}/><path d="M9 4 L15 20 H3 Z M23 6 L29 20 H17 Z" fill="#e1efda" {L}/>',
    "朽木": '<path d="M4 18 h22 a3 5 0 0 1 0 10 h-22 a3 5 0 0 1 0 -10 Z" fill="#ead9c0" {L}/><path d="M9 18 q2-7 6-7 q4 0 5 7" fill="#fde3d3" {L}/>',
    "土壤": '<path d="M3 14 H29 V28 H3 Z" fill="#ead9c0" {L}/><path d="M8 20 h3 M17 24 h3 M22 18 h3 M16 14 V6 M16 9 q-5 -3 -7 0 M16 8 q5 -4 7 -1" {L}/>',
    "农田": '<path d="M3 26 L12 14 H20 L29 26 Z" fill="#fff1c2" {L}/><path d="M10 26 L14 14 M16 26 V14 M22 26 L18 14 M16 10 V4 M13 7 q3-2 3 3 M19 7 q-3-2 -3 3" {L}/>',
    "室内": '<path d="M4 15 L16 5 L28 15 V28 H4 Z" fill="#fff1c2" {L}/><path d="M13 28 V20 H19 V28" {L}/>',
    "自养": '<circle cx="9" cy="9" r="4" fill="#fff1c2" {L}/><path d="M9 1 v2 M1 9 h2 M3 3 l1.5 1.5" {L}/><path d="M12 28 C12 18 18 12 28 12 C28 22 22 28 12 28 Z M12 28 L22 18" fill="#e1efda" {L}/>',
    "食虫": '<path d="M5 26 C5 14 10 6 16 6 C22 6 27 14 27 26 Z" fill="#e1efda" {L}/><path d="M5 26 L8 22 L11 26 L14 22 L17 26 L20 22 L23 26 L27 22" {L}/><circle cx="16" cy="14" r="2.5" fill="#1f2328"/>',
    "腐生": '<path d="M4 22 h24 v6 h-24 Z" fill="#ead9c0" {L}/><path d="M9 22 V16 M16 22 V13 M23 22 V17" {L}/><path d="M5 16 a4 3 0 0 1 8 0 Z M11 13 a5 4 0 0 1 10 0 Z M19 17 a4 3 0 0 1 8 0 Z" fill="#fde3d3" {L}/>',
    "共生": '<circle cx="11" cy="16" r="7" fill="#e1efda" {L}/><circle cx="21" cy="16" r="7" fill="#fde3d3" {L}/>',
    "寄生": '<path d="M5 26 C5 14 12 8 20 8 C26 8 28 12 28 16 C28 22 22 26 16 26 Z" fill="#fde3d3" {L}/><path d="M10 26 V20 M10 20 a3 2 0 0 1 6 0 Z" fill="#e1efda" {L}/>',
    "发酵": '<path d="M10 4 H22 M12 4 V12 L6 26 a2 2 0 0 0 2 3 H24 a2 2 0 0 0 2 -3 L20 12 V4" fill="#fff1c2" {L}/><circle cx="13" cy="22" r="2" {L}/><circle cx="19" cy="18" r="1.6" {L}/>',
    "杂食": '<path d="M5 15 H27 a11 11 0 0 1 -22 0 Z" fill="#fde3d3" {L}/><path d="M12 10 V5 M20 10 V5" {L}/>',
}
SKILL = {
    "sun": '<circle cx="20" cy="20" r="7" fill="#fff1c2" {L}/><path d="M20 4 v5 M20 31 v5 M4 20 h5 M31 20 h5 M8.7 8.7 l3.5 3.5 M27.8 27.8 l3.5 3.5 M8.7 31.3 l3.5 -3.5 M27.8 12.2 l3.5 -3.5" {L}/>',
    "root": '<path d="M20 4 V20 M20 20 C14 24 12 30 8 34 M20 20 C26 24 28 30 32 34 M20 20 V36 M14 27 l-5 0 M26 27 l5 0" {L}/><circle cx="11" cy="31" r="2.6" fill="#fde3d3" {L}/><circle cx="29" cy="31" r="2.6" fill="#fde3d3" {L}/>',
    "seed": '<path d="M20 34 C10 34 8 22 14 14 C17 10 20 6 20 6 C20 6 23 10 26 14 C32 22 30 34 20 34 Z" fill="#ead9c0" {L}/><path d="M20 12 V30" {L}/>',
    "wind": '<path d="M4 14 H26 a4 4 0 1 0 -4 -4 M4 22 H32 a4 4 0 1 1 -4 4 M4 30 H18" {L}/>',
    "bee": '<ellipse cx="20" cy="22" rx="9" ry="7" fill="#fff1c2" {L}/><path d="M17 15.5 v13 M23 15.5 v13" {L}/><path d="M16 15 C10 6 4 10 8 15 Z M24 15 C30 6 36 10 32 15 Z" fill="#dcf1f9" {L}/>',
    "drop": '<path d="M20 5 C26 14 30 19 30 25 a10 10 0 0 1 -20 0 C10 19 14 14 20 5 Z" fill="#dceafb" {L}/><path d="M15 25 a5 5 0 0 0 5 5" {L}/>',
    "thorn": '<path d="M20 4 V36" {L}/><path d="M20 10 L30 6 L21 14 M20 18 L10 14 L19 22 M20 26 L30 22 L21 30" fill="#e1efda" {L}/>',
    "toxic": '<path d="M20 4 L36 33 H4 Z" fill="#fde4e0" {L}/><path d="M20 14 V24" {L}/><circle cx="20" cy="29" r="1.8" fill="{INK}"/>',
    "spore": '<circle cx="20" cy="20" r="4" fill="#fde3d3" {L}/><circle cx="9" cy="11" r="2.6" {L}/><circle cx="31" cy="10" r="2.2" {L}/><circle cx="8" cy="29" r="2.2" {L}/><circle cx="31" cy="30" r="2.8" {L}/><circle cx="20" cy="6" r="1.8" {L}/><circle cx="21" cy="34" r="1.8" {L}/>',
    "web": '<path d="M20 20 L6 6 M20 20 L34 6 M20 20 L6 34 M20 20 L34 34 M20 20 L20 3 M20 20 L37 20 M20 20 L20 37 M20 20 L3 20" {L}/><path d="M10 20 a10 10 0 0 1 20 0 a10 10 0 0 1 -20 0" {L}/>',
    "fire": '<path d="M20 4 C24 12 32 16 30 26 a10 10 0 0 1 -20 0 C10 20 14 18 16 12 C18 16 20 16 20 4 Z" fill="#fde3d3" {L}/>',
    "cold": '<path d="M20 4 V36 M6 12 L34 28 M6 28 L34 12 M16 6 l4 4 l4 -4 M16 34 l4 -4 l4 4" {L}/>',
    "clone": '<circle cx="12" cy="26" r="6" fill="#e1efda" {L}/><circle cx="28" cy="26" r="6" fill="#e1efda" {L}/><circle cx="20" cy="12" r="6" fill="#e1efda" {L}/><path d="M15 21 L18 16 M25 21 L22 16 M18 26 H22" {L}/>',
    "food": '<path d="M8 22 H32 a12 12 0 0 1 -24 0 Z" fill="#fde3d3" {L}/><path d="M14 16 q2-5 0-9 M20 16 q2-5 0-9 M26 16 q2-5 0-9" {L}/>',
    "glow": '<circle cx="20" cy="20" r="8" fill="#e8f7a8" {L}/><path d="M20 3 v5 M20 32 v5 M3 20 h5 M32 20 h5 M8 8 l3 3 M29 29 l3 3 M8 32 l3 -3 M29 11 l3 -3" {L}/>',
    "nfix": '<path d="M20 4 V18 C14 22 10 28 8 34 M20 18 C26 22 30 28 32 34" {L}/><circle cx="12" cy="27" r="3.4" fill="#fde3d3" {L}/><circle cx="27" cy="26" r="3.4" fill="#fde3d3" {L}/><circle cx="20" cy="31" r="3" fill="#fde3d3" {L}/>',
    "micro": '<circle cx="17" cy="17" r="10" fill="#dceafb" {L}/><path d="M24.5 24.5 L34 34" {L}/><circle cx="14" cy="15" r="2.2" {L}/><circle cx="20" cy="19" r="2.6" {L}/>',
    "bamboo": '<path d="M12 4 V36 M12 12 H16 M12 22 H16 M12 30 H16" {L}/><path d="M13 12 C20 6 28 6 34 8 C28 13 20 14 13 12 Z" fill="#e1efda" {L}/>',
    "climb": '<path d="M10 36 V4 M30 36 V4" {L}/><path d="M14 26 l6-6 l6 6 M14 16 l6-6 l6 6" {L}/>',
    "flip": '<path d="M8 14 a12 12 0 0 1 22 0 M30 14 l-2-7 M30 14 l-7 1" {L}/><path d="M12 30 h16 M16 24 v6 M24 24 v6" {L}/>',
    "whisker": '<circle cx="20" cy="20" r="3" fill="{INK}"/><path d="M17 18 L4 12 M17 21 L3 22 M17 24 L5 31 M23 18 L36 12 M23 21 L37 22 M23 24 L35 31" {L}/>',
    "trunk": '<path d="M10 6 C24 6 28 14 26 24 C25 30 22 34 17 33 C14 32 14 29 17 28" {L}/><path d="M26 18 C30 18 33 22 33 26" {L}/>',
    "ear": '<path d="M20 4 C34 4 36 22 28 30 C24 34 20 32 20 26 Z" fill="#dceafb" {L}/><path d="M6 14 q3 6 0 12 M11 11 q4 9 0 18" {L}/>',
    "huddle": '<circle cx="13" cy="22" r="6" {L}/><circle cx="27" cy="22" r="6" {L}/><circle cx="20" cy="14" r="6" fill="#dceafb" {L}/>',
    "dive": '<path d="M20 4 V32 M12 24 l8 8 l8-8" {L}/><path d="M4 8 q4-3 8 0 t8 0 t8 0 t8 0" {L}/>',
    "camo": '<path d="M6 20 a14 10 0 0 1 28 0 a14 10 0 0 1 -28 0 Z" {L}/><circle cx="14" cy="18" r="2.5" fill="{INK}"/><circle cx="22" cy="22" r="3" fill="#fde3d3" {L}/><circle cx="28" cy="17" r="2" fill="{INK}"/>',
    "ink": '<path d="M20 5 C26 14 30 19 30 25 a10 10 0 0 1 -20 0 C10 19 14 14 20 5 Z" fill="{INK}"/>',
    "jar": '<path d="M11 12 H29 V32 a3 3 0 0 1 -3 3 H14 a3 3 0 0 1 -3 -3 Z" fill="#fde3d3" {L}/><path d="M9 6 H31 V12 H9 Z" {L}/><path d="M33 4 a6 6 0 0 1 0 10 M33 4 l-3 0 M33 4 l0 3" {L}/>',
    "roar": '<path d="M6 16 h6 l8-7 v22 l-8-7 h-6 Z" {L}/><path d="M25 14 q4 6 0 12 M30 10 q6 10 0 20" {L}/>',
    "team": '<circle cx="11" cy="13" r="4" {L}/><circle cx="29" cy="13" r="4" {L}/><circle cx="20" cy="11" r="4.5" fill="#fde3d3" {L}/><path d="M4 30 a7 7 0 0 1 14 0 M22 30 a7 7 0 0 1 14 0 M12 32 a8 8 0 0 1 16 0" {L}/>',
}


def chip(k, sz=30):
    return _s(sz, CHIP[k].replace("{L}", L))


def skill(k, sz=40):
    return _s(sz, SKILL[k].replace("{L}", L).replace("{INK}", INK), 40)
