from flask import Flask, render_template, request
from Secant import Secant
from Multiple_roots import Multiple_roots
from Vandermonde import Vandermonde
from SOR import Sor
from LinealPlotter import LinealPlotter
from QuadraticPlotter import QuadraticPlotter
from false_rule import reglaFalsa
from fixed_point import Punto_Fijo

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
"""
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
"""
@app.route("/LUsimple")
def lusimple():
    return render_template("LUsimple.html")

@app.route("/fixedPointInformation", methods=["GET", "POST"])
def FlaskFixedPoint():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    l_b=request.form.get("l_b")
    b=request.form.get("b")
    lis_it,lis_xi,lis_gx,lis_fx,lis_er,string2 = Punto_Fijo(iter,x0,fun,fun2,err)
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

if __name__=="__main__":
    app.run(debug=True)