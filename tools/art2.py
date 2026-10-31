"""Phase-2 parametric animal illustrations (same v4 line style as art.py).
Animals are drawn in local coords (facing left, ground at y=0) inside <g class="fit">; a tiny script in the
card template scales/places them into the habitat box, so templates don't need exact extents."""
import math
from iso import INK, GREY, MUTE, BLUE, BLUE_L, BLUE_M, ORG, ORG_L, YEL, YEL_L, SAGE, SAGE_L
from art import P, E, C, svg, slab, shadow, tuft, rock, sun, acacia, bamboo, leafb, seaweed, tentacle, wavy, leg, cushion, yarn

_uid = [0]
def uid(p="c"):
    _uid[0] += 1
    return f"{p}{_uid[0]}"


def fit(body, cx, by, w, h, mx=1.6):
    return f'<g class="fit" data-cx="{cx:.0f}" data-by="{by:.0f}" data-w="{w:.0f}" data-h="{h:.0f}" data-max="{mx}"><g class="inner">{body}</g></g>'


def R(x, y, w, h, fill="none", rx=0, sw=3, col=INK, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{col}" stroke-width="{sw}" {extra}/>'


def poly(pts, fill="none", sw=3, col=INK):
    return P("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z", fill, sw, col)


def clip(shape_d, body):
    i = uid("k")
    return f'<clipPath id="{i}"><path d="{shape_d}"/></clipPath><g clip-path="url(#{i})">{body}</g>'


def darker(hexc, f=0.86):
    h = hexc.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f))


# ====================================================================== habitats
def tree(x, y, s=1, crown=SAGE_L, trunk="#d9c3a0"):
    return (P(f"M{x-8*s} {y} L{x-6*s} {y-110*s} L{x+6*s} {y-110*s} L{x+8*s} {y} Z", trunk, 2.8) +
            P(wavy(x, y - 170 * s, 70 * s, 78 * s, 9, 8 * s), crown, 2.8) + P(f"M{x-30*s} {y-160*s} q20 -14 40 -4", sw=2, col=SAGE))


def pine(x, y, s=1):
    return (P(f"M{x-6*s} {y} V{y-40*s} H{x+6*s} V{y} Z", "#d9c3a0", 2.6) +
            poly([(x - 60 * s, y - 40 * s), (x, y - 200 * s), (x + 60 * s, y - 40 * s)], SAGE_L, 2.8) +
            P(f"M{x-40*s} {y-90*s} L{x} {y-110*s} L{x+40*s} {y-90*s} M{x-26*s} {y-140*s} L{x} {y-156*s} L{x+26*s} {y-140*s}", sw=2, col=SAGE))


def mountains(w, y, col="#eef0f2", snow=True):
    o = poly([(60, y), (230, y - 210), (400, y)], col, 2.8) + poly([(300, y), (520, y - 260), (740, y)], col, 2.8) + poly([(640, y), (790, y - 180), (920, y)], col, 2.8)
    if snow:
        o += poly([(230, y - 210), (196, y - 168), (216, y - 176), (236, y - 160), (262, y - 172)], "#fff", 2.4)
        o += poly([(520, y - 260), (478, y - 206), (504, y - 214), (526, y - 196), (556, y - 214)], "#fff", 2.4)
    return o


def fence(iso, T, a0, a1, b, n=5):
    o = ""
    pts = [iso.P(a0 + (a1 - a0) * i / (n - 1), b, T) for i in range(n)]
    for x, y in pts:
        o += R(x - 6, y - 70, 12, 70, "#f3e2c4", 2, 2.6)
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    for dy in (50, 25):
        o += P(f"M{x0} {y0-dy} L{x1} {y1-dy}", sw=9) + P(f"M{x0} {y0-dy} L{x1} {y1-dy}", sw=4, col="#f3e2c4")
    return o


def flower(x, y, col=ORG_L, s=1):
    o = P(f"M{x} {y} q-4 -20 0 -40", sw=2.4, col=SAGE)
    for i in range(5):
        a = math.pi * 2 * i / 5
        o += C(x + math.cos(a) * 9 * s, y - 44 + math.sin(a) * 9 * s, 7 * s, col, 2)
    return o + C(x, y - 44, 5 * s, YEL, 1.6)


def bubbles(pts):
    return "".join(C(x, y, r, "#fff", 2.2, BLUE) for x, y, r in pts)


