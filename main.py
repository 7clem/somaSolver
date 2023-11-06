

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np

import piece as p
import ops

x, y, z = np.indices((3, 3, 3))

p1 = p.list2boolmatrix(p.ell)
p2 = ops.apply('incX', p.tee)
print(p2)
p2 = p.list2boolmatrix( ops.apply('incX', p.tee))
#print(f'p1 = {p1}')
print(f'p2 = {p2}')

# combine the objects into a single boolean array
voxelarray = p1 | p2

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[p1] = 'red'
colors[p2] = 'green'

# print(colors)

#  and plot everything
ax = plt.figure().add_subplot(projection='3d')
print(f'colors = {colors}')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')  # edgecolor='k')

plt.show()
