import socket
import smtplib
import sys
import os

### Macros ###
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

### Main ###

# Connect to the local host (an EECS server, where this code should be executed)

mailserver = "localhost"

# Create a socket called clientSocket and establish a TCP connection w/mailserver
#todo

recv = clienSocket.recv(1024).decode()

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
#todo

# Send RCPT TO command and print server response
#todo

# Send DATA command and print server response
#todo

# Send message data
#todo

# Message ends w/single period
#todo

# Send QUIT command and get server response
#todo
