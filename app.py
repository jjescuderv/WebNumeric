from flask import Flask, render_template, request
from Secant import Secant
from Multiple_roots import Multiple_roots
from Vandermonde import Vandermonde
from SOR import Sor
from LinealPlotter import LinealPlotter
from QuadraticPlotter import QuadraticPlotter
from false_rule import reglaFalsa
from fixed_point import Punto_Fijo
from LUsimple import lu_simple
from LUpar import lu_partial_pivoting
from newton import Newton
from bisection import Bisection
from CubicPlotter import CubicPlotter
from Doolittle import Doolittle
from Jacobi import jacobi
from Gauss_Seidel import gauss_seidel
from Gauss_partial_pivoting import gauss_partial_pivoting
from Gauss_total_pivoting import gauss_total_pivoting
from Gauss_simple import gauss_simple
from incremental_searches import Incremental_searches
import sympy as sp
from sympy import sin, cos, log, exp
from crout import Crout
from chol import Cholesky
from diffdiv import Newton_diff
from lagrange import Lagrange

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ----------------------------------------------------- Juan Escudero -----------------------------------------------------

@app.route("/direct_methods")
def direct_methods():
    result = []
    return render_template("matrices/direct_methods.html", result=result)

@app.route("/gauss", methods=["GET", "POST"])
def gauss():
    mat = request.form.getlist('mat[]')
    vec = request.form.getlist('vec[]')
    method = int(request.form.get('method'))
    n = int(request.form.get('matrix_size'))

    if method == 1:
        result = gauss_simple(n, mat, vec)
    elif method == 2:
        result = gauss_partial_pivoting(n, mat, vec)
    else:
        result = gauss_total_pivoting(n, mat, vec)

    return render_template("matrices/direct_methods.html", result=result)

@app.route("/lu_factorization")
def lu_factorization():
    result = []
    return render_template("matrices/lu_factorization.html", result=result)

@app.route("/lu", methods=["GET", "POST"])
def lu():
    mat = request.form.getlist('mat[]')
    vec = request.form.getlist('vec[]')
    method = int(request.form.get('method'))
    n = int(request.form.get('matrix_size'))

    if method == 1:
        result = lu_simple(n, mat, vec)
    else:
        result = lu_partial_pivoting(n, mat, vec)

    return render_template("matrices/lu_factorization.html", result=result)

@app.route("/gauss_seidel")
def gauss_seidelT():
    return render_template('gauss_seidel.html')

@app.route("/gauss_seidelTable", methods=["GET", "POST"])
def Flask_gauss_seidel():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    b=request.form.get("b")
    x0=request.form.get("x0")
    Nmax=request.form.get("iter")
    tol=request.form.get("error")
    lb=request.form.get("lb")
    lx0=request.form.get("lx0")
    
    if m == ''  or n=='' or A=='' or b=='' or x0=='' or tol=='' or lb=='' or  m!=n or Nmax=='' or lx0=='':
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    try:
        m = int(m)
    except:
        return "<h1 style='text-align: center;'>Check the number of rows</h1>"

    try:
       n = int(n)
    except:
        return "<h1 style='text-align: center;'>Check the number of columns</h1>"

    try:
        lb = int(lb)
    except:
        return "<h1 style='text-align: center;'>Check the length b vector</h1>"
    
    try:
        Nmax = int(Nmax)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"
    
    try:
        lx0 = int(lx0)
    except:
        return "<h1 style='text-align: center;'>Check the length x0 vector</h1>"

    try:
        tol = sp.sympify(tol)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"
    
    try:
        T,C,respect1,lis_iter,lis_er,lis_xi = gauss_seidel(A,b,x0,tol,Nmax,m,n,lb,lx0)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    a=len(lis_iter)
    lis_a=list(range(0,a))

    return render_template("gauss_seidelT.html", T=T,C=C,radio=respect1,iter=lis_iter,er=lis_er,xi=lis_xi,lis_a=lis_a)

