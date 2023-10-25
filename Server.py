import socket

from threading import Thread
from auxilary_data import NUM_CURCURRENCY_CLIENTS,MAX_SIZE_MESSAGE, PORT, HOST_IP


#Details about the socket connection between clients and server
host = HOST_IP
port = PORT

#Storage DS

#The key is the associated connection with the client and the value is the name of the client
clients = {}

#The key is the connection of the client and the value is the address of the client
addresses = {}


#Create Socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bidn the server details
sock.bind((host, port))

#Send Message to all the connected clients in out Chat Room
def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf-8") + msg)


def handle_clients(conn, address):
    name = conn.recv(MAX_SIZE_MESSAGE).decode()
    welcome = "Welcome "+ name + ". you can type #quit if you ever want to leave the Chat Room"
    conn.send(bytes(welcome, "utf-8"))
    msg = name + "Has recently Joined the Chat Room"
    broadcast(bytes(msg, "utf-8"))
    #Store the associated client data inside the Client Dictionary
    clients[conn] = name
    #This loop going to run as well as the clients are send messages to the server
    while True:
        msg = conn.recv(MAX_SIZE_MESSAGE)
        #Check if the client type to quit
        if msg != bytes("#quit", "utf-8"):
            broadcast(msg, name + ":")
        else:
            conn.send(bytes("#quit", "utf-8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " Has Left the Chat Room"))





def accept_client_connections():
    #This loop going to run as well as the clients are send messages to the server
    while True:
        client_conn, client_address = sock.accept()
        #Welcome to process for the actual client
        print(client_address, "Has Connected")
        client_conn.send("Welcome to the chat room, Please type your name to continue".encode("utf-8"))
        #Store the data of the client inside our clients
        addresses[client_conn] = client_address
        Thread(target=handle_clients, args=(client_conn,client_address)).start()




if __name__ == '__main__':
    sock.listen(NUM_CURCURRENCY_CLIENTS)
    print("The server is running and listening to client requests...")

    #Thread will handle the concurrency-clients
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()