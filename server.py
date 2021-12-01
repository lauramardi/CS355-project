import sys
import socket


def server():
    # Creating the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)

    # Process first request
    client_socket, address = server_socket.accept()
    message = client_socket.recv(256)
    hash1 = message.decode()

    # Process second request
    client_socket, address = server_socket.accept()
    message = client_socket.recv(256)
    hash2 = message.decode()

    if hash1 == hash2:
        print('The files are the same')
    else:
        print('The files are not the same')


if __name__ == "__main__":
    server()
