#CHARGE POINT

import json
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name

host=socket.gethostname()
port = 8009

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
msg = {"command":"BootNotificationPayload","Payload":{'charge_point_model': 'Optimus', 'charge_point_vendor': 'The Mobility', 'charge_box_serial_number': None, 'charge_point_serial_number': None, 'firmware_version': None, 'iccid': None, 'imsi': None, 'meter_serial_number': None, 'meter_type': None}
}
a=json.dumps(msg)
s.sendall(bytes(a,encoding="utf-8"))



message = s.recv(1024)
print(message.decode())






s.close()


        