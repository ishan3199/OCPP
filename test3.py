# for php backend server communication

import socket

host = socket.gethostname()
listensocket = socket.socket() #Creates an instance of socket
Port = 8004 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IP address of local machine


listensocket.connect((host , Port))

#Starts serve

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print(address)

message = clientsocket.recv(1024)
# First recieve message from client
print(type(message))



# now send message to server



listensocket.close()