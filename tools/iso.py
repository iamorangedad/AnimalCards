"""Palette + dimetric projection helper, extracted from the OrangeSTEM v4 poster scenes (scenes_v4.py)."""
import math

INK, GREY, MUTE = "#1f2328", "#6b7075", "#c9ccd1"
BLUE, BLUE_L, BLUE_M = "#2f7de1", "#dceafb", "#9cc4f3"
ORG, ORG_L = "#e8692e", "#fde3d3"
YEL, YEL_L = "#f6c343", "#fff1c2"
SAGE, SAGE_L = "#5f8f5a", "#e1efda"
PAPER = "#ffffff"
SW = 2.6  # standard stroke width
LINE = f'stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'


class Iso:
    def __init__(self, ox, oy, k=1.0):
        self.ox, self.oy, self.k = ox, oy, k

    def P(self, x, y, z=0):
        return (self.ox + (x - y) * 0.894 * self.k, self.oy + ((x + y) * 0.447 - z) * self.k)

    def poly(self, pts, fill, extra=""):
        d = " ".join(f"{a:.1f},{b:.1f}" for a, b in (self.P(*p) for p in pts))
        return f'<polygon points="{d}" fill="{fill}" {LINE} {extra}/>'

    def path(self, pts, fill="none", close=True, extra=""):
        q = [self.P(*p) for p in pts]
        d = "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in q) + (" Z" if close else "")
        return f'<path d="{d}" fill="{fill}" {LINE} {extra}/>'

    def box(self, x0, y0, z0, W, D, Hh, top, left, right):
        x1, y1, z1 = x0 + W, y0 + D, z0 + Hh
        return (self.poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], left)
                + self.poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], right)
                + self.poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], top))
