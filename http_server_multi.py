import os
import socket
import threading

### Macros ###
basepath = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))
extension = "{}lab2_files{}".format(os.path.sep)
max_queue_size = 10

### Thread classes ###
class serverThread (threading.Thread):
    def __init__(self, socket, host, port, ):
        threading.Thread__init__(self)
        #todo
        # Prepare server socket
        print("Server starting: {}:{}\n".format(host, port))
        serverSocket.bind((host, port))
        serverSocket.listen(max_queue_size)

    def run(self):
        #todo
        running = True
        
        while running:
            print("Ready to serve...")
            clientSocket[count], addr = s.accept() # accept is blocking
            #need to bind to new port somehow
            clientHandler[count] = new clientThread(clientSocket[count], ) # todo
            clientHandler[count].start() # will invoke run
            count += 1
            
        if threading.activeCount():
            for h in clientHanndler:
                if h.isAlive():
                    #need to call h's "stop" function?
                    h.join()

    def stahp: #rename
        #todo
        running = False
        print("Closing server.")
        serverSocket.close()

class clientThread (threading.Thread):
    def __init__(self, connection, address):
        threading.Thread.__init__(self)
        #todo

    def run(self):
        print("Connecting to {]\n".format(address))
        running = True
        
        while running:
            try:
                # Request line
                message = str(connection.recv(1024), "utf-8")
                print("\tRecieved:\n()".format(message)) 
                filepath = message.split()[1]
                filepath = "{}{}{}".format(basepath, extension, filepath[1:])
                print("Attempting to open {}".format(filepath))
                
                if not os.path.isfile(filepath):
                    print("Could not find {}. Responding...".format(filename[1:]))
                    raise IOError("404 file not found")

                print("File found. Responding...")
                f = open(filepath, "rb")
                outputdata = f.read()
                
                # Send HTTP header
                connection.send(b"HTTP/1.x 200 OK")
                connection.send(b'\r\n\r\n')

                # Send the content of the requested file client
                for i in range(0, len(outputdata)):
                    connection.send(outputdata[i:i+i])

                connection.send(b'\r\n\r\n')
            except IOError:
                # Send response message for file not found
                connection.send(b"HTTP/1.x 404 NOUT FOUND")
                connection.send(b'\r\n\r\n')
                
                # Send HTML for error display
                connection.send(b"""
<html>
<body>
<h1>Error 404</h1> 404 file not found
</body>
</html>
""")
        
                # Close client socket
                connection.send(b'\r\n\r\n')
                    
        connection.close() #or use finally statement to close connection?

    def stahp: # todo: rename
        running = False # maybe change running to int?

### Main ###
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverHandler = new serverThread(serverSocket, socket.gethostname(), 12345, ) #todo

while True:
    if : #todo: determine exit command
        break

#need to call serverHandler's "stop" function?
serverHasndler.join()

