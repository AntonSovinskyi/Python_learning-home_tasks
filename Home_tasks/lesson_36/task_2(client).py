import socket

HOST = '127.0.0.1'  # The server's hostname or IP address 0.0.0.0
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter message: ')
        if message == 'exit':
            break
        s.sendall(message.encode('ascii'))
        data = s.recv(2048)
        print('Echo', repr(data))
