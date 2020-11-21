from sympy import *

def Punto_Fijo(itera,x0,f,g,error):
  x = Symbol('x')
  itera = int(itera)
  x0 = float(x0)
  #f = input("ingrese la funcion a evaluar: ")
  #g = input("ingrese la funcion g: ")
  f = sympify(f)
  g = sympify(g)
  #error = input("Ingrese el maximo error absoluto aceptado: ")
  error = sympify(error)
  error = float(error)
  gx = g.subs(x, x0)
  fx = f.subs(x, x0)
  xi = gx
  e = 10
  c = 1
  gxant=0
  e = abs(gx - gxant)
  string = ""
  
  lis_xi=[]
  lis_fx=[]
  lis_gx=[]
  lis_er=[]
  lis_it=[]
  
  string += '\n'+str(format('iter',"5")+'\t'+format('  xi',"12")+'\t'+format('  g(xi)',"12")+'\t'+format('  f(xi)',"12")+'\t'+format('E',"1")+'\n')
  string += '\n'+str(format(0,"3.0f")+'\t'+format(x0,"12.10f")+'\t'+format(float(xi),"12.10f")+'\t'+format(float(fx),"1.1e")+'\n')
  lis_xi.append(x0)
  lis_it.append(0)
  lis_fx.append(fx)
  lis_gx.append(gx)
  lis_er.append(" ")
  while (e >= error and c <= itera):
    gxant = gx
    gx = g.subs(x, xi)
    fx = f.subs(x, xi)
    xi = gx
    e = abs(gx - gxant)
    if c == 1:
      string += '\n'+str(format(1,"3.0f")+'\t'+format(gxant,"12.10f")+'\t'+format(float(gx),"12.10f")+'\t'+format(float(fx),"1.1e")+'\t'+format(float(e),"1.1e")+'\n')
      lis_xi.append(x0)
      lis_it.append(1)
      lis_fx.append(gx)
      lis_gx.append(gxant)
      lis_er.append(e)
      c= c+1
    gxx = g.subs(x, gx)
    fxx = f.subs(x, gx)
    string += '\n'+str(format(c,"3.0f")+'\t'+format(float(xi),"12.10f")+'\t'+format(float(gxx),"12.10f")+'\t'+format(float(fxx),"1.1e")+'\t'+format(float(e),"1.1e")+'\n')
    lis_xi.append(xi)
    lis_it.append(c)
    lis_fx.append(fxx)
    lis_gx.append(gxx)
    lis_er.append(e)
    c = c + 1

  string2 = '\n'+str("Se encontro una aproximacion de la raiz en "+ format(float(gx),"12.15f")+'\n')
  return lis_it,lis_xi,lis_gx,lis_fx,lis_er,string2
  
#Punto_Fijo()