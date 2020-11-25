import numpy as np 
import sympy as sp


def Newton_diff(n, values_x, values_y):

    X = list(map(float, values_x.split()))
    Y = list(map(float, values_y.split()))

    x = sp.Symbol('x')
    n = len(X)
    D = np.zeros((n,n))
    coef = []
    poly = []
    for i in range(0,len(X)):
        for j in range(i+1,len(X)):
            if(X[i]==X[j]):
                return "", "", "", "X vector contain repeated values, the method will not run"
    
    D[:,0] = np.transpose(Y)
    for i in range(2,n+1):
        aux0 = D[i-2:n,i-2]
        aux = np.diff(aux0)
        aux2 = np.subtract(X[i-1:n], X[0:n-i+1])
        D[i-1:n,i-1]=aux/np.transpose(aux2)
    

    coef = np.diag(np.transpose(D))
   

    listmult = []
    
    for i in range(0, len(X)):
        if i==0:
            straux = "(x-("+str(X[i])+"))"
            listmult.append(straux)
 
        if i>=1:
            straux += "*(x-("+str(X[i])+"))"
            listmult.append(straux)

    poly.append(str(coef[0]))
    for i in range(1,len(coef)):
        poly.append(str(coef[i])+"*"+listmult[i-1])

    return str(D), str(coef), str(poly), ""
