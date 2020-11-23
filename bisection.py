import sympy as sp
from sympy import sin, cos, log, exp

#itera = 100                        int
#a = 0                              float
#b = 1                              float
#fstr = log(sin(x)**2+1)-1/2        sympyfy
#tolstr = 10**-7                    sympyfy



def Bisection(itera, a, b, f, tol):
    x = sp.Symbol('x')

    xmi = (a+b)/2
    fxm = f.subs(x, xmi)
    e = abs(xmi-a)
    c = 1
    
    list_a = []
    list_xm = []
    list_b = []
    list_fxm = []
    list_E = []

    list_a.append(format(a, "12.10f"))
    list_xm.append(format(xmi, "12.10f"))
    list_b.append(format(b, "12.10f"))
    list_fxm.append(format(fxm, "1.1e"))
    list_E.append(" ")
    

    while (e >= tol and c <= itera):
        xmi = (a+b)/2
        fai = f.subs(x, a)
        fbi = f.subs(x, b)
        fxm = f.subs(x, xmi)
        e = abs(xmi-a)
        if c > 1:
            list_a.append(format(a, "12.10f"))
            list_xm.append(format(xmi, "12.10f"))
            list_b.append(format(b, "12.10f"))
            list_fxm.append(format(fxm, "1.1e"))
            list_E.append(format(e, "1.1e"))

        if fai == 0:
            root=format(a, "12.15f")
            return  list_a, list_xm, list_b, list_fxm, list_E, root

        elif fbi == 0:
            root=format(b, "12.15f")
            return  list_a, list_xm, list_b, list_fxm, list_E, root

        if fai*fxm < 0:
            a = a
            b = xmi
            e = abs(xmi-a)
        else:
            a = xmi
            b = b
            e = abs(xmi-b)
        c = c+1


    root=format(xmi, "12.15f")

    return  list_a, list_xm, list_b, list_fxm, list_E, root