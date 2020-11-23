from flask import Flask, render_template, request
from Secant import Secant
from Multiple_roots import Multiple_roots
from Vandermonde import Vandermonde
from SOR import Sor
from LinealPlotter import LinealPlotter
from QuadraticPlotter import QuadraticPlotter
from false_rule import reglaFalsa
from fixed_point import Punto_Fijo
from LUsimple import Lusimple
from newton import Newton
from bisection import Bisection
from CubicPlotter import CubicPlotter
from Doolittle import Doolittle
from Jacobi import jacobi
import sympy as sp
from sympy import sin, cos, log, exp

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/secant")
def secant():
    return render_template("secant.html")

@app.route("/secantTable", methods=["GET", "POST"])
def FlaskSecant():
    iter=request.form.get("iter")
    x0=request.form.get("x0")
    x1=request.form.get("x1")
    fun=request.form.get("fun")
    err=request.form.get("err")
    
    if iter =='' or x0 =='' or x1=='' or fun=='' or err=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>" 

    lis_xi,lis_fx,lis_er,e,xa=Secant(iter,x0,x1,fun,err)

    a=len(lis_xi)
    lis_a=list(range(0,a))
    return render_template("secantT.html", lis_xi=lis_xi,lis_fx=lis_fx,lis_er=lis_er,e=e,xa=xa, lis_a=lis_a)

@app.route("/multipleRoots")
def multipleRoots():
    return render_template('multroots.html')

@app.route("/MultipleRootsTable", methods=["GET", "POST"])
def FlaskmultRoots():
    iter=request.form.get("iter")
    x0=request.form.get("x0")
    x1=request.form.get("x1")
    fun=request.form.get("fun")
    err=request.form.get("err")

    if iter =='' or x0 =='' or x1=='' or fun=='' or err=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    lis_x0, lis_f0, lis_f1, lis_f2, lis_er, e, g = Multiple_roots(iter,x0,x1,fun,err)

    a=len(lis_x0)
    lis_a=list(range(0,a))

    return render_template("multiplerootsT.html", lis_x0=lis_x0, lis_f0=lis_f0, lis_f1=lis_f1, lis_f2=lis_f2, lis_er=lis_er, e=e, g=g, lis_a=lis_a)


@app.route("/false-rule")
def falserule():
    return render_template("falseRule.html")

@app.route("/falseRuleInformation", methods=["GET", "POST"])
def FlaskFalseRule():
    iter=request.form.get("iter")
    x0=request.form.get("x0")
    x1=request.form.get("x1")
    fun=request.form.get("fun")
    err=request.form.get("err")
    string = reglaFalsa(iter,x0,x1,fun,err)
    return render_template("dataRule.html",string = string)

@app.route("/fixed-point")
def fixedpoint():
    return render_template("fixedPoint.html")

@app.route("/fixedPointInformation", methods=["GET", "POST"])
def FlaskFixedPoint():
    iter=request.form.get("iter")
    x0=request.form.get("x0")
    fun=request.form.get("fun")
    fun2=request.form.get("fun2")
    err=request.form.get("err")
    lis_it,lis_xi,lis_gx,lis_fx,lis_er,string2 = Punto_Fijo(iter,x0,fun,fun2,err)
    return render_template("dataFixedP.html",iter = lis_it,xi = lis_xi,gx = lis_gx,fx=lis_fx,er=lis_er,string=string2)

@app.route("/LUsimple")
def lusimple():
    return render_template("LUsimple.html")

@app.route("/LuSimpleInformation", methods=["GET", "POST"])
def FlaskLUsimple():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    l_b=request.form.get("l_b")
    b=request.form.get("b")
    if n=='' or m=='' or A=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"
    
    
    lis_stage,lis_m,list_L,list_U,result = Lusimple(m,n,A,l_b,b)
    x = len(lis_stage)
    z = list(range(0,x))
    return render_template("dataLuSimple.html",stage = lis_stage,M = lis_m, L=list_L,U=list_U,result = result,Z = z)

@app.route("/vandermonde")
def vandermonde():
    return render_template('vandermonde.html')

@app.route("/vandermondeTable", methods=["GET", "POST"])
def FlaskVandermonde():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    A,b,a = Vandermonde(n,x,y)

    return render_template("vandermondeT.html", A=A, b=b, a=a)

#FlaskSor
@app.route("/sor")
def sor():
    return render_template('sor.html')

@app.route("/sorTable", methods=["GET", "POST"])
def FlaskSor():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    b=request.form.get("b")
    x0=request.form.get("x0")
    iter=request.form.get("iter")
    error=request.form.get("error")
    w=request.form.get("w")
    
    if m == ''  or n=='' or A=='' or b=='' or x0=='' or iter=='' or error=='' or w=='' or m!=n:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    Tw,re,Cw,x1,x2,x3,er = Sor(m,n,A,b,x0,iter,error,w)

    a=len(x1)
    lis_a=list(range(0,a))

    return render_template("sorT.html", Tw=Tw,re=re,Cw=Cw,x1=x1,x2=x2,x3=x3,er=er,lis_a=lis_a)

