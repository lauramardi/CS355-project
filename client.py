import socket
import ssl
import hashlib

hostname = 'localhost'
context = ssl.create_default_context()
global length


class Client:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash = ''

    def send_lines(self):
        with socket.create_connection((hostname, 8443)) as client_socket:
            with context.wrap_socket(client_socket, server_hostname=hostname) as server_socket:
                print(server_socket.version())
                f = open(self.file_path)
                sha256 = hashlib.sha256()
                global length
                length = 0

                for _ in range(10):
                    line = f.readlines()
                    length += len(line)
                    if not line:
                        break
                    sha256.update(line)

                self.hash = sha256.hexdigest()
                client_socket.sendall(self.hash.encode())

    def compare(self, other_hash):
        if self.hash == other_hash:
            return True
        return False
