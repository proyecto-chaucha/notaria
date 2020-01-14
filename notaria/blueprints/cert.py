from flask import Blueprint, render_template, session, redirect, url_for, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.functions.wallet import get_keychain, get_unspent, create_tx
from notaria.functions.cert import process_file
from notaria.forms.cert import upload_form
from notaria.models.cert import cert_model
from sqlite3 import OperationalError

bp = Blueprint('cert', __name__, url_prefix='/cert')


@bp.route('/')
@login_required
def index():
    try:
        certs = cert_model.query.filter_by(username=session['user']).all()
    except OperationalError:
        certs = []
    return render_template('certs.html', certs=certs)


@bp.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():

    privkey, address = get_keychain(session['user'])
    unspent = get_unspent(address)

    form = upload_form()

    if form.validate_on_submit():
        if process_file(session['user'], form):
            return redirect(url_for('cert.index'))
        else:
            flash("error al procesar el archivo")

    return render_template('upload.html', form=form, unspent=unspent)


@bp.route('/view/<string:sha3>')
@login_required
def view(sha3):
    flash(sha3)
    certs = cert_model.query.filter_by(username=session['user']).all()
    return render_template('certs.html', certs=certs)
