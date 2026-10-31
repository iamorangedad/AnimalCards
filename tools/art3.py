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


# ---------------------------------------------------------------- birds
def branch(x0, x1, y, sw=14):
    return P(f"M{x0} {y} L{x1} {y-6}", sw=sw + 5) + P(f"M{x0} {y} L{x1} {y-6}", sw=sw, col="#d9c3a0")


def a_baldeagle(w, h):
    b = bird(F="#5a3d2b", wing="#4a3222", rx=92, ry=62, tilt=-24, neck=24, nw=56, hr=40, beak="hook", beak_col="#f2c53a", leg_len=40, leg_col="#f2c53a", legw=7,
             tail="short", tail_col="#ffffff", head_col="#ffffff")
    return scene("forest", w, h, G_(rock(0, 0, 2.2), 0, 0) + G_(b, 0, -86), box=(w / 2, h * .78, 520, 420))


def a_barnowl(w, h):
    o = []
    o.append(P("M-90 -40 C-110 -160 -80 -250 0 -260 C80 -250 110 -160 90 -40 C60 -4 -60 -4 -90 -40 Z", "#d9b27a"))
    o.append(P("M-30 -40 C-40 -120 40 -120 30 -40 Z", "#fbf6ec", 0))
    o.append(P("M-88 -60 C-120 -150 -90 -220 -60 -200 C-50 -150 -50 -90 -60 -40 Z M88 -60 C120 -150 90 -220 60 -200 C50 -150 50 -90 60 -40 Z", "#c99a5a", 2.8))
    o.append("".join(C(-60 + (i * 31) % 120, -190 + (i * 23) % 120, 2.5, "#fff", 0) for i in range(14)))
    o.append(P("M0 -190 C-30 -240 -90 -250 -84 -190 C-80 -150 -40 -130 0 -120 C40 -130 80 -150 84 -190 C90 -250 30 -240 0 -190 Z", "#ffffff"))
    o.append(E(-34, -182, 11, 14, INK, 0) + E(34, -182, 11, 14, INK, 0) + C(-37, -187, 3, "#fff", 0) + C(31, -187, 3, "#fff", 0))
    o.append(P("M0 -176 L-8 -150 L0 -140 L8 -150 Z", "#e8d2b0", 2.4))
    o.append(P("M-30 0 l-10 -40 M-30 0 l-18 -2 M-30 0 l-2 -2 M30 0 l10 -40 M30 0 l18 -2 M30 0 l2 -2", sw=4, col=INK))
    perch = P("M-160 4 H160", sw=16) + P("M-160 4 H160", sw=10, col="#c9a27a")
    return scene("farm", w, h, perch + "".join(o), box=(w / 2, h * .76, 400, 420))


def a_ostrich(w, h):
    b = bird(F="#2e2a28", wing="#ffffff", rx=110, ry=70, tilt=-6, neck=230, nw=24, hr=26, beak="short", beak_col="#e9cdb0", leg_len=210, leg_col="#e8b8a0", legw=11,
             tail="up", tail_col="#ffffff", head_col="#c9b8ae")
    return scene("savanna", w, h, b, box=(w / 2, h * .8, 520, 420))


def a_flamingo(w, h):
    b = bird(F="#f6a3b5", wing="#ef6f8a", rx=86, ry=52, tilt=-10, neck=200, nw=20, hr=24, beak="flamingo", leg_len=230, leg_col="#ef7f98", legw=6,
             tail="short", tail_col="#2a2a2a", head_col="#f6a3b5", webbed=True)
    return scene("wetland", w, h, b, box=(w / 2, h * .8, 480, 420))


