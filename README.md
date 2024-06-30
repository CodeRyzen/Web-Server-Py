# Web-Server-Py
This is a basic HTTP server written in Python using the socket library. The server listens on 127.0.0.1:8000 and responds with a "Hello World!" message to any incoming HTTP request.

# Requirements
Python 3.x

# How to Run
 - Clone the repository or download the script.
 - Open a terminal and navigate to the directory containing the script.
 - Run the script using Python:
  
   ```py
    python server.py
   ```
 - The server will start running and listening on 127.0.0.1:8000.

# How it Works
  - The server binds to the local IP address 127.0.0.1 and port 8000.
  - It listens for incoming connections.
  - When a connection is accepted, the server reads the incoming data (HTTP request).
  - It then sends back a simple HTTP response with a "Hello World!" message.
  - The server continues to run indefinitely, handling each incoming connection in a loop.

# Code Explanation
  ```py
  import socket

# Create a socket object
server = socket.socket()

# Bind the server to the local IP and port 8000
server.bind(('127.0.0.1', 8000))

# Listen for incoming connections
server.listen()
print("Server is running!")

# Main loop to handle incoming connections
while True:
    # Accept a connection
    client_socket, add = server.accept()
    
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    
    # HTTP response headers
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    
    # Response content
    content = "Hello World!".encode('utf-8')
    # Send the response headers and content
    client_socket.send(HDRS.encode('utf-8') + content)
    # Shutdown the connection
    client_socket.shutdown(socket.SHUT_WR)
  ```
