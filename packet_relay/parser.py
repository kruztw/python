import binascii

def parse(data,out):
    # print(data, out)
    if b"attack" in data:
        return b"attack: 1000000"

    return data
