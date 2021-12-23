# ---------------------------------------------------------------------------- #
#   PROGRAM: http_server.py
#   OVERVIEW: Creates a TCP/IP socket server in PYTHON3
#         This program creates a remote host to send and receive data
#
#   AUTHOR: Christopher Dueber
#     DATE: AUGUST 1 2021
# ---------------------------------------------------------------------------- #

# HTTP Server example in python
# Command to run: python3 http_server.py

# Library import
import socket
import sys
import select

# Thread module
from _thread import *


# Accepts IP through a specific port
host = ''
port = 1234

# Create a TCP/IP socket
# INET creates IPv4 socket
# STREAM creates a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allows sockets to reuse address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# Attempts to bind socket to IP address and port number with error handling
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

# sServer listens for incoming requests with a queue of 5
s.listen(5)
print('Waiting for client request. . . ')

# Socket handling
clientList = []




# Error handling for IP / Port
#if len(sys.argv) != 2:
#    print('Critical error: IP or port not received')
#    exit()

# Manage received message
#def receive_message(s):
#    try:
#        message_header = s.recv(pName_len)
#        if not len(pName_len):
#            print('Name too long, choose name < 10 characters')
#            return False
#
#        message_len = int(message_header.decode('utf-8').strip())
#        return {'header': message_header, 'data': s.recv(message_len)}
#    except Exception as e:
#        raise


# Thread function using Python's Stardard Encodings (UTF-8) encode() for conversion between text and bytes
# I found this method on the BindaryTides help page
def threaded_client(conn):
    conn.send('Connecting, please wait . . .')

    # While TCP connection is established, accept individual requests from client and return message
    while True:
        try:
            message = conn.recv(4096)
            if message:
                print (message)
                #message_to_send = message
                #broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(messsage, conn):
    for clients in clientList:
        if clients != conn:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(conn):
    if conn in clientList:
        clientList.remove(conn)

while True:
    conn, addr = s.accept()
    clientList.append(conn)

    start_new_thread(threaded_client,(conn,))


conn.close()
s.close()


        #conn, addr = s.accept()
        #print('Welcome to Hangman server! ')

        # 2nd tuple intentionally left empty
        #start_new_thread(threaded_client,(conn,))

# Server message send function  #
# conn.send(str.encode(reply))
