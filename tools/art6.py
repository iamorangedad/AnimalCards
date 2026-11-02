"""Phase-5 art (cards 1001–1500). Reuses the parametric helpers of art2–art5."""
import art as _art
from art2 import *
from art3 import *
from art4 import *
from art5 import *
import art5 as _a5
import art4 as _a4
import art3 as _a3
import art2 as _a2
_pond = _a4._pond
ART6 = {}
_sn = getattr(_a5, "_snail", None)
# ---- batch p5_pet1 ----
ART6["rough-collie"] = DOGQ(F="#c98a4a", belly="#ffffff", wool="#d9a060", neck_wool="#ffffff", ears="point", tail="bushy", tail_col="#c98a4a", snout=(56, 26), snout_col="#ffffff", lh=110, bl=260)
ART6["dalmatian"] = DOGQ(F="#ffffff", pattern="spots", pat_col="#2a2a2e", ears="droop", tail="thin", tail_col="#ffffff", snout_col="#ffffff", lh=116, bl=260)
ART6["bulldog"] = DOGQ("home", (.76, 520, 320), F="#e8d8c0", belly="#ffffff", pattern="patches", pat_col="#c98a4a", ears="small", tail="short", lh=60, bl=230, bd=120, head=(62, 56), snout=(20, 30), snout_col="#ffffff")
ART6["yorkie"] = DOGQ("home", (.76, 440, 300), F="#4a5260", wool="#5a6270", head=(46, 42), snout=(26, 22), snout_col="#c98a4a", mask="#c98a4a", ears="point", tail="short", lh=60, bl=170, bd=70, nw=46)
ART6["pomeranian"] = DOGQ("home", (.76, 440, 300), F="#e8963a", wool="#f0a84a", neck_wool="#f0a84a", ears="point", tail="curl", tail_col="#f0a84a", snout=(22, 20), lh=56, bl=170, bd=96, head=(48, 44))
ART6["schnauzer"] = DOGQ("home", (.76, 480, 320), F="#7a7e86", belly="#c9ccd1", ears="point", tail="short", snout=(52, 32), snout_col="#dcdfe4", lh=84, bl=210, bd=86)
ART6["shih-tzu"] = DOGQ("home", (.76, 460, 300), F="#f2ead8", wool="#f6f0e2", neck_wool="#c99a6a", ears="droop", tail="curl", tail_col="#f6f0e2", snout=(18, 22), mask="#c99a6a", lh=50, bl=190, bd=90, head=(50, 46))
ART6["akita"] = DOGQ("snow", F="#d9843a", belly="#ffffff", ears="point", tail="curl", tail_col="#d9843a", snout=(44, 32), snout_col="#ffffff", lh=116, bl=270, bd=116, head=(58, 50))
ART6["greyhound"] = DOGQ(F="#9aa0a8", belly="#c9ccd1", ears="small", tail="thin", tail_col="#9aa0a8", snout=(64, 22), lh=140, bl=270, bd=86, nw=56, head=(46, 34))
ART6["st-bernard"] = DOGQ("snow", F="#ffffff", pattern="patches", pat_col="#b8642a", ears="droop", tail="bushy", tail_col="#b8642a", snout=(46, 36), snout_col="#ffffff", lh=120, bl=290, bd=130, head=(64, 56), mask="#b8642a")
ART6["abyssinian"] = CATQ(F="#c9844a", belly="#e8c08a", ears="big", tail="long", tail_col="#a8642a", lh=104, bl=240, bd=80, head=(42, 36))
ART6["russian-blue"] = CATQ(F="#8a96a8", ears="point", tail="long", tail_col="#8a96a8", lh=96, bl=230, bd=86)
ART6["norw-forest"] = CATQ("snow", F="#8a7a6a", wool="#a89a8a", neck_wool="#e8e0d6", pattern="stripes", pat_col="#5a4a3a", tail="bushy", tail_col="#7a6a5a", lh=96, bl=270, bd=104)
ART6["lionhead"] = lambda w, h: scene("meadow", w, h, blob(F="#d9a46a", L=190, H=150, belly="#f6efe2", ears="round", tail="puff", nose="#e8a0a0", whisk=True) +
                                       "".join(C(-70 + 40 * math.cos(a / 6 * math.pi), -110 + 40 * math.sin(a / 6 * math.pi), 26, "#e8b88a", 0) for a in range(12)), box=(w / 2, h * .74, 420, 300))
