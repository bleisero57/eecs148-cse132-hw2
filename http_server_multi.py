import socket
import os

max_queue_size = 10
html_path = "{0}lab2_files{0}{1}.html".format(os.path.sep, ) #TODO

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare server socket
host = gethostname()
port = 666
serverSocket.bind((host, "")) #TODO?
serverSocket.listen(max_queue_size)

while True:
    
