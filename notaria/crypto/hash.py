from hashlib import sha3_256
from notaria.models.users import userModel
from flask import current_app as app


def validate_user(form):
    username = form.user.data
    passwd = form.passwd.data

    user = userModel.query.filter_by(username=username).first()
    salted_pwd = sha3_hex(passwd + app.config['SECRET_KEY'])

    if not user:
        return None
    elif username == user.username and salted_pwd == user.passwd:
        return True
    else:
        return False


def sha3_hex(s):
    return sha3_256(s.encode('utf-8')).hexdigest()


def sha3_bin(s):
    return sha3_256(s.encode('utf-8')).digest()
