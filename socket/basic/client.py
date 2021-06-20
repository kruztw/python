#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = '127.0.0.1'
port = 8888

s.connect((host, port))

msg = s.recv(1024)
s.close()

print (msg.decode('utf-8'))

