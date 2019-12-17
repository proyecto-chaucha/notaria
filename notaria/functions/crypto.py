from hashlib import sha3_256


def sha3_hex(s):
    return sha3_256(s.encode('utf-8')).hexdigest()


def sha3_bin(s):
    return sha3_256(s.encode('utf-8')).digest()
