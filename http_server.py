import socket
import os

max_queue_size = 1

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prepare server socket
host = socket.gethostname() # localhost
port = 12345
print("Server starting: {}:{}\n".format(host, port))
serverSocket.bind((host, port))
serverSocket.listen(max_queue_size)

while True:
    # Establish connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    print("Connecting to {}\n".format(addr))
    
    try:
        # Request line
        message = str(connectionSocket.recv(1024), "utf-8")
        print("Recieved:\n{}".format(message))
        filename = message.split()[1]
        base = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))
        filepath = "{2}{0}lab2_files{0}{1}".format(os.path.sep, filename[1:], base)
        print("Attempting to open {}".format(filepath))
        
        if os.path.isfile(filepath):
            f = open(filepath, "rb")
            print("File found. Responding...")
            outputdata = f.read()
        else:
            print("Could not find {}. Responding...".format(filename[1:]))
            raise IOError("404 file not found")
        
        # Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.x 200 OK")
        connectionSocket.send(b'\r\n\r\n') # separates header from body
        
        # Send the content of the requested file to client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i+1])
            
        connectionSocket.send(b'\r\n\r\n') # end body
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b"HTTP/1.x 404 NOT FOUND")
        connectionSocket.send(b'\r\n\r\n')

        # Send HTML for error display
        connectionSocket.send(b"""
<html>
<body>
<h1>Error 404</h1> 404 file not found
</body>
</html>
""")
        
        # Close client socket
        connectionSocket.send(b'\r\n\r\n')
        connectionSocket.close()

print("Closing server.")
serverSocket.close()
