"""PJ-320B-SMT 3D model (XKB 3.5 mm stereo jack, SMT, right angle, no switch).

Built from XKB drawing X-PJ-320B-SMT rev A1 (and the SOFNG PJ-320B sheet, same
outline):
  body   11.3 long x 6.0 wide x 5.0 high, black
  nose   dia 5.0, 2.7 long, plug opening dia 3.6 (total length 14.0)
  pegs   two locating pegs, dia 0.7 x 1.0 below the board, 6.0 apart
  leads  three flat SMT leads, 1.2 wide, out of the body sides to +-4.0:
         3 sleeve and 4 tip on one side (2.1 / 9.1 from the body front),
         2 ring on the other (4.1)

Coordinates are KiCad's model frame: origin = footprint origin (midpoint of
the pegs), plug enters from -X, Y = -(footprint Y), Z up from the board.

Rebuild:  python3 PJ-320B-SMT.py   (needs cadquery)
"""
import os
import cadquery as cq

X_NOSE, X_FRONT, X_BACK = -7.8, -5.1, 6.2
W, H = 3.0, 5.0
T = 0.2  # lead thickness


def box(x0, x1, y0, y1, z0, z1):
    return (cq.Workplane("XY")
            .box(x1 - x0, y1 - y0, z1 - z0, centered=False)
            .translate((x0, y0, z0)))


def xcyl(x0, x1, r, z):
    return (cq.Workplane("YZ").workplane(offset=x0)
            .center(0, z).circle(r).extrude(x1 - x0))


body = box(X_FRONT, X_BACK, -W, W, 0, H)
nose = xcyl(X_NOSE, X_FRONT, 2.5, H / 2)
shell = body.union(nose).cut(xcyl(X_NOSE - 0.1, X_BACK - 1.5, 1.8, H / 2))
pegs = (cq.Workplane("XY").pushPoints([(-3, 0), (3, 0)])
        .circle(0.35).extrude(-1.0))
shell = shell.union(pegs)


def lead(x, side):
    # side = +1 model +Y (footprint -Y), -1 model -Y (footprint +Y)
    ya, yb = sorted((side * W, side * 4.0))
    foot = box(x - 0.6, x + 0.6, ya, yb, 0, T)
    yc, yd = sorted((side * W, side * (W + T)))
    riser = box(x - 0.6, x + 0.6, yc, yd, 0, 1.6)
    return foot.union(riser)


# footprint pads: 3 (-3,+4) sleeve, 2 (-1,-4) ring, 4 (+4,+4) tip
leads = lead(-3, -1).union(lead(-1, +1)).union(lead(4, -1))

asm = cq.Assembly(name="PJ-320B-SMT")
asm.add(shell, name="body", color=cq.Color(0.08, 0.08, 0.08))
asm.add(leads, name="leads", color=cq.Color(0.82, 0.82, 0.85))

here = os.path.dirname(os.path.abspath(__file__))
asm.export(os.path.join(here, "PJ-320B-SMT.step"))
print("written PJ-320B-SMT.step")
