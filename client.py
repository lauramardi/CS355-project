import socket
import ssl
import hashlib

hostname = 'localhost'
context = ssl.create_default_context()
global length


def client(file_path):
    with socket.create_connection((hostname, 8443)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=hostname) as server_socket:
            print(server_socket.version())
            f = open(file_path)
            sha256 = hashlib.sha256()
            global length
            length = 0

            for _ in range(10):
                line = f.readlines()
                length += len(line)
                if not line:
                    break
                sha256.update(line)

            client_socket.sendall(sha256.hexdigest().encode())
