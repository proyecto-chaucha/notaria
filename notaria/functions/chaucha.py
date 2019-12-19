from notaria.models.users import user_model
from flask import current_app as app
import bitcoin

def get_address(username):
    user = user_model.query.filter_by(username=username).first()

    username = user.username
    email = user.email
    SECRET = app.config['SECRET_KEY']

    master = bitcoin.bip32_master_key((username +  SECRET + email).encode())

    addrs = []

    for i in range(10):
        child = bitcoin.bip32_ckd(master, i)
        addr = bitcoin.bip32_extract_key(child)
        addrs.append(bitcoin.privtoaddr(addr, 0x58))

    return addrs