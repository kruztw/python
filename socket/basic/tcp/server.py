#!/usr/bin/python3

import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = '127.0.0.1'
port = 8888

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()      

    msg='Hello from server！'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
