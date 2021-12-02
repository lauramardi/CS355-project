# CS355-project

Language used: Python
Libraries used: Crypto (PublicKey, Cipher, Random), hashlib, socket

Protocol specification: 
Communication: we have made use of socket programming, having a server which allows multiple client connections (maximum of 2), that will be both parties of the encryption: Alice and Bob. They will first send out their public key in order to be able to identify that they are indeed the ones transmitting the message. Then, they transmit encrypted parts of their file to the other party and check if the section they encrypted  is the same as the other party’s section of the file.
Protocol: We have both parties create a public key, and a private key which they send to the server, who is going to be in charge of verifying the signatures on the messages being sent, and decoding the actual messages.
As for encryption:
We have implemented hashing (Sha256) to prevent from sending the whole file. 
Encrypt the hashed content using RSA encryption with the session key and public key (using PKCS1_OAEP cipher), and the plaintext is encrypted with the session key (using AES encryption).
Send the encrypted message from both parties to the server, which decrypts them and checks that the decrypted contents are the same for both clients. Then the server sends a response to the clients saying whether it found a mismatch or they are indeed the same file.

Security analysis:
Security goal: Allow Alice and Bob to check that their respective password files are identical without any of the parties revealing to the other party the contents of their file. 
We can verify (from our code) that this goal is achieved. Both parties share encrypted versions of the hash of certain sections of their files to a common server that compares the content from the two parties and informs us if the files match or not. Since the parties can only launch passive attack, we can infer that the files will not be modified in transfer. So, we have achieved our security goal.
