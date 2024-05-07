import numpy as np
import numpy.random


def grid2_function(x):

    iteration = np.array([])
    rule = np.array([0,0,0,1,0,1,0,0])
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i+1][j] == 1:
                x[i][j]=1
    print(x.shape)
    return x

a= numpy.random.randint(2,size=(5, 5))
# Set the border elements to 0
a[0, :] = 0  # First row
a[-1, :] = 0  # Last row
a[:, 0] = 0  # First column
a[:, -1] = 0  # Last column
print(a)
b = grid2_function(a)
print(b)