import socket
import hashlib
from Crypto import Random
import Crypto.Cipher.AES as AES


hostname = 'localhost'


def padding(s):
    return s + ((16 - len(s) % 16) * '`')


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
        en = AESKey.encrypt(padding(self.hash))
        client_socket.sendall(en.encode())

    def compare(self, other_hash):
        if self.hash == other_hash:
            return True
        return False