ART6["parrotlet"] = mk_bird(dict(F="#7fc65a", wing="#5aa83a", rx=50, ry=38, tilt=-28, neck=4, nw=40, hr=28, beak="hook", beak_col="#f2c0b0", leg_len=24, leg_col="#e8b0a0",
                                 tail="short", tail_col="#3a7ad9", head_col="#9fe07a"), kind="rainforest", front_fn=lambda x, y, r: E(x - r * 2.2, y + r * 1.5, r * .9, r * .4, "#3a7ad9", 0))
ART6["society-finch"] = mk_bird(dict(F="#f6f0e2", wing="#8a5a3a", rx=54, ry=40, tilt=-20, neck=4, nw=38, hr=28, beak="cone", beak_col="#8a8a8a", leg_len=24, leg_col="#e8b8a0",
                                     tail="short", tail_col="#6a4a2a", head_col="#8a5a3a"))
ART6["pearl-gourami"] = tank(fish(F="#b8aa98", L=220, H=120, tail="round", eye_r=8, fin_col="#c9a07a", belly="#f2803a",
                                  extras="".join(C(-80 + (i * 37) % 170, -40 + (i * 23) % 70, 6, "#f6f0e2", 0) for i in range(22)) + P("M-100 0 L100 6", sw=5, col="#2a2a2e")))
ART6["ghost-shrimp"] = tank(shrimp(F="#e6eef2", L=240, H=56) + G_(shrimp(F="#e6eef2", L=150, H=36), 70, 90), box=(None, 340, 360, 240))
ART6["african-snail"] = lambda w, h: scene("meadow", w, h,
    P("M-230 0 C-230 -30 -140 -44 80 -34 C150 -30 190 -12 200 0 Z", "#9a8a72", 2.8) + P("M-220 -14 l-30 -70 M-196 -20 l-12 -62", sw=4) + C(-250, -86, 6, INK, 0) + C(-208, -84, 6, INK, 0) +
    P("M-60 -30 C-90 -160 60 -260 140 -170 C180 -110 120 -40 60 -30 Z", "#a8642a", 3) + "".join(P(f"M{-40+k*30} {-50-k*28} q60 -10 90 40", sw=7, col="#5a3a1a") for k in range(5)), box=(w / 2, h * .76, 520, 360))
ART6["gargoyle-gecko"] = lambda w, h: scene("rainforest", w, h, branch(-240, 240, 4, 12) + lizard("#a89a7a", L=210, H=58, tail=.8, snout=44, sh=44, spots="#6a5a42", legs=14, legh=34, eye_top=True), box=(w / 2, h * .68, 560, 260))

def _a4_crab_col(w, h, F, kind="wetland"):
    o = []
    for s in (-1, 1):
        for i in range(4):
            x = s * (60 + i * 22)
            o.append(P(f"M{s*50} {-40+i*10} L{x+s*50} {-70+i*6} L{x+s*80} {10+i*4}", sw=8, col=INK) + P(f"M{s*50} {-40+i*10} L{x+s*50} {-70+i*6} L{x+s*80} {10+i*4}", sw=5, col=F))
        cx = s * 120
        o.append(P(f"M{s*40} -70 L{cx} -130", sw=12, col=INK) + P(f"M{s*40} -70 L{cx} -130", sw=8, col=F))
        o.append(E(cx, -150, 40, 30, F, 2.6) + E(cx + s * 10, -168, 14, 8, "#1a1a1a", 0))
    o.append(E(0, -50, 100, 64, F, 3) + C(-22, -112, 8, INK, 0) + C(22, -112, 8, INK, 0) + P("M-22 -104 v-6 M22 -104 v-6", sw=3))
    return scene(kind, w, h, "".join(o), box=(w / 2, h * .72, 520, 300))
