from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.functions.wallet import get_keychain, get_unspent

bp = Blueprint('wallet', __name__, url_prefix='/wallet')

@bp.route('/')
@login_required
def index():
    privkey, address = get_keychain(session['user'])
    unspent = get_unspent(address)

    return render_template('admin.html', address=address, unspent=unspent)
