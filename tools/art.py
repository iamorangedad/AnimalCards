"""Big card illustrations: thin-outline flat animals standing on a dimetric habitat slab (v4 poster style).
Each ART[key](w, h) returns an <svg>. Palette: ink + type colour + orange/yellow accents, light fills."""
import math, sys
from iso import Iso, INK, GREY, MUTE, BLUE, BLUE_L, BLUE_M, ORG, ORG_L, YEL, YEL_L, SAGE, SAGE_L

SW = 3


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'


def P(d, fill="none", sw=SW, col=INK, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'


def E(cx, cy, rx, ry, fill="none", sw=SW, col=INK, rot=0, extra=""):
    tr = f' transform="rotate({rot} {cx} {cy})"' if rot else ""
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{col}" stroke-width="{sw}"{tr} {extra}/>'


def C(cx, cy, r, fill="none", sw=SW, col=INK):
    return E(cx, cy, r, r, fill, sw, col)


def G(body, tx=0, ty=0, s=1, flip=False):
    sx = -s if flip else s
    return f'<g transform="translate({tx} {ty}) scale({sx} {s})">{body}</g>'


def slab(w, h, top, left, right, W_=420, D=230, T=26, k=1.0, cy=None):
    """dimetric ground slab centred in the frame; returns (svg, iso, z_top)."""
    iso = Iso(0, 0, k)
    # centre of top face
    cx, cyy = iso.P(W_ / 2, D / 2, T)
    iso.ox, iso.oy = w / 2 - cx, (cy or h * 0.70) - cyy
    return iso.box(0, 0, 0, W_, D, T, top, left, right), iso, T


def shadow(cx, cy, rx, ry=None):
    return E(cx, cy, rx, ry or rx * 0.22, "#1f2328", 0, "none", extra='fill-opacity=".10"')


def tuft(x, y, s=1, col=SAGE):
    return P(f"M{x-10*s} {y} q{4*s} {-14*s} {2*s} {-26*s} M{x} {y} q0 {-18*s} {-2*s} {-34*s} M{x+10*s} {y} q{-3*s} {-14*s} {4*s} {-24*s}", sw=2.4, col=col)


# ---------------------------------------------------------------- giant panda
def bamboo(x, y0, y1, s=1):
    o = P(f"M{x} {y0} L{x} {y1}", sw=14 * s, col=INK) + P(f"M{x} {y0} L{x} {y1}", sw=9 * s, col=SAGE_L)
    for yy in range(int(y1) + 40, int(y0), 70):
        o += P(f"M{x-7*s} {yy} H{x+7*s}", sw=2.4)
    return o


def leafb(x, y, ang, L=60):
    a = math.radians(ang)
    ex, ey = x + L * math.cos(a), y + L * math.sin(a)
    nx, ny = -math.sin(a) * L * .18, math.cos(a) * L * .18
    mx, my = (x + ex) / 2, (y + ey) / 2
    return P(f"M{x:.0f} {y:.0f} Q{mx+nx:.0f} {my+ny:.0f} {ex:.0f} {ey:.0f} Q{mx-nx:.0f} {my-ny:.0f} {x:.0f} {y:.0f} Z", SAGE_L, 2.4) + P(f"M{x:.0f} {y:.0f} L{ex:.0f} {ey:.0f}", sw=1.6, col=SAGE)


def panda_body():
    """sitting giant panda, 3/4 front, local coords: seat at y=0, height ~ 380."""
    BK, WH = INK, "#ffffff"
    o = []
    # hind legs (black, splayed forward)
    o.append(E(-112, -26, 72, 46, BK, rot=-12))
    o.append(E(118, -24, 70, 44, BK, rot=14))
    # body
    o.append(P("M-128 -30 C-160 -120 -128 -228 -60 -252 L60 -252 C128 -228 160 -120 128 -30 C80 -2 -80 -2 -128 -30 Z", WH))
    # foot pads
    o.append(E(-150, -36, 26, 22, "#3a3f45", 0) + E(156, -34, 26, 22, "#3a3f45", 0))
    # shoulder band + arms
    o.append(P("M-118 -190 C-80 -262 80 -262 118 -190 C88 -214 -88 -214 -118 -190 Z", BK))
    o.append(P("M-118 -196 C-150 -150 -120 -96 -62 -104 C-40 -108 -40 -132 -60 -140 C-84 -150 -90 -176 -84 -204 Z", BK))
    o.append(P("M118 -196 C150 -150 130 -112 84 -128 C62 -134 58 -156 76 -166 C92 -172 96 -186 92 -204 Z", BK))
    # head
    o.append(C(-70, -380, 32, BK) + C(70, -380, 32, BK))
    o.append(P("M-96 -300 C-112 -360 -70 -412 0 -412 C70 -412 112 -360 96 -300 C80 -250 -80 -250 -96 -300 Z", WH))
    o.append(E(-40, -322, 24, 32, BK, 0, rot=28) + E(40, -322, 24, 32, BK, 0, rot=-28))
    o.append(C(-36, -326, 7, WH, 0) + C(36, -326, 7, WH, 0) + C(-34, -326, 3.5, BK, 0) + C(38, -326, 3.5, BK, 0))
    o.append(E(0, -292, 14, 9, BK, 0))
    o.append(P("M0 -284 L0 -276 M-14 -270 Q0 -262 14 -270", sw=2.6))
    # belly hint
    o.append(P("M-60 -90 Q0 -70 60 -90", sw=2, col=MUTE))
    return "".join(o)


def panda(w, h):
    s, iso, T = slab(w, h, SAGE_L, "#cfe3c6", "#bcd6b1", W_=520, D=260, cy=h * 0.60)
    o = [s]
    stalks = [((0, 200), 1.0, 30), ((0, 120), .85, 90), ((0, 40), .75, 60), ((140, 0), .8, 70), ((300, 0), 1.0, 20), ((420, 0), .85, 80)]
    for (a, b), sc, top in stalks:
        x, y = iso.P(a, b, T)
        o.append(bamboo(x, y, top, sc))
        o.append(leafb(x, top + 60, -35 if x > w / 2 else 215, 62) + leafb(x, top + 140, 205 if x > w / 2 else -25, 56))
    for a, b in ((60, 230), (470, 60), (380, 250), (150, 120)):
        o.append(tuft(*iso.P(a, b, T), 1))
    cx, cy = w / 2, h * 0.70
    o.append(shadow(cx, cy, 170))
    o.append(G(panda_body(), cx, cy, 0.86))
    k = 0.86
    st = P("M0 0 L80 -250", sw=13) + P("M0 0 L80 -250", sw=8, col=SAGE_L) + P("M24 -76 l13 4 M56 -176 l13 4", sw=2.4)
    o.append(G(st, cx + 70 * k, cy - 110 * k))
    o.append(leafb(cx + 70 * k + 80, cy - 110 * k - 250, -60, 66) + leafb(cx + 70 * k + 80, cy - 110 * k - 250, 10, 58) + leafb(cx + 70 * k + 68, cy - 110 * k - 212, -130, 54))
    o.append(E(cx + 118 * k, cy - 170 * k, 28, 22, INK, rot=-25))
    return svg(w, h, "".join(o))



# ---------------------------------------------------------------- helpers
def leg(x0, x1, top, bot=0, fill="#fff", r=10):
    return P(f"M{x0} {top} L{x0} {bot-r} Q{x0} {bot} {x0+r} {bot} L{x1-r} {bot} Q{x1} {bot} {x1} {bot-r} L{x1} {top}", fill)


def bez(p, t):
    (a, b), (c, d), (e, f), (g, h) = p
    u = 1 - t
    return (u**3*a + 3*u*u*t*c + 3*u*t*t*e + t**3*g, u**3*b + 3*u*u*t*d + 3*u*t*t*f + t**3*h)


def tentacle(pts, w0, w1, fill, suck=True, side=1, n=26):
    L, R, cs = [], [], []
    for i in range(n + 1):
        t = i / n
        x, y = bez(pts, t)
        x2, y2 = bez(pts, min(1, t + 0.01)) if t < 1 else bez(pts, 1)
        if t >= 1:
            xa, ya = bez(pts, 0.99); dx, dy = x - xa, y - ya
        else:
            dx, dy = x2 - x, y2 - y
        m = math.hypot(dx, dy) or 1
        nx, ny = -dy / m, dx / m
        wd = (w0 + (w1 - w0) * t) / 2
        L.append((x + nx * wd, y + ny * wd)); R.append((x - nx * wd, y - ny * wd))
        if suck and 2 <= i <= n - 3 and i % 2 == 0:
            cs.append((x - side * nx * wd * .55, y - side * ny * wd * .55, max(2.2, wd * .32)))
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in L + R[::-1]) + " Z"
    o = P(d, fill, 2.8)
    for x, y, r in cs:
        o += C(round(x, 1), round(y, 1), round(r, 1), "#fff", 1.6, ORG)
    return o


