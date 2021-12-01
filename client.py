import socket
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes


class Client:
    def __init__(self, file_path, public_key):
        self.file_path = file_path
        self.public_key = public_key
        self.hash = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8000))

    def send_lines(self):
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

        # Encrypt the hash
        recipient_key = RSA.import_key(open(self.public_key).read())
        session_key = get_random_bytes(16)

        # Encrypt session key with the public key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        print(len(enc_session_key))

        # Encrypt plaintext with the session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(self.hash.encode())

        self.socket.sendall(enc_session_key)
        self.socket.sendall(cipher_aes.nonce)
        self.socket.sendall(tag)
        self.socket.sendall(ciphertext)

    def compare(self, other_hash):
        if self.hash == other_hash:
            return 1
        return 0
