#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host = '127.0.0.1'
port = 8888

s.bind((host, port))

msg, s_pair = s.recvfrom(1024);
print(msg, s_pair)

s.sendto(b"hello from server", s_pair)
