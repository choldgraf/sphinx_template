"""
==================
The trapezoid rule
==================

This demonstrates how the trapezoid rule can be used to determine
the area under the curve for an arbitrary function.

For more information about this, `see here <http://www.mathwords.com/t/trapezoid_rule.htm>`_

"""

import os.path as op
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from my_package.trapezoid import trapzf


def my_function(a):
    return 2.2 * a**3 + .3 * a**2 + 2 * a + .1

# Show the function
fig, ax = plt.subplots()
a = np.linspace(-5, 5, 1000)
b = my_function(a)
ax.scatter(a, b)
ax.set_title('Inputs / Outputs')

# Calculate area under the curve
n_points_list = np.logspace(np.log10(5), np.log10(20), 100)
areas = []
for n_points in n_points_list:
    areas.append(trapzf(my_function, -5, 5, n_points))

# We'll add some size and color, just to make it pretty
fig, ax = plt.subplots()
ax.scatter(n_points_list, areas,
           s=areas, c=areas, cmap=plt.cm.viridis)
ax.set_title('Area over n_points')
plt.tight_layout()
plt.show()
