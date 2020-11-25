import numpy as np

# Global variables declaration


#A = 4 -1 0 3 1 15.5 3 8 0 -1.3 -4 1.1 14 5 -2 30
#b = 1 1 1 1

def Crout(n, mat, vec):
    errors = []
    #Initialization
 
    matrices = []
    iteration = []
    
    values_A = list(map(float, mat))
    A = np.array(values_A).reshape(n, n)

    det = np.linalg.det(A)
    if(det == 0):
        errors.append(A)
        errors.append("The matrix must be non singular")
        return errors

    
    values_b = list(map(float, vec))
    b = np.array(values_b).reshape(n, 1)

    iteration.append(np.copy(A))
    matrices.append(np.copy(iteration))
    
    L = np.eye(n) #Identity matrix
    U = np.eye(n)
    iteration = []

    #Factorization
    for i in range(0,n-1):#Cycle for stages
        for j in range(i,n):#Cycle for L construction
            L[j,i]=A[j,i]-(np.dot(L[j,0:i],np.transpose(U[0:i,i])))

        iteration.append(np.copy(A))
        iteration.append(np.copy(L))

        for j in range(i+1,n):#Cycle for U construction
            if(L[i,i] == 0):
                return 0
            U[i,j] = (A[i,j] - (np.dot(L[i,0:i],np.transpose(U[0:i,j]))))/L[i,i] #Division by the element of the diagonal of the stage
        
        iteration.append(np.copy(U))
        matrices.append(np.copy(iteration))
        iteration = []

    L[n-1,n-1]=A[n-1,n-1]-np.dot(L[n-1,0:n-1],np.transpose(U[0:n-1,n-1])) #Lonely stage
    
    iteration.append(np.copy(A))
    iteration.append(np.copy(L))
    iteration.append(np.copy(U))
    matrices.append(np.copy(iteration))

    MLB = np.concatenate((L, b), axis=1)
    z = prog_subst(MLB)
    MUZ = np.concatenate((U,z), axis=1)
    x = back_subst(MUZ)

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



