"""Phase-2 art, part 3: ocean, birds, reptiles/amphibians, insects."""
import math
from iso import INK, GREY, MUTE, BLUE, BLUE_L, BLUE_M, ORG, ORG_L, YEL, YEL_L, SAGE, SAGE_L
from art import P, E, C, svg, slab, shadow, tuft, rock, sun, seaweed, tentacle, wavy, leg
from art2 import uid, fit, R, poly, clip, darker, tree, pine, mountains, flower, bubbles, G_, scene, quad, fish, turtle, bird, blob

WATER = "#dbe9f7"


def coast(w, h, animal, box, rocky=True, extra=""):
    o = [R(0, h * .40, w, h * .60, BLUE_L, 0, 0, "none")]
    for y in (h * .5, h * .62, h * .8):
        for x in (60, 300, 640, 820):
            o.append(P(f"M{x} {y:.0f} q15 -8 30 0 q15 8 30 0", sw=2, col=BLUE_M))
    o.append(sun(820, 80, 34))
    if rocky:
        o.append(P(f"M{w*.18:.0f} {h*.86:.0f} C{w*.2:.0f} {h*.66:.0f} {w*.36:.0f} {h*.6:.0f} {w*.5:.0f} {h*.62:.0f} C{w*.66:.0f} {h*.6:.0f} {w*.8:.0f} {h*.66:.0f} {w*.82:.0f} {h*.86:.0f} Z", "#e4e6e9", 3))
        o.append(P(f"M{w*.3:.0f} {h*.7:.0f} l40 -6 M{w*.62:.0f} {h*.72:.0f} l30 8", sw=2, col=MUTE))
    o.append(extra)
    cx, by, bw, bh = box
    o.append(fit(animal, cx, by, bw, bh))
    return svg(w, h, "".join(o))


# ---------------------------------------------------------------- ocean
def a_bluewhale(w, h):
    L, H = 560, 110
    grooves = "".join(P(f"M{-L/2+50+i*14} {H*.28+i*1.5} L{-L/2+190+i*10} {H*.36+i*1.2}", sw=1.8, col="#5c7fa3") for i in range(4))
    spots = "".join(C(-60 + (i * 53) % 260, -H * .3 + (i * 17) % 40, 5, "#9fb9d3", 0) for i in range(10))
    f = fish(F="#7d9dbf", L=L, H=H, tail="fluke", belly="#c9d8e8", dorsal=False, eye_r=6, extras=grooves + spots, fin_col="#6d8db0")
    f += P(f"M{L*.2} {-H*.45} l26 -18 l10 16 Z", "#6d8db0", 2.6)
    krill = "".join(P(f"M{x} {y} q6 -5 12 0", sw=2, col=ORG) for x, y in ((-380, -20), (-400, 10), (-360, 30), (-420, -10), (-390, 40)))
    return scene("sea", w, h, f + krill, box=(w / 2, h * .56, 680, 300))


def a_orca(w, h):
    L, H = 420, 130
    patch = E(-L / 2 + 70, -H * .26, 26, 11, "#fff", 2.2) + P(f"M{L*.02} {-H*.42} q40 -6 70 6 q-30 10 -70 8 Z", "#d9dde2", 0)
    f = fish(F="#2c2c2e", L=L, H=H, tail="fluke", belly="#ffffff", cetacean=True, tall_dorsal=True, eye_r=5, extras=patch, fin_col="#2c2c2e", dorsal_col="#2c2c2e")
    return scene("sea", w, h, f, box=(w / 2, h * .6, 600, 330))


def a_dolphin(w, h):
    L, H = 380, 110
    beak = P(f"M{-L/2+10} {-H*.12} C{-L/2-20} {-H*.1} {-L/2-34} {H*.02} {-L/2-30} {H*.1} C{-L/2-10} {H*.12} {-L/2+10} {H*.14} {-L/2+16} {H*.12} Z", "#9aa7b4", 2.8)
    f = beak + fish(F="#9aa7b4", L=L, H=H, tail="fluke", belly="#e6ebf0", cetacean=True, eye_r=6, mouth=False, fin_col="#8794a1")
    f += P(f"M{-L/2-28} {H*.08} q20 6 40 0", sw=2.2)
    return scene("sea", w, h, f, box=(w / 2, h * .58, 600, 300))


