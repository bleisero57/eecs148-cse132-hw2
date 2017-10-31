import socket
import sys
import os

if len(sys.argv) != 4:
    print("USASGE: http_client.py [server host] [server port] [file name]")
    host = input("Enter host: ")
    port = input("Enter port: ")
    filename = input("Enter filename: ")
else:
    host = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]

port = int(port)

if filename[-5:].lower() == ".html":
    req = "GET {}{} HTTP/1.1".format(os.path.sep, filename)
else:
    req = "GET {}{}.html HTTP/1.1".format(os.path.sep, filename)
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print("\tConnecting to {}:{}".format(host, port))
sock.send(req.encode())
print("\tSending request:\n{}\n".format(req))
recv = str(sock.recv(1024), "utf-8")
print("\tRevieved:\n{}".format(recv))
sock.close()