def scene(kind, w, h, animal, box=None, extra=""):
    """kind: home, farm, savanna, plateau, forest, rainforest, snow, sea, deep, ice, pond, tank, meadow, leaf, desert, wetland, branch"""
    o = []
    cy = h * 0.62
    if kind in ("sea", "deep"):
        o.append(R(0, 0, w, h, BLUE_L if kind == "sea" else "#cfe0f6", 0, 0, "none"))
        for x0 in (120, 380, 640):
            o.append(P(f"M{x0} 0 L{x0+60} {h*0.5:.0f} L{x0+120} 0", "#ffffff", 0, extra='fill-opacity=".45"'))
        s, iso, T = slab(w, h, YEL_L, "#f5e3a6", "#ecd58a", W_=520, D=240, cy=h * 0.76)
        o.append(s)
        for (a, b), hh, sc in (((30, 200), 200, .9), ((480, 40), 230, 1.0)):
            o.append(seaweed(*iso.P(a, b, T), hh, sc))
        o.append(rock(*iso.P(400, 200, T), 1.1) + rock(*iso.P(120, 60, T), .8))
        o.append(bubbles([(820, 120, 12), (845, 80, 8), (830, 44, 6), (110, 160, 9), (95, 115, 6)]))
        bx = box or (w / 2, h * 0.58, 600, 330)
    elif kind == "tank":
        o.append(R(150, 40, 640, 470, BLUE_L, 14, 3.4))
        o.append(R(150, 40, 640, 40, "#fff", 14, 3.4))
        o.append(P("M150 450 Q470 420 790 450 L790 496 Q790 510 776 510 L164 510 Q150 510 150 496 Z", YEL_L, 3))
        for x in (210, 250, 690, 730):
            o.append(seaweed(x, 470, 220 if x % 20 else 170, .8))
        o.append(rock(560, 478, .8) + rock(330, 482, .6))
        o.append(bubbles([(700, 140, 10), (716, 110, 7), (706, 86, 5)]))
        bx = box or (w / 2, 380, 420, 250)
    elif kind == "ice":
        o.append(R(0, h * 0.42, w, h * 0.58, BLUE_L, 0, 0, "none"))
        for y in (300, 380, 520):
            for x in (60, 760, 850):
                o.append(P(f"M{x} {y} q15 -8 30 0 q15 8 30 0", sw=2, col=BLUE_M))
        o.append(poly([(40, h * .42), (100, 160), (170, 130), (240, h * .42)], "#fff", 2.6))
        o.append(poly([(700, h * .42), (760, 180), (830, 150), (900, h * .42)], "#fff", 2.6))
        s, iso, T = slab(w, h, "#ffffff", "#e8f1fb", BLUE_M, W_=500, D=250, T=34, cy=h * 0.63)
        o.append(s)
        bx = box or (w / 2, h * 0.75, 560, 400)
    else:
        pal = {"home": (YEL_L, "#f5e3a6", "#ecd58a"), "savanna": (YEL_L, "#f5e3a6", "#ecd58a"), "desert": ("#fbe9c8", "#f3d9a8", "#e8c98a"),
               "snow": ("#ffffff", "#e8f1fb", BLUE_M)}.get(kind, (SAGE_L, "#cfe3c6", "#bcd6b1"))
        if kind in ("plateau", "snow"):
            o.append(mountains(w, h * 0.50))
        if kind == "desert":
            o.append(sun(800, 80) + P(f"M0 {h*0.46:.0f} Q200 {h*0.36:.0f} 420 {h*0.46:.0f} Q640 {h*0.38:.0f} {w} {h*0.46:.0f}", "#fbe9c8", 2.6))
        if kind == "home":
            o.append(R(150, 40, 170, 200, "#fff", 8) + R(162, 52, 146, 176, BLUE_L, 4, 0, "none") + P("M235 52 V228 M162 140 H308", sw=3) + C(275, 95, 18, YEL_L, 2.4, YEL))
        s, iso, T = slab(w, h, *pal, W_=540, D=250, cy=cy)
        o.append(s)
        if kind == "home":
            for a in range(65, 540, 65):
                o.append(P("M{:.0f} {:.0f} L{:.0f} {:.0f}".format(*iso.P(a, 0, T), *iso.P(a, 250, T)), sw=1.6, col="#e2c879"))
        if kind == "farm":
            o.append(fence(iso, T, 20, 520, 8, 6))
            o.append(P("M720 140 L800 90 L880 140 Z", ORG_L, 2.8) + R(730, 140, 140, 110, "#fff") + R(782, 190, 36, 60, ORG_L, 2))
        if kind == "savanna":
            o.append(sun(800, 80) + acacia(*iso.P(520, 10, T), 1.2))
        if kind in ("forest",):
            for a, sc in ((20, 1.0), (140, .8), (420, .9)):
                o.append(pine(*iso.P(a, 10, T), sc) if a != 140 else tree(*iso.P(a, 10, T), sc))
            o.append(tree(*iso.P(530, 40, T), 1.0))
        if kind == "rainforest":
            for a, sc in ((30, 1.15), (500, 1.1)):
                o.append(tree(*iso.P(a, 10, T), sc, "#cfe8c4"))
            o.append(P("M120 0 C150 120 110 200 140 300 M820 0 C790 100 830 180 800 260", sw=3, col=SAGE))
            o.append(leafb(140, 300, 120, 40) + leafb(800, 260, 60, 40))
        if kind in ("pond", "wetland"):
            px, py = iso.P(330, 150, T)
            o.append(E(px, py, 190, 70, BLUE_L, 2.6) + P(f"M{px-80} {py} q15 -8 30 0 q15 8 30 0 M{px+30} {py+20} q15 -8 30 0 q15 8 30 0", sw=2, col=BLUE_M))
            for a, b in ((60, 60), (90, 40), (480, 200)):
                x, y = iso.P(a, b, T)
                o.append(P(f"M{x} {y} q-6 -50 0 -90 M{x+8} {y} q6 -40 2 -70", sw=2.6, col=SAGE) + E(x, y - 96, 5, 14, "#c9a27a", 2))
        if kind in ("meadow", "leaf"):
            for a, b, c_ in ((60, 220, ORG_L), (480, 60, YEL_L), (420, 230, "#fde3ef"), (140, 40, ORG_L)):
                o.append(flower(*iso.P(a, b, T), c_))
        if kind == "snow":
            for x, y in ((120, 80), (330, 60), (700, 70), (840, 160)):
                o.append(P(f"M{x-9} {y} H{x+9} M{x} {y-9} V{y+9} M{x-6} {y-6} L{x+6} {y+6} M{x-6} {y+6} L{x+6} {y-6}", sw=2, col=BLUE_M))
        if kind not in ("home", "snow", "desert"):
            for a, b in ((60, 230), (300, 240), (500, 190), (200, 120)):
                o.append(tuft(*iso.P(a, b, T), 1.1, col="#b8a15a" if kind == "savanna" else SAGE))
        if kind == "plateau":
            o.append(sun(820, 70, 30))
        bx = box or (w / 2, h * 0.75, 620, 420)
    o.append(extra)
    cx, by, bw, bh = bx
    if kind not in ("sea", "deep", "tank"):
        o.append(shadow(cx, by, min(bw * .42, 240)))
    o.append(fit(animal, cx, by, bw, bh))
    return svg(w, h, "".join(o))


