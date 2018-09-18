from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user
from collections import namedtuple
import pygal

from negocio.usuarios import UserLogic
from entidades.objects import Usuario
from presentacion.forms import LoginForm, SignupForm, RegistrosForm
from negocio.registros import RegistroLogic

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")

#@app.route("/lista")
#def lista():
#    carlist = ['Subaru', 'Chevy']
#    if request.method == 'POST':
#        manufacturer = request.form['manu']
#        flash(str(manufacturer))
#    return render_template("new_register.html", title = 'Home', carlist=carlist)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserLogic.find_by_username(form.username.data)
        if user is not None and UserLogic.check_password(form.password.data, form.username.data):
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Usuario o contrasena incorrecta.')
    return render_template("login.html", form=form)

 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@app.route("/new_register", methods=["GET", "POST"])
def new_register():
    form = RegistrosForm()
    registro = {"categoria": form.categoria.data,
                "valor": form.valor.data,
                "descripcion": form.descripcion.data}
    reglogic = RegistroLogic()
    reglogic.insert_one(registro)
    flash('Registro cargado!')
    return redirect(url_for("new_register.html"))

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = Usuario(form.email.data,
                form.username.data,
                form.password.data)
        userlogic = UserLogic()
        userlogic.insert_one(user)
        flash('Welcome! Please login.')
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)

@app.route("/graphs")
def grapic_example():
    graph = pygal.Pie(inner_radius=.40)
    graph.title = 'Todos tus registros pillo'
    graph.add('Comida', 19.5)
    graph.add('Alquiler', 36.6)
    graph.add('Ropa', 36.3)
    graph.add('Bancos', 4.5)
    graph.add('Salidas', 2.3)
    graph_data = graph.render_data_uri()
    return render_template("graphs.html", graph_data=graph_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__== "__main__":
    app.run(debug=False, host="localhost")