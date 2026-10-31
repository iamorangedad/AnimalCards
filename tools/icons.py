"""Small line icons for type chips and skill badges (self-drawn SVG)."""
INK = "#1f2328"
L = f'fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'


def _s(sz, body, vb=32):
    return f'<svg viewBox="0 0 {vb} {vb}" width="{sz}" height="{sz}">{body}</svg>'


CHIP = {
    "陆地": '<path d="M3 24 L11 12 L16 18 L21 10 L29 24 Z" fill="#e1efda" {L}/>',
    "水中": '<path d="M3 12 q4-4 8 0 t8 0 t10 0 M3 20 q4-4 8 0 t8 0 t10 0" {L}/>',
    "冰原": '<path d="M4 24 L10 10 L16 16 L20 8 L28 24 Z" fill="#dceafb" {L}/><path d="M4 27 H28" {L}/>',
    "天空": '<path d="M8 22 a6 6 0 0 1 2-11 a8 8 0 0 1 15 3 a4 4 0 0 1 -1 8 Z" fill="#dcf1f9" {L}/>',
    "草食": '<path d="M7 25 C7 13 15 6 26 6 C26 17 19 25 7 25 Z M7 25 L18 14" fill="#e1efda" {L}/>',
    "肉食": '<path d="M9 23 L23 9 M20 6 a3 3 0 1 1 6 6 M6 20 a3 3 0 1 0 6 6" {L}/>',
    "杂食": '<path d="M5 15 H27 a11 11 0 0 1 -22 0 Z" fill="#fde3d3" {L}/><path d="M12 10 V5 M20 10 V5" {L}/>',
}
SKILL = {
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
