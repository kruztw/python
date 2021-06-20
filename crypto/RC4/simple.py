# coding: utf-8
 
import binascii
 
 
def encrypt(PlainBytes:bytes, KeyBytes:bytes) -> str:
    keystreamList = []
    cipherList = []
 
    keyLen = len(KeyBytes)
    plainLen = len(PlainBytes)
    s_box = list(range(256))
 
    j = 0
    for i in range(256):
        j = (j + s_box[i] + KeyBytes[i % keyLen]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
 
    i = 0
    j = 0
    for m in range(plainLen):
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]
        cipherList.append(k ^ PlainBytes[m])
 
    result_hexstr = ''.join(['%02x' % i for i in cipherList])
    return result_hexstr.upper()

 
def decrypt(Cipher:bytes, KeyBytes:bytes) -> str:
    s_box = list(range(256))

    j = 0
    out = []

    #KSA Phase
    for i in range(256):
        j = (j + s_box[i] + key[i % len(key)] ) % 256
        s_box[i] , s_box[j] = s_box[j] , s_box[i]

    #PRGA Phase
    i = j = 0
    for char in Cipher:
        i = ( i + 1 ) % 256
        j = ( j + s_box[i] ) % 256
        s_box[i] , s_box[j] = s_box[j] , s_box[i]
        out.append(chr(char ^ s_box[(s_box[i] + s_box[j]) % 256]))

    return ''.join(out)

 
if __name__ == "__main__":
    data = binascii.a2b_hex(binascii.hexlify(b'hello RC4'))
    key = binascii.a2b_hex(binascii.hexlify(b'secret key'))
    
    cipher = encrypt(data, key)
    print("cipher: ", cipher)

    plain = decrypt(binascii.a2b_hex(cipher), key)
    print("plain: ", plain)
