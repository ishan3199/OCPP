#backend verification

import json
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name

host = socket.gethostname()
port = 8004

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
msg = {"command": "SendBootNotification"}
a = json.dumps(msg)
s.sendall(bytes(a, encoding="utf-8"))

message = s.recv(1024)
b = json.loads(message.decode('utf-8'))
c=json.loads(b[0])

if c['Payload']['charge_point_model'] =='Optimus' and c['Payload']['charge_point_vendor'] == 'The Mobility':
    msg2 = {"command": "BootNotificationResponse",
           "data": {'status':'Accepted'}}


    a3 = json.dumps(msg2)
    s.sendall(bytes(a3, encoding="utf-8"))
    print(a3)

else:
    msg3 = {"command": "BootNotificationResponse",
            "data": {'status': 'Rejected'}}
    a4 = json.dumps(msg3)
    s.sendall(bytes(a4, encoding="utf-8"))
    print(a4)


s.close()


