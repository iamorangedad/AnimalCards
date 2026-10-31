"""Phase-4 art (cards 401-1000): plants, fungi (parametric) + new animals using the shared helpers."""
import math
from iso import INK, GREY, MUTE, BLUE, BLUE_L, BLUE_M, ORG, ORG_L, YEL, YEL_L, SAGE, SAGE_L
from art import P, E, C, svg, slab, shadow, tuft, rock, sun, seaweed, wavy, bamboo
from art2 import uid, fit, R, poly, clip, darker, tree, pine, mountains, flower, bubbles, G_, scene, quad, fish, turtle, bird, blob, ape

ART5 = {}
LEAF, LEAF_D, STEM = "#8fcf6a", "#4f9a3a", "#5f9a4a"
def f1(v): return f"{v:.1f}"

# ------------------------------------------------------------------ primitives
def leaf(x, y, ang, L=60, W=None, col=LEAF, vein=True, sw=2.4):
    W = L * 0.38 if W is None else W
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); nx, ny = -uy, ux
    tx, ty = x + ux * L, y + uy * L
    c1 = (x + ux * L * .35 + nx * W, y + uy * L * .35 + ny * W); c2 = (x + ux * L * .35 - nx * W, y + uy * L * .35 - ny * W)
    d = f"M{f1(x)} {f1(y)} Q{f1(c1[0])} {f1(c1[1])} {f1(tx)} {f1(ty)} Q{f1(c2[0])} {f1(c2[1])} {f1(x)} {f1(y)} Z"
    o = P(d, col, sw)
    if vein: o += P(f"M{f1(x)} {f1(y)} L{f1(x+ux*L*.85)} {f1(y+uy*L*.85)}", sw=1.6, col=darker(col, .7))
    return o

def line(d, sw=7, col=STEM):
    return P(d, sw=sw + 3.4) + P(d, sw=sw, col=col)

def stalk(x0, y0, x1, y1, bend=0, sw=7, col=STEM):
    mx, my = (x0 + x1) / 2 + bend, (y0 + y1) / 2
    return line(f"M{f1(x0)} {f1(y0)} Q{f1(mx)} {f1(my)} {f1(x1)} {f1(y1)}", sw, col)

def rot_ell(cx, cy, r, ang, rx, ry, col, sw=2.2):
    a = math.radians(ang)
    return E(cx + math.cos(a) * r, cy + math.sin(a) * r, rx, ry, col, sw, INK, ang)

def petals(x, y, n=5, r=26, rx=None, ry=None, col="#f6a6c0", center=YEL, cr=None, rot=0, sw=2.2):
    rx = rx or r * .62; ry = ry or r * .42
    o = "".join(rot_ell(x, y, r * .62, rot + 360 * i / n, rx, ry, col, sw) for i in range(n))
    return o + (C(x, y, cr or r * .32, center, sw) if center else "")

def daisy(x, y, r=30, col="#ffffff", center=YEL, n=18):
    return petals(x, y, n, r, r * .55, r * .14, col, center, r * .34)

def pompom(x, y, r=34, col="#f6d43a", rings=3):
    o = C(x, y, r, col, 2.4)
    for k in range(1, rings + 1):
        rr = r * (1 - k / (rings + 1)); n = 6 + k * 3
        o += "".join(P(f"M{f1(x+math.cos(t)*rr)} {f1(y+math.sin(t)*rr)} q{f1(math.cos(t+1.2)*6)} {f1(math.sin(t+1.2)*6)} {f1(math.cos(t)*-5)} {f1(math.sin(t)*-5)}", sw=1.8, col=darker(col, .7))
                     for t in [2 * math.pi * i / n + k for i in range(n)])
    return P(wavy(x, y, r, r, 14, r * .12), col, 2.4) + o[len(C(x, y, r, col, 2.4)):]

def rose(x, y, r=30, col="#e8485a"):
    o = "".join(C(x + math.cos(2 * math.pi * i / 6) * r * .45, y + math.sin(2 * math.pi * i / 6) * r * .45, r * .55, col, 2.2) for i in range(6))
    o += C(x, y, r * .6, darker(col, .92), 2.2)
    o += P(f"M{f1(x)} {f1(y)} a{r*.18} {r*.18} 0 1 1 {f1(r*.22)} {f1(-r*.1)} a{r*.34} {r*.34} 0 1 1 {f1(-r*.5)} {f1(r*.18)}", sw=2, col=INK)
    return o

def cup(x, y, r=30, col="#e8485a"):  # tulip-like
    d = f"M{f1(x-r)} {f1(y-r*.6)} Q{f1(x-r)} {f1(y+r)} {f1(x)} {f1(y+r)} Q{f1(x+r)} {f1(y+r)} {f1(x+r)} {f1(y-r*.6)} L{f1(x+r*.5)} {f1(y-r*.1)} L{f1(x)} {f1(y-r*.9)} L{f1(x-r*.5)} {f1(y-r*.1)} Z"
    return P(d, col, 2.4) + P(f"M{f1(x)} {f1(y-r*.9)} Q{f1(x-r*.2)} {f1(y+r*.3)} {f1(x)} {f1(y+r)}", sw=1.8, col=darker(col, .75))

def trumpet(x, y, ang=-90, L=60, r=30, col="#ffffff", throat=YEL):
    a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); nx, ny = -uy, ux
    bx, by = x + ux * L, y + uy * L
    d = (f"M{f1(x+nx*6)} {f1(y+ny*6)} L{f1(bx+nx*r)} {f1(by+ny*r)} Q{f1(bx+ux*r*.4)} {f1(by+uy*r*.4)} {f1(bx-nx*r)} {f1(by-ny*r)} L{f1(x-nx*6)} {f1(y-ny*6)} Z")
    return P(d, col, 2.4) + E(bx, by, r, r * .36, darker(col, .96), 2.2, INK, ang + 90) + E(bx - ux * 4, by - uy * 4, r * .4, r * .16, throat, 0, INK, ang + 90)

def bell(x, y, r=12, col="#ffffff"):
    return P(f"M{f1(x-r)} {f1(y+r)} Q{f1(x-r)} {f1(y-r*.8)} {f1(x)} {f1(y-r*.8)} Q{f1(x+r)} {f1(y-r*.8)} {f1(x+r)} {f1(y+r)} q{f1(-r*.5)} {f1(-r*.3)} {f1(-r)} 0 q{f1(-r*.5)} {f1(-r*.3)} {f1(-r)} 0 Z", col, 2.2)

def spike(x, y, H=90, r=8, col="#9a7ad9", n=8, side=True):
    o = stalk(x, y, x, y - H, 0, 4)
    for i in range(n):
        yy = y - H * .35 - i * (H * .65 / n)
        o += E(x - r * .7, yy, r, r * .6, col, 2) + E(x + r * .7, yy - r * .4, r, r * .6, col, 2) if side else E(x, yy, r, r * .7, col, 2)
    return o

def cluster(x, y, r=40, col="#8ab8f0"):
    o = C(x, y, r, darker(col, .92), 2.4)
    for i in range(16):
        t = i * 2.4; rr = r * .72 * math.sqrt((i + .5) / 16)
        o += petals(x + math.cos(t) * rr, y + math.sin(t) * rr, 4, 9, 7, 5, col, darker(col, .7), 2.2, i * 20, 1.6)
    return o

def seedhead(x, y, r=34):
    o = "".join(P(f"M{x} {y} L{f1(x+math.cos(t)*r)} {f1(y+math.sin(t)*r)}", sw=1.4, col=GREY) + C(x + math.cos(t) * r, y + math.sin(t) * r, 3, "#fff", 1.4)
                for t in [2 * math.pi * i / 28 for i in range(28)])
    return o + C(x, y, 6, "#d9c9a0", 2)

def leaves_along(x, y0, y1, n=4, L=60, col=LEAF, spread=40, droop=0):
    o = ""
    for i in range(n):
        yy = y0 + (y1 - y0) * (i + .5) / n; s = -1 if i % 2 else 1
        o += leaf(x, yy, (-90 + s * (spread + 20)) + s * droop, L, None, col)
    return o

