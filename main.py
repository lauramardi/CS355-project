from client import Client

alice = Client('bob.txt', 'public.pem')
alice.send_lines()

bob = Client('alice.txt', 'public.pem')
bob.send_lines()
