import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP


def server():
    # Creating the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)

    # Process first request
    client_socket1, address1 = server_socket.accept()
    enc_session_key_1 = client_socket1.recv(256)
    nonce_1 = client_socket1.recv(16)
    tag_1 = client_socket1.recv(16)
    ciphertext_1 = client_socket1.recv(64)

    hash1 = decode_message(enc_session_key_1, nonce_1, tag_1, ciphertext_1)

    # Process second request
    client_socket2, address2 = server_socket.accept()
    enc_session_key_2 = client_socket2.recv(256)
    nonce_2 = client_socket2.recv(16)
    tag_2 = client_socket2.recv(16)
    ciphertext_2 = client_socket2.recv(64)

    hash2 = decode_message(enc_session_key_2, nonce_2, tag_2, ciphertext_2)

    if hash1 == hash2:
        print('Files are the same!')
    else:
        print('The files are not the same')


def decode_message(enc_session_key, nonce, tag, ciphertext):
    private_key = RSA.import_key(open("private.pem").read())

    # Decrypt the session key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data using the session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return data


if __name__ == "__main__":
    server()
