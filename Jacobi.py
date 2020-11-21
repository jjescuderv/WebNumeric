import numpy as np
import sympy as sm
import math


# Global variables declaration
A = b = x0 = tol = Nmax = None


def jacobi():
    global x0
    
    D=np.diag(np.diag(A))
    L=-np.tril(A,-1)
    U=-np.triu(A,1)
    print("Results", '\n')
    print("T:", '\n')
    T=  np.linalg.matrix_power(D,-1)*(np.matrix(L)+np.matrix(U))
    print(T)
    print()
    print("C: ", '\n')
    C=np.linalg.matrix_power(D,-1)*b
    C=Diagonal(C)
    print(C, '\n')
    
    respec,mat=(np.linalg.eig(T))
    respect1 = np.amax(np.abs(respec))
    print("spectral radius: ", respect1, '\n')
    E = 1000
    cont = 0

    print('iter', '\t', "E ",'\t','\n')
    print(cont,'\t', 0, '\t', printRow(x0) )
    while E > tol and cont < Nmax:
        
        xinic = T*np.matrix(x0)+np.matrix(C)
        #print(xinic)
        E = np.linalg.norm(xinic-x0,2)
        x0 = xinic
        cont = cont+1
        print(cont,'\t', E, '\t', printRow(x0) )


def printRow(ar):
    row = ""
    a = ar.shape[0]
    for i in range(0,a):
        row += str(ar[i][0]) + " "
    return row
        

def data_input():
    print("Jacobi")
    global A, b, x0 , tol , Nmax

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
    b_len = int(input("Enter the length of b: "))
    # Check for vector length
    if(b_len != m):
        print("ERROR: b must have length n. \n")
        return
    print("Enter the elements of the vector separated by space: ")
    values_b = list(map(float, input().split()))
    b = np.array(values_b).reshape(b_len, 1)
    
    x0_len = int(input("Enter the length of x0: "))
    if(x0_len != m):
        print("ERROR: x0 must have length n. \n")
        return
    print("Enter the elements of the vector separated by space: ")
    values_x0 = list(map(float, input().split()))
    x0 = np.array(values_x0).reshape(x0_len, 1)
    
    tol = sm.sympify(input("Enter the maximum tolerance "))
    
    Nmax = int(input("Enter the maximum iteration "))

def Diagonal(m):
    ar = []
    a = np.size(m,1)
    for i in range(0,np.size(m,1)):
        ar.append(m[i][i])
    arr = np.array(ar).reshape(a, 1)
    return arr
        
    
if __name__ == "__main__":
    np.set_printoptions(formatter={'float': '{: f}'.format})
    data_input()
    jacobi()