# ====================================================================== quadruped
def quad(F="#e9d3b0", bl=300, bd=130, lh=150, lw=34, belly=None, farleg=None, neck=(40, 30), nw=None, head=(62, 52), snout=(46, 34),
         snout_col=None, ears="point", tail="thin", tail_col=None, pattern=None, pat_col=INK, horns=None, hooves=None, mane=None, hump=None,
         nose=INK, eye=True, chest=0, shoulder=0, extras="", front_extras="", taper=0.8, legs_style="straight", headdown=0):
    farleg = farleg or darker(F)
    snout_col = snout_col or F
    x0, x1, yt, yb = -bl / 2, bl / 2, -(lh + bd), -lh
    o = []
    # tail (behind)
    tc = tail_col or F
    tx, ty = x1 - 6, yt + bd * .25
    if tail == "thin":
        o.append(P(f"M{tx} {ty} C{tx+40} {ty+10} {tx+50} {ty+70} {tx+40} {ty+120}", sw=7) + P(f"M{tx} {ty} C{tx+40} {ty+10} {tx+50} {ty+70} {tx+40} {ty+120}", sw=3, col=tc))
    elif tail == "tuft":
        o.append(P(f"M{tx} {ty} C{tx+26} {ty+20} {tx+30} {ty+70} {tx+26} {ty+bd*.9}", sw=3))
        o.append(P(wavy(tx + 26, ty + bd * .9 + 14, 11, 18, 5, 4), tail_col or darker(F, .6), 2.4))
    elif tail == "bushy":
        o.append(P(f"M{tx-10} {ty-4} C{tx+60} {ty-10} {tx+110} {ty+40} {tx+120} {ty+100} C{tx+90} {ty+110} {tx+40} {ty+60} {tx-6} {ty+30} Z", tc, 3))
        o.append(P(f"M{tx+120} {ty+100} C{tx+104} {ty+100} {tx+96} {ty+92} {tx+92} {ty+80} C{tx+104} {ty+82} {tx+114} {ty+88} {tx+120} {ty+100} Z", tail_col and "#fff" or "#fff", 2.4))
    elif tail == "horse":
        o.append(P(f"M{tx-4} {ty} C{tx+50} {ty+10} {tx+50} {ty+90} {tx+40} {ty+150} C{tx+20} {ty+120} {tx+10} {ty+60} {tx-10} {ty+20} Z", tail_col or darker(F, .55), 2.8))
    elif tail == "curl":
        o.append(P(f"M{tx} {ty+10} c20 -8 30 10 18 18 c-10 6 -16 -6 -4 -10", sw=3.5))
    elif tail == "long":
        o.append(P(f"M{tx} {ty} C{tx+70} {ty+20} {tx+60} {ty+120} {tx+120} {ty+110}", sw=22) + P(f"M{tx} {ty} C{tx+70} {ty+20} {tx+60} {ty+120} {tx+120} {ty+110}", sw=16, col=tc))
    elif tail == "short":
        o.append(E(tx + 10, ty + 12, 16, 10, tc, rot=20))
    # legs
    fx, bx_ = x0 + bd * .45, x1 - bd * .5
    def lg(x, fill, top=yb - bd * .35):
        w0, w1 = lw * 1.1, lw * taper
        if legs_style == "bent":   # sprawled reptile style
            return P(f"M{x-w0/2} {top} L{x-w0/2-16} {-lh*.45} L{x-w1/2} {0} L{x+w1/2+14} 0 L{x+w0/2-6} {-lh*.45} L{x+w0/2} {top} Z", fill, 2.8)
        d = f"M{x-w0/2} {top} L{x-w1/2} {-8} Q{x-w1/2} 0 {x-w1/2+8} 0 L{x+w1/2-8} 0 Q{x+w1/2} 0 {x+w1/2} -8 L{x+w0/2} {top} Z"
        s = P(d, fill, 2.8)
        if hooves:
            s += P(f"M{x-w1/2} -14 L{x+w1/2} -14 L{x+w1/2} -6 Q{x+w1/2} 0 {x+w1/2-6} 0 L{x-w1/2+6} 0 Q{x-w1/2} 0 {x-w1/2} -6 Z", hooves, 2.4)
        return s
    o.append(lg(fx + lw * .9, farleg) + lg(bx_ + lw * .9, farleg))
    o.append(lg(fx, F) + lg(bx_, F))
    # body
    hy = shoulder
    bdpath = (f"M{x0+bd*.35} {yb} C{x0-bd*.28-chest} {yb} {x0-bd*.32-chest} {yt+bd*.05} {x0+bd*.4} {yt-hy} "
              f"L{x1-bd*.45} {yt} C{x1+bd*.25} {yt} {x1+bd*.25} {yb} {x1-bd*.35} {yb} Z")
    o.append(P(bdpath, F))
    if hump == "camel":
        o.append(P(f"M{x0+bd*.5} {yt+4} C{x0+bd*.6} {yt-80} {x0+bd*1.25} {yt-80} {x0+bd*1.3} {yt+2} C{x0+bd*1.45} {yt-70} {x0+bd*2.1} {yt-70} {x0+bd*2.2} {yt+4}", F, 3))
    if hump == "bison":
        o.append(P(f"M{x0+bd*.1} {yt+bd*.3} C{x0+bd*.2} {yt-60} {x0+bd*1.4} {yt-70} {x0+bd*1.9} {yt+6} L{x0+bd*1.6} {yb+10} L{x0+bd*.1} {yb} Z", mane or darker(F, .7), 3))
    inner = ""
    if belly:
        inner += E(0, yb + 4, bl * .45, bd * .32, belly, 0)
    if pattern == "stripes":
        for i in range(-4, 6):
            xx = i * bl / 9
            inner += P(f"M{xx} {yt-20} q{-14} {bd*.45} {4} {bd+20}", sw=9, col=pat_col)
    elif pattern == "spots":
        for i in range(36):
            inner += C(x0 + (i * 37) % bl, yt + 10 + (i * 53) % int(bd - 10), 5, pat_col, 0)
    elif pattern == "rosettes":
        for i in range(22):
            cx_, cy_ = x0 + 20 + (i * 47) % (bl - 20), yt + 18 + (i * 61) % int(bd - 22)
            inner += C(cx_, cy_, 9, "none", 3.2, pat_col)
    elif pattern == "patches":
        for i in range(9):
            cx_, cy_ = x0 + 30 + (i * 71) % (bl - 30), yt + 22 + (i * 43) % int(bd - 30)
            inner += P(wavy(cx_, cy_, 26, 20, 5, 4, i), pat_col, 0)
    elif pattern == "giraffe":
        for i in range(16):
            cx_, cy_ = x0 + 16 + (i * 53) % (bl - 10), yt + 18 + (i * 37) % int(bd - 10)
            inner += R(cx_ - 18, cy_ - 15, 36, 30, pat_col, 6, 0, "none")
    if inner:
        o.append(clip(bdpath, inner))
    o.append(P(bdpath, "none"))
    o.append(extras)
    # neck + head
    nl, na = neck
    nw = nw or bd * .55
    a = math.radians(na)
    nx0, ny0 = x0 + bd * .3, yt + bd * .35
    hx, hy_ = nx0 - nl * math.sin(a), ny0 - nl * math.cos(a) + headdown
    if nl > 0:
        ux, uy = math.cos(a), -math.sin(a)
        pts = [(nx0 + ux * nw / 2 + 10, ny0 + uy * nw / 2 + 20), (hx + ux * nw * .35, hy_ + uy * nw * .35), (hx - ux * nw * .35, hy_ - uy * nw * .35), (nx0 - ux * nw / 2, ny0 - uy * nw / 2 + 10)]
        o.append(P("M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z", F, 0))
        o.append(P(f"M{pts[0][0]:.1f} {pts[0][1]:.1f} L{pts[1][0]:.1f} {pts[1][1]:.1f} M{pts[2][0]:.1f} {pts[2][1]:.1f} L{pts[3][0]:.1f} {pts[3][1]:.1f}"))
        if pattern == "giraffe":
            for t in (.25, .55, .8):
                o.append(R(nx0 + (hx - nx0) * t - 12, ny0 + (hy_ - ny0) * t - 10, 24, 20, pat_col, 5, 0, "none"))
        if pattern == "stripes" and pat_col == INK and mane == "zebra":
            for t in (.2, .45, .7):
                o.append(P(f"M{nx0+(hx-nx0)*t-24:.0f} {ny0+(hy_-ny0)*t-6:.0f} l40 18", sw=8))
    if mane == "horse":
        o.append(P(f"M{nx0+14} {ny0-6} C{nx0+10} {(ny0+hy_)/2} {hx+30} {hy_-10} {hx+16} {hy_-head[1]*.7} L{hx+34} {hy_-head[1]*.3} C{hx+40} {(ny0+hy_)/2} {nx0+24} {ny0} {nx0+40} {ny0+10} Z", darker(F, .55), 2.6))
    if mane == "zebra":
        o.append(P(f"M{nx0+10} {ny0-4} L{hx+14} {hy_-head[1]*.7}", sw=16) + P(f"M{nx0+10} {ny0-4} L{hx+14} {hy_-head[1]*.7}", sw=10, col="#fff"))
    o.append(head_(hx, hy_, F, head, snout, snout_col, ears, horns, nose, eye))
    o.append(front_extras)
    return "".join(o)


