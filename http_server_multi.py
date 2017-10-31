import os
import socket
import threading

### Macros ###
basepath = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))
extension = "{}lab2_files{}".format(os.path.sep)
max_queue_size = 10
count = 0
H = socket.gethostname()
P = 12345
errorpage = b"""
<html>
<body>
<h1>Error 404</h1> 404 file not found
</body>
</html>
"""

### Thread classes ###
class serverThread (threading.Thread):
    def __init__(self, socket, host, port):
        threading.Thread__init__(self)
        #todo

    def run(self):
        # Prepare server socket
        print("[SERVER]> Server starting: {}:{}\n".format(host, port))
        serverSocket.bind((host, port))
        serverSocket.listen(max_queue_size)
        running = True
        
        while running:
            print("[SERVER]> Ready to serve...")
            clientSocket[count], addr = s.accept() # accept is blocking
            #need to bind to new port somehow?
            clientHandler[count] = new clientThread(clientSocket[count], addr, counter) # todo
            clientHandler[count].start() # will invoke run
            count += 1
            
        if threading.activeCount():
            for h in clientHanndler:
                if h.isAlive():
                    h.quit()
                    h.join()

    def quit(self):
        #todo
        running = False
        print("[SERVER]> Closing server.")
        serverSocket.close()

class clientThread (threading.Thread):
    def __init__(self, connection, address, number):
        threading.Thread.__init__(self)
        #todo

    def run(self):
        print("[CLIENT {1}]> Connecting to {0}\n".format(address, number))
        running = True
        
        while running:
            try:
                # Request line
                message = str(connection.recv(1024), "utf-8")
                print("[CLIENT {1}]> Recieved:\n(0)".format(message, number)) 
                filepath = message.split()[1]
                filepath = "{}{}{}".format(basepath, extension, filepath[1:])
                print("[CLIENT {1}]> Attempting to open {0}".format(filepath, number))
                
                if not os.path.isfile(filepath):
                    print("[CLIENT {1}]> Could not find {0}. Responding...".format(filename[1:], number))
                    raise IOError("404 file not found")

                print("[CLIENT {1}]> File found. Responding...")
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
                connection.send(errorpage)
        
                # Close client socket
                connection.send(b'\r\n\r\n')
                    
        connection.close() #or use finally statement to close connection?

    def quit(self):
        running = False

### Main ###
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverHandler = new serverThread(serverSocket, H, P)
print("[MAIN]> Created server thread on {}:{}".format(H, P))
serverHandler.start()

while True:
    x = input("[MAIN]> ")
    if x.lower() == "exit" or x.lower() == "quit" or x.lower() == "stop": 
        serverHandler.quit()
        serverHandler.join()
        break
