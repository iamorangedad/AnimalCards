"""Phase-3 art (cards 106-400): parametric variants of the shared helpers."""
import math
from iso import INK, GREY, MUTE, BLUE, BLUE_L, BLUE_M, ORG, ORG_L, YEL, YEL_L, SAGE, SAGE_L
from art import P, E, C, svg, slab, shadow, tuft, rock, sun, seaweed, tentacle, wavy, leg, bamboo
from art2 import uid, fit, R, poly, clip, darker, tree, pine, mountains, flower, bubbles, G_, scene, quad, fish, turtle, bird, blob, ape
from art3 import coast, pinniped, anemone, branch, lizard, snake_coil, frog, legs6, antenna, wing

ART4 = {}
def reg(i):
    def d(f):
        ART4[i] = f
        return f
    return d

def bhead(rx=90, ry=62, neck=30, hr=34, leg_len=70, sit=False):
    by = -(leg_len + ry * .9)
    nx, ny = -rx * .72, by - ry * .3
    return nx - neck * .35, ny - neck - hr * .6

def crest_fan(hx, hy, hr, col, n=5, L=1.0, back=True):
    o = ""
    for i in range(n):
        a = math.radians(-100 + i * 14 if back else -80 - i * 14)
        x1, y1 = hx + math.cos(a) * hr * 2.2 * L + hr * .5, hy + math.sin(a) * hr * 2.2 * L
        o += P(f"M{hx+hr*.1:.0f} {hy-hr*.7:.0f} Q{hx+hr*.2+ (x1-hx)*.3:.0f} {y1+hr*.6:.0f} {x1:.0f} {y1:.0f}", sw=7, col=INK) + P(f"M{hx+hr*.1:.0f} {hy-hr*.7:.0f} Q{hx+hr*.2+(x1-hx)*.3:.0f} {y1+hr*.6:.0f} {x1:.0f} {y1:.0f}", sw=4, col=col)
    return o

def perch_scene(b, kind="home", box=None, w=0, h=0, x0=-150, x1=150):
    return scene(kind, w, h, branch(x0, x1, 4) + b, box=box or (w / 2, h * .66, 420, 380))

def cage_bird(w, h, kind="home", box=None, **kw):
    b = bird(**kw)
    return perch_scene(b, kind, box, w, h)

def birdkw(**kw):
    return kw

def headparts(kw):
    return bhead(kw.get("rx", 90), kw.get("ry", 62), kw.get("neck", 30), kw.get("hr", 34), kw.get("leg_len", 70))

def mk_bird(kw, kind="home", box=None, perch=True, front_fn=None, extra_fn=None, scale_box=None):
    def f(w, h):
        k = dict(kw)
        hx, hy = headparts(k)
        if front_fn: k["front"] = k.get("front", "") + front_fn(hx, hy, k.get("hr", 34))
        b = bird(**k)
        if extra_fn: b = extra_fn(hx, hy, k.get("hr", 34)) + b
        bx = box or ((w / 2, h * .66, 420, 380) if perch else (w / 2, h * .76, 460, 360))
        return scene(kind, w, h, (branch(-150, 150, 4) if perch else "") + b, box=bx)
    return f

# ------------------------------------------------------------------ 宠物 106-
@reg("ferret")
def a_ferret(w, h):
    a = quad(F="#e9dcc4", bl=300, bd=80, lh=50, lw=22, belly="#fbf6ec", farleg="#5a4a3a", neck=(30, 60), nw=56, head=(40, 32), snout=(34, 22),
             snout_col="#fbf6ec", ears="round", tail="long", tail_col="#5a4a3a", mask="#6b5440")
    return scene("home", w, h, a, box=(w / 2, h * .74, 600, 260))

ck = dict(F="#bfc3c7", wing="#9aa0a6", rx=58, ry=40, tilt=-36, neck=8, nw=40, hr=30, beak="hook", beak_col="#c9c2b8", leg_len=28, leg_col="#9a8f86", legw=5,
          tail="long", tail_col="#8a9096", head_col="#f6e26a")
ART4["cockatiel"] = mk_bird(ck, front_fn=lambda x, y, r: C(x + r * .05, y + r * .25, r * .32, "#f08a4a", 0) + crest_fan(x, y, r, "#f6e26a", 4, .9))
ART4["lovebird"] = mk_bird(dict(F="#8fcf6a", wing="#6fae4f", rx=56, ry=42, tilt=-28, neck=4, nw=44, hr=30, beak="hook", beak_col="#f2dcc0", leg_len=26, leg_col="#9a8f86",
          tail="short", tail_col="#5aa0d8", head_col="#f6a09a", eye_ring="#ffffff"), kind="savanna")
ART4["canary"] = mk_bird(dict(F="#f6d93a", wing="#e9c22a", rx=58, ry=42, tilt=-24, neck=4, nw=40, hr=28, beak="cone", beak_col="#f2dcc0", leg_len=28, leg_col="#e8b8a0",
          tail="fork", tail_col="#e9c22a"))
ART4["zebra-finch"] = mk_bird(dict(F="#bfc3c7", wing="#a9a097", rx=54, ry=40, tilt=-20, neck=4, nw=38, hr=28, beak="cone", beak_col="#e2483c", leg_len=26, leg_col="#f2a98a",
          tail="short", tail_col="#3a3f45", belly="#f6efe2"), front_fn=lambda x, y, r: C(x + r * .25, y + r * .15, r * .32, "#f08a4a", 0) + P(f"M{x-r*.6} {y+r*.2} l6 24", sw=4, col=INK),
          extra_fn=lambda x, y, r: "")
ART4["monk-parakeet"] = mk_bird(dict(F="#8fcf6a", wing="#5aa04a", rx=60, ry=44, tilt=-34, neck=6, nw=42, hr=30, beak="hook", beak_col="#f2c9a0", leg_len=28, leg_col="#9a8f86",
          tail="long", tail_col="#5aa04a", head_col="#c9ced3", belly="#c9ced3"), kind="meadow")
ART4["african-grey"] = mk_bird(dict(F="#a9adb2", wing="#8f949a", rx=62, ry=46, tilt=-40, neck=8, nw=44, hr=32, beak="hook", beak_col="#2a2a2a", leg_len=28, leg_col="#6b6b6b",
          tail="short", tail_col="#e2483c", eye_ring="#ffffff"), kind="rainforest")
ART4["cockatoo"] = mk_bird(dict(F="#fbfbf8", wing="#eceee9", rx=64, ry=48, tilt=-40, neck=8, nw=44, hr=34, beak="hook", beak_col="#2a2a2a", leg_len=30, leg_col="#6b6b6b",
          tail="short", tail_col="#eceee9"), kind="forest", front_fn=lambda x, y, r: crest_fan(x, y, r, "#f6d93a", 5, 1.1))
ART4["sun-conure"] = mk_bird(dict(F="#f6c33a", wing="#4fa04a", rx=58, ry=44, tilt=-36, neck=6, nw=42, hr=30, beak="hook", beak_col="#2a2a2a", leg_len=28, leg_col="#8a8a8a",
          tail="long", tail_col="#3a7fd0", head_col="#f6a03a", belly="#f6903a", eye_ring="#ffffff"), kind="rainforest")
ART4["myna"] = mk_bird(dict(F="#2a2a2e", wing="#1f1f22", rx=62, ry=42, tilt=-14, neck=6, nw=40, hr=28, beak="short", beak_col="#f2e3a0", leg_len=40, leg_col="#e8c86a",
          tail="short", tail_col="#1f1f22", eye_ring=None), kind="meadow", perch=False,
          front_fn=lambda x, y, r: P(f"M{x-r*.7} {y-r*.7} q-4 -20 10 -26 q4 14 6 22", "#2a2a2e", 2.4) + E(-20, -74, 14, 7, "#fff", 0))

ART4["degu"] = lambda w, h: scene("desert", w, h, rodent("#a8875e", 230, 140, belly="#e9dcc4", ears="round", tail="rope", tailcol="#7a5a3a", tl=1.0, tuft_=True, nose="#6b5038"), box=(w / 2, h * .74, 560, 280))

@reg("sugar-glider")
def a_glider(w, h):
    F = "#a9adb2"
    o = [P("M-150 -160 C-60 -200 80 -200 170 -150 L190 -80 C80 -60 -60 -60 -170 -90 Z", "#c9ccd1", 3)]
    o.append(P("M150 -120 C230 -120 280 -90 320 -40", sw=26) + P("M150 -120 C230 -120 280 -90 320 -40", sw=20, col=F) + P("M300 -52 L330 -30", sw=20, col=INK))
    o.append(E(0, -130, 140, 44, F) + P("M-120 -136 L130 -136", sw=8, col=INK))
    o.append(C(-160, -140, 40, F) + C(-150, -184, 14, F, 2.8) + C(-186, -176, 14, F, 2.8) + P("M-160 -180 L-160 -150", sw=6, col=INK))
    o.append(C(-176, -146, 9, INK, 0) + C(-142, -146, 9, INK, 0) + C(-178, -149, 3, "#fff", 0) + C(-144, -149, 3, "#fff", 0) + E(-160, -122, 6, 4, "#e8a0a0", 0))
    return scene("forest", w, h, G_("".join(o), 0, 0), box=(w / 2, h * .56, 600, 300))

ART4["leopard-gecko"] = lambda w, h: scene("desert", w, h, lizard("#f2d36a", L=220, H=60, tail=.7, snout=50, sh=40, belly="#fbf3d8", spots="#5a4a3a", legs=16, legh=34, smile=True), box=(w / 2, h * .76, 560, 240))
ART4["crested-gecko"] = lambda w, h: scene("rainforest", w, h, branch(-220, 220, 4, 12) + lizard("#d98a4a", L=200, H=56, tail=.9, snout=44, sh=42, crest="#f2b06a", legs=14, legh=34, eye_top=True), box=(w / 2, h * .68, 560, 260))
ART4["bearded-dragon"] = lambda w, h: scene("desert", w, h, lizard("#d9a860", L=240, H=64, tail=1.1, snout=56, sh=40, belly="#f2dcb0", crest="#b98a4a", dewlap="#a87a40", legs=18, legh=36, spots="#c99a50"), box=(w / 2, h * .76, 600, 260))
ART4["corn-snake"] = lambda w, h: scene("farm", w, h, snake_coil("#f2a05a", pat="#d9482c"), box=(w / 2, h * .76, 420, 400))
ART4["ball-python"] = lambda w, h: scene("savanna", w, h, snake_coil("#7a5a3a", pat="#d9b27a", L=1.1), box=(w / 2, h * .76, 440, 400))
ART4["russian-tortoise"] = lambda w, h: scene("desert", w, h, turtle(shell="#c9a86a", skin="#b9a888", L=260, H=150, scute="#8a6a3a", neck=50, plastron="#e9d8a8"), box=(w / 2, h * .76, 500, 280))
ART4["sulcata"] = lambda w, h: scene("desert", w, h, turtle(shell="#d9b47a", skin="#c9ae84", L=340, H=180, scute="#b8935a", neck=60, plastron="#f0dcb0"), box=(w / 2, h * .76, 600, 320))
ART4["reeves-turtle"] = lambda w, h: scene("pond", w, h, turtle(shell="#6b5a3a", skin="#6f7a5a", L=260, H=110, stripes="#e9d86a", scute="#5a4a30", neck=40, plastron="#e9d8a8"), box=(w / 2, h * .76, 500, 240))

ART4["hill-myna"] = mk_bird(dict(F="#1f2228", wing="#1a1c20", rx=64, ry=44, tilt=-18, neck=6, nw=42, hr=30, beak="short", beak_col="#f08a2a", leg_len=34, leg_col="#f2c53a",
          tail="short", tail_col="#1a1c20"), kind="rainforest",
          front_fn=lambda x, y, r: P(f"M{x+r*.1} {y+r*.1} q{r*.5} {r*.1} {r*.8} {-r*.5}", sw=8, col="#f6d93a") + E(-10, -70, 14, 7, "#fff", 0))
ART4["hwamei"] = mk_bird(dict(F="#b9874a", wing="#9a6e3a", rx=62, ry=42, tilt=-14, neck=6, nw=40, hr=28, beak="short", beak_col="#e8c86a", leg_len=34, leg_col="#c9a27a",
          tail="long", tail_col="#7a5530"), kind="forest",
          front_fn=lambda x, y, r: C(x - r * .2, y - r * .15, r * .32, "none", 3.4, "#ffffff") + P(f"M{x-r*.0} {y-r*.2} l{r*.7} {-r*.05}", sw=4, col="#ffffff"))
ART4["white-eye"] = mk_bird(dict(F="#b9d86a", wing="#8fb84a", rx=50, ry=36, tilt=-20, neck=4, nw=34, hr=24, beak="short", beak_col="#3a3f45", leg_len=24, leg_col="#6b7075",
          tail="short", tail_col="#7aa040", belly="#f2f2ea", eye_ring="#ffffff"), kind="meadow",
          extra_fn=lambda x, y, r: G_(flower(0, 0, "#f6c9d8", 1.4), 190, -10))

def rodent(F, L, H, belly="#fff8ec", ears="round", tail=None, stripe=None, nose="#e88a8a", cheeks=False, tailcol=None, tl=1.0, tuft_=False):
    o = ""
    if tail == "rope":
        tc = tailcol or "#f2b8b0"
        d = f"M{L*.4} {-H*.2} C{L*.8} {-H*.1} {L*(.9+.3*tl)} {-H*.05} {L*(1.05+.4*tl)} {-H*.25}"
        o += P(d, sw=H * .09 + 4) + P(d, sw=H * .09, col=tc)
        if tuft_:
            o += E(L * (1.05 + .4 * tl), -H * .25, 16, 9, darker(F, .7), 2.2, rot=-20)
    b = blob(F=F, L=L, H=H, belly=belly, ears=ears, tail=None, cheeks=cheeks, stripe=None, nose=nose)
    if stripe:
        b += P(f"M{-L*.25} {-H*1.0} C{0} {-H*1.08} {L*.25} {-H*.98} {L*.42} {-H*.6}", sw=6, col=stripe)
    return o + b

