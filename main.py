from client import Client

alice = Client('Lab3Grading.txt')
alice.send_lines()

bob = Client('Lab3Grading.txt')
bob.send_lines()
