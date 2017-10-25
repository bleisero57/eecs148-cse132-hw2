import socket
import os

max_queue_size = 1 # this version of the http server handles 1 client only
#TODO: use cmd line to request file?
#ex: http_server.py request.html
rqpath = "{0}lab2_files{0}{1}.html".format(os.path.sep, )

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare server socket
host = gethostname() # should be 127.0.0.1 (localhost)
port = 80
serverSocket.bind((host, port))
serverSocket.listen(max_queue_size)

while True:
    print ("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print ("Connecting to {}".format(addr))
    
    try:
        # Request line
        message = "GET {0}{1} HTTP/1.1".format(os.path.realpath(__file__), rqpath)
        filename = message.split()[1]
        f = open(filename[1:], "rb")
        output = #TODO
        
        # Send one HTTP header line into socket
        clientSocket.send(b"header") #TODO
        clientSocket.send(b"\n")
        
        # Send the content of the requested file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
            
        connectionSocket.send(b'\r\n\r\n') # blank line?
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b"""
<html>
<body>
<h1>Error 404</h1> 404 not found
</body>
</html>
""")
        
        # Close client socket
        connectionSocket.close()

serverSocket.close()
