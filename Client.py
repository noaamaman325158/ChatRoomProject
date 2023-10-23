import socket

MAX_SIZE_MESSAGE = 1024
host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect the server to the client
sock.connect((host, port))

#1024 bytes should be enough for message
message = sock.recv(MAX_SIZE_MESSAGE)

while message:
    print("Message: ", message.decode())
    message = sock.recv(MAX_SIZE_MESSAGE)


sock.close()
