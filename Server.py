import socket

#Details about the socket connection between clients and server
host = 'localhost'
port = 8080

#Create Socket obejct
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bidn the server details
sock.bind((host, port))

sock.listen(1)
print("The server is running and listening to client request: ")
#accept some details about the client
conn, address = sock.accept()

message = "Hey there!"

conn.send(message.encode())

conn.close()

