import os
import socket
import threading
import time
from datetime import datetime, timezone

HOST = '127.0.0.1'  # Local host
PORT = 8888  # Port number
BUFFER_SIZE = 1024  # Buffer size for receiving data

# mapping response number into response types
RESPONSE_TYPE = {
    200: 'OK',
    400: 'Bad Request', 
    404: 'File Not Found', 
    304: 'Not Modified',
}

# mapping file extension to MIME types
MIME_TYPE = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
}

def date_from_secs(secs):
    if secs:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(secs))
    return None

def handle_request(connectionSocket, addr):
    request = connectionSocket.recv(BUFFER_SIZE).decode()       # receive data from client
    requestLines = request.split("\r\n")                        # split request message into lines
    responseNumber = 0              # save response type number
    fileName = ''                   # save file name for log file
    # processing request line to get requested file path
    if len(requestLines) > 0:
        requestComponents = requestLines[0].split(' ')
        response = ''
        if len(requestComponents) == 3:
            method, path, protocol = requestComponents
            # GET requests
            if method == 'GET':
                filePath = path.lstrip('/')                 # removes leading characters
                if not filePath:
                    filePath = 'htmldocs/index.html'
                    fileName = 'index.html'
                fileExtension = os.path.splitext(filePath)[1]   # split extension number
                mimeType = MIME_TYPE.get(fileExtension, 'application/octet-stream') # convert to MIME type
                fileStat = os.stat(filePath)        # file info
                lastModifiedTime = date_from_secs(fileStat.st_mtime)    # file modified time
                # check if file exists
                if os.path.exists(filePath):
                    # check if requested resource has been modified since the specified date
                    if "If-Modified_Since" in requestLines:
                        # 304 file not modified: if-modified-since < file modified time
                        if requestLines[requestLines.index('If-Modified-Since')+1] == f'If-Modified-Since: {lastModifiedTime}':
                            responseNumber = 304
                            response += f'HTTP/1.1 304 Not Modified\r\n'
                            time = datetime.now(timezone.utc)   # time now
                            response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                            response += f"last_modified: {lastModifiedTime}\r\n"
                            response += f"Content-Type: {mimeType}\r\n"
                            connectionSocket.sendall(response.encode())
                            print(response)
                            # print("\n")
                            connectionSocket.close()
                            return
                    # else:
                    # 200 - OK: send response header and file content
                    responseNumber = 200
                    response += "HTTP/1.1 200 OK\r\n"
                    time = datetime.now(timezone.utc)
                    response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                    response += f"last_modified: {lastModifiedTime}\r\n"
                    response += f"Content-Type: {mimeType}\r\n"
                    connectionSocket.sendall(response.encode())
                    with open(filePath, 'rb') as file:
                        connectionSocket.sendfile(file)
                    print(response)
                else:
                    # file not found - 404
                    responseNumber = 404
                    response += "HTTP/1.1 404 File Not Found\r\n"
                    time = datetime.now(timezone.utc)
                    response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                    response += f"last_modified: {lastModifiedTime}\r\n"
                    response += f"Content-Type: {mimeType}\r\n"
                    connectionSocket.sendall(response.encode())
                    print("HTTP/1.1 404 File Not Found\n")
                    print(response)
                    fileName = '404.html'
                    with open('htmldocs/404.html', 'rb') as file:
                        connectionSocket.sendfile(file)
                    print(response)
            elif method == 'HEAD':
                filePath = path.lstrip('/')                 # removes leading characters
                if not filePath:
                    filePath = 'htmldocs/index.html'
                    fileName = 'index.html'
                fileExtension = os.path.splitext(filePath)[1]   # split extension number
                mimeType = MIME_TYPE.get(fileExtension, 'application/octet-stream') # convert to MIME type
                fileStat = os.stat(filePath)        # file info
                lastModifiedTime = date_from_secs(fileStat.st_mtime)    # file modified time
                # check if file exists
                if os.path.exists(filePath):
                    # check if requested resource has been modified since the specified date
                    if "If-Modified_Since" in requestLines:
                        # 304 file not modified: if-modified-since < file modified time
                        if requestLines[requestLines.index('If-Modified-Since')+1] == f'If-Modified-Since: {lastModifiedTime}':
                            responseNumber = 304
                            response += f'HTTP/1.1 304 Not Modified\r\n'
                            time = datetime.now(timezone.utc)   # time now
                            response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                            response += f"last_modified: {lastModifiedTime}\r\n"
                            response += f"Content-Type: {mimeType}\r\n"
                            connectionSocket.sendall(response.encode())
                            print(response)
                            # print("\n")
                            connectionSocket.close()
                            return
                    # else:
                    # 200 - OK: send response header and file content
                    responseNumber = 200
                    response += "HTTP/1.1 200 OK\r\n"
                    time = datetime.now(timezone.utc)
                    response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                    response += f"last_modified: {lastModifiedTime}\r\n"
                    response += f"Content-Type: {mimeType}\r\n"
                    connectionSocket.sendall(response.encode())
                    # with open(filePath, 'rb') as file:
                    #     connectionSocket.sendfile(file)
                    print(response)
                else:
                    # file not found - 404
                    responseNumber = 404
                    response += "HTTP/1.1 404 File Not Found\r\n"
                    time = datetime.now(timezone.utc)
                    response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                    response += f"last_modified: {lastModifiedTime}\r\n"
                    response += f"Content-Type: {mimeType}\r\n"
                    connectionSocket.sendall(response.encode())
                    print("HTTP/1.1 404 File Not Found\n")
                    print(response)
                    fileName = '404.html'
                    # with open('htmldocs/404.html', 'rb') as file:
                    #     connectionSocket.sendfile(file)
                    print(response)

            else:
                # malformed request
                fileExtension = os.path.splitext('htmldocs/400.html')[1]
                mimeType = MIME_TYPE.get(fileExtension, 'application/octet-stream')
                responseNumber = 400
                response += "HTTP/1.1 400 Bad Request\r\n"
                time = datetime.now(timezone.utc)
                response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
                # response += f"last_modified: {lastModifiedTime}\r\n"
                response += f"Content-Type: {mimeType}\r\n"
                connectionSocket.sendall(response.encode())
                fileName = '400.html'
                with open('htmldocs/400.html', 'rb') as file:
                    connectionSocket.sendfile(file)
                print(response)

        else:
            # other request
            # 400 - bad request
            fileExtension = os.path.splitext('htmldocs/400.html')[1]
            mimeType = MIME_TYPE.get(fileExtension, 'application/octet-stream')
            responseNumber = 400
            response += "HTTP/1.1 400 Bad Request\r\n"
            time = datetime.now(timezone.utc)
            response += f"datetime:{time}\r\nkeep-alive:timeout=10\r\n"
            # response += f"last_modified: {lastModifiedTime}\r\n"
            response += f"Content-Type: {mimeType}\r\n"
            connectionSocket.sendall(response.encode())
            fileName = '400.html'
            with open('htmldocs/400.html', 'rb') as file:
                connectionSocket.sendfile(file)
            print(response)
    
    # responseType = RESPONSE_TYPE[responseNumber]
    timeNow = time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    clientIP = connectionSocket.getpeername()[0]
    
    # log file - client hostname/IP address, access time, request file name, response type
    with open('log.txt', 'a') as logFile:
        logFile.write(f'|\t{clientIP}\t|\t{timeNow}\t|\t{fileName}\t|\t{responseNumber}\t\t|\n')

    connectionSocket.close()

# Create socket object and bind to port
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

print("Socket is bind to %s" %(PORT))
print("Serving on http://%s:%s" %(HOST,PORT))

# loop to handle incoming connections
while True:
    # Accept incoming connection
    connectionSocket, addr = serverSocket.accept()
    # print('Got connection from', addr)
    print("Server socket:",  serverSocket.getsockname())    # print the four-tuple of server socket
    print("Client socket:", connectionSocket.getpeername())     # print the four-tuple of client socket

    # Create new thread to handle request
    serverThread = threading.Thread(target = handle_request, args=(connectionSocket, addr))
    serverThread.start()
    
    break