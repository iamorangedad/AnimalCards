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
# ---- batch p5_sea1 ----
_ceta = _a4._ceta; _sea = _a4._sea; _cuttle = _a4._cuttle; _ray = _a5._ray; _flat = _a5._flat
def _fs(F, L=320, H=120, box=(.58, 600, 280), pre="", post="", kind="sea", **kw):
    return lambda w, h: scene(kind, w, h, pre + fish(F=F, L=L, H=H, **kw) + post, box=(w / 2, h * box[0], box[1], box[2]))
ART6["n-elephant-seal"] = lambda w, h: coast(w, h, pinniped("#7a6e66", L=440, up=0.5, belly="#9a8e84") + E(-214, -150, 36, 26, "#6a5e56", 2.6) + P("M-236 -132 q-8 20 6 34", sw=3), (w / 2, h * .66, 640, 330), rocky=False)
ART6["sa-fur-seal"] = lambda w, h: coast(w, h, pinniped("#5a4a3e", L=320, up=0.6, ears=True, belly="#7a6a5a"), (w / 2, h * .66, 540, 320))
ART6["risso"] = _ceta("#9aa0a6", 400, 120, belly="#c9ced2", box=None, tall=True, extras="".join(P(f"M{x} {y} l{dx} {dy}", sw=3, col="#f4f6f8") for x, y, dx, dy in [(-140, -30, 40, 10), (-90, -40, 50, -6), (-30, -20, 44, 16), (20, -44, 50, 4), (70, -20, 36, 12), (-110, 0, 30, -10), (0, 4, 40, -8)]))
ART6["brydes"] = _ceta("#3a4250", 520, 110, belly="#dfe4ea", box=None, extras="".join(P(f"M-250 {y} C-210 {y-4} -170 {y-6} -130 {y-4}", sw=3, col="#6a7280") for y in (-30, -16, -2)))
ART6["blacktip"] = _fs("#9a9488", 420, 120, tail="shark", tail_col="#9a9488", belly="#eef0f0", gills=5, eye_r=6, mouth=False, fin_col="#1a1a1e", post=P("M300 -40 L330 -70 L340 -40 Z", "#1a1a1e", 0))
ART6["lemon-shark"] = _fs("#c9b46a", 440, 130, tail="shark", belly="#efe6c0", gills=5, eye_r=6, mouth=False, fin_col="#a8944a")
def _saw():
    t = "".join(P(f"M{-220-i*16} -6 l-4 -12 M{-220-i*16} 6 l-4 12", sw=3, col="#f4f0e6") for i in range(10))
    return P("M-200 -12 L-390 -8 L-390 8 L-200 12 Z", "#8a7e6a", 2.6) + t
ART6["sawfish"] = _fs("#8a7e6a", 420, 100, pre=_saw(), tail="shark", belly="#d9d2c4", gills=5, eye_r=6, mouth=False, fin_col="#6a5e4a", box=(.58, 680, 280))
ART6["giant-grouper"] = _fs("#5a4a32", 400, 190, tail="round", belly="#7a6a4a", eye_r=8, mouth=True, fin_col="#e8c23a", spots="#e8d8a0", box=(.6, 600, 360))
ART6["parrotfish"] = _fs("#3a7a6a", 360, 200, tail="round", belly="#5a9a8a", eye_r=8, mouth=True, fin_col="#2a5a4a", post=E(-150, -80, 46, 40, "#4a8a7a", 2.8) + P("M-196 6 l-10 0", sw=6, col="#f4f0e0"), box=(.6, 600, 360))
def _porcu(w, h):
    o = "".join(P(f"M{math.cos(a/16*2*math.pi)*120:.0f} {-90+math.sin(a/16*2*math.pi)*110:.0f} l{math.cos(a/16*2*math.pi)*34:.0f} {math.sin(a/16*2*math.pi)*34:.0f}", sw=5) for a in range(16))
    o += E(0, -90, 130, 118, "#d9c9a0", 3) + "".join(C(x, y, 7, "#3a3020", 0) for x, y in [(-40, -160), (20, -170), (70, -140), (-80, -120), (40, -110), (90, -90), (-20, -130)])
    o += E(-10, -40, 90, 50, "#f4efe2", 0) + C(-70, -110, 22, "#fff", 2.6) + C(-74, -110, 11, INK, 0) + P("M130 -100 L190 -140 L190 -50 Z", "#c9b98a", 2.8) + E(-128, -70, 10, 8, "#f4efe2", 2.4)
    return scene("sea", w, h, o, box=(w / 2, h * .72, 460, 420))
ART6["porcupinefish"] = _porcu
ART6["picasso-trigger"] = _fs("#e8e2d0", 280, 160, tail="round", belly="#f6f2e6", eye_r=8, fin_col="#d9d0b8", stripes=("#2a3a5a", [.42, .55]),
                              post=P("M-60 -60 L40 30", sw=10, col="#3a8ac8") + P("M-60 -40 L30 40", sw=4, col="#f2c83a") + P("M-150 4 L-60 6", sw=6, col="#3a8ac8") + P("M60 -30 l40 30 l-40 30", sw=6, col="#2a2a2a"), box=(.6, 520, 340))
ART6["flying-fish"] = _fs("#2a5aa8", 300, 80, tail="fork", belly="#eef2f6", eye_r=8, fin_col="#9aa6b4", box=(.5, 600, 320),
                          pre=P("M-60 -10 C-20 -140 80 -190 160 -170 C80 -120 40 -60 20 -10 Z", "#b9c4d0", 2.6, extra='fill-opacity=".9"'))
ART6["dwarf-seahorse"] = _recol(_a3.a_seahorse, [("#e8b84a", "#c9b86a"), ("#c99a30", "#9a8a4a")])
def _seahare(w, h):
    o = P("M-200 -20 C-180 -120 120 -150 220 -40 C160 0 -120 10 -200 -20 Z", "#7a5a3a", 3) + "".join(C(x, y, 8, "#a8845a", 0) for x, y in [(-60, -80), (20, -100), (100, -70), (-120, -50), (40, -50)])
    o += P("M-180 -60 C-200 -120 -190 -140 -176 -150", sw=12) + P("M-180 -60 C-200 -120 -190 -140 -176 -150", sw=7, col="#7a5a3a")
    o += P("M-150 -80 C-160 -140 -150 -160 -136 -166", sw=12) + P("M-150 -80 C-160 -140 -150 -160 -136 -166", sw=7, col="#7a5a3a") + C(-176, -80, 6, INK, 0)
    o += "".join(E(x, y, r, r, "#8a4aa8", 0, extra='fill-opacity=".55"') for x, y, r in [(240, -60, 40), (280, -100, 30), (260, -20, 28)])
    return scene("sea", w, h, o, box=(w / 2, h * .74, 560, 260))
ART6["sea-hare"] = _seahare
def _sanddollar(w, h):
    o = E(0, -40, 190, 80, "#a8708a", 3) + "".join(P(f"M0 -40 L{math.cos(a)*90:.0f} {-40+math.sin(a)*38:.0f}", sw=14, col="#c99aac") for a in [-math.pi/2 + i*2*math.pi/5 for i in range(5)])
    o += C(0, -40, 10, "#7a4a5a", 0) + E(170, 40, 60, 22, "#f4f0e6", 2.4)
    return scene("deep", w, h, o, box=(w / 2, h * .74, 480, 220))
ART6["sand-dollar"] = _sanddollar
ART6["sardine"] = lambda w, h: scene("sea", w, h, "".join(G_(fish(F="#3a5a7a", L=220, H=60, tail="fork", belly="#eef2f6", eye_r=7, fin_col="#5a7a9a", spots="#2a3a4a"), x, y) for x, y in [(-120, -160), (100, -110), (-60, -20), (140, 20)]), box=(w / 2, h * .62, 560, 340))
ART6["mahi-mahi"] = _fs("#2a9a6a", 400, 140, tail="fork", tail_col="#e8c23a", belly="#f2d84a", eye_r=8, fin_col="#2a6aa8", dorsal_col="#2a6aa8", tall_dorsal=True, spots="#2a5aa8",
                        pre=E(-160, -30, 50, 60, "#2a9a6a", 2.8))
ART6["albacore"] = _fs("#2a3a5a", 400, 140, tail="fork", belly="#e2e8ee", eye_r=8, mouth=True, fin_col="#3a4a6a", post=P("M-60 0 C20 10 120 30 180 40", sw=14, col="#3a4a6a"))
ART6["wahoo"] = _fs("#3a5a8a", 480, 80, tail="fork", belly="#dfe6ee", eye_r=6, mouth=True, fin_col="#2a3a5a", stripes=("#24345a", [.25, .33, .41, .49, .57, .65, .73]), box=(.58, 660, 240))
ART6["halibut"] = _recol(_flat, [("#a89a7a", "#6a5a44"), ("#7a6a4a", "#4a3e2e")])
ART6["wolffish"] = _fs("#6a7078", 400, 120, tail="round", belly="#a8aeb4", eye_r=8, mouth=False, fin_col="#5a6068", spots="#3a3e44",
                       post=P("M-200 0 L-170 -6 L-170 14 Z", "#f6f2e6", 2) + P("M-196 -4 l4 10 M-188 -4 l4 10 M-180 -4 l4 10", sw=2.4))
ART6["ribbontail"] = lambda w, h: scene("sea", w, h, G_(E(0, -40, 170, 120, "#c9a46a", 3) + "".join(C(x, y, 9, "#3a8ae8", 0) for x, y in [(-90, -80), (-30, -110), (40, -100), (100, -60), (-110, -10), (-40, -40), (30, -30), (90, 0), (-60, 30), (20, 30)]) +
                                                    P("M160 -40 C240 -40 300 -30 380 -20", sw=10, col="#c9a46a") + P("M220 -40 C260 -60 300 -40 330 -26", sw=6, col="#3a8ae8") + C(-120, -100, 12, "#fff", 2.4) + C(-120, -100, 6, INK, 0) + C(-80, -126, 12, "#fff", 2.4) + C(-80, -126, 6, INK, 0), -60, 0), box=(w / 2, h * .66, 620, 280))
ART6["zebra-shark"] = _fs("#d9c9a0", 360, 120, tail="shark", belly="#efe6d0", gills=5, eye_r=6, mouth=False, fin_col="#b8a87a", spots="#3a3020",
                          post=P("M150 0 C220 -10 300 -20 380 0 C300 20 220 30 150 20 Z", "#d9c9a0", 2.6) + "".join(C(x, 6, 7, "#3a3020", 0) for x in (200, 250, 300, 340)), box=(.58, 680, 280))