# ---- batch p5_farm1 ----
_FLY = getattr(_a5, "_FLY")
ART6["gayal"] = Q("forest", None, F="#2e2622", bl=340, bd=160, lh=110, lw=36, neck=(20, 60), nw=96, head=(56, 50), snout=(40, 38), snout_col="#3a3230", ears="side", horns="cow", tail="tuft", tail_col="#2e2622", hooves="#f6f0e2")
ART6["zebu"] = COW("#e8e2d8", horns="cow", snout_col="#9a948c", extras=P("M-120 -190 C-110 -260 -40 -260 -30 -190 Z", "#e8e2d8", 3))
ART6["cochin"] = HEN("#e8b05a", wing="#d99a3a", rx=96, ry=80, leg_len=40)
ART6["tibetan-mastiff"] = DOGQ("plateau", F="#2a2622", wool="#3a3430", neck_wool="#3a3430", mask="#b8642a", ears="droop", tail="curl", tail_col="#3a3430", snout=(42, 36), lh=116, bl=280, bd=130, head=(64, 56))
ART6["mud-crab"] = lambda w, h: _a4_crab_col(w, h, "#3a5a3a")
ART6["red-seabream"] = lambda w, h: scene("sea", w, h, fish(F="#e8707a", L=330, H=170, tail="fork", eye_r=9, fin_col="#d9505a", belly="#f6d8d8",
                                                        extras="".join(C(-60 + (i * 41) % 200, -50 + (i * 23) % 60, 5, "#5ab8e8", 0) for i in range(14))), box=(w / 2, h * .66, 520, 280))
ART6["crucian"] = _pond(fish(F="#9a8a4a", L=300, H=170, tail="fork", eye_r=8, fin_col="#7a6a3a", belly="#e9dcb0"))
ART6["rohu"] = _pond(fish(F="#a8b0b8", L=360, H=130, tail="fork", eye_r=7, fin_col="#c97a6a", belly="#eef0f2", extras="".join(C(-80 + (i * 37) % 220, -30 + (i * 19) % 50, 6, "#d98a7a", 0) for i in range(12))))
ART6["iberian-pig"] = PIG("#3a3436", hooves="#1a1a1a", snout=(44, 34), ears="side")
ART6["toulouse-goose"] = lambda w, h: scene("farm", w, h, bird(F="#8a8a8e", wing="#6a6a70", rx=120, ry=74, tilt=-6, neck=80, nw=40, hr=32, beak="duck", beak_col="#f2902a", leg_len=34, leg_col="#f2902a", legw=6,
                                                             tail="short", tail_col="#6a6a70", webbed=True, crest=None, belly="#f2f0ec"), box=(w / 2 - 40, h * .76, 500, 400))
ART6["italian-bee"] = _FLY("meadow", F="#e8b84a", stripes="#7a4a1a", ab=1.0, eye="#2a2a2a", sting=True)
ART6["hampshire-pig"] = PIG("#2a2628", extras=P("M40 -150 L120 -150 L120 0 L40 0 Z", "#f6f2ee", 0), ears="point")
ART6["jacob-sheep"] = Q("farm", (.75, 560, 360), F="#2a2628", bl=290, bd=150, lh=96, lw=24, wool="#f6efe0", pattern="patches", pat_col="#3a3436", neck=(10, 60), nw=74, head=(44, 46), snout=(30, 32), snout_col="#f6efe0",
                        ears="side", horns="ram", tail="short", hooves="#2a2628")
