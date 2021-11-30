import ssl
import socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cacert.pem', 'private.key')


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
        server_socket.bind(('127.0.0.1', 8443))
        server_socket.listen(5)
        ssl_socket = ssl.wrap_socket(server_socket, keyfile='private.key', certfile='cacert.pem', server_side=True)
        while True:
            with context.wrap_socket(server_socket, server_side=True) as client_socket:
                conn, addr = client_socket.accept()
                # Read the hash sent by the client
                message = conn.recv(256).decode()
                print(message)
                break


if __name__ == "__main__":
    server()
