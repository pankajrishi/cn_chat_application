# CN_Chat_Application

## Overview

This project implements a **multi-client chat application** using **TCP socket programming in Python**.
The system consists of a **central server** and multiple **clients** that connect to the server to exchange messages in real time.

The server manages all client connections and broadcasts messages to every connected user.
Clients can join the chat using a username, send messages, receive messages from other users, and exit the chat using a command.

This project demonstrates practical concepts of:

* Client–Server architecture
* TCP socket communication
* Multi-threading for handling multiple clients
* Simple application-layer protocol design
* Real-time messaging

---

## Features

* Multiple clients can connect to the server simultaneously
* Messages from one client are broadcast to all other clients
* Users are notified when someone joins or leaves the chat
* Clients can exit using `/quit`
* Server handles unexpected client disconnections
* Uses **TCP sockets for reliable communication**

---

## Technologies Used

* Python 3
* Standard `socket` library
* `threading` module for concurrency

No external networking libraries are used.

---

## Project Structure

```
chat-app/
│
├── server.py      # Chat server
├── client.py      # Chat client
├── README.md      # Project documentation
└── Report.md      # Project report
```

---

## System Architecture

The system follows a **Client–Server architecture**.

### Server

The server is responsible for:

* Accepting incoming client connections
* Maintaining a list of connected clients
* Broadcasting messages to all clients
* Handling join and leave events
* Managing client threads

Each client connection is handled in a **separate thread**, allowing multiple users to communicate at the same time.

### Client

The client program:

* Connects to the server
* Allows the user to enter a username
* Sends messages typed by the user
* Receives messages from other users in real time
* Allows the user to exit using `/quit`

---

## Communication Protocol

A simple **text-based protocol** is used between the client and server.

### Commands

| Command           | Description                      |
| ----------------- | -------------------------------- |
| JOIN `<username>` | Sent when a user joins the chat  |
| MSG `<message>`   | Sent when a user sends a message |
| QUIT              | Sent when a user leaves the chat |

### Example Messages

```
JOIN Alice
MSG Hello everyone
QUIT
```

---

## Concurrency

The server supports multiple clients using **multi-threading**.

When a client connects:

1. The server accepts the connection
2. A new thread is created
3. The thread continuously listens for messages from that client

This allows the server to support **10 or more clients simultaneously**.

---

## How to Run the Application

### Step 1: Start the Server

Open a terminal and run:

```
python server.py
```

You should see:

```
Chat server started...
Waiting for connections...
```

---

### Step 2: Start Clients

Open multiple terminals and run:

```
python client.py
```

Each client will be prompted to enter a username.

Example:

```
Enter your username: Pankaj
```

---

### Example Chat

Client 1:

```
Enter your username: Pankaj
Hello everyone
```

Client 2:

```
Enter your username: Nikhil
Pankaj joined the chat
Pankaj: Hello everyone
```

Client 2 sends:

```
Hi Pankaj
```

Client 1 sees:

```
Nikhil: Hi Pankaj
```

---

## Leaving the Chat

To exit the chat, type:

```
/quit
```

The server will notify other users that the client has left the chat.

Example:

```
Pankaj left the chat
```

---

## Testing

The application was tested with the following scenarios:

* Multiple clients connecting to the server
* Simultaneous message sending
* Client leaving using `/quit`
* Client disconnecting unexpectedly
* Long and short messages

The server remained stable during all tests.

---

## Limitations

* Messages are not stored permanently
* No graphical interface (terminal-based chat)
* Server must be running before clients connect

---

## Possible Improvements

Future improvements could include:

* Message timestamps
* Persistent chat history
* List of active users
* Private messaging
* GUI interface

---

## Conclusion

This project demonstrates the implementation of a basic **real-time chat system** using TCP socket programming.
It helped in understanding networking concepts such as **client–server communication, threading, and protocol design**.

---

## Author

Pankaj Rishi
