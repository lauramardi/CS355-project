import ssl
import socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
    server_socket.bind(('127.0.0.1', 8443))
    server_socket.listen(5)
    with context.wrap_socket(server_socket, server_side=True) as client_socket:
        conn, addr = client_socket.accept()