def _wobbe(w, h):
    f = fish(F="#8a7a5a", L=440, H=90, tail="shark", belly="#a89a7a", gills=5, eye_r=5, mouth=False, fin_col="#6a5a3a", spots="#5a4a30")
    t = "".join(P(f"M{-220+i*6} {30+(i%3)*4} l{-10+(i%4)*4} 22", sw=4, col="#6a5a3a") for i in range(12)) + "".join(P(f"M{-216+i*8} -30 l-6 -16", sw=4, col="#6a5a3a") for i in range(6))
    return scene("sea", w, h, rock(160, 80, 1.2) + G_(f + t, 0, 0), box=(w / 2, h * .66, 620, 260))
ART6["wobbegong"] = _wobbe
def _cots(w, h):
    o = []
    n = 16
    for i in range(n):
        a = 2 * math.pi * i / n
        x, y = math.cos(a) * 170, math.sin(a) * 170 * .5 - 90
        o.append(P(f"M{math.cos(a)*50:.0f} {-90+math.sin(a)*25:.0f} L{x:.0f} {y:.0f}", sw=30, col=INK) + P(f"M{math.cos(a)*50:.0f} {-90+math.sin(a)*25:.0f} L{x:.0f} {y:.0f}", sw=22, col="#8a6aa0"))
    o.append(E(0, -90, 80, 44, "#8a6aa0", 3))
    import random
    r = random.Random(3)
    for _ in range(60):
        a = r.uniform(0, 2 * math.pi); rr = r.uniform(20, 160)
        x, y = math.cos(a) * rr, -90 + math.sin(a) * rr * .5
        o.append(P(f"M{x:.0f} {y:.0f} l{r.uniform(-4,4):.0f} -16", sw=3, col="#e8c23a"))
    return scene("sea", w, h, "".join(o), box=(w / 2, h * .8, 460, 240))
ART6["cots"] = _cots
ART6["anemone"] = _recol(_a3.a_clownfish, [("#e7a9c8", "#f2e6b0"), ("#c97aa0", "#d94a5a")])
def _brain(w, h):
    o = P("M-200 0 C-200 -180 200 -180 200 0 Z", "#c9b06a", 3)
    for k in range(6):
        y = -20 - k * 22
        wdt = math.sqrt(max(0, 1 - ((k * 22 + 20) / 140) ** 2)) * 190
        o += P(wavy(-wdt, y, 2 * wdt, 10, 8, int(4 + wdt / 30)), "none", 0) if False else P(" ".join(["M%.0f %.0f" % (-wdt, y)] + ["Q%.0f %.0f %.0f %.0f" % (-wdt + (j + .5) * 2 * wdt / 10, y + (12 if j % 2 else -12), -wdt + (j + 1) * 2 * wdt / 10, y) for j in range(10)]), sw=4, col="#8a7038")
    return scene("sea", w, h, o, box=(w / 2, h * .8, 460, 220))
ART6["brain-coral"] = _brain
def _bdragon(w, h):
    o = P("M-180 0 C-120 -30 120 -30 200 -6 C120 10 -120 16 -180 0 Z", "#2a6ad8", 3) + P("M-150 -2 C-80 -14 80 -14 170 -4", sw=4, col="#bcd4f6")
    for x, s in ((-80, 1), (0, 1.1), (90, .9)):
        for sg in (-1, 1):
            o += "".join(P(f"M{x} {sg*6} L{x+dx} {sg*(40+abs(dx)//2)*s:.0f}", sw=6, col="#2a6ad8") for dx in (-30, -10, 10, 30))
    o += P("M-180 0 l-20 -16 M-180 0 l-20 16", sw=4, col="#2a6ad8")
    return scene("sea", w, h, G_(o, 0, -240), box=(w / 2, h * .6, 520, 280))
ART6["blue-dragon"] = _bdragon
def _sdancer(w, h):
    o = P("M-220 -40 C-200 -140 -100 -170 0 -130 C100 -170 200 -140 230 -40 C180 10 100 -20 0 10 C-100 -20 -180 10 -220 -40 Z", "#d92a3a", 3)
    o += P("M-200 -50 C-160 -110 -80 -130 0 -104 C80 -130 160 -110 210 -50", sw=8, col="#f4e6e6") + "".join(C(x, y, 6, "#f4e6e6", 0) for x, y in [(-60, -80), (40, -76), (120, -70), (-130, -70)])
    o += P("M-200 -70 l-20 -40 M-180 -80 l-6 -44", sw=8, col="#b8202e") + P("M200 -60 C230 -100 250 -80 240 -50", "#f2a03a", 2.4)
    return scene("sea", w, h, o, box=(w / 2, h * .66, 560, 280))
ART6["spanish-dancer"] = _sdancer
ART6["flamboyant"] = _recol(_cuttle, [("#c9a07a", "#5a3a2a"), ("#e8d4b8", "#f2c83a"), ("#7a5a3a", "#d94a8a")])
# ---- batch p5_bird1 ----
def _crest_gold(x, y, r):
    return "".join(P(f"M{x} {y-r*.8} l{dx} {-r*1.2}", sw=4, col="#e8c23a") + C(x + dx, y - r * 2.0, 4, "#e8c23a", 0) for dx in (-18, -8, 2, 12, 22))
ART6["crowned-crane"] = B("savanna", (.8, 480, 420), F="#8a929a", wing="#f4f2ee", rx=80, ry=50, tilt=-12, neck=90, nw=22, hr=24, beak="short", beak_col="#2a2a2a", leg_len=180, leg_col="#2a2a2a", legw=5,
                          tail="short", tail_col="#7a3a2a", head_col="#1f1f22", front_fn=lambda x, y, r: _crest_gold(x, y, r) + E(x + r * .1, y + r * .2, r * .4, r * .3, "#ffffff", 0) + C(x - r * .2, y + r * 1.0, r * .3, "#d8302a", 0))
ART6["whooping"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#ffffff", rx=86, ry=52, tilt=-10, neck=110, nw=22, hr=24, beak="long", beak_col="#c9a03a", leg_len=190, leg_col="#2a2a2a", legw=5,
                     tail="short", tail_col="#2a2a2a", head_col="#ffffff", front_fn=lambda x, y, r: E(x - r * .1, y - r * .5, r * .6, r * .3, "#d8302a", 0) + E(x - r * .5, y + r * .2, r * .4, r * .25, "#2a2a2a", 0))
ART6["sarus"] = B("wetland", (.8, 480, 420), F="#9aa2aa", wing="#8a929a", rx=88, ry=52, tilt=-10, neck=120, nw=22, hr=24, beak="long", beak_col="#6a6a5a", leg_len=200, leg_col="#d8a0a0", legw=5,
                  tail="short", tail_col="#8a929a", head_col="#d84a3a", front_fn=lambda x, y, r: C(x, y - r * .4, r * .5, "#b9c0c6", 0))
ART6["bf-spoonbill"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#f4f2ee", rx=84, ry=50, tilt=-12, neck=70, nw=24, hr=24, beak="long", beak_col="#1f1f22", leg_len=150, leg_col="#1f1f22", legw=5, tail="short", tail_col="#ffffff",
                         head_col="#ffffff", front_fn=lambda x, y, r: E(x - r * 3.1, y + r * .1, r * .6, r * .4, "#1f1f22", 2.4) + E(x - r * .5, y, r * .6, r * .5, "#1f1f22", 0))
ART6["little-egret"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#f6f6f4", rx=70, ry=42, tilt=-14, neck=120, nw=18, hr=20, beak="long", beak_col="#1f1f22", leg_len=180, leg_col="#1f1f22", legw=4, tail="short", tail_col="#ffffff",
                         front_fn=lambda x, y, r: P(f"M{x} {y-r*.4} C{x+r*1.5} {y-r*1.2} {x+r*2.5} {y-r*.6} {x+r*3.2} {y+r*.2}", sw=3, col="#d9d9d4"))
ART6["marabou"] = B("savanna", (.8, 480, 420), F="#3a3e44", wing="#2a2e34", rx=92, ry=58, tilt=-8, neck=50, nw=34, hr=26, beak="long", beak_col="#d8c8a8", leg_len=170, leg_col="#e8e2d8", legw=6, tail="short", tail_col="#2a2e34",
                    head_col="#e8a8a0", belly="#ffffff", front_fn=lambda x, y, r: E(x + r * .4, y + r * 2.0, r * .7, r * .9, "#e8a8a0", 2.4))
ART6["griffon"] = B("plateau", (.78, 520, 420), pre=G_(rock(0, 0, 2.2), 0, 0), F="#b8925a", wing="#5a3e2a", rx=96, ry=64, tilt=-22, neck=30, nw=40, hr=28, beak="hook", beak_col="#c9c0a8", leg_len=40, leg_col="#8a8a8a", legw=7,
                    tail="short", tail_col="#4a3222", head_col="#f2ece0", front_fn=lambda x, y, r: E(x + r * .6, y + r * 1.4, r * 1.3, r * .45, "#f6f2e8", 2.4))
ART6["cattle-egret"] = B("farm", (.8, 480, 400), F="#ffffff", wing="#f6f6f4", rx=70, ry=46, tilt=-14, neck=40, nw=26, hr=24, beak="long", beak_col="#e8c23a", leg_len=110, leg_col="#c9b07a", legw=5, tail="short", tail_col="#ffffff",
                         head_col="#f2c08a", front_fn=lambda x, y, r: E(x + r * .8, y + r * 1.6, r * .9, r * .5, "#f2c08a", 0))
ART6["lb-crow"] = BP("forest", F="#1f1f26", wing="#2a2a36", rx=72, ry=46, tilt=-24, neck=10, nw=44, hr=32, beak="short", beak_col="#1f1f26", leg_len=30, leg_col=INK, legw=5, tail="long", tail_col="#1f1f26",
                     front_fn=lambda x, y, r: P(f"M{x-r*.7} {y-r*.5} C{x-r*1.6} {y-r*.6} {x-r*2.2} {y} {x-r*2.3} {y+r*.2} L{x-r*.7} {y+r*.5} Z", "#1f1f26", 2.4))
