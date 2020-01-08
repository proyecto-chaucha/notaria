from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class login_form(FlaskForm):
    user = StringField('Nombre de usuario', validators=[DataRequired()])
    passwd = PasswordField('Contraseña', validators=[DataRequired()])


class register_form(FlaskForm):
    user = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired()])
    passwd = PasswordField('Contraseña', validators=[DataRequired()])