def wavy(cx, cy, rx, ry, n=14, amp=12, rot=0):
    pts = []
    for i in range(n * 2):
        a = math.pi * 2 * i / (n * 2) + rot
        r = 1 + (amp / rx if i % 2 == 0 else -amp / rx * 0.2)
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(pts) + 1, 2):
        c = pts[i % len(pts)]; e = pts[(i + 1) % len(pts)]
        d += f" Q{c[0]:.1f} {c[1]:.1f} {e[0]:.1f} {e[1]:.1f}"
    return d + " Z"


def rock(x, y, s=1, fill="#e4e6e9"):
    return P(f"M{x-40*s} {y} L{x-32*s} {y-30*s} L{x-6*s} {y-44*s} L{x+26*s} {y-36*s} L{x+42*s} {y} Z", fill, 2.6) + P(f"M{x-6*s} {y-44*s} L{x+2*s} {y}", sw=1.8, col=MUTE)


def sun(x, y, r=40):
    o = C(x, y, r, YEL_L, 2.6, YEL)
    for i in range(8):
        a = math.pi * i / 4
        o += P(f"M{x+math.cos(a)*(r+10):.0f} {y+math.sin(a)*(r+10):.0f} L{x+math.cos(a)*(r+22):.0f} {y+math.sin(a)*(r+22):.0f}", sw=2.6, col=YEL)
    return o


