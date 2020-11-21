from sympy import *
import pandas as pd

def Secant(iter,x0,x1,f,error):
    #print("Secant")
    iter=float(iter)
    x0=float(x0)
    x1=float(x1)
    x=Symbol('x')
    f=f
    error=float(eval(error))
    """
    iter=float(input("Enter the maximum number of iterations: "))
    x0=float(input("Enter an initial approximation: "))
    x1=float(input("Enter the second initial approximation: "))"""
    """
    f=input("Enter the function to evaluate: ")
    error=float(eval(input("Enter the maximum absolute error accepted: ")))
    #f0 """
    x=x0
    f0=eval(f)
    float(f0)

    #f1
    x=x1
    f1=eval(f)
    float(f1)

    #xa
    #print('x1: ',x1)
    #print('x0: ',x0)
    #print('f1: ',f1)
    #print('f0: ',f0)
    xa=x1-((f1*(x1-x0))/(f1-f0))

    #error and iterations
    e=float(abs(xa-x1))
    ##print(e)
    c=2.0

    x=xa
    ft=eval(f)

    lis_xi=[x0,x1,xa]
    lis_fx=[f0,f1,ft]
    lis_er=['','',e]
    d = {'Xi':lis_xi,'f(Xi)':lis_fx,'E':lis_er}

    while e>=error and c<=iter:  
        x0=x1
        x1=xa

        x=x0
        f0=eval(f)
    
        x=x1
        f1=eval(f)
        xa=x1-((f1*(x1-x0))/(f1-f0))
        
        e=abs(xa-x1)
        c+=1.0

        x=xa
        ft=eval(f)
        lis_xi.append(x)
        lis_fx.append(ft)
        lis_er.append(e)

    data_frame = pd.DataFrame(data=d)
    #print(data_frame)
    #print('With an error of: ', e)
    #print('There is a root in: ', xa)
    return lis_xi,lis_fx,lis_er,str(e),str(xa)


#Secant(100,1.0,1.5,'ln(x**2+1)',(10**-7))