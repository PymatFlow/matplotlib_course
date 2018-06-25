# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:29:00 2016

@author: matlab1.com
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-4,4,0.25)

y = np.arange(-4,4,0.25)

X,Y = np.meshgrid(x,y)

R = np.sqrt(X**2+Y**2)

Z = np.sin(R)

fig = plt.figure()
ax =Axes3D(fig)

ax.plot_surface(X,Y,Z)