# ---------------------------------------------------------------- domestic cat
def cat_body():
    F, S = ORG_L, ORG
    o = []
    o.append(P("M58 -10 C150 -4 168 -60 140 -110 C128 -132 150 -150 160 -132", sw=22) + P("M58 -10 C150 -4 168 -60 140 -110 C128 -132 150 -150 160 -132", sw=16, col=F))
    o.append(P("M-78 0 C-100 -90 -70 -190 0 -196 C70 -190 100 -90 78 0 Z", F))
    o.append(P("M-34 -150 C-40 -100 -40 -40 -30 0 M34 -150 C40 -100 40 -40 30 0", sw=2.4))
    o.append(P("M-30 0 C-34 -40 -30 -100 -18 -140 C-6 -120 6 -120 18 -140 C30 -100 34 -40 30 0 Z", "#fff", 2.4))
    o.append(E(-36, -6, 28, 14, F) + E(36, -6, 28, 14, F))
    for dy in (-150, -110):
        o.append(P(f"M-76 {dy} q14 -6 22 4 M76 {dy} q-14 -6 -22 4", sw=4, col=S))
    # head
    o.append(P("M-70 -300 L-58 -372 L-14 -330 Z M70 -300 L58 -372 L14 -330 Z", F))
    o.append(P("M-58 -356 L-52 -322 L-30 -334 Z M58 -356 L52 -322 L30 -334 Z", "#f6b8a0", 0))
    o.append(E(0, -268, 78, 66, F))
    o.append(P("M-12 -332 L-8 -306 M0 -334 L0 -304 M12 -332 L8 -306", sw=4, col=S))
    o.append(E(-30, -274, 13, 16, YEL, 2.4) + E(30, -274, 13, 16, YEL, 2.4))
    o.append(E(-30, -274, 4, 13, INK, 0) + E(30, -274, 4, 13, INK, 0))
    o.append(C(-27, -280, 3, "#fff", 0) + C(33, -280, 3, "#fff", 0))
    o.append(P("M-8 -246 L8 -246 L0 -237 Z", "#e88a8a", 2.2))
    o.append(P("M0 -237 Q-6 -226 -16 -228 M0 -237 Q6 -226 16 -228", sw=2.4))
    o.append(P("M-30 -240 L-96 -250 M-30 -234 L-94 -228 M30 -240 L96 -250 M30 -234 L94 -228", sw=1.8, col=GREY))
    return "".join(o)


