from socket import *
import rsa

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8001))
public_key, private_key = rsa.newkeys(512)

server_socket.listen()
print("Server started at post 8001")

received_msg = str.encode("Your message is received!")
while True:
    conn, addr = server_socket.accept()
    print(conn, addr)
    # send public key
    conn.send(public_key.save_pkcs1())
    message_bytes_encr = conn.recv(1024)
    # decrypt message
    message_bytes = rsa.decrypt(message_bytes_encr, private_key)
    message = message_bytes.decode('utf-8')
    print(message)
    conn.send(received_msg)