def head_(hx, hy, F, head, snout, scol, ears, horns, nose, eye=True):
    rx, ry = head
    sl, sh = snout
    o = []
    ex, ey = hx + rx * .35, hy - ry * .75
    if ears == "point":
        o.append(poly([(ex - 18, ey + 14), (ex - 4, ey - 34), (ex + 22, ey + 8)], F, 2.8) + poly([(ex - 10, ey + 8), (ex - 3, ey - 16), (ex + 10, ey + 4)], "#f6c9b0", 0))
    elif ears == "big":
        o.append(poly([(ex - 22, ey + 16), (ex - 6, ey - 56), (ex + 26, ey + 10)], F, 2.8) + poly([(ex - 12, ey + 8), (ex - 5, ey - 32), (ex + 12, ey + 4)], "#f6c9b0", 0))
    elif ears == "round":
        o.append(C(ex, ey + 2, 18, F, 2.8) + C(ex, ey + 4, 9, "#f6c9b0", 0))
    elif ears == "long":
        o.append(E(ex + 8, ey - 40, 13, 46, F, 2.8, rot=14) + E(ex + 8, ey - 38, 6, 34, "#f6c9b0", 0, rot=14))
    elif ears == "droop":
        o.append(E(ex + 14, hy + 4, 16, 36, darker(F, .8), 2.8, rot=-12))
    elif ears == "side":
        o.append(E(ex + 20, ey + 14, 28, 11, F, 2.8, rot=-20) + E(ex + 18, ey + 14, 16, 5, "#f6c9b0", 0, rot=-20))
    elif ears == "small":
        o.append(E(ex + 6, ey + 6, 9, 13, F, 2.6, rot=20))
    if horns == "cow":
        o.append(P(f"M{hx-4} {hy-ry*.8} C{hx-14} {hy-ry*1.4} {hx-34} {hy-ry*1.5} {hx-40} {hy-ry*1.4} C{hx-30} {hy-ry*1.2} {hx-16} {hy-ry*1.05} {hx+8} {hy-ry*.7} Z", "#fff8e8", 2.6))
    elif horns == "goat":
        o.append(P(f"M{hx} {hy-ry*.8} C{hx+10} {hy-ry*1.8} {hx+50} {hy-ry*2.0} {hx+70} {hy-ry*1.5} C{hx+50} {hy-ry*1.6} {hx+24} {hy-ry*1.4} {hx+16} {hy-ry*.75} Z", "#d9cbb5", 2.6))
    elif horns == "ram":
        o.append(C(hx + rx * .35, hy - ry * .1, ry * .62, "#e9dcc4", 3) + C(hx + rx * .35, hy - ry * .1, ry * .3, "none", 2.4))
    elif horns == "antler":
        bx_, by_ = hx + 6, hy - ry * .85
        o.append(P(f"M{bx_} {by_} L{bx_+14} {by_-60} L{bx_+40} {by_-110} M{bx_+10} {by_-44} L{bx_-14} {by_-80} M{bx_+28} {by_-86} L{bx_+10} {by_-118} M{bx_+16} {by_-62} L{bx_+50} {by_-74}", sw=8) +
                 P(f"M{bx_} {by_} L{bx_+14} {by_-60} L{bx_+40} {by_-110} M{bx_+10} {by_-44} L{bx_-14} {by_-80} M{bx_+28} {by_-86} L{bx_+10} {by_-118} M{bx_+16} {by_-62} L{bx_+50} {by_-74}", sw=3.6, col="#e6d2b0"))
    elif horns == "ossicone":
        o.append(R(hx - 2, hy - ry * 1.5, 10, ry * .8, F, 4, 2.6) + C(hx + 3, hy - ry * 1.5, 8, darker(F, .5), 2.4))
        o.append(R(hx + 18, hy - ry * 1.45, 10, ry * .75, F, 4, 2.6) + C(hx + 23, hy - ry * 1.45, 8, darker(F, .5), 2.4))
    elif horns == "chiru":
        o.append(P(f"M{hx} {hy-ry*.8} C{hx-8} {hy-ry*2.2} {hx-14} {hy-ry*3.2} {hx-10} {hy-ry*3.8}", sw=8) + P(f"M{hx} {hy-ry*.8} C{hx-8} {hy-ry*2.2} {hx-14} {hy-ry*3.2} {hx-10} {hy-ry*3.8}", sw=4, col="#2c2c2c"))
        for t in range(6):
            o.append(P(f"M{hx-8-t*.8} {hy-ry*(1.1+t*.42)} h10", sw=2, col="#fff"))
    elif horns in ("bison", "wildebeest", "yak"):
        k = {"bison": 1.0, "wildebeest": 1.4, "yak": 2.0}[horns]
        o.append(P(f"M{hx+4} {hy-ry*.75} C{hx-20*k} {hy-ry*.9} {hx-34*k} {hy-ry*1.1-20*k} {hx-26*k} {hy-ry*1.2-36*k} C{hx-22*k} {hy-ry*1.1-16*k} {hx-6*k} {hy-ry*.95-6} {hx+18} {hy-ry*.5} Z", "#3a3a3a" if horns != "yak" else "#e9e1d3", 2.6))
    o.append(E(hx, hy, rx, ry, F))
    if sl:
        sx, sy = hx - rx * .7 - sl * .45, hy + ry * .3
        o.append(E(sx, sy, sl * .6 + 6, sh * .62, scol, 2.8))
        o.append(E(sx - sl * .5, sy - sh * .2, 7, 5.5, nose, 0) if nose else "")
        o.append(P(f"M{sx-sl*.45} {sy+sh*.22} q{sl*.3} {sh*.2} {sl*.65} 0", sw=2.2))
    if horns == "rhino":
        sx, sy = hx - rx * .7 - sl * .45, hy + ry * .3
        o.append(P(f"M{sx-sl*.35} {sy-sh*.5} L{sx-sl*.55} {sy-sh*1.9} L{sx-sl*.0} {sy-sh*.55} Z", "#d8d2c6", 2.6))
        o.append(P(f"M{sx+sl*.25} {sy-sh*.6} L{sx+sl*.2} {sy-sh*1.3} L{sx+sl*.55} {sy-sh*.55} Z", "#d8d2c6", 2.6))
    if eye:
        o.append(C(hx - rx * .25, hy - ry * .22, 5.5, INK, 0) + C(hx - rx * .25 - 1.5, hy - ry * .22 - 2, 1.8, "#fff", 0))
    return "".join(o)


