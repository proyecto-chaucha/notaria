import bitcoin
from os import urandom

user = 'cesar'
email = 'cvxz@pm.me'
SECRET_KEY = urandom(32)

master_key = bitcoin.bip32_master_key((user + email).encode() + SECRET_KEY)
print(master_key)

for i in range(10):
    child = bitcoin.bip32_ckd(master_key, i)
    addr = bitcoin.bip32_extract_key(child)
    print(bitcoin.privtoaddr(addr, 0x58))