ART6["nubian-goat"] = GOAT("#9a5a32", ears="long", horns=None, mask="#e8d8c0")
ART6["brown-swiss"] = COW("#7a6658", horns="cow", snout_col="#2a2422", udder="#e8c8b8")
ART6["percheron"] = HORSE("#9aa0a8", bl=350, bd=160, lh=170, lw=40, snout_col="#6a7078")
ART6["plymouth-rock"] = HEN("#8a8e96", wing="#6a6e76")
ART6["cayuga"] = lambda w, h: scene("pond", w, h, bird(F="#1e2a26", wing="#2a5a4a", rx=92, ry=56, tilt=-22, neck=26, nw=40, hr=32, beak="duck", beak_col="#1a1a1a", leg_len=36, leg_col="#2a2a2a", legw=6, tail="up", tail_col="#1e2a26", webbed=True), box=(w / 2 - 30, h * .76, 460, 340))
ART6["seabass"] = lambda w, h: scene("sea", w, h, fish(F="#9aa8b4", L=360, H=120, tail="fork", eye_r=8, fin_col="#7a8894", belly="#eef2f4"), box=(w / 2, h * .66, 540, 240))
ART6["ayu"] = _pond(fish(F="#a8a87a", L=320, H=80, tail="fork", eye_r=7, fin_col="#d9c04a", belly="#eef0e2", extras=C(-30, -10, 14, "#f2d03a", 0)))
# ---- batch p5_grass ----
ANT = _a5.ANT; CAN = _a5.CAN; _apeS = _a5._apeS; _ringtail = _a5._ringtail; rodent = _a4.rodent; lighter = _a5.lighter
def _armad(F, scale=1.0, kind="savanna", band=15):
    def f(w, h):
        o = E(0, -90, 160 * scale, 80 * scale, F, 3) + "".join(P(f"M{x} {-90-78*scale} C{x-4} -120 {x-4} -60 {x} -14", sw=3) for x in range(int(-60 * scale), int(70 * scale), band))
        o += P(f"M{-150*scale} -70 C{-210*scale} -80 {-230*scale} -50 {-250*scale} -40 C{-220*scale} -30 {-170*scale} -30 {-140*scale} -40 Z", lighter(F, .2), 2.8) + C(-190 * scale, -60, 5, INK, 0)
        o += P(f"M{150*scale} -80 C{210*scale} -70 {260*scale} -40 {280*scale} -10", sw=18, col=INK) + P(f"M{150*scale} -80 C{210*scale} -70 {260*scale} -40 {280*scale} -10", sw=12, col=F)
        o += "".join(P(f"M{x} -20 l0 30", sw=14, col=INK) + P(f"M{x} -20 l0 30", sw=9, col=lighter(F, .2)) for x in (-90 * scale, -40 * scale, 50 * scale, 100 * scale))
        return scene(kind, w, h, o, box=(w / 2, h * .76, 560, 300))
    return f
ART6["black-wildebeest"] = Q("savanna", (.76, 560, 440), F="#3a3430", bl=280, bd=124, lh=140, lw=24, neck=(30, 50), nw=70, head=(40, 36), snout=(52, 30), snout_col="#2a2420",
                             ears="side", horns="wildebeest", mane="zebra", tail="horse", tail_col="#f4f0ea", hooves=INK, beard="#2a2420", shoulder=26)
ART6["roan-antelope"] = ANT("savanna", "#b8865a", horns="goat", bl=290, bd=130, lh=160, lw=26, head=(42, 36), snout=(46, 30), snout_col="#f4efe6", mask="#2a2420", ears="big", mane="zebra")
ART6["blesbok"] = ANT("savanna", "#6a3a2a", horns="goat", bl=260, bd=110, lh=140, lw=20, head=(38, 32), snout=(44, 26), snout_col="#ffffff", belly="#ffffff")
ART6["euro-hare"] = lambda w, h: scene("meadow", w, h, rodent("#a8784a", 260, 150, belly="#e9d4b8", ears="big", tail="puff", tailcol="#ffffff", tl=.3, nose="#5a3a2a"), box=(w / 2, h * .76, 480, 320))
ART6["daurian-gs"] = lambda w, h: scene("meadow", w, h, rodent("#b8a07a", 220, 140, belly="#ece0c8", ears="small", tail="bushy", tailcol="#9a8460", tl=.4, nose="#5a4a3a"), box=(w / 2, h * .76, 420, 290))
ART6["patas"] = _apeS("savanna", F="#c9703a", face="#3a3030", H=270, ear_col="#c9703a", brow=False, hair="#f4efe6")
ART6["wild-bactrian"] = lambda w, h: scene("desert", w, h, quad(F="#c9a878", bl=280, bd=120, lh=190, lw=26, hump="camel", neck=(110, 52), nw=50, head=(38, 30), snout=(44, 30),
                                                         ears="small", tail="tuft", tail_col="#8a6a42"), box=(w / 2, h * .75, 560, 440))
