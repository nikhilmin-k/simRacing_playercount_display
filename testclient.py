#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50007        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_string = "{\"idA\": 244210, \"idB\": 365960, \"idC\": 284160, \"idD\": 1066890, \"idE\": 805550, \"idF\": 378860}"
    s.send(send_string.encode());
    data = s.recv(1024)

print('Received', repr(data))

