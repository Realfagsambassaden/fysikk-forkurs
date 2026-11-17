#!/usr/bin/env python3
"""U–I-kurver for en ohmsk motstand, en glødelampe og en silisiumdiode. Skriver ikke-ohmske.tex.
Modeller (realistiske, men forenklede):
- motstand: U = R I med R = 24 ohm
- glødelampe 12 V / 0.5 A (wolfram): I ≈ 0.5 A · (U/12 V)^0.55. Dobbel spenning gir ca. 1.4–1.5 ganger strømmen,
  og kald resistans blir ca. 1/10 av varm, som målt for wolframlamper.
- Si-likeretterdiode (som 1N4001): Shockley-likningen I = I_s (e^{U/(n V_T)} − 1) med I_s = 5 nA, n = 2, V_T = 25.9 mV.
  Gir ca. 0.7 V ved noen mA og ca. 1.0 V ved 1 A, som i databladene.
Kjør: python3 figurer/_ikke-ohmske.py && python3 figurer/lag.py"""
import math
from pathlib import Path
H = Path(__file__).resolve().parent
W, Hh = 4.0, 3.0   # panelstørrelse (cm)

def panel(x0, tittel, imax, umax, kurve, itikk, utikk, ienhet='A', ekstra=''):
    sx, sy = W / imax, Hh / umax
    s = rf'\begin{{scope}}[xshift={x0}cm]' '\n'
    s += rf'\draw[akse] (0,0) -- ({W+0.3},0) node[right,font=\small]{{$I$ ({ienhet})}};' '\n'
    s += rf'\draw[akse] (0,0) -- (0,{Hh+0.35}) node[left,font=\small]{{$U$ (V)}};' '\n'
    for v, lab in itikk: s += rf'\draw ({v*sx:.3f},0) -- ({v*sx:.3f},-0.08) node[below,font=\scriptsize]{{${lab}$}};' '\n'
    for v, lab in utikk: s += rf'\draw (0,{v*sy:.3f}) -- (-0.08,{v*sy:.3f}) node[left,font=\scriptsize]{{${lab}$}};' '\n'
    pts = [(i*sx, u*sy) for i, u in kurve if u <= umax*1.001 and i <= imax*1.001]
    s += r'\draw[very thick,gronn] ' + ' -- '.join(f'({x:.3f},{y:.3f})' for x, y in pts) + ';\n'
    s += rf'\node[font=\bfseries\small] at ({W/2},{Hh+0.75}) {{{tittel}}};' '\n' + ekstra
    s += r'\end{scope}' '\n'
    return s

N = 200
mot = [(0.5*k/N, 24*0.5*k/N) for k in range(N+1)]
lampe = [(0.5*(k/N), 12*(k/N)**(1/0.55)) for k in range(N+1)]
Is, nVT = 5e-9, 2*0.0259
diode = [(i, nVT*math.log(i/Is + 1)) for i in [0] + [10**(-9 + 9*k/N) for k in range(N+1)]]
diode = [(i, u) for i, u in diode if i <= 1.0]
diode = [(0, 0)] + diode

t = r'\begin{tikzpicture}' '\n'
t += panel(0, 'Ohmsk motstand', 0.5, 12, mot, [(0.25, '0.25'), (0.5, '0.50')], [(6, '6'), (12, '12')],
           ekstra=r'\node[font=\scriptsize,align=center] at (2.6,0.8) {rett linje:\\ $R$ er konstant};' '\n')
t += panel(5.6, 'Glødelampe', 0.5, 12, lampe, [(0.25, '0.25'), (0.5, '0.50')], [(6, '6'), (12, '12')],
           ekstra=r'\draw[dashed,rod] (0,0) -- (1.25,0.31);' '\n' r'\node[font=\scriptsize,align=left,rod,anchor=west] at (0.15,1.35) {nesten rett:\\ ohmsk når\\ tråden er kald};' '\n' r'\draw[->,thin,rod] (0.5,0.85) -- (0.6,0.25);' '\n'
                  r'\node[font=\scriptsize,align=center] at (1.4,2.6) {$R$ øker når\\ tråden blir varm};' '\n')
t += panel(11.2, 'Diode (silisium)', 1.0, 1.2, diode, [(0.5, '0.5'), (1.0, '1.0')], [(0.6, '0.6'), (1.2, '1.2')],
           ekstra=r'\node[font=\scriptsize,align=center] at (2.4,1.5) {nesten fast\\ $U \approx 0.7$–$1.0\ \mathrm{V}$};' '\n')
t += r'\end{tikzpicture}' '\n'
(H / 'ikke-ohmske.tex').write_text(t, encoding='utf-8'); print('skrevet')