ART6["bowerbird"] = B("rainforest", (.78, 480, 380), pre="".join(P(f"M{-200+i*8} 0 L{-210+i*8} -90", sw=3, col="#8a6a3a") for i in range(8)) + "".join(C(x, 4, 8, "#3a6ad8", 1.6) for x in (-120, -96, 70, 100, 130)),
                      F="#2a2a5a", wing="#1f1f4a", rx=60, ry=40, tilt=-20, neck=8, nw=36, hr=28, beak="short", beak_col="#e8e0a8", leg_len=30, leg_col="#e8e0a8", legw=4, tail="long", tail_col="#1f1f4a",
                      front_fn=lambda x, y, r: C(x - r * .2, y - r * .1, r * .28, "#6a5ad8", 0))
def _bayanest(w, h):
    o = P("M-40 -280 C-40 -240 -80 -200 -80 -130 C-80 -60 -30 -40 0 -40 C30 -40 80 -60 80 -130 C80 -200 40 -240 40 -280 Z", "#c9b06a", 3) + "".join(P(f"M{-70+i*12} -60 C{-60+i*12} -150 {-40+i*8} -220 {-20+i*4} -270", sw=2, col="#a8904a") for i in range(12))
    o += P("M-20 -40 L-20 40 C-20 60 20 60 20 40 L20 -40", "#c9b06a", 2.6) + P("M-160 -290 L160 -290", sw=8, col="#7a5a3a")
    b = bird(F="#e8c83a", wing="#8a6a3a", rx=40, ry=28, tilt=-20, neck=4, nw=28, hr=20, beak="cone", beak_col="#3a2a1a", leg_len=14, leg_col="#c9a07a", legw=3, tail="short", tail_col="#6a5030", head_col="#e8c83a")
    return scene("savanna", w, h, o + G_(b, 120, -120), box=(w / 2, h * .9, 440, 420))
ART6["baya"] = _bayanest
def _beehummer(w, h):
    flower = P("M60 0 L60 -150", sw=6, col="#3f7a3a") + "".join(E(60 + math.cos(a) * 30, -170 + math.sin(a) * 30, 22, 14, "#e85a8a", 2.4) for a in [i * 1.256 for i in range(5)]) + C(60, -170, 12, "#f2c83a", 2)
    b = E(-80, -190, 34, 22, "#5a9a6a", 2.6) + C(-112, -204, 16, "#d8304a", 2.4) + C(-116, -206, 4, INK, 0) + P("M-126 -204 L-168 -196", sw=3, col=INK) + E(-70, -230, 40, 12, "#cfe0f0", 2, extra='fill-opacity=".8"') + P("M-50 -186 L-10 -176 L-40 -170 Z", "#3a6a4a", 2)
    return scene("rainforest", w, h, flower + b, box=(w / 2, h * .8, 420, 360))
ART6["bee-hummer"] = _beehummer
ART6["gannet"] = B("sea", (.74, 460, 420), pre=G_(rock(0, 0, 1.8), 0, 0), F="#ffffff", wing="#f6f6f4", rx=80, ry=46, tilt=-24, neck=30, nw=30, hr=26, beak="long", beak_col="#9aa6b4", leg_len=30, leg_col="#3a3a3a", legw=5,
                   tail="short", tail_col="#ffffff", head_col="#f2d88a", front_fn=lambda x, y, r: P(f"M{x+r*1.8} {y+r*2.8} l{r*1.6} {r*.4}", sw=10, col="#1f1f22"))
ART6["great-frigate"] = B("sea", (.74, 460, 420), pre=G_(rock(0, 0, 1.8), 0, 0), F="#1f1f26", wing="#2a2a36", rx=80, ry=44, tilt=-20, neck=14, nw=30, hr=24, beak="long", beak_col="#8a8a8a", leg_len=24, leg_col="#3a3a3a", legw=4,
                          tail="fork", tail_col="#1f1f26", front_fn=lambda x, y, r: E(x + r * .2, y + r * 2.0, r * 1.0, r * 1.1, "#e8302a", 2.6))
ART6["grebe"] = B("pond", (.74, 460, 360), F="#8a6a4a", wing="#5a4a3a", rx=88, ry=44, tilt=-4, neck=60, nw=24, hr=24, beak="long", beak_col="#d88a8a", leg_len=0, sit=True, tail="short", tail_col="#5a4a3a",
                  head_col="#ffffff", belly="#f6f2ea", front_fn=lambda x, y, r: P(f"M{x} {y-r*.8} l{r*.6} {-r*.9} l{r*.4} {r*.9}", "#1f1f22", 2) + E(x + r * .8, y + r * .6, r * .5, r * .8, "#c9602a", 0))
ART6["coot"] = B("pond", (.74, 460, 360), F="#2a2a2e", wing="#1f1f22", rx=84, ry=48, tilt=-4, neck=24, nw=38, hr=28, beak="short", beak_col="#ffffff", leg_len=0, sit=True, tail="short", tail_col="#1f1f22",
                 front_fn=lambda x, y, r: E(x - r * .6, y - r * .4, r * .25, r * .4, "#ffffff", 0))
ART6["green-peafowl"] = B("forest", (.8, 500, 400), F="#2a7a5a", wing="#8a6a3a", rx=80, ry=50, tilt=-14, neck=60, nw=26, hr=22, beak="short", beak_col="#6a6a5a", leg_len=90, leg_col="#8a8a8a", legw=5,
                          tail="long", tail_col="#2a6a4a", head_col="#2a8a6a", front_fn=lambda x, y, r: P(f"M{x} {y-r} l0 {-r*1.2}", sw=4, col="#2a8a6a") + C(x, y - r * 2.2, 6, "#2a8a6a", 0) + E(x - r * .2, y + r * .1, r * .4, r * .3, "#f2c83a", 0))
ART6["nightjar"] = lambda w, h: scene("forest", w, h, branch(-200, 200, 5) + G_(E(0, -40, 110, 34, "#8a7a6a", 3) + "".join(P(f"M{x} {-50+(x%3)*6} l14 6", sw=3, col="#4a3e30") for x in range(-80, 90, 18)) +
                                                                            C(-100, -54, 28, "#8a7a6a", 2.6) + P("M-114 -60 q8 -6 16 0", sw=3, col=INK) + P("M120 -40 L190 -30 L120 -20 Z", "#7a6a5a", 2.4) + P("M-130 -46 l-10 4", sw=3, col=INK), 0, -6), box=(w / 2, h * .62, 460, 260))
ART6["bn-oriole"] = BP("forest", F="#f2c83a", wing="#1f1f22", rx=58, ry=40, tilt=-20, neck=6, nw=38, hr=28, beak="short", beak_col="#e88aa0", leg_len=22, leg_col="#6a6a6a", legw=4, tail="short", tail_col="#1f1f22",
                       head_col="#f2c83a", front_fn=lambda x, y, r: P(f"M{x-r*.9} {y-r*.1} L{x+r*1.3} {y+r*.1}", sw=r * .35, col="#1f1f22"))
ART6["bird-of-paradise"] = B("rainforest", (.66, 460, 380), F="#7a4a2a", wing="#6a3a22", rx=58, ry=40, tilt=-20, neck=8, nw=38, hr=28, beak="short", beak_col="#9ab0c8", leg_len=22, leg_col="#9aa0a8", legw=4, tail="short", tail_col="#6a3a22",
                              head_col="#f2d83a", pre=branch(-150, 150, 4) + "".join(P(f"M40 -120 C{120+i*20} {-200+i*20} {200+i*30} {-120+i*30} {260+i*20} {-40+i*30}", sw=6, col="#f2c83a") for i in range(6)) + P("M40 -110 C150 -60 200 40 260 90", sw=2, col=INK),
                              front_fn=lambda x, y, r: E(x + r * .2, y + r * .9, r * .7, r * .4, "#3a8a4a", 0))
ART6["hyacinth-macaw"] = BP("rainforest", F="#2a3aa8", wing="#1f2f8a", rx=58, ry=46, tilt=-50, neck=6, nw=44, hr=32, beak="hook", beak_col="#2a2a2e", leg_len=24, leg_col="#3a3a3a", legw=5, tail="long", tail_col="#1f2f8a",
                            front_fn=lambda x, y, r: C(x - r * .1, y - r * .1, r * .35, "#f2d83a", 0) + E(x - r * .9, y + r * .6, r * .4, r * .2, "#f2d83a", 0))
ART6["keel-toucan"] = BP("rainforest", F="#1f1f22", wing="#1f1f22", rx=58, ry=44, tilt=-50, neck=6, nw=42, hr=30, beak="short", beak_col="#1f1f22", leg_len=24, leg_col="#5a6a9a", legw=5, tail="long", tail_col="#1f1f22",
                         front_fn=lambda x, y, r: P(f"M{x-r*.6} {y-r*.6} C{x-r*2.6} {y-r*.9} {x-r*3.4} {y-r*.2} {x-r*3.4} {y+r*.2} C{x-r*2.6} {y+r*.4} {x-r*1.4} {y+r*.4} {x-r*.6} {y+r*.4} Z", "#7ac83a", 2.6)
                                                  + P(f"M{x-r*1.6} {y-r*.7} L{x-r*1.9} {y+r*.4}", sw=r * .35, col="#e8802a") + P(f"M{x-r*2.6} {y-r*.6} L{x-r*2.8} {y+r*.3}", sw=r * .3, col="#d8302a") + E(x + r * .1, y + r * 1.2, r * .8, r * .5, "#f2d83a", 0))
ART6["moorhen"] = B("pond", (.74, 460, 360), F="#2a2e3a", wing="#4a4a3a", rx=80, ry=46, tilt=-6, neck=24, nw=36, hr=26, beak="short", beak_col="#d8302a", leg_len=0, sit=True, tail="up", tail_col="#1f1f22",
                    front_fn=lambda x, y, r: E(x - r * .6, y - r * .4, r * .25, r * .4, "#d8302a", 0) + P(f"M{x+r*1.2} {y+r*2.2} l{r*2.0} {r*.2}", sw=4, col="#ffffff"))
