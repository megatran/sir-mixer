#!/use/bin/python

import threading
from threading import Thread
import time
import datetime
import socket
import sys

COMMAND_PORT = 1337
DEVICE_PORT = 7331
validDrinks = set()
validDrinks.add(1)
validDrinks.add(2)
validDrinks.add(3)

def CommandHandlerThread(commandSocket, deviceSocket):
    print("Running CommandHandlerThread")
    command = commandSocket.recv(1)
    deviceSocket.send(command)
    commandSocket.close()
    print(str(datetime.datetime.now()), ": sent command", command, "to the device, exiting command handling thread")
    return

def commandListeningServer(deviceSocket):
    # a server that listens for commands to make drinks
    commandSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    commandSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    commandSocket.bind((socket.gethostname(), COMMAND_PORT))
    commandSocket.listen(1)
    while True:
        (commandSocketInput, addr) = commandSocket.accept()
        print("Received connection, starting CommandHandlerThread")
        thread = Thread(target=CommandHandlerThread, args=(commandSocketInput, deviceSocket))
        thread.start()

# start listening for a device that will connect to this server that we can relay commands to
deviceServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
deviceServerSocket.bind((socket.gethostname(), DEVICE_PORT))
deviceServerSocket.listen(1)
(deviceSocket, addr) = deviceServerSocket.accept()
print("Accepted connection from a device with address", addr)

thread = Thread(target=commandListeningServer, args=(deviceSocket,))
thread.start()