def cushion(cx, cy, rx, ry, th=30):
    return (P(f"M{cx-rx} {cy} L{cx-rx} {cy+th} A{rx} {ry} 0 0 0 {cx+rx} {cy+th} L{cx+rx} {cy}", BLUE_M) +
            E(cx, cy, rx, ry, BLUE_L) + E(cx, cy, rx * .72, ry * .72, "none", 2, col=BLUE_M, extra='stroke-dasharray="6 6"'))


def yarn(x, y, r=34):
    o = C(x, y, r, ORG_L, 2.8)
    for k in (-.55, 0, .55):
        o += P(f"M{x-r*.92:.0f} {y+r*k*.6:.0f} Q{x:.0f} {y+r*k*.6-r*.5:.0f} {x+r*.92:.0f} {y+r*k*.6:.0f}", sw=2, col=ORG)
    o += P(f"M{x+r*.7:.0f} {y+r*.7:.0f} C{x+r*2:.0f} {y+r*1.6:.0f} {x+r*2.6:.0f} {y+r*.2:.0f} {x+r*3.6:.0f} {y+r*.9:.0f}", sw=2.4, col=ORG)
    return o


def cat(w, h):
    s, iso, T = slab(w, h, YEL_L, "#f5e3a6", "#ecd58a", W_=520, D=260, cy=h * 0.60)
    o = [s]
    # floorboards
    for a in range(65, 520, 65):
        o.append(P("M{:.0f} {:.0f} L{:.0f} {:.0f}".format(*iso.P(a, 0, T), *iso.P(a, 260, T)), sw=1.6, col="#e2c879"))
    # window frame behind
    o.append('<rect x="150" y="40" width="170" height="200" rx="8" fill="#fff" stroke="#1f2328" stroke-width="3"/>' +
             '<rect x="162" y="52" width="146" height="176" rx="4" fill="#dceafb" stroke="none"/>' +
             P("M235 52 V228 M162 140 H308", sw=3) + C(275, 95, 18, YEL_L, 2.4, YEL))
    o.append(yarn(*iso.P(400, 60, T + 30)))
    cx, cy = w / 2 + 10, h * 0.70
    o.append(cushion(cx, cy - 22, 160, 60))
    o.append(G(cat_body(), cx, cy - 28, 0.95))
    # fish toy
    fx, fy = iso.P(120, 220, T)
    o.append(P(f"M{fx-30} {fy} Q{fx} {fy-22} {fx+26} {fy} Q{fx} {fy+22} {fx-30} {fy} Z M{fx+26} {fy} L{fx+44} {fy-14} L{fx+44} {fy+14} Z", BLUE_L, 2.6) + C(fx - 14, fy - 3, 3, INK, 0))
    return svg(w, h, "".join(o))