def a_peafowl(w, h):
    train = P("M60 -150 C200 -170 360 -120 420 -10 C330 10 160 0 60 -80 Z", "#3f8f6a")
    train += "".join(E(150 + (i % 4) * 66, -120 + (i // 4) * 36 + (i % 4) * 14, 14, 11, "#e9c64a", 2) + C(150 + (i % 4) * 66, -120 + (i // 4) * 36 + (i % 4) * 14, 6, "#2b5aa8", 0)
                     for i in range(10))
    b = bird(F="#2b5aa8", wing="#c9b89a", rx=74, ry=50, tilt=-10, neck=70, nw=34, hr=26, beak="short", beak_col="#c9b89a", leg_len=90, leg_col="#b8a890", legw=6,
             tail="short", tail_col="#3f8f6a", crest="peacock", head_col="#2b5aa8", eye_ring="#ffffff")
    return scene("forest", w, h, train + b, box=(w / 2, h * .76, 600, 380))


def a_crane(w, h):
    b = bird(F="#ffffff", wing="#2a2a2a", rx=96, ry=56, tilt=-8, neck=150, nw=22, hr=24, beak="long", beak_col="#9aa58a", leg_len=220, leg_col="#3a3f45", legw=6,
             tail="up", tail_col="#2a2a2a", crest="red", head_col="#2a2a2a")
    return scene("wetland", w, h, b, box=(w / 2, h * .8, 500, 420))


def a_hummingbird(w, h):
    b = bird(F="#5fae6a", wing="#3f6f4a", rx=80, ry=44, tilt=-24, neck=4, nw=44, hr=32, beak="needle", leg_len=0, tail="fork", tail_col="#3f6f4a",
             belly="#eef0ea", sit=True, front=E(-92, -60, 20, 14, "#e2483c", 0))
    wings = P("M10 -90 C-20 -230 60 -280 110 -250 C90 -180 60 -130 30 -86 Z", "#d9e8dc", 2.6, extra='fill-opacity=".8"')
    fl = "".join(G_(flower(0, 0, "#e7a9c8", 1.4), x, y) for x, y in ((-190, 120), (-150, 140)))
    return scene("meadow", w, h, fl + G_(wings + b, 0, 0), box=(w / 2, h * .66, 420, 360))


def a_magpie(w, h):
    b = bird(F="#1f2328", wing="#2f4f7a", rx=70, ry=44, tilt=-16, neck=10, nw=40, hr=28, beak="short", beak_col="#1f2328", leg_len=60, leg_col="#1f2328", legw=5,
             tail="long", tail_col="#2a4a5a", belly="#ffffff")
    b += P("M-10 -110 C20 -130 60 -126 70 -100", sw=14, col="#ffffff")
    return scene("meadow", w, h, b, box=(w / 2, h * .76, 480, 320))


def a_sparrow(w, h):
    b = bird(F="#e9dcc8", wing="#a36b3e", rx=60, ry=44, tilt=-10, neck=4, nw=40, hr=30, beak="cone", beak_col="#3a3f45", leg_len=36, leg_col="#c9a27a", legw=4,
             tail="short", tail_col="#7a5a3a", head_col="#9a5a34", belly="#f3ece2")
    b += E(-62, -112, 9, 7, INK, 0) + P("M-80 -96 q10 10 24 0", sw=6, col=INK)
    b += "".join(P(f"M{-10+i*20} -120 l10 6", sw=3, col="#3a2a1a") for i in range(3))
    seeds = "".join(E(-120 + i * 18, -4, 5, 3, "#c9a27a", 1.6) for i in range(4))
    return scene("meadow", w, h, b + seeds, box=(w / 2, h * .76, 360, 260))


def a_woodpecker(w, h):
    b = bird(F="#1f2328", wing="#1f2328", rx=56, ry=34, tilt=0, neck=6, nw=34, hr=24, beak="long", beak_col="#3a3f45", leg_len=20, leg_col="#6b7075", legw=4,
             tail="short", tail_col="#1f2328", belly="#f3efe6", crest=None)
    b += "".join(R(-10 + i * 16, -78, 8, 6, "#ffffff", 0, 0) for i in range(4)) + E(-40, -68, 16, 10, "#ffffff", 0) + E(60, -52, 12, 8, "#e2483c", 0)
    b += E(-48, -112, 10, 7, "#e2483c", 0)
    g = f'<g transform="rotate(70)">{b}</g>'
    trunk = R(-30, -360, 60, 400, "#c9a27a", 6, 3) + P("M-12 -300 v60 M10 -200 v80 M-4 -80 v40", sw=2, col="#8a6a4a")
    return scene("forest", w, h, trunk + G_(g, 40, -120), box=(w / 2, h * .76, 360, 440))


def a_swan(w, h):
    b = bird(F="#fbfbf8", wing="#eceee9", rx=110, ry=56, tilt=-4, neck=150, nw=28, hr=26, beak="duck", beak_col="#f2d23a", leg_len=0, tail="up", tail_col="#fbfbf8", sit=True)
    water = P("M-200 -10 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0 q25 -12 50 0 q25 12 50 0", sw=2.6, col=BLUE)
    return scene("pond", w, h, b + water, box=(w / 2 - 20, h * .74, 480, 400))


def a_macaw(w, h):
    b = bird(F="#3a7fd0", wing="#2f6ab8", rx=60, ry=46, tilt=-50, neck=10, nw=40, hr=32, beak="hook", beak_col="#2a2a2a", leg_len=24, leg_col="#6b6b6b", legw=5,
             tail="long", tail_col="#3a7fd0", belly="#f6c33a", eye_ring="#ffffff")
    return scene("rainforest", w, h, branch(-160, 160, 4) + b, box=(w / 2, h * .66, 440, 420))


def a_pigeon(w, h):
    b = bird(F="#a9b0ba", wing="#c3c8cf", rx=72, ry=48, tilt=-12, neck=20, nw=46, hr=28, beak="short", beak_col="#3a3f45", leg_len=40, leg_col="#d96a6a", legw=5,
             tail="short", tail_col="#7c838d", head_col="#8f97a2")
    b += P("M-82 -100 C-70 -90 -52 -90 -40 -100", sw=10, col="#6fae8f") + P("M-8 -100 l50 6 M-4 -86 l50 6", sw=6, col="#3a3f45")
    return scene("meadow", w, h, b, box=(w / 2, h * .76, 420, 300))


ART3.update({"bald-eagle": a_baldeagle, "barn-owl": a_barnowl, "ostrich": a_ostrich, "flamingo": a_flamingo, "peafowl": a_peafowl, "crane": a_crane,
             "hummingbird": a_hummingbird, "magpie": a_magpie, "sparrow": a_sparrow, "woodpecker": a_woodpecker, "swan": a_swan, "macaw": a_macaw, "pigeon": a_pigeon})


# ---------------------------------------------------------------- reptiles & amphibians
def lizard(F, L=300, H=60, tail=1.0, snout=70, sh=34, belly=None, scutes=None, crest=None, dewlap=None, casque=None, eye_top=False, legs=26, legh=40,
           spots=None, gills=None, flat=False, fin=None, curl=False, toes=True, eye_col=INK, smile=False):
    o = []
    x0, x1 = -L / 2, L / 2
    yb = -legh * .6
    yt = yb - H
    tl = L * tail
    farc = darker(F, .85)
    # far legs
    for x in (x0 + L * .22, x1 - L * .18):
        o.append(P(f"M{x+10} {yb-H*.3} l-14 {legh*.5} l-14 {legh*.5}", sw=legs * .8 + 5) + P(f"M{x+10} {yb-H*.3} l-14 {legh*.5} l-14 {legh*.5}", sw=legs * .8, col=farc))
    # tail
    if curl:
        td = f"M{x1-10} {yt+H*.2} C{x1+tl*.6} {yt} {x1+tl*.7} {yb+H*.6} {x1+tl*.4} {yb+H*.2} C{x1+tl*.25} {yb} {x1+tl*.4} {yb-H*.5} {x1+tl*.5} {yb-H*.2}"
        o.append(P(td, sw=H * .5 + 5) + P(td, sw=H * .5, col=F))
    else:
        o.append(P(f"M{x1-20} {yt+H*.1} C{x1+tl*.4} {yt+H*.4} {x1+tl*.8} {yb} {x1+tl} {yb+H*.2} C{x1+tl*.7} {yb+H*.3} {x1+tl*.3} {yb+H*.2} {x1-20} {yb} Z", F))
        if fin:
            o.append(P(f"M{x0+L*.1} {yt+4} C{x1} {yt-H*.6} {x1+tl*.6} {yb-H*.2} {x1+tl} {yb+H*.2} C{x1+tl*.5} {yb+H*.6} {x1} {yb+H*.5} {x0+L*.3} {yb+4}", fin, 2.4, extra='fill-opacity=".7"'))
    # body
    body = f"M{x0} {yt+H*.2} C{x0+L*.1} {yt-H*.1} {x1-L*.1} {yt-H*.1} {x1} {yt+H*.2} C{x1+6} {yb-H*.2} {x1-L*.1} {yb+4} {x1-L*.3} {yb+4} L{x0+L*.2} {yb+4} C{x0} {yb} {x0-6} {yb-H*.3} {x0} {yt+H*.2} Z"
    inner = ""
    if belly:
        inner += R(x0 - 20, yb - H * .25, L + 40, H * .5, belly, 0, 0, "none")
    if spots:
        inner += "".join(E(x0 + 20 + (i * 41) % int(L - 30), yt + 10 + (i * 17) % int(H * .6), 9, 6, spots, 0) for i in range(18))
    if scutes:
        inner += "".join(P(f"M{x0+20+i*26} {yt-4} l8 -10 l8 10", scutes, 2) for i in range(int(L / 26) - 1))
        inner += "".join(P(f"M{x0+10} {yt+12+j*12} H{x1}", sw=1.6, col=darker(F, .7)) for j in range(3))
    o.append(P(body, F) + (clip(body, inner) if inner else "") + P(body, "none"))
    if scutes:
        o.append("".join(poly([(x0 + 24 + i * 26, yt + 2), (x0 + 32 + i * 26, yt - 10), (x0 + 40 + i * 26, yt + 2)], scutes, 2.2) for i in range(int(L / 26) - 1)))
    if crest:
        o.append("".join(poly([(x0 + 10 + i * 18, yt + 4), (x0 + 18 + i * 18, yt - 18 + (i % 2) * 6), (x0 + 26 + i * 18, yt + 4)], crest, 2.2) for i in range(int(L / 18))))
    # head
    hx, hy = x0 - snout * .35, yt + H * .45
    hd = f"M{x0+20} {yt+H*.05} C{x0-10} {yt-sh*.3} {x0-snout*.6} {hy-sh*.6} {x0-snout} {hy-sh*.2} L{x0-snout} {hy+sh*.35} C{x0-snout*.6} {hy+sh*.6} {x0} {yb} {x0+20} {yb}"
    if casque:
        o.append(P(f"M{x0+20} {yt+H*.1} C{x0+10} {yt-casque} {x0-snout*.2} {yt-casque*1.1} {x0-snout*.45} {hy-sh*.5} Z", F, 2.8))
    o.append(P(hd + " Z", F))
    if dewlap:
        o.append(P(f"M{x0-snout*.3} {hy+sh*.45} C{x0-snout*.2} {hy+sh*1.6} {x0+10} {hy+sh*1.5} {x0+20} {yb-4} Z", dewlap, 2.6))
    if gills:
        for k, a in enumerate((-50, -20, 10)):
            gx, gy = x0 + 6, yt + 6 + k * 10
            d = f"M{gx} {gy} q{-6+k*4} -30 {10+k*6} -50"
            o.append(P(d, sw=12) + P(d, sw=7, col=gills))
    ey = (yt - 4) if eye_top else (hy - sh * .25)
    ex = x0 - snout * .25
    if eye_top:
        o.append(E(ex, ey, 14, 11, F))
    o.append(C(ex, ey, 7, "#f2e28a" if eye_col == INK else "#fff", 2) + C(ex, ey, 3.5, INK, 0))
    if smile:
        o.append(P(f"M{x0-snout+4} {hy+sh*.15} C{x0-snout*.5} {hy+sh*.45} {x0-snout*.2} {hy+sh*.4} {x0+2} {hy+sh*.1}", sw=2.6))
    else:
        o.append(P(f"M{x0-snout+4} {hy+sh*.12} L{x0+6} {hy+sh*.15}", sw=2.4))
    # near legs
    for x in (x0 + L * .18, x1 - L * .22):
        d = f"M{x} {yb-H*.3} l-18 {legh*.5} l-12 {legh*.5}"
        o.append(P(d, sw=legs + 5) + P(d, sw=legs, col=F))
        if toes:
            o.append(P(f"M{x-30} 0 l-14 0 M{x-30} 0 l-10 -8 M{x-30} 0 l6 0", sw=3))
    return "".join(o)


def a_cnalligator(w, h):
    a = lizard("#5f6650", L=300, H=56, tail=.95, snout=86, sh=26, belly="#c9c6a6", scutes="#4a5040", legs=22, legh=30)
    return scene("wetland", w, h, a, box=(w / 2, h * .78, 620, 260))


def a_nilecroc(w, h):
    a = lizard("#7f8a5a", L=340, H=62, tail=1.0, snout=110, sh=26, belly="#e1dcb0", scutes="#5f6a44", legs=24, legh=30)
    teeth = "".join(poly([(-170 - 110 + 14 + i * 14, -76 + 2), (-170 - 110 + 20 + i * 14, -70), (-170 - 110 + 26 + i * 14, -76 + 2)], "#fff", 1.4) for i in range(5))
    return scene("wetland", w, h, a + teeth, box=(w / 2, h * .78, 640, 260))


def a_komodo(w, h):
    a = lizard("#8a7a60", L=300, H=70, tail=.9, snout=80, sh=34, belly="#b8a98a", legs=28, legh=50)
    return scene("savanna", w, h, a, box=(w / 2, h * .78, 620, 280))


def a_chameleon(w, h):
    a = lizard("#7cbf5a", L=160, H=70, tail=1.1, snout=40, sh=40, casque=70, curl=True, legs=14, legh=46, spots="#e9d86a", eye_top=True, toes=False)
    return scene("rainforest", w, h, branch(-180, 200, 4, 12) + a, box=(w / 2, h * .66, 440, 360))


def snake_coil(F, pat=None, hood=False, L=1.0):
    o = []
    for r, y in ((150, -30), (120, -60)):
        o.append(E(0, y, r * L, 34 * L, F, 3))
        if pat:
            o.append("".join(P(f"M{math.cos(a)*r*L:.0f} {y+math.sin(a)*34*L:.0f} l4 -8", sw=6, col=pat) for a in [i * .5 for i in range(13)]))
    neck = f"M-60 -80 C-80 -160 -40 -220 -70 -280"
    o.append(P(neck, sw=50 * L + 6) + P(neck, sw=50 * L, col=F))
    if hood:
        o.append(P("M-70 -300 C-150 -300 -150 -200 -76 -170 C-0 -200 10 -300 -70 -300 Z", F, 3) + P("M-70 -290 C-110 -280 -110 -220 -74 -196 C-40 -220 -36 -280 -70 -290 Z", darker(F, .85), 0))
    o.append(E(-80, -300, 40, 26, F) + C(-100, -306, 5, INK, 0) + P("M-118 -296 l-26 2 l-8 -6 M-144 -294 l-8 6", sw=2.6, col="#e2483c"))
    return "".join(o)


def a_kingcobra(w, h):
    return scene("rainforest", w, h, snake_coil("#6a6a3a", pat="#e9d86a", hood=True), box=(w / 2, h * .76, 440, 420))


def a_python(w, h):
    F = "#a68a4a"
    d = "M260 -20 C180 -40 140 20 60 0 C-20 -20 -40 -80 -120 -60 C-180 -46 -200 -20 -250 -30"
    o = P(d, sw=58) + P(d, sw=52, col=F)
    o += "".join(P(d, sw=46, col="#5a4a2a", extra=f'stroke-dasharray="14 40" stroke-dashoffset="{k}"') for k in (0,))
    o += P(d, sw=10, col="#d9c38a", extra='stroke-dasharray="20 34"')
    o += E(-270, -34, 40, 22, F) + C(-290, -42, 5, INK, 0) + P("M-306 -30 l-24 2 l-8 -6 M-330 -28 l-8 6", sw=2.6, col="#e2483c")
    return scene("rainforest", w, h, o, box=(w / 2, h * .76, 640, 220))


def a_tortoise(w, h):
    t = turtle(shell="#6b6a5a", skin="#9a9480", L=320, H=170, scute="#5a594a", neck=70, plastron="#8a8470")
    return scene("savanna", w, h, t, box=(w / 2, h * .76, 560, 300))


def a_iguana(w, h):
    a = lizard("#6fae5a", L=220, H=60, tail=1.6, snout=60, sh=34, crest="#5a9a4a", dewlap="#8fc86a", legs=18, legh=40, belly="#a9d48a")
    return scene("rainforest", w, h, branch(-260, 260, 4, 12) + a, box=(w / 2, h * .66, 620, 300))


def frog(F, belly, spots=None):
    o = []
    o.append(P("M100 -10 C160 -10 170 -60 120 -80 C90 -90 60 -50 60 -20 Z", darker(F, .9)))  # hind leg thigh
    o.append(P("M120 -8 l60 4 l-50 -12", sw=8, col=INK) + P("M110 -4 l70 4", sw=10, col=darker(F, .9)))
    body = "M-140 -60 C-140 -150 60 -160 120 -80 C150 -40 110 0 40 0 L-90 0 C-130 0 -140 -30 -140 -60 Z"
    inner = E(-40, -10, 120, 30, belly, 0)
    if spots:
        inner += "".join(E(-80 + (i * 47) % 200, -110 + (i * 23) % 60, 12, 8, spots, 0) for i in range(8))
    o.append(P(body, F) + clip(body, inner) + P(body, "none"))
    o.append(C(-100, -130, 26, F) + C(-100, -130, 15, "#f2e28a", 2) + E(-100, -130, 9, 5, INK, 0))
    o.append(C(-40, -108, 22, darker(F, .85), 2.6) + C(-40, -108, 10, darker(F, .7), 0))  # eardrum
    o.append(P("M-136 -70 C-100 -50 -60 -56 -30 -70", sw=2.6))
    o.append(P("M-60 -20 l-14 20 M-74 0 l-14 0 M-74 0 l-4 -6 M-74 0 l8 0", sw=8, col=F) + P("M-88 0 l-12 0 M-74 0 l10 0", sw=3))
    return "".join(o)


def a_bullfrog(w, h):
    return scene("pond", w, h, frog("#6f9a4a", "#efe8c8", spots="#4f7a3a"), box=(w / 2 - 20, h * .76, 420, 240))


def a_giantsal(w, h):
    a = lizard("#6a5a44", L=300, H=46, tail=.8, snout=50, sh=34, spots="#4a3e30", legs=20, legh=22, fin="#6a5a44", smile=True)
    return scene("pond", w, h, a, box=(w / 2, h * .76, 600, 220))


def a_axolotl(w, h):
    a = lizard("#f6c3cf", L=200, H=54, tail=.9, snout=34, sh=40, gills="#e86a8a", legs=12, legh=26, fin="#fbe1e7", smile=True, eye_col="k", toes=False)
    return scene("tank", w, h, a, box=(w / 2, 400, 440, 220))


ART3.update({"cn-alligator": a_cnalligator, "nile-croc": a_nilecroc, "komodo": a_komodo, "chameleon": a_chameleon, "king-cobra": a_kingcobra,
             "python": a_python, "tortoise": a_tortoise, "iguana": a_iguana, "bullfrog": a_bullfrog, "giant-salamander": a_giantsal, "axolotl": a_axolotl})