def herb(flower_fn, H=220, n_leaf=4, leafL=60, leafcol=LEAF, stems=((0, 0),), bend=20, basal=False):
    """generic flowering plant: stems=[(dx, dh)], flower_fn(x, y) at top."""
    o = ""
    for k, (dx, dh) in enumerate(stems):
        top = -(H + dh)
        o += stalk(0, 0, dx, top, bend * (1 if k % 2 == 0 else -1), 6)
        if not basal: o += leaves_along(dx * .5, -20, top * .6, n_leaf, leafL, leafcol)
    if basal: o += "".join(leaf(0, 0, -90 + a, leafL * 1.3, None, leafcol) for a in (-60, -30, 30, 60, -75, 75))
    for dx, dh in stems: o += flower_fn(dx, -(H + dh))
    return o

def pot(w=150, h=110, col="#d9895a"):
    return P(f"M{-w/2} {-h} L{w/2} {-h} L{w/2*.8} 0 L{-w/2*.8} 0 Z", col, 2.8) + R(-w / 2 - 8, -h - 18, w + 16, 22, darker(col, .92), 3, 2.8)

def potted(body, w=150, h=110, col="#d9895a"):
    return pot(w, h, col) + G_(body, 0, -h - 14)

def PL(kind, body, box=(.76, 560, 440)):
    return lambda w, h: scene(kind, w, h, body, box=(w / 2, h * box[0], box[1], box[2]))

# ------------------------------------------------------------------ trees
BARK = "#a8825a"
def trunk(H=220, w0=34, w1=20, col=BARK, lines=True):
    o = P(f"M{-w0/2} 0 Q{-w1/2-4} {-H*.5} {-w1/2} {-H} L{w1/2} {-H} Q{w1/2+4} {-H*.5} {w0/2} 0 Z", col, 2.8)
    if lines: o += P(f"M{-w0*.15} {-H*.15} q-4 -30 0 -60 M{w0*.15} {-H*.45} q4 -24 0 -48", sw=1.8, col=darker(col, .7))
    return o

def crown_round(cx, cy, rx, ry, col=SAGE_L, n=11):
    return P(wavy(cx, cy, rx, ry, n, min(rx, ry) * .1), col, 2.8) + P(f"M{cx-rx*.45} {cy-ry*.1} q{rx*.3} {-ry*.25} {rx*.6} {-ry*.05}", sw=2, col=darker(col, .7))

def T_round(H=200, rx=150, ry=120, col="#bfe0a8", bark=BARK, tw=36):
    return trunk(H, tw, tw * .6, bark) + crown_round(0, -H - ry * .55, rx, ry, col)

def T_cone(H=380, W=150, col="#9cc98a", bark=BARK, tiers=4, tw=24):
    o = trunk(H * .25, tw, tw * .7, bark)
    for i in range(tiers):
        y0 = -H * .18 - i * H * .2; ww = W * (1 - i * .2)
        o += poly([(-ww, y0), (0, y0 - H * .38), (ww, y0)], col, 2.8)
    return o

def T_column(H=440, W=70, col="#8fbf7a", bark="#a8603a", tw=40):
    return trunk(H * .45, tw, tw * .7, bark) + P(wavy(0, -H * .62, W, H * .4, 12, 8), col, 2.8)

def T_palm(H=360, col="#8fcf6a", bark="#b89a6a", fruit=None, lean=30, n=7):
    o = P(f"M-14 0 Q{lean*.6} {-H*.5} {lean} {-H} L{lean+16} {-H} Q{lean*.6+20} {-H*.5} 16 0 Z", bark, 2.8)
    o += "".join(P(f"M{-10+i*.0} {-H*i/7:.0f} l26 0", sw=1.6, col=darker(bark, .7)) for i in range(1, 7))
    tx, ty = lean + 8, -H
    for i in range(n):
        a = math.radians(-170 + i * (160 / (n - 1))); L = 150
        ex, ey = tx + math.cos(a) * L, ty + math.sin(a) * L * .6 + 40
        o += P(f"M{tx} {ty} Q{tx+math.cos(a)*L*.5} {ty+math.sin(a)*L*.5-30} {f1(ex)} {f1(ey)} Q{tx+math.cos(a)*L*.5} {ty+math.sin(a)*L*.5-10} {tx} {ty} Z", col, 2.4)
    if fruit: o += "".join(C(tx - 14 + i * 14, ty + 18 + (i % 2) * 6, 13, fruit, 2.2) for i in range(3))
    return o

def T_weeping(H=200, rx=170, ry=120, col="#bfe0a8", bark=BARK):
    o = trunk(H, 36, 22, bark) + crown_round(0, -H - ry * .3, rx, ry * .7, col)
    o += "".join(P(f"M{x} {-H-ry*.1} q{(x%30)-15} {ry*.6} {x*.04} {ry*1.3}", sw=3, col=darker(col, .75)) for x in range(-int(rx * .9), int(rx * .9), 22))
    return o

def T_umbrella(H=220, W=220, col="#9cc98a", bark="#b8a08a", forks=True):
    o = trunk(H * .55, 40, 26, bark)
    if forks: o += line(f"M0 {-H*.5} L{-W*.4} {-H*.9} M0 {-H*.5} L{W*.4} {-H*.9} M0 {-H*.55} L0 {-H*.95}", 12, bark)
    return o + P(f"M{-W} {-H*.92} Q0 {-H*1.5} {W} {-H*.92} Q0 {-H*.78} {-W} {-H*.92} Z", col, 2.8)

def T_baobab(H=240, col="#bfe0a8", bark="#c9b8a0"):
    o = P(f"M-90 0 Q-110 {-H*.5} -50 {-H} L50 {-H} Q110 {-H*.5} 90 0 Z", bark, 2.8)
    o += line(f"M-40 {-H} L-110 {-H-70} M-10 {-H} L-30 {-H-100} M20 {-H} L60 {-H-90} M40 {-H} L120 {-H-60}", 12, bark)
    return o + "".join(crown_round(x, -H - y, 44, 28, col, 7) for x, y in ((-110, 80), (-30, 110), (60, 100), (120, 70)))

def T_bamboo(n=5, H=420, col="#8fbf5a"):
    o = ""
    for i in range(n):
        x = -120 + i * 60; h = H * (.8 + .2 * ((i * 7) % 3) / 2)
        o += line(f"M{x} 0 L{x+(i-2)*6} {-h}", 14, col)
        o += "".join(P(f"M{x-8+(i-2)*6*k/6} {-h*k/6} h16", sw=2.4) for k in range(1, 6))
        o += leaf(x + (i - 2) * 6, -h, -60 - i * 15, 70, 14, LEAF) + leaf(x + (i - 2) * 6, -h + 40, -130 + i * 10, 64, 13, LEAF)
    return o

def needles_tier(y, w, col):
    return P(f"M{-w} {y} q{w} {-30} {2*w} 0", col, 2.6)

def T_monkey(H=360, col="#6f9a4a", bark="#8a7a6a"):
    o = trunk(H, 30, 20, bark)
    for i in range(5):
        y = -H * .45 - i * H * .13; w = 140 - i * 22
        o += line(f"M0 {y} Q{-w*.5} {y-20} {-w} {y+20}", 12, col) + line(f"M0 {y} Q{w*.5} {y-20} {w} {y+20}", 12, col)
    return o

def T_cycad(col="#6faa4a", bark="#8a6a4a", H=110):
    o = P(f"M-34 0 L-28 {-H} L28 {-H} L34 0 Z", bark, 2.8) + "".join(P(f"M-30 {-k*18} h60", sw=1.6, col=darker(bark, .7)) for k in range(1, 6))
    for a in range(-170, 0, 22):
        r = math.radians(a); ex, ey = math.cos(r) * 170, -H + math.sin(r) * 120 + 30
        o += line(f"M0 {-H} Q{ex*.5} {-H+math.sin(r)*120-30} {f1(ex)} {f1(ey)}", 3, col)
        o += "".join(P(f"M{f1(ex*t)} {f1(-H+(ey+H)*t-14*math.sin(math.pi*t))} l{f1(-math.sin(r)*14)} {f1(math.cos(r)*14)} M{f1(ex*t)} {f1(-H+(ey+H)*t-14*math.sin(math.pi*t))} l{f1(math.sin(r)*14)} {f1(-math.cos(r)*14)}", sw=2.2, col=col) for t in (.3, .45, .6, .75, .9))
    return o