# ====================================================================== sitting small mammal (rodents etc.)
def blob(F="#e9c79a", L=220, H=150, belly="#fff8ec", ears="round", head=None, tail=None, snout=1, whisk=True, spines=False, nose="#e88a8a", cheeks=False, feet=True, stripe=None):
    o = []
    hr = head or H * .48
    if tail == "bushy":
        o.append(P(f"M{L*.3} {-H*.3} C{L*.8} {-H*.3} {L*.95} {-H*1.4} {L*.6} {-H*1.7} C{L*.4} {-H*1.6} {L*.5} {-H*1.2} {L*.45} {-H*1.0} C{L*.4} {-H*.8} {L*.3} {-H*.7} {L*.2} {-H*.6} Z", darker(F, .9), 3))
    if tail == "puff":
        o.append(C(L * .48, -H * .35, 20, "#fff", 2.8))
    if tail == "long":
        o.append(P(f"M{L*.4} {-H*.2} C{L*.8} {-H*.2} {L*.9} {-H*.9} {L*.75} {-H*1.2}", sw=14) + P(f"M{L*.4} {-H*.2} C{L*.8} {-H*.2} {L*.9} {-H*.9} {L*.75} {-H*1.2}", sw=9, col=F))
    body = f"M{-L*.45} {-H*.25} C{-L*.5} {-H*.9} {-L*.1} {-H*1.08} {L*.12} {-H} C{L*.5} {-H*.92} {L*.56} {-H*.3} {L*.42} {-4} L{-L*.36} -4 C{-L*.46} -4 {-L*.46} {-H*.1} {-L*.45} {-H*.25} Z"
    o.append(P(body, F))
    if spines:
        pts = []
        n = 34
        for i in range(n + 1):
            a = math.pi * (1.02 + 1.0 * i / n)
            r = 1.12 if i % 2 == 0 else 0.96
            pts.append((L * .06 + math.cos(a) * L * .5 * r, -H * .32 + math.sin(a) * H * .78 * r))
        pts += [(L * .5, -H * .2), (L * .3, -H * .35), (-L * .2, -H * .55), (-L * .38, -H * .4)]
        o.append(poly(pts, "#8f765c", 2.6))
        for i in range(0, n, 2):
            a = math.pi * (1.06 + 0.9 * i / n)
            o.append(P(f"M{L*.06+math.cos(a)*L*.3:.0f} {-H*.32+math.sin(a)*H*.45:.0f} L{L*.06+math.cos(a)*L*.5:.0f} {-H*.32+math.sin(a)*H*.75:.0f}", sw=2, col="#f2dfc4"))
    if stripe:
        o.append(clip(body, P(f"M{-L*.3} {-H*1.0} C{0} {-H*1.15} {L*.3} {-H*1.0} {L*.5} {-H*.7}", sw=18, col=stripe)))
    o.append(clip(body, E(-L * .1, -H * .05, L * .38, H * .34, belly, 0)))
    o.append(P(body, "none"))
    if feet:
        o.append(E(-L * .28, -4, 22, 9, darker(F, .9), 2.6) + E(L * .18, -4, 24, 10, darker(F, .9), 2.6))
    hx, hy = -L * .38, -H * .78
    if ears == "round":
        o.append(C(hx + hr * .45, hy - hr * .8, hr * .34, F, 2.8) + C(hx + hr * .45, hy - hr * .78, hr * .18, "#f6c9b0", 0))
    elif ears == "long":
        o.append(E(hx + hr * .5, hy - hr * 1.5, hr * .26, hr * .95, F, 2.8, rot=12) + E(hx + hr * .5, hy - hr * 1.46, hr * .12, hr * .7, "#f6c9b0", 0, rot=12))
        o.append(E(hx + hr * .9, hy - hr * 1.3, hr * .24, hr * .85, darker(F, .92), 2.8, rot=32))
    elif ears == "big":
        o.append(C(hx + hr * .5, hy - hr * .85, hr * .55, F, 2.8) + C(hx + hr * .5, hy - hr * .83, hr * .34, "#f6c9b0", 0))
    elif ears == "petal":
        o.append(E(hx + hr * .55, hy - hr * .55, hr * .34, hr * .22, darker(F, .9), 2.6, rot=-30))
    o.append(E(hx, hy, hr * 1.05, hr * .9, F))
    if cheeks:
        o.append(E(hx - hr * .1, hy + hr * .35, hr * .55, hr * .42, belly, 0))
    o.append(C(hx - hr * .4, hy - hr * .15, 6, INK, 0) + C(hx - hr * .42, hy - hr * .2, 2, "#fff", 0))
    nx, ny = hx - hr * 1.02, hy + hr * .12
    o.append(E(nx + 2, ny, 6, 5, nose, 1.8))
    if whisk:
        o.append(P(f"M{nx+6} {ny+4} l-38 -6 M{nx+6} {ny+6} l-36 8 M{nx+8} {ny+8} l-30 18", sw=1.6, col=GREY))
    return "".join(o)


