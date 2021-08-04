from scapy.all import *

# srp : send and recv p: layer3
response, not_response = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="127.0.0.1"), retry=1, timeout=2)

print("----------------- response --------------------")
print(response)

print("----------------- not response ----------------")
print(not_response[0])
print("src mac: ", not_response[0].hwsrc)
print("dst mac: ", not_response[0].hwdst)
print("type   : ", hex(not_response[0].ptype))
print("src ip: ", not_response[0].psrc)
print("dst ip: ", not_response[0].pdst)
