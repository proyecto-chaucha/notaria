from pycoin.networks.registry import network_for_netcode
from os import urandom

network = network_for_netcode("CHA")

user = 'cesar'
email = 'cvxz@pm.me'
SECRET_KEY = urandom(32)

key = network.keys.bip32_seed(user.encode() + SECRET_KEY + email.encode())
print(key.hwif(as_private=1))
print(key.hwif())

for i in range(12):
	path = "0/%i/5" % i
	addr = key.subkey_for_path(path)

	print(path)
	print(addr.wif())
	print(addr.address())