def a_whiteshark(w, h):
    L, H = 420, 130
    teeth = "".join(poly([(-L / 2 + 30 + i * 9, H * .12), (-L / 2 + 34 + i * 9, H * .2), (-L / 2 + 38 + i * 9, H * .12)], "#fff", 1.6) for i in range(4))
    f = fish(F="#8f9aa6", L=L, H=H, tail="shark", belly="#f4f5f6", gills=5, eye_r=6, mouth=False, fin_col="#7d8894")
    f += P(f"M{-L/2+20} {H*.12} q30 10 64 0", "#5a2a2a", 2.6) + teeth
    return scene("sea", w, h, f, box=(w / 2, h * .58, 620, 300))


def a_whaleshark(w, h):
    L, H = 560, 140
    f = fish(F="#5f7488", L=L, H=H, tail="shark", belly="#dfe5eb", spots="#e8eef4", gills=5, eye_r=5, mouth=False, fin_col="#53677a")
    f += P(f"M{-L/2+4} {H*.02} q24 10 50 4", sw=3)
    f += "".join(P(f"M{-L/2+150+i*60} {-H*.5} L{-L/2+170+i*60} {H*.2}", sw=1.6, col="#8fa2b4") for i in range(5))
    fishes = "".join(G_(fish(F="#cfd8e0", L=40, H=14, tail="fork", eye_r=2, mouth=False, pectoral=False, dorsal=False), x, y) for x, y in ((-420, -80), (-380, -40), (-440, -20)))
    return scene("sea", w, h, f + fishes, box=(w / 2, h * .58, 680, 300))


def a_greenturtle(w, h):
    t = turtle(shell="#8a7a4e", skin="#c9c08a", sea=True, scute="#a69466", plastron="#f3e3a6")
    return scene("sea", w, h, t, box=(w / 2, h * .56, 520, 280))


def a_seaotter(w, h):
    F = "#7a5a40"
    o = []
    # floating on its back: body horizontal, head to the left
    o.append(P("M-160 -40 C-150 -100 120 -110 170 -60 C200 -30 190 0 150 6 C60 14 -100 14 -150 0 Z", F))
    o.append(P("M-120 -60 C-60 -96 80 -96 130 -66 C90 -50 -60 -46 -120 -60 Z", "#a58466", 0))
    o.append(P("M160 -40 C210 -50 250 -40 270 -20 C240 -10 200 -14 170 -12 Z", F, 2.8))  # tail
    o.append(E(200, -66, 18, 30, F, 2.8, rot=30) + E(150, -82, 16, 26, F, 2.8, rot=20))  # hind feet up
    o.append(C(-180, -70, 52, "#c9b39a") + C(-206, -116, 10, "#c9b39a") + C(-150, -118, 10, "#c9b39a"))
    o.append(C(-196, -76, 5, INK, 0) + C(-164, -76, 5, INK, 0) + E(-180, -58, 9, 6, INK, 0) + P("M-180 -52 v6 M-196 -44 q16 8 32 0", sw=2.2))
    o.append(P("M-214 -54 l-26 -4 M-214 -48 l-24 6 M-146 -54 l26 -4 M-146 -48 l24 6", sw=1.6))
    o.append(E(-80, -100, 26, 16, "#e9d8b8", 2.8) + P("M-100 -100 q20 -12 40 0", sw=1.8, col=MUTE))  # shell on chest
    o.append(E(-110, -94, 14, 10, F, 2.6) + E(-50, -94, 14, 10, F, 2.6))  # paws
    water = P("M-300 -6 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0", sw=2.6, col=BLUE)
    return coast(w, h, "".join(o) + water, (w / 2, h * .74, 620, 280), rocky=False)


