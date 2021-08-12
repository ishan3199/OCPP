#CHARGE POINT

import json
import socket
import time

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name

host=socket.gethostname()
port = 8009

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes


msg2 = {"command":"AuthorizationPayload","Payload":{'idTag':'hello123'}
}
a1=json.dumps(msg2)
s.sendall(bytes(a1,encoding="utf-8"))

message2=s.recv(1024)
if message2 == b'{"AuthorizationConf": {"IdTagInfo": {"expiryDate": "NA", "parentIdTag": "NA", "status": "Accepted"}}}':





    msg23  = {"command":"BootNotificationPayload","Payload":{'charge_point_model': 'Optmus', 'charge_point_vendor': 'The Mobility', 'charge_box_serial_number': None, 'charge_point_serial_number': None, 'firmware_version': None, 'iccid': None, 'imsi': None, 'meter_serial_number': None, 'meter_type': None}

            }
    a3 = json.dumps(msg23)
    s.sendall(bytes(a3, encoding="utf-8"))
    print("ID tag Accepted... "
          "Boot Notification sent!!..")



else:
    msg23 = {"command": "Not Authorized"}

    a3 = json.dumps(msg23)
    s.sendall(bytes(a3, encoding="utf-8"))
    print("Not Authorized")




















s.close()


