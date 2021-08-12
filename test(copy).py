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



msg2 = {"command": "SendAuthorizationdata"}
a2 = json.dumps(msg2)
s.sendall(bytes(a2, encoding="utf-8"))

message2 = s.recv(1024)
b2 = json.loads(message2.decode('utf-8'))
if len(b2) == 1:
    c2=json.loads(b2[0])
    if c2['Payload']['idTag'] == 'hello123':
        msg3 = {"command": "AuthorizationResponse",
                "data": {'status': 'Accepted'}}

        a4 = json.dumps(msg3)
        s.sendall(bytes(a4, encoding="utf-8"))
        print(a4)

    else:
        msg5 = {"command": "AuthorizationResponse",
                "data": {'status': 'Rejected'}}
        a5 = json.dumps(msg5)
        s.sendall(bytes(a5, encoding="utf-8"))
        print(a5)


else:
    c3=b2[1]
    print("Recieving Boot Notification from CP")
    print(c3)
    if c3['command'] == 'BootNotificationPayload':
        if c3['Payload']['charge_point_model'] == 'Optimus' and c3['Payload']['charge_point_vendor'] == 'The Mobility':
            msg3 = {"command": "BootNotificationResponse","data": {'status':'Accepted'}}
            a5 = json.dumps(msg3)
            s.sendall(bytes(a5, encoding="utf-8"))

        else:
            msg3 = {"command": "BootNotificationResponse", "data": {'status': 'Rejected'}}
            a6 = json.dumps(msg3)
            s.sendall(bytes(a6, encoding="utf-8"))





s.close()


