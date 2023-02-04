from socket import *
serverPort = 14000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
print ('The server is ready to receive')
while True:
     serverSocket.listen(1)
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024).decode()
     print("Client message is received :",sentence)
     if (sentence == "Exit"):
          connectionSocket.send('exit'.encode())
          connectionSocket.close()
          break
     else:
          size = len(sentence.encode('utf-8'))
          capitalizedSentence = sentence.upper()
          print('Size of client message =', size)
          connectionSocket.send(capitalizedSentence.encode())
          connectionSocket.send(str(size).encode())
          connectionSocket.close()

print('Server closed')