# ---------------------------------------------------------------- african elephant
def elephant_body():
    F, D_ = "#e3e6ea", "#c9ced4"
    o = []
    o.append(leg(70, 116, -200, 0, D_, 14) + leg(-92, -48, -200, 0, D_, 14))
    o.append(P("M190 -250 C204 -200 206 -170 200 -140", sw=3) + P("M196 -150 l-6 18 M200 -148 l2 18 M204 -150 l8 16", sw=2.4))
    o.append(P("M-130 -200 C-150 -290 -90 -350 10 -352 C120 -354 196 -310 194 -226 C192 -180 176 -160 160 -150 L-100 -150 C-120 -160 -128 -175 -130 -200 Z", F))
    o.append(leg(118, 168, -190, 0, F, 14) + leg(-46, 2, -190, 0, F, 14))
    for x in (130, 144, 156, -36, -22, -8):
        o.append(P(f"M{x} -2 v-8", sw=2, col=GREY))
    o.append(P("M-60 -150 Q30 -134 120 -150", sw=2, col=MUTE))
    # head
    o.append(P("M-110 -330 C-180 -350 -240 -310 -236 -240 C-234 -200 -222 -180 -204 -168 L-130 -180 Z", F))
    # trunk
    tr = "M-224 -210 C-262 -160 -252 -90 -258 -40 C-262 -10 -238 2 -228 -22"
    o.append(P(tr, sw=40) + P(tr, sw=33, col=F))
    for y in (-150, -125, -100, -75):
        o.append(P(f"M-268 {y} q12 4 22 0", sw=1.8, col=GREY))
    # tusk
    o.append(P("M-214 -198 C-228 -160 -258 -140 -296 -146 C-266 -158 -244 -174 -232 -200 Z", "#fffdf4", 2.6))
    # ear
    o.append(P("M-150 -336 C-60 -370 -10 -300 -24 -220 C-34 -160 -80 -130 -116 -160 C-140 -180 -128 -210 -150 -230 C-170 -260 -176 -310 -150 -336 Z", "#d3d8de"))
    o.append(P("M-130 -300 C-80 -310 -60 -260 -66 -210", sw=2, col=GREY))
    o.append(C(-196, -276, 6, INK, 0) + P("M-210 -290 q12 -8 24 -2", sw=2.2))
    return "".join(o)


def acacia(x, y, s=1):
    o = P(f"M{x} {y} C{x+4*s} {y-70*s} {x-10*s} {y-120*s} {x-50*s} {y-160*s} M{x+2*s} {y-80*s} C{x+30*s} {y-110*s} {x+50*s} {y-140*s} {x+70*s} {y-160*s}", sw=9 * s) + \
        P(f"M{x} {y} C{x+4*s} {y-70*s} {x-10*s} {y-120*s} {x-50*s} {y-160*s} M{x+2*s} {y-80*s} C{x+30*s} {y-110*s} {x+50*s} {y-140*s} {x+70*s} {y-160*s}", sw=4 * s, col="#cdb48a")
    o += P(f"M{x-130*s} {y-160*s} C{x-120*s} {y-200*s} {x-40*s} {y-214*s} {x+10*s} {y-206*s} C{x+60*s} {y-220*s} {x+140*s} {y-204*s} {x+150*s} {y-166*s} C{x+90*s} {y-150*s} {x-60*s} {y-148*s} {x-130*s} {y-160*s} Z", SAGE_L)
    o += P(f"M{x-90*s} {y-170*s} q40 -12 80 0 M{x+20*s} {y-176*s} q40 -12 90 4", sw=2, col=SAGE)
    return o


def elephant(w, h):
    s, iso, T = slab(w, h, YEL_L, "#f5e3a6", "#ecd58a", W_=540, D=250, cy=h * 0.62)
    o = [s, sun(800, 80)]
    o.append(acacia(*iso.P(500, 20, T), 1.35))
    for a, b in ((60, 220), (300, 240), (500, 180), (120, 40), (380, 90)):
        o.append(tuft(*iso.P(a, b, T), 1.1, col="#b8a15a"))
    cx, cy = w / 2 + 20, h * 0.76
    o.append(shadow(cx - 20, cy, 220))
    o.append(G(elephant_body(), cx, cy, 1.05))
    return svg(w, h, "".join(o))


