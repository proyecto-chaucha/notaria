from notaria.models.users import user_model
from notaria.functions.crypto import sha3_hex
from flask import current_app as app
from requests import get
import bitcoin

def get_address(username, n=0):
    user = user_model.query.filter_by(username=username).first()

    username = user.username
    email = user.email
    SECRET = app.config['SECRET_KEY']

    privkey = sha3_hex(username + SECRET + email)
    return bitcoin.privtoaddr(privkey, 0x58)


def get_unspent(addr):
    unspent = get(app.config['INSIGHT'] + '/api/addr/' + addr + '/utxo').json()

    confirmed = unconfirmed = 0.0

    inputs = []
    for i in unspent:
        if i['confirmations'] >= 6 and i['amount'] >= 0.001:
            confirmed += i['amount']
            inputs.append({
                'output': '%s:%i' % (i['txid'], i['vout']),
                'value': i['satoshis'],
                'address': i['address']
                })
        else:
            unconfirmed += i['amount']

    return {
            'confirmed' : '%.8f' % confirmed,
            'inputs' : inputs, 
            'unconfirmed' : '%.8f' % unconfirmed
            }