ART6["greylag"] = B("pond", (.74, 460, 360), F="#9a948a", wing="#7a746a", rx=100, ry=52, tilt=-4, neck=50, nw=34, hr=28, beak="duck", beak_col="#e8802a", leg_len=0, sit=True, tail="up", tail_col="#6a645a", belly="#d8d2c8")
ART6["pintail"] = B("pond", (.74, 460, 360), F="#c9c6c0", wing="#8a8680", rx=96, ry=46, tilt=-4, neck=44, nw=28, hr=26, beak="duck", beak_col="#4a5a6a", leg_len=0, sit=True, tail="up", tail_col="#1f1f22",
                    head_col="#6a4a32", belly="#f6f4f0", post=P("M120 -70 L230 -150", sw=5, col="#1f1f22"), front_fn=lambda x, y, r: P(f"M{x+r*.6} {y+r*.6} l{r*.2} {r*1.6}", sw=5, col="#ffffff"))
ART6["wood-duck"] = B("pond", (.74, 460, 360), F="#8a5a3a", wing="#2a4a5a", rx=92, ry=48, tilt=-4, neck=20, nw=38, hr=34, beak="duck", beak_col="#d8302a", leg_len=0, sit=True, tail="up", tail_col="#1f2a3a",
                      head_col="#2a6a4a", belly="#e8d8b0", front_fn=lambda x, y, r: P(f"M{x-r*.6} {y-r*.6} C{x} {y-r*.9} {x+r} {y-r*.6} {x+r*1.6} {y}", sw=3, col="#ffffff") + C(x - r * .3, y - r * .1, r * .2, "#d8302a", 0)
                      + P(f"M{x-r*.6} {y+r*.4} C{x} {y+r*.7} {x+r*.6} {y+r*.6} {x+r*1.0} {y+r*.3}", sw=3, col="#ffffff"))
ART6["shelduck"] = B("wetland", (.78, 460, 380), F="#ffffff", wing="#f6f6f4", rx=90, ry=48, tilt=-6, neck=40, nw=30, hr=26, beak="duck", beak_col="#d8304a", leg_len=40, leg_col="#e8a0a0", legw=5, tail="short", tail_col="#1f1f22",
                     head_col="#1f3a2a", front_fn=lambda x, y, r: P(f"M{x+r*.6} {y+r*1.6} C{x+r*1.6} {y+r*2.0} {x+r*2.6} {y+r*2.2} {x+r*3.4} {y+r*2.0}", sw=r * .6, col="#b8602a"))
ART6["avocet"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#1f1f22", rx=70, ry=40, tilt=-10, neck=50, nw=20, hr=22, beak="needle", beak_col="#1f1f22", leg_len=140, leg_col="#8ab0d0", legw=4, tail="short", tail_col="#ffffff",
                   head_col="#ffffff", front_fn=lambda x, y, r: E(x + r * .2, y - r * .4, r * .9, r * .5, "#1f1f22", 0) + P(f"M{x-r} {y+r*.2} C{x-r*2.2} {y+r*.2} {x-r*3.0} {y-r*.2} {x-r*3.4} {y-r*.9}", sw=4, col="#1f1f22"))
ART6["stilt"] = B("wetland", (.8, 480, 420), F="#ffffff", wing="#1f1f22", rx=64, ry=38, tilt=-10, neck=40, nw=20, hr=20, beak="needle", beak_col="#1f1f22", leg_len=210, leg_col="#e86a8a", legw=4, tail="short", tail_col="#f6f6f4", head_col="#ffffff")
ART6["curlew"] = B("wetland", (.8, 480, 420), F="#a8906a", wing="#8a7450", rx=72, ry=46, tilt=-10, neck=40, nw=24, hr=22, beak="needle", beak_col="#3a2a1a", leg_len=110, leg_col="#7a8a9a", legw=4, tail="short", tail_col="#8a7450",
                   front_fn=lambda x, y, r: P(f"M{x-r} {y+r*.1} C{x-r*2.4} {y+r*.2} {x-r*3.6} {y+r*.9} {x-r*4.4} {y+r*2.0}", sw=5, col="#3a2a1a") + "".join(C(x + r * (1 + i * .6), y + r * (2 + (i % 2)), 3, "#5a4a30", 0) for i in range(6)))
ART6["godwit"] = B("wetland", (.8, 480, 420), F="#c9603a", wing="#8a6a4a", rx=72, ry=44, tilt=-10, neck=40, nw=24, hr=22, beak="needle", beak_col="#d88a8a", leg_len=110, leg_col="#3a3a3a", legw=4, tail="short", tail_col="#8a6a4a",
                   front_fn=lambda x, y, r: P(f"M{x-r} {y+r*.1} C{x-r*2.4} {y} {x-r*3.6} {y-r*.3} {x-r*4.4} {y-r*.7}", sw=5, col="#5a3a3a"))
ART6["red-knot"] = B("wetland", (.8, 460, 380), F="#c9704a", wing="#8a8a8a", rx=62, ry=42, tilt=-10, neck=20, nw=30, hr=22, beak="long", beak_col="#2a2a2a", leg_len=70, leg_col="#4a4a4a", legw=4, tail="short", tail_col="#7a7a7a")
ART6["herring-gull"] = B("sea", (.74, 440, 420), pre=G_(rock(0, 0, 1.8), 0, 0), F="#ffffff", wing="#a8b4c0", rx=78, ry=46, tilt=-14, neck=20, nw=36, hr=28, beak="short", beak_col="#f2c83a", leg_len=50, leg_col="#e8b0a8", legw=5,
                         tail="short", tail_col="#1f1f22", front_fn=lambda x, y, r: C(x - r * 1.3, y + r * .4, 4, "#d8302a", 0))
ART6["bh-gull"] = B("pond", (.74, 440, 400), F="#ffffff", wing="#c9d0d8", rx=70, ry=42, tilt=-12, neck=16, nw=32, hr=26, beak="short", beak_col="#c8202a", leg_len=40, leg_col="#c8202a", legw=4, tail="short", tail_col="#1f1f22",
                    head_col="#4a3a32")
ART6["burrowing-owl"] = lambda w, h: scene("savanna", w, h, E(120, 10, 80, 30, "#5a4a3a", 0) + G_(bird(F="#a8845a", wing="#8a6a44", rx=50, ry=60, tilt=-80, neck=4, nw=52, hr=40, beak="hook", beak_col="#c9b88a", leg_len=70, leg_col="#c9b88a", legw=4, tail="short", tail_col="#8a6a44",
                                                                                     front="".join(C(x, y, 5, "#f6efe0", 0) for x, y in [(-20, -150), (10, -170), (30, -130), (-10, -110)])), -40, 0), box=(w / 2, h * .76, 420, 380))
ART6["goshawk"] = B("forest", (.78, 480, 420), pre=branch(-180, 180, 5), F="#8a929a", wing="#5a6470", rx=80, ry=56, tilt=-26, neck=14, nw=46, hr=34, beak="hook", beak_col="#3a3a3a", leg_len=40, leg_col="#f2c53a", legw=6,
                    tail="long", tail_col="#5a6470", belly="#e8eaec", front_fn=lambda x, y, r: P(f"M{x-r*.6} {y-r*.3} L{x+r*1.2} {y-r*.2}", sw=4, col="#ffffff") + C(x - r * .3, y, r * .2, "#e8802a", 0))
ART6["stellers-eagle"] = B("snow", (.78, 520, 420), pre=G_(rock(0, 0, 2.2), 0, 0), F="#3a2e26", wing="#ffffff", rx=96, ry=64, tilt=-22, neck=24, nw=56, hr=40, beak="hook", beak_col="#f2c83a", leg_len=40, leg_col="#f2c83a", legw=7,
                           tail="short", tail_col="#ffffff", head_col="#3a2e26", front_fn=lambda x, y, r: E(x - r * .9, y + r * .1, r * .7, r * .5, "#f2c83a", 2.4))
ART6["serpent-eagle"] = B("forest", (.78, 480, 420), pre=branch(-180, 180, 5), F="#6a4a32", wing="#4a3222", rx=80, ry=56, tilt=-26, neck=14, nw=46, hr=34, beak="hook", beak_col="#6a6a6a", leg_len=40, leg_col="#f2c53a", legw=6,
                          tail="short", tail_col="#2a2a2a", belly="#9a7a52", front_fn=lambda x, y, r: E(x - r * .5, y, r * .4, r * .3, "#f2d83a", 0) + "".join(C(x + r * (.6 + i * .5), y + r * 2.4 + (i % 2) * 10, 4, "#f6efe0", 0) for i in range(5)))
ART6["turkey-vulture"] = B("plateau", (.78, 520, 420), pre=G_(rock(0, 0, 2.2), 0, 0), F="#2a2420", wing="#3a342e", rx=90, ry=60, tilt=-20, neck=20, nw=30, hr=22, beak="hook", beak_col="#f2ece0", leg_len=40, leg_col="#e8d8c8", legw=6,
                           tail="long", tail_col="#2a2420", head_col="#c8302a")
ART6["wood-pigeon"] = BP("forest", F="#9aa0b0", wing="#7a8090", rx=66, ry=48, tilt=-16, neck=8, nw=42, hr=26, beak="short", beak_col="#f2c83a", leg_len=24, leg_col="#d88a8a", legw=4, tail="long", tail_col="#5a6070",
                         belly="#c8a0a8", front_fn=lambda x, y, r: E(x + r * 1.0, y + r * 1.0, r * .5, r * .25, "#ffffff", 0))

