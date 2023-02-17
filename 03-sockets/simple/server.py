from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8001))

server_socket.listen()
print("Server started at post 8001")

received_msg = str.encode("Your message is received!")
while True:
    conn, addr = server_socket.accept()
    print(conn, addr)
    message_bytes = conn.recv(1024)
    message = message_bytes.decode('utf-8')
    print(message)
    conn.send(received_msg)


