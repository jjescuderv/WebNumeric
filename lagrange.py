import numpy as np 

def Lagrange(n, values_x, values_y):
    n = int(n)
    L = np.zeros([n,n])

    X = list(map(float, values_x.split()))
    Y = list(map(float, values_y.split()))
    
    for i in range(0,n):
        aux0 = np.setdiff1d(X, X[i])
        aux = [1, aux0[0]*(-1)]
        for j in range(1,n-1):
            aux = np.convolve(aux, [1, aux0[j]*(-1)])
        L[i,:] = aux/np.polyval(aux, X[i])
    
    poly = []
    for i in range(0,len(Y)):
        poly.append("+"+str(Y[i])+"*L"+str(i))

    coef = Y

    for i in range(n-1,-1,-1):
        print('   x^' + str(i) + '    ', end='')
    print()
    print(L,"\n")
    print(coef,"\n")
    print(poly,"\n")

    strpoly = ""

    for i in range (0, len(poly)):
        strpoly += poly[i]

    return str(L), str(coef), strpoly

np.set_printoptions(formatter={'float': '{: f}'.format})
