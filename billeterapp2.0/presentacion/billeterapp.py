from flask import Flask, render_template, url_for, redirect, request, flash, abort
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
import pygal
from pygal.style import Style
from datetime import datetime
from collections import namedtuple

from negocio.usuarios import UserLogic
from entidades.objects import Usuario
from presentacion.forms import LoginForm, SignupForm, GastoForm, IngresoForm, SueldoForm
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
        sueldo = RegistroLogic.get_sueldo(current_user.get_id())
    else: 
        moves = None
        balance = None
        sueldo = None
    return render_template("index.html", title="index", moves=moves, balance=balance, sueldo=sueldo)

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


@app.route("/gastonew", methods=["GET", "POST"])
@login_required
def gastonew():
    form = GastoForm()
    if form.validate_on_submit():
        gasto = {"tipo": "gasto",
                "categoria": form.categoria.data.split(","),
                "valor": form.valor.data,
                "descripcion": form.descripcion.data,
                "fecha": datetime.utcnow(),
                "userid": current_user.get_id()}
        RegistroLogic.insert_one(gasto)
        flash('Su gasto ha sido cargado con exito!')
        return redirect(url_for("index"))
    return render_template("registros_form.html", form=form, type="Gasto", title="Registrar gasto")
        

@app.route("/ingresonew", methods=["GET", "POST"])
@login_required
def ingresonew():
    userid=current_user.get_id()
    lista_cats = RegistroLogic.get_cats_names(userid, "ingreso")
    form = IngresoForm()
    if form.validate_on_submit():
        ingreso = {"tipo": "ingreso",
                    "categoria": form.categoria.data.split(","),
                    "valor": form.valor.data,
                    "descripcion": form.descripcion.data,
                    "fecha": datetime.utcnow(),
                    "userid": userid}
        RegistroLogic.insert_one(ingreso)
        flash('Si ingreso ha sido cargado con exito!')
        return redirect(url_for("index"))
    return render_template("registros_form.html", form=form, type="ingreso", datalist=lista_cats, title="Registrar ingreso")


@app.route("/sueldonew", methods=["GET", "POST"])
@login_required
def sueldonew():
    form = SueldoForm()
    if form.validate_on_submit():
        sueldo ={   "tipo": "ingreso",
                    "categoria": ["sueldo"],
                    "valor": form.valor.data,
                    "descripcion": "Ingreso de Sueldo",
                    "fecha": datetime.utcnow(),
                    "userid": current_user.get_id()}
        RegistroLogic.insert_one(sueldo)
        flash('Su sueldo ha sido cargado con exito!')
        return redirect(url_for("index"))
    return render_template("sueldo_form.html", form=form, type="sueldo", title="Registrar último sueldo")


@app.route("/edit/<string:registro_id>", methods=["GET", "POST"])
@login_required
def edit(registro_id):
    registro = RegistroLogic.get_by_id(registro_id)
    if not registro:
        abort(404)
    if current_user.get_id() != registro["userid"]:
        abort(401)
    registro["id"] = registro.pop("_id")
    registro["categoria"] = ", ".join(registro["categoria"])
    d_reg = namedtuple("Registro", registro.keys(), verbose=True)(*registro.values())
    form = GastoForm(obj=d_reg) if registro["tipo"] == "gasto" else IngresoForm(obj=d_reg)
    if form.validate_on_submit():
        reg = {"categoria": form.categoria.data.split(","),
                    "valor": form.valor.data,
                    "descripcion": form.descripcion.data}
        RegistroLogic.update_registro(registro_id, reg)
        flash("Su {} ha sido modificado correctamente!".format(registro["tipo"]))
        return redirect(url_for("index"))
    return render_template("registros_form.html", form=form, title="Editar", tipo="editar")

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
@login_required
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
    for c,v in RegistroLogic.get_cats(current_user.get_id(), 'gasto').items():
        graph2.add(c,v)
    graph_da = graph2.render_data_uri()
    graph3 = pygal.Pie(inner_radius=.40, style=custom_style)
    graph3.title = 'Distribucion de ingresos'
    for c,v in RegistroLogic.get_cats(current_user.get_id(), 'ingreso').items():
        graph3.add(c,v)
    graph_dat = graph3.render_data_uri()
    return render_template("graphs.html", graph_data=graph_data, graph_da=graph_da, graph_dat=graph_dat)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

@app.errorhandler(401)
def forbidden(e):
    return render_template('401.html'), 401

if __name__ == "__main__":
    app.run(debug=False, host="localhost")