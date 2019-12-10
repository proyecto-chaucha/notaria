import functools
from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('index.html', hello="Hola mundooo")