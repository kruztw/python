# code: https://ctftime.org/writeup/27932

from wincrypto import CryptCreateHash, CryptHashData, CryptDeriveKey, CryptEncrypt, CryptDecrypt
from wincrypto.constants import CALG_SHA_256, CALG_AES_128, bType_SIMPLEBLOB


def decrypt(cipher):
    key = b"secret_key"
    sha256_hasher = CryptCreateHash(CALG_SHA_256)
    CryptHashData(sha256_hasher, key)
    aes_key = CryptDeriveKey(sha256_hasher, CALG_AES_128)
    decrypted_data = CryptDecrypt(aes_key, cipher)
    return decrypted_data

def encrypt(plain_text):
    key = b"secret_key"
    sha256_hasher = CryptCreateHash(CALG_SHA_256)
    CryptHashData(sha256_hasher, key)
    aes_key = CryptDeriveKey(sha256_hasher, CALG_AES_128)
    encrypted_data = CryptEncrypt(aes_key, plain_text)
    return encrypted_data



cipher = encrypt(b"hello world")
print(cipher, len(cipher))

plain = decrypt(cipher)
print(plain, len(plain))
