from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Regexp, Email, EqualTo, ValidationError

from negocio.usuarios import UserLogic
from util.validations import UserValidations

class LoginForm(Form):
    username = StringField("Usuario: ", validators=[DataRequired()])
    password = PasswordField("Contrasena: ", validators=[DataRequired()])
    remember_me = BooleanField("Mantenerme logeado: ")
    submit = SubmitField("Iniciar sesion")


class SignupForm(Form):
    username = StringField("Usuario: ", 
                    validators=[
                        DataRequired(),
                        Length(3, 80),
                        Regexp("^[A-Za-z0-9_]{3,}$",
                        message="El usuario consiste en numeros, letras y guionbajos.")])

    password = PasswordField("Contrasena: ", 
                    validators=[
                        DataRequired(), 
                        EqualTo("password2", message="Las contrasenas deben coincidir.")])
    
    password2 = PasswordField("Confirmar contrasena: ", validators=[DataRequired()])

    email = StringField("Email: ", validators=[DataRequired(), Length(1, 20), Email()])

    def validate_email(self, email_field):
        if UserValidations.is_email_valid(email_field.data):
            raise ValidationError("Ya existe un usuario con este email.")
    
    def validate_username(self, username_field):
        if UserValidations.is_username_valid(username_field.data):
            raise ValidationError("Usuario existente.")