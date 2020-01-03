from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.functions.wallet import get_keychain, get_unspent, create_tx
from notaria.forms.wallet import send_form

bp = Blueprint('wallet', __name__, url_prefix='/wallet')

@bp.route('/')
@login_required
def index():
    privkey, address = get_keychain(session['user'])
    unspent = get_unspent(address)

    return render_template('admin.html', address=address, unspent=unspent)

@bp.route("/send", methods=['GET', 'POST'])
@login_required
def send():
    form = send_form(request.form)
    if form.validate_on_submit():
    	tx = create_tx(session['user'], form, 'hola')
    	flash(tx)

    return render_template('send.html', form=form)