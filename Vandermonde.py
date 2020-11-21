import numpy as np
import pandas as pd
import math
from polynomial import Polynomial as P

def Vandermonde(n,values_x,values_y):
    n=int(n)
    # n = int(input("Enter the number of elements of x and y: "))
    
    # For x
    #print("\nVECTOR DATA (x)")
    x_len = n
    #print("Enter the elements of the vector separated by space: ")
    values_x = list(map(float, values_x.split()))
    #values_x=values_x
    #x = np.array(values_x).reshape(x_len, 1)
    x= values_x

    #print('x:\n',x)

    #For y
    #print("\nVECTOR DATA (y)")
    y_len = n
    #print("Enter the elements of the vector separated by space:")
    #values_y = list(map(float, input().split()))
    values_y = list(map(float, values_y.split()))
    y = values_y
    #y = np.array(values_y).reshape(y_len, 1)

    #print('y:\n',y)

    A= np.zeros((n, n), float)
    i=0
    j=0
    while i < n: 
        while j < n: 
            A[i,j]=(x[i])**(n-(j+1))
            j+=1
        i+=1
        j=0
    
    #print('Vandermonde matrix: \n',A)

    b = np.linalg.solve(A, y)

    #print('\nPolynomial coefficients: \n',b)

    a = P(b)
    str(a)
    #print('Polynomial: ',a)

    return str(A),str(b),str(a)

if __name__ == "__main__":
    Vandermonde()