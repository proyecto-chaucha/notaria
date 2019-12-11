import functools
from flask import Blueprint, render_template, session, redirect, url_for, request

from notaria.views.utils import login_required
from notaria.forms.login import loginForm 
from notaria.models.users import userModel


bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/')
def home():
    hello = "Hola mundooo"
    return render_template('index.html', hello=hello)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm(request.form)
    if form.validate_on_submit():
        submitted_username = form.user.data

        user = userModel.query.filter_by(username=submitted_username).first()

        if user and user.username == submitted_username:
            session['user'] = form.user.data
            return redirect(url_for('index.admin'))
        else:
            return ":C"

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    if 'user' in session:
    	session.pop('user', None)
    	return redirect(url_for('index.home'))
    else:
    	return redirect(url_for('index.login'))


@bp.route('/admin')
@login_required
def admin():
    return render_template('admin.html')