# ====================================================================== bird (side, facing left)
def bird(F="#f2e3c8", wing=None, rx=90, ry=62, tilt=-10, neck=30, nw=36, hr=34, beak="short", beak_col=ORG, leg_len=70, leg_col=ORG, legw=5,
         tail="short", tail_col=None, crest=None, head_col=None, belly=None, eye_ring=None, wattle=None, extras="", front="", flat_feet=False, webbed=False, sit=False):
    wing = wing or darker(F, .85)
    hc = head_col or F
    o = []
    by = -(leg_len + ry * .9)
    tc = tail_col or wing
    if tail == "short":
        o.append(poly([(rx * .7, by - ry * .2), (rx * 1.45, by - ry * .5), (rx * 1.4, by + ry * .05), (rx * .8, by + ry * .35)], tc, 2.8))
    elif tail == "long":
        o.append(poly([(rx * .7, by - ry * .1), (rx * 2.2, by + ry * .5), (rx * 2.1, by + ry * .9), (rx * .7, by + ry * .4)], tc, 2.8))
    elif tail == "up":
        o.append(P(f"M{rx*.6} {by-ry*.3} C{rx*1.2} {by-ry*1.6} {rx*1.6} {by-ry*1.5} {rx*1.6} {by-ry*1.1} C{rx*1.4} {by-ry*.3} {rx*1.0} {by+ry*.2} {rx*.7} {by+ry*.3} Z", tc, 2.8))
    elif tail == "fan":
        o.append(P(f"M{rx*.6} {by} C{rx*1.0} {by-ry*1.2} {rx*1.2} {by-ry*1.5} {rx*1.5} {by-ry*1.1} C{rx*1.5} {by-ry*.4} {rx*1.2} {by+ry*.3} {rx*.7} {by+ry*.4} Z", tc, 2.8))
    elif tail == "fork":
        o.append(poly([(rx * .7, by - ry * .1), (rx * 1.7, by - ry * .1), (rx * 1.3, by + ry * .15), (rx * 1.7, by + ry * .5), (rx * .7, by + ry * .4)], tc, 2.8))
    # legs
    if not sit:
        for dx in (-rx * .18, rx * .15):
            x = dx
            o.append(P(f"M{x} {by+ry*.6} L{x+4} {-leg_len*.5} L{x-2} 0", sw=legw + 4) + P(f"M{x} {by+ry*.6} L{x+4} {-leg_len*.5} L{x-2} 0", sw=legw, col=leg_col))
            if webbed:
                o.append(P(f"M{x-2} -2 L{x-30} 0 L{x-22} -10 Z", leg_col, 2.4))
            else:
                o.append(P(f"M{x-2} 0 l-22 2 M{x-2} 0 l-14 -8 M{x-2} 0 l10 0", sw=3.2, col=INK))
    # body
    bd = f"M{-rx} {by} a{rx} {ry} 0 1 0 {2*rx} 0 a{rx} {ry} 0 1 0 {-2*rx} 0 Z"
    g = [E(0, by, rx, ry, F)]
    if belly:
        g.append(clip(bd, E(-rx * .3, by + ry * .5, rx * .8, ry * .6, belly, 0)) + E(0, by, rx, ry))
    g.append(P(f"M{-rx*.45} {by-ry*.35} C{-rx*.1} {by-ry*.75} {rx*.75} {by-ry*.6} {rx*1.05} {by+ry*.05} C{rx*.6} {by+ry*.55} {-rx*.1} {by+ry*.45} {-rx*.45} {by-ry*.35} Z", wing, 2.8))
    g.append(P(f"M{rx*.1} {by+ry*.05} q{rx*.3} {ry*.1} {rx*.55} 0 M{rx*.2} {by+ry*.25} q{rx*.3} {ry*.08} {rx*.5} -4", sw=2, col=GREY))
    o.append(f'<g transform="rotate({tilt} 0 {by})">' + "".join(g) + "</g>")
    o.append(extras)
    # neck/head
    nx, ny = -rx * .72, by - ry * .3
    hx, hy = nx - neck * .35, ny - neck - hr * .6
    if neck > 0:
        o.append(P(f"M{nx+nw*.5} {ny} L{hx+nw*.35} {hy} L{hx-nw*.35} {hy} L{nx-nw*.5} {ny+10} Z", hc if neck > 60 else F, 0))
        o.append(P(f"M{nx+nw*.5} {ny} L{hx+nw*.35} {hy} M{hx-nw*.35} {hy} L{nx-nw*.5} {ny+10}"))
    if crest == "peacock":
        for i in range(5):
            o.append(P(f"M{hx+4} {hy-hr} l{-8+i*5} {-26}", sw=1.8) + C(hx + 4 - 8 + i * 5, hy - hr - 28, 4, BLUE, 0))
    elif crest == "comb":
        o.append(P(f"M{hx-hr*.6} {hy-hr*.7} q2 -26 14 -16 q6 -24 16 -8 q10 -20 16 2 q8 -10 10 10 Z", "#e2483c", 2.6))
    elif crest == "red":
        o.append(E(hx + 2, hy - hr * .7, hr * .45, hr * .3, "#e2483c", 0))
    elif crest == "tuft":
        o.append(P(f"M{hx+hr*.2} {hy-hr*.9} l18 -22 l-2 26 Z", hc, 2.4))
    o.append(C(hx, hy, hr, hc))
    if eye_ring:
        o.append(C(hx - hr * .2, hy - hr * .15, hr * .34, eye_ring, 2))
    o.append(C(hx - hr * .2, hy - hr * .15, 5, INK, 0) + C(hx - hr * .23, hy - hr * .2, 1.8, "#fff", 0))
    bx = hx - hr * .9
    if beak == "short":
        o.append(poly([(bx + 4, hy - hr * .25), (bx - hr * .7, hy + hr * .05), (bx + 4, hy + hr * .3)], beak_col, 2.6))
    elif beak == "cone":
        o.append(poly([(bx + 6, hy - hr * .35), (bx - hr * .55, hy + hr * .05), (bx + 6, hy + hr * .4)], beak_col, 2.6))
    elif beak == "hook":
        o.append(P(f"M{bx+6} {hy-hr*.4} C{bx-hr*.6} {hy-hr*.5} {bx-hr*.8} {hy+hr*.1} {bx-hr*.5} {hy+hr*.55} C{bx-hr*.4} {hy+hr*.2} {bx-hr*.1} {hy+hr*.2} {bx+6} {hy+hr*.3} Z", beak_col, 2.6))
    elif beak == "duck":
        o.append(P(f"M{bx+6} {hy-hr*.15} L{bx-hr*.8} {hy-hr*.05} Q{bx-hr*1.0} {hy+hr*.25} {bx-hr*.7} {hy+hr*.32} L{bx+6} {hy+hr*.35} Z", beak_col, 2.6))
    elif beak == "long":
        o.append(poly([(bx + 6, hy - hr * .2), (bx - hr * 1.8, hy + hr * .15), (bx + 6, hy + hr * .25)], beak_col, 2.6))
    elif beak == "needle":
        o.append(P(f"M{bx+4} {hy} L{bx-hr*2.2} {hy+4}", sw=4))
    elif beak == "flamingo":
        o.append(P(f"M{bx+6} {hy-hr*.35} L{bx-hr*.6} {hy-hr*.2} C{bx-hr*.9} {hy} {bx-hr*.9} {hy+hr*.5} {bx-hr*.7} {hy+hr*.9} C{bx-hr*.5} {hy+hr*.5} {bx-hr*.2} {hy+hr*.3} {bx+6} {hy+hr*.35} Z", "#fff", 2.6) +
                 P(f"M{bx-hr*.62} {hy-hr*.15} C{bx-hr*.9} {hy} {bx-hr*.9} {hy+hr*.5} {bx-hr*.7} {hy+hr*.9} L{bx-hr*.62} {hy+hr*.4} Z", INK, 0))
    if wattle:
        o.append(E(bx + 2, hy + hr * .75, hr * .2, hr * .35, "#e2483c", 2.4))
    o.append(front)
    return "".join(o)