ART4["gerbil"] = lambda w, h: scene("desert", w, h, rodent("#d9b27a", 200, 140, ears="round", tail="rope", tailcol="#d9b27a", tl=1.2, tuft_=True, nose="#c98a6a"), box=(w / 2, h * .74, 560, 280))
ART4["fancy-rat"] = lambda w, h: scene("home", w, h, rodent("#f6f4ee", 240, 140, ears="round", tail="rope", tl=1.4, belly="#ffffff"), box=(w / 2, h * .74, 600, 280))
ART4["fancy-mouse"] = lambda w, h: scene("home", w, h, rodent("#c9b49a", 170, 110, ears="big", tail="rope", tl=1.3, belly="#f6efe2") +
                                         G_(poly([(0, 0), (40, -40), (80, 0)], YEL_L, 2.6) + C(30, -14, 6, "#e8d48a", 0) + C(52, -10, 4, "#e8d48a", 0), 160, 0), box=(w / 2, h * .74, 520, 260))
ART4["robo-hamster"] = lambda w, h: scene("desert", w, h, rodent("#e6c79a", 180, 130, belly="#ffffff", ears="round", nose="#e8a0a0"), box=(w / 2, h * .74, 400, 260))
ART4["winter-white"] = lambda w, h: scene("snow", w, h, rodent("#f2f2ee", 200, 140, belly="#ffffff", ears="round", stripe="#a9adb2", cheeks=True), box=(w / 2, h * .74, 420, 270))
ART4["campbell"] = lambda w, h: scene("home", w, h, rodent("#c9b29a", 200, 140, belly="#f4f0ea", ears="round", stripe="#5a4a3e", cheeks=True), box=(w / 2, h * .74, 420, 270))
ART4["cn-hamster"] = lambda w, h: scene("home", w, h, rodent("#a9927a", 220, 120, belly="#f4f0ea", ears="round", stripe="#3a3f45", tail="rope", tl=.25, tailcol="#c9b29a"), box=(w / 2, h * .74, 440, 260))

def tank(f, box=(None, 330, 330, 210)):
    return lambda w, h: scene("tank", w, h, f, box=(w / 2 if box[0] is None else box[0], box[1], box[2], box[3]))

ART4["neon-tetra"] = tank(fish(F="#c9d3dc", L=220, H=80, tail="fork", eye_r=8, fin_col="#e6ecf1",
                               extras=P("M-96 -10 L90 -10", sw=12, col="#3fb6e8") + P("M-10 14 C30 20 70 16 96 6", sw=14, col="#e2483c")) +
                          G_(fish(F="#c9d3dc", L=140, H=52, tail="fork", eye_r=6, extras=P("M-60 -6 L58 -6", sw=8, col="#3fb6e8") + P("M-6 9 L60 4", sw=9, col="#e2483c")), 150, -110))
ART4["betta"] = tank(P("M-20 30 C-40 120 60 160 120 120 C80 80 60 50 30 30 Z", "#c8324a", 2.6, extra='fill-opacity=".9"') +
                     P("M-40 -40 C-20 -140 80 -150 140 -90 C100 -60 60 -50 20 -40 Z", "#c8324a", 2.6, extra='fill-opacity=".9"') +
                     fish(F="#3a5ab8", L=200, H=90, tail="fan", tail_col="#c8324a", eye_r=8, fin_col="#c8324a", dorsal=False), box=(None, 320, 360, 260))
ART4["koi"] = lambda w, h: scene("pond", w, h, G_(fish(F="#fbfaf6", L=300, H=110, tail="fork", eye_r=8, fin_col="#fbfaf6",
                                 extras=P(wavy(-40, -20, 50, 26, 6, 6), "#e8582c", 0) + P(wavy(60, 0, 40, 24, 6, 6), "#e8582c", 0) + P("M-150 6 q-10 8 -4 18", sw=2.4)), 0, -60), box=(w / 2, h * .7, 520, 260))
ART4["angelfish"] = tank(poly([(-30, -40), (40, -230), (70, -40)], "#e9e6dc", 2.6) + poly([(-20, 40), (50, 230), (70, 40)], "#e9e6dc", 2.6) +
                         fish(F="#e9e6dc", L=180, H=170, tail="fork", eye_r=8, dorsal=False, fin_col="#e9e6dc", stripes=("#3a3f45", [.18, .48, .72])), box=(None, 300, 300, 330))
ART4["zebrafish"] = tank(fish(F="#e9e2c8", L=230, H=70, tail="fork", eye_r=7, fin_col="#e9e2c8",
                              extras="".join(P(f"M-90 {y} L100 {y}", sw=6, col="#3a5ab8") for y in (-16, -4, 8, 20))), box=(None, 330, 330, 200))
ART4["platy"] = tank(fish(F="#f08a2a", L=200, H=100, tail="round", eye_r=8, fin_col="#f6a04a", tail_col="#2a2a2a"), box=(None, 330, 300, 200))
ART4["discus"] = tank(fish(F="#3a8fc9", L=200, H=200, tail="round", eye_r=8, fin_col="#e8582c",
                           extras="".join(P(f"M-80 {y} q80 -20 170 0", sw=6, col="#e8582c") for y in (-50, -20, 10, 40))), box=(None, 320, 300, 300))

def shrimp(F="#e2483c", L=260, H=60, claw=False, strip=None):
    o = []
    for i in range(5):
        x = -60 + i * 30
        o.append(P(f"M{x} {-H*.2} l-8 {H*.9}", sw=4, col=darker(F, .8)))
    segs = 6
    for i in range(segs):
        x = -L * .3 + i * L * .12
        o.append(E(x, -H * .55 + i * 3, L * .1, H * (.5 - i * .03), F, 2.6))
    o.append(P(f"M{L*.42} {-H*.4} l50 -30 l-10 36 l14 30 Z", F, 2.6))
    o.append(P(f"M{-L*.42} {-H*.7} C{-L*.5} {-H*1.6} {-L*.9} {-H*1.8} {-L*1.1} {-H*1.4}", sw=2.4) + P(f"M{-L*.42} {-H*.6} C{-L*.6} {-H*1.0} {-L*1.0} {-H*1.0} {-L*1.2} {-H*.6}", sw=2.4))
    o.append(P(f"M{-L*.46} {-H*.9} l-40 -10", sw=4, col=darker(F, .8)) + C(-L * .38, -H * .85, 7, INK, 0))
    if claw:
        o.append(P(f"M{-L*.3} {-H*.2} l-40 30 l-40 -10", sw=8, col=darker(F, .8)))
    return "".join(o)

ART4["cherry-shrimp"] = tank(shrimp() + G_(shrimp(L=160, H=38), 60, 90), box=(None, 340, 360, 240))
ART4["oscar"] = tank(fish(F="#5a5048", L=240, H=140, tail="round", eye_r=9, fin_col="#5a5048", extras=P(wavy(20, -10, 50, 30, 7, 6), "#e8702c", 0) + P(wavy(-60, 20, 40, 20, 6, 5), "#e8702c", 0) + C(90, -10, 12, "#e8702c", 3, INK)),
                     box=(None, 320, 360, 240))

# ------------------------------------------------------------------ 农场
def Q(kind, box=None, **kw):
    return lambda w, h: scene(kind, w, h, quad(**kw), box=box and (w / 2, h * box[0], box[1], box[2]))

ART4["water-buffalo"] = Q("wetland", F="#4a4a4e", bl=320, bd=150, lh=110, lw=36, neck=(10, 60), nw=90, head=(48, 44), snout=(42, 36), snout_col="#5a5a5e",
                          ears="side", horns="yak", tail="tuft", tail_col="#2a2a2e", hooves=INK, nose=None, headdown=10)
ART4["dom-yak"] = Q("plateau", F="#3a2e25", bl=300, bd=140, lh=110, lw=34, pattern="patches", pat_col="#f4efe6", neck=(10, 50), nw=90, head=(48, 46), snout=(40, 38),
                    snout_col="#f4efe6", ears="side", horns="yak", tail="horse", tail_col="#f4efe6", skirt="#2e241d", hooves=INK, nose=None)

def _turkey(w, h):
    k = dict(F="#6b4a32", wing="#4a3222", rx=96, ry=74, tilt=-6, neck=40, nw=34, hr=26, beak="short", beak_col="#e9d8b8", leg_len=80, leg_col="#e8a0a0", legw=7,
             tail="fan", tail_col="#8a6a44", head_col="#9ab8d8", wattle=True)
    hx, hy = headparts(k)
    fan = "".join(P(f"M60 -170 L{60+math.cos(math.radians(a))*190:.0f} {-170+math.sin(math.radians(a))*190:.0f}", sw=26, col=INK) +
                  P(f"M60 -170 L{60+math.cos(math.radians(a))*186:.0f} {-170+math.sin(math.radians(a))*186:.0f}", sw=20, col="#8a6a44" if i % 2 else "#a8865a") for i, a in enumerate(range(-160, -10, 18)))
    b = fan + bird(**k) + P(f"M{hx-26} {hy-8} q-6 30 4 50", sw=7, col="#e2483c")
    return scene("farm", w, h, b, box=(w / 2, h * .78, 520, 420))
ART4["turkey"] = _turkey
ART4["muscovy"] = mk_bird(dict(F="#2a2e33", wing="#ffffff", rx=96, ry=52, tilt=-6, neck=22, nw=40, hr=30, beak="duck", beak_col="#e9c9b8", leg_len=34, leg_col="#e8a06a", legw=6,
                               tail="short", tail_col="#2a2e33", head_col="#ffffff", webbed=True), kind="pond", perch=False,
                          front_fn=lambda x, y, r: E(x - r * .3, y - r * .05, r * .45, r * .32, "#d9482c", 0) + C(x - r * .2, y - r * .15, 4, INK, 0), box=None)
ART4["quail"] = mk_bird(dict(F="#b9875a", wing="#8a6a44", rx=66, ry=50, tilt=-4, neck=4, nw=40, hr=26, beak="short", beak_col="#5a4a3a", leg_len=28, leg_col="#e8b8a0", legw=4,
                             tail="short", tail_col="#7a5a3a", belly="#e9cfa8"), kind="farm", perch=False,
                        extra_fn=lambda x, y, r: "".join(E(130 + i * 26, -12, 11, 14, "#f2e8d0", 2.2) + C(128 + i * 26, -14, 3, "#6b5038", 0) for i in range(3)))
ART4["guineafowl"] = mk_bird(dict(F="#5a6068", wing="#4a5058", rx=84, ry=60, tilt=-6, neck=26, nw=30, hr=22, beak="short", beak_col="#e9c9b8", leg_len=60, leg_col="#6b6b6b",
                                  tail="short", tail_col="#4a5058", head_col="#7ab0d8", wattle=True,
                                  extras="".join(C(-60 + (i * 31) % 150, -150 + (i * 17) % 90, 4, "#ffffff", 0) for i in range(30))), kind="farm", perch=False,
                             front_fn=lambda x, y, r: poly([(x - r * .3, y - r * .8), (x - r * .05, y - r * 1.7), (x + r * .3, y - r * .8)], "#c9a27a", 2.4))
ART4["mule"] = Q("farm", F="#8a5a3a", bl=300, bd=124, lh=150, lw=28, neck=(70, 30), nw=66, head=(42, 38), snout=(58, 36), snout_col="#c9a88a",
                 ears="long", mane="zebra", tail="horse", tail_col="#3a2a1e", hooves="#3a3f45", belly="#c9a88a")
ART4["llama"] = Q("plateau", (.76, 500, 440), F="#f1ece2", bl=240, bd=110, lh=150, lw=24, pattern="patches", pat_col="#8a5a3a", neck=(150, 6), nw=46, head=(34, 32),
                  snout=(32, 24), ears="big", tail="short", hooves="#5a5048", nose="#5a5048")
ART4["dromedary"] = Q("desert", (.75, 560, 440), F="#d8b27a", bl=280, bd=120, lh=190, lw=26, neck=(110, 52), nw=50, head=(38, 30), snout=(44, 30),
                      ears="small", tail="tuft", tail_col="#8a6a42", extras=P("M-50 -304 C-30 -372 50 -372 70 -304", "#d8b27a", 3))
ART4["reindeer"] = Q("snow", None, F="#8a6a4a", bl=280, bd=120, lh=130, lw=26, belly="#e9e1d2", neck=(50, 34), nw=70, head=(40, 36), snout=(44, 30),
                     snout_col="#c9b49a", ears="side", horns="antler", tail="short", tail_col="#f4efe6", hooves="#3a3f45", neck_wool="#e9e1d2")

# farm batch 2
def _dpigeon(w, h):
    b = bird(F="#f4f2ee", wing="#e4e2dc", rx=72, ry=48, tilt=-12, neck=20, nw=46, hr=28, beak="short", beak_col="#e9c9b8", leg_len=40, leg_col="#d96a6a", legw=5,
             tail="short", tail_col="#dcdad4", head_col="#f4f2ee")
    loft = P("M120 -40 L120 -150 L200 -200 L280 -150 L280 -40 Z", "#d9b27a", 2.6) + P("M170 -90 h60 v40 h-60 Z", "#5a4a3a", 2.2)
    return scene("farm", w, h, loft + b, box=(w / 2, h * .76, 520, 330))
ART4["dom-pigeon"] = _dpigeon
ART4["highland"] = Q("plateau", None, F="#b8642e", bl=300, bd=140, lh=100, lw=34, neck=(10, 50), nw=90, head=(50, 46), snout=(40, 38),
                     snout_col="#c9784a", ears="side", horns="ram" if False else "cow", tail="horse", tail_col="#8a4a22", hooves=INK, nose=None, skirt="#a8582a")
ART4["hereford"] = Q("farm", None, F="#9a3a22", bl=330, bd=150, lh=120, lw=36, belly="#f6f2ea", neck=(20, 60), nw=90, head=(52, 50), snout=(44, 40),
                     snout_col="#f6f2ea", ears="side", horns=None, tail="tuft", tail_col="#f6f2ea", hooves=INK, nose="#e8b0a8", mask="#f6f2ea")

