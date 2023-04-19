# import the socket library
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # create a socket object

# define the server's name and port
serverName = '127.0.0.1'
serverPort = 12345

clientSocket.connect((serverName, serverPort))

# password = 4655
password = input("Please input password:")
clientSocket.send(str(password).encode())

sentence = clientSocket.recv(1024).decode()     # receive data from server and decode to get string
print ("from server:", sentence)

clientSocket.close()    # close the connection

