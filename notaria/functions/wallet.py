from notaria.models.users import user_model
from notaria.functions.crypto import sha3_hex
from flask import current_app as app
from requests import get
from bitcoin import privtoaddr, mktx

def get_keychain(username, n=0):
    user = user_model.query.filter_by(username=username).first()

    username = user.username
    email = user.email
    SECRET = app.config['SECRET_KEY']

    privkey = sha3_hex(username + SECRET + email)
    address = privtoaddr(privkey, 0x58)

    return [privkey, address]


def get_unspent(addr):
    unspent = get(app.config['INSIGHT'] + '/api/addr/' + addr + '/utxo').json()

    confirmed = unconfirmed = 0.0

    inputs = []
    for i in unspent:
        if i['confirmations'] >= 6 and i['amount'] >= 0.001:
            confirmed += i['amount']

            utxo = {}
            utxo['output'] = '%s:%i' % (i['txid'], i['vout'])
            utxo['value'] = i['satoshis']
            utxo['address'] = i['address']

            inputs.append(utxo)
        else:
            unconfirmed += i['amount']

    result = {}
    result['confirmed'] = '%.8f' % confirmed
    result['inputs'] = inputs
    result['unconfirmed'] = '%.8f' % unconfirmed

    return result

def create_tx(username, amount, receptor, op_return = ''):

    privkey, address = get_keychain(username)
    balance, inputs, _ = get_unspent(address)

    if not len(receptor) == 34 and not receptor.startswith('c'):
        return "Dirección inválida"

    elif amount > balance:
        return "Balance insuficiente"

    elif amount <= 0:
        return "Monto inválido"

    amount *= 1e8
    used_utxo = 0

    for utxo in inputs:
        used_utxo += utxo['value']
        if used_utxo >= amount:
            break

    output = []
    min_fee = (used_utxo - amount) - 0.001*1e8

    if min_fee >= 0:
        output.append({'address': receptor, 'value': amount})
        output.append({'address': address, 'value' : min_fee})

    elif min_fee == 0:
        output.append({'address': receptor, 'value': amount - 0.001*1e8})

    else:
        return "?????"

    tx = mktx(used_utxo, output)

    for i, _ in enumeratr(used_utxo):
        tx = sign(tx, i, privkey)

    return tx