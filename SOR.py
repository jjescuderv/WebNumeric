#ITERATIVE GAUSS SEIDEL METHOD WITH RELAXATION#
import numpy as np
import pandas as pd
import math

A=b=m=n = None
def Sor():
    global A, b, m, n

    # For A
    print("MATRIX DATA (A)")
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    # Check for square matrix
    if(m != n):
        print("ERROR: Matrix must be square. \n")
        return
    print("Enter the elements of the matrix (rowwise) separated by space: ")
    values_A = list(map(float, input().split()))
    A = np.array(values_A).reshape(m, n)

    # Check for nonsingular matrix
    det = np.linalg.det(A)
    if(det == 0):
        print("det(A) = " + str(det))
        print("ERROR: Matrix must be nonsingular. \n")
        return

    # For b
    print("\nVECTOR DATA (b)")
    b_len = n#int(input("Enter the length of b: "))
    # Check for vector length
    if(b_len != m):
        print("ERROR: b must have length n. \n")
        return
    print("Enter the elements of the vector separated by space: ")
    values_b = list(map(float, input().split()))
    b = np.array(values_b).reshape(b_len, 1)

    #For x0
    print("\nVECTOR DATA (X0)")
    x0_len = n#int(input("Enter the length of x0: "))
    # Check for vector length
    if(x0_len != m):
        print("ERROR: X0 must have length n. \n")
        return
    print("Enter the elements of the vector separated by space: ")
    values_x0 = list(map(float, input().split()))
    x0 = np.array(values_x0).reshape(x0_len, 1)

    iter=float(input("Enter the maximum number of iterations: "))
    error=float(eval(input("Enter the maximum absolute error accepted: ")))
    w=float(input("Enter the lambda of relaxation: "))

    #print(A)
    #print(b)
    #print(x0)
    #print(iter)
    #print(error)
    #print(w)

    k= np.linalg.norm(A)* np.linalg.norm(np.linalg.inv(A))

    print('Conditional: ', k)

    d= np.zeros((m, n), float)
    np.fill_diagonal(d,(A.diagonal()))

    #print('d: \n',d)

   
    l= d-(np.tril(A,0))
    print(l)
   
    u= d-(np.triu(A,0))
    #print(u)

    print('\n SOLUTION:\n');
    print('\nThe gaussian transition matrix seidel:\n');
    Tw=(np.linalg.inv((d-(w*l)))).dot(((1-w)*d+(w*u)))
    print(Tw)

    #re=max(np.absolute(np.linalg.eig(Tw)))
    valores, vectores = np.linalg.eig(Tw)
    print(valores)
    z=np.absolute(valores)
    y=max(z)
    re=y
    print('re:', re)

    if re>1:
        print('Spectral radius greater than 1\n The method does not converge')
        exit()

    print('\nThe constant vector is:\n')
    y= np.linalg.inv(d-(w*l))
    #print('y: \n',y)
    #print(b)
    Cw= w*(y.dot(b))
    #print('\n')
    print(Cw)

    i=0
    err=error+1;
    x1=[x0.item(0)]
    x2=[x0.item(1)]
    x3=[x0.item(2)]
    er=[err]

    d = {'X1':x1,'x2':x2,'x3':x3,'Error':er}
    while err>error and i<iter:
        xi=(Tw.dot(x0))+Cw
        err = math.sqrt( ((xi.item(0)-x0.item(0))**2)+((xi.item(1)-x0.item(1))**2)+((xi.item(2)-x0.item(2))**2) )
        x0=xi
        i=i+1
        x1.append(x0.item(0))
        x2.append(x0.item(1))
        x3.append(x0.item(2))
        er.append(err)

    data_frame = pd.DataFrame(data=d)
    pd.set_option('precision', 15)
    print(data_frame)

if __name__ == "__main__":
    Sor()