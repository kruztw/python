from scapy.all import *

data='hello,word!'
pkt=IP(src='127.0.0.1',dst='127.0.0.1')/TCP(sport=8787,dport=8888)/data
send(pkt,inter=1,count=2) 

send(IP(dst="127.0.0.1")/UDP(dport=53))                # layer3
sendp(Ether()/IP(dst="127.0.0.1")/UDP(dport=53))       # layer2

