import functools
from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.forms.users import login_form, register_form
from notaria.functions.users import validate_user, register_user


bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def home():
    hello = "Hola mundooo"
    return render_template('index.html', hello=hello)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = login_form(request.form)
    if form.validate_on_submit():

        valid_user = validate_user(form)

        if valid_user:
            session['user'] = form.user.data
            return redirect(url_for('index.admin'))
        elif valid_user == None:
            flash("Usuario no existe")
        else:
            flash("Contraseña incorrecta")

    return render_template('login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
@login_restricted
def register():
    form = register_form(request.form)

    if form.validate_on_submit():
        register_user(form)
    
    return render_template('register.html', form=form)


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
