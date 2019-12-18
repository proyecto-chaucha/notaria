from notaria import chaucha
from notaria.models.users import user_model
from flask import current_app as app

def get_address(username):
    user = user_model.query.filter_by(username=username).first()

    username = user.username
    email = user.email
    SECRET_KEY = app.config['SECRET_KEY']

    key = chaucha.keys.bip32_seed((username + email + SECRET_KEY).encode())

    return [key.subkey_for_path('0/%i/0' % n).address() for n in range(20)] 