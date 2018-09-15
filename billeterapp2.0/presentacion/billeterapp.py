from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user

from presentacion.forms import LoginForm, SignupForm
from negocio.usuarios import UserLogic

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="index")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userlogic = UserLogic()
        user = userlogic.find_by_username(form.username.data)
        if user is not None: #user.check_password(form.password.data, form.username.data):
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}.".format(user.username))
            return redirect(request.args.get('next') or url_for('bookmarks.user',
                                                username=user.username))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form)


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
        userlogic = UserLogic()
        userlogic.insert_one(user)
        flash('Welcome! Please login.')
        return redirect(url_for("login"))
    return render_template("signup.html", form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__== "__main__":
    app.run(debug=False, host="localhost")