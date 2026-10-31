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