# ---------------------------------------------------------------- emperor penguin
def penguin_body(chick=False):
    o = []
    if not chick:
        o.append(P("M0 -380 C-52 -382 -72 -330 -76 -272 C-92 -170 -96 -80 -70 -20 C-50 8 50 8 70 -20 C96 -80 92 -170 76 -272 C72 -330 52 -382 0 -380 Z", INK))
        o.append(P("M0 -300 C-38 -300 -58 -250 -62 -180 C-68 -100 -56 -30 -40 -10 C-20 2 20 2 40 -10 C56 -30 68 -100 62 -180 C58 -250 38 -300 0 -300 Z", "#fff", 0))
        o.append(P("M-44 -280 C-34 -300 34 -300 44 -280 C30 -250 -30 -250 -44 -280 Z", YEL_L, 0))
        o.append(P("M-58 -320 C-48 -300 -50 -270 -36 -262 C-30 -280 -40 -310 -58 -320 Z M58 -320 C48 -300 50 -270 36 -262 C30 -280 40 -310 58 -320 Z", YEL, 0))
        o.append(P("M-74 -240 C-110 -180 -118 -120 -100 -90 C-90 -110 -78 -170 -66 -210 Z", INK, 2.6) + P("M74 -240 C110 -180 118 -120 100 -90 C90 -110 78 -170 66 -210 Z", INK, 2.6))
        o.append(P("M-10 -346 C-6 -326 -2 -310 4 -296 C8 -316 10 -334 10 -346 Z", INK, 0) + P("M-2 -330 L4 -300", sw=3, col=ORG))
        o.append(C(-24, -350, 4, "#fff", 0) + C(24, -350, 4, "#fff", 0))
        o.append(E(-26, -2, 22, 8, INK, 0) + E(26, -2, 22, 8, INK, 0))
    else:
        o.append(P(wavy(0, -60, 52, 62, 12, 5), "#d9dcdf", 2.6))
        o.append(C(0, -142, 40, INK, 0))
        o.append(P("M-30 -146 C-30 -120 30 -120 30 -146 C24 -132 -24 -132 -30 -146 Z", "#fff", 0) + E(-16, -150, 11, 12, "#fff", 0) + E(16, -150, 11, 12, "#fff", 0))
        o.append(C(-15, -150, 4, INK, 0) + C(15, -150, 4, INK, 0) + P("M-5 -138 L0 -126 L5 -138 Z", INK, 0))
        o.append(E(-18, -2, 14, 6, INK, 0) + E(18, -2, 14, 6, INK, 0))
    return "".join(o)


def penguin(w, h):
    o = []
    # sea
    o.append(f'<rect x="0" y="{h*0.42:.0f}" width="{w}" height="{h*0.58:.0f}" fill="{BLUE_L}" stroke="none"/>')
    for y in (300, 360, 470, 540):
        for x in (60, 700, 820):
            o.append(P(f"M{x} {y} q15 -8 30 0 q15 8 30 0", sw=2, col=BLUE_M))
    # icebergs
    o.append(P(f"M40 {h*0.42:.0f} L90 150 L150 120 L220 190 L260 {h*0.42:.0f} Z", "#fff", 2.6) + P("M150 120 L160 252", sw=1.8, col=BLUE_M))
    o.append(P(f"M690 {h*0.42:.0f} L740 170 L800 190 L860 140 L900 {h*0.42:.0f} Z", "#fff", 2.6) + P("M800 190 L790 252", sw=1.8, col=BLUE_M))
    s, iso, T = slab(w, h, "#ffffff", "#e8f1fb", BLUE_M, W_=480, D=250, T=34, cy=h * 0.63)
    o.append(s)
    for a, b in ((80, 60), (360, 200)):
        x, y = iso.P(a, b, T)
        o.append(P(f"M{x-24} {y} l20 -6 l18 8", sw=2, col=BLUE_M))
    cx, cy = w / 2 - 30, h * 0.74
    o.append(shadow(cx, cy, 90) + shadow(cx + 140, cy - 10, 60))
    o.append(G(penguin_body(), cx, cy, 1.15))
    o.append(G(penguin_body(True), cx + 140, cy - 10, 1.0))
    # snowflakes
    for x, y in ((330, 60), (600, 40), (640, 150), (300, 170)):
        o.append(P(f"M{x-9} {y} H{x+9} M{x} {y-9} V{y+9} M{x-6} {y-6} L{x+6} {y+6} M{x-6} {y+6} L{x+6} {y-6}", sw=2, col=BLUE_M))
    return svg(w, h, "".join(o))


