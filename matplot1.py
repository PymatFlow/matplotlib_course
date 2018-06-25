# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:19:56 2016

@author: matlab1.com
"""

# matplotlib
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,256)

S = np.sin(x)
C = np.cos(x)

plt.figure(figsize=(8,6),dpi=80)


sin_plot,=plt.plot(x,S,color="blue",linewidth=3,linestyle="-")


cos_plot,=plt.plot(x,C,color="green",linewidth=3,linestyle="--")

plt.xlim(-4,4)
plt.ylim(-1,1)

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])

plt.legend([sin_plot,cos_plot],['sin','output'])

plt.show()