from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8001))

msg = input("Message: ")

msg_bytes = str.encode(msg)
client_socket.send(msg_bytes)

server_msg_bytes = client_socket.recv(1024)
server_msg = server_msg_bytes.decode('utf-8')

print(server_msg)