# --------------------------------------------------------------------------------------------------------------------------

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

    try:
        itera = int(iter)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        a = float(x0)
    except:
        return "<h1 style='text-align: center;'>Check first initial value</h1>"

    try:
        b = float(x1)
    except:
        return "<h1 style='text-align: center;'>Check second initial value</h1>"

    if b==a:
        return "<h1 style='text-align: center;'>Interval ends must be different</h1>"

    try:
        f = sp.sympify(fun)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"

    try:
        tol = sp.sympify(err)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"

    try:
        lis_xi,lis_fx,lis_er,e,xa=Secant(iter,x0,x1,fun,err)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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
    fun=request.form.get("fun")
    err=request.form.get("err")

    if iter =='' or x0 =='' or fun=='' or err=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    try:
        itera = int(iter)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        a = float(x0)
    except:
        return "<h1 style='text-align: center;'>Check first initial value</h1>"

    try:
        f = sp.sympify(fun)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"

    try:
        tol = sp.sympify(err)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"

    try:
        lis_x0, lis_f0, lis_f1, lis_f2, lis_er, e, g = Multiple_roots(iter,x0,fun,err)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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
    if iter =='' or x0 =='' or x1 =='' or fun =='' or err=='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        iter = int(iter)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        x0 = float(x0)
    except:
        return "<h1 style='text-align: center;'>Check a value</h1>"

    try:
        x1 = float(x1)
    except:
        return "<h1 style='text-align: center;'>Check b value</h1>"

    if x0==x1:
        return "<h1 style='text-align: center;'>Interval ends must be different</h1>"

    try:
        fun = sp.sympify(fun)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"

    try:
        err = float(eval(err))
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"

    try:
        string = reglaFalsa(iter,x0,x1,fun,err)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"
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
    
    if iter =='' or x0 =='' or  fun2 =='' or fun =='' or err=='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        iter = int(iter)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        x0 = float(x0)
    except:
        return "<h1 style='text-align: center;'>Check initial value</h1>"

    try:
        fun2 = sp.sympify(fun2)
    except:
        return "<h1 style='text-align: center;'>Check function g entered</h1>"

    try:
        fun = sp.sympify(fun)
    except:
        return "<h1 style='text-align: center;'>Check function f entered</h1>"

    try:
        err = float(eval(err))
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"

    try:
        lis_it,lis_xi,lis_gx,lis_fx,lis_er,string2 = Punto_Fijo(iter,x0,fun,fun2,err)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"
   
    return render_template("dataFixedP.html",iter = lis_it,xi = lis_xi,gx = lis_gx,fx=lis_fx,er=lis_er,string=string2)

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

    try:
        A = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,a = Vandermonde(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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

    try:
        itera = int(iter)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        M = int(m)
    except:
        return "<h1 style='text-align: center;'>Check m value</h1>"

    try:
        N = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value</h1>"

    try:
        values_A = list(map(float, A.split()))
    except:
        return "<h1 style='text-align: center;'>Check A Matix entered</h1>"

    try:
        values_b = list(map(float, b.split()))
    except:
        return "<h1 style='text-align: center;'>Check b vector entered</h1>"

    try:
        values_x0 = list(map(float, x0.split()))
    except:
        return "<h1 style='text-align: center;'>Check b vector entered</h1>"

    try:
        valuesErr = float(eval(error))
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered</h1>"

    try:
        valueW = float(w)
    except:
        return "<h1 style='text-align: center;'>Check w value entered</h1>"

    try:
        Tw,re,Cw,x1,x2,x3,er = Sor(m,n,A,b,x0,itera,error,w)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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

    try:
        A = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,S = LinealPlotter(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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

    try:
        A = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,S = QuadraticPlotter(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    return render_template("quadraticplotterT.html", A=A, b=b, S=S)

#------------------------------------------------------JHONATAN------------------------------------------------

@app.route("/newton")
def newton():
    return render_template("newton.html")

@app.route("/newton_results", methods=["GET", "POST"])
def newton_results():
    iterastr=request.form.get("itera")
    x0str=request.form.get("x0")
    funstr=request.form.get("fun")
    dfunstr=request.form.get("dfun")
    tolstr=request.form.get("tol")

    if iterastr =='' or x0str =='' or funstr =='' or dfunstr =='' or tolstr =='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        itera = int(iterastr)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        x0 = float(x0str)
    except:
        return "<h1 style='text-align: center;'>Check initial value</h1>"

    try:
        fun = sp.sympify(funstr)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"

    try:
        dfun = sp.sympify(dfunstr)
    except:
        return "<h1 style='text-align: center;'>Check </h1>"
    try:
        tol = sp.sympify(tolstr)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"


    try:
        list_a,list_f,list_e,root=Newton(itera,x0,fun,dfun,tol)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"


    it=len(list_a)
    list_it=list(range(0,it))
    return render_template("newton.html", list_a=list_a,list_f=list_f,list_e=list_e, list_it=list_it, root=root)

@app.route("/searches")
def searches():
    return render_template("searches.html")

@app.route("/searches_results", methods=["GET", "POST"])
def searches_results():

    iterastr=request.form.get("itera")
    x0str=request.form.get("x0")
    deltastr=request.form.get("delta")
    fstr=request.form.get("f")


    if iterastr =='' or x0str =='' or deltastr =='' or fstr =='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        itera = int(iterastr)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"

    try:
        x0 = float(x0str)
    except:
        return "<h1 style='text-align: center;'>Check a value</h1>"

    try:
        delta = float(deltastr)
    except:
        return "<h1 style='text-align: center;'>Check b value</h1>"

    try:
        f = sp.sympify(fstr)
    except:
        return "<h1 style='text-align: center;'>Check function entered</h1>"


    try:
        list_apr = Incremental_searches(itera,x0,delta,f)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    return render_template("searches.html", list_apr=list_apr)

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
        list_a, list_xm, list_b, list_fxm, list_E, root, error= Bisection(itera,a,b,f,tol)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"
    
    it=len(list_a)
    list_it=list(range(1,it+1))
    return render_template("bisection.html", list_a=list_a, list_xm=list_xm, list_b=list_b, list_fxm = list_fxm,
    list_E = list_E, list_it=list_it, root=root, error = error)



@app.route("/crout")
def crout():
    test = []
    return render_template("crout.html", test=test)

@app.route("/crout_results", methods=["GET", "POST"])
def crout_results():
    mat = request.form.getlist('mat[]')
    vec = request.form.getlist('vec[]')
    n = int(request.form.get('matrix_size'))

    result = Crout(n, mat, vec)

    return render_template("crout.html", result=result)

@app.route("/chol")
def chol():
    test = []
    return render_template("chol.html", test=test)

@app.route("/chol_results", methods=["GET", "POST"])
def chol_results():
    mat = request.form.getlist('mat[]')
    vec = request.form.getlist('vec[]')
    n = int(request.form.get('matrix_size'))

    result = Cholesky(n, mat, vec)

    return render_template("chol.html", result=result)

@app.route("/diffdiv")
def diffdiv():
    return render_template('diffdiv.html')

@app.route("/diffdiv_results", methods=["GET", "POST"])
def diffdiv_results():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    try:
        A = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,a = Newton_diff(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    return render_template("diffdiv.html", A=A, b=b, a=a)

@app.route("/lagrange")
def lagrange():
    return render_template('lagrange.html')

@app.route("/lagrange_results", methods=["GET", "POST"])
def lagrange_results():
    n=request.form.get("n")
    x=request.form.get("x")
    y=request.form.get("y")
    
    if n=='' or x=='' or y=='':
        return "<h1 style='text-align: center;'>Check Values Entered</h1>"

    try:
        A = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,a = Lagrange(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    return render_template("lagrange.html", A=A, b=b, a=a)

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

    try:
        n = int(n)
    except:
        return "<h1 style='text-align: center;'>Check n value entered</h1>"

    try:
        values_x = list(map(float, x.split()))
    except:
        return "<h1 style='text-align: center;'>Check x vector entered</h1>"

    try:
        values_y = list(map(float, y.split()))
    except:
        return "<h1 style='text-align: center;'>Check y vector entered</h1>"

    try:
        A,b,S = CubicPlotter(n,x,y)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

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
    if m =='' or n =='' or  A =='' or l_b =='' or b=='':
        return "<h1 style='text-align: center;'>You are missing one or more values</h1>" 

    try:
        m = int(m)
    except:
        return "<h1 style='text-align: center;'>Check the number of rows</h1>"

    try:
       n = int(n)
    except:
        return "<h1 style='text-align: center;'>Check the number of columns</h1>"

    try:
        l_b = int(l_b)
    except:
        return "<h1 style='text-align: center;'>Check the length b vector</h1>"

    try:
        lis_stage,lis_m,list_L,list_U,result = Doolittle(m,n,A,l_b,b)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"
     
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
    
    if m == ''  or n=='' or A=='' or b=='' or x0=='' or tol=='' or lb=='' or  m!=n or Nmax=='' or lx0=='':
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    try:
        m = int(m)
    except:
        return "<h1 style='text-align: center;'>Check the number of rows</h1>"

    try:
       n = int(n)
    except:
        return "<h1 style='text-align: center;'>Check the number of columns</h1>"

    try:
        lb = int(lb)
    except:
        return "<h1 style='text-align: center;'>Check the length b vector</h1>"
    
    try:
        Nmax = int(Nmax)
    except:
        return "<h1 style='text-align: center;'>Check iteration value</h1>"
    
    try:
        lx0 = int(lx0)
    except:
        return "<h1 style='text-align: center;'>Check the length x0 vector</h1>"

    try:
        tol = sp.sympify(tol)
    except:
        return "<h1 style='text-align: center;'>Check tolerance entered {{tol}}</h1>"
    
    try:
        T,C,respect1,lis_iter,lis_er,lis_xi = jacobi(A,b,x0,tol,Nmax,m,n,lb,lx0)
    except:
        return "<h1 style='text-align: center;'>Check values entered</h1>"

    a=len(lis_iter)
    lis_a=list(range(0,a))

    return render_template("JacobiT.html", T=T,C=C,radio=respect1,iter=lis_iter,er=lis_er,xi=lis_xi,lis_a=lis_a)

if __name__=="__main__":
    app.run(debug=True)
