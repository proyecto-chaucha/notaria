from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

class upload_form(FlaskForm):
    document = FileField('Subir archivo', validators=[FileRequired()])