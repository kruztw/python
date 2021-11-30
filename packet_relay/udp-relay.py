#!/usr/bin/env python

# code: https://github.com/Pynard/writeups/blob/main/2021/RARCTF/challenges/rarpg.md
# Super simple script that listens to a local UDP port and relays all packets to an arbitrary remote host.
# Packets that the host sends back will also be relayed to the local UDP client.
# Works with Python 2 and 3

# writeup: https://ctftime.org/writeup/29753

import sys, socket
import parser
import importlib

# Whether or not to print the IP address and port of each packet received
debug=True

if len(sys.argv) != 2 or len(sys.argv[1].split(':')) != 3:
    print('Usage: udp-relay.py localPort:remoteHost:remotePort')
    exit(-1)

localPort, remoteHost, remotePort = sys.argv[1].split(':')

localPort = int(localPort)
remotePort = int(remotePort)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', localPort))

knownClient = None
knownServer = (remoteHost, remotePort)

sys.stdout.write('All set, listening on '+str(localPort)+'.\n')
while True:
    importlib.reload(parser)
    data, addr = s.recvfrom(32768)
    if knownClient is None or addr != knownServer:
        if debug:
            print("")
        knownClient = addr

    if debug:
        print("Packet received from "+str(addr))

    if addr == knownClient:
        if debug:
            print("\tforwording tO "+str(knownServer)) 

        s.sendto(parser.parse(data,True), knownServer)
    else:
        if debug:
            print("\tforwarding to "+str(knownClient))
        s.sendto(parser.parse(data,False), knownClient)
