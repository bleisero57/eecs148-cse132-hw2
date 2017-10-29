import socket
import sys
import os

if len(sys.argv) < 4:
    print("USASGE: http_client.py [server host] [server port] [file name]")
    host = #todo: get server host from user
    port = #todo: get server port from user
else:
    host = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #todo
    # Send header
    #send seperator
    # Send message
    #send seperator

    rcv = str(sock.recv(1024), "utf-8")
    print("\tRevieved:\n{}".format(rcv))
finally:
    sock.close()
