from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, FloatField, DateField, SelectField, SelectMultipleField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, url, Length, Regexp, Email, EqualTo, ValidationError, NumberRange

from negocio.usuarios import UserLogic
from negocio.registros import RegistroLogic
from util.validations import UserValidations

class LoginForm(Form):
    username = StringField("Usuario: ", validators=[DataRequired()])
    password = PasswordField("Contrasena: ", validators=[DataRequired()])
    remember_me = BooleanField("Mantenerme logeado: ")
    submit = SubmitField("Iniciar sesion")

class SueldoForm(Form):
    valor = FloatField("Valor del sueldo", validators=[DataRequired(), NumberRange(0, None, "El valor ingresado debe ser mayor a cero.")])


class IngresoForm(Form):
    categoria = StringField("Categoria del ingreso: ",validators=[DataRequired()])
    valor = FloatField("Valor del ingreso: ", validators=[DataRequired(), NumberRange(0, None, "El valor ingresado debe ser mayor a cero.")])
    descripcion = StringField("Descripcion(opcional): ")

class GastoForm(Form):
    categoria = StringField("Categoria del gasto: ", validators=[DataRequired()])
    valor = FloatField("Valor del gasto: ", validators=[DataRequired(), NumberRange(0, None, "El valor ingresado debe ser mayor a cero.")])
    descripcion = StringField("Descripcion(opcional): ")

class SignupForm(Form):
    username = StringField("Usuario: ", 
                    validators=[
                        DataRequired(),
                        Length(3, 80, "El nombre de usuario debe contener entre 3 y 80 caracteres."),
                        Regexp("^[A-Za-z0-9_]{3,}$",
                        message="El usuario consiste en numeros, letras y guionbajos.")])

    password = PasswordField("Contrasena: ", 
                    validators=[
                        DataRequired(), 
                        EqualTo("password2", message="Las contrasenas deben coincidir.")])
    
    password2 = PasswordField("Confirmar contrasena: ", validators=[DataRequired()])

    email = StringField("Email: ", validators=[DataRequired(), Length(1, 50), Email()])

    def validate_email(self, email_field):
        if UserValidations.is_email_valid(email_field.data):
            raise ValidationError("Ya existe un usuario con este email.")
    
    def validate_username(self, username_field):
        if UserValidations.is_username_valid(username_field.data):
            raise ValidationError("El usuario ya existe.")