ART6["lechwe"] = ANT("wetland", "#d9984a", horns="goat", bl=250, bd=104, lh=140, lw=18, belly="#ffffff", head=(36, 30), snout=(40, 24))
ART6["oribi"] = ANT("savanna", "#d9a060", horns="goat", bl=200, bd=80, lh=130, lw=14, belly="#ffffff", head=(32, 28), snout=(34, 22), ears="big", box=(.76, 480, 380))
ART6["steenbok"] = ANT("savanna", "#d98a4a", horns="goat", bl=180, bd=76, lh=110, lw=12, belly="#ffffff", head=(32, 28), snout=(32, 20), ears="big", box=(.76, 460, 340))
ART6["grants-gazelle"] = ANT("savanna", "#d4a46a", horns="chiru", bl=250, bd=100, lh=150, lw=16, belly="#ffffff", head=(34, 30), snout=(40, 24))
ART6["dama-gazelle"] = ANT("desert", "#ffffff", horns="goat", bl=250, bd=96, lh=170, lw=16, belly="#ffffff", neck=(60, 26), head=(34, 30), snout=(38, 22), snout_col="#b8643a", mask="#b8643a")
ART6["scimitar-oryx"] = ANT("desert", "#f4efe6", horns="goat", bl=290, bd=120, lh=150, lw=24, head=(40, 34), snout=(44, 28), neck=(40, 40), mask="#b8643a", tail="tuft", tail_col="#5a3a2a")
ART6["jackrabbit"] = lambda w, h: scene("desert", w, h, rodent("#b89a7a", 250, 140, belly="#ece0d0", ears="big", tail="puff", tailcol="#2a2a2a", tl=.3, nose="#5a3a2a"), box=(w / 2, h * .76, 460, 320))
ART6["swift-fox"] = CAN("meadow", "#e0aa6a", bl=210, bd=84, lh=100, lw=16, head=(36, 32), snout=(36, 20), ears="big", tail_col="#2a2a2a")
ART6["pampas-deer"] = Q("meadow", (.78, 540, 440), F="#c9925a", bl=250, bd=100, lh=140, lw=18, belly="#f4efe6", neck=(56, 30), nw=50, head=(36, 30), snout=(40, 24), snout_col="#d9a06a",
                        ears="big", horns="antler", tail="short", tail_col="#ffffff", hooves=INK)
ART6["hairy-armadillo"] = _armad("#8a7a6a", .85, "meadow", 13)
ART6["giant-armadillo"] = _armad("#6a6058", 1.1, "savanna", 18)
ART6["steppe-polecat"] = Q("meadow", (.75, 560, 280), F="#e8dcc0", bl=280, bd=70, lh=50, lw=18, belly="#2a2622", neck=(18, 36), nw=46, head=(36, 30), snout=(24, 20), snout_col="#ffffff",
                           mask="#2a2622", ears="round", tail="bushy", tail_col="#2a2622")
