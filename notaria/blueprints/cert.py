from flask import Blueprint, render_template, session, redirect, url_for, flash

from notaria.blueprints.restrictions import login_required, login_restricted
from notaria.functions.wallet import get_keychain, get_unspent, create_tx
from notaria.forms.cert import upload_form
from werkzeug.utils import secure_filename

bp = Blueprint('cert', __name__, url_prefix='/cert')


@bp.route('/')
@login_required
def index():
    return render_template('index.html')


@bp.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():

    form = upload_form()

    if form.validate_on_submit():
        filename = secure_filename(form.document.data.filename)
        content = form.document.data.stream.read()

        flash("%s (%.2f kb) subido exitosamente" % (filename, len(content)/1024))


    return render_template('upload.html', form=form)
