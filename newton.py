import sympy as sp
from sympy import sin, cos, log, exp


#itera = 100
#x0 = 0.5
#fun = log(sin(x)**2+1)-1/2
#dfun = 2*((sin(x)**2+1)**-1)*sin(x)*cos(x)
#tol = 10**-7

def Newton(itera, x0, fun, dfun, tol):
    x = sp.Symbol('x')

    #errors = []
    #errors.append(x0str)
    #errors.append("x0 is shitr")
    #return errors
   
    
    f = fun.subs(x, x0)
    df = dfun.subs(x, x0)
    
    c = 1
    a = x0-f/df
    e = (abs(a-x0))

    

    list_a = []
    list_f = []
    list_e = []

    
    list_a.append(format(x0, "12.10f"))
    list_f.append(format(f, "1.1e"))
    list_e.append(format(" "))


    

    while (e > tol and c <= itera):
        
        a = x0-(f/df)
        
        f = fun.subs(x, a)
       
        df = dfun.subs(x, a)
        
        e = (abs(a-x0))
        x0 = a
        
        c=c+1

        
        list_a.append(format(a, "12.10f"))
        
        if(f == 0):
            list_f.append(f)
        else:
            list_f.append(format(f, "1.1e"))
        
        list_e.append(format(e, "1.1e"))
    

    root=format(a, "12.15f")

    return list_a,list_f,list_e,root