from binascii import a2b_hex, b2a_hex

m = b'aaaa'

str_m = m.decode()
print(str_m, type(str_m))


bytes_m = str_m.encode()
print(bytes_m, type(bytes_m))

print(a2b_hex('61')) # == unhexlify
print(b2a_hex(b'a')) # == hexlify

