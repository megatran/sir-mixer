#!/usr/python
import sys
import socket
import os
import datetime

DEVICE_PORT = 7331
HOSTNAME = '54.152.117.238'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOSTNAME, DEVICE_PORT))
print('connected to server')
while True:
    data = client.recv(1)
    print(str(datetime.datetime.now()), ': received data:', data)
    os.system('./arduino.sh ' + str(data).replace('\'', ''))

