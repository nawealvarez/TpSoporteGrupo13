from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
import pygal
<<<<<<< HEAD
import json
=======
from pygal.style import Style
>>>>>>> ce90c7a142a7f4ca837a4feab8217160a0e9fd9e
from datetime import datetime

from negocio.usuarios import UserLogic
from entidades.objects import Usuario
from presentacion.forms import LoginForm, SignupForm, GastoForm, IngresoForm, RegistrosForm
from negocio.registros import RegistroLogic


app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['DEBUG'] = True
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return UserLogic.find_by_id(int(userid))


@app.route("/")
@app.route("/index")
def index():
    if current_user.is_authenticated:
        moves = RegistroLogic.get_lasts_registers(current_user.get_id(), 10)
        balance = RegistroLogic.get_balance(current_user.get_id())
        #graph = pygal.Pie(inner_radius=.40)
        #graph.title = 'Todos tus registros'
        #print(current_user.get_id())
        #for c,v in RegistroLogic.get_categorias(current_user.get_id()).items():
        #    graph.add(c,v)
        #graph_data = graph.render_data_uri()
    else: 
        moves = None
        balance = None
        #graph_data = None
    return render_template("index.html", title="index", moves=moves, balance=balance)

<<<<<<< HEAD

=======
>>>>>>> ce90c7a142a7f4ca837a4feab8217160a0e9fd9e
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
    return redirect(url_for('index'))

<<<<<<< HEAD

@app.route("/new_register", methods=["GET", "POST"])
def new_register():
    form = RegistrosForm()
    if form.validate_on_submit():
        registro = {"tipo": form.tipo.data,
                    "categoria": form.categoria.data,
                    "valor": form.valor.data,
                    "descripcion": form.descripcion.data,
                    "fecha": datetime.utcnow(),
                    "userid": current_user.get_id()}
        RegistroLogic.insert_one(registro)
        flash('Registro cargado!')
        return redirect(url_for("new_register"))
    return render_template("new_register.html", form=form)

=======
>>>>>>> ce90c7a142a7f4ca837a4feab8217160a0e9fd9e
@app.route("/gastonew", methods=["GET", "POST"])
def gastonew():
    form = GastoForm()
    if form.validate_on_submit():
        gasto = {"tipo": "gasto",
                "categoria": form.categoria.data,
                "valor": form.valor.data,
                "descripcion": form.descripcion.data,
                "fecha": datetime.utcnow(),
                "userid": current_user.get_id()}
        RegistroLogic.insert_one(gasto)
        flash('Gasto cargado!')
        return redirect(url_for("gastonew"))
    return render_template("gastonew.html", form=form)
        

@app.route("/ingresonew", methods=["GET", "POST"])
def ingresonew():
    form = IngresoForm()
    if form.validate_on_submit():
        ingreso = {"tipo": "ingreso",
                    "categoria": form.categoria.data,
                    "valor": form.valor.data,
                    "descripcion": form.descripcion.data,
                    "fecha": datetime.utcnow(),
                    "userid": current_user.get_id()}
        RegistroLogic.insert_one(ingreso)
        flash('Ingreso cargado!')
        return redirect(url_for("ingresonew"))
    return render_template("ingresonew.html", form=form)

@app.context_processor
def util_processor():
    def get_all_categories():
        return RegistroLogic.get_all_categories()
        #return {"nombre": "juan"}
    return dict(get_all_categories=get_all_categories)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = Usuario(form.username.data,
                       form.email.data)
        user.password = form.password.data
        UserLogic.insert_one(user)
        flash('Welcome! Please login.')
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)


@app.route("/graphs")
def grapic_example():
    custom_style = Style(background='transparent', title_font_size=40, legend_font_size=35, transition='400ms ease-in')
    graph = pygal.Pie(inner_radius=.40, style=custom_style)
    graph.title = 'Todos tus registros'
    print(current_user.get_id())
    for c,v in RegistroLogic.get_tipos(current_user.get_id()).items():
        graph.add(c,v)
    graph_data = graph.render_data_uri()
    graph2 = pygal.Pie(inner_radius=.40, style=custom_style)
    graph2.title = 'Distribucion de gastos'
    for c,v in RegistroLogic.get_categorias(current_user.get_id(), 'gasto').items():
        graph2.add(c,v)
    graph_da = graph2.render_data_uri()
    graph3 = pygal.Pie(inner_radius=.40, style=custom_style)
    graph3.title = 'Distribucion de ingresos'
    for c,v in RegistroLogic.get_categorias(current_user.get_id(), 'ingreso').items():
        graph3.add(c,v)
    graph_dat = graph3.render_data_uri()
    return render_template("graphs.html", graph_data=graph_data, graph_da=graph_da, graph_dat=graph_dat)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=False, host="localhost")