from hashlib import sha3_256

digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def sha3_hex(s):
    return sha3_256(s.encode('utf-8')).hexdigest()


def sha3_bin(s):
    return sha3_256(s.encode('utf-8')).digest()


def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')


def check_addr(bc):
        # http://rosettacode.org/wiki/Bitcoin/address_validation#Python
    try:
        bcbytes = decode_base58(bc, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False
