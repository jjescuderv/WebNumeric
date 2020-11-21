from flask import Flask, render_template, request
from Secant import Secant
from Multiple_roots import Multiple_roots
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
    print(iter)
    #lis_xi,lis_fx,lis_er,e,xa=Secant(iter,1.0,1.5,'ln(x**2+1)',(10**-7))
    lis_xi,lis_fx,lis_er,e,xa=Secant(iter,x0,x1,fun,err)
    #return "INFO data: {}{}{} error: {} xa: {}".format(lis_xi,lis_fx,lis_er,e,xa)
    #return "Hola"
    a=len(lis_xi)
    lis_a=list(range(0,a))
    return render_template("data1.html", lis_xi=lis_xi,lis_fx=lis_fx,lis_er=lis_er,e=e,xa=xa, lis_a=lis_a)

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

    lis_x0, lis_f0, lis_f1, lis_f2, lis_er, e, g = Multiple_roots(iter,x0,x1,fun,err)

    a=len(lis_x0)
    lis_a=list(range(0,a))

    return render_template("data2.html", lis_x0=lis_x0, lis_f0=lis_f0, lis_f1=lis_f1, lis_f2=lis_f2, lis_er=lis_er, e=e, g=g, lis_a=lis_a)


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

@app.route("/fixedPointInformation", methods=["GET", "POST"])
def FlaskFixedPoint():
    m=request.form.get("m")
    n=request.form.get("n")
    A=request.form.get("A")
    l_b=request.form.get("l_b")
    b=request.form.get("b")
    lis_it,lis_xi,lis_gx,lis_fx,lis_er,string2 = Punto_Fijo(iter,x0,fun,fun2,err)
    return render_template("dataFixedP.html",iter = lis_it,xi = lis_xi,gx = lis_gx,fx=lis_fx,er=lis_er,string=string2)

if __name__=="__main__":
    app.run(debug=True)