from scapy.all import *
 
r = rdpcap("dnscap.pcap")
 
for i in range(0,len(r)):
    print(r[i][DNSQR])