# ====================================================================== fish / cetacean (side, facing left)
def fish(F=ORG_L, L=300, H=150, tail="fork", tail_col=None, dorsal=True, dorsal_col=None, stripes=None, spots=None, eye_r=10, mouth=True,
         belly=None, gills=0, cetacean=False, fin_col=None, extras="", pectoral=True, tall_dorsal=False):
    tc = tail_col or F
    fc = fin_col or darker(F, .9)
    o = []
    x0, x1 = -L / 2, L / 2
    body = f"M{x0} 0 C{x0+L*.1} {-H*.62} {x1-L*.35} {-H*.62} {x1-L*.05} {-H*.1} L{x1-L*.05} {H*.1} C{x1-L*.35} {H*.55} {x0+L*.1} {H*.55} {x0} 0 Z"
    tx = x1 - L * .07
    if tail == "fork":
        o.append(P(f"M{tx} 0 L{tx+L*.22} {-H*.55} Q{tx+L*.14} 0 {tx+L*.22} {H*.55} Z", tc, 2.8))
    elif tail == "round":
        o.append(P(f"M{tx} 0 C{tx+L*.18} {-H*.55} {tx+L*.3} {-H*.3} {tx+L*.28} 0 C{tx+L*.3} {H*.3} {tx+L*.18} {H*.55} {tx} 0 Z", tc, 2.8))
    elif tail == "fan":
        o.append(P(f"M{tx} 0 C{tx+L*.3} {-H*.9} {tx+L*.5} {-H*.5} {tx+L*.42} {-H*.1} C{tx+L*.5} {H*.4} {tx+L*.3} {H*.9} {tx} 0 Z", tc, 2.8, extra='fill-opacity=".85"'))
        o.append(P(f"M{tx+4} 0 q{L*.2} {-H*.3} {L*.36} {-H*.25} M{tx+4} 0 q{L*.2} {H*.3} {L*.36} {H*.3}", sw=1.8, col=ORG))
    elif tail == "shark":
        o.append(P(f"M{tx} {-H*.08} L{tx+L*.2} {-H*.75} Q{tx+L*.12} {-H*.1} {tx+L*.15} {H*.45} Z", tc, 2.8))
    elif tail == "fluke":
        o.append(P(f"M{tx} {-H*.05} C{tx+L*.08} {-H*.2} {tx+L*.16} {-H*.45} {tx+L*.24} {-H*.42} C{tx+L*.2} {-H*.15} {tx+L*.2} {H*.05} {tx+L*.26} {H*.25} C{tx+L*.16} {H*.25} {tx+L*.08} {H*.1} {tx} {H*.06} Z", tc, 2.8))
    if dorsal:
        dc = dorsal_col or fc
        if tall_dorsal:
            o.append(P(f"M{-L*.05} {-H*.48} L{L*.05} {-H*1.25} L{L*.16} {-H*.42} Z", dc, 2.8))
        elif cetacean or tail == "shark":
            o.append(P(f"M{-L*.05} {-H*.5} C{L*.02} {-H*.75} {L*.08} {-H*.9} {L*.12} {-H*.95} C{L*.1} {-H*.7} {L*.12} {-H*.55} {L*.18} {-H*.42} Z", dc, 2.8))
        else:
            o.append(P(f"M{-L*.15} {-H*.45} C{-L*.05} {-H*.95} {L*.2} {-H*.85} {L*.25} {-H*.4} Z", dc, 2.8))
            o.append(P(f"M{L*.0} {H*.4} L{L*.12} {H*.7} L{L*.2} {H*.36} Z", dc, 2.6))
    inner = ""
    if belly:
        inner += E(-L * .05, H * .38, L * .48, H * .3, belly, 0)
    if stripes:
        col, xs = stripes
        for xx in xs:
            inner += P(f"M{x0+L*xx} {-H} C{x0+L*xx-18} {-H*.3} {x0+L*xx-18} {H*.3} {x0+L*xx} {H}", sw=22, col=INK) + P(f"M{x0+L*xx} {-H} C{x0+L*xx-18} {-H*.3} {x0+L*xx-18} {H*.3} {x0+L*xx} {H}", sw=15, col=col)
    if spots:
        for i in range(60):
            inner += C(x0 + 30 + (i * 37) % int(L - 40), -H * .45 + (i * 23) % int(H * .6), 4, spots, 0)
    if inner:
        o.append(P(body, F) + clip(body, inner))
    o.append(P(body, "none" if inner else F))
    for g in range(gills):
        gx = x0 + L * (.2 + g * .035)
        o.append(P(f"M{gx} {-H*.2} q-6 {H*.2} 0 {H*.38}", sw=2.4))
    if pectoral:
        o.append(P(f"M{x0+L*.28} {H*.08} C{x0+L*.36} {H*.18} {x0+L*.4} {H*.5} {x0+L*.32} {H*.62} C{x0+L*.28} {H*.42} {x0+L*.24} {H*.25} {x0+L*.26} {H*.12} Z", fc, 2.6))
    ex = x0 + L * .12
    o.append(C(ex, -H * .12, eye_r, "#fff", 2.4) + C(ex - 1, -H * .12, eye_r * .55, INK, 0))
    if mouth:
        o.append(P(f"M{x0+4} {H*.04} q{L*.04} {H*.08} {L*.09} {H*.04}", sw=2.4))
    o.append(extras)
    return "".join(o)


# ====================================================================== turtle
def turtle(shell="#a7c48f", skin="#b9cf9a", L=300, H=120, sea=False, stripes=None, scute="#7f9f6a", neck=40, ear_patch=None, plastron="#f3e3a6"):
    o = []
    x0, x1 = -L / 2, L / 2
    if sea:
        o.append(P(f"M{x0+40} {-H*.2} C{x0-20} {-H*.1} {x0-60} {H*.3} {x0-90} {H*.6} C{x0-40} {H*.55} {x0} {H*.3} {x0+60} {H*.05} Z", skin, 2.8))
        o.append(P(f"M{x1-50} {-H*.1} C{x1} {0} {x1+30} {H*.3} {x1+40} {H*.5} C{x1} {H*.4} {x1-30} {H*.2} {x1-60} {H*.1} Z", skin, 2.8))
    else:
        for x in (x0 + 60, x1 - 60):
            o.append(R(x - 20, -H * .25, 40, H * .25, skin, 12, 2.8))
            o.append(P(f"M{x-14} -2 v-6 M{x} -2 v-6 M{x+14} -2 v-6", sw=2))
        o.append(P(f"M{x1-10} {-H*.3} l34 14 l-30 6 Z", skin, 2.6))
    hx, hy = x0 - neck * .6, -H * .55 - (0 if not sea else -H * .2)
    o.append(P(f"M{x0+30} {-H*.3} L{hx+10} {hy-16} L{hx+14} {hy+18} L{x0+30} {-H*.08} Z", skin, 2.8))
    o.append(E(hx, hy, 34, 24, skin))
    if stripes:
        o.append(P(f"M{hx+30} {hy+8} L{x0+30} {-H*.18} M{hx+24} {hy+18} L{x0+30} {-H*.12}", sw=2.4, col=stripes))
    if ear_patch:
        o.append(E(hx + 14, hy + 2, 12, 6, ear_patch, 0))
    o.append(C(hx - 12, hy - 6, 5, INK, 0) + P(f"M{hx-32} {hy+8} q10 4 20 0", sw=2.2))
    o.append(P(f"M{x0} {-H*.2} L{x1} {-H*.2} L{x1-10} {-H*.05} L{x0+10} {-H*.05} Z", plastron, 2.6))
    sh = f"M{x0} {-H*.2} C{x0+10} {-H*1.2} {x1-10} {-H*1.2} {x1} {-H*.2} Z"
    o.append(P(sh, shell))
    sc = ""
    for i in range(-1, 2):
        sc += P(f"M{i*L*.22-L*.1} {-H*.82} L{i*L*.22+L*.1} {-H*.82} L{i*L*.22+L*.13} {-H*.45} L{i*L*.22-L*.13} {-H*.45} Z", scute, 2.4)
    o.append(clip(sh, sc) + P(sh, "none"))
    o.append(P(f"M{x0+10} {-H*.32} L{x1-10} {-H*.32}", sw=2.2))
    return "".join(o)


