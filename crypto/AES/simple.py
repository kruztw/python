#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


message = pad(b"flag{AES_CBC_MODE_IS_LIKE_ECB_MODE_IF_PREVIOUS_OUTPUT_IS_FIXED}", 16)
key = pad(b"very_secret_key", 16)
IV = pad(b'very_secret_IV', 16)

def encrypt(plain):
    aes = AES.new(key, AES.MODE_CBC, IV)
    return aes.encrypt(plain)

def decrypt(cipher):
    aes = AES.new(key, AES.MODE_CBC, IV)
    return aes.decrypt(cipher)


cipher = encrypt(message)
plain = decrypt(cipher) 

print(cipher.hex())
print(plain)
