import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    connection, address = server_socket.accept()

    with connection:
        print(f'Connected to {address}')
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f'Server received this data: {data!r}')
            connection.sendall(data)

print('Server closed')
