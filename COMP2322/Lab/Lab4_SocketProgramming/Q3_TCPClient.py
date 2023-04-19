# import the socket library
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create a socket object

# define the server's name and port
serverName = '127.0.0.1'
serverPort = 12345

# client connect to server
clientPort = 34655
clientSocket.bind(('', clientPort))
clientSocket.connect((serverName, serverPort))

sentence = clientSocket.recv(1024).decode()     # receive data from server and decode to get string
print ("from server:", sentence)

clientSocket.close()    # close the connection

