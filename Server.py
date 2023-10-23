import socket

NUM_CURCURRENCY_CLIENTS = 5
#Details about the socket connection between clients and server
host = '127.0.0.1'
port = 8080

#Storage DS
clients = {}
addresses = {}


#Create Socket obejct
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bidn the server details
sock.bind((host, port))


if __name__ == '__main__':
    sock.listen(NUM_CURCURRENCY_CLIENTS)
    print("The server is running and listening to client requests...")
