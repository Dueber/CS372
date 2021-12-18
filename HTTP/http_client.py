# ---------------------------------------------------------------------------- #
#  PROGRAM: http_client.py
# OVERVIEW: Creates a socket client in PYTHON3
#           This program creates a connection to a remote host to
#           receive a small amount of data
#
#   AUTHOR: Christopher Dueber
#     DATE: JULY 18 2021
# ---------------------------------------------------------------------------- #

# Command to run: python3 http_client.py

# Library import
import socket
import sys

# Create a TCP/IP socket
# INET creates IPv4 socket
# STREAM creates a TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Used to find IP address and assign it as host for socket connection
host = 'gaia.cs.umass.edu'

# Assign port to 80 for socket connection
port = 80

# Fetch IP address (IPv4 format) of host name, if connection fail exit socket creation
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    sys.exit()


# IF host IP is found, connect to listening server
# TODO: Try to use s.create_connection(addr, src)
s.connect((remote_ip, port))

print("Successful connection! \r\n")
print("Socket created: ", host + "\r\n" + "IP address: ", remote_ip + "\r\n")

# HTTP-compliant GET request to the server
message = b'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'

# Send GET request through TCP connection
s.send(message)

# Print message recieved from listening server (packets of 4096 bytes)
# Using Python's Stardard Encodings (UTF-8) decode() for conversion between bytes and text
print(s.recv(4096).decode())

# End TCP connection
s.close()
