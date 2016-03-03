import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,4),facecolor='white')
ax = fig.add_axes([0,0,1,1],frameon='None',aspect=1)


n = 256
X = np.linspace(-np.pi,np.pi,n)
Y = np.sin(2*X)

plt.plot(X,Y+1,color='blue',alpha=1.00)
plt.plot(X,Y-1,color='blue',alpha=1.00)

plt.fill_between(X,1,1+Y,color='blue',alpha=.25)
plt.fill_between(X,-1,Y-1,where=Y-1>-1,color='blue',alpha=.25)
plt.fill_between(X,-1,Y-1,where=Y-1<-1,color='red',alpha=.25)
ax.set_xlim(-4,4),ax.set_xticks([])
ax.set_ylim(-4,4),ax.set_yticks([])

plt.show()