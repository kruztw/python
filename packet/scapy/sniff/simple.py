from scapy.all import *

package = sniff(iface='wlo1', count=2, filter='tcp')
print(package[0].show())
#wrpcap("save.pcap",package)
