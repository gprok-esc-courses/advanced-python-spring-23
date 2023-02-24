from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class Client:
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 8001))

        msg = input("Your Username: ")

        msg_bytes = str.encode(msg)
        self.client_socket.send(msg_bytes)
        th = Thread(target=self.send_message)
        th.start()

        while True:
            server_msg_bytes = self.client_socket.recv(1024)
            server_msg = server_msg_bytes.decode('utf-8')

            print(server_msg)

    def send_message(self):
        while True:
            msg = input("Type your message: ")
            self.client_socket.send(str.encode(msg))


if __name__ == '__main__':
    client = Client()
