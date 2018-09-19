from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from flask_webhelpers import ObjectGrid
import pygal

from negocio.usuarios import UserLogic
from entidades.objects import Usuario
from presentacion.forms import LoginForm, SignupForm, RegistrosForm
from negocio.registros import RegistroLogic

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return UserLogic.find_by_id(int(userid))

@app.route("/")
@app.route("/index")
def index():
    moves = RegistroLogic.get_lasts_registers(current_user.get_id(), 10),
    return render_template("index.html", title="index", moves=moves)

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
    if form.validate_on_submit():
        registro = {"categoria": form.categoria.data,
                    "valor": form.valor.data,
                    "descripcion": form.descripcion.data}
        RegistroLogic.insert_one(registro)
        flash('Registro cargado!')
        return redirect(url_for("new_register"))
    return render_template("new_register.html", form=form)

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