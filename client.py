import socket
import sys
import ssl
import hashlib

hostname = 'localhost'


class Client:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash = ''

    def send_lines(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((hostname, 8000))
        # with context.wrap_socket(client_socket, server_hostname=hostname) as server_socket:
        f = open(self.file_path)
        sha256 = hashlib.sha256()
        length = 0

        for _ in range(10):
            line = f.readline()
            length += len(line)
            if not line:
                break
            sha256.update(line.encode())

        self.hash = sha256.hexdigest()
        client_socket.sendall(self.hash.encode())

    def compare(self, other_hash):
        if self.hash == other_hash:
            return True
        return False


def fetch_data(directory):
    # grab data from specific directory
    fetch = f.get(directory, None).encode("utf-8")
    return fetch
