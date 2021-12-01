from client import Client

alice = Client('Lab3Grading.txt', 'bob_public.pem', 'alice_private.pem')
print('Alices message')
alice.send_lines()

bob = Client('Lab3Grading.txt', 'alice_public.pem', 'bob_private.pem')
print('Bobs message')
bob.send_lines()
