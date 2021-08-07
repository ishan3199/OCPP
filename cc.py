# CENTRAL SYSTEM

import socket
import select
import time
import ast
from datetime import datetime
import json

servers = []
portlist=[8004,8009] # 8004 for php 8009 for chargepoint
k=[]
i=0
var1=0
s=0
username='user'
password='abc'
chargepoint_id="test_cp2"

host = socket.gethostname()


print(socket.gethostbyname(host))

for port in portlist:
    ds = ("0.0.0.0", port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ds)
    server.listen(1)

    servers.append(server)

while True:
    # Wait for any of the listening servers to get a client
    # connection attempt
    readable,_,_ = select.select(servers, [], [])
    ready_server = readable[0]

    connection, address = ready_server.accept()
    if ready_server.getsockname()[1] == 8004:
        print("New connection made from backend!")
    else:
        print("New connection made from Chargepoint!")

    if ready_server.getsockname()[1] == 8004:

        message = connection.recv(1024)
        print(json.loads(message.decode('utf-8')))  # Gets the incomming message
        a = json.loads(message.decode('utf-8'))
        if a['command'] == 'AUTH':
            if a['data']['username'] == username and a['data']['password'] == password:
                msg = {"command": "AUTH-RESPONSE", "data": {"STATUS": "Accepted"}}
                f = json.dumps(msg)
                connection.sendall(bytes(f, encoding="utf-8"))

            else:

                msg = {"command": "AUTH-RESPONSE", "data": {"STATUS": "Rejected"}}
                e = json.dumps(msg)
                connection.sendall(bytes(e, encoding="utf-8"))

        elif a['command'] == 'AUTH-CHARGER':
            if a['data']['charge_point_id'] == chargepoint_id:
                msg1 = {"id_tag_info": {"status": 'Accepted'}}
                f1 = json.dumps(msg1)
                connection.sendall(bytes(f1, encoding="utf-8"))
            else:
                msg1 = {"id_tag_info": {"status": 'Rejected'}}
                f2 = json.dumps(msg1)
                connection.sendall(bytes(f2, encoding="utf-8"))


        elif a['command'] == 'SendBootNotification':
            print(k)

            var2=json.dumps(k)
            connection.sendall(bytes(var2, encoding="utf-8"))
            boot=connection.recv(1024)
            ad = json.loads(boot.decode('utf-8'))
            print(ad)
            if ad['data']['status'] == 'Accepted':
                approval = '2'
                var1 = '1'
            else:
                var1 = '1'
                approval = '3'




        else:
            pass

    else:
        pass






    if ready_server.getsockname()[1] == 8009:



        if i == 0:

            message2 = connection.recv(1024)
            print(json.loads(message2.decode('utf-8')))  # Gets the incomming message
            a = json.loads(message2.decode('utf-8'))
            msg2 = a
            f3 = json.dumps(msg2)
            k.append(f3)
            var1='3'

        if i == 1:

            if var1 == '1':

                if approval=='2':
                    msg4 = {"BootNotificationConf": {"CurrentTime": datetime.utcnow().isoformat(),"interval": 10,"status": 'Accepted'}}
                    f4 = json.dumps(msg4)
                    connection.sendall(bytes(f4, encoding="utf-8"))


                elif approval == '3':
                    msg4 = {"BootNotificationConf": {"CurrentTime": datetime.utcnow().isoformat(), "interval": 10,
                                                "status": 'Rejected'}}
                    f4 = json.dumps(msg4)
                    connection.sendall(bytes(f4, encoding="utf-8"))

        i=i+1

    else:
        message4="Waiting for server"
        connection.send(message4.encode('ascii'))







connection.close()



    # Might want to spawn thread here to handle connection,
    # if it is long-lived