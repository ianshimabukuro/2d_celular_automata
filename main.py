import numpy as np
from grid_to_grid_function import grid2_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio

order = 100
percentage = 0.05
#Initialize the initial matrix
a= np.random.random(size=(order, order))
for i in range(1, a.shape[0]):
    for j in range(1, a.shape[1]):
        if a[i][j] < percentage:
            a[i][j] = 0
        else:
            a[i][j] = 1



# Set the border elements to 0
a[0, :] = 0  # First row
a[-1, :] = 0  # Last row
a[:, 0] = 0  # First column
a[:, -1] = 0  # Last column

for i in range(0,500):
    a = grid2_function(a)
    plt.clf()
    plt.imshow(a, cmap=plt.get_cmap('Paired'))
    plt.pause(0.1)

