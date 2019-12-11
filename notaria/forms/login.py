from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"%s - %s" %
                  (getattr(form, field).label.text, error), 'is-danger')


class loginForm(FlaskForm):
    user = StringField('Nombre de usuario', validators=[DataRequired()])
    passwd = PasswordField('Contraseña', validators=[DataRequired()])