def _silkworm(w, h):
    leaf = P("M-260 40 C-160 -120 120 -120 240 30 C120 110 -160 120 -260 40 Z", "#8fc06a", 2.8) + P("M-250 40 C-80 10 80 10 230 30", sw=2.4)
    body = "".join(E(-120 + i * 34, -10 - math.sin(i / 2) * 18, 26, 30 - abs(i - 3) * 1.5, "#f4f1e6", 2.6) for i in range(8))
    head = E(-150, -6, 22, 24, "#e9e2cf", 2.6) + C(-160, -10, 4, INK, 0)
    legs_ = "".join(P(f"M{-120+i*34} 18 l0 12", sw=3) for i in range(8))
    marks = P("M-60 -40 q8 -10 16 0 M-26 -46 q8 -10 16 0", sw=2.4, col="#a99f8a")
    coc = E(200, -40, 40, 26, "#fbf7e8", 2.6) + P("M170 -40 q30 -12 60 0 M172 -30 q28 -10 56 2", sw=1.6, col="#c9c0a8")
    return scene("leaf", w, h, leaf + legs_ + body + head + marks + coc, box=(w / 2, h * .66, 560, 280))
ART4["silkworm"] = _silkworm
_pond = lambda f, b=(.68, 520, 260): (lambda w, h: scene("pond", w, h, f, box=(w / 2, h * b[0], b[1], b[2])))
ART4["carp"] = _pond(fish(F="#b9963a", L=320, H=120, tail="fork", eye_r=8, fin_col="#9a7a2a", belly="#e9d9a0",
                          extras=P("M-155 8 q-14 10 -6 24", sw=3) + P("M-150 -2 q-16 0 -18 10", sw=2.4)))
ART4["grass-carp"] = _pond(fish(F="#8a9a6a", L=340, H=100, tail="fork", eye_r=8, fin_col="#6f7f52", belly="#e6e2c4"))
ART4["silver-carp"] = lambda w, h: scene("pond", w, h, G_(fish(F="#c9d0d6", L=320, H=110, tail="fork", eye_r=8, fin_col="#a9b2ba", belly="#f2f4f6"), 0, -90) +
                                         P("M-200 40 q20 -20 40 0 M160 30 q20 -20 40 0", sw=3, col="#7fb7d8"), box=(w / 2, h * .7, 520, 300))
ART4["tilapia"] = _pond(fish(F="#8a8f86", L=280, H=130, tail="round", eye_r=8, fin_col="#c95a4a", belly="#d9dcd2",
                             stripes=("#6b706a", [.3, .45, .6, .75])))

def _crab(w, h):
    F = "#5a6a4a"
    o = []
    for s in (-1, 1):
        for i in range(4):
            x = s * (60 + i * 22)
            o.append(P(f"M{s*50} {-40+i*10} L{x+s*50} {-70+i*6} L{x+s*80} {10+i*4}", sw=8, col=INK) + P(f"M{s*50} {-40+i*10} L{x+s*50} {-70+i*6} L{x+s*80} {10+i*4}", sw=5, col=F))
        cx = s * 120
        o.append(P(f"M{s*40} -70 L{cx} -130", sw=12, col=INK) + P(f"M{s*40} -70 L{cx} -130", sw=8, col=F))
        o.append(E(cx, -150, 34, 26, "#e9dcc0", 2.6) + E(cx, -134, 30, 16, "#6b5a3a", 0, extra='fill-opacity=".85"'))
    o.append(E(0, -50, 90, 62, F, 3) + C(-22, -112, 8, INK, 0) + C(22, -112, 8, INK, 0) + P("M-22 -104 v-6 M22 -104 v-6", sw=3))
    return scene("wetland", w, h, "".join(o), box=(w / 2, h * .72, 520, 300))
ART4["mitten-crab"] = _crab
ART4["whiteleg-shrimp"] = lambda w, h: scene("pond", w, h, G_(shrimp(F="#e6dccf", L=300, H=66), 0, -40) + G_(shrimp(F="#e6dccf", L=180, H=40), 80, 70), box=(w / 2, h * .7, 480, 300))

# farm batch 3
def _oyster(w, h):
    o = ""
    for dx, dy, s in ((-90, 0, 1), (110, 20, .8)):
        o += G_(P(f"M{-120*s} 0 C{-110*s} {-90*s} {60*s} {-110*s} {130*s} {-30*s} C{100*s} {30*s} {-60*s} {40*s} {-120*s} 0 Z", "#b9b3a6", 2.8) +
                "".join(P(f"M{-100*s+i*40*s} {-10*s} q{20*s} {-40*s} {50*s} {-60*s}", sw=2, col="#8a8478") for i in range(5)), dx, dy)
    o += G_(P("M-70 0 C-60 -50 50 -60 80 -20 C50 10 -40 20 -70 0 Z", "#f2ece0", 2.4) + E(0, -18, 40, 18, "#e6dcc8", 2), 0, 120)
    return scene("sea", w, h, o, box=(w / 2, h * .7, 440, 260))
ART4["oyster"] = _oyster
ART4["rainbow-trout"] = lambda w, h: scene("pond", w, h, G_(fish(F="#b9c2a6", L=320, H=96, tail="fork", eye_r=8, fin_col="#9aa486", belly="#eef0e6",
                                             extras=P("M-120 8 C-40 0 60 0 140 4", sw=16, col="#e88aa0") + "".join(C(-80 + (i * 37) % 220, -30 + (i * 13) % 18, 3.5, INK, 0) for i in range(18))), 0, -50), box=(w / 2, h * .7, 520, 260))
ART4["salmon"] = lambda w, h: scene("sea", w, h, G_(fish(F="#9aa8b6", L=340, H=100, tail="fork", eye_r=8, fin_col="#7a8898", belly="#eef2f6",
                                      extras="".join(P(f"M{-100+i*30} {-30+(i%3)*8} l6 6 m0 -6 l-6 6", sw=2.4) for i in range(8))), 0, -60), box=(w / 2, h * .7, 520, 260))
ART4["softshell"] = lambda w, h: scene("pond", w, h, turtle(shell="#7a8060", skin="#8a9070", L=300, H=70, scute=None, neck=70, plastron="#e9e2c8"), box=(w / 2, h * .76, 560, 220))
ART4["mink"] = Q("wetland", (.74, 600, 260), F="#3a2a22", bl=300, bd=76, lh=46, lw=22, neck=(30, 56), nw=54, head=(38, 30), snout=(32, 22), snout_col="#3a2a22",
                 ears="round", tail="bushy", tail_col="#2a1e18", extras=C(-196, -126, 6, "#ffffff", 0))
def _eel(F, L=420, H=34, belly=None, spots=None, fins=False):
    pts = [(-L / 2 + i * L / 20, -H - 40 * math.sin(i / 3.2)) for i in range(21)]
    d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    o = P(d, sw=H + 6, col=INK) + P(d, sw=H, col=F)
    if belly: o += P(d, sw=H * .3, col=belly, extra=f'transform="translate(0 {H*.28:.0f})"')
    if spots: o += "".join(C(x, y - 4, 3.5, spots, 0) for x, y in pts[3::2])
    x, y = pts[0]
    o += C(x + 10, y - 6, 5, INK, 0) + P(f"M{x-14} {y+4} l10 0", sw=2.4)
    return o
ART4["swamp-eel"] = lambda w, h: scene("wetland", w, h, _eel("#9a7a3a", belly="#d9c48a", spots="#5a4a2a"), box=(w / 2, h * .72, 520, 220))
ART4["loach"] = lambda w, h: scene("pond", w, h, G_(_eel("#b99a5a", L=320, H=40, belly="#ece0c0", spots="#5a4a2a") + P("M-178 -40 l-14 -10 M-178 -34 l-16 2 M-178 -28 l-12 10", sw=2.4), 0, -40), box=(w / 2, h * .7, 480, 220))
ART4["jp-eel"] = lambda w, h: scene("pond", w, h, G_(_eel("#4a5a4a", L=460, H=38, belly="#e6e8d8"), 0, -40), box=(w / 2, h * .7, 540, 220))
def _worm(w, h):
    soil = P("M-280 40 Q0 0 280 40 L280 120 L-280 120 Z", "#6b4f3a", 2.6) + "".join(C(-240 + i * 44, 70 + (i % 3) * 14, 5, "#4a3626", 0) for i in range(12))
    pts = [(-200 + i * 20, -20 - 30 * math.sin(i / 2.5)) for i in range(21)]
    d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    o = P(d, sw=30, col=INK) + P(d, sw=24, col="#c8504a") + "".join(P(f"M{x} {y-10} l0 20", sw=1.6, col="#e9c86a") for x, y in pts[2::2])
    o += E(-40, -38, 18, 15, "#e08a6a", 2.4)
    return scene("meadow", w, h, soil + o, box=(w / 2, h * .7, 560, 260))
ART4["red-wiggler"] = _worm
ART4["holstein"] = Q("farm", None, F="#ffffff", bl=340, bd=150, lh=140, lw=34, pattern="patches", pat_col=INK, neck=(20, 60), nw=90, head=(52, 50),
                     snout=(44, 40), snout_col="#f6c9c0", nose="#c9857a", ears="side", horns=None, tail="tuft", tail_col=INK, hooves=INK, udder="#f6c9c0")

# farm batch 4
ART4["crayfish"] = lambda w, h: scene("wetland", w, h, G_(shrimp(F="#c8322a", L=260, H=64, claw=True) + P("M-110 -20 l-60 -40 l-30 10 M-170 -60 l-40 0", sw=14, col="#a82a22"), 20, -10), box=(w / 2, h * .72, 480, 280))
ART4["giant-prawn"] = lambda w, h: scene("pond", w, h, G_(shrimp(F="#6f8fb0", L=280, H=62, claw=True) + P("M-90 -14 l-80 -10 l-60 -30", sw=8, col="#2f5a9a"), 20, -20), box=(w / 2, h * .7, 500, 280))
ART4["bighead"] = _pond(fish(F="#6f7a72", L=320, H=120, tail="fork", eye_r=7, fin_col="#5a645c", belly="#dfe2da",
                             extras="".join(C(-40 + (i * 41) % 180, -30 + (i * 23) % 50, 9, "#4a544c", 0) for i in range(12)) + P("M-150 -40 C-90 -60 -70 30 -150 40", sw=2.4)))
ART4["black-carp"] = _pond(fish(F="#3a3f45", L=340, H=96, tail="fork", eye_r=7, fin_col="#2a2e33", belly="#7a8088"))
ART4["catfish"] = _pond(fish(F="#8a9096", L=320, H=90, tail="fork", eye_r=6, fin_col="#6a7076", belly="#e6e8ea",
                             extras="".join(C(-40 + (i * 37) % 200, -24 + (i * 13) % 30, 4, INK, 0) for i in range(10)) +
                             "".join(P(f"M-150 {y} q-30 {y/2} -60 {y*1.4}", sw=2.6) for y in (-6, 4, 12))))
ART4["milkfish"] = lambda w, h: scene("sea", w, h, G_(fish(F="#c9d3da", L=340, H=88, tail="fork", eye_r=7, fin_col="#a9b6c0", belly="#f4f6f8"), 0, -50), box=(w / 2, h * .7, 520, 240))
def _snail(w, h):
    body = P("M-200 0 C-200 -30 -120 -40 60 -30 C120 -26 160 -10 170 0 Z", "#b8a48a", 2.8) + P("M-190 -14 l-30 -60 M-170 -18 l-10 -54", sw=4) + C(-220, -76, 6, INK, 0) + C(-180, -74, 6, INK, 0)
    sh = C(0, -100, 90, "#b9874a", 3) + "".join(P(f"M0 -100 m{r} 0 a{r} {r} 0 1 1 {-2*r} 0", sw=8, col="#6b4a2a") for r in (70, 45, 22)) + C(0, -100, 8, "#6b4a2a", 0)
    return scene("meadow", w, h, body + sh, box=(w / 2, h * .74, 460, 300))
ART4["snail"] = _snail
ART4["coypu"] = Q("wetland", (.74, 560, 280), F="#6b4a32", bl=280, bd=110, lh=44, lw=24, belly="#8a6a4a", neck=(20, 40), nw=70, head=(48, 40), snout=(34, 30),
                  snout_col="#e9e2d6", ears="small", tail="long", tail_col="#3a2a22", extras=P("M-238 -88 l0 14 M-232 -88 l0 14", sw=5, col="#f08a2a"))
ART4["merino"] = Q("farm", (.75, 560, 360), F="#c9a88a", bl=290, bd=150, lh=96, lw=24, wool="#f6efe0", neck=(10, 60), nw=74, head=(44, 46), snout=(30, 32),
                   snout_col="#f2e8d6", ears="side", horns="ram", tail="short", tail_col="#f6efe0", nose="#c9a88a")
ART4["border-collie"] = lambda w, h: scene("meadow", w, h, quad(F="#2a2a2e", bl=250, bd=100, lh=100, lw=28, belly="#ffffff", neck=(26, 40), nw=74, head=(54, 46), snout=(48, 32),
                                         snout_col="#ffffff", ears="point", tail="bushy", tail_col="#2a2a2e", front_extras=""), box=(w / 2, h * .76, 560, 380))

# ------------------------------------------------------------------ 高原草原
ART4["leopard"] = lambda w, h: scene("savanna", w, h, branch(-260, 120, 3, 16) if False else quad(F="#e9c27a", bl=290, bd=96, lh=120, lw=26, belly="#fbf2dc", pattern="spots", pat_col=INK,
                                     neck=(26, 40), nw=60, head=(40, 34), snout=(24, 26), snout_col="#fbf2dc", ears="round", tail="long", tail_col="#e9c27a"))
