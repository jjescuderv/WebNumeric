import numpy as np
import math

# Global variables declaration
A=b=n=m = None

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


def Lusimple(m,n,values_A,b_len,values_b):
    m,n,A,b = data_input(m,n,values_A,b_len,values_b)
    n = np.size(A,1)
    L=np.eye(n)
    U=np.zeros((n,n))
    M=A
    lis_stage=[]
    lis_m=[]
    list_L=[]
    list_U=[]
    #print("Stage 0")
    #print(M)
    lis_stage.append("Stage 0")
    lis_m.append(M)
    list_L.append(" ")
    list_U.append(" ")
    #print()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if M[j,i] != 0:
                L[j,i]=np.divide(M[j,i], M[i,i])
                M[j,i:n]= np.subtract(M[j,i:n], (np.divide(M[j,i], M[i,i]))*M[i,i:n])
        U[i,i:n]=M[i,i:n]
        U[i+1,i+1:n]=M[i+1,i+1:n]
        #print("Stage ", i+1)
        string = "Stage " + str(i+1)
        lis_stage.append(string)
        lis_m.append(M)
        list_L.append(L)
        list_U.append(U)
        #print(M)
        #print()
        #print("L: ", L)
        #print()
        #print("U: ", U)
        #print()
        
    MLB = np.concatenate((L, b), axis=1)
    
    z = prog_subst(MLB)
    
    MUZ = np.concatenate((U,z), axis=1)
    #print("Results: ")
    #print()
    #print(back_subst(MUZ))
    result = back_subst(MUZ)
    return lis_stage,lis_m,list_L,list_U,result
    
def data_input(m,n,values_A,b_len,values_b):
    #print("LU_SIMPLE")
    #global A, b, m, n

    # For A
    #print("MATRIX DATA (A)")
    m = int(m)
    n = int(n)
    # Check for square matrix
    if(m != n):
        #print("ERROR: Matrix must be square. \n")
        return
    #print("Enter the elements of the matrix (rowwise) separated by space: ")
    values_A = list(map(float, values_A.split()))
    A = np.array(values_A).reshape(m, n)

    # Check for nonsingular matrix
    det = np.linalg.det(A)
    if(det == 0):
        #print("det(A) = " + str(det))
        #print("ERROR: Matrix must be nonsingular. \n")
        return

    # For b
    #print("\nVECTOR DATA (b)")
    b_len = int(b_len)
    # Check for vector length
    if(b_len != m):
        #print("ERROR: b must have length n. \n")
        return
    #print("Enter the elements of the vector separated by space: ")
    values_b = list(map(float, values_b.split()))
    b = np.array(values_b).reshape(b_len, 1)
    return m,n,A,b
    
if __name__ == "__main__":
    np.set_printoptions(formatter={'float': '{: f}'.format})
    data_input()
    Lusimple()
            
            
    