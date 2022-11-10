"""Create a server and client, which will use user datagram protocol (UDP) for communication."""


import socket

# Create a UDP socket
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Bind the socket to the port
    s.bind((HOST, PORT))

    while True:
        # Wait for a connection
        print('Waiting for a connection:')
        connection, client_address = s.recvfrom(1024)
        print(f"Received {connection}, from {client_address}")
