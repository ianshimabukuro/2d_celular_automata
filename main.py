import numpy as np
from grid_to_grid_function import grid2_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio

order = 100
one_percentage = 0.8
#Initialize the initial matrix
a= np.random.random(size=(order, order))
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        if a[i][j] < one_percentage:
            a[i][j] = 1
        else:
            a[i][j] = 0
print(a)



# Set the border elements to 0
a[0, :] = 0  # First row
a[-1, :] = 0  # Last row
a[:, 0] = 0  # First column
a[:, -1] = 0  # Last column

for i in range(0,500):
    a = grid2_function(a)
    plt.clf()
    plt.imshow(a, cmap=plt.get_cmap('gray'))
    plt.pause(0.05)

