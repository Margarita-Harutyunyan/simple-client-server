


# echo-client.py

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        text = input('Enter a message you want to send to the server: ')
        if not text:
            break
        btext = text.encode()
        client_socket.sendall(btext)
        data = client_socket.recv(1024)
        print(f'Client received {data}')
