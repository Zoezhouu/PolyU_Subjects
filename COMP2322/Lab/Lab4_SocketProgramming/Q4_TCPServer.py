# import the socket library
import socket

# create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("socket successfully created")

# reserve a port = 12345 on your computer
serverPort = 12345

serverSocket.bind(('', serverPort))     # bind to the port
print ("socket binded to %s" %(serverPort))

serverSocket.listen(5)  # put the socket into listening mode
print ("socket is listening")

while True:
    connectionSocket, addr = serverSocket.accept()  # establish connection with client
    print ('got connection from', addr)

    pw = connectionSocket.recv(1024).decode()
    if (pw == "4655"):
        sentence = "Your password is correct!"
    else:
        sentence = "Your password is incorrect!"
    # sentence = 'thank you for connecting'   # send message to the client
    connectionSocket.send(sentence.encode())    #send byte type
    
    connectionSocket.close()    # close the connect ion with the client
    break