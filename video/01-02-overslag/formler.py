# Lager formelbildene f1–f3 til animasjonen:  python3 video/01-02-overslag/formler.py video/01-02-overslag
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, sys, os
plt.rcParams['mathtext.fontset']='cm'
ut=sys.argv[1]
F={'f1':(r'$10^{3}=1000\qquad 10^{-3}=0{,}001$',54,'#ecefe6'),
   'f2':(r'$V=5\cdot10^{6}\cdot 8\ \mathrm{min}\cdot 10\ \mathrm{L/min}$',54,'#ecefe6'),
   'f3':(r'$V=4\cdot10^{8}\ \mathrm{L}$',70,'#6ef04a')}
for k,(t,fs,c) in F.items():
    fig=plt.figure(figsize=(0.1,0.1),dpi=100)
    fig.text(0,0,t,fontsize=fs,color=c)
    fig.savefig(os.path.join(ut,k+'.png'),transparent=True,bbox_inches='tight',pad_inches=0.08,dpi=100)
    plt.close(fig)