ART6["sand-cat"] = CATQ("desert", F="#e0c898", belly="#f4ead8", ears="big", tail="long", tail_col="#c9a878", lh=80, bl=220, bd=86, head=(48, 40))
ART6["goitered"] = ANT("desert", "#c9a070", horns="chiru", bl=240, bd=96, lh=150, lw=16, belly="#ffffff", head=(34, 30), snout=(38, 22), tail="short", tail_col="#2a2a2a")
ART6["przewalski-gaz"] = ANT("plateau", "#c9a070", horns="chiru", bl=230, bd=92, lh=130, lw=16, belly="#ffffff", head=(34, 30), snout=(36, 22))
ART6["zokor"] = lambda w, h: scene("meadow", w, h, P("M-220 20 C-190 -30 -110 -30 -80 20 Z", "#9a7a5a", 2.6) + rodent("#a88a72", 230, 130, belly="#c9b098", ears="small", tail="rope", tl=.2, tailcol="#c9b098", nose="#e8a0a0"), box=(w / 2, h * .76, 460, 290))
ART6["brown-hyena"] = CAN("desert", "#5a4a3e", bl=260, bd=120, lh=130, lw=26, tail_col="#3a3028", snout_col="#3a3028", mane="zebra", ears="point", wool="#6a5a4e")
ART6["common-duiker"] = ANT("savanna", "#9a8466", horns="goat", bl=190, bd=82, lh=110, lw=12, belly="#d9cbb0", head=(34, 30), snout=(34, 22), ears="big", box=(.76, 460, 340))
ART6["13-lined"] = lambda w, h: scene("meadow", w, h, rodent("#a87a4a", 230, 120, belly="#e9d4b0", ears="small", stripe="#f4ead0", tail="rope", tl=.5, tailcol="#a87a4a", nose="#5a3a2a"), box=(w / 2, h * .76, 440, 280))
ART6["mule-deer"] = Q("forest", (.78, 560, 460), F="#8a7a6a", bl=270, bd=116, lh=150, lw=22, belly="#d9cfc0", neck=(56, 34), nw=58, head=(40, 34), snout=(42, 28), snout_col="#d9cfc0",
                      ears="big", horns="antler", tail="short", tail_col="#2a2a2a", hooves=INK)
ART6["rhebok"] = ANT("plateau", "#a8a49a", horns="goat", bl=220, bd=90, lh=130, lw=14, belly="#e9e6e0", head=(34, 30), snout=(36, 22), neck=(60, 26))
ART6["mountain-zebra"] = Q("plateau", (.76, 560, 440), F="#ffffff", bl=270, bd=116, lh=150, lw=24, pattern="stripes", pat_col=INK, neck=(40, 46), nw=64, head=(40, 36), snout=(50, 30),
                           snout_col="#3a3f45", ears="point", mane="zebra", tail="tuft", tail_col=INK, hooves=INK)
ART6["black-footed-cat"] = CATQ("savanna", F="#d9b88a", belly="#f4ead8", pattern="spots", pat_col="#2a2420", ears="round", tail="long", tail_col="#d9b88a", lh=70, bl=190, bd=74, head=(42, 36))
# ---- batch p5_forest ----
_bear = _a4.bear; branch = _a3.branch; _treeape = _a5._treeape
def _recol(fn, pairs):
    def f(w, h):
        s = fn(w, h)
        for a, b in pairs: s = s.replace(a, b)
        return s
    return f
ART6["fisher"] = Q("forest", (.75, 580, 300), F="#3a2e28", bl=290, bd=86, lh=64, lw=22, belly="#4a3e36", neck=(22, 40), nw=56, head=(38, 32), snout=(28, 22), snout_col="#4a3e36", ears="round", tail="bushy", tail_col="#2a2220")
ART6["tree-kangaroo"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 18) + G_(kangaroo(F="#a8502a", belly="#e8c08a"), 0, -20), box=(w / 2, h * .72, 480, 420))
ART6["sloth-2"] = _recol(lambda w, h: scene("rainforest", w, h, sloth(), box=(w / 2, h * .68, 560, 360)), [("#b39c80", "#c9a880")])
ART6["black-howler"] = _treeape("rainforest", _ringtail("#2a2622", None, 12), F="#2a2622", face="#3a3430", H=270, ear_col="#2a2622", brow=False, hair="#2a2622")
ART6["woolly-monkey"] = _treeape("rainforest", _ringtail("#8a6a4a", None, 14), F="#8a6a4a", face="#3a3030", H=260, ear_col="#8a6a4a", brow=False)
ART6["banteng"] = Q("forest", None, F="#8a4a2a", bl=330, bd=150, lh=120, lw=34, neck=(20, 60), nw=90, head=(52, 48), snout=(42, 38), snout_col="#d9c8b0", ears="side", horns="cow", tail="tuft",
                    tail_col="#2a2220", hooves="#f4efe6", extras=E(150, -120, 40, 30, "#ffffff", 0))