# ---- batch p5_rep1 ----
ART6["pond-turtle"] = TU_("pond", shell="#2a2a24", skin="#3a3a30", L=260, H=110, scute="#e8d24a", neck=40, plastron="#e8d8a8")
ART6["siamese-croc"] = L_("wetland", F="#5a6a4a", L=320, H=58, tail=.95, snout=80, sh=26, belly="#d8d6b0", scutes="#3a4a30", legs=22, legh=30)
ART6["american-croc"] = L_("wetland", F="#8a8a5a", L=330, H=56, tail=.95, snout=96, sh=24, belly="#e8e4c0", scutes="#5a5a3a", legs=22, legh=30)
ART6["chuckwalla"] = L_("desert", (.78, 560, 260), pre=G_(rock(0, 30, 2.2), 0, 0), F="#5a4a3a", L=240, H=70, tail=.8, snout=40, sh=40, belly="#d8b07a", spots="#8a6a4a", legs=22, legh=32)
ART6["giant-day-gecko"] = L_("rainforest", (.7, 480, 280), pre=branch(-220, 220, 4, 10), F="#3ad04a", L=180, H=44, tail=1.0, snout=34, sh=30, spots="#e8402a", legs=16, legh=28)
ART6["flying-dragon"] = L_("rainforest", (.7, 520, 300), pre=branch(-240, 240, 4, 10) + P("M-60 -20 C-20 -110 60 -110 80 -20 Z", "#e8a03a", 2.4), F="#8a7a5a", L=160, H=34, tail=1.8, snout=30, sh=24, dewlap="#f2d23a", legs=14, legh=26)
ART6["five-lined"] = L_("forest", (.78, 520, 220), F="#2a2a30", L=180, H=36, tail=1.3, snout=30, sh=26, spots="#e8e0a0", legs=14, legh=22, post=P("M-140 0 L120 0", sw=3, col="#2a6ae8"))
ART6["glass-lizard"] = S_("meadow", F="#8a7a4a", pat="#4a3a22", L=.9, head_col="#8a7a4a")
ART6["coral-snake"] = S_("forest", F="#e8302a", band="#f2d23a", L=.8, head_col="#1f1f22")
ART6["sea-krait"] = S_("sea", F="#8aa0c0", band="#1f1f24", L=.8, head_col="#1f1f24")
ART6["bushmaster"] = S_("rainforest", F="#c9a06a", pat="#3a2a1a", L=1.1, head_col="#c9a06a")
ART6["pit-viper"] = lambda w, h: scene("forest", w, h, branch(-240, 240, 4, 14) + "".join(E(0, -40 - i * 4, 120 - i * 18, 26, "#4ac04a", 3) for i in range(4)) + E(120, -60, 30, 20, "#4ac04a", 3) + E(132, -66, 4, 4, "#e8302a", 0), box=(w / 2, h * .64, 520, 300))
ART6["caecilian"] = S_("rainforest", F="#3a3a44", band="#f2e8a0", L=.7, head_col="#3a3a44")
ART6["firebelly"] = FR_("pond", "#4a8a3a", "#f2502a", spots="#1f1f1a")
ART6["glass-frog"] = FR_("leaf", "#a8e86a", "#e8f2d8", spots="#f2f2c8", box=(.74, 380, 220))
ART6["indian-cobra"] = C_("savanna", "#5a4a30", pat="#e8d8a8", hood=True)
ART6["banded-krait"] = S_("wetland", F="#f2d23a", band="#1f1f22", L=.9, head_col="#1f1f22")
ART6["coastal-taipan"] = S_("savanna", F="#a8784a", L=1.0, belly="#f2e0a0", head_col="#e8d8a8")
ART6["tiger-snake"] = S_("wetland", F="#5a5a2a", band="#e8d24a", L=.9, head_col="#3a3a22")
ART6["carpet-python"] = S_("forest", F="#6a5a3a", pat="#d8c08a", L=1.2, head_col="#6a5a3a")
ART6["rainbow-boa"] = S_("rainforest", F="#c9603a", pat="#3a1f1a", L=1.1, head_col="#c9603a")
ART6["leopard-frog"] = FR_("meadow", "#6ab05a", "#f2f0e0", spots="#2a4a22")
ART6["wood-frog"] = FR_("forest", "#a87a4a", "#f2e8d0", spots="#3a2a1a")
ART6["eastern-newt"] = L_("forest", (.78, 460, 220), F="#f2702a", L=150, H=32, tail=1.1, snout=24, sh=20, spots="#e8302a", legs=14, legh=22)
ART6["spotted-sal"] = L_("forest", (.78, 520, 240), F="#2a2a3a", L=200, H=44, tail=.9, snout=30, sh=30, spots="#f2d23a", legs=18, legh=26)
ART6["titicaca-frog"] = FR_("pond", "#6a6a4a", "#c8c0a0", spots="#4a4a30", box=(.76, 480, 260), post=P("M-120 40 C-80 70 80 70 120 40", sw=6, col="#5a5a3a"))
ART6["beaded-lizard"] = L_("desert", F="#2a2420", L=260, H=58, tail=.7, snout=50, sh=36, spots="#e8c84a", legs=20, legh=30)
ART6["shingleback"] = L_("desert", (.78, 540, 240), F="#5a3a2a", L=240, H=70, tail=.35, snout=40, sh=44, spots="#d8c8a0", legs=16, legh=22)
ART6["armadillo-lizard"] = L_("desert", (.78, 480, 240), pre=G_(rock(0, 30, 2.0), 0, 0), F="#8a6a3a", L=160, H=40, tail=.9, snout=26, sh=28, crest="#6a4a22", belly="#f2e05a", legs=14, legh=24, spots="#3a2a1a")
ART6["pig-nosed"] = TU_("pond", shell="#8a8a7a", skin="#a8a090", L=280, H=100, scute="#8a8a7a", neck=40, plastron="#e8e0c8")

# ---- batch p5_ins1 ----
_mant = _a5._mant; _drag = _a5._drag
ART6["honeypot"] = lambda w, h: scene("desert", w, h, _a4._ant(F="#c9a06a", head="#8a5a2a") + E(150, -70, 70, 60, "#f2b03a", 3) + E(130, -90, 20, 14, "#fbe0a0", 0), box=(w / 2, h * .74, 460, 260))
ART6["weaver-ant"] = ANT_("rainforest", F="#e8902a", head="#d8802a", mand=True, pre=_a4.LEAF)
ART6["bull-dung"] = BE_("farm", F="#3a2a22", shine="#7a6a5a", L=.8, pre=C(220, -60, 70, "#7a5a3a", 3), post=P("M-60 -100 C-90 -150 -60 -180 -40 -190 M-60 -100 C-30 -150 -20 -170 0 -180", sw=8))
ART6["elephant-beetle"] = BE_("rainforest", F="#3a2a1a", shine="#c9a86a", horn="hercules", pre=_a4.LOG)
ART6["two-spot"] = lambda w, h: scene("meadow", w, h, _a4.LEAF + E(0, -70, 120, 90, "#e8302a", 3) + P("M0 -160 L0 20", sw=3) + C(-50, -80, 22, INK, 0) + C(50, -80, 22, INK, 0) + E(-130, -70, 34, 40, INK, 2) + C(-140, -90, 8, "#f2f2e8", 0) + C(-140, -50, 8, "#f2f2e8", 0) + antenna(-150, -100, 60, -200, 6, 3), box=(w / 2, h * .72, 460, 280))
ART6["jewel-beetle"] = BE_("forest", F="#2aa05a", shine="#e8402a", L=.9, spots="".join(P(f"M{20+i*40} -150 l0 130", sw=10, col=c) for i, c in enumerate(("#e8402a", "#3a7ae8", "#e8402a", "#f2c83a"))), pre=_a4.LOG)
ART6["giraffe-weevil"] = lambda w, h: scene("rainforest", w, h, _a4.LEAF + P("M-20 -40 C-20 -120 140 -120 150 -50 C140 -20 0 -20 -20 -40 Z", "#c8302a", 3) + P("M-20 -70 C-60 -120 -80 -180 -110 -220", sw=22) + P("M-20 -70 C-60 -120 -80 -180 -110 -220", sw=16, col="#1f1f22") + E(-120, -230, 26, 18, "#1f1f22", 3) + legs6([0, 50, 100], -30, h=36, sw=6), box=(w / 2, h * .72, 460, 320))
ART6["owl-butterfly"] = BF_("rainforest", F="#8a6a4a", F2="#6a5a4a", vein="#3a2a1a", spots="#f2d23a")
ART6["wild-silkmoth"] = BF_("forest", F="#a8907a", F2="#8a7a6a", vein="#5a4a3a", spots="#e8dcc0", moth=True)
ART6["blue-damsel"] = _drag("#2a5ab8", "#eef6fb", "#1f2a3a", "pond", thin=True)
ART6["devil-mantis"] = _mant("#e8e0d0", "#f2e8f0", "savanna", extra="".join(E(60 + i * 50, -40, 30, 14, "#e8402a", 2.4) for i in range(2)) + E(-40, -40, 50, 24, "#3a6ae8", 2.4))
ART6["hissing-roach"] = ROACH_("rainforest", F="#5a2a1a", L=1.2, pre=_a4.LOG)
ART6["backswimmer"] = SH_("pond", F="#c9b89a", L=1.0, legs_long=True)
ART6["scorpionfly"] = FLY_("forest", F="#e8a02a", stripes="#3a2a1a", ab=1.1, eye="#3a2a1a", wcol="#f2f2e8", post=P("M140 -60 C190 -100 200 -150 170 -160", sw=10, col="#c8502a"))
ART6["emma-cricket"] = HOP_("meadow", F="#3a2a1a", wingc="#5a4a3a", ant_long=True)
def _glowworm(w, h):
    o = "".join(E(-120 + i * 34, -40, 22, 16 - abs(i - 3) * .6, "#5a4a3a" if i < 6 else "#e8f26a", 2.6) for i in range(8))
    o += "".join(C(-120 + i * 34, -40, 34, "#f2f8a0", 0, ) for i in (6, 7)).replace('fill="#f2f8a0"', 'fill="#f2f8a0" fill-opacity=".35"')
    o += C(-150, -40, 14, "#3a2e22", 2.4) + "".join(P(f"M{-110+i*34} -26 l-6 16 M{-110+i*34} -26 l6 16", sw=3) for i in range(3))
    return scene("meadow", w, h, P("M-250 10 C-120 -10 120 -10 250 10", sw=10, col="#3f7a3a") + o, box=(w / 2, h * .66, 460, 240))
