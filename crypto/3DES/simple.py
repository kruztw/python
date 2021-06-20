#!/usr/bin python3

from Crypto.Cipher import DES3

key = b'0000000000000002'
IV = b"00000000"
msg = "abc"

method = DES3.new(key, DES3.MODE_CFB, IV)
cipher = method.encrypt(msg.encode("utf-8"))

method = DES3.new(key, DES3.MODE_CFB, IV)
plain  = method.decrypt(cipher)

print(plain, cipher)