ART6["sambar"] = Q("forest", (.78, 560, 460), F="#6a5040", bl=290, bd=124, lh=150, lw=24, belly="#8a7060", neck=(56, 36), nw=62, head=(42, 36), snout=(44, 30), snout_col="#5a4030", ears="big", horns="antler", tail="short", tail_col="#2a2220", hooves=INK)
ART6["pere-david"] = Q("wetland", (.78, 560, 460), F="#b8845a", bl=290, bd=120, lh=140, lw=24, belly="#d9b890", neck=(50, 34), nw=58, head=(42, 34), snout=(48, 28), snout_col="#8a6a4a", ears="side", horns="antler", tail="long", tail_col="#5a4030", hooves=INK)
ART6["flying-squirrel"] = lambda w, h: scene("forest", w, h, P("M-150 -40 L150 -40 L120 40 L-120 40 Z", "#b8b0a4", 3) + rodent("#b8b0a4", 200, 120, belly="#f4f0ea", ears="round", tail="bushy", tailcol="#a8a094", tl=.6, nose="#e8a0a0"), box=(w / 2, h * .62, 460, 300))
ART6["edible-dormouse"] = lambda w, h: scene("forest", w, h, branch(-260, 260, 4, 16) + rodent("#9a9690", 220, 130, belly="#ece8e2", ears="round", tail="bushy", tailcol="#8a8680", tl=.8, nose="#e8a0a0"), box=(w / 2, h * .66, 460, 300))
ART6["blue-duiker"] = ANT("rainforest", "#6a6670", horns="goat", bl=170, bd=74, lh=90, lw=12, belly="#c9c6cc", head=(32, 28), snout=(32, 20), ears="small", box=(.76, 440, 320))
ART6["black-muntjac"] = Q("forest", (.78, 520, 400), F="#3a2e28", bl=220, bd=90, lh=100, lw=16, belly="#5a4a40", neck=(40, 28), nw=44, head=(34, 28), snout=(32, 22), snout_col="#3a2e28", ears="big", horns="antler", tail="short", tail_col="#ffffff", hooves=INK)
ART6["sumatran-orang"] = lambda w, h: scene("rainforest", w, h, ape(F="#d9843a", face="#b89a80", H=310, arms=1.4, cheekpads=False, hair="#e8944a", ear_col="#b89a80"), box=(w / 2, h * .76, 460, 410))
ART6["eastern-gorilla"] = lambda w, h: scene("forest", w, h, ape(F="#1e1e22", face="#3a3a3e", H=350, arms=1.3, crest=True, ear_col="#1e1e22", hair="#2a2a2e"), box=(w / 2, h * .76, 470, 420))
ART6["siamang"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 14) + ape(F="#1a1a1e", face="#2a2a2e", H=270, arms=1.7, ear_col="#1a1a1e", brow=False) + C(-6, -150, 34, "#7a6a6a", 3), box=(w / 2, h * .76, 480, 420))
ART6["ruffed-lemur"] = _treeape("rainforest", _ringtail("#1e1e22", None, 14), F="#f4f2ee", face="#1e1e22", H=250, ear_col="#f4f2ee", brow=False, hair="#1e1e22")
ART6["slender-loris"] = _recol(_a4._loris, [("#c9a07a", "#a8988a"), ("#5a3a26", "#3a2a22")])
ART6["colugo"] = lambda w, h: scene("rainforest", w, h, P("M-180 -60 L180 -60 L150 40 L-150 40 Z", "#8a8a7a", 3) + rodent("#8a8a7a", 220, 120, belly="#b8b8a8", ears="small", tail="rope", tailcol="#8a8a7a", tl=.6, nose="#3a3a3a"), box=(w / 2, h * .62, 480, 300))
ART6["treeshrew"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 14) + rodent("#8a5a3a", 200, 110, belly="#c9a07a", ears="small", tail="bushy", tailcol="#6a4a2a", tl=1.0, nose="#3a2a1e"), box=(w / 2, h * .66, 460, 290))
ART6["large-civet"] = Q("forest", (.75, 580, 280), F="#a89a88", bl=280, bd=84, lh=60, lw=20, pattern="spots", pat_col="#2a2a2a", neck=(20, 46), nw=56, head=(38, 30), snout=(36, 22), snout_col="#2a2a2a", ears="round", tail="long", tail_col="#2a2a2a")
ART6["yt-marten"] = Q("forest", (.75, 580, 300), F="#3a2a22", bl=280, bd=82, lh=64, lw=20, belly="#e8b83a", neck=(22, 40), nw=56, head=(38, 32), snout=(28, 22), snout_col="#3a2a22", ears="round", tail="long", tail_col="#2a1e1a", mask="#e8b83a")
ART6["leopard-cat"] = CATQ("forest", F="#d9a860", belly="#f4ead8", pattern="spots", pat_col="#2a2420", ears="round", tail="long", tail_col="#d9a860", lh=84, bl=220, bd=78)
ART6["marbled-cat"] = lambda w, h: scene("rainforest", w, h, branch(-260, 260, 4, 18) + G_(quad(F="#a8886a", bl=230, bd=78, lh=64, lw=20, belly="#d9c4a8", pattern="patches", pat_col="#4a3a2a",
                                             neck=(18, 34), nw=50, head=(34, 30), snout=(22, 22), snout_col="#d9c4a8", ears="round", tail="bushy", tail_col="#a8886a"), 0, -10), box=(w / 2, h * .66, 580, 320))
