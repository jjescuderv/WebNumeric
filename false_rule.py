import sympy as sm
import math
def reglaFalsa(limite_iteraciones, a, b, funcion,tolerancia):
    x = sm.symbols('x')
    funcion = sm.sympify(funcion)
    fa = float(funcion.subs(x, a))
    fb = float(funcion.subs(x, b))
    a=float(a)
    b=float(b)
    tolerancia=float(eval(tolerancia))
    limite_iteraciones = float(limite_iteraciones)
    string = ""
    if(fa == 0):
        print('a es raiz')
    elif(fb == 0):
        print('b es raiz')
    elif(fa * fb < 0):
        error = 1
        cont = 1
        c = (fb*a - fa*b)/(fb - fa)
        fc = funcion.subs(x, c)
        while(fc != 0 and cont < limite_iteraciones and error > tolerancia):
            if (fa * fc < 0):
                b = c
                fb = funcion.subs(x, c)
            else:
                a = c
                fa = funcion.subs(x, c)
            caux = c    
            c = (fb*a - fa*b)/(fb - fa)
            fc = funcion.subs(x, c)
            error = abs(caux - c)
            cont+=1
        if (fc == 0):
            print('c es una raiz '+ str(c))
            string = 'c es una raiz '+ str(c)
        elif (error < tolerancia):
            print('c es una aproximacion de la raiz c: '+ str(c) +' error: '+ str(error)+ ' en la iteracion '+str(cont))
            string = 'c es una aproximacion de la raiz c: '+ str(c) +' error: '+ str(error)+ ' en la iteracion '+str(cont)
        else:
            print('numero de iteraciones maximas alcanzado, no se alcanzo la convergencia')
            string = 'numero de iteraciones maximas alcanzado, no se alcanzo la convergencia'
    else:
        print('intervalo inadecuado, no cumple con el teorema fa * fb < 0')
        string = 'intervalo inadecuado, no cumple con el teorema fa * fb < 0'
    return string

#funcion = 'x**3 - 6.2*x**2 + 10.01*x -4.84'

#reglaFalsa(1, 1.9, funcion, 100, 0.0000001)