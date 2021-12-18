# ---------------------------------------------------------------------------- #
#   PROGRAM: http_server.py
#   OVERVIEW: Creates a TCP/IP socket server in PYTHON3
#         This program creates a remote host to send a receive  data
#
#   AUTHOR: Christopher Dueber
#     DATE: JULY 18 2021
# ---------------------------------------------------------------------------- #

# Command to run: python3 http_server.py

# Library import
import socket
import sys

# Thread module
from _thread import *

# Accepts IP through a specific port
host = ''
port = 1234

# Create a TCP/IP socket
# INET creates IPv4 socket
# STREAM creates a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempts to bind socket to IP address and port number with error handling
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

# sServer listens for incoming requests with a queue of 5
s.listen(5)
print('Waiting for client request. . . ')

# HTML data by request
data = "HTTP/1.1 200 OK\r\n"\
"Content-Type: text/html; charset=UTF-8\r\n\r\n"\
"<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

# Thread function using Python's Stardard Encodings (UTF-8) encode() for conversion between text and bytes
# I found this method on the BindaryTides help page
def threaded_client(conn):
    conn.send(str.encode(data))

# While TCP connection is established, accept individual requests from client and return message
while True:
    conn, addr = s.accept()
    print('Request received, message sent to client. ')

    # 2nd tuple intentionally left empty
    start_new_thread(threaded_client,(conn,))