# ---------------------------------------------------------------- common octopus
def octopus_body():
    F = ORG_L
    o = []
    arms = [
        (((-40, -170), (-120, -150), (-230, -140), (-260, -60)), 1),
        (((-30, -160), (-80, -80), (-170, -10), (-120, 20)), 1),
        (((-14, -150), (-30, -60), (-70, 0), (-30, 14)), -1),
        (((40, -170), (120, -150), (230, -150), (250, -70)), -1),
        (((30, -160), (90, -90), (170, -20), (130, 18)), -1),
        (((14, -150), (40, -60), (80, -10), (40, 12)), 1),
    ]
    back = [(((-50, -190), (-170, -230), (-250, -250), (-290, -200)), 1), (((50, -190), (170, -240), (260, -260), (300, -210)), -1)]
    for pts, sd in back:
        o.append(tentacle(pts, 34, 6, "#f9cdb3", True, sd))
    o.append(P("M-58 -210 C-100 -290 -78 -410 0 -414 C78 -410 100 -290 58 -210 Z", F))
    for x, y, r in ((-30, -340, 9), (24, -370, 7), (36, -300, 10), (-10, -290, 6), (-46, -280, 6)):
        o.append(C(x, y, r, "#f6b38e", 0))
    for pts, sd in arms:
        o.append(tentacle(pts, 40, 8, F, True, sd))
    o.append(E(0, -190, 74, 44, F))
    o.append(E(-34, -200, 18, 16, "#fff", 2.6) + E(34, -200, 18, 16, "#fff", 2.6))
    o.append('<rect x="-44" y="-203" width="20" height="7" rx="3.5" fill="#1f2328"/><rect x="24" y="-203" width="20" height="7" rx="3.5" fill="#1f2328"/>')
    o.append(P("M-50 -224 q16 -10 32 -2 M50 -224 q-16 -10 -32 -2", sw=2.4))
    return "".join(o)


def seaweed(x, y, hgt, s=1):
    d = f"M{x} {y} C{x-20*s} {y-hgt*.3} {x+20*s} {y-hgt*.6} {x} {y-hgt}"
    return P(d, sw=12 * s) + P(d, sw=7 * s, col=SAGE_L)


def octopus(w, h):
    o = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{BLUE_L}" fill-opacity=".55" stroke="none"/>']
    for x0 in (120, 380, 640):
        o.append(P(f"M{x0} 0 L{x0+60} {h*0.5:.0f} L{x0+120} 0", "#ffffff", 0, extra='fill-opacity=".45"'))
    s, iso, T = slab(w, h, YEL_L, "#f5e3a6", "#ecd58a", W_=520, D=260, cy=h * 0.62)
    o.append(s)
    for (a, b), hh, sc in (((40, 200), 260, 1.0), ((20, 120), 200, .8), ((470, 30), 280, 1.0), ((500, 110), 190, .8)):
        o.append(seaweed(*iso.P(a, b, T), hh, sc))
    for (a, b), sc in (((380, 60), 1.3), ((100, 40), 1.0), ((440, 220), .9)):
        o.append(rock(*iso.P(a, b, T), sc))
    sx, sy = iso.P(200, 230, T)
    o.append(P(f"M{sx-26} {sy} Q{sx} {sy-40} {sx+26} {sy} Z", "#fff", 2.6) + P(f"M{sx} {sy} L{sx-12} {sy-24} M{sx} {sy} L{sx} {sy-28} M{sx} {sy} L{sx+12} {sy-24}", sw=1.6, col=GREY))
    cx, cy = w / 2 + 10, h * 0.72
    o.append(shadow(cx, cy + 6, 200))
    o.append(G(octopus_body(), cx, cy, 1.0))
    for x, y, r in ((620, 120, 12), (650, 70, 8), (634, 30, 6), (300, 150, 9), (280, 100, 6)):
        o.append(C(x, y, r, "#fff", 2.2, BLUE))
    return svg(w, h, "".join(o))


