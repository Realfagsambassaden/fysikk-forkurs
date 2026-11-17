#!/usr/bin/env python3
"""Regner ut feltlinjene i og rundt et stående batteri (mange + ved pluss-polen øverst, mange − ved minus-polen nederst)
og skriver batteri-felt.tex. Kjør: python3 figurer/_batteri.py && python3 figurer/lag.py"""
import math
from pathlib import Path
H = Path(__file__).resolve().parent
pos = [(-0.75, 2.1), (-0.25, 2.1), (0.25, 2.1), (0.75, 2.1), (-0.5, 1.75), (0.0, 1.75), (0.5, 1.75)]
L = [(x, y, 1) for x, y in pos] + [(x, -y, -1) for x, y in pos]
boks = (-10, 10, -12, 12)
def E(x, y):
    ex = ey = 0.0
    for qx, qy, q in L:
        dx, dy = x - qx, y - qy; r3 = (dx*dx + dy*dy) ** 1.5
        ex += q*dx/r3; ey += q*dy/r3
    return ex, ey
def spor(x, y, h=0.02):
    p = [(x, y)]
    for _ in range(3000):
        ex, ey = E(x, y); n = math.hypot(ex, ey)
        x += h*ex/n; y += h*ey/n; p.append((x, y))
        if not (boks[0] < x < boks[1] and boks[2] < y < boks[3]): break
        if any(q < 0 and math.hypot(x-qx, y-qy) < 0.28 for qx, qy, q in L): break
    return p[::4] + [p[-1]]
def linje(p):
    s = r'\draw[fl] ' + ' -- '.join(f'({x:.2f},{y:.2f})' for x, y in p) + ';\n'
    inne = [j for j, (x, y) in enumerate(p[:-2]) if abs(x) < 2.5 and abs(y) < 3.5]
    i = min(inne, key=lambda j: abs(p[j][1])) if inne else len(p)//2
    if abs(p[i][1]) > 1.5: i = inne[min(3, len(inne)-1)]
    a, b = p[i], p[min(i+2, len(p)-1)]
    return s + rf'\draw[flp] ({a[0]:.3f},{a[1]:.3f}) -- ({b[0]:.3f},{b[1]:.3f});' + '\n'
t = r'\definecolor{felt}{RGB}{215,120,30}' '\n' r'\tikzset{fl/.style={felt,thin,opacity=.85}, flp/.style={felt,thin,opacity=.85,-{Stealth[length=1.7mm]}}}' '\n'
t += r'\begin{tikzpicture}[scale=0.8]' '\n' r'\begin{scope}' '\n' r'\clip (-2.7,-3.6) rectangle (2.7,3.6);' '\n'
for k in range(18):
    v = 2*math.pi*(k+.5)/18
    t += linje(spor(1.1*math.cos(v), 1.92 + 0.42*math.sin(v)))
t += r'\end{scope}' '\n'
t += r'''\draw[very thick] (-1.25,-2.5) rectangle (1.25,2.5);
\draw[very thick] (-0.4,2.5) rectangle (0.4,2.85);
\node[anchor=west] at (2.85,1.95) {pluss-pol};
\node[anchor=west] at (2.85,-1.95) {minus-pol};
'''
for qx, qy, q in L:
    t += rf'\node[inner sep=0pt,font=\large] at ({qx},{qy}) {{${"+" if q > 0 else "-"}$}};' '\n'
t += r'\end{tikzpicture}' '\n'
(H / 'batteri-felt.tex').write_text(t, encoding='utf-8'); print('skrevet')
