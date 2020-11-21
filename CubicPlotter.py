import numpy as np

def CubicPlotter(n,x,y):
    n = int(n)
    
    # For x
    print("\nVECTOR DATA (x)")
    x_len = n
    print("Enter the elements of the vector separated by space: ")
    values_x = list(map(float, x.split()))
    x = np.array(values_x).reshape(x_len, 1)

    #print('x:\n',x)

    #For y
    print("\nVECTOR DATA (y)")
    y_len = n
    print("Enter the elements of the vector separated by space:")
    values_y = list(map(float, y.split()))
    y = np.array(values_y).reshape(y_len, 1)

    #print('y:\n',y)


    n-=1
    M= np.zeros((n*4, n*4), float)
    b=np.zeros((n*4,1),float)
    m=[]
    i=0
    while i<4:
        m.append(i)
        i+=1
    
    #print(m)
    M[0,m]=[((x[0])**3), ((x[0])**2),  x[0], 1]
    b[0]=y[0]

    i=1
    while i<=n: #interpolation
        M[i,[(4*i-3)-1, (4*i-2)-1, (4*i-1)-1, (4*i)-1] ]= [((x[i])**3), ((x[i])**2), x[i], 1]
        b[i]=y[i]
        i+=1

    i=2
    while i<=n: #continuity 
        z=list(range((4*i)-8,4*i))
        M[n+(i-1), z ]= [((x[i-1])**3), ((x[i-1])**2), x[i-1], 1, -((x[i-1])**3), -((x[i-1])**2), -x[i-1], -1]
        #b[n+i]=0
        i+=1

    i=2
    while i<=n:  #smoothness 
        z=list(range((4*i)-8,4*i))
        M[ (n+(n-1)+i)-1 , z ]=[(3*(x[i-1]**2)), (2*x[i-1]), 1, 0, -(3*(x[i-1]**2)), -(2*x[i-1]), -1, 0]
        #b[n+(n-1)+i]=0;
        i+=1

    
    i=2
    while i<=n: #Concavity
        z=list(range((4*i)-8,4*i))  
        M[ (3*n+(i-2))-1 , z ]=[(6*x[i-1]), 2, 0, 0, -(6*x[i-1]), -2, 0, 0]
        #b[3*n]=0;
        i+=1
    
    M[((4*n)-1)-1,0]=6*x[0] 
    M[((4*n)-1)-1,1]=2
    #b[(4*n)-1]=0
    
    M[(4*n)-1,((4*n)-3)-1]=6*x[n+1-1]  
    M[(4*n)-1,((4*n)-2)-1]=2
    #b[4*n]=0 #border condition

    print('\n M:\n',M)
    print('\n b:\n',b)

    S = np.linalg.solve(M, b)

    print('Tracer coefficients:\n', S)
    
    return M,b,S

if __name__ == "__main__":
    CubicPlotter()