import os
from flask import Flask
from flask_login import LoginManager
from flask_moment import Moment

app = Flask(__name__)
app.config["SECRET_KEY"] = 'oS\xf8\xf4\xe2\xc8\xda\xe3\x7f\xc75*\x83\xb1\x06\x8c\x85\xa4\xa7piE\xd6I'
app.config["DEBUG"] = True
