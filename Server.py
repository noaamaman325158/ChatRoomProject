import socket

from threading import Thread

NUM_CURCURRENCY_CLIENTS = 5
#Details about the socket connection between clients and server
host = '127.0.0.1'
port = 8080

#Storage DS
clients = {}

#The key is the connection of the client and the value is the address of the client
addresses = {}


#Create Socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bidn the server details
sock.bind((host, port))

def accept_client_connections():
    #This loop going to run as well as the clients are send messages to the server
    while True:
        client_conn, client_address = sock.accept()
        #Welcome to process for the actual client
        print(client_address, "Has Connected")
        client_conn.send("Welcome to the chat room, Please type your name to continue".encode("utf-8"))
        #Store the data of the client inside our clients
        addresses[client_conn] = client_address




if __name__ == '__main__':
    sock.listen(NUM_CURCURRENCY_CLIENTS)
    print("The server is running and listening to client requests...")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()