from client import Client

alice = Client('Lab3Grading.txt', 'public.pem')
alice.send_lines()

bob = Client('Lab3Grading.txt', 'public.pem')
bob.send_lines()