ART6["fishing-cat"] = CATQ("wetland", F="#9a9a88", belly="#d9d6c8", pattern="spots", pat_col="#2a2a2a", ears="small", tail="long", tail_col="#9a9a88", lh=80, bl=250, bd=100, head=(46, 40))
ART6["tayra"] = Q("rainforest", (.75, 580, 300), F="#2a2220", bl=290, bd=86, lh=66, lw=22, neck=(22, 40), nw=58, head=(38, 32), snout=(28, 22), snout_col="#a8845a", mask="#a8845a", ears="round", tail="bushy", tail_col="#2a2220")
ART6["paca"] = lambda w, h: scene("rainforest", w, h, rodent("#6a4a32", 260, 150, belly="#e8dcc8", ears="small", stripe=None, tail=None, nose="#3a2a1e") +
                                  "".join(C(-80 + i * 34, -70 - (i % 2) * 26, 8, "#f4efe6", 0) for i in range(6)), box=(w / 2, h * .76, 460, 300))
ART6["agouti"] = lambda w, h: scene("rainforest", w, h, rodent("#b8783a", 240, 140, belly="#d9a868", ears="small", tail=None, nose="#3a2a1e"), box=(w / 2, h * .76, 440, 300))
ART6["bush-dog"] = CAN("rainforest", "#8a4a2a", bl=230, bd=96, lh=60, lw=22, head=(40, 34), snout=(28, 24), ears="round", tail="short", tail_col="#3a2a22", farleg="#3a2a22")
ART6["javan-rhino"] = Q("rainforest", None, F="#7a7880", bl=330, bd=150, lh=90, lw=46, neck=(0, 0), head=(56, 50), snout=(52, 44), ears="point", horns="rhino", tail="tuft", tail_col="#4a4642", headdown=30, nose=None,
                        extras=P("M-80 -240 C-70 -190 -70 -140 -80 -100 M110 -240 C100 -190 100 -140 110 -100", sw=4, col="#5a5860"))
ART6["spectacled-bear"] = _bear("forest", "#1e1c1c", "#e8d0a0", chest="#e8d0a0", mask="#e8d0a0")