def _meerkat(w, h):
    F = "#c9a87a"
    o = P("M30 0 C80 -10 120 10 150 -10", sw=12, col=INK) + P("M30 0 C80 -10 120 10 150 -10", sw=8, col=F)
    o += E(0, -110, 46, 110, F, 3) + E(4, -100, 28, 80, "#e9d8b8", 0)
    o += P("M-20 -150 q-20 20 -10 40 M20 -150 q20 20 10 40", sw=10, col=INK) + P("M-20 -150 q-20 20 -10 40 M20 -150 q20 20 10 40", sw=6, col=F)
    o += E(0, -240, 34, 30, F, 3) + P("M-6 -250 l-40 14 l40 8 Z", F, 2.6) + C(-46, -236, 5, INK, 0)
    o += E(-12, -250, 9, 7, INK, 0) + C(-14, -252, 2.5, "#ffffff", 0) + C(24, -262, 10, "#5a4a3a", 2.4)
    o += "".join(P(f"M{-30+i*14} -160 l4 14", sw=2, col="#8a6a42") for i in range(5))
    return scene("desert", w, h, P("M-120 10 C-100 -30 -40 -30 -20 10 Z", "#b88a5a", 2.6) + o, box=(w / 2, h * .8, 440, 470))
ART4["meerkat"] = _meerkat
ART4["warthog"] = Q("savanna", (.75, 560, 340), F="#7a6a5e", bl=280, bd=120, lh=80, lw=28, neck=(0, 0), head=(58, 52), snout=(40, 40), snout_col="#6a5a4e", nose=None,
                    ears="point", tail="thin", tail_col="#3a2e25", hooves=INK, pig=True, mane="zebra",
                    extras=P("M-250 -150 q-20 -40 6 -60 M-226 -150 q-6 -36 18 -52", sw=8, col="#f4efe6"))
ART4["af-buffalo"] = Q("savanna", None, F="#3a3533", bl=330, bd=150, lh=110, lw=38, neck=(10, 60), nw=90, head=(50, 46), snout=(42, 38), snout_col="#4a4543",
                       ears="side", horns="bison", tail="tuft", tail_col="#1f1c1a", hooves=INK, nose=None)
ART4["tommy"] = Q("savanna", (.76, 560, 440), F="#d9a868", bl=230, bd=90, lh=140, lw=18, belly="#fbf6ec", neck=(40, 28), nw=46, head=(32, 28), snout=(34, 24),
                  snout_col="#e9c890", ears="side", horns="chiru", tail="short", tail_col=INK, hooves=INK)
ART4["impala"] = Q("savanna", (.76, 560, 440), F="#c9864a", bl=250, bd=96, lh=150, lw=18, belly="#fbf6ec", neck=(44, 28), nw=50, head=(34, 30), snout=(36, 26),
                   snout_col="#e9b07a", ears="side", horns="chiru", tail="short", tail_col="#ffffff", hooves=INK)
ART4["springbok"] = Q("desert", (.76, 560, 440), F="#c98a4a", bl=240, bd=96, lh=146, lw=18, belly="#ffffff", neck=(42, 28), nw=48, head=(34, 30), snout=(34, 26),
                      snout_col="#ffffff", ears="side", horns="goat", tail="short", tail_col="#ffffff", hooves=INK)
ART4["black-rhino"] = Q("savanna", None, F="#8a8580", bl=330, bd=150, lh=95, lw=46, neck=(0, 0), head=(58, 52), snout=(56, 46), ears="point", horns="rhino",
                        tail="tuft", tail_col="#4a4642", headdown=30, nose=None)
ART4["grevy"] = Q("savanna", None, F="#ffffff", bl=290, bd=124, lh=156, lw=26, pattern="stripes", pat_col=INK, neck=(70, 32), nw=66, head=(42, 38), snout=(54, 34),
                  snout_col="#5a4a3e", ears="big", mane="zebra", tail="tuft", tail_col=INK, hooves=INK, belly="#ffffff")
ART4["przewalski"] = Q("plateau", None, F="#c9a06a", bl=270, bd=124, lh=130, lw=28, belly="#efdcb8", neck=(60, 34), nw=70, head=(44, 40), snout=(54, 36),
                       snout_col="#efdcb8", ears="point", mane="zebra", tail="horse", tail_col="#3a2a1e", hooves=INK)
ART4["tib-gazelle"] = Q("plateau", (.76, 560, 440), F="#b8a08a", bl=230, bd=92, lh=130, lw=18, belly="#f4efe6", neck=(40, 28), nw=46, head=(32, 28), snout=(32, 24),
                        snout_col="#c9b49a", ears="side", horns="chiru", tail="short", tail_col="#ffffff", hooves=INK)
ART4["kiang"] = Q("plateau", None, F="#a8683a", bl=270, bd=120, lh=140, lw=26, belly="#f4efe6", neck=(60, 34), nw=66, head=(42, 38), snout=(54, 34),
                  snout_col="#f4efe6", ears="long", mane="zebra", tail="tuft", tail_col="#3a2a1e", hooves=INK)
ART4["tib-fox"] = Q("plateau", (.75, 540, 320), F="#d98a3a", bl=230, bd=86, lh=80, lw=20, belly="#c9c3ba", neck=(30, 40), nw=60, head=(48, 42), snout=(40, 28),
                    snout_col="#f4efe6", ears="small", tail="bushy", tail_col="#c9c3ba")
ART4["pika"] = lambda w, h: scene("plateau", w, h, rodent("#a89078", 200, 150, belly="#e9dccb", ears="round", nose="#5a4a3e"), box=(w / 2, h * .76, 400, 280))
ART4["marmot"] = lambda w, h: scene("plateau", w, h, rodent("#c9a46a", 280, 170, belly="#e9d4a8", ears="small", tail="bushy", tailcol="#8a6a42", tl=.5, nose="#3a2a1e"), box=(w / 2, h * .76, 520, 300))
ART4["argali"] = Q("plateau", None, F="#9a7a5a", bl=280, bd=124, lh=130, lw=26, belly="#f4efe6", neck=(30, 50), nw=74, head=(44, 40), snout=(40, 30),
                   snout_col="#e9dccb", ears="side", horns="ram", tail="short", tail_col="#f4efe6", hooves=INK, neck_wool="#e9dccb")
ART4["bharal"] = Q("plateau", None, F="#8f969c", bl=260, bd=110, lh=120, lw=24, belly="#f4f2ee", neck=(30, 44), nw=64, head=(40, 36), snout=(38, 28),
                   snout_col="#6b7075", ears="side", horns="bison", tail="short", tail_col="#3a3f45", hooves=INK)
ART4["mon-gazelle"] = Q("meadow", (.76, 560, 440), F="#d9b27a", bl=240, bd=96, lh=130, lw=18, belly="#fbf6ec", neck=(40, 30), nw=48, head=(34, 30), snout=(34, 26),
                        snout_col="#e9cf9a", ears="side", horns="chiru", tail="short", tail_col="#fbf6ec", hooves=INK)
ART4["saiga"] = Q("desert", (.76, 560, 400), F="#d9c4a0", bl=240, bd=100, lh=110, lw=18, belly="#fbf6ec", neck=(30, 34), nw=54, head=(40, 34), snout=(46, 40),
                  snout_col="#c9b48e", ears="side", horns="chiru", tail="short", hooves=INK, nose=None)
ART4["pronghorn"] = Q("meadow", (.76, 560, 440), F="#c98a4a", bl=240, bd=100, lh=140, lw=18, belly="#ffffff", neck=(40, 32), nw=50, head=(36, 30), snout=(36, 26),
                      snout_col="#3a2a1e", ears="side", horns="goat", tail="short", tail_col="#ffffff", hooves=INK)
ART4["prairie-dog"] = lambda w, h: scene("meadow", w, h, P("M-200 20 C-170 -30 -90 -30 -60 20 Z", "#b88a5a", 2.6) + rodent("#c9a06a", 210, 150, belly="#efdcb8", ears="small", tail="rope", tl=.3, tailcol="#2a2a2a", nose="#5a4a3a"), box=(w / 2, h * .76, 460, 300))
ART4["coyote"] = Q("desert", None, F="#b99a72", bl=250, bd=96, lh=130, lw=22, belly="#efe4d2", neck=(40, 36), nw=60, head=(40, 34), snout=(50, 26),
                   snout_col="#efe4d2", ears="point", tail="bushy", tail_col="#8a6a4a")
ART4["aardvark"] = Q("savanna", (.75, 560, 320), F="#b8a090", bl=260, bd=120, lh=70, lw=30, neck=(10, 40), nw=70, head=(40, 34), snout=(90, 24), snout_col="#c9b4a4",
                     nose="#a88a7a", ears="long", tail="thin", tail_col="#b8a090", headdown=30)
ART4["serval"] = Q("savanna", None, F="#e6b85a", bl=240, bd=86, lh=150, lw=20, belly="#fbf2dc", pattern="spots", pat_col=INK, neck=(34, 34), nw=52, head=(32, 28),
                   snout=(20, 22), snout_col="#fbf2dc", ears="big", tail="short", tail_col=INK)
ART4["caracal"] = Q("desert", None, F="#c98a52", bl=250, bd=92, lh=130, lw=22, belly="#f4e6d0", neck=(30, 36), nw=54, head=(36, 32), snout=(22, 24), snout_col="#f4e6d0",
                    ears="point", tail="short", tail_col="#c98a52")
ART4["manul"] = Q("plateau", (.75, 520, 320), F="#b9b2a8", bl=230, bd=104, lh=60, lw=24, belly="#e6e0d6", neck=(20, 40), nw=70, head=(50, 42), snout=(24, 24), snout_col="#efe9e0",
                  ears="small", tail="bushy", tail_col="#8a847a", pattern="stripes", pat_col="#6b655c")
ART4["guanaco"] = Q("plateau", (.76, 500, 440), F="#c98a4a", bl=240, bd=110, lh=150, lw=24, belly="#f4efe6", neck=(150, 6), nw=46, head=(34, 32), snout=(32, 24),
                    snout_col="#6b6b6b", ears="big", tail="short", hooves="#5a5048", nose="#5a5048")
ART4["vicuna"] = Q("plateau", (.76, 500, 440), F="#d9a868", bl=220, bd=96, lh=150, lw=20, belly="#ffffff", neck=(140, 6), nw=40, head=(30, 28), snout=(28, 22),
                   snout_col="#d9a868", ears="big", tail="short", hooves="#5a5048", nose="#5a5048")
ART4["gemsbok"] = Q("desert", (.76, 560, 460), F="#b9aa98", bl=280, bd=120, lh=140, lw=26, belly="#ffffff", neck=(40, 36), nw=60, head=(40, 36), snout=(40, 30),
                    snout_col="#ffffff", ears="side", horns="chiru", tail="horse", tail_col=INK, hooves=INK, mask=INK)
ART4["eland"] = Q("savanna", None, F="#c9a07a", bl=320, bd=150, lh=130, lw=30, belly="#e9dccb", pattern="stripes", pat_col="#f4efe6", neck=(30, 50), nw=80, head=(42, 40), snout=(40, 32),
                  snout_col="#8a6a4a", ears="side", horns="chiru", tail="tuft", tail_col=INK, hooves=INK, hump=True)
ART4["honey-badger"] = Q("savanna", (.75, 540, 300), F="#2a2a2e", bl=250, bd=96, lh=56, lw=26, belly="#2a2a2e", neck=(10, 40), nw=70, head=(42, 36), snout=(30, 26), snout_col="#2a2a2e",
                         ears="small", tail="short", tail_col="#2a2a2e", extras=P("M-220 -150 C-100 -190 80 -190 150 -120", sw=40, col="#e9e6df"))
ART4["anteater"] = Q("savanna", (.75, 580, 340), F="#8a7560", bl=280, bd=110, lh=80, lw=26, belly="#5a4a3a", neck=(10, 40), nw=70, head=(30, 26), snout=(120, 16), snout_col="#8a7560",
                     ears="small", tail="bushy", tail_col="#5a4a3a", headdown=40, extras=P("M-160 -160 L60 -110", sw=22, col=INK) + P("M-150 -140 L60 -100", sw=8, col="#f4efe6"))

# ------------------------------------------------------------------ 森林
def bear(kind, F, snout_col, chest=None, **kw):
    k = dict(F=F, bl=320, bd=150, lh=110, lw=44, neck=(10, 50), nw=100, head=(56, 50), snout=(40, 34), snout_col=snout_col, ears="round", tail="short", shoulder=30)
    k.update(kw)
    def f(w, h):
        a = quad(**k)
        if chest: a += P("M-200 -200 q30 30 70 0", sw=18, col=INK) + P("M-200 -200 q30 30 70 0", sw=12, col=chest)
        return scene(kind, w, h, a)
    return f
ART4["moon-bear"] = bear("forest", "#232326", "#b8a48a")
ART4["sun-bear"] = bear("rainforest", "#2a2624", "#d9a860", bl=280, bd=130, lh=90, head=(50, 44), ears="small")
ART4["am-black-bear"] = bear("forest", "#2a2a2e", "#a8865a")
ART4["red-deer"] = Q("forest", (.78, 560, 460), F="#9a5a32", bl=280, bd=116, lh=150, lw=22, belly="#c9a07a", neck=(60, 34), nw=60, head=(40, 34), snout=(44, 28),
                     ears="side", horns="antler", tail="short", tail_col="#e9dcc4", hooves="#3a3f45", neck_wool="#7a4a2a")
ART4["moose"] = Q("forest", (.78, 580, 460), F="#4a3a2e", bl=320, bd=140, lh=170, lw=26, belly="#3a2e25", neck=(30, 50), nw=80, head=(50, 40), snout=(70, 44), snout_col="#5a4a3e",
                  ears="side", horns="antler", tail="short", hooves="#2a2a2a", shoulder=36, beard="#3a2e25")
ART4["roe-deer"] = Q("forest", (.78, 540, 440), F="#b8743e", bl=230, bd=96, lh=130, lw=18, belly="#e9cfa8", neck=(50, 30), nw=46, head=(34, 28), snout=(34, 24),
                     snout_col="#3a2a1e", ears="side", horns="antler", tail="short", tail_col="#ffffff", hooves="#3a3f45")
ART4["wild-boar"] = Q("forest", (.75, 560, 340), F="#5a4a3e", bl=290, bd=130, lh=80, lw=30, neck=(0, 0), head=(62, 52), snout=(44, 36), snout_col="#4a3a2e", nose=None,
                      ears="point", tail="thin", tail_col="#3a2e25", hooves=INK, pig=True, mane="zebra", extras=P("M-262 -110 q-14 -20 0 -34", sw=6, col="#f4efe6"))
