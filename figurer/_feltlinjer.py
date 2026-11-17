#!/usr/bin/env python3
"""Regner ut feltlinjer og skriver TikZ-filene masse-tiltrekning.tex og ladning-fire-tilfeller.tex.
Kjør: python3 figurer/_feltlinjer.py && python3 figurer/lag.py"""
import math
from pathlib import Path
H = Path(__file__).resolve().parent
FELT = r'\definecolor{felt}{RGB}{215,120,30}' '\n' r'\tikzset{fl/.style={felt,thin,opacity=.85}, flp/.style={felt,thin,opacity=.85,-{Stealth[length=1.7mm]}}}' '\n'

def linje(pts, pil_inn=False):
    """Polyline + en liten pil midt på (i linjas retning, eller motsatt med pil_inn)."""
    s = r'\draw[fl] ' + ' -- '.join(f'({x:.2f},{y:.2f})' for x, y in pts) + ';\n'
    i = len(pts) // 2
    a, b = pts[i], pts[min(i + 2, len(pts) - 1)]
    if pil_inn: a, b = b, a
    return s + rf'\draw[flp] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});' + '\n'

def E(x, y, ladn):
    ex = ey = 0.0
    for (qx, qy, q) in ladn:
        dx, dy = x - qx, y - qy; r3 = (dx * dx + dy * dy) ** 1.5
        ex += q * dx / r3; ey += q * dy / r3
    return ex, ey

def spor(x, y, ladn, boks, retning=1, h=0.02, r_stopp=0.3):
    pts = [(x, y)]
    for _ in range(2000):
        ex, ey = E(x, y, ladn); n = math.hypot(ex, ey)
        x += retning * h * ex / n; y += retning * h * ey / n
        pts.append((x, y))
        if not (boks[0] < x < boks[1] and boks[2] < y < boks[3]): break
        if any(math.hypot(x - qx, y - qy) < r_stopp for qx, qy, _ in ladn): break
    return pts[::4] + [pts[-1]]

def par(cx, cy, qa, qb, d=1.3, n=12, bx=2.9, by=1.55):
    """To ladninger qa (venstre) og qb (høyre) med sentrum (cx, cy). Feltlinjer ut fra + (eller inn mot − når begge er −)."""
    ladn = [(cx - d, cy, qa), (cx + d, cy, qb)]
    boks = (cx - bx, cx + bx, cy - by, cy + by)
    ut = ''
    for (qx, qy, q) in ladn:
        if qa < 0 and qb < 0:  # begge negative: spor baklengs fra hver ladning, pil innover
            ret, inn = -1, True
        elif q > 0:
            ret, inn = 1, False
        else:  # negativ i et par med motsatt fortegn: bare linjene som kommer utenfra
            ret, inn = -1, True
        for k in range(n):
            v = 2 * math.pi * (k + .5) / n
            pts = spor(qx + .36 * math.cos(v), qy + .36 * math.sin(v), ladn, boks, ret, r_stopp=.36)
            ende = pts[-1]
            if q < 0 and qa * qb < 0 and any(math.hypot(ende[0] - x, ende[1] - y) < .4 for x, y, _ in ladn): continue
            ut += linje(pts, inn)
    return ut

# --- Ladningsparene ---
t = FELT + r'\begin{tikzpicture}[scale=1.0]' '\n' r'\tikzset{q/.style={circle,draw,thick,minimum size=7mm,font=\large,inner sep=0pt}}' '\n'
paneler = [(0, 0, 1, 1), (6.6, 0, -1, -1), (0, -3.9, 1, -1), (6.6, -3.9, -1, 1)]
for cx, cy, qa, qb in paneler:
    t += par(cx, cy, qa, qb)
for cx, cy, qa, qb in paneler:
    s = lambda q: '+' if q > 0 else '-'
    t += rf'\node[q] (a) at ({cx-1.3},{cy}) {{${s(qa)}$}}; \node[q] (b) at ({cx+1.3},{cy}) {{${s(qb)}$}};' '\n'
    if qa * qb > 0:
        t += r'\draw[vek,rod] (a.west)--++(-1.0,0) node[above,pos=.6,font=\small]{$\vec F$}; \draw[vek,rod] (b.east)--++(1.0,0) node[above,pos=.6,font=\small]{$\vec F$};' '\n'
    else:
        t += r'\draw[vek,rod] (a.east)--++(0.8,0) node[above,pos=.55,font=\small]{$\vec F$}; \draw[vek,rod] (b.west)--++(-0.8,0) node[above,pos=.55,font=\small]{$\vec F$};' '\n'
t += r'\node[font=\small] at (3.3,-1.9) {Like ladninger frastøter hverandre};' '\n'
t += r'\node[font=\small] at (3.3,-5.8) {Motsatte ladninger tiltrekker hverandre};' '\n'
t += r'\end{tikzpicture}' '\n'
(H / 'ladning-fire-tilfeller.tex').write_text(t, encoding='utf-8')

# --- Jorda og månen ---
t = FELT + r'\begin{tikzpicture}[scale=1.0]' '\n'
for k in range(16):
    v = 2 * math.pi * (k + .5) / 16
    t += linje([(r * math.cos(v), r * math.sin(v)) for r in (2.6, 2.0, 1.4)])
for k in range(8):
    v = 2 * math.pi * (k + .5) / 8
    t += linje([(6.2 + r * math.cos(v), r * math.sin(v)) for r in (1.0, 0.78, 0.55)])
t += r'''\draw[very thick,bla] (0,0) circle (1.3);
\node at (0,0) {Jorda};
\draw[thick] (6.2,0) circle (0.45);
\node[below=1mm] at (6.2,-1.0) {Månen};
\draw[vek,rod] (1.3,0)--++(1.5,0) node[above,midway]{$\vec G$};
\draw[vek,rod] (5.75,0)--++(-1.5,0) node[above,midway]{$\vec G$};
\node[font=\small,align=center] at (3.1,-2.9) {Masse trekker alltid på masse};
\end{tikzpicture}
'''
(H / 'masse-tiltrekning.tex').write_text(t, encoding='utf-8')
print('skrevet')
