import os
import socket
import threading

### Macros ###
basepath = os.path.realpath(os.path.join(os.path.dirname(__file__), "."))
extension = "{0}lab2_files{0}".format(os.path.sep)
max_queue_size = 10
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
    def __init__(self, sock, host, port):
        threading.Thread.__init__(self)
        self.serverSocket = sock
        self.host = host
        self.port = port
        self.clientHandler = []
        self.count = 0

    def run(self):
        # Prepare server socket
        print("[SERVER]> Server starting: {}:{}\n".format(self.host, self.port))
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(max_queue_size)
        self.running = True
        
        while self.running:
            print("[SERVER]> Ready to serve...")
            self.clientSocket, self.addr = self.serverSocket.accept() # accept is blocking
            self.clientHandler.append(clientThread(self.clientSocket, self.addr, self.count))
            self.clientHandler[len(self.clientHandler) - 1].start() # will invoke run
            self.count += 1

    def quit(self):
        self.running = False
        print("[SERVER]> Closing server.")
		
        if threading.activeCount():
            for h in self.clientHandler:
                if h.isAlive():
                    h.quit()
                    h.join()

        self.serverSocket.close()

class clientThread (threading.Thread):
    def __init__(self, connection, address, number):
        threading.Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.number = number

    def run(self):
        print("[CLIENT {1}]> Connecting to {0}\n".format(self.address, self.number))
        self.running = True
        
        while self.running:
            try:
                # Request line
                self.message = str(self.connection.recv(1024), "utf-8")
                print("[CLIENT {1}]> Recieved:\n(0)".format(self.message, self.number)) 
                self.filepath = self.message.split()[1]
                self.filepath = "{}{}{}".format(basepath, extension, self.filepath[1:])
                print("[CLIENT {1}]> Attempting to open {0}".format(self.filepath, self.number))
                
                if not os.path.isfile(self.filepath):
                    print("[CLIENT {1}]> Could not find {0}. Responding...".format(self.filepath[1:], self.number))
                    raise IOError("404 file not found")

                print("[CLIENT {}]> File found. Responding...".format(self.filepath))
                self.f = open(self.filepath, "rb")
                self.outputdata = self.f.read()
                
                # Send HTTP header
                self.connection.send(b"HTTP/1.x 200 OK")
                self.connection.send(b'\r\n\r\n')

                # Send the content of the requested file client
                for i in range(0, len(self.outputdata)):
                    self.connection.send(self.outputdata[i:i+i])

                self.connection.send(b'\r\n\r\n')
                self.connection.close()
            except IOError:
                # Send response message for file not found
                self.connection.send(b"HTTP/1.x 404 NOT FOUND")
                self.connection.send(b'\r\n\r\n')
                
                # Send HTML for error display
                self.connection.send(errorpage)
                self.connection.send(b'\r\n\r\n')
                self.connection.close()

    def quit(self):
        self.running = False

### Main ###
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverHandler = serverThread(serverSocket, H, P)
print("[MAIN]> Created server thread on {}:{}".format(H, P))
serverHandler.start()
print("[MAIN]> To turn server off, enter \"exit\" or \"quit\" or \"stop\"")

while True:
    x = input("") #input("[MAIN]> ")
    if x.lower() == "exit" or x.lower() == "quit" or x.lower() == "stop": 
        serverHandler.quit()
        serverHandler.join()
        break