ART4["lynx"] = Q("snow", None, F="#c9a07a", bl=250, bd=96, lh=140, lw=26, belly="#efe4d2", pattern="spots", pat_col="#6b5038", neck=(30, 36), nw=60, head=(40, 34), snout=(22, 24),
                 snout_col="#efe4d2", ears="point", tail="short", tail_col=INK)
ART4["clouded-leopard"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 18) + G_(quad(F="#c9b08a", bl=260, bd=84, lh=70, lw=22, belly="#efe4d2", pattern="patches", pat_col="#5a4a3a",
                                             neck=(20, 36), nw=56, head=(36, 32), snout=(24, 24), snout_col="#efe4d2", ears="round", tail="long", tail_col="#c9b08a"), 0, -10), box=(w / 2, h * .66, 580, 320))
def _lemur(w, h):
    tail = "".join(P(f"M60 -{40+i*0}", sw=0) for i in range(0))
    pts = [(70 + 20 * math.sin(i / 3) , -60 - i * 24) for i in range(14)]
    d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    t = P(d, sw=34, col=INK) + P(d, sw=28, col="#ffffff") + "".join(P(f"M{x-14:.0f} {y:.0f} L{x+14:.0f} {y:.0f}", sw=12, col=INK) for x, y in pts[::2])
    return scene("forest", w, h, t + ape(F="#a9a5a0", face="#ffffff", H=260, ear_col="#a9a5a0", brow=False, snub=False), box=(w / 2, h * .76, 440, 440))
ART4["lemur"] = _lemur
ART4["rhesus"] = lambda w, h: scene("forest", w, h, ape(F="#a8865a", face="#e8a8a0", H=280, ear_col="#e8a8a0", brow=False), box=(w / 2, h * .76, 420, 400))
ART4["jp-macaque"] = lambda w, h: scene("snow", w, h, ape(F="#b9aa98", face="#e2483c", H=290, ear_col="#e88a80", brow=False, hair="#b9aa98"), box=(w / 2, h * .76, 430, 400))
ART4["gibbon"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 14) + ape(F="#2a2622", face="#5a4a3a", H=260, arms=1.6, ear_col="#2a2622", brow=False, hair="#e9e2d6"), box=(w / 2, h * .76, 480, 420))
ART4["mandrill"] = lambda w, h: scene("rainforest", w, h, ape(F="#6b6a3a", face="#3a5ab8", H=300, ear_col="#6b6a3a", brow=True, cheekpads=True) +
                                      P("M-14 -300 l0 70", sw=14, col="#e2483c"), box=(w / 2, h * .76, 440, 400))
ART4["bonobo"] = lambda w, h: scene("rainforest", w, h, ape(F="#2a2622", face="#3a3530", H=320, arms=1.2, ear_col="#2a2622", hair="#2a2622"), box=(w / 2, h * .76, 440, 400))
ART4["okapi"] = Q("rainforest", (.8, 540, 460), F="#5a3a2a", bl=260, bd=110, lh=150, lw=22, neck=(110, 30), nw=56, head=(36, 30), snout=(40, 26), snout_col="#e9dcc4",
                  ears="big", horns="ossicone", tail="tuft", hooves="#3a2a1e", extras="".join(P(f"M{110+i*14} -170 l0 60", sw=7, col="#ffffff") for i in range(4)) + "".join(P(f"M{-110+i*14} -100 l0 60", sw=7, col="#ffffff") for i in range(3)))
ART4["tapir"] = Q("rainforest", (.75, 580, 340), F="#2a2a2e", bl=300, bd=140, lh=90, lw=34, neck=(0, 20), nw=80, head=(52, 44), snout=(56, 26), snout_col="#2a2a2e",
                  ears="round", tail="short", tail_col="#2a2a2e", hooves=INK, nose=None, headdown=30, extras=P("M-40 -230 L120 -230 L130 -110 L-40 -110 Z", "#f4f2ee", 0))
ART4["capybara"] = Q("wetland", (.75, 560, 320), F="#a8784a", bl=290, bd=140, lh=70, lw=32, neck=(10, 40), nw=90, head=(64, 54), snout=(50, 46), snout_col="#8a603a", nose="#3a2a1e",
                     ears="small", tail="short", tail_col="#a8784a")
def _armadillo(w, h):
    o = E(0, -90, 160, 80, "#b9a08a", 3) + "".join(P(f"M{x} -165 C{x-4} -120 {x-4} -60 {x} -14", sw=3) for x in range(-60, 70, 15))
    o += P("M-150 -70 C-210 -80 -230 -50 -250 -40 C-220 -30 -170 -30 -140 -40 Z", "#c9b09a", 2.8) + C(-190, -60, 5, INK, 0) + P("M-170 -110 l-8 -30 l18 20", "#c9b09a", 2.4)
    o += P("M150 -80 C210 -70 260 -40 280 -10", sw=18, col=INK) + P("M150 -80 C210 -70 260 -40 280 -10", sw=12, col="#b9a08a")
    o += "".join(P(f"M{x} -20 l0 30", sw=14, col=INK) + P(f"M{x} -20 l0 30", sw=9, col="#c9b09a") for x in (-90, -40, 50, 100))
    return scene("forest", w, h, o, box=(w / 2, h * .76, 540, 280))
ART4["armadillo"] = _armadillo
def _pangolin(w, h):
    o = E(0, -90, 160, 76, "#8a7a6a", 3) + "".join(P(f"M{x-20+(r%2)*10} {-150+r*24} q14 -12 28 0", sw=2.6, col="#5a4a3a") for r in range(5) for x in range(-120, 140, 30))
    o += P("M-150 -80 C-210 -80 -240 -60 -260 -50 C-230 -40 -170 -40 -140 -50 Z", "#c9b4a0", 2.8) + C(-200, -66, 4, INK, 0)
    o += P("M150 -70 C230 -60 280 0 230 30", sw=40, col=INK) + P("M150 -70 C230 -60 280 0 230 30", sw=34, col="#8a7a6a")
    o += "".join(P(f"M{x} -20 l0 30", sw=14, col=INK) + P(f"M{x} -20 l0 30", sw=9, col="#c9b4a0") for x in (-90, -40, 50, 100))
    return scene("forest", w, h, o, box=(w / 2, h * .76, 540, 290))
ART4["pangolin"] = _pangolin
ART4["badger"] = Q("forest", (.75, 540, 300), F="#9a9a9a", bl=260, bd=100, lh=50, lw=26, belly="#3a3a3a", neck=(10, 40), nw=70, head=(46, 36), snout=(36, 22), snout_col="#f4f4f4",
                   ears="small", tail="short", tail_col="#9a9a9a", farleg="#2a2a2a", extras=P("M-258 -128 L-170 -128", sw=10, col=INK))
def _euhedge(w, h):
    o = E(0, -70, 130, 70, "#8a6a4a", 3) + "".join(P(f"M{-110+i*14} {-70-((i*37)%40)} l{6+(i%3)*4} -26", sw=4, col="#f2e6d2" if i % 2 else "#5a4030") for i in range(18))
    o += P("M-110 -40 C-160 -40 -190 -20 -200 -6 C-170 0 -130 0 -100 -10 Z", "#c9a88a", 2.6) + C(-196, -8, 6, INK, 0) + C(-150, -34, 5, INK, 0)
    return scene("meadow", w, h, o, box=(w / 2, h * .76, 420, 240))
ART4["eu-hedgehog"] = _euhedge
ART4["chipmunk"] = lambda w, h: scene("forest", w, h, rodent("#c98a4a", 200, 120, belly="#f4e6d0", ears="round", stripe="#3a2a1e", tail="bushy", tailcol="#a8743e", tl=.8, cheeks=True), box=(w / 2, h * .74, 440, 260))
ART4["beaver"] = lambda w, h: scene("pond", w, h, rodent("#7a5034", 280, 160, belly="#9a6a44", ears="small", nose="#2a1e18") +
                                    E(200, -10, 70, 22, "#4a3a30", 2.8) + "".join(P(f"M{150+i*20} -24 l0 28", sw=1.6, col="#7a6a5a") for i in range(5)) +
                                    P("M-40 40 l200 -10 M-20 60 l220 -6", sw=12, col="#8a6a42"), box=(w / 2, h * .72, 540, 280))
ART4["otter"] = Q("wetland", (.74, 600, 260), F="#6b4a32", bl=300, bd=76, lh=44, lw=22, belly="#c9a88a", neck=(30, 56), nw=58, head=(40, 32), snout=(32, 24), snout_col="#c9a88a",
                  ears="round", tail="long", tail_col="#6b4a32")
ART4["wolverine"] = Q("snow", (.75, 540, 300), F="#4a3628", bl=250, bd=100, lh=60, lw=28, belly="#3a2a1e", neck=(10, 40), nw=70, head=(44, 36), snout=(30, 24), snout_col="#6b5040",
                      ears="small", tail="bushy", tail_col="#3a2a1e", extras=P("M-120 -150 C-40 -130 40 -130 130 -150", sw=14, col="#c9a06a"))
ART4["sable"] = Q("snow", (.74, 580, 260), F="#5a3a26", bl=280, bd=72, lh=46, lw=20, belly="#5a3a26", neck=(30, 50), nw=52, head=(36, 30), snout=(30, 20), snout_col="#7a5a42",
                  ears="round", tail="bushy", tail_col="#4a2e1e", extras=C(-190, -112, 10, "#e9c27a", 0))
ART4["civet"] = Q("forest", (.75, 580, 280), F="#8a7a6a", bl=270, bd=80, lh=56, lw=20, neck=(20, 46), nw=54, head=(38, 30), snout=(34, 22), snout_col="#2a2a2a",
                  ears="round", tail="long", tail_col="#2a2a2a", mask="#ffffff")
def _loris(w, h):
    b = branch(-260, 260, 4, 18)
    o = E(0, -80, 80, 56, "#c9a07a", 3) + C(-80, -110, 44, "#c9a07a", 3) + E(-96, -116, 14, 16, "#5a3a26", 0) + E(-62, -116, 14, 16, "#5a3a26", 0)
    o += C(-96, -116, 8, INK, 0) + C(-62, -116, 8, INK, 0) + C(-93, -119, 2.5, "#ffffff", 0) + C(-59, -119, 2.5, "#ffffff", 0) + P("M-80 -150 l0 30", sw=6, col="#f4efe6")
    o += "".join(P(f"M{x} -40 l{d} 40", sw=16, col=INK) + P(f"M{x} -40 l{d} 40", sw=11, col="#c9a07a") for x, d in ((-50, -20), (-10, 10), (40, -10), (70, 20)))
    o += P("M10 -136 C40 -150 70 -140 80 -110", sw=10, col="#8a5a3a")
    return scene("rainforest", w, h, b + G_(o, 0, -6), box=(w / 2, h * .66, 460, 300))
ART4["slow-loris"] = _loris
def _tarsier(w, h):
    b = P("M-20 60 L-20 -300", sw=24, col=INK) + P("M-20 60 L-20 -300", sw=18, col="#8a6a42")
    o = E(30, -120, 40, 60, "#a8865a", 3) + C(30, -200, 46, "#a8865a", 3) + "".join(C(x, -205, 20, "#f6d36a", 2.6) + C(x, -205, 10, INK, 0) for x in (10, 52))
    o += E(-6, -240, 14, 22, "#c9a07a", 2.4) + E(68, -240, 14, 22, "#c9a07a", 2.4) + P("M40 -60 C70 40 90 60 60 120", sw=6, col="#8a6a42")
    o += P("M0 -140 l-24 -10 M0 -100 l-24 6 M10 -64 l-28 4", sw=8, col="#a8865a")
    return scene("rainforest", w, h, b + o, box=(w / 2, h * .76, 320, 440))
ART4["tarsier"] = _tarsier
ART4["proboscis"] = lambda w, h: scene("rainforest", w, h, ape(F="#c97a42", face="#e9b88a", H=300, ear_col="#e9b88a", brow=False, hair="#c97a42") +
                                       P("M-14 -330 C-40 -300 -40 -270 -10 -262 C14 -270 14 -300 -14 -330 Z", "#e88a6a", 2.6), box=(w / 2, h * .76, 440, 400))
ART4["takin"] = Q("forest", None, F="#d9b25a", bl=290, bd=140, lh=100, lw=34, neck=(10, 50), nw=90, head=(56, 50), snout=(50, 44), snout_col="#5a4a3a", nose=None,
                  ears="side", horns="wildebeest", tail="short", tail_col="#d9b25a", hooves=INK, shoulder=30)
ART4["muntjac"] = Q("forest", (.78, 520, 400), F="#b8743e", bl=220, bd=90, lh=100, lw=16, belly="#e9cfa8", neck=(40, 28), nw=44, head=(34, 28), snout=(32, 22),
                    snout_col="#3a2a1e", ears="side", horns="antler", tail="short", tail_col="#ffffff", hooves="#3a3f45")
ART4["wt-deer"] = Q("forest", (.78, 560, 440), F="#b07a4a", bl=260, bd=104, lh=150, lw=20, belly="#ffffff", neck=(60, 30), nw=52, head=(36, 30), snout=(40, 26),
                    snout_col="#ffffff", ears="side", horns="antler", tail="tuft", tail_col="#ffffff", hooves="#3a3f45")
def _ffox(w, h):
    b = P("M-260 -280 L260 -280", sw=14, col=INK) + P("M-260 -280 L260 -280", sw=9, col="#8a6a42")
    o = P("M0 -270 C-120 -240 -160 -120 -100 -20 C-60 -80 -30 -80 0 -40 C30 -80 60 -80 100 -20 C160 -120 120 -240 0 -270 Z", "#3a3533", 3)
    o += E(0, -150, 34, 80, "#5a4a3a", 3) + C(0, -60, 30, "#c9884a", 3) + P("M-10 -40 l10 28 l10 -28", "#c9884a", 2.4) + C(-10, -56, 4, INK, 0) + C(10, -56, 4, INK, 0)
    o += P("M-20 -84 l-6 -16 l14 8 M20 -84 l6 -16 l-14 8", "#3a3533", 2.4)
    return scene("forest", w, h, b + o, box=(w / 2, h * .66, 360, 360))
