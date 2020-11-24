import numpy as np

def back_subst(M, n):
    x = np.ones([n, 1])
    
    for i in range(n-1, -1, -1):
        value = 0

        for j in range(i+1, n):
            value += M[i, j]*x[j]

        x[i] = (M[i,n]-value)/M[i,i]

    return x
