import numpy as np
import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(6,6),facecolor='white',)
ax = fig.add_axes([0,0,1,1],frameon='None',aspect=1)


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
#T = np.ones((n,1)) * -1.93648626

sact = ax.scatter(X,Y,s=75,lw=0.5,c=T,alpha=0.5)

ax.set_xlim(-1.5,1.5),ax.set_xticks([])
ax.set_ylim(-1.5,1.5),ax.set_yticks([])

print T
plt.show()