import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

username = input("Enter your username: ")

join_message = "JOIN " + username
client_socket.send(join_message.encode())


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\n" + message)
            else:
                break
        except:
            break


def send_messages():
    while True:

        message = input()

        if message == "/quit":
            client_socket.send("QUIT".encode())
            client_socket.close()
            break

        send_msg = "MSG " + message
        client_socket.send(send_msg.encode())


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_messages()