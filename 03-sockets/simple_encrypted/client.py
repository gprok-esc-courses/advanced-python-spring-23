from socket import *

import rsa

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8001))

# receive server's public key
server_public_key_bytes = client_socket.recv(1024)
server_public_key = rsa.PublicKey.load_pkcs1(server_public_key_bytes, "PEM")
print(server_public_key)

msg = input("Message: ")

msg_bytes = str.encode(msg)
msg_bytes_encr = rsa.encrypt(msg_bytes, server_public_key)
client_socket.send(msg_bytes_encr)

server_msg_bytes = client_socket.recv(1024)
server_msg = server_msg_bytes.decode('utf-8')

print(server_msg)