ART4["flying-fox"] = _ffox
# ---------------- ocean (phase 3)
def _ceta(F, L, H, belly=None, dorsal=True, tall=False, extras="", fin=None, kind="sea", box=None, pre="", post=""):
    f = pre + fish(F=F, L=L, H=H, tail="fluke", belly=belly, cetacean=True, eye_r=5, mouth=False, fin_col=fin or darker(F), dorsal=dorsal, tall_dorsal=tall, extras=extras) + post
    return lambda w, h: scene(kind, w, h, f, box=box or (w / 2, h * .58, 640, 300))
_hb_fin = P("M-120 30 C-90 110 -40 170 10 190 C-10 140 -50 80 -80 30 Z", "#3d4a58", 2.6) + "".join(C(-200 + i * 22, -30 - (i % 2) * 8, 4, "#9aa7b4", 0) for i in range(4))
ART4["humpback"] = _ceta("#3d4a58", 520, 130, belly="#dfe5eb", extras=_hb_fin + "".join(P(f"M{-250+i*16} {20+i} L{-120+i*10} {30+i}", sw=1.6, col="#9aa7b4") for i in range(4)), box=None)
_sp_head = P("M-280 -40 C-300 -60 -300 40 -270 50 L-150 50 L-150 -60 Z", "#5a5a60", 2.8)
ART4["sperm-whale"] = _ceta("#5a5a60", 520, 140, dorsal=False, pre="", post=P("M-270 -60 C-290 -50 -292 30 -270 54", sw=3) + P("M-250 48 l120 -4", sw=3) + "".join(P(f"M{-60+i*40} -66 l14 -8 l14 8", sw=2.4) for i in range(4)), extras=P("M-260 -60 L-60 -66", sw=0))
ART4["beluga"] = _ceta("#f4f6f8", 380, 130, belly="#ffffff", dorsal=False, kind="ice" , box=None,
                       post=P("M-196 -20 C-200 -60 -160 -80 -130 -64", "#f4f6f8", 2.6), fin="#e4e8ec")
ART4["narwhal"] = _ceta("#8a96a2", 400, 120, belly="#e6ebf0", dorsal=False, kind="ice",
                        extras="".join(C(-120 + (i * 37) % 280, -40 + (i * 23) % 50, 6, "#4a5560", 0) for i in range(16)),
                        post=P("M-200 -6 L-420 -40", sw=10, col=INK) + P("M-200 -6 L-420 -40", sw=6, col="#f4ecd8") + "".join(P(f"M{-240-i*30} {-12-i*4.6:.0f} l6 -8", sw=1.6) for i in range(6)),
                        box=(480, 0, 0, 0))
ART4["narwhal"] = (lambda base: (lambda w, h: scene("ice", w, h, fish(F="#8a96a2", L=360, H=110, tail="fluke", belly="#e6ebf0", cetacean=True, eye_r=5, mouth=False, dorsal=False,
                   extras="".join(C(-100 + (i * 37) % 250, -36 + (i * 23) % 46, 6, "#4a5560", 0) for i in range(16))) + P("M-180 -6 L-380 -40", sw=10, col=INK) + P("M-180 -6 L-380 -40", sw=6, col="#f4ecd8"),
                   box=(w / 2, h * .62, 640, 280))))(None)
ART4["cn-white-dolphin"] = (lambda w, h: scene("sea", w, h, P("M-200 -12 C-230 -10 -244 2 -240 10 C-220 12 -200 14 -194 12 Z", "#f2b8b8", 2.8) +
                            fish(F="#f2c4c4", L=380, H=110, tail="fluke", belly="#fbe4e4", cetacean=True, eye_r=6, mouth=False, fin_col="#e8a8a8") + P("M-214 -60 q30 -40 70 -10", sw=0), box=(w / 2, h * .58, 600, 300)))
ART4["finless"] = _ceta("#8a96a2", 320, 110, belly="#c9d2db", dorsal=False, box=None, post=P("M20 -54 L160 -40", sw=2, col="#5a6570"))
def _walrus(w, h):
    a = pinniped("#b98a6a", L=320, up=1.0)
    hx, hy = -320 / 2 - 10, -90 - 120
    a += P(f"M{hx-44} {hy+20} L{hx-50} {hy+110}", sw=12, col=INK) + P(f"M{hx-44} {hy+20} L{hx-50} {hy+110}", sw=7, col="#f6eedc")
    a += P(f"M{hx-24} {hy+22} L{hx-24} {hy+112}", sw=12, col=INK) + P(f"M{hx-24} {hy+22} L{hx-24} {hy+112}", sw=7, col="#f6eedc")
    a += "".join(C(hx - 60 + i * 9, hy + 14 + (i % 2) * 6, 2, INK, 0) for i in range(6))
    return scene("ice", w, h, a, box=(w / 2, h * .7, 560, 360))
