from notaria.models.users import user_model
from flask import current_app as app
from notaria.functions.crypto import sha3_hex
from notaria import db


def validate_user(form):
    username = form.user.data.lower().strip()
    passwd = form.passwd.data.lower().strip()

    user = user_model.query.filter_by(username=username).first()
    salted_pwd = sha3_hex(passwd + app.config['SECRET_KEY'])

    if not user:
        return None
    elif username == user.username and salted_pwd == user.passwd:
        return True
    else:
        return False


def register_user(form):
    username = form.user.data.lower().strip()
    email = form.email.data.lower().strip()
    passwd = sha3_hex(form.passwd.data + app.config['SECRET_KEY'])

    if validate_user(form) == None:
        user = user_model(username=username, passwd=passwd, email=email)
        db.session.add(user)
        db.session.commit()

        return True
    else:
        return False
