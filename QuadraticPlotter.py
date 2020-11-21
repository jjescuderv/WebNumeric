import numpy as np

def QuadraticPlotter(n,x,y):
    
    #n = int(input("Enter the number of elements of x and y: "))
    n=int(n)
    # For x
    #print("\nVECTOR DATA (x)")
    x_len = n
    #print("Enter the elements of the vector separated by space: ")
    values_x = list(map(float, x.split()))
    X = np.array(values_x).reshape(x_len, 1)

    #print('x:\n',x)

    #For y
    #print("\nVECTOR DATA (y)")
    y_len = n
    #print("Enter the elements of the vector separated by space:")
    values_y = list(map(float, y.split()))
    Y = np.array(values_y).reshape(y_len, 1)

    #print('y:\n',y)

    m = 3*(n-1)
    A = np.zeros((m,m),float)
    b = np.zeros((m,1),float)
    coef = np.zeros((n-1,3),float)
    
    for i in range(1,n):
        z=list(range((3*i)-3,3*i))
        A[i,z]=[X[i]**2, X[i], 1]
        b[i]=Y[i]
    
    A[0,0:3]=[X[0]**2 ,X[0]**1, 1]
    b[0]=Y[0]
    
    for i  in range(2,n):
        z=list(range((3*i)-6,3*i))
        A[(n-1+i)-1,z] = [X[i-1]**2, X[i-1], 1, -X[i-1]**2, -X[i-1], -1]
        #b[(2*n-3+i)-1]=0
    
    for i in range(2,n):
        z=list(range((3*i)-6,3*i))
        A[(2*n-3+i)-1,z] = [2*X[i-1], 1, 0, -2*X[i-1], -1,0]
        #b[n+5+i]=0
        
    A[m-1,0]=2
    b[m-1]=0
    S = np.linalg.solve(A, b)

    print('Tracer coefficients:\n', S,'\n')
    
    return A,b,S    


if __name__ == "__main__":
    QuadraticPlotter(4,'-1 0 3 4','15.5 3 8 1')