ART6["glow-worm"] = _glowworm
ART6["oriental-hornet"] = FLY_("desert", F="#8a3a1a", stripes="#f2c83a", ab=1.3, eye="#3a2a1a", sting=True, wcol="#e8dcc0")
ART6["velvet-ant"] = ANT_("meadow", F="#e8302a", head="#1f1f22", mand=False)
ART6["garden-tiger"] = BF_("meadow", F="#f2f0e8", F2="#e8602a", vein="#5a3a2a", spots="#3a6ae8", moth=True)
ART6["cecropia"] = BF_("forest", F="#8a4a3a", F2="#a85a3a", vein="#f2e8d8", spots="#f2f2f2", moth=True)
ART6["ulysses"] = BF_("rainforest", F="#2a8ae8", F2="#1f1f22", vein="#1f1f22", spots="#2a8ae8", tails=True)
ART6["small-tortoise"] = BF_("meadow", F="#e8702a", F2="#d8602a", vein=INK, spots="#3a7ae8")
ART6["common-blue"] = BF_("meadow", F="#7aa0f2", F2="#6a90e8", vein="#3a4a7a", spots="#ffffff")
ART6["black-cicada"] = FLY_("forest", F="#3a4a3a", stripes="#7aa06a", ab=0.9, eye="#3a2a1a", wcol="#eef6fb", pre=R(-200, -2, 420, 24, "#8a6a4a", 10, 3))
ART6["whirligig"] = BE_("pond", F="#1f1f22", shine="#8a9ad0", L=.7, post="".join(E(60, -60, 170 + i * 50, 30 + i * 12, "none", 2) for i in range(2)))
ART6["atlas-beetle"] = BE_("rainforest", F="#2a3a2a", shine="#8ac08a", horn="hercules", pre=_a4.LOG, post=P("M10 -140 C-20 -190 -80 -200 -120 -190", sw=12) + P("M10 -140 C-20 -190 -80 -200 -120 -190", sw=7, col="#2a3a2a"))
ART6["dobsonfly"] = FLY_("pond", F="#6a5a3a", ab=1.6, eye="#3a2a1a", wcol="#e8e4d0", wings=2, post=P("M-100 -86 C-140 -110 -170 -90 -190 -60 M-100 -80 C-140 -70 -170 -50 -180 -20", sw=6, col="#4a3a22"))
ART6["thrips"] = SH_("farm", F="#e8c84a", L=1.2, wingc="#f2efe0", pre=P("M-200 0 C-120 -120 0 -140 60 -60 Z", "#f2a0c0", 3))
ART6["mound-termite"] = lambda w, h: scene("savanna", w, h, P("M-200 0 C-180 -120 -120 -300 -60 -320 C-20 -240 0 -160 20 -140 C40 -200 80 -220 100 -180 C140 -100 180 -40 200 0 Z", "#c8803a", 3) + G_(_a4._ant(F="#f2e8d0", head="#c98a3a", mand=True), 120, 40, .5), box=(w / 2, h * .76, 480, 360))
ART6["thorn-bug"] = lambda w, h: scene("forest", w, h, branch(-260, 260, 4, 10) + P("M-120 -10 C-100 -60 60 -70 140 -20 Z", "#7ac04a", 3) + P("M-40 -50 L-10 -170 L30 -50 Z", "#7ac04a", 3) + P("M-30 -60 L-10 -150", sw=4, col="#e8402a") + C(-110, -24, 10, "#e8402a", 2), box=(w / 2, h * .66, 460, 300))

# ---- batch p5_fw1 ----
_eel = _a4._eel
def _pf(F, L=320, H=110, **kw): return _pond(fish(F=F, L=L, H=H, **kw))
ART6["arapaima"] = _pf("#5a6a5a", 440, 100, tail="round", eye_r=6, fin_col="#c8402a", belly="#e8b8a0", extras="".join(E(80 + i * 30, -10, 12, 18, "#c8402a", 0) for i in range(4)))
ART6["piranha"] = _pf("#8a9098", 260, 170, tail="fork", eye_r=9, fin_col="#6a7078", belly="#e8402a")
ART6["electric-eel"] = lambda w, h: scene("pond", w, h, G_(_eel("#3a3a30", L=480, H=44, belly="#e8a03a"), 0, -40) + P("M-260 -160 l20 30 l-14 4 l20 30", sw=4, col="#f2d23a") + P("M240 -170 l-20 30 l14 4 l-20 30", sw=4, col="#f2d23a"), box=(w / 2, h * .7, 560, 260))
ART6["pirarucu-ray"] = lambda w, h: _pond(E(0, -20, 160, 130, "#5a4a3a", 3) + "".join(C(x, y, 14, "#f2a03a", 3) for x, y in [(-80, -70), (-10, -100), (60, -80), (100, -20), (-100, 10), (-30, -30), (40, 10), (-20, 60), (70, 50)]) + P("M150 -20 C220 -20 280 -10 320 0", sw=10) + C(-110, -60, 6, INK, 0) + C(-110, 20, 6, INK, 0))(w, h)
ART6["mekong-cat"] = _pf("#8a9098", 460, 120, tail="fork", eye_r=5, fin_col="#6a7078", belly="#e8eaec", mouth=True)
ART6["wels"] = _pf("#5a5a4a", 440, 100, tail="round", eye_r=5, dorsal=False, fin_col="#4a4a3a", belly="#d8d4c0", spots="#3a3a2a", extras=P("M-210 0 C-260 -20 -290 -60 -300 -90 M-210 10 C-250 20 -270 50 -280 70", sw=4))
ART6["pike"] = _pf("#6a8a4a", 420, 80, tail="fork", eye_r=6, fin_col="#8a7a3a", belly="#e8e8c8", spots="#e8e8a0")
ART6["perch"] = _pf("#8a9a4a", 300, 120, tail="fork", eye_r=8, fin_col="#e8602a", belly="#f2f0d0", stripes=("#3a4a2a", (.3, .45, .6, .75)))
ART6["zander"] = _pf("#8a9a8a", 380, 100, tail="fork", eye_r=9, fin_col="#6a7a6a", belly="#eef0e8", stripes=("#5a6a5a", (.3, .45, .6, .75)))
ART6["bass"] = _pf("#6a8a4a", 340, 130, tail="fork", eye_r=8, fin_col="#5a7a3a", belly="#f0eed8", extras=P("M-120 0 L160 0", sw=12, col="#3a4a2a"))
ART6["bluegill"] = _pf("#5a7a8a", 260, 170, tail="fork", eye_r=8, fin_col="#4a6a7a", belly="#f2c84a", stripes=("#3a5a6a", (.3, .45, .6, .75)), extras=E(-70, -10, 14, 12, "#1f2a4a", 0))
ART6["trout-brown"] = _pf("#a8884a", 360, 100, tail="fork", eye_r=7, fin_col="#8a6a3a", belly="#f2e8c8", spots="#c8402a")
ART6["grayling"] = _pf("#8a8a9a", 340, 100, tail="fork", eye_r=7, fin_col="#a85aa0", belly="#eceef2", tall_dorsal=True, dorsal_col="#a85aa0")
ART6["huchen"] = _pf("#8a6a5a", 440, 100, tail="fork", eye_r=6, fin_col="#c8503a", belly="#e8dcc8", spots="#3a2a1a")
ART6["sturgeon-chinese"] = _pf("#6a7880", 460, 90, tail="shark", eye_r=5, fin_col="#5a6870", belly="#e2e6e8", mouth=False, extras="".join(poly([(-150 + i * 60, -40), (-130 + i * 60, -54), (-110 + i * 60, -40)], "#e8ecee", 2) for i in range(6)))
ART6["paddlefish"] = _pf("#6a7a8a", 380, 90, tail="shark", eye_r=5, fin_col="#5a6a7a", belly="#e2e8ec", mouth=False, extras=P("M-180 -10 L-330 -20 C-350 -10 -350 10 -330 14 L-180 10 Z", "#6a7a8a", 2.6))
ART6["gar"] = _pf("#6a6a4a", 460, 80, tail="round", eye_r=6, fin_col="#5a5a3a", belly="#e8e4c8", spots="#3a3a2a", extras=P("M-220 -10 L-300 -6 L-300 6 L-220 14 Z", "#6a6a4a", 2.6))
ART6["bichir"] = _pf("#8a7a4a", 420, 70, tail="round", eye_r=6, dorsal=False, fin_col="#7a6a3a", belly="#e8dcb0", stripes=("#3a2a1a", (.3, .45, .6, .75)), extras="".join(poly([(-100 + i * 40, -34), (-90 + i * 40, -60), (-80 + i * 40, -34)], "#7a6a3a", 2) for i in range(7)))
ART6["lungfish"] = _pf("#6a6a50", 420, 90, tail="round", eye_r=5, dorsal=False, fin_col="#5a5a40", belly="#d8d0a8", spots="#4a4a30")
ART6["african-lung"] = lambda w, h: scene("wetland", w, h, G_(_eel("#8a7a5a", L=460, H=40, belly="#d8ccb0", spots="#4a3a2a"), 0, -40) + P("M-40 -30 L-60 30 M-10 -30 L0 30 M100 -40 L80 20 M130 -40 L150 20", sw=3), box=(w / 2, h * .72, 540, 240))
ART6["archerfish"] = lambda w, h: _pond(fish(F="#d8d8c8", L=280, H=120, tail="fork", eye_r=10, fin_col="#c8c0a0", belly="#f4f4ec", stripes=("#2a2a2a", (.3, .45, .6, .75))) + P("M-150 -40 C-200 -160 -240 -240 -260 -300", sw=4, col="#5a9ae8"))(w, h)
ART6["mudskipper"] = lambda w, h: scene("wetland", w, h, G_(fish(F="#8a8a6a", L=240, H=70, tail="round", eye_r=10, fin_col="#6a8aa0", belly="#d8d8c0", spots="#5aa0e8", tall_dorsal=True, dorsal_col="#5a8ac0"), 0, -40), box=(w / 2, h * .74, 460, 220))
ART6["snakehead-giant"] = _pf("#3a4a3a", 440, 90, tail="round", eye_r=6, fin_col="#2a3a2a", belly="#d8dccc", stripes=("#1f2a1f", (.3, .45, .6, .75)))
ART6["tench"] = _pf("#6a7a3a", 320, 130, tail="round", eye_r=7, fin_col="#5a6a2a", belly="#d8c050")
ART6["roach-fish"] = _pf("#a8b0b8", 300, 110, tail="fork", eye_r=8, fin_col="#e8503a", belly="#eef2f6")
ART6["barbel"] = _pf("#a8904a", 380, 100, tail="fork", eye_r=7, fin_col="#c8703a", belly="#efe6c8", extras=P("M-190 10 l-30 20 M-180 14 l-20 28", sw=3))
ART6["gudgeon"] = _pf("#b0a890", 240, 70, tail="fork", eye_r=6, fin_col="#9a9078", belly="#efece0", extras=P("M-100 0 L110 0", sw=6, col="#3a3a2a"))
ART6["medaka"] = _pf("#e8d8a0", 200, 60, tail="round", eye_r=9, fin_col="#e8c870", belly="#f8f4e0")
ART6["killifish"] = _pf("#3a8ab8", 220, 80, tail="round", eye_r=7, fin_col="#e8502a", belly="#7ac0e0", spots="#c8402a")
ART6["eel-european"] = lambda w, h: scene("pond", w, h, G_(_eel("#5a5a3a", L=480, H=36, belly="#e8e0a0"), 0, -40), box=(w / 2, h * .7, 540, 220))
# ---- batch p5_arc1 ----
_arach = _a5._arach
def _spd(F, abd=None, mark=None, leg=None, kind="forest", ab=(0, 30, 70, 60), ceph=(0, -45, 40), legl=1.0, hair=None, pre="", post="", web=False, box=(.76, 520, 320)):
    def f(w, h):
        o = pre
        if web:
            o += "".join(P(f"M0 -60 L{math.cos(a)*260:.0f} {-60+math.sin(a)*160:.0f}", sw=1.6, col="#c9ccd0") for a in [i * math.pi / 6 for i in range(12)])
            o += "".join(P(" ".join(("M" if k == 0 else "L") + f"{math.cos(k*math.pi/6)*r:.0f} {-60+math.sin(k*math.pi/6)*r*.62:.0f}" for k in range(13)), sw=1.4, col="#c9ccd0") for r in (60, 110, 160, 210))
        lc = leg or F
        for s in (-1, 1):
            for i in range(4):
                d = f"M{s*18} {ceph[1]+10+i*6} L{s*(80+i*14)*legl:.0f} {ceph[1]-60+i*30} L{s*(130+i*20)*legl:.0f} {ceph[1]+80+i*4}"
                o += P(d, sw=10, col=INK) + P(d, sw=6, col=lc)
        o += E(ab[0], ab[1], ab[2], ab[3], abd or F, 3)
        if mark: o += mark
        if hair: o += "".join(P(f"M{x} {y} l-4 -10", sw=2, col=hair) for x in range(-ab[2] + 16, ab[2] - 10, 16) for y in (ab[1] - 20, ab[1], ab[1] + 20))
        o += C(ceph[0], ceph[1], ceph[2], F, 3) + C(-10, ceph[1] - ceph[2] * .6, 5, INK, 0) + C(10, ceph[1] - ceph[2] * .6, 5, INK, 0)
        return scene(kind, w, h, o + post, box=(w / 2, h * box[0], box[1], box[2]))
    return f