# ====================================================================== pets
def a_dog(w, h):
    a = quad(F="#e8c08a", bl=250, bd=110, lh=100, lw=32, belly="#fff4e2", neck=(26, 40), nw=80, head=(60, 52), snout=(50, 38), snout_col="#f6e1c0",
             ears="droop", tail="thin", tail_col="#e8c08a", front_extras="")
    collar = P("M-150 -270 q16 18 48 6", sw=10) + P("M-150 -270 q16 18 48 6", sw=6, col=BLUE) + C(-128, -258, 8, YEL, 2.4)
    ball = C(260, -24, 24, YEL_L, 2.8) + P("M240 -36 q20 12 40 -2 M240 -12 q20 -12 40 2", sw=2, col=YEL)
    return scene("meadow", w, h, a, box=(w / 2 - 20, h * .76, 560, 400), extra="") .replace("</svg>", f"{G_(ball, w/2+250, h*.8)}</svg>")


def G_(b, x, y, s=1):
    return f'<g transform="translate({x:.0f} {y:.0f}) scale({s})">{b}</g>'


def a_rabbit(w, h):
    return scene("meadow", w, h, blob(F="#f1ece4", L=240, H=170, belly="#ffffff", ears="long", tail="puff", nose="#f2a0a0", whisk=True),
                 extra=G_(P("M0 0 C-20 -40 -10 -70 10 -80 C24 -60 24 -30 0 0 Z", ORG, 2.6) + P("M10 -80 l-10 -24 M10 -80 l14 -20 M10 -80 l2 -28", sw=3, col=SAGE), 690, 470))


def a_hamster(w, h):
    return scene("home", w, h, blob(F="#e9b97a", L=230, H=160, belly="#fff6e6", ears="round", cheeks=True, stripe=None),
                 box=(w / 2 + 20, h * .74, 440, 300), extra=G_(P("M-40 0 L-40 -36 L40 -36 L40 0", "#fff", 2.6) + E(0, -36, 40, 10, "#f6e1c0", 2.4) + "".join(C(-24 + i * 12, -40, 5, "#c9a27a", 1.8) for i in range(5)), 720, 460))


def a_goldfish(w, h):
    f = fish(F="#f7a24a", L=210, H=130, tail="fan", tail_col="#fbc98a", belly="#fde3c0", eye_r=11, fin_col="#fbc98a")
    return scene("tank", w, h, f, box=(w / 2, 330, 330, 210))


def a_budgie(w, h):
    b = bird(F="#a9d77c", wing="#e9e6a0", rx=58, ry=42, tilt=-30, neck=6, nw=40, hr=30, beak="hook", beak_col="#e9d8b8", leg_len=30, leg_col="#9aa2c8",
             tail="long", tail_col="#4f7fc9", head_col="#f6e26a", belly="#a9d77c")
    b += "".join(P(f"M{-70+i*12} {-120-i*2} q6 -4 12 0", sw=2.4) for i in range(4))
    perch = P("M-140 0 H140", sw=12) + P("M-140 0 H140", sw=7, col="#d9c3a0")
    return scene("home", w, h, b + perch, box=(w / 2 + 40, h * .62, 420, 330))


def a_guinea(w, h):
    return scene("home", w, h, blob(F="#c98a55", L=260, H=150, belly="#fff4e2", ears="petal", tail=None, stripe="#fff6e6", nose="#8a5a3a"),
                 box=(w / 2 + 20, h * .74, 480, 300),
                 extra=G_(P("M-30 0 C-40 -20 -10 -40 0 -60 C10 -40 40 -20 30 0 Z", SAGE_L, 2.6) + P("M0 0 V-50", sw=2, col=SAGE), 700, 470))


def a_slider(w, h):
    t = turtle(shell="#7fa36a", skin="#9fbf7f", stripes=YEL, ear_patch="#e2483c", scute="#6b8f58")
    return scene("pond", w, h, t, box=(w / 2 - 40, h * .76, 460, 260))


def a_guppy(w, h):
    f1 = fish(F="#c9d3dc", L=150, H=60, tail="fan", tail_col="#f08a4b", eye_r=7, fin_col="#7fb0e8", dorsal_col="#7fb0e8")
    f2 = G_(fish(F="#d9dde2", L=180, H=70, tail="round", tail_col="#c9ccd1", eye_r=7), 160, 90, .9)
    return scene("tank", w, h, f1 + f2, box=(w / 2, 340, 420, 220))


def a_hedgehog(w, h):
    return scene("meadow", w, h, blob(F="#f2dfc4", L=260, H=160, belly="#fff6e6", ears="round", spines=True, nose=INK, whisk=False),
                 box=(w / 2, h * .76, 480, 300), extra=G_(C(0, -16, 16, "#e2483c", 2.6) + P("M0 -32 q4 -10 10 -12", sw=2.4, col=SAGE), 700, 470))


def a_chinchilla(w, h):
    return scene("home", w, h, blob(F="#c9ccd1", L=230, H=170, belly="#f4f5f6", ears="big", tail="bushy", nose="#e8a0a0"),
                 box=(w / 2 + 10, h * .74, 480, 330))


ART2 = {"dog": a_dog, "rabbit": a_rabbit, "hamster": a_hamster, "goldfish": a_goldfish, "budgie": a_budgie, "guinea-pig": a_guinea,
        "slider": a_slider, "guppy": a_guppy, "hedgehog": a_hedgehog, "chinchilla": a_chinchilla}