def pinniped(F, L=300, up=0.0, spots=None, ears=False, belly=None):
    """seal / sea lion body lying (up=0) or propped up (up=1)."""
    o = []
    hx, hy = -L / 2 - 10, -90 - 120 * up
    body = f"M{L/2+40} -10 C{L/2} -40 {L*.1} {-120-60*up} {-L/2+20} {hy+10} C{-L/2+40} {hy+50} {-L/2+30} -6 {-L/2+60} 0 Z"
    o.append(P(f"M{L/2+20} -14 l50 -20 l-10 22 l20 10 l-54 0 Z", darker(F), 2.6))
    if spots:
        sp = "".join(E(-L / 2 + 60 + (i * 47) % (L - 40), -20 - (i * 29) % 80, 7, 5, spots, 0) for i in range(22))
        o.append(P(body, F) + clip(body, sp) + P(body, "none"))
    else:
        o.append(P(body, F))
    if belly:
        o.append(P(f"M{-L/2+40} {hy+50} C{-L/2+50} -40 {-L/2+60} -10 {-L/2+90} -4", sw=10, col=belly))
    if up:
        o.append(P(f"M{hx-30} {hy+20} C{hx-40} {hy+90} {hx-20} {hy+160} {hx+10} {hy+200} L{hx+90} {hy+140} C{hx+60} {hy+80} {hx+40} {hy+30} {hx+30} {hy} Z", F))
    o.append(E(hx, hy, 50, 40, F))
    o.append(E(hx - 36, hy + 12, 24, 16, darker(F, .95), 2.6))
    o.append(C(hx - 14, hy - 8, 6, INK, 0) + E(hx - 56, hy + 6, 6, 5, INK, 0) + P(f"M{hx-50} {hy+18} l-22 -2 M{hx-50} {hy+22} l-20 6 M{hx-40} {hy+20} l18 4", sw=1.6))
    if ears:
        o.append(P(f"M{hx+20} {hy-22} q10 -8 14 4", sw=3))
    fx = -L / 2 + 60
    o.append(P(f"M{fx} -10 C{fx-20} 0 {fx-50} 4 {fx-60} 0 C{fx-40} -14 {fx-10} -24 {fx+10} -26 Z", darker(F), 2.6))
    return "".join(o)


def a_sealion(w, h):
    a = pinniped("#8a6a4a", L=280, up=1.0, ears=True)
    return coast(w, h, a, (w / 2, h * .66, 560, 360))


def a_spottedseal(w, h):
    a = pinniped("#b9bfc6", L=320, up=0.0, spots="#5a636d")
    return scene("ice", w, h, a, box=(w / 2, h * .72, 560, 260))


def a_polarbear(w, h):
    return scene("ice", w, h, quad(F="#f6f4ee", bl=320, bd=140, lh=120, lw=44, neck=(70, 18), nw=96, head=(56, 44), snout=(50, 34), snout_col="#f6f4ee",
                 ears="round", tail="short", nose=INK, farleg="#e4e1d8"), box=(w / 2, h * .74, 600, 380))


def a_seahorse(w, h):
    F = "#e8b84a"
    o = []
    o.append(P("M30 -40 C70 -20 70 30 30 40 C10 44 0 30 10 20 C20 10 34 20 26 28", sw=16) + P("M30 -40 C70 -20 70 30 30 40 C10 44 0 30 10 20 C20 10 34 20 26 28", sw=10, col=F))
    body = "M-10 -300 C30 -310 60 -280 50 -240 C80 -200 90 -130 60 -80 C40 -46 10 -40 0 -60 C-30 -110 -40 -180 -20 -230 C-30 -250 -30 -290 -10 -300 Z"
    rings = "".join(P(f"M-60 {-250+i*22} L100 {-246+i*22}", sw=1.8, col="#c99a30") for i in range(9))
    o.append(P(body, F) + clip(body, rings) + P(body, "none"))
    o.append(P("M-14 -290 C-60 -290 -96 -276 -110 -262 C-96 -250 -60 -256 -24 -258 Z", F, 2.8))
    o.append(poly([(-6, -300), (4, -326), (14, -304), (26, -322), (30, -296)], F, 2.6))
    o.append(P("M54 -200 C90 -210 100 -170 70 -150 C76 -170 70 -186 54 -186 Z", "#f6d98a", 2.4))
    o.append(C(4, -276, 8, "#fff", 2.4) + C(2, -276, 4.5, INK, 0))
    grass = "".join(P(f"M{x} 40 C{x-16} -40 {x+16} -120 {x+4} -220", sw=10) + P(f"M{x} 40 C{x-16} -40 {x+16} -120 {x+4} -220", sw=5, col=SAGE_L) for x in (-160, -130, 150))
    return scene("sea", w, h, grass + "".join(o), box=(w / 2, h * .72, 420, 420))


def anemone(x, y, s=1):
    o = ""
    for i in range(11):
        a = -math.pi + math.pi * i / 10
        x2, y2 = x + math.cos(a) * 90 * s, y - 40 * s + math.sin(a) * 90 * s
        d = f"M{x+math.cos(a)*30*s:.0f} {y-30*s:.0f} Q{x+math.cos(a)*60*s:.0f} {y2-40*s:.0f} {x2:.0f} {y2:.0f}"
        o += P(d, sw=16 * s) + P(d, sw=10 * s, col="#e7a9c8")
    return P(f"M{x-50*s} {y} C{x-50*s} {y-40*s} {x+50*s} {y-40*s} {x+50*s} {y} Z", "#c97aa0", 2.8) + o