ART6["black-widow"] = _spd("#1a1a1e", ab=(0, 30, 70, 64), mark=P("M-14 40 L14 40 L0 58 Z M-14 76 L14 76 L0 58 Z", "#d8202a", 0), kind="home", legl=1.1)
ART6["orb-weaver"] = _spd("#2a2a22", abd="#f2c83a", mark="".join(P(f"M-60 {y} H60", sw=8, col="#1a1a1a") for y in (10, 34, 58)), web=True, leg="#e8c83a", kind="meadow")
ART6["jumping-spider"] = _spd("#3a2e22", abd="#2a6ad8", mark=E(0, 34, 50, 34, "#d8402a", 0) + "".join(C(x, 30, 8, "#f2c83a", 0) for x in (-26, 0, 26)), ceph=(0, -50, 46), legl=.8, kind="meadow",
                              post=C(-18, -60, 12, INK, 0) + C(18, -60, 12, INK, 0) + C(-14, -64, 4, "#ffffff", 0) + C(22, -64, 4, "#ffffff", 0))
ART6["wolf-spider"] = _spd("#6a5440", abd="#5a4632", mark=P("M0 -10 L0 80", sw=10, col="#a8906a"), hair="#8a7454", kind="forest")
ART6["goliath-spider"] = _arach("#5a4030", hair="#c9a07a", kind="rainforest")
ART6["huntsman"] = _spd("#8a6a4a", abd="#7a5a3a", ab=(0, 26, 60, 44), legl=1.4, kind="home", box=(.74, 560, 300))
ART6["recluse"] = _spd("#a8865a", abd="#8a6a4a", mark=P("M0 -70 L-14 -30 L14 -30 Z", "#4a3220", 0), legl=1.2, kind="home")
ART6["diving-bell"] = lambda w, h: scene("pond", w, h, E(80, -80, 120, 90, "#e6f2fb", 2.4, extra='fill-opacity=".85"') + G_(_spd("#4a4038", abd="#6a6a6a", legl=.8, kind="pond")(w, h).split("<g")[0] if False else "", 0, 0)
                                       + "".join(P(f"M{80+math.cos(a)*120:.0f} {-80+math.sin(a)*90:.0f} L{80+math.cos(a)*160:.0f} {-80+math.sin(a)*130:.0f}", sw=1.6, col="#c9d6e0") for a in [i * .7 for i in range(9)])
                                       + E(80, -70, 34, 28, "#5a5450", 3, ) + C(80, -110, 20, "#4a4038", 3) + "".join(P(f"M{80+s*14} -96 L{80+s*(50+i*10)} {-130+i*24} L{80+s*(70+i*12)} {-60+i*10}", sw=5, col="#4a4038") for s in (-1, 1) for i in range(4)), box=(w / 2, h * .74, 460, 360))
def _trapdoor(w, h):
    o = P("M-260 0 L260 0", sw=6, col="#6a5232") + E(0, 60, 70, 40, "#3a2e22", 0) + P("M-70 0 C-60 -50 40 -60 80 -20", "#8a6a3a", 3)
    o += G_("".join(P(f"M{s*10} {-6+i*4} L{s*(40+i*8)} {-30+i*12} L{s*(60+i*10)} {10+i*2}", sw=6, col="#2a1e14") for s in (-1, 1) for i in range(4)) + E(0, 6, 34, 26, "#2a1e14", 2.6) + C(0, -20, 18, "#2a1e14", 2.6), 0, 40)
    return scene("forest", w, h, o, box=(w / 2, h * .62, 460, 300))
ART6["trapdoor"] = _trapdoor
ART6["deathstalker"] = _arach("#e8d07a", tail=True, kind="desert", box=(.74, 480, 360))
ART6["bark-scorpion"] = _arach("#c9a86a", tail=True, kind="desert", box=(.74, 480, 360))
ART6["whip-scorpion"] = lambda w, h: _arach("#3a2a22", tail=False, kind="forest")(w, h).replace("</svg>", "</svg>") + "" if False else scene("forest", w, h,
    "".join(P(f"M{s*20} {-20+i*8} L{s*(90+i*16)} {-80+i*26} L{s*(140+i*22)} 30", sw=10, col="#2a1e18") for s in (-1, 1) for i in range(3)) + P("M-20 -40 L-160 -200 M20 -40 L160 -200", sw=4, col="#2a1e18")
    + E(0, 10, 40, 80, "#3a2a22", 3) + C(0, -70, 30, "#3a2a22", 3) + P("M0 90 C10 160 -20 220 10 260", sw=3, col="#2a1e18") + "".join(P(f"M{s*20} -80 L{s*60} -120 L{s*40} -140", sw=8, col="#2a1e18") for s in (-1, 1)), box=(w / 2, h * .62, 460, 380))
ART6["camel-spider"] = _spd("#d8b880", abd="#c9a870", ab=(0, 40, 50, 70), ceph=(0, -40, 44), legl=1.1, hair="#f2e0b0", kind="desert",
                            post=P("M-20 -84 L-30 -130 L-10 -110 M20 -84 L30 -130 L10 -110", "#8a5a30", 3))
ART6["tick"] = _spd("#5a2a1a", abd="#8a3a2a", ab=(0, 20, 70, 84), ceph=(0, -76, 22), legl=.7, kind="meadow", mark=E(0, -20, 40, 30, "#2a1a10", 0))
ART6["dust-mite"] = lambda w, h: scene("home", w, h, "".join(P(f"M{s*30} {-60+i*30} L{s*(110+i*6)} {-90+i*34} L{s*(140+i*6)} {-30+i*40}", sw=8, col="#c9b8a0") for s in (-1, 1) for i in range(4))
                                         + E(0, -20, 90, 110, "#f2e8d8", 3) + "".join(P(f"M{-60+i*20} -60 C{-50+i*20} -20 {-60+i*20} 20 {-50+i*20} 60", sw=2, col="#c9b8a0") for i in range(7)) + C(0, -140, 26, "#e8dcc8", 3), box=(w / 2, h * .74, 420, 380))
ART6["coconut-crab"] = lambda w, h: _a4_crab_col(w, h, "#5a3a8a", kind="savanna")
ART6["red-crab"] = lambda w, h: _a4_crab_col(w, h, "#d8302a", kind="rainforest")
def _fiddler(w, h):
    s = _a4_crab_col(w, h, "#3a6ad8", kind="wetland")
    return s
ART6["fiddler"] = lambda w, h: scene("wetland", w, h, "".join(P(f"M{s*40} {-30+i*8} L{s*(90+i*14)} {-60+i*6} L{s*(120+i*16)} {10+i*4}", sw=8, col=INK) + P(f"M{s*40} {-30+i*8} L{s*(90+i*14)} {-60+i*6} L{s*(120+i*16)} {10+i*4}", sw=5, col="#3a6ad8") for s in (-1, 1) for i in range(4))
    + E(0, -50, 80, 46, "#3a6ad8", 3) + P("M60 -70 L130 -140", sw=16, col=INK) + P("M60 -70 L130 -140", sw=11, col="#f2d83a") + E(170, -170, 70, 40, "#f2d83a", 3) + P("M-50 -70 L-80 -110", sw=8) + E(-90, -118, 14, 10, "#f2e0a0", 2)
    + P("M-20 -92 l-6 -30 M20 -92 l6 -30", sw=4) + C(-26, -124, 6, INK, 0) + C(26, -124, 6, INK, 0), box=(w / 2, h * .74, 520, 300))
ART6["king-crab"] = lambda w, h: scene("deep", w, h, "".join(P(f"M{s*40} {-30+i*8} L{s*(130+i*20)} {-110+i*10} L{s*(200+i*20)} {20+i*4}", sw=12, col=INK) + P(f"M{s*40} {-30+i*8} L{s*(130+i*20)} {-110+i*10} L{s*(200+i*20)} {20+i*4}", sw=8, col="#c8402a") for s in (-1, 1) for i in range(3))
    + E(0, -60, 90, 70, "#c8402a", 3) + "".join(P(f"M{x} {y} l0 -14", sw=4, col="#8a2a1a") for x in range(-70, 80, 20) for y in (-90, -60, -30)) + C(-20, -130, 6, INK, 0) + C(20, -130, 6, INK, 0), box=(w / 2, h * .76, 560, 300))
