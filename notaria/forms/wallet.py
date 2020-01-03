from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError


class send_form(FlaskForm):
    address = StringField('Destinatario', validators=[DataRequired()])
    amount = DecimalField('Monto', validators=[DataRequired()])
