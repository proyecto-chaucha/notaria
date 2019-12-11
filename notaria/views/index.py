import functools
from flask import Blueprint, render_template, session, redirect, url_for, request
from .utils import login_required
from notaria.forms import users


bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def home():
    hello = "Hola mundooo"
    return render_template('index.html', hello=hello)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = users.loginForm(request.form)
    if form.validate_on_submit():
        session['user'] = form.user.data
        return "OK"

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    if 'user' in session:
    	session.pop('user', None)
    	return "logout"
    else:
    	redirect(url_for('index.login'))


@bp.route('/admin')
@login_required
def admin():
    return "logged :D"