# ------------------------------------------------------------------ crops / veg / fruit
def grain(kind="wheat", n=5, H=300, col="#e6c35a", leafcol="#a8c86a"):
    o = ""
    for i in range(n):
        x = -100 + i * 50; h = H * (.9 + .1 * (i % 2))
        o += stalk(x, 0, x + (i - n // 2) * 8, -h, 6, 4, leafcol)
        o += leaf(x, -h * .35, -60 if i % 2 else -120, 90, 10, leafcol)
        tx, ty = x + (i - n // 2) * 8, -h
        if kind in ("wheat", "barley", "rye"):
            for k in range(7):
                yy = ty - k * 12; o += E(tx - 6, yy, 7, 5, col, 1.8, INK, -30) + E(tx + 6, yy - 4, 7, 5, col, 1.8, INK, 30)
                if kind in ("barley", "rye"): o += P(f"M{tx-10} {yy-2} l-14 -26 M{tx+10} {yy-6} l14 -26", sw=1.4, col=darker(col, .7))
        elif kind == "rice":
            o += line(f"M{tx} {ty} Q{tx+40} {ty-30} {tx+60} {ty+30}", 3, darker(col, .85))
            o += "".join(E(tx + 10 + k * 8, ty - 14 + k * 6 + (k * k) * .6, 5, 8, col, 1.6, INK, 30) for k in range(7))
        elif kind == "sorghum":
            o += P(wavy(tx, ty - 30, 22, 36, 10, 5), col, 2.2) + "".join(C(tx - 12 + (k % 3) * 12, ty - 50 + (k // 3) * 14, 5, darker(col, .8), 1.4) for k in range(9))
        elif kind == "millet":
            o += line(f"M{tx} {ty} Q{tx+30} {ty-20} {tx+44} {ty+40}", 16, col) + P(f"M{tx} {ty} Q{tx+30} {ty-20} {tx+44} {ty+40}", sw=1.2, col=darker(col, .7), extra='stroke-dasharray="2 4"')
        elif kind == "oat":
            o += "".join(P(f"M{tx} {ty-k*16} l{18*(1 if k%2 else -1)} 14", sw=2) + E(tx + 22 * (1 if k % 2 else -1), ty - k * 16 + 22, 5, 10, col, 1.6) for k in range(5))
        elif kind == "quinoa":
            o += P(wavy(tx, ty - 26, 26, 40, 10, 6), col, 2.2) + "".join(C(tx - 14 + (k % 3) * 14, ty - 46 + (k // 3) * 14, 5, darker(col, .85), 1.4) for k in range(9))
    return o

def corn(H=360):
    o = stalk(0, 0, 0, -H, 0, 10, "#8fbf5a")
    o += "".join(leaf(0, -H * (.15 + i * .15), (-30 if i % 2 else -150), 150, 16, "#a8d06a") for i in range(5))
    o += P(f"M0 {-H} l-20 -40 M0 {-H} l0 -50 M0 {-H} l20 -40 M0 {-H} l-36 -26 M0 {-H} l36 -26", sw=3, col="#c9a04a")
    o += E(28, -H * .5, 16, 50, "#f6d43a", 2.4, INK, 20) + "".join(P(f"M{22+k*4} {-H*.5-40} l6 70", sw=1, col="#c9a020") for k in range(3))
    o += P(f"M10 {-H*.5+40} Q4 {-H*.5} 20 {-H*.5-50} M44 {-H*.5+36} Q50 {-H*.5} 40 {-H*.5-46}", "#a8d06a", 2.4)
    return o

def shrub(W=200, H=160, col="#9cc98a", fruits=None, fr=10, fcol="#e8485a", trunk_h=30):
    o = trunk(trunk_h, 18, 14, BARK, False) if trunk_h else ""
    o += crown_round(0, -trunk_h - H * .5, W / 2, H / 2, col, 9)
    if fruits:
        for i in range(fruits):
            t = i * 2.4; rr = math.sqrt((i + .5) / fruits) * .8
            o += C(math.cos(t) * W / 2 * rr, -trunk_h - H * .5 + math.sin(t) * H / 2 * rr, fr, fcol, 2.2)
    return o

def soil_cut(body_above, below, W=300, D=110):
    """ground cross-section: brown box below y=0 with tubers etc."""
    return R(-W / 2, 0, W, D, "#e9d6b8", 8, 2.6) + P(f"M{-W/2} 0 h{W}", sw=3) + below + body_above

def tuber(x, y, rx=30, ry=20, col="#d9b27a", rot=0, eyes=True):
    o = E(x, y, rx, ry, col, 2.4, INK, rot)
    if eyes: o += C(x - rx * .3, y - ry * .1, 2, darker(col, .6), 0) + C(x + rx * .35, y + ry * .2, 2, darker(col, .6), 0)
    return o

def vine_trellis(W=300, H=300, fruit_fn=None, n=4, leafcol=LEAF):
    o = R(-W / 2, -H, 10, H, "#d9c3a0", 2, 2.4) + R(W / 2 - 10, -H, 10, H, "#d9c3a0", 2, 2.4) + P(f"M{-W/2} {-H+20} H{W/2} M{-W/2} {-H*.55} H{W/2}", sw=3, col="#b89a6a")
    o += P(f"M{-W/2+10} {-H*.2} C{-W*.2} {-H*.9} {W*.1} {-H*.2} {W/2-10} {-H*.8}", sw=4, col=STEM)
    for i in range(7):
        x = -W / 2 + 30 + i * (W - 60) / 6; y = -H * (.35 + .35 * ((i * 3) % 4) / 3)
        o += leaf(x, y, -90 + (i % 3 - 1) * 50, 50, 26, leafcol)
    if fruit_fn:
        for i in range(n):
            o += fruit_fn(-W / 2 + 50 + i * (W - 100) / max(1, n - 1), -H * .45 + (i % 2) * 40)
    return o

def branch_fruit(fruit_fn, n=3, leafcol=LEAF, L=320, leafL=70, spread=None):
    o = line(f"M{-L/2} {-200} Q0 {-250} {L/2} {-220}", 9, "#8a6a4a")
    for i in range(5):
        x = -L / 2 + 30 + i * (L - 60) / 4; y = -210 - 20 * math.sin(math.pi * (i + .5) / 5)
        o += leaf(x, y, -60 - (i % 2) * 70, leafL, None, leafcol)
    xs = spread or [(-L / 2 + 60 + k * (L - 120) / max(1, n - 1)) for k in range(n)]
    for x in xs:
        y = -205 - 20 * math.sin(math.pi * (x + L / 2) / L)
        o += P(f"M{x} {y} l0 20", sw=2.4) + fruit_fn(x, y + 20)
    return o + P("M-160 0 h0", sw=0)

# fruit shapes: fn(x, y_top) -> svg (hanging from top point)
def F_round(r=34, col="#e8485a", hi=True, leaf_=False, stemcol="#6b4a32"):
    def f(x, y):
        o = C(x, y + r, r, col, 2.6)
        if hi: o += E(x - r * .35, y + r * .6, r * .18, r * .28, "#ffffff", 0, INK, 20, 'fill-opacity=".55"')
        return o + P(f"M{x} {y+4} q2 -8 6 -12", sw=3, col=stemcol)
    return f
def F_pear(r=30, col="#d9c45a"):
    return lambda x, y: P(f"M{x} {y} C{x+r*.5} {y} {x+r*.4} {y+r*.9} {x+r} {y+r*1.6} C{x+r*1.2} {y+r*2.6} {x-r*1.2} {y+r*2.6} {x-r} {y+r*1.6} C{x-r*.4} {y+r*.9} {x-r*.5} {y} {x} {y} Z", col, 2.6)
def F_oval(rx=24, ry=40, col="#f2a03a", rot=0):
    return lambda x, y: E(x, y + ry, rx, ry, col, 2.6, INK, rot)
def F_cluster(r=10, col="#6a3a8a", rows=5):
    def f(x, y):
        o = ""
        for rr in range(rows):
            k = rows - rr
            for j in range(k): o += C(x + (j - (k - 1) / 2) * r * 1.8, y + r + rr * r * 1.6, r, col, 1.8)
        return o
    return f
def F_spiky(r=40, col="#b8b84a"):
    def f(x, y):
        o = C(x, y + r, r, col, 2.6)
        o += "".join(poly([(x + math.cos(t) * r * .98, y + r + math.sin(t) * r * .98), (x + math.cos(t + .12) * r * 1.16, y + r + math.sin(t + .12) * r * 1.16), (x + math.cos(t + .24) * r * .98, y + r + math.sin(t + .24) * r * .98)], darker(col, .9), 1.6) for t in [i * .4 for i in range(16)])
        return o + "".join(C(x + math.cos(t) * r * .5, y + r + math.sin(t) * r * .5, 2.2, darker(col, .6), 0) for t in [i * .9 for i in range(7)])
    return f
def F_banana(col="#f6d43a"):
    def f(x, y):
        o = R(x - 6, y - 10, 12, 30, "#8a9a5a", 3, 2.2)
        for i in range(5):
            dx = (i - 2) * 22
            o += P(f"M{x+dx*.4} {y+16} C{x+dx} {y+40} {x+dx*1.4} {y+70} {x+dx*1.2+40} {y+110} C{x+dx*1.2+10} {y+90} {x+dx*1.1-6} {y+60} {x+dx*.4-10} {y+18} Z", col, 2.4)
        return o
    return f
def F_pine(col="#e8a83a"):
    def f(x, y):
        o = E(x, y + 70, 40, 60, col, 2.6) + "".join(P(f"M{x-40} {y+30+k*20} L{x+40} {y+70+k*20} M{x+40} {y+30+k*20} L{x-40} {y+70+k*20}", sw=1.4, col=darker(col, .7)) for k in range(-1, 3))
        return o + "".join(leaf(x, y + 14, -90 + a, 50, 9, "#6faa4a") for a in (-40, -20, 0, 20, 40))
    return f
def F_berry(r=9, col="#3a4a8a", n=6):
    return lambda x, y: "".join(C(x + math.cos(i * 1.1) * r * 1.4, y + r * 2 + math.sin(i * 1.1) * r * 1.4, r, col, 1.8) for i in range(n))
def F_strawberry(r=26, col="#e8304a"):
    def f(x, y):
        o = P(f"M{x} {y+r*2.2} C{x-r*1.4} {y+r*1.2} {x-r*1.2} {y+4} {x} {y+8} C{x+r*1.2} {y+4} {x+r*1.4} {y+r*1.2} {x} {y+r*2.2} Z", col, 2.4)
        o += "".join(E(x + (k % 3 - 1) * r * .5, y + r * .6 + (k // 3) * r * .45, 1.6, 2.6, "#f6e46a", 0) for k in range(9))
        return o + "".join(leaf(x, y + 8, -90 + a, 18, 6, "#6faa4a", False) for a in (-70, -30, 30, 70))
    return f
def F_melon(r=60, col="#5aa04a", stripe="#2f6a2a", flesh=None):
    def f(x, y):
        o = C(x, y + r, r, col, 2.8) + "".join(P(f"M{x+k*r*.25} {y+2} Q{x+k*r*.4} {y+r} {x+k*r*.25} {y+2*r-2}", sw=4, col=stripe) for k in (-3, -1, 1, 3))
        return o
    return f

def V_root(col="#f28a2a", L=140, W=36, tops="#7cc46a", white=False):
    o = P(f"M{-W} 0 Q{-W*.6} {L*.5} 0 {L} Q{W*.6} {L*.5} {W} 0 Z", col, 2.6) + "".join(P(f"M{-W*.6+k*6} {L*(.2+k*.15)} h{W*.5}", sw=1.6, col=darker(col, .7)) for k in range(4))
    return "".join(leaf(0, 0, -90 + a, 110, 18, tops) for a in (-40, -15, 15, 40)) + o

def V_bulb(col="#c98a5a", r=50, tops="#8fcf6a", cloves=False):
    o = "".join(line(f"M0 {-r*1.6} Q{a*.6} {-r*3} {a} {-r*4}", 5, tops) for a in (-30, 0, 30))
    o += P(f"M0 {-r*1.9} C{r*1.2} {-r*1.6} {r*1.2} 0 0 0 C{-r*1.2} 0 {-r*1.2} {-r*1.6} 0 {-r*1.9} Z", col, 2.6)
    o += "".join(P(f"M0 {-r*1.85} Q{k*r*.35} {-r*.9} 0 0", sw=1.6, col=darker(col, .7)) for k in (-2, -1, 1, 2))
    return o + P("M-10 0 l-6 12 M0 0 v14 M10 0 l6 12", sw=2)

def V_head(col="#b8e08a", r=70, tall=False):
    ry = r * (1.5 if tall else 1)
    o = "".join(E(x, -ry, r * .7, ry * .95, darker(col, .9), 2.4, INK, a) for x, a in ((-r * .45, -12), (r * .45, 12)))
    o += E(0, -ry, r * .7, ry, col, 2.6) + "".join(P(f"M0 {-ry*.2} Q{k*r*.3} {-ry} {k*r*.15} {-ry*1.8}", sw=1.8, col=darker(col, .7)) for k in (-1, 0, 1))
    return o

def V_rosette(col="#5aa04a", n=9, L=110, W=40, ruffle=False):
    o = ""
    for i in range(n):
        a = -170 + i * (160 / (n - 1)); o += leaf(0, 0, a, L * (.8 + .2 * (i % 2)), W, col if i % 2 else darker(col, .9))
    return o

def V_pods(col="#7cc46a", n=4, L=90, W=16, peas=True):
    def f(x, y):
        o = P(f"M{x} {y} C{x+W*1.6} {y+L*.3} {x+W*1.2} {y+L*.8} {x+W*.2} {y+L} C{x-W*.4} {y+L*.7} {x-W*.4} {y+L*.3} {x} {y} Z", col, 2.4)
        if peas: o += "".join(C(x + W * .4, y + L * (.2 + k * .2), W * .34, darker(col, .85), 1.4) for k in range(4))
        return o
    return f

def V_long(col="#5a3a7a", L=150, W=30, curve=30, cap="#6faa4a", warty=False):
    def f(x, y):
        o = P(f"M{x-W*.4} {y} C{x-W} {y+L*.4} {x-W+curve} {y+L} {x+curve} {y+L} C{x+W+curve} {y+L} {x+W} {y+L*.4} {x+W*.4} {y} Z", col, 2.6)
        if warty: o += "".join(E(x + (k % 2 - .5) * W * .7 + curve * k / 10, y + L * (.15 + k * .08), 4, 7, darker(col, .85), 1.2) for k in range(10))
        return o + P(f"M{x-W*.6} {y+4} L{x} {y-10} L{x+W*.6} {y+4} Z", cap, 2.2)
    return f

# ------------------------------------------------------------------ desert
CACT = "#7ab86a"
def ribs(x, y0, y1, w, n=3, col=CACT):
    return "".join(P(f"M{x+(k-(n-1)/2)*w/n} {y0} V{y1}", sw=1.8, col=darker(col, .7)) for k in range(n))

def saguaro(H=420, col=CACT):
    w = 34
    o = ""
    for sx, y, h in ((-1, -H * .38, 120), (1, -H * .55, 100)):
        o += line(f"M0 {y} H{sx*70} Q{sx*86} {y} {sx*86} {y-18} V{y-h}", 2 * w - 18, col)
    o += P(f"M{-w} 0 V{-H+w} a{w} {w} 0 0 1 {2*w} 0 V0 Z", col, 2.8) + ribs(0, -H + 30, -10, w * 1.4)
    return o

def opuntia(col="#8fc06a", fruit="#c9304a"):
    o = ""
    for x, y, a, s in ((0, -70, 0, 1), (-60, -180, -25, .85), (60, -190, 25, .85), (-20, -290, -10, .7), (90, -300, 35, .6)):
        o += E(x, y, 60 * s, 80 * s, col, 2.6, INK, a) + "".join(P(f"M{x+dx} {y+dy} l4 -6 M{x+dx} {y+dy} l-5 -4", sw=1.4) for dx, dy in ((-20, -20), (18, 10), (0, 40), (24, -40), (-26, 30)))
    return o + "".join(E(x, y, 12, 16, fruit, 2.2) for x, y in ((-30, -365), (5, -372), (110, -365)))

def barrel(r=110, col="#7ab86a", spine="#f2c83a"):
    o = P(f"M{-r} 0 Q{-r*1.05} {-r*1.3} 0 {-r*1.4} Q{r*1.05} {-r*1.3} {r} 0 Z", col, 2.8)
    o += "".join(P(f"M{k*r*.22} {-r*1.38} Q{k*r*.32} {-r*.7} {k*r*.26} -2", sw=2, col=darker(col, .7)) for k in range(-4, 5))
    o += "".join(P(f"M{k*r*.22} {-r*(1.25-.2*j)} l{8} -8 M{k*r*.22} {-r*(1.25-.2*j)} l-8 -8", sw=2, col=spine) for k in range(-3, 4) for j in range(5))
    return o + E(0, -r * 1.38, r * .4, 14, "#f6e08a", 2.2)

def rosette(col="#8ab8a0", n=11, L=200, W=34, teeth=True, tip=INK):
    o = ""
    for i in range(n):
        a = -175 + i * (170 / (n - 1)); rad = math.radians(a)
        o += leaf(0, 0, a, L * (.75 + .25 * math.sin(math.pi * i / (n - 1))), W, col if i % 2 else darker(col, .9), False)
    return o

def lithops(col="#c9b89a", top="#a89a7a"):
    o = ""
    for x, s in ((-60, 1), (40, .9), (110, .75)):
        o += P(f"M{x-40*s} 0 Q{x-44*s} {-60*s} {x-4*s} {-62*s} L{x-4*s} 0 Z", col, 2.6) + P(f"M{x+4*s} 0 L{x+4*s} {-62*s} Q{x+44*s} {-60*s} {x+40*s} 0 Z", col, 2.6)
        o += E(x - 22 * s, -58 * s, 16 * s, 5 * s, top, 1.6) + E(x + 22 * s, -58 * s, 16 * s, 5 * s, top, 1.6)
    return o

def twiggy(W=220, H=200, col="#8a7a5a", leafcol="#9cc98a", leaves=True, ball=False):
    o = ""
    for i in range(9):
        a = math.radians(-160 + i * 17.5); L = H * (.8 + .2 * (i % 3) / 2)
        ex, ey = math.cos(a) * W * .6, math.sin(a) * L
        o += line(f"M0 0 Q{ex*.3} {ey*.6} {f1(ex)} {f1(ey)}", 3, col)
        if leaves: o += "".join(C(ex * t, ey * t, 5, leafcol, 1.4) for t in (.6, .8, 1.0))
    if ball: o = P(wavy(0, -H * .55, W * .5, H * .5, 16, 10), "none", 3, darker(col, .8)) + o
    return o

# ------------------------------------------------------------------ aquatic (draw with y=0 as water surface)
def pad(x, y, r=60, col="#7cc46a", rim=False):
    o = P(f"M{x} {y} L{x+r*.95} {y-r*.12} A{r} {r*.38} 0 1 1 {x+r*.8} {y+r*.2} Z", col, 2.4)
    if rim: o = E(x, y, r, r * .38, col, 2.4) + E(x, y - r * .06, r * .92, r * .32, darker(col, .9), 1.8)
    return o + P(f"M{x} {y} l{-r*.6} {-r*.1} M{x} {y} l{-r*.2} {r*.25} M{x} {y} l{r*.3} {-r*.25}", sw=1.4, col=darker(col, .7))

def lily_flower(x, y, r=34, col="#f6f0f4", center=YEL, n=8):
    o = "".join(rot_ell(x, y - r * .3, r * .5, -90 + (i - (n - 1) / 2) * (150 / n), r * .55, r * .2, col, 2) for i in range(n))
    return o + E(x, y - r * .2, r * .3, r * .14, center, 1.8)

def water(W=440):
    return E(0, 0, W / 2, 40, BLUE_L, 2.4) + P(f"M{-W*.3} 6 q12 -6 24 0 q12 6 24 0 M{W*.1} 16 q12 -6 24 0 q12 6 24 0", sw=2, col=BLUE_M)

def reeds(n=6, H=320, head="plume", col="#a8c86a", headcol="#c9a07a"):
    o = ""
    for i in range(n):
        x = -120 + i * 48; h = H * (.8 + .2 * ((i * 5) % 3) / 2)
        o += stalk(x, 0, x + (i - n / 2) * 6, -h, 8, 4, col) + leaf(x, -h * .4, -60 if i % 2 else -120, 90, 10, col)
        tx, ty = x + (i - n / 2) * 6, -h
        if head == "plume": o += P(f"M{tx} {ty} q30 -20 40 -60 q-30 10 -40 60", headcol, 2)
        elif head == "cattail": o += R(tx - 9, ty - 4, 18, 70, "#7a4a2a", 9, 2.4) + P(f"M{tx} {ty-4} v-30", sw=2)
        elif head == "umbel": o += "".join(P(f"M{tx} {ty} l{math.cos(math.radians(a))*60:.0f} {math.sin(math.radians(a))*50:.0f}", sw=1.6, col="#7a9a3a") for a in range(-170, -5, 12))
    return o

def ribbons(n=7, H=260, col="#6faa4a"):
    return "".join(line(f"M{-120+i*40} 0 C{-120+i*40+30} {-H*.3} {-120+i*40-30} {-H*.7} {-120+i*40+(i%3-1)*20} {-H*(.8+.2*(i%2))}", 9, col) for i in range(n))

# ------------------------------------------------------------------ fungi
def mushroom(x=0, cap="convex", r=70, H=120, capcol="#c9884a", stemcol="#f4ecd8", spots=None, gills=True, ring=False, volva=False, sw_stem=None, tilt=0):
    sw_ = sw_stem or r * .32
    o = ""
    if volva: o += P(f"M{x-sw_*1.1} 0 Q{x-sw_*1.2} {-H*.22} {x-sw_*.6} {-H*.25} L{x+sw_*.6} {-H*.25} Q{x+sw_*1.2} {-H*.22} {x+sw_*1.1} 0 Z", "#f4f2ea", 2.4)
    o += P(f"M{x-sw_*.6} 0 Q{x-sw_*.45} {-H*.5} {x-sw_*.4} {-H} L{x+sw_*.4} {-H} Q{x+sw_*.45} {-H*.5} {x+sw_*.6} 0 Z", stemcol, 2.6)
    if ring: o += P(f"M{x-sw_*.7} {-H*.72} Q{x} {-H*.6} {x+sw_*.7} {-H*.72} L{x+sw_*.5} {-H*.8} L{x-sw_*.5} {-H*.8} Z", "#ffffff", 2.2)
    y = -H
    if cap == "convex": d = f"M{x-r} {y} Q{x-r} {y-r*.9} {x} {y-r*.9} Q{x+r} {y-r*.9} {x+r} {y} Z"
    elif cap == "flat": d = f"M{x-r} {y} Q{x-r*.9} {y-r*.45} {x} {y-r*.45} Q{x+r*.9} {y-r*.45} {x+r} {y} Z"
    elif cap == "conical": d = f"M{x-r*.7} {y} Q{x-r*.5} {y-r*1.2} {x} {y-r*1.5} Q{x+r*.5} {y-r*1.2} {x+r*.7} {y} Z"
    elif cap == "bell": d = f"M{x-r*.75} {y+r*.3} Q{x-r*.8} {y-r*1.3} {x} {y-r*1.3} Q{x+r*.8} {y-r*1.3} {x+r*.75} {y+r*.3} Z"
    elif cap == "funnel": d = f"M{x-r} {y-r*.5} Q{x} {y-r*.1} {x+r} {y-r*.5} Q{x+r*.3} {y+r*.1} {x} {y+r*.2} Q{x-r*.3} {y+r*.1} {x-r} {y-r*.5} Z"
    elif cap == "egg": d = f"M{x-r*.6} {y+r*.5} Q{x-r*.7} {y-r*1.6} {x} {y-r*1.6} Q{x+r*.7} {y-r*1.6} {x+r*.6} {y+r*.5} Z"
    else: d = f"M{x-r} {y} Q{x-r} {y-r*.9} {x} {y-r*.9} Q{x+r} {y-r*.9} {x+r} {y} Z"
    o += P(d, capcol, 2.8)
    if gills and cap in ("convex", "flat"): o += E(x, y, r * .98, r * .12, darker(capcol, .8), 2) + "".join(P(f"M{x} {y} l{k*r*.12} {r*.1}", sw=1.2, col=INK) for k in range(-7, 8))
    if spots:
        for k in range(7):
            sx = x + math.cos(k * 2.2) * r * .55; sy = y - r * .45 + math.sin(k * 2.2) * r * .25
            o += E(sx, sy, r * .1, r * .07, spots, 1.6)
    return G_(o, 0, 0) if not tilt else f'<g transform="rotate({tilt} {x} 0)">{o}</g>'

def group(*items):
    return "".join(items)

def bracket(n=3, col="#c98a3a", band=None, log=True):
    o = R(-40, -340, 80, 340, "#b89a7a", 6, 2.8) if log else ""
    for i in range(n):
        y = -100 - i * 80; w = 120 - i * 15
        o += P(f"M30 {y} Q{30+w*.4} {y-50} {30+w} {y-10} Q{30+w*.5} {y+12} 30 {y+10} Z", col, 2.6)
        if band: o += P(f"M36 {y-6} Q{30+w*.4} {y-30} {30+w*.85} {y-8}", sw=3, col=band)
    return o

def log_(L=380, col="#b89a7a"):
    return P(f"M{-L/2} 0 L{L/2} 0 L{L/2} -60 L{-L/2} -60 Z", col, 2.8) + E(L / 2, -30, 18, 30, "#e9d6b8", 2.6) + P(f"M{-L/3} -40 h120 M{-L/6} -18 h140", sw=1.6, col=darker(col, .7))

def petri(colonies, R_=170, agar="#fbf1c8"):
    o = E(0, 0, R_ + 14, (R_ + 14) * .42, "#eef4f8", 2.6) + E(0, -6, R_, R_ * .4, agar, 2.4)
    for x, y, r, col in colonies:
        o += E(x, y - 6, r, r * .42, col, 2) + E(x, y - 8, r * .5, r * .2, darker(col, .85), 0)
    return o + P(f"M{-R_*.6} {-R_*.36} q{R_*.3} -14 {R_*.6} -12", sw=2, col="#ffffff")

def scope_view(cells, R_=180):
    o = C(0, -R_, R_, "#f4fbff", 3)
    for x, y, rx, ry, a, col in cells:
        o += E(x, -R_ + y, rx, ry, col, 2, INK, a)
    return o + C(0, -R_, R_, "none", 6) 
from art5 import *

# ====================================================================== animals (phase 4)
def Q(kind, box=None, extra="", **kw):
    return lambda w, h: scene(kind, w, h, quad(**kw), box=box and (w / 2, h * box[0], box[1], box[2]), extra=extra)
def DOGQ(kind="meadow", box=(.76, 560, 380), **kw):
    base = dict(F="#e8c08a", bl=250, bd=104, lh=100, lw=28, belly=None, neck=(26, 40), nw=74, head=(54, 46), snout=(48, 32), ears="droop", tail="thin")
    base.update(kw); return Q(kind, box, **base)
def CATQ(kind="home", box=(.76, 540, 360), **kw):
    base = dict(F="#c9b8a0", bl=230, bd=90, lh=90, lw=20, neck=(24, 36), nw=56, head=(44, 38), snout=(20, 22), ears="point", tail="long")
    base.update(kw); return Q(kind, box, **base)
ART5["golden-retriever"] = DOGQ(F="#e6b45a", belly="#f2d08a", tail="bushy", tail_col="#e6b45a", snout_col="#efc878", lh=110, bl=270)
ART5["labrador"] = DOGQ(F="#e9cf8a", tail="thin", tail_col="#e9cf8a", snout_col="#f2dca0", lh=108, bl=260, bd=110)
ART5["gsd"] = DOGQ(F="#c98a4a", belly="#d9a868", pattern="patches", pat_col="#2a2a2e", ears="point", tail="bushy", tail_col="#5a4030", snout=(52, 30), snout_col="#2a2a2e", lh=116, bl=270)
ART5["poodle"] = DOGQ(F="#f4f0ea", wool="#ffffff", neck_wool="#ffffff", ears="droop", tail="short", lh=130, bl=220, bd=90, snout=(46, 26), head=(46, 42))
ART5["chihuahua"] = DOGQ("home", (.76, 460, 300), F="#e6c08a", ears="big", tail="thin", lh=70, bl=170, bd=74, head=(52, 48), snout=(22, 22), snout_col="#f2d8b0", nw=50)
ART5["shiba"] = DOGQ(F="#d98a3a", belly="#f6ead8", ears="point", tail="curl", tail_col="#d98a3a", snout=(40, 30), snout_col="#f6ead8", lh=96, bl=220)
ART5["husky"] = DOGQ("snow", F="#7a8088", belly="#ffffff", ears="point", tail="bushy", tail_col="#7a8088", snout_col="#ffffff", lh=110, bl=250, mask="#ffffff")
ART5["corgi"] = DOGQ(F="#e09a4a", belly="#ffffff", ears="big", tail="short", lh=50, bl=240, bd=96, snout=(42, 30), snout_col="#ffffff")
ART5["dachshund"] = DOGQ("home", (.76, 560, 300), F="#9a5a2e", ears="droop", tail="thin", tail_col="#9a5a2e", lh=46, bl=280, bd=80, head=(46, 40), snout=(56, 26))
ART5["beagle"] = DOGQ(F="#ffffff", pattern="patches", pat_col="#c98a4a", ears="droop", tail="thin", tail_col="#ffffff", lh=90, bl=230, snout_col="#ffffff")
ART5["pug"] = DOGQ("home", (.76, 480, 320), F="#e0c08a", ears="small", tail="curl", tail_col="#e0c08a", lh=70, bl=200, bd=100, head=(56, 52), snout=(16, 26), snout_col="#3a3030")
ART5["frenchie"] = DOGQ("home", (.76, 480, 320), F="#d9c4a8", ears="big", tail="short", lh=70, bl=200, bd=100, head=(56, 50), snout=(18, 28), snout_col="#3a3030")
ART5["samoyed"] = DOGQ("snow", F="#ffffff", wool="#ffffff", neck_wool="#ffffff", ears="point", tail="curl", tail_col="#ffffff", lh=104, bl=240, snout=(40, 30))
ART5["persian"] = CATQ(F="#e9e4dc", wool="#f4f0ea", neck_wool="#f4f0ea", ears="round", tail="bushy", tail_col="#f4f0ea", snout=(10, 22), head=(50, 44), lh=70)
ART5["siamese"] = CATQ(F="#f2e6d2", snout_col="#5a4030", tail_col="#5a4030", ears="point", lh=100, bl=240, bd=80)
ART5["maine-coon"] = CATQ(F="#9a7a5a", pattern="stripes", pat_col="#5a4030", tail="bushy", tail_col="#7a5a3a", lh=100, bl=280, bd=104, head=(50, 42), neck_wool="#b89a7a")
ART5["british-sh"] = CATQ(F="#8f98a4", ears="round", tail="long", tail_col="#8f98a4", lh=80, bl=230, bd=104, head=(56, 48), snout=(14, 24))
ART5["ragdoll"] = CATQ(F="#f2ece2", snout_col="#8a7a6a", wool="#f6f2ea", tail="bushy", tail_col="#8a7a6a", lh=86, bl=250, bd=96)
ART5["sphynx"] = CATQ(F="#f2c8b0", ears="big", tail="long", tail_col="#f2c8b0", lh=100, bl=220, bd=76, head=(40, 36))
ART5["scottish-fold"] = CATQ(F="#c9ccd1", ears="small", tail="long", tail_col="#c9ccd1", lh=80, bl=220, bd=96, head=(54, 48), snout=(12, 22))
ART5["bengal-cat"] = CATQ("forest", F="#e0aa5a", belly="#f6e6c8", pattern="rosettes", pat_col="#5a3a20", tail="long", tail_col="#e0aa5a", lh=104, bl=260, bd=84)
ART5["holland-lop"] = lambda w, h: scene("meadow", w, h, blob(F="#c98a55", L=200, H=150, belly="#f6efe2", ears="petal", tail="puff", nose="#e8a0a0", whisk=True), box=(w / 2, h * .74, 420, 300))
def _perch_bird(kind, **kw):
    from art4 import BP
    return BP(kind, **kw)
ART5["java-sparrow"] = _perch_bird("home", F="#8a929e", wing="#7a828e", rx=54, ry=38, tilt=-18, neck=4, nw=36, hr=28, beak="cone", beak_col="#e8506a", leg_len=22, leg_col="#f2a8a8", legw=4,
                                  tail="short", tail_col="#2a2a2e", head_col="#2a2a2e", belly="#e8d8d0", eye_ring="#e8506a", front_fn=lambda x, y, r: E(x + r * .1, y + r * .25, r * .55, r * .4, "#ffffff", 0))
ART5["gouldian"] = _perch_bird("savanna", F="#5ab84a", wing="#4aa03a", rx=52, ry=36, tilt=-18, neck=4, nw=34, hr=26, beak="cone", beak_col="#f2e0c8", leg_len=22, leg_col="#e8b8a0", legw=4,
                               tail="long", tail_col="#2a2a2e", head_col="#d9302a", belly="#f6d43a", front_fn=lambda x, y, r: E(x + r * .5, y + r * 1.2, r * .7, r * .3, "#9a5ad9", 0))
ART5["eclectus"] = _perch_bird("rainforest", F="#3ab84a", wing="#2a9a3a", rx=66, ry=50, tilt=-34, neck=8, nw=46, hr=34, beak="hook", beak_col="#f2a03a", leg_len=28, leg_col="#6b6b6b",
                               tail="short", tail_col="#2a9a3a", front_fn=lambda x, y, r: E(x + r * 1.4, y + r * 1.6, r * .5, r * .9, "#d9302a", 0))

# ---- batch p4pet2 ----
from art4 import tank, L_, C_, FR_, TU_
from art3 import lizard, snake_coil, frog
from art2 import fish, turtle
ART5["lorikeet"] = _perch_bird("forest", F="#3aa84a", wing="#2a9a3a", rx=56, ry=40, tilt=-28, neck=6, nw=38, hr=28, beak="hook", beak_col="#e8402a", leg_len=22, leg_col="#8a8a8a", legw=4,
                               tail="long", tail_col="#3aa84a", head_col="#3a5ad9", belly="#3a5ad9", front_fn=lambda x, y, r: E(x + r * .3, y + r * .9, r * .75, r * .5, "#f29a2a", 0))
ART5["ringneck"] = _perch_bird("home", F="#8ad86a", wing="#6ac04a", rx=56, ry=38, tilt=-26, neck=6, nw=38, hr=28, beak="hook", beak_col="#d9302a", leg_len=22, leg_col="#8a8a8a", legw=4,
                               tail="long", tail_col="#6ac04a", front_fn=lambda x, y, r: P(f"M{x-r*.9} {y+r*.55} q{r*.9} {r*.6} {r*1.8} 0", sw=5, col=INK) + P(f"M{x-r*.9} {y+r*.7} q{r*.9} {r*.6} {r*1.8} 0", sw=4, col="#f2a0b8"))
def _fishes(main, sm=None, box=(None, 330, 360, 220)):
    return tank(main + (G_(sm, 160, -110) if sm else ""), box=box)
ART5["molly"] = _fishes(fish(F="#2a2a2e", L=210, H=90, tail="round", eye_r=8, fin_col="#3a3a3e", tail_col="#3a3a3e"),
                        fish(F="#f2f2ee", L=150, H=64, tail="round", eye_r=6, fin_col="#e6e6e0"))
ART5["swordtail"] = _fishes(fish(F="#e8582c", L=200, H=74, tail="fork", eye_r=7, fin_col="#f2884a",
                                 extras=P("M110 22 L250 40 L246 50 L106 34 Z", "#2a2a2e", 2.4)))
ART5["cardinal-tetra"] = tank(fish(F="#d9302a", L=210, H=76, tail="fork", eye_r=8, fin_col="#e6ecf1",
                                   extras=P("M-96 -12 L96 -12", sw=12, col="#3fb6e8")) +
                              G_(fish(F="#d9302a", L=140, H=52, tail="fork", eye_r=6, extras=P("M-60 -8 L60 -8", sw=8, col="#3fb6e8")), 150, -110) +
                              G_(fish(F="#d9302a", L=120, H=46, tail="fork", eye_r=5, extras=P("M-52 -7 L52 -7", sw=7, col="#3fb6e8")), -150, 110))
ART5["arowana"] = tank(fish(F="#e8b84a", L=380, H=90, tail="round", eye_r=9, fin_col="#d9902a", tail_col="#d9902a", belly="#f6dc8a",
                            extras=P("M150 -6 l20 -26", sw=4, col=INK) + P("M150 -6 l26 -20", sw=4, col=INK)), box=(None, 330, 480, 200))
ART5["corydoras"] = tank(fish(F="#a89060", L=200, H=90, tail="fork", eye_r=8, fin_col="#c9b48a", belly="#e9dcc0",
                              extras=P("M-60 -20 L80 -20", sw=10, col="#3a6a5a") + P("M96 30 l18 14 M90 34 l10 18", sw=3)), box=(None, 380, 330, 200))
ART5["dwarf-gourami"] = tank(fish(F="#3a7ad9", L=200, H=120, tail="round", eye_r=8, fin_col="#d9302a",
                                  extras="".join(P(f"M{x} -50 L{x+30} 50", sw=10, col="#d9402a") for x in (-70, -30, 10, 50)) + P("M40 40 L-30 130", sw=3, col="#d9402a")))
ART5["tiger-barb"] = _fishes(fish(F="#f2c86a", L=190, H=110, tail="fork", eye_r=8, fin_col="#e8402a", stripes=("#2a2a2e", [.15, .4, .65, .88])),
                             fish(F="#f2c86a", L=130, H=76, tail="fork", eye_r=6, fin_col="#e8402a", stripes=("#2a2a2e", [.15, .4, .65, .88])))
ART5["white-cloud"] = lambda w, h: scene("pond", w, h, fish(F="#a8b89a", L=200, H=60, tail="fork", eye_r=7, fin_col="#e8402a", tail_col="#e8402a",
                                          extras=P("M-90 -4 L96 -4", sw=6, col="#f2e6a0")) + G_(fish(F="#a8b89a", L=140, H=44, tail="fork", eye_r=5, fin_col="#e8402a", tail_col="#e8402a"), 170, -80), box=(w / 2, h * .66, 460, 220))
ART5["red-foot"] = TU_("rainforest", shell="#3a3430", skin="#3a3a3a", L=270, H=150, scute="#e8b84a", neck=46, plastron="#e8d8a8",
                       post="".join(C(x, 40, 10, "#e8402a", 0) for x in (-90, -40, 60, 110)))
ART5["hermann"] = TU_("meadow", shell="#d9b84a", skin="#b9a888", L=250, H=140, scute="#3a3430", neck=46, plastron="#f2e2a8")
ART5["blue-tongue"] = L_("desert", (.78, 620, 260), F="#b9a88a", L=300, H=70, tail=.6, snout=56, sh=40, belly="#e9dcc0", legs=14, legh=22,
                         spots="#6a5a4a", post=P("M-172 4 l-34 -8 l6 8 l-6 8 Z", "#3a5ad9", 2.4))
ART5["kingsnake"] = C_("desert", "#2a2a2e", pat="#f6f2e0", L=1.0)
ART5["hognose"] = C_("meadow", "#b99a6a", pat="#6a4a2a", L=.85)
ART5["pacman"] = FR_("rainforest", "#6ab84a", "#f2e6b8", spots="#a8402a", box=(.76, 460, 280))
ART5["whites-frog"] = FR_("leaf", "#6ac05a", "#f6f2e0", box=(.74, 420, 240))
def _arach(F, L=120, tail=False, hair=None, box=(.76, 520, 300), kind="desert"):
    def f(w, h):
        o = ""
        for s in (-1, 1):
            for i in range(4):
                d = f"M{s*20} {-30+i*8} L{s*(90+i*16)} {-90+i*26} L{s*(140+i*22)} 30"
                o += P(d, sw=12, col=INK) + P(d, sw=7, col=F)
        if tail:
            o += P("M0 0 C0 80 -40 120 -120 90 C-180 60 -200 -10 -160 -60", sw=26, col=INK) + P("M0 0 C0 80 -40 120 -120 90 C-180 60 -200 -10 -160 -60", sw=20, col=F)
            o += P("M-160 -60 l-10 -26 l24 12", "#3a3a3a", 2.4)
            for s in (-1, 1):
                d = f"M{s*20} -70 L{s*90} -140"
                o += P(d, sw=14, col=INK) + P(d, sw=9, col=F) + E(s * 110, -160, 44, 26, F, 3) + P(f"M{s*90} -176 L{s*150} -190", sw=4)
            o += E(0, -30, 44, 74, F, 3) + "".join(P(f"M-36 {y} H36", sw=2.4) for y in (-60, -30, 0, 30))
        else:
            o += E(0, 20, 66, 56, F, 3) + C(0, -50, 46, F, 3) + "".join(P(f"M{x} {y} l-4 -10", sw=2, col=hair) for x in range(-40, 50, 16) for y in (0, 30, 50))
            o += C(-10, -78, 5, INK, 0) + C(10, -78, 5, INK, 0)
        return scene(kind, w, h, o, box=(w / 2, h * box[0], box[1], box[2]))
    return f
ART5["rose-tarantula"] = _arach("#8a6a5a", hair="#e8a8a0")
ART5["emperor-scorpion"] = _arach("#2a2a30", tail=True, kind="rainforest", box=(.74, 480, 360))
def _hermit(w, h):
    shell = P("M-20 0 C-40 -140 160 -170 170 -40 C176 20 100 30 40 20 Z", "#d9a07a", 3) + P("M150 -40 C120 -110 40 -100 50 -40 C60 0 120 -10 110 -50", sw=3, col="#8a5a3a")
    o = ""
    for i in range(3):
        d = f"M{-20-i*14} 0 L{-80-i*24} -30 L{-110-i*24} 30"
        o += P(d, sw=12, col=INK) + P(d, sw=8, col="#e8804a")
    o += P("M-30 -30 L-100 -80", sw=16, col=INK) + P("M-30 -30 L-100 -80", sw=11, col="#8a4ab8") + E(-120, -96, 34, 26, "#8a4ab8", 3)
    o += P("M-30 -40 L-50 -110 M-20 -40 L-30 -116", sw=3) + C(-50, -114, 6, INK, 0) + C(-30, -120, 6, INK, 0)
    return scene("meadow", w, h, shell + o, box=(w / 2, h * .76, 440, 260))
ART5["hermit-crab"] = _hermit

# ---- batch p4farm1 ----
from art2 import bird, blob, rock
def COW(F, kind="farm", horns=None, snout_col=None, udder=None, **kw):
    a = dict(F=F, bl=330, bd=140, lh=140, lw=34, neck=(20, 60), nw=90, head=(52, 50), snout=(44, 40), snout_col=snout_col or F, nose="#5a4a44",
             ears="side", horns=horns, tail="tuft", tail_col=darker(F, .7), hooves=INK, udder=udder)
    a.update(kw); return Q(kind, (.76, 600, 380), **a)
ART5["angus"] = COW("#2a2a2e", snout_col="#3a3a3e")
ART5["jersey"] = COW("#c98a4a", horns="cow", snout_col="#f2e6d6", udder="#f2c9b8", bl=300, lh=130, belly="#e6c09a")
ART5["wagyu"] = COW("#2e2a2a", horns="cow", snout_col="#3a3434")
ART5["simmental"] = COW("#c9783a", horns="cow", pattern="patches", pat_col="#fbf8f2", snout_col="#fbf8f2")
ART5["charolais"] = COW("#f2e8d6", horns="cow", snout_col="#f6d8c8", bl=350, bd=160)
def PIG(F, **kw):
    a = dict(F=F, bl=300, bd=150, lh=80, lw=36, neck=(0, 0), head=(64, 58), snout=(34, 40), snout_col=darker(F, .9), nose=None, ears="point", tail="curl", hooves=darker(F, .7), pig=True)
    a.update(kw); return Q("farm", (.75, 560, 340), **a)
ART5["duroc"] = PIG("#b8643a")
ART5["berkshire"] = PIG("#2e2a2e", snout_col="#f2f2ee", hooves="#f2f2ee")
ART5["large-white"] = PIG("#f8ece6", bl=330)
ART5["meishan"] = PIG("#3a3438", ears="side", hooves="#f2f2ee", extras="".join(P(f"M{60+i*8} {-150-i*6} q10 6 20 0", sw=2.4, col="#8a8288") for i in range(4)))
def HEN(F, wing=None, tail_col=None, kind="farm", **kw):
    a = dict(F=F, wing=wing or darker(F, .9), rx=80, ry=66, tilt=-12, neck=20, nw=46, hr=32, beak="cone", beak_col=YEL, leg_len=60, leg_col=YEL, legw=6,
             tail="up", tail_col=tail_col or F, crest="comb", wattle=True)
    a.update(kw)
    return lambda w, h: scene(kind, w, h, bird(**a), box=(w / 2, h * .76, 420, 380))
ART5["leghorn"] = HEN("#ffffff", wing="#f1ebe0")
def _silkie(w, h):
    b = bird(F="#fbfaf6", wing="#efece4", rx=86, ry=72, tilt=-6, neck=10, nw=60, hr=40, beak="cone", beak_col="#6a7a9a", leg_len=40, leg_col="#6a7a9a", legw=6, tail="up", tail_col="#fbfaf6", crest="comb")
    fluff = "".join(C(-60 + (i * 37) % 140, -150 + (i * 23) % 80, 16, "#fbfaf6", 0) for i in range(10))
    return scene("farm", w, h, b + fluff, box=(w / 2, h * .76, 400, 360))
ART5["silkie"] = _silkie
ART5["rir"] = HEN("#9a3a22", wing="#7a2a1a", tail_col="#2a2a2e")
ART5["brahma"] = HEN("#f6f4ee", wing="#e6e2d8", tail_col="#2a2a2e", rx=96, ry=76, leg_col="#f2d27a",
                     front="".join(P(f"M{-20+i*14} -30 l-6 24", sw=5, col="#f6f4ee") for i in range(4)))
ART5["pekin"] = lambda w, h: scene("pond", w, h, bird(F="#fffdf6", wing="#f3efe2", rx=96, ry=58, tilt=-26, neck=30, nw=42, hr=34, beak="duck", beak_col="#f29a2a", leg_len=40, leg_col="#f29a2a", legw=6, tail="up", tail_col="#fffdf6", webbed=True), box=(w / 2 - 30, h * .76, 460, 340))
ART5["runner"] = lambda w, h: scene("wetland", w, h, bird(F="#c9a87a", wing="#a8885a", rx=46, ry=96, tilt=-6, neck=60, nw=30, hr=28, beak="duck", beak_col="#4a5a3a", leg_len=30, leg_col="#e8902a", legw=6, tail="short", tail_col="#a8885a", webbed=True, belly="#e9d8b8"), box=(w / 2, h * .76, 300, 420))
def SHEEP(face, wool="#fbfaf6", **kw):
    a = dict(F=face, bl=280, bd=140, lh=100, lw=24, wool=wool, neck=(10, 60), nw=70, head=(44, 46), snout=(30, 32), ears="side", tail="short", tail_col=wool, nose=None, farleg=darker(face, .8))
    a.update(kw); return Q("farm", (.75, 560, 360), **a)
ART5["suffolk"] = SHEEP("#2a2a2e")
ART5["dorper"] = lambda w, h: scene("savanna", w, h, quad(F="#f6f2ea", bl=290, bd=140, lh=100, lw=26, neck=(10, 60), nw=70, head=(44, 46), snout=(30, 32), ears="side", tail="short", nose=None,
                                    extras="", front_extras="", mask="#2a2a2e"), box=(w / 2, h * .75, 560, 360))
def GOAT(F, kind="farm", **kw):
    a = dict(F=F, bl=260, bd=110, lh=130, lw=24, neck=(40, 26), nw=60, head=(42, 40), snout=(38, 30), ears="side", horns="goat", tail="short", hooves="#5a5048", beard=darker(F, .9))
    a.update(kw); return Q(kind, **a)
ART5["boer"] = GOAT("#fbf8f2", ears="long", mask="#a8502a", bl=290, bd=130)
ART5["saanen"] = GOAT("#fbfaf6", horns=None, udder="#f6c9c0")
ART5["angora-goat"] = GOAT("#f6f2ea", wool="#fbf8f0", kind="plateau")
ART5["cashmere"] = GOAT("#f2ece2", kind="plateau", horns="goat", wool="#f6f0e6")
ART5["angora-rabbit"] = lambda w, h: scene("home", w, h, blob(F="#fbfaf6", L=260, H=200, belly="#ffffff", ears="round", tail="puff", nose="#f2a0a0", whisk=False) +
                                           "".join(C(-100 + (i * 41) % 220, -170 + (i * 29) % 120, 22, "#fbfaf6", 0) for i in range(12)), box=(w / 2, h * .74, 460, 340))
ART5["nz-rabbit"] = lambda w, h: scene("farm", w, h, blob(F="#fbfaf6", L=250, H=170, belly="#ffffff", ears="long", tail="puff", nose="#f2a0a0", whisk=True), box=(w / 2, h * .74, 460, 320))
def HORSE(F, kind="farm", **kw):
    a = dict(F=F, bl=320, bd=130, lh=170, lw=30, neck=(90, 32), nw=70, head=(46, 40), snout=(66, 42), snout_col=F, ears="point", mane="horse", tail="horse", tail_col=darker(F, .6), hooves="#3a3f45")
    a.update(kw); return Q(kind, **a)
ART5["shire"] = HORSE("#2a2a2e", bl=360, bd=160, lh=180, lw=40, snout_col="#f6f2ea",
                      front_extras="".join(P(f"M{x} -40 q-8 20 0 36 h30 q8 -16 0 -36", "#f6f2ea", 2.4) for x in (-170, 130)))
ART5["arabian"] = HORSE("#b8b8bc", kind="desert", tail_col="#e6e6e8")
