

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np

import ops
import piece as p


# p1 = p.list2boolmatrix(p.ell)
p1 = p.list2boolmatrix(ops.apply(p.tee, 'rXr'))
#p2 = p.list2boolmatrix(ops.apply(p.tee, 'incX'))
print(f'p1 = {p1}')
#print(f'p2 = {p2}')

# combine the objects into a single boolean array
voxelarray = p1  #| p2

# set the colors of each object
colors = np.empty(voxelarray.shape, dtype=object)
colors[p1] = 'blue'
# colors[p2] = 'green'

print(colors)

#  and plot everything
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxelarray, facecolors=colors, edgecolor='k')

plt.show()
