#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host = '127.0.0.1'
port = 9999

s.bind((host, port))

while True:
    msg, s_pair = s.recvfrom(1024);
    if b"connect" in msg:
        print(f"recv connection from {s_pair}")
        s.sendto(b"attack point ?", s_pair)
    elif b"attack" in msg:
        print(f"recv: {msg}")
