import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = []
usernames = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Chat server started...")
print("Waiting for connections...")

# function to send message to all clients
def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                if client in clients:
                    clients.remove(client)


def handle_client(client_socket):

    username = ""

    try:
        while True:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            parts = message.split(" ", 1)
            command = parts[0]

            if command == "JOIN":
                username = parts[1].strip()
                usernames[client_socket] = username

                join_msg = username + " joined the chat"
                print(join_msg)

                broadcast(join_msg, client_socket)

            elif command == "MSG":
                text = parts[1]
                full_message = usernames[client_socket] + ": " + text
                print(full_message)

                broadcast(full_message, client_socket)

            elif command == "QUIT":
                break

    except:
        pass

    if client_socket in clients:
        clients.remove(client_socket)

    if client_socket in usernames:
        username = usernames[client_socket]
        leave_msg = username + " left the chat"
        print(leave_msg)

        broadcast(leave_msg, client_socket)

        del usernames[client_socket]

    client_socket.close()


while True:

    client_socket, addr = server_socket.accept()
    print("Connected with", addr)

    clients.append(client_socket)

    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()