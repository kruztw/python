m = b'aa'
m_hex = m.hex()
m = bytes.fromhex(m_hex)
print(m_hex, type(m_hex))
print(m)
