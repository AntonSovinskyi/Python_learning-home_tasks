"""Create a server and client, which will use user datagram protocol (UDP) for communication."""


import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter message: ')
        if message == 'exit':
            break
        s.sendto(message.encode('ascii'), (HOST, PORT))

