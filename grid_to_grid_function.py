import numpy as np
import numpy.random


def grid2_function(x):

    iteration = np.array([])
    rule = np.array([0,0,0,1,0,1,0,0])
    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):
            if x[i+1][j] == 1 and x[i-1][j] == 0:
                x[i][j]=1
            else:
                x[i][j] = 0

    return x

