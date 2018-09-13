from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user

from negocio.usuarios import UserLogic
from presentacion.forms import LoginForm, SignupForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e"

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = UserLogic()
        user = u.find_by_username(form.username.data)
        if user is not None: #Check password aca
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form, title="Login")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = {"email": form.email.data,
                    "username": form.username.data,
                    "password": form.password.data}
        u = UserLogic()
        u.insert_one(user)
        flash('Welcome, {}! Please login.'.format(user["username"]))
        return redirect(url_for('.login'))
    return render_template("signup.html", form=form, title="Signup")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__== "__main__":
    app.run(debug=False, host="localhost")