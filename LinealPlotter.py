import numpy as np

def LinealPlotter():
    n = int(input("Enter the number of elements of x and y: "))
    
    # For x
    print("\nVECTOR DATA (x)")
    x_len = n
    print("Enter the elements of the vector separated by space: ")
    values_x = list(map(float, input().split()))
    x = np.array(values_x).reshape(x_len, 1)

    #print('x:\n',x)

    #For y
    print("\nVECTOR DATA (y)")
    y_len = n
    print("Enter the elements of the vector separated by space:")
    values_y = list(map(float, input().split()))
    y = np.array(values_y).reshape(y_len, 1)

    #print('y:\n',y)


    n-=1
    A= np.zeros((n*2, n*2), float)
    b=np.zeros((n*2,1),float)
    pos=1

    m=[0,1]

    A[0,m]=[x[0], 1]
    b[0]=y[0]

    i=0
    #[2*i-1, 2*i]
    while i<n:  #interpolation condition 
        A[i+1,[2*(i+1)-1, 2*i]]=[1, x[i+1]]
        b[i+1]=y[i+1]
        i+=1    
    
    i=1
    int(n)
    while i<n:  #continuity condition 
        z=list(reversed(range(2*(i+1)-4,(2*(i+1)))))
        A[ n+i , z]  = [-1, -(x[i]), 1, (x[i])]
        #b[(n)+(i)]=0
        i+=1

    print('A:\n',A)
    print('B:\n',b)

    S = np.linalg.solve(A, b)

    print('Tracer coefficients: \n', S)

if __name__ == "__main__":
    LinealPlotter()