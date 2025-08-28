## FEL using plot_surface


import numpy as np

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

import random

from matplotlib import cm

from scipy.interpolate import griddata

from scipy.interpolate import Rbf

from numpy import linspace

#from matplotlib.ticker import LinearLocator, FormatStrFormatter

import matplotlib

from scipy import interpolate

import matplotlib.mlab as ml

fig = plt.figure(figsize=None, dpi=300, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None)

ax = fig.add_subplot(111)

### input file with x,y,z coordinates

x,y,z = np.loadtxt('gibbs12.txt').T 

X,Y = np.unique(x),np.unique(y)

xi = linspace(min(X),max(X),len(X))

yi = linspace(min(Y),max(Y),len(Y))

xi,yi = np.meshgrid(xi,yi)

X1, Y1 = np.meshgrid(X,Y)

print (len(x))

Z = griddata((x,y),z,(X1,Y1),method='cubic')

#surf = ax.plot_surface(X1, Y1, Z, rstride=1,cstride=1,alpha=1,cmap=cm.jet, linewidth=0.0, antialiased=3)

cset = ax.contourf(X1, Y1, Z, zdir='z', offset=-0, cmap=cm.jet, antialiased=3, vmin=0, vmax=18)

### put name of each axis. Cgange fontsize and lablesize accordingly

ax.set_xlabel('PC1',fontsize=12)

#ax.set_xlim(-6, 6)

ax.tick_params(axis="x", labelsize=6)

ax.set_ylabel('PC2',fontsize=12)

#ax.set_ylim(-6, 6)

ax.tick_params(axis="y", labelsize=6)

#ax.set_zlabel('Z axis', fontsize=12)

#ax.tick_params(axis="z", labelsize=6)

#ax.set_zlim(0.0, 12.0)

# Add a color bar which maps values to colors.

#fig.colorbar(surf, shrink=0.8, aspect=20)

#fig.colorbar(surf, shrink=0.5, aspect=20, extend='neither', ticks=[0, 2, 4, 6, 8, 10, 12])

plt.show()



