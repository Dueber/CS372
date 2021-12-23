# ---------------------------------------------------------------------------- #
#  PROGRAM: http_client3.py
# OVERVIEW: Creates a socket client in PYTHON3
#           This program creates a connection to a http_server.py to
#           receive a small amount of data
#
#   AUTHOR: Christopher Dueber
#     DATE: JULY 18 2021
# ---------------------------------------------------------------------------- #

# Socket client example using PYTHON3
# Command to run: python3 http_client3.py

# Library import
import socket, sys, select

from _thread import *

recieveMode = False

# Create a TCP/IP socket
# INET creates IPv4 socket
# STREAM creates a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address
host = 'localhost'

# Port number
port = 1234

# Connect socket to host ip through designated port
s.connect((host, port))
print('Contacting server IP: ', host + '\r\n' + 'Port: ', port)

def _

def _userInput():
    name = input('Enter your username:')
    nameFlag == True
    return name


while True:
    packetSize = s.recv(4096)
    if not packetSize:
        break
    print(packetSize.decode())
