# for php backend server communication

import socket

host = socket.gethostname()
listensocket = socket.socket() #Creates an instance of socket
Port = 8007 #Port to host server on

IP = socket.gethostname() #IP address of local machine


listensocket.connect((host , Port))

#Starts serve

#Accepts the incomming connection



message = listensocket.recv(1024)
# First recieve message from client
print(message.decode())



# now send message to server



listensocket.close()