import socket                                         

# create a socket object
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = '192.168.1.103'
port = 9999
# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    print(f"Started !")
    # establish a connection
    clientsocket,addr = serversocket.accept()      
    print(f"Got a connection from {addr}")
    print(f"received : {clientsocket.recv(1024)}")