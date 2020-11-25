import numpy as np
import math

def prog_subst(M):  #L,b = z
    n = len(M)
    x = np.zeros([n,1])
    
    x[0] = M[0,n]/M[0,0]
    array=[[1]]
    for i in range(1,n):
        aux=np.concatenate((array, np.transpose(x[0:i])), axis=1)
        arrayaux = [M[i-1,n]]
        
        aux1 = np.concatenate((arrayaux, -M[i,0:i]), axis=0)
        
        x[i] = np.dot(aux,aux1)/M[i,i]
        
    return x

def back_subst(M): #U,z = x
    n = len(M)
    x = np.ones([n, 1])
    

    for i in range(n-1, -1, -1):
        value = 0

        for j in range(i+1, n):
            value += M[i, j]*x[j]

        x[i] = (M[i,n]-value)/M[i,i]

    return x

def lu_simple(n, mat, vec):
    iteration = []
    errors = []
    matrices = []

    values_A = list(map(float, mat))
    A = np.array(values_A).reshape(n, n)

    det = np.linalg.det(A)
    if(det == 0):
        errors.append(A)
        errors.append("The matrix must be non singular")
        return errors

    values_b = list(map(float, vec))
    b = np.array(values_b).reshape(n, 1)

    M = A
    iteration.append(np.copy(M))
    matrices.append(np.copy(iteration))
    L = np.eye(n)
    U = np.zeros((n,n))
    iteration = []

    for i in range(0,n-1):
        for j in range(i+1,n):
            if M[j,i] != 0:
                L[j,i]=np.divide(M[j,i], M[i,i])
                M[j,i:n]= np.subtract(M[j,i:n], (np.divide(M[j,i], M[i,i]))*M[i,i:n])

        U[i,i:n]=M[i,i:n]
        U[i+1,i+1:n]=M[i+1,i+1:n]
        
        iteration.append(np.copy(M))
        iteration.append(np.copy(L))
        iteration.append(np.copy(U))
        matrices.append(np.copy(iteration))
        iteration = []
        
    MLB = np.concatenate((L, b), axis=1)
    z = prog_subst(MLB)
    MUZ = np.concatenate((U,z), axis=1)
    x = back_subst(MUZ)

    ans = [x, matrices, n]
    return ans
    
            
            
    