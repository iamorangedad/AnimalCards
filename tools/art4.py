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
