from Crypto.Util.number import getPrime,inverse,long_to_bytes,bytes_to_long
from Crypto.PublicKey import RSA
from binascii import hexlify, unhexlify

flag = "shellctf{something_here}"

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = inverse(e,phi)

encrypted_flag = pow(bytes_to_long(flag.encode()),e,n)
decrypted_flag = long_to_bytes(pow(encrypted_flag,d,n)).decode()

assert decrypted_flag == flag 
with open('pubkey.pem', 'w') as pub:
    pub.write(RSA.construct((n,e)).publickey().exportKey().decode())

with open('privkey.pem', 'w') as priv:
    priv.write(RSA.construct((n, e, d)).exportKey().decode())

# 用 openssl 無法解密, 到時看到例子再來補
#with open('flag.enc', 'wb') as f:
#    encrypted_flag = hex(encrypted_flag)[2:]
#    encrypted_flag = '0'*(len(encrypted_flag)%2) + encrypted_flag 
#    f.write(unhexlify(encrypted_flag))
