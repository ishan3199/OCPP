# SERVER FOR RASPBERRY PI


import socket
import json
import time
import ast

username='user'
password='abc'

chargepoint_id="test_cp2"

host = socket.gethostname()
print(socket.gethostbyname(host))

listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an instance of socket
Port = 8002 #Port to host server on
maxConnections = 999


listensocket.bind(('',Port))


listensocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates an instance of socket
Port2 = 8003 #Port to host server on
maxConnections2 = 999

listensocket2.bind(('',Port2))

listensocket2.listen(maxConnections2)
print("Server started at " + host + " on port " + str(Port2))


#Starts server
listensocket.listen(maxConnections)
print("Server started at " + host + " on port " + str(Port))

while True:

#Accepts the incomming connection
    (clientsocket, address) = listensocket.accept()
    print("New connection made!")


    message = clientsocket.recv(1024)
    print(json.loads(message.decode('utf-8')))# Gets the incomming message
    a=json.loads(message.decode('utf-8'))
    if a['command']=='AUTH':
        if a['data']['username'] == username and a['data']['password'] == password:
            msg = {"command": "AUTH-RESPONSE", "data": {"STATUS":"Accepted"}}
            f = json.dumps(msg)
            clientsocket.sendall(bytes(f, encoding="utf-8"))

        else:

            msg = {"command": "AUTH-RESPONSE", "data": {"STATUS": "Rejected"}}
            e = json.dumps(msg)
            clientsocket.sendall(bytes(e, encoding="utf-8"))

    elif a['command']=='AUTH-CHARGER':
        if a['data']['charge_point_id'] == chargepoint_id:
            msg1 = {"id_tag_info": {"status":'Accepted'}}
            f1 = json.dumps(msg1)
            clientsocket.sendall(bytes(f1, encoding="utf-8"))
        else:
            msg1= {"id_tag_info": {"status":'Rejected'}}
            f2 = json.dumps(msg1)
            clientsocket.sendall(bytes(f2, encoding="utf-8"))





    else:
        pass


while True:

    (clientsocket2, address2) = listensocket2.accept()
    print("Boot Notification recieved")
    message3 = clientsocket2.recv(1024)
    print(json.loads(message3.decode('utf-8')))# Gets the incomming message
    a3=json.loads(message3.decode('utf-8'))


listensocket2.close()



listensocket.close()
