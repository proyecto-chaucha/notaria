from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm


class upload_form(FlaskForm):
    document = FileField('Subir archivo', validators=[FileRequired()])
