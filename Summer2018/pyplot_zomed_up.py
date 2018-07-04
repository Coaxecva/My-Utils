#!/usr/bin/env python
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def my_dist(x):
    return np.exp(-x ** 2)

overview_data_x = np.arange(-100, 100)
overview_data_y = my_dist(x)

fig, ax = plt.subplots() # create a new figure with a default 111 subplot
ax.plot(overview_data_x, overview_data_y)

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
axins = zoomed_inset_axes(ax, 2.5, loc=2) # zoom-factor: 2.5, location: upper-left

axins.plot(overview_data_x, overview_data_y)

x1, x2, y1, y2 = -10, 10, 0.9, 1.0 # specify the limits
axins.set_xlim(x1, x2) # apply the x-limits
axins.set_ylim(y1, y2) # apply the y-limits

plt.yticks(visible=False)
plt.xticks(visible=False)
axins.xaxis.set_visible('False')
axins.yaxis.set_visible('False')

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
plt.show()
