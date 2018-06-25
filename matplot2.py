# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:18:08 2016

@author: matlab1.com
"""
import numpy as np
import matplotlib.pyplot as plt

n =8

x = np.arange(n)

y = np.abs((1-x)*5*np.random.rand())

plt.bar(x,y)