def a_clownfish(w, h):
    f = fish(F="#f58a2c", L=200, H=110, tail="round", stripes=("#ffffff", [.22, .5, .82]), eye_r=9, fin_col="#f58a2c", dorsal_col="#f58a2c")
    an = anemone(0, 0, 1.3)
    return scene("sea", w, h, G_(an, 60, 0) + G_(f, -60, -190), box=(w / 2, h * .74, 520, 400))


def a_jelly(w, h):
    o = []
    for i in range(4):
        x = -50 + i * 34
        o.append(P(f"M{x} -40 C{x-20} 40 {x+20} 120 {x-6} 220", sw=12, col="#d9c8ee") + P(f"M{x} -40 C{x-20} 40 {x+20} 120 {x-6} 220", sw=2, col="#a48ad0"))
    o.append(P("M-200 -40 C-200 -260 200 -260 200 -40 Q100 -20 0 -34 Q-100 -20 -200 -40 Z", "#efe6fb", 3, extra='fill-opacity=".9"'))
    for i in range(4):
        a = -math.pi * .82 + i * math.pi * .21
        cx, cy = math.cos(a) * 90, -110 + math.sin(a) * 40
        o.append(P(f"M{cx-20:.0f} {cy:.0f} a20 20 0 1 1 40 0", sw=7, col="#b78ad8"))
    o.append("".join(P(f"M{-196+i*20} -38 q4 20 -2 40", sw=2, col="#a48ad0") for i in range(20)))
    return scene("deep", w, h, "".join(o), box=(w / 2, h * .88, 440, 420))


def a_starfish(w, h):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + math.pi * i / 5
        r = 150 if i % 2 == 0 else 52
        pts.append((math.cos(a) * r, math.sin(a) * r * .55 - 90))
    d = "M" + " ".join(f"{'Q' if j % 2 else 'L'}" * 0 + f"{x:.0f} {y:.0f}" + (" L" if j < 9 else "") for j, (x, y) in enumerate(pts)) + " Z"
    star = P(d, "#f08a4b", 3.2, extra='stroke-linejoin="round"')
    dots = "".join(C(math.cos(-math.pi / 2 + math.pi * 2 * k / 5) * rr, math.sin(-math.pi / 2 + math.pi * 2 * k / 5) * rr * .55 - 90, 5, "#fbd3b0", 0)
                   for k in range(5) for rr in (40, 70, 100))
    return scene("sea", w, h, star + dots + C(0, -90, 8, "#fbd3b0", 0), box=(w / 2, h * .8, 420, 220))


def a_manta(w, h):
    F = "#3a4654"
    o = []
    o.append(P("M0 -120 C80 -130 200 -90 320 -40 C220 -20 120 10 40 20 L0 30 L-40 20 C-120 10 -220 -20 -320 -40 C-200 -90 -80 -130 0 -120 Z", F))
    o.append(P("M0 30 C4 80 10 140 0 200", sw=5))
    o.append(P("M-30 -118 C-46 -150 -40 -170 -24 -170 C-20 -150 -14 -130 -10 -120 Z M30 -118 C46 -150 40 -170 24 -170 C20 -150 14 -130 10 -120 Z", F, 2.8))
    o.append(P("M-200 -60 C-120 -60 -60 -20 0 -20 C60 -20 120 -60 200 -60", sw=2, col="#e8eef4"))
    o.append(E(-110, -50, 26, 10, "#e8eef4", 0) + E(110, -50, 26, 10, "#e8eef4", 0))
    o.append(C(-34, -110, 5, "#fff", 0) + C(34, -110, 5, "#fff", 0))
    return scene("sea", w, h, G_("".join(o), 0, -40), box=(w / 2, h * .58, 640, 320))


ART3 = {"blue-whale": a_bluewhale, "orca": a_orca, "dolphin": a_dolphin, "white-shark": a_whiteshark, "whale-shark": a_whaleshark,
        "green-turtle": a_greenturtle, "sea-otter": a_seaotter, "sea-lion": a_sealion, "spotted-seal": a_spottedseal, "polar-bear": a_polarbear,
        "seahorse": a_seahorse, "clownfish": a_clownfish, "jellyfish": a_jelly, "starfish": a_starfish, "manta": a_manta}
