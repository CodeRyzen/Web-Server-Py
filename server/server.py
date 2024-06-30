import socket

server = socket.socket()
server.bind(('127.0.0.1', 8000))
server.listen()
print("Server is running!")

while True:
    client_socket, add = server.accept()
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    content = "Hello World!".encode('utf-8')
    client_socket.send(HDRS.encode('utf-8') + content)
    client_socket.shutdown(socket.SHUT_WR)
