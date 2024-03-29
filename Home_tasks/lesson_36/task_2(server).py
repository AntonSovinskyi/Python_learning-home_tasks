"""Extend the echo server, which returns to client the data,
encrypted using the Caesar cipher algorithm by a specific key
obtained from the client.

"""


import socket
from Cesar_cipher import Cesar_cipher

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('Starting up on {} port {}.'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('Connection from ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(2048).decode('ascii')
            print(f'Received {data}')
            print('Coding...')
            if data:
                print('Sending coded data back to the client.')
                connection.sendall(Cesar_cipher(data).encode('ascii'))
            else:
                print('No data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