ART4["walrus"] = _walrus
ART4["leopard-seal"] = lambda w, h: scene("ice", w, h, pinniped("#7d8792", L=360, up=0.0, spots="#3a424a", belly="#c9d0d8"), box=(w / 2, h * .72, 600, 260))
ART4["harbor-seal"] = lambda w, h: coast(w, h, pinniped("#9aa0a6", L=280, up=0.3, spots="#5a636d"), (w / 2, h * .66, 520, 300))
def _sirenian(F, tail):
    o = P("M-200 -30 C-200 -110 160 -120 200 -40 C210 -20 200 0 180 6 C80 20 -120 20 -190 0 Z", F, 3)
    if tail == "fluke":
        o += P("M190 -30 L280 -80 Q250 -20 280 30 Z", F, 2.8)
    else:
        o += E(250, -20, 70, 50, F, 2.8)
    o += P("M-180 -20 C-240 -20 -250 20 -230 40 C-200 40 -180 20 -170 6 Z", darker(F, .9), 2.8)
    o += P("M-100 0 C-110 50 -80 70 -60 60 C-70 40 -70 20 -60 6 Z", darker(F, .9), 2.6) + C(-150, -40, 4, INK, 0)
    o += "".join(C(-236 + (i % 3) * 8, 10 + (i // 3) * 8, 1.6, INK, 0) for i in range(6))
    grass = "".join(P(f"M{x} 90 C{x-10} 50 {x+10} 20 {x} -10", sw=8, col=INK) + P(f"M{x} 90 C{x-10} 50 {x+10} 20 {x} -10", sw=4, col=SAGE_L) for x in (-260, -220, 120, 160, 210))
    return G_(o, 0, -40) + grass
ART4["dugong"] = lambda w, h: scene("sea", w, h, _sirenian("#a89a8c", "fluke"), box=(w / 2, h * .7, 620, 300))
ART4["manatee"] = lambda w, h: scene("sea", w, h, _sirenian("#8a8a84", "paddle"), box=(w / 2, h * .7, 620, 300))
ART4["hawksbill"] = lambda w, h: scene("sea", w, h, turtle(shell="#8a5a2a", skin="#d9b88a", sea=True, scute="#e0a050", plastron="#f3e3a6"), box=(w / 2, h * .56, 520, 280))
ART4["loggerhead"] = lambda w, h: scene("sea", w, h, turtle(shell="#a8643a", skin="#d9a070", sea=True, scute="#c98050", plastron="#f3e3a6", neck=60), box=(w / 2, h * .56, 520, 280))
ART4["leatherback"] = lambda w, h: scene("deep", w, h, turtle(shell="#3a3f45", skin="#5a6068", L=360, sea=True, scute="#3a3f45", plastron="#c9ccd0") +
                                         "".join(P(f"M{-120+i*60} -100 L{-110+i*60} -30", sw=2.4, col="#9aa0a6") for i in range(5)) + "".join(C(-120 + (i * 41) % 240, -70 + (i * 13) % 40, 3, "#ffffff", 0) for i in range(10)), box=(w / 2, h * .62, 560, 280))
# ocean batch 2
def _sea(f, box=(.58, 620, 300), kind="sea"):
    return lambda w, h: scene(kind, w, h, f, box=(w / 2, h * box[0], box[1], box[2]))
_hh = P("M-210 -30 L-250 -60 L-250 -66 L-226 -70 L-200 -40 Z M-210 20 L-250 50 L-250 56 L-226 60 L-200 30 Z", "#8f9aa6", 2.6)
def _hammer(w, h):
    f = fish(F="#8f9aa6", L=420, H=110, tail="shark", belly="#eef0f2", gills=5, eye_r=0.1, mouth=False, fin_col="#7d8894", tall_dorsal=True)
    head = P("M-200 -30 C-216 -34 -230 -40 -236 -40 L-236 40 C-230 40 -216 34 -200 30 Z", "#8f9aa6", 0) + P("M-236 -64 C-226 -60 -214 -40 -206 -20 L-206 20 C-214 40 -226 60 -236 64 C-246 60 -248 50 -244 40 C-240 20 -240 -20 -244 -40 C-248 -50 -246 -60 -236 -64 Z", "#8f9aa6", 2.8)
    head += C(-238, -56, 4, INK, 0) + C(-238, 56, 4, INK, 0)
    return scene("sea", w, h, G_(f + head, 0, 0), box=(w / 2, h * .58, 620, 300))
ART4["hammerhead"] = _hammer
ART4["tiger-shark"] = _sea(fish(F="#7d8a8f", L=440, H=130, tail="shark", belly="#eef0f0", gills=5, eye_r=6, mouth=False, fin_col="#6a777c",
                               extras="".join(P(f"M{-80+i*34} -60 l-10 50", sw=8, col="#4a5458") for i in range(7))) + P("M-200 14 q30 10 64 0", "#5a2a2a", 2.4))
ART4["bluefin"] = _sea(fish(F="#24456b", L=420, H=140, tail="fork", belly="#e2e8ee", eye_r=8, mouth=True, fin_col="#e8c23a", dorsal_col="#24456b",
                           extras="".join(poly([(60 + i * 18, -40), (68 + i * 18, -50), (76 + i * 18, -40)], "#e8c23a", 1.4) for i in range(5))))
ART4["swordfish"] = _sea(P("M-200 -10 L-380 -2 L-200 8 Z", "#5a6a7a", 2.6) + fish(F="#5a6a7a", L=400, H=110, tail="fork", belly="#d9dfe5", eye_r=9, mouth=False, fin_col="#4a5a6a", tall_dorsal=True, pectoral=True), box=(.58, 660, 280))
def _sunfish(w, h):
    o = E(0, -60, 170, 150, "#b9c3cc", 3) + P("M-20 -200 L30 -360 L80 -190 Z", "#9aa6b0", 2.8) + P("M-20 80 L30 240 L80 70 Z", "#9aa6b0", 2.8)
    o += P("M160 -150 C200 -100 200 -20 160 30", "#9aa6b0", 2.8) + C(-110, -100, 12, "#fff", 2.4) + C(-112, -100, 6, INK, 0) + E(-160, -50, 10, 8, "none", 2.4) + E(-30, -60, 26, 14, "#9aa6b0", 2.4)
    return scene("sea", w, h, o, box=(w / 2, h * .8, 420, 440))
ART4["sunfish"] = _sunfish
ART4["cod"] = _sea(fish(F="#a89a6a", L=360, H=110, tail="fan" if False else "fork", belly="#efeadc", eye_r=8, fin_col="#8a7e56", spots="#7a6e48",
                       extras=P("M-170 30 l-6 20", sw=3) + P("M-160 -10 C-60 -14 60 -14 160 -8", sw=2.4, col="#efeadc")))
ART4["moray"] = lambda w, h: scene("sea", w, h, rock(-180, 60, 1.4) + G_(_eel("#8a7a4a", L=440, H=44, spots="#3a3020"), 40, -50) + P("M-170 -64 l18 6 l-4 6", "#fff", 1.6), box=(w / 2, h * .72, 560, 280))
def _lionfish(w, h):
    f = fish(F="#f3e6d8", L=220, H=110, tail="round", eye_r=8, stripes=("#b8402a", [.15, .3, .45, .6, .75, .9]), fin_col="#e8c8b0", dorsal=False)
    sp = "".join(P(f"M{-60+i*16} -40 L{-80+i*20} {-150-(i%3)*20}", sw=4, col="#b8402a") for i in range(10))
    pf = "".join(P(f"M-30 20 L{-140+i*30} {120+(i%2)*20}", sw=3, col="#d98a6a") for i in range(6))
    return scene("sea", w, h, sp + pf + f, box=(w / 2, h * .62, 460, 360))
ART4["lionfish"] = _lionfish
def _cuttle(w, h):
    o = E(40, -90, 150, 64, "#c9a07a", 3) + P("M-100 -150 C-60 -170 160 -170 190 -90 C160 -10 -60 -10 -100 -30", sw=10, col="#e8d4b8")
    o += "".join(P(f"M{-60+i*40} -110 q10 -14 20 0", sw=3, col="#7a5a3a") for i in range(6))
    o += C(-90, -100, 26, "#c9a07a", 2.8) + E(-94, -104, 10, 6, INK, 0, extra='transform="rotate(0)"') + P("M-104 -104 q10 6 20 0", sw=2.4, col="#f6e6c0")
    o += "".join(P(f"M-110 {-110+i*10} C-160 {-120+i*14} -190 {-90+i*16} -220 {-100+i*20}", sw=8, col=INK) + P(f"M-110 {-110+i*10} C-160 {-120+i*14} -190 {-90+i*16} -220 {-100+i*20}", sw=4, col="#c9a07a") for i in range(4))
    return scene("sea", w, h, o, box=(w / 2, h * .66, 560, 280))
ART4["cuttlefish"] = _cuttle
def _gsquid(w, h):
    o = P("M140 -100 L300 -130 L320 -100 L300 -70 Z", "#b8483a", 2.8) + E(80, -100, 120, 44, "#c8584a", 3) + C(-30, -100, 18, "#fff", 2.4) + C(-32, -100, 10, INK, 0)
    o += "".join(P(f"M-40 {-110+i*8} C-140 {-140+i*20} -220 {-60+i*10} -300 {-120+i*30}", sw=9, col=INK) + P(f"M-40 {-110+i*8} C-140 {-140+i*20} -220 {-60+i*10} -300 {-120+i*30}", sw=5, col="#c8584a") for i in range(5))
    return scene("deep", w, h, o, box=(w / 2, h * .62, 640, 280))
ART4["giant-squid"] = _gsquid
def _mantis(w, h):
    s = shrimp(F="#3aa86a", L=280, H=64, strip=None)
    s += P("M-120 -40 l-50 -40 l-20 30", sw=12, col=INK) + P("M-120 -40 l-50 -40 l-20 30", sw=8, col="#e84a6a")
    s += C(-130, -90, 9, "#3a8ae0", 2.4) + C(-112, -96, 9, "#3a8ae0", 2.4) + P("M100 -60 l40 -20 l10 30 Z", "#e88a3a", 2.4)
    return scene("sea", w, h, G_(s, 20, -20), box=(w / 2, h * .7, 500, 280))
ART4["mantis-shrimp"] = _mantis
ART4["lobster"] = lambda w, h: scene("sea", w, h, G_(shrimp(F="#3a5a4a", L=300, H=70, claw=True) +
                                     P("M-100 -20 l-60 -50 M-100 -10 l-70 20", sw=10, col="#2a4a3a") + E(-180, -84, 40, 22, "#3a5a4a", 2.6) + E(-190, 22, 40, 22, "#3a5a4a", 2.6), 20, -20), box=(w / 2, h * .7, 520, 300))
def _spidercrab(w, h):
    F = "#d9824a"
    o = ""
    for s in (-1, 1):
        for i in range(4):
            d = f"M{s*40} {-40+i*8} L{s*(160+i*30)} {-150+i*30} L{s*(240+i*20)} {40}"
            o += P(d, sw=10, col=INK) + P(d, sw=6, col=F)
        d = f"M{s*30} -70 L{s*140} -200 L{s*200} -160"
        o += P(d, sw=10, col=INK) + P(d, sw=6, col=F)
    o += E(0, -50, 60, 50, F, 3) + "".join(C(-30 + (i * 23) % 60, -70 + (i * 17) % 40, 4, "#f2b88a", 0) for i in range(8)) + C(-14, -98, 5, INK, 0) + C(14, -98, 5, INK, 0)
    return scene("deep", w, h, o, box=(w / 2, h * .76, 600, 320))
ART4["spider-crab"] = _spidercrab
def _horseshoe(w, h):
    o = P("M-160 0 C-160 -120 160 -120 160 0 Z", "#8a6a42", 3) + P("M60 -20 L200 -60 L210 -50 L80 0 Z", "#6a5032", 2.6) + P("M120 -10 L300 10", sw=8, col=INK) + P("M120 -10 L300 10", sw=4, col="#6a5032")
    o += P("M-110 -50 C-60 -80 60 -80 110 -50", sw=2.4, col="#5a4428") + C(-60, -60, 5, INK, 0) + C(60, -60, 5, INK, 0)
    return scene("sea", w, h, G_(o, -40, 0), box=(w / 2, h * .76, 560, 220))
ART4["horseshoe-crab"] = _horseshoe
def _urchin(w, h):
    o = "".join(P(f"M0 -90 L{math.cos(a)*150:.0f} {-90+math.sin(a)*120:.0f}", sw=5, col="#5a2a7a") for a in [i * math.pi / 16 for i in range(-16, 1)])
    o += E(0, -80, 90, 70, "#7a3a9a", 3)
    return scene("sea", w, h, rock(0, 40, 1.6) + o, box=(w / 2, h * .74, 420, 300))
ART4["sea-urchin"] = _urchin
def _cucumber(w, h):
    o = P("M-200 -20 C-200 -90 180 -100 200 -30 C210 0 180 10 150 10 C40 16 -140 16 -190 0 Z", "#5a6a3a", 3)
    o += "".join(poly([(-160 + i * 34, -50 - (i % 2) * 14), (-152 + i * 34, -80 - (i % 2) * 14), (-144 + i * 34, -50 - (i % 2) * 14)], "#7a8a4a", 2) for i in range(10))
    o += "".join(P(f"M-200 -20 l-30 {-20+i*12}", sw=4, col="#e8d4a0") for i in range(4))
    return scene("sea", w, h, o, box=(w / 2, h * .76, 520, 220))
ART4["sea-cucumber"] = _cucumber
def _clam(w, h):
    o = P("M-200 0 C-200 -140 200 -140 200 0 Z", "#d9d4c4", 3) + P("M-170 -20 C-120 -110 120 -110 170 -20 C100 -40 -100 -40 -170 -20 Z", "#3a8aa8", 2.6)
    o += "".join(P(f"M{-180+i*40} 0 l{(i-4.5)*6:.0f} -110", sw=2.4, col="#a8a090") for i in range(10)) + "".join(C(-120 + i * 30, -50 - (i % 2) * 8, 4, "#9ad0e0", 0) for i in range(9))
    return scene("sea", w, h, o, box=(w / 2, h * .78, 480, 240))
ART4["giant-clam"] = _clam
def _mow(w, h):
    o = P("M-160 -20 C-170 -100 120 -140 170 -60 C180 -30 140 -10 100 -10 Z", "#b8a0e8", 3, extra='fill-opacity=".9"') + P("M-100 -80 C-40 -150 60 -150 120 -90", "#e8a0c8", 2.4)
    o += "".join(P(f"M{-120+i*24} -14 C{-130+i*24} 60 {-110+i*24} 140 {-126+i*24} {220+(i%3)*20}", sw=4, col="#5a6ad8") for i in range(10))
    return scene("sea", w, h, o, box=(w / 2, h * .9, 420, 420))
ART4["man-o-war"] = _mow
def _nautilus(w, h):
    sh = C(0, -100, 120, "#f6efe2", 3) + "".join(P(f"M{-120+i*30} {-200+i*6} q30 60 0 {120-i*12}", sw=10, col="#b8643a") for i in range(5)) + C(30, -100, 50, "#f6efe2", 2.6) + P("M30 -100 m40 0 a40 40 0 1 1 -80 0", sw=2.4, col=MUTE)
    sh += "".join(P(f"M-110 {-90+i*8} C-150 {-80+i*12} -180 {-60+i*14} -200 {-70+i*18}", sw=3, col="#c9a07a") for i in range(8)) + C(-100, -120, 8, INK, 0)
    return scene("deep", w, h, sh, box=(w / 2, h * .68, 420, 320))
ART4["nautilus"] = _nautilus
ART4["blue-tang"] = _sea(fish(F="#2a5ac8", L=240, H=150, tail="fork", tail_col="#f2c83a", eye_r=9, fin_col="#1a2a5a", dorsal_col="#1a2a5a",
                             extras=P("M-60 -40 C0 -70 60 -50 80 -20 C40 -30 0 -10 -30 10 C-50 0 -60 -20 -60 -40 Z", "#1a2a5a", 0)), box=(.62, 460, 320))
# ---------------- birds (phase 3)
def B(kind, box=(.78, 480, 400), pre="", post="", front_fn=None, extra_fn=None, **kw):
    def f(w, h):
        k = dict(kw)
        hx, hy = headparts(k)
        if front_fn: k["front"] = k.get("front", "") + front_fn(hx, hy, k.get("hr", 34))
        b = bird(**k)
        if extra_fn: b = extra_fn(hx, hy, k.get("hr", 34)) + b
        return scene(kind, w, h, pre + b + post, box=(w / 2, h * box[0], box[1], box[2]))
    return f
def BP(kind, box=(.66, 420, 380), **kw):
    return B(kind, box, pre=branch(-150, 150, 4), **kw)
ART4["swallow"] = BP("farm", F="#1f3a6a", wing="#18305a", rx=62, ry=34, tilt=-14, neck=4, nw=36, hr=26, beak="short", beak_col=INK, leg_len=20, leg_col=INK, legw=4,
                     tail="fork", tail_col="#18305a", belly="#f6eee0", front_fn=lambda x, y, r: C(x - r * .2, y + r * .5, r * .45, "#b8402a", 0))
ART4["kingfisher"] = BP("wetland", F="#2a8ac8", wing="#1f6aa8", rx=54, ry=38, tilt=-20, neck=4, nw=40, hr=32, beak="long", beak_col=INK, leg_len=18, leg_col="#e8603a", legw=4,
                        tail="short", tail_col="#1f6aa8", belly="#e88a3a", front_fn=lambda x, y, r: E(x + r * .2, y + r * .35, r * .5, r * .2, "#e88a3a", 0))
ART4["mandarin-duck"] = B("pond", (.74, 460, 360), F="#8a5a3a", wing="#5a3a7a", rx=96, ry=50, tilt=-4, neck=20, nw=40, hr=34, beak="duck", beak_col="#e8403a", leg_len=0, sit=True,
                          tail="up", tail_col="#3a2a2a", head_col="#3a5a3a", belly="#f6eee0", front_fn=lambda x, y, r: E(x + r * .1, y - r * .05, r * .7, r * .25, "#ffffff", 0) + P(f"M{x+r*.4} {y+r*.4} l{r*.6} {r*.9} l{-r*.9} 0 Z", "#e8862a", 2))
ART4["mallard"] = B("pond", (.74, 460, 360), F="#a89a8a", wing="#7a6a5a", rx=100, ry=50, tilt=-4, neck=24, nw=40, hr=32, beak="duck", beak_col="#e8c83a", leg_len=0, sit=True,
                    tail="up", tail_col="#2a2a2a", head_col="#2a7a4a", belly="#c9c2b8", front_fn=lambda x, y, r: P(f"M{x-r*.6} {y+r*1.0} q{r*.6} {r*.3} {r*1.2} 0", sw=4, col="#ffffff"))
ART4["golden-eagle"] = B("plateau", (.78, 520, 420), pre=G_(rock(0, 0, 2.2), 0, 0), F="#5a3d2b", wing="#4a3222", rx=92, ry=62, tilt=-24, neck=24, nw=56, hr=40, beak="hook",
                         beak_col="#3a3a3a", leg_len=40, leg_col="#f2c53a", legw=7, tail="short", tail_col="#4a3222", head_col="#c99a4a")
ART4["peregrine"] = B("plateau", (.78, 460, 400), pre=G_(rock(0, 0, 1.8), 0, 0), F="#5a6a7a", wing="#3a4a5a", rx=70, ry=50, tilt=-30, neck=10, nw=48, hr=34, beak="hook",
                      beak_col="#3a3a3a", leg_len=30, leg_col="#f2c53a", legw=6, tail="short", tail_col="#3a4a5a", belly="#f2ede4", eye_ring="#f2c53a",
                      front_fn=lambda x, y, r: P(f"M{x-r*.1} {y+r*.1} l{r*.1} {r*.9}", sw=8, col=INK))
def _owl(F, spots, face, eye, tufts=False, box=(.74, 380, 420), kind="snow"):
    def f(w, h):
        o = P("M-90 -40 C-110 -160 -80 -250 0 -260 C80 -250 110 -160 90 -40 C60 -4 -60 -4 -90 -40 Z", F)
        o += "".join(C(-60 + (i * 31) % 120, -200 + (i * 23) % 150, 4, spots, 0) for i in range(22)) if spots else ""
        o += C(0, -200, 70, face, 2.8)
        if tufts: o += P("M-50 -250 l-20 -40 l36 24 Z M50 -250 l20 -40 l-36 24 Z", F, 2.6)
        o += C(-28, -206, 16, eye, 2.4) + C(28, -206, 16, eye, 2.4) + C(-28, -206, 8, INK, 0) + C(28, -206, 8, INK, 0) + P("M0 -194 L-8 -176 L0 -168 L8 -176 Z", "#3a3a3a", 2)
        o += P("M-40 -20 l-6 20 M-30 -20 l0 22 M30 -20 l0 22 M40 -20 l6 20", sw=5, col="#3a3a3a")
        return scene(kind, w, h, o, box=(w / 2, h * box[0], box[1], box[2]))
    return f
ART4["snowy-owl"] = _owl("#fbfbf8", "#3a3a3a", "#fbfbf8", "#f2c53a")
ART4["eagle-owl"] = _owl("#b8864a", "#5a3a20", "#d9b27a", "#f08a2a", tufts=True, kind="forest")
ART4["great-egret"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#f2f2ee", rx=80, ry=44, tilt=-14, neck=170, nw=16, hr=20, beak="long", beak_col="#f2c53a", leg_len=220, leg_col=INK, legw=5, tail="short", tail_col="#ffffff")
ART4["grey-heron"] = B("wetland", (.8, 480, 420), F="#a9b0b8", wing="#7a828a", rx=84, ry=48, tilt=-14, neck=150, nw=20, hr=22, beak="long", beak_col="#e8c83a", leg_len=200, leg_col="#c9b07a", legw=5,
                       tail="short", tail_col="#7a828a", head_col="#ffffff", front_fn=lambda x, y, r: P(f"M{x} {y-r*.4} l{r*2.4} {-r*.3}", sw=5, col=INK))
ART4["crested-ibis"] = B("wetland", (.8, 460, 420), F="#fbf2ee", wing="#f2c0b0", rx=84, ry=50, tilt=-12, neck=60, nw=22, hr=24, beak="long", beak_col=INK, leg_len=130, leg_col="#e8403a", legw=5,
                         tail="short", tail_col="#f2c0b0", crest="tuft", head_col="#fbf2ee", front_fn=lambda x, y, r: C(x - r * .3, y, r * .55, "#e8403a", 0))
ART4["white-stork"] = B("farm", (.8, 480, 420), F="#ffffff", wing="#2a2a2a", rx=96, ry=54, tilt=-10, neck=90, nw=26, hr=24, beak="long", beak_col="#e8403a", leg_len=200, leg_col="#e8403a", legw=6, tail="short", tail_col="#ffffff")
ART4["pelican"] = B("wetland", (.78, 500, 400), F="#fbf6f2", wing="#2a2a2a", rx=120, ry=66, tilt=-6, neck=70, nw=34, hr=30, beak="long", beak_col="#f2c06a", leg_len=0, sit=True, tail="short", tail_col="#fbf6f2",
                    front_fn=lambda x, y, r: P(f"M{x-r*.6} {y+r*.4} C{x-r*2} {y+r*2.2} {x-r*3.6} {y+r*1.4} {x-r*4.4} {y+r*.5}", "#f2d88a", 2.4))
ART4["cuckoo"] = BP("forest", F="#8a949e", wing="#6a747e", rx=64, ry=38, tilt=-20, neck=6, nw=36, hr=26, beak="short", beak_col="#3a3a3a", leg_len=20, leg_col="#f2c53a", legw=4,
                    tail="long", tail_col="#5a646e", belly="#f2efe8", eye_ring="#f2c53a", extras="".join(P(f"M{-40+i*16} 10 l14 0", sw=2, col="#5a646e") for i in range(6)))
ART4["hoopoe"] = B("meadow", (.78, 440, 380), F="#e0a06a", wing="#2a2a2a", rx=62, ry=40, tilt=-12, neck=12, nw=34, hr=26, beak="long", beak_col="#3a3a3a", leg_len=40, leg_col="#5a5a5a", legw=4,
                   tail="short", tail_col="#2a2a2a", extra_fn=lambda x, y, r: crest_fan(x, y, r, "#e0a06a", 6, 1.1), post="".join(P(f"M{-30+i*24} -70 l10 22", sw=6, col="#ffffff") for i in range(4)))
ART4["pheasant"] = B("meadow", (.78, 520, 360), F="#b8642a", wing="#8a6a3a", rx=82, ry=48, tilt=-6, neck=30, nw=30, hr=26, beak="short", beak_col="#e8d4a0", leg_len=60, leg_col="#9a8a7a", legw=5,
                     tail="long", tail_col="#a8743e", head_col="#2a6a5a", front_fn=lambda x, y, r: C(x, y + r * .05, r * .5, "#e8403a", 0) + P(f"M{x+r*.4} {y+r*.9} q{r*.6} {r*.3} {r*1.2} 0", sw=5, col="#ffffff"))
ART4["golden-pheasant"] = B("forest", (.78, 520, 360), F="#e8403a", wing="#2a4a8a", rx=72, ry=44, tilt=-6, neck=26, nw=28, hr=24, beak="short", beak_col="#f2d88a", leg_len=56, leg_col="#d9b07a", legw=5,
                            tail="long", tail_col="#c9884a", head_col="#f2c53a", crest="tuft", front_fn=lambda x, y, r: E(x + r * .6, y + r * 1.0, r * .9, r * .6, "#f28a2a", 2.4))
ART4["emu"] = B("savanna", (.8, 520, 420), F="#6a5a4a", wing="#5a4a3a", rx=100, ry=70, tilt=-4, neck=180, nw=26, hr=26, beak="short", beak_col="#3a3a3a", leg_len=200, leg_col="#7a7a7a", legw=10,
                tail="short", tail_col="#5a4a3a", head_col="#5a6a8a")
# birds batch 2
ART4["cassowary"] = B("rainforest", (.8, 520, 420), F="#1f1f22", wing="#2a2a2e", rx=100, ry=72, tilt=-4, neck=110, nw=28, hr=26, beak="short", beak_col="#3a3a3a", leg_len=170, leg_col="#6a6a5a", legw=12,
                      tail="short", tail_col="#1f1f22", head_col="#3a8ad0", front_fn=lambda x, y, r: P(f"M{x-r*.3} {y-r*.7} L{x+r*.1} {y-r*2.0} L{x+r*.6} {y-r*.7} Z", "#8a6a42", 2.4) + E(x + r * .3, y + r * 1.4, r * .25, r * .6, "#e8403a", 0))
ART4["kiwi"] = B("forest", (.78, 460, 300), F="#8a6a4a", wing="#7a5a3a", rx=110, ry=76, tilt=0, neck=0, nw=50, hr=34, beak="long", beak_col="#e8d4b0", leg_len=40, leg_col="#c9b49a", legw=8, tail="short", tail_col="#8a6a4a")
ART4["puffin"] = B("plateau", (.78, 400, 380), pre=G_(rock(0, 0, 1.6), 0, 0), F="#1f1f22", wing="#1f1f22", rx=58, ry=48, tilt=-60, neck=6, nw=46, hr=32, beak="short", beak_col="#e8603a", leg_len=24, leg_col="#e8803a", legw=6,
                   tail="short", tail_col="#1f1f22", belly="#ffffff", webbed=True, front_fn=lambda x, y, r: C(x, y, r * .75, "#f2f2ee", 0) + C(x - r * .2, y - r * .1, r * .15, INK, 0) + P(f"M{x-r*1.0} {y-r*.3} l{-r*.6} {r*.3} l{r*.6} {r*.4} Z", "#e8603a", 2))
def _albatross(w, h):
    o = P("M0 -100 C-120 -130 -260 -120 -360 -90 C-260 -96 -120 -80 -10 -70 Z M0 -100 C120 -130 260 -120 360 -90 C260 -96 120 -80 10 -70 Z", "#3a3a3a", 2.6)
    o += E(0, -84, 70, 22, "#ffffff", 2.8) + C(-70, -90, 18, "#ffffff", 2.6) + P("M-86 -92 L-130 -86 L-86 -82 Z", "#f2c0a0", 2.2) + C(-74, -94, 3, INK, 0) + P("M66 -84 l20 -6 l-4 12 Z", "#ffffff", 2)
    return scene("sea", w, h, o, box=(w / 2, h * .52, 680, 200))
ART4["albatross"] = _albatross
ART4["king-penguin"] = lambda w, h: scene("ice", w, h, art.ART["penguin"](w, h)[0:0] + bird(F="#3a3f45", wing="#2a2e33", rx=56, ry=90, tilt=-84, neck=10, nw=40, hr=30, beak="long", beak_col="#e88a3a", leg_len=12, leg_col=INK, legw=6,
                                     tail="short", tail_col="#2a2e33", belly="#ffffff", webbed=True, front=""), box=(w / 2, h * .74, 380, 420)) if False else _kingp(w, h)
def _kingp(w, h):
    o = E(0, -150, 70, 130, "#2a2e33", 3) + E(10, -140, 50, 110, "#ffffff", 0) + E(10, -210, 34, 30, "#f2c53a", 0)
    o += C(-10, -280, 40, "#1f1f22", 3) + E(10, -260, 10, 20, "#f28a2a", 0) + P("M-40 -280 L-100 -270 L-40 -264 Z", INK, 2) + P("M-80 -272 l30 0", sw=4, col="#e88a3a") + C(-20, -288, 4, "#fff", 0)
    o += P("M-60 -160 C-90 -120 -90 -80 -70 -50", sw=16, col=INK) + E(-20, 0, 26, 8, INK, 0) + E(30, 0, 26, 8, INK, 0)
    return scene("ice", w, h, o, box=(w / 2, h * .76, 300, 420))
ART4["king-penguin"] = _kingp
ART4["toucan"] = BP("rainforest", F="#1f1f22", wing="#1f1f22", rx=58, ry=44, tilt=-50, neck=6, nw=42, hr=30, beak="short", beak_col="#e8803a", leg_len=24, leg_col="#5a6a9a", legw=5,
                    tail="long", tail_col="#1f1f22", belly="#ffffff", eye_ring="#5a9ad0",
                    front_fn=lambda x, y, r: P(f"M{x-r*.7} {y-r*.4} C{x-r*2.4} {y-r*.8} {x-r*3.6} {y} {x-r*3.8} {y+r*.4} C{x-r*2.6} {y+r*.5} {x-r*1.4} {y+r*.4} {x-r*.7} {y+r*.4} Z", "#f28a2a", 2.4) + C(x - r * 3.6, y + r * .2, r * .2, INK, 0) + C(x + r * .2, y + r * .9, r * .6, "#ffffff", 0))
ART4["condor"] = B("plateau", (.78, 520, 420), pre=G_(rock(0, 0, 2.2), 0, 0), F="#1f1f22", wing="#2a2a2e", rx=96, ry=64, tilt=-22, neck=26, nw=50, hr=30, beak="hook", beak_col="#e8d4b0", leg_len=40, leg_col="#6a6a6a", legw=7,
                    tail="short", tail_col="#1f1f22", head_col="#c9887a", front_fn=lambda x, y, r: E(x + r * .6, y + r * 1.4, r * 1.2, r * .4, "#ffffff", 2.4))
ART4["secretary-bird"] = B("savanna", (.8, 500, 420), F="#c9ccd0", wing="#2a2a2a", rx=80, ry=52, tilt=-10, neck=50, nw=30, hr=28, beak="hook", beak_col="#9aa0a6", leg_len=220, leg_col="#f2d8b0", legw=6,
                            tail="long", tail_col="#3a3a3a", extra_fn=lambda x, y, r: crest_fan(x, y, r, "#2a2a2a", 6, 1.0), front_fn=lambda x, y, r: C(x - r * .2, y, r * .5, "#f28a2a", 0))
ART4["shoebill"] = B("wetland", (.8, 480, 420), F="#9aa6b2", wing="#7a8692", rx=86, ry=60, tilt=-14, neck=60, nw=40, hr=40, beak="short", beak_col="#c9b48a", leg_len=150, leg_col=INK, legw=7, tail="short", tail_col="#7a8692",
                      front_fn=lambda x, y, r: P(f"M{x-r*.8} {y-r*.3} C{x-r*2.2} {y-r*.4} {x-r*2.6} {y+r*.3} {x-r*2.4} {y+r*.9} C{x-r*1.8} {y+r*1.1} {x-r*1.0} {y+r*.8} {x-r*.7} {y+r*.4} Z", "#c9b48a", 2.6))
ART4["raven"] = BP("forest", F="#1f1f26", wing="#2a2a36", rx=72, ry=46, tilt=-24, neck=10, nw=44, hr=30, beak="short", beak_col="#1f1f26", leg_len=30, leg_col=INK, legw=5, tail="long", tail_col="#1f1f26",
                   front_fn=lambda x, y, r: P(f"M{x-r*.7} {y-r*.2} L{x-r*2.0} {y+r*.2} L{x-r*.7} {y+r*.4} Z", "#1f1f26", 2.4))
ART4["great-tit"] = BP("forest", F="#d9d26a", wing="#6a8a7a", rx=50, ry=38, tilt=-24, neck=4, nw=38, hr=28, beak="cone", beak_col=INK, leg_len=22, leg_col="#6a7a8a", legw=4, tail="long", tail_col="#5a6a7a",
                       head_col="#1f1f22", front_fn=lambda x, y, r: C(x + r * .1, y + r * .1, r * .5, "#ffffff", 0) + P(f"M{x} {y+r*.8} L{x+r*.6} {y+r*3.2}", sw=8, col=INK))
ART4["robin"] = BP("forest", F="#8a7a5a", wing="#7a6a4a", rx=50, ry=40, tilt=-20, neck=4, nw=40, hr=28, beak="short", beak_col=INK, leg_len=24, leg_col="#8a6a5a", legw=4, tail="short", tail_col="#7a6a4a",
                   belly="#f2efe6", front_fn=lambda x, y, r: C(x - r * .1, y + r * .6, r * .9, "#e8703a", 0))
ART4["cardinal"] = BP("forest", F="#d8282a", wing="#b81e22", rx=54, ry=40, tilt=-24, neck=4, nw=40, hr=30, beak="cone", beak_col="#f2802a", leg_len=24, leg_col="#8a6a5a", legw=4, tail="long", tail_col="#b81e22",
                      crest="tuft", front_fn=lambda x, y, r: E(x - r * .6, y + r * .1, r * .45, r * .5, INK, 0))
ART4["bar-headed-goose"] = B("plateau", (.8, 480, 400), F="#c9ccd0", wing="#9aa0a6", rx=96, ry=56, tilt=-6, neck=90, nw=28, hr=26, beak="duck", beak_col="#f2c53a", leg_len=70, leg_col="#f2a03a", legw=6, tail="short", tail_col="#9aa0a6",
                            head_col="#ffffff", front_fn=lambda x, y, r: P(f"M{x-r*.2} {y-r*.9} q{r*.6} {r*.2} {r*1.0} {r*.6} M{x-r*.4} {y-r*.4} q{r*.6} {r*.2} {r*1.0} {r*.6}", sw=6, col=INK))
ART4["bn-crane"] = B("plateau", (.8, 500, 420), F="#e8eaee", wing="#2a2a2a", rx=96, ry=56, tilt=-8, neck=150, nw=22, hr=24, beak="long", beak_col="#9aa58a", leg_len=220, leg_col="#3a3f45", legw=6,
                     tail="up", tail_col="#2a2a2a", crest="red", head_col="#1f1f22")
ART4["starling"] = BP("farm", F="#2a2e3a", wing="#2a3a4a", rx=56, ry=40, tilt=-20, neck=4, nw=38, hr=26, beak="long", beak_col="#f2d23a", leg_len=24, leg_col="#c98a7a", legw=4, tail="short", tail_col="#2a3a4a",
                      extras="".join(C(-40 + (i * 23) % 90, -20 + (i * 13) % 40, 3, "#e8e0c8", 0) for i in range(14)))
ART4["kookaburra"] = BP("savanna", F="#f2ece0", wing="#7a5a3a", rx=66, ry=50, tilt=-30, neck=6, nw=48, hr=36, beak="long", beak_col="#3a3a3a", leg_len=24, leg_col="#8a8a7a", legw=5, tail="long", tail_col="#a8643a",
                        front_fn=lambda x, y, r: P(f"M{x-r*.1} {y-r*.1} l{r*1.0} {r*.2}", sw=7, col="#5a3a20"))
ART4["arctic-tern"] = B("sea", (.56, 560, 260), pre="", F="#ffffff", wing="#c9ccd0", rx=70, ry=30, tilt=-6, neck=10, nw=30, hr=24, beak="long", beak_col="#e8282a", leg_len=0, sit=True, tail="fork", tail_col="#ffffff", head_col="#1f1f22",
                        post=P("M-10 -60 C60 -140 160 -160 240 -140 C160 -120 80 -90 20 -50 Z", "#dfe3e8", 2.6))
