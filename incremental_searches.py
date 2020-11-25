import sympy as sp
from sympy import sin, cos, log, exp

#itera = 100                    int
#x0 = -3                        float
#delta= 0.5                     float
#fun = log(sin(x)**2+1)-1/2     symp

def Incremental_searches(itera, x0, delta, f):

    x = sp.Symbol('x')
  
    fun = f
    x1 = x0+delta
  
    c = 1 

    list_apr = []
    straux = ""

    while c <= itera:
        f1 = fun.subs(x, x0)
        f2 = fun.subs(x, x1)
        if f1 == 0:
            straux = "There is a root of f in: " + x0
            list_apr.append(straux)
        elif f2 == 8:
            straux = "There is a root of f in: " + x1
            list_apr.append(straux)
        elif f1*f2 < 0:
            straux = "There is a root of f in: " + "[ " + format(x0, "12.10f") + " , " + format(x1, "12.10f") + " ]"
            list_apr.append(straux)

        x0 = x1
        x1 = x1+delta
        c = c+1

    return list_apr