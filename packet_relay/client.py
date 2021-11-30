#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.sendto(b"connect", ("127.0.0.1", 8888))

msg, s_pair = s.recvfrom(1024)

atk_point = input()
if int(atk_point) > 10:
    print("Detected by anti-hacking system (Sometimes you can't patch the game, you need to implement MITM attack)")
    exit(-1)

s.sendto(b"attack: " + atk_point.encode(), s_pair)
