import numpy as np
from grid_to_grid_function import grid2_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio

order = 50
#Initialize the initial matrix
a= np.random.randint(2,size=(order, order))

# Set the border elements to 0
a[0, :] = 0  # First row
a[-1, :] = 0  # Last row
a[:, 0] = 0  # First column
a[:, -1] = 0  # Last column

for i in range(0,500):
    a = grid2_function(a)
    plt.clf()
    plt.imshow(a, cmap=plt.get_cmap('Blues'))
    plt.pause(0.1)

print(a)
b = grid2_function(a)
print(b)