import numpy as np
import numpy.random


def grid2_function(x):

    for i in range(1,x.shape[0]-1):
        for j in range(1,x.shape[1]-1):

            #Specify the rule
            n_n = 0
            if x[i+1][j] == 1:
                n_n+=1
            if x[i-1][j] == 1:
                n_n+=1
            if x[i][j+1] == 1:
                n_n+=1
            if x[i][j-1] == 1:
                n_n+=1
            if x[i + 1][j+ 1] == 1:
                n_n += 1
            if x[i - 1][j + 1] == 1:
                n_n += 1
            if x[i + 1][j - 1] == 1:
                n_n += 1
            if x[i - 1][j - 1] == 1:
                n_n += 1

            if n_n<2 and x[i][j] == 1:
                x[i][j]=0
            elif (n_n==2 or n_n==3) and x[i][j] == 1:
                x[i][j]=1
            elif n_n>3 and x[i][j] == 1:
                x[i][j]=0
            elif n_n == 3 and x[i][j] == 0:
                x[i][j] = 1
            else:
                x[i][j] = 0



    return x

