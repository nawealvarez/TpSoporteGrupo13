from flask import Flask, render_template
from flask_pymongo import PyMongo
from presentacion.billeterapp import app
from datos.manejodedatos import Manejobd

mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = mongo.Aversiahorradb.usuarios.find({"online": True})
    return render_template("index.html",
        online_users=online_users)