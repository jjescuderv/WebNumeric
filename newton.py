import sympy as sp
from sympy import sin, cos, log, exp


#itera = 100
#x0 = 0.5
#fun = log(sin(x)**2+1)-1/2
#dfun = 2*((sin(x)**2+1)**-1)*sin(x)*cos(x)
#tol = 10**-7

def Newton(iterastr, x0str, fstr, dfstr, tolstr):
    x = sp.Symbol('x')
    error = False
    
    itera = int(iterastr)
    x0 = float(x0str)
    fun = sp.sympify(fstr)
    dfun = sp.sympify(dfstr)
    tol = sp.sympify(tolstr)
    
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
        list_f.append(format(f, "1.1e"))
        list_e.append(format(e, "1.1e"))


    root=format(a, "12.15f")

    return list_a,list_f,list_e,root