from flask import Blueprint, render_template, session, redirect, url_for, request, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.functions.wallet import get_address, get_unspent

bp = Blueprint('wallet', __name__, url_prefix='/wallet')

@bp.route('/')
def home():
    hello = "Wallet blueprint"
    return render_template('index.html', hello=hello)
