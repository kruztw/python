val = b'ABC'

int_val = int.from_bytes(val, byteorder='little')
print(int_val, type(int_val), hex(int_val))

byte_val = int_val.to_bytes(len(hex(int_val)[2:])//2, byteorder='little')
print(byte_val, type(byte_val))

