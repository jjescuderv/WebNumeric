import numpy as np

def lu_partial_pivoting(n, mat, vec):
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
    L = np.identity(n)
    P = np.identity(n)
    U = np.zeros((n, n))
    iteration = []

    for i in range(0, n-1):
        col = M[i+1:n, i]
        grpos = np.argmax(np.absolute(col))
        gr = abs(col[grpos])

        if gr>abs(M[i,i]):
            auxM = np.copy(M[grpos+i+1, i:n])
            auxP = np.copy(P[grpos+i+1, :])
            M[grpos+i+1, i:n] = M[i, i:n]
            P[grpos+i+1, :] = P[i, :]
            M[i, i:n+1] = auxM
            P[i, :] = auxP
            if i>0:
                auxL = np.copy(L[grpos+i+1, 0:i])
                print(auxL)
                L[grpos+i+1, 0:i] = L[i, 0:i]
                L[i, 0:i] = auxL

        for j in range(i+1, n):
            if M[j,i]!=0:
                L[j,i] =np.divide(M[j,i], M[i,i])
                M[j,i:n+1] = np.subtract(M[j,i:n+1], np.divide(M[j,i], M[i,i])*M[i,i:n+1])

        U[i,i:n] = M[i,i:n]
        U[i+1,i+1:n] = M[i+1,i+1:n]

        iteration.append(np.copy(M))
        iteration.append(np.copy(L))
        iteration.append(np.copy(U))
        iteration.append(np.copy(P))
        matrices.append(np.copy(iteration))
        iteration = [] 

    U[n-1,n-1] = M[n-1,n-1]
    Pb = np.dot(P, b)
    z = prog_subst(np.concatenate((L, Pb), axis=1))
    x = back_subst(np.concatenate((U, z), axis=1))
    
    ans = [x, matrices, n]
    return ans

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
