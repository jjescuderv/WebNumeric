#https://docs.sympy.org/latest/install.html
from sympy import *
import pandas as pd
    
def Multiple_roots(iter,x0,x1,f,error):
    #print("Multiple roots")
    iter=float(iter)
    x0=float(x0)
    x1=float(x1)
    x=Symbol('x')
    f=f
    error=float(eval(error))
    #iter=float(input("Enter the maximum number of iterations: "))
    #x0=float(input("Enter an initial approximation: "))
    #x=Symbol('x')
    #f=input("Enter the function to evaluate: ")
    fp=str(diff(f,x))
    #print('fp: ',fp)
    fpp=str(diff(fp,x))
    #print('fpp: ',fpp)
    #error=float(eval(input("Enter the maximum absolute error accepted: ")))

    x=x0
    f0=float(eval(f))
    #print(f0)
    f1=float(eval(fp))
    #print(f1)
    f2=float(eval(fpp))
    #print(f2)

    g=x0-((f0*f1)/((f1**2)-(f0*f2)))
    #print('g', g)

    e=1.0
    g2=0.0
    c=2.0 


    lis_x0=[x0]
    lis_f0=[f0]
    lis_f1=[f1]
    lis_f2=[f2]
    lis_er=['']
    d = {'Xn':lis_x0,'f':lis_f0,'fp':lis_f1,'fpp':lis_f2,'E':lis_er}

    x=g
    f0=float(eval(f))
    f1=float(eval(fp))
    f2=float(eval(fpp))
    e=abs(x0-g)
    lis_x0.append(x)
    lis_f0.append(f0)
    lis_f1.append(f1)
    lis_f2.append(f2)
    lis_er.append(e)

    while e>=error and c<=iter:
        x=g
        f0=eval(f)
        f1=eval(fp)
        f2=eval(fpp)
        g2=g
        g=g2-((f0*f1)/((f1**2)-(f0*f2)))
        e=abs(g-g2)
        c=c+1.0
        lis_x0.append(g)
        lis_f0.append(f0)
        lis_f1.append(f1)
        lis_f2.append(f2)
        lis_er.append(e)

    data_frame = pd.DataFrame(data=d)
    #print(data_frame)
    #print('Iterations: ', int(c))
    #print('With an error of: ', e)
    #print('There is a root in: ', g)

    return  lis_x0, lis_f0, lis_f1, lis_f2, lis_er, str(e), str(g)

Multiple_roots(100,1.0,1.5,'ln(x**2+1)',('10**-7'))