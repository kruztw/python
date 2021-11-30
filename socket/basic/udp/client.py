#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.sendto(b"hello from client", ("127.0.0.1", 8888))
msg, s_pair = s.recvfrom(1024)
print(msg, s_pair)
