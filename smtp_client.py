import socket
import sys
import os

### Macros ###
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

### Main ###

# Connect to the local host (an EECS server, where this code should be executed)
mailserver = "localhost"
#mailserver = socket.gethostname()

# Create a socket called clientSocket and establish a TCP connection w/mailserver
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, 465))

recv = clientSocket.recv(1024).decode()

print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server resposne

heloCommand = 'HELO Alice\r\n'

clientSocket.send(heloCommand.encode())

recv1 = clienSocket.recv(1024).decode()

print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response

mailCommand = "MAIL FROM: \r\n"#todo

clientSocket.send(mailCommand.encode())

recv2 = clientSocket.recv(1024).decode()

print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')
    
# Send RCPT TO command and print server response

rcptCommand = ""

clientSocket.send(rcptCommand.encode())

recv3 = clientSocket.recv(1024).decode()

print(recv3)

if recv3[:3] != '250':
    print('250 reply not received from server.')
    
# Send DATA command and print server response

dataCommand = ""

clientSocket.send(dataCommand.encode())

recv4 = clientSocket.recv(1024).decode()

print(recv4)

if recv4[:3] != '354':
    print('345 reply not received from server.')
    
# Send message data

clientSocket.send(msg.encode())

recv5 = clientSocket.recv(1024).decode()

print(recv5)

if recv5[:3] != '250':
    print('250 reply not received from server.')

# Message ends w/single period

clientSocket.send(endmsg.encode())

recv6 = clientSocket.recv(1024).decode()

print(recv6)

if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response

quitCommand = "QUIT"

clientSocket.send(mailCommand.encode())

recv7 = clientSocket.recv(1024).decode()

print(recv7)

if recv7[:3] != '221':
    print('221 reply not received from server.')
