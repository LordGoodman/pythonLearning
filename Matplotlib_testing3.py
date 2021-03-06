import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.rcParams['toolbar'] = 'None'

fig = plt.figure(figsize=(6,6),facecolor='white')

ax = fig.add_axes([0,0,1,1],frameon=False,aspect=1)

n = 50
size_min = 50
size_max = 50*50

P = np.random.uniform(0,1,(n,2))
C = np.ones((n,4)) * (0,0,0,1)
S = np.linspace(size_min,size_max,n)
C[:,3] = np.linspace(0,1,n)

scat = ax.scatter(P[:,0],P[:,1],s=S,lw=0.5,edgecolors=C,facecolors='None')

ax.set_xlim(0,1),ax.set_xticks([])
ax.set_ylim(0,1),ax.set_yticks([])

def update(frame):
    global S,C,P
    #ring become lager
    S[:]+= (size_max - size_min)/n 
    
    #ring become more transperant
    C[:,3] =np.maximum(0,C[:,3] - 1.0/n)
    
    i = frame %50
    
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1
    
    scat.set_edgecolor(C)
    scat.set_sizes(S)
    scat.set_offsets(P) 

    return scat,
    
animation = FuncAnimation(fig, update, interval=10)
     
plt.show()