ART6["blue-crab"] = lambda w, h: _a4_crab_col(w, h, "#4a8ac8", kind="sea")
ART6["pistol-shrimp"] = _sea(G_(shrimp(F="#e88a5a", L=240, H=56), 0, 0) + P("M-80 -10 L-140 30", sw=10, col=INK) + E(-170, 40, 46, 26, "#e88a5a", 3) + "".join(P(f"M-230 {30+k*6} l-30 {k*8-10}", sw=3, col="#ffffff") for k in range(3)), box=(.62, 520, 280))
ART6["sea-louse"] = lambda w, h: scene("sea", w, h, G_(fish(F="#9aa6b4", L=480, H=160, tail="fork", belly="#e8eef2", eye_r=10, fin_col="#7a8694"), 0, 0) + "".join(G_(E(0, 0, 20, 14, "#c9a46a", 2) + P("M0 14 l-4 14 M6 14 l4 14", sw=3, col="#a8844a"), x, y) for x, y in ((40, -30), (90, 10), (-30, 20))), box=(w / 2, h * .6, 600, 300))
def _pillbug(w, h):
    o = E(0, -40, 150, 70, "#5a5a62", 3) + "".join(P(f"M{x} -104 C{x-8} -60 {x-8} -20 {x} 20", sw=3, col="#3a3a40") for x in range(-110, 130, 22))
    o += P("M-150 -40 C-190 -70 -210 -90 -230 -80 M-150 -30 C-190 -40 -210 -30 -230 -20", sw=4) + "".join(P(f"M{x} 26 l-4 16", sw=4) for x in range(-110, 130, 30))
    return scene("forest", w, h, o, box=(w / 2, h * .74, 460, 240))
ART6["pill-bug"] = _pillbug
def _goose(w, h):
    o = P("M-260 -260 C-100 -250 100 -270 260 -250", sw=24, col="#8a6a3a")
    for x in (-120, -20, 80):
        o += P(f"M{x} -250 C{x+10} -200 {x-10} -160 {x} -120", sw=16, col="#5a3a3a") + P(f"M{x-30} -120 C{x-30} -40 {x+30} -40 {x+30} -120 C{x+20} -150 {x-20} -150 {x-30} -120 Z", "#f2eee6", 3) + P(f"M{x} -126 L{x} -50", sw=2, col="#9aa0a6")
        o += "".join(P(f"M{x-10+k*8} -40 C{x-20+k*8} 0 {x-30+k*10} 20 {x-40+k*12} 30", sw=2.4, col="#5a3a3a") for k in range(4))
    return scene("sea", w, h, o, box=(w / 2, h * .9, 460, 400))
ART6["barnacle"] = _goose
ART6["copepod"] = lambda w, h: scene("sea", w, h, P("M-80 -60 C-80 -140 80 -140 100 -60 C80 -10 -60 -10 -80 -60 Z", "#e8b07a", 3, extra='fill-opacity=".9"') + P("M100 -60 L200 -40 M200 -40 l30 -14 M200 -40 l30 14", sw=4)
    + P("M-70 -100 C-160 -160 -260 -150 -300 -120", sw=3) + P("M-70 -90 C-160 -120 -260 -60 -300 -40", sw=3) + C(-60, -80, 8, "#c8302a", 0) + C(40, -70, 14, "#d84a2a", 0, ), box=(w / 2, h * .62, 520, 260))
# ---- batch p5_pol1 ----
_peng5 = _a5._peng
def _icef(F, **kw): return _fs(F, kind="ice" if False else "sea", **kw)
ART6["collared-lemming"] = lambda w, h: scene("snow", w, h, rodent("#ecebe6", 220, 130, belly="#ffffff", ears="small", nose="#3a3430"), box=(w / 2, h * .74, 400, 250))
ART6["stoat"] = Q("snow", (.74, 580, 260), F="#8a5a32", bl=290, bd=66, lh=44, lw=20, belly="#f4ecd8", neck=(30, 50), nw=50, head=(36, 30), snout=(30, 20), snout_col="#f4ecd8",
                  ears="round", tail="thin", tail_col="#1f1f22")
ART6["ringed-seal"] = lambda w, h: scene("ice", w, h, pinniped("#6a7480", L=320, up=0.1, belly="#b8c0c8") + "".join(E(x, y, 14, 9, "none", 3) for x, y in [(-80, -50), (-20, -60), (40, -55), (100, -45), (-50, -30), (70, -30)]), box=(w / 2, h * .72, 560, 260))
ART6["bearded-seal"] = lambda w, h: scene("ice", w, h, pinniped("#8a7a6a", L=380, up=0.15, belly="#a89a8a") + "".join(P(f"M-170 {-40+i*6} l-40 {-6+i*4}", sw=2.4, col="#f4f0e8") for i in range(5)), box=(w / 2, h * .72, 620, 260))
ART6["hooded-seal"] = lambda w, h: scene("ice", w, h, pinniped("#9aa0a8", L=360, up=0.2, spots="#2a2e34", belly="#c9ced4") + E(-160, -72, 34, 24, "#3a3e44", 2.6), box=(w / 2, h * .72, 600, 260))
ART6["ross-seal"] = lambda w, h: scene("ice", w, h, pinniped("#4a525c", L=320, up=0.35, belly="#c9ced4") + "".join(P(f"M-120 {-70+i*12} l60 0", sw=3, col="#8a929c") for i in range(3)), box=(w / 2, h * .72, 560, 280))
ART6["crabeater"] = lambda w, h: scene("ice", w, h, pinniped("#c9c0b0", L=360, up=0.1, belly="#e6e0d4") + "".join(P(f"M{x} {y} l18 10", sw=3, col="#8a7a6a") for x, y in [(-40, -50), (20, -60), (80, -48)]), box=(w / 2, h * .72, 600, 260))
ART6["ant-fur-seal"] = lambda w, h: coast(w, h, pinniped("#6a5a4a", L=320, up=0.6, ears=True, belly="#8a7a6a"), (w / 2, h * .66, 540, 320))
ART6["arctic-cod"] = _fs("#8a7a5a", L=320, H=90, kind="sea", tail="fork", belly="#e8e2d0", spots="#5a4a3a")
ART6["icefish"] = _fs("#c9ccd0", L=340, H=90, kind="sea", tail="round", belly="#f2f2f2", post=P("M-170 -6 L-210 -20 L-176 6 Z", "#c9ccd0", 2) + "".join(P(f"M{x} -40 l-20 60", sw=4, col="#7a7e86") for x in (-60, 0, 60)))
ART6["toothfish"] = _fs("#5a5048", L=380, H=120, kind="sea", tail="round", belly="#a89a8a", spots="#3a322a")
ART6["chinstrap"] = _peng5("#2a2a2e", "#ffffff", lambda: C(-10, -276, 36, "#ffffff", 0) + P("M-44 -256 C-20 -240 20 -240 30 -262", sw=4, col=INK) + C(-22, -286, 7, "#2a2a2e", 0), beak="#2a2a2a", feet="#f2b0b0")
ART6["gentoo"] = _peng5("#2a2e34", "#ffffff", lambda: P("M-28 -306 C-6 -318 18 -312 24 -296", sw=8, col="#ffffff"), beak="#e8602a", feet="#f2903a")
ART6["macaroni"] = _peng5("#1f1f22", "#ffffff", lambda: P("M-30 -300 C-6 -320 30 -330 60 -310 M-30 -300 C0 -312 36 -316 66 -296", sw=6, col="#f2b02a"), beak="#c8502a", feet="#f2b0b0")
ART6["snow-petrel"] = B("snow", (.78, 440, 400), pre=G_(rock(0, 0, 1.8), 0, 0), F="#ffffff", wing="#f4f6f8", rx=64, ry=44, tilt=-12, neck=12, nw=32, hr=26, beak="short", beak_col="#1f1f22", leg_len=30, leg_col="#6a8aa8", legw=5, tail="short", tail_col="#ffffff")
ART6["ptarmigan"] = B("snow", (.78, 440, 360), F="#ffffff", wing="#f4f4f2", rx=78, ry=58, tilt=-6, neck=10, nw=44, hr=30, beak="short", beak_col="#1f1f22", leg_len=20, leg_col="#ffffff", legw=10, tail="short", tail_col="#1f1f22",
                      front_fn=lambda x, y, r: P(f"M{x-r*.9} {y-r*.15} L{x+r*.5} {y-r*.15}", sw=5, col=INK) + P(f"M{x-r*.2} {y-r*.5} l{r*.4} 0", sw=4, col="#e8302a"))
ART6["ivory-gull"] = B("ice", (.76, 440, 400), F="#ffffff", wing="#ffffff", rx=72, ry=44, tilt=-12, neck=16, nw=32, hr=26, beak="short", beak_col="#6a7a5a", leg_len=30, leg_col="#1f1f22", legw=5, tail="short", tail_col="#ffffff",
                       front_fn=lambda x, y, r: P(f"M{x-r*1.5} {y+r*.1} l{-r*.3} {r*.05}", sw=4, col="#f2c83a"))
ART6["gyrfalcon"] = B("snow", (.78, 480, 420), F="#f4f4f2", wing="#9aa0a8", rx=84, ry=58, tilt=-24, neck=14, nw=48, hr=34, beak="hook", beak_col="#5a6470", leg_len=40, leg_col="#f2c53a", legw=7, tail="long", tail_col="#9aa0a8")
def _midge(w, h):
    o = "".join(P(f"M{x} -40 L{x+dx} 10", sw=4, col="#1f1f22") for x, dx in [(-30, -40), (-10, -20), (10, 10), (-30, -10), (-10, 10), (10, 40)])
    o += E(70, -50, 70, 22, "#2a2a2e", 2.6) + "".join(P(f"M{40+i*24} -70 l0 40", sw=2, col="#5a5a5a") for i in range(4))
    o += E(-10, -54, 32, 26, "#1f1f22", 2.6) + C(-50, -60, 18, "#1f1f22", 2.6) + P("M-62 -74 l-30 -30 M-58 -76 l-14 -36", sw=3, col="#1f1f22")
    o += E(10, -80, 18, 7, "#8a8a8a", 1.6)
    return scene("snow", w, h, G_(rock(0, 0, 2.6), 0, 60) + G_(o, 0, 0, 1.2), box=(w / 2, h * .66, 420, 300))
ART6["ant-midge"] = _midge
ART6["ant-minke"] = _ceta("#3a424e", 440, 110, belly="#eef2f4", box=None, extras=P("M-80 30 l40 30", sw=10, col="#9aa0a8"))
