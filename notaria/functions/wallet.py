from notaria.models.users import user_model
from notaria.functions.crypto import sha3_hex
from flask import current_app as app
from requests import get
from bitcoin import privtoaddr, mktx, sign

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

def create_tx(username, form, op_return = ''):

    privkey, address = get_keychain(username)
    unspent = get_unspent(address)

    inputs = unspent['inputs']
    
    balance = int(float(unspent['confirmed'])*1e8)
    amount = int(float(form.amount.data)*1e8)
    
    receptor = form.address.data

    if not len(receptor) == 34 and not receptor.startswith('c'):
        return "Dirección inválida"

    elif amount > balance:
        return "Balance insuficiente"

    elif amount <= 0:
        return "Monto inválido"

    used_utxo = 0
    used_inputs = []

    for utxo in inputs:
        used_utxo += utxo['value']
        used_inputs.append(utxo)

        if used_utxo >= amount:
            break

    output = []
    min_fee = (used_utxo - amount) - 100000

    if min_fee >= 0:
        output.append({'address': receptor, 'value': amount})
        output.append({'address': address, 'value' : min_fee})

    elif min_fee == 0:
        output.append({'address': receptor, 'value': amount - 100000})

    else:
        return "?????"

    print(used_inputs)
    print(output)
    tx = mktx(used_inputs, output)

    for i, _ in enumerate(used_inputs):
        tx = sign(tx, i, privkey)

    return tx