import sys
import socket


def server():
    # Creating the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)

    # Process first request
    client_socket1, address1 = server_socket.accept()
    message1 = client_socket1.recv(2048)


    # Process second request
    client_socket2, address2 = server_socket.accept()
    message2 = client_socket2.recv(2048)

    server_socket.sendto(message1, address2)
    server_socket.sendto(message2, address1)


if __name__ == "__main__":
    server()