@app.route("/linealplotter")
def linealplotter():
    return render_template('linealplotter.html')

@app.route("/linealplotterTable", methods=["GET", "POST"])
def Flasklinealp():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    A,b,S = LinealPlotter(n,x,y)

    return render_template("linealplotterT.html", A=A, b=b, S=S)

@app.route("/quadraticplotter")
def quadraticplotter():
    return render_template('quadraticplotter.html')

@app.route("/quadraticplotterTable", methods=["GET", "POST"])
def FlaskQuadraticp():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    A,b,S = QuadraticPlotter(n,x,y)

    return render_template("quadraticplotterT.html", A=A, b=b, S=S)

#------------------------------------------------------JHONATAN------------------------------------------------

@app.route("/newton")
def newton():
    return render_template("newton.html")

@app.route("/newton_results", methods=["GET", "POST"])
def newton_results():
    itera=request.form.get("itera")
    x0=request.form.get("x0")
    fun=request.form.get("fun")
    dfun=request.form.get("dfun")
    tol=request.form.get("tol")
    
    if itera =='' or x0 =='' or fun=='' or dfun=='' or tol=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>" 

    list_a,list_f,list_e,root=Newton(itera,x0,fun,dfun,tol)

    it=len(list_a)
    list_it=list(range(0,it))
    return render_template("newton.html", list_a=list_a,list_f=list_f,list_e=list_e, list_it=list_it, root=root)

@app.route("/bisection")
def bisection():
    return render_template("bisection.html")

@app.route("/bisection_results", methods=["GET", "POST"])
def bisection_results():

    iterastr=request.form.get("itera")
    astr=request.form.get("a")
    bstr=request.form.get("b")
    fstr=request.form.get("f")
    tolstr=request.form.get("tol")


    if iterastr =='' or astr =='' or bstr =='' or fstr =='' or tolstr=='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        itera = int(iterastr)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        a = float(astr)
    except:
        return "<h1 style='text-align: center;'>Check a value</h1>"

    try:
        b = float(bstr)
    except:
        return "<h1 style='text-align: center;'>Check b value</h1>"

    if b==a:
        return "<h1 style='text-align: center;'>Interval ends must be different</h1>"

    try:
        f = sp.sympify(fstr)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"

    try:
        tol = sp.sympify(tolstr)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"


    try:
        list_a, list_xm, list_b, list_fxm, list_E, root= Bisection(itera,a,b,f,tol)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"
    
    it=len(list_a)
    list_it=list(range(1,it+1))
    return render_template("bisection.html", list_a=list_a, list_xm=list_xm, list_b=list_b, list_fxm = list_fxm,
    list_E = list_E, list_it=list_it, root=root)

#----------------------------------------------------END JHONATAN ---------------------------------------------
   
@app.route("/cubicplotter")
def cubicplotter():
    return render_template('cubicplotter.html')

@app.route("/cubicplotterTable", methods=["GET", "POST"])
def FlaskCubicPlotter():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    A,b,S = CubicPlotter(n,x,y)

    return render_template("cubicplotterT.html", A=A, b=b, S=S)

@app.route("/doolittle")
def doolittle():
    return render_template('doolittle.html')

@app.route("/doolittleTable", methods=["GET", "POST"])
def FlaskDoolittle():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    l_b=request.form.get("l_b")
    b=request.form.get("b")
    if n=='' or m=='' or A=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"
    
    
    lis_stage,lis_m,list_L,list_U,result = Doolittle(m,n,A,l_b,b)
    x = len(lis_stage)
    z = list(range(0,x))
    return render_template("dataDoolittle.html",stage = lis_stage,M = lis_m, L=list_L,U=list_U,result = result,Z = z)

@app.route("/jacobi")
def Jacobi():
    return render_template('jacobi.html')

@app.route("/JacobiTable", methods=["GET", "POST"])
def FlaskJacobi():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    b=request.form.get("b")
    x0=request.form.get("x0")
    Nmax=request.form.get("iter")
    tol=request.form.get("error")
    lb=request.form.get("lb")
    lx0=request.form.get("lx0")
    
    if m == ''  or n=='' or A=='' or b=='' or x0=='' or iter=='' or tol=='' or  m!=n:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    T,C,respect1,lis_iter,lis_er,lis_xi = jacobi(A,b,x0,tol,Nmax,m,n,lb,lx0)

    a=len(lis_iter)
    lis_a=list(range(0,a))

    return render_template("JacobiT.html", T=T,C=C,radio=respect1,iter=lis_iter,er=lis_er,xi=lis_xi,lis_a=lis_a)

if __name__=="__main__":
    app.run(debug=True)