# ---------------------------------------------------------------- lion
def lion_body():
    F, M = "#f9e2b3", ORG_L
    o = []
    o.append(P("M180 -236 C220 -220 236 -170 240 -110", sw=12) + P("M180 -236 C220 -220 236 -170 240 -110", sw=6, col=F))
    o.append(P(wavy(244, -98, 16, 20, 6, 6), ORG, 2.6))
    o.append(leg(118, 154, -170, 0, "#efd29a", 12) + leg(-96, -62, -170, 0, "#efd29a", 12))
    o.append(P("M-120 -240 C-60 -266 80 -262 150 -248 C196 -236 200 -180 180 -150 L170 -140 L-100 -140 C-130 -160 -140 -210 -120 -240 Z", F))
    o.append(P("M140 -250 C186 -230 190 -170 168 -130 L160 0 L124 0 L126 -120 C110 -150 108 -200 140 -250 Z", F))
    o.append(leg(-56, -18, -170, 0, F, 12))
    o.append(P("M-50 -160 Q40 -140 120 -150", sw=2, col=MUTE))
    for x in (126, 140, -48, -34):
        o.append(P(f"M{x} -2 v-8", sw=2, col=GREY))
    o.append(P(wavy(-150, -270, 92, 100, 15, 14, 0.2), M, 3))
    o.append(P(wavy(-150, -270, 70, 78, 13, 10, 0.5), "#f6c9a4", 2))
    o.append(C(-118, -340, 16, F) + C(-196, -330, 16, F))
    o.append(E(-160, -262, 58, 62, F))
    o.append(E(-170, -226, 34, 24, "#fff7e6", 2.4))
    o.append(P("M-186 -248 L-160 -248 L-172 -234 Z", "#c4795a", 2.2))
    o.append(P("M-172 -234 V-222 M-172 -222 q-10 8 -20 2 M-172 -222 q10 8 20 2", sw=2.4))
    o.append(E(-184, -280, 6, 7, INK, 0) + E(-138, -280, 6, 7, INK, 0))
    o.append(P("M-196 -294 q12 -6 22 0 M-150 -294 q12 -6 22 0", sw=2.2))
    o.append(C(-198, -226, 2, INK, 0) + C(-192, -218, 2, INK, 0) + C(-150, -226, 2, INK, 0) + C(-154, -218, 2, INK, 0))
    return "".join(o)


def lion(w, h):
    s, iso, T = slab(w, h, YEL_L, "#f5e3a6", "#ecd58a", W_=540, D=250, cy=h * 0.62)
    o = [s, sun(150, 90, 36)]
    kx, ky = iso.P(470, 50, T)
    o.append(P(f"M{kx-120} {ky+10} L{kx-100} {ky-70} L{kx-40} {ky-110} L{kx+40} {ky-96} L{kx+90} {ky-40} L{kx+100} {ky+20} Z", "#ece7df", 2.8) +
             P(f"M{kx-40} {ky-110} L{kx-20} {ky+10} M{kx+40} {ky-96} L{kx+30} {ky-20}", sw=1.8, col=MUTE))
    for a, b in ((60, 220), (300, 240), (500, 190), (120, 40), (200, 130), (420, 160)):
        o.append(tuft(*iso.P(a, b, T), 1.2, col="#b8a15a"))
    cx, cy = w / 2 + 40, h * 0.76
    o.append(shadow(cx, cy, 210))
    o.append(G(lion_body(), cx, cy, 1.1))
    return svg(w, h, "".join(o))


ART = {"giant-panda": panda, "domestic-cat": cat, "african-elephant": elephant,
       "emperor-penguin": penguin, "common-octopus": octopus, "lion": lion}


try:
    import art2 as _a2
    ART.update(_a2.ART2)
except ImportError as _e:  # pragma: no cover
    raise
