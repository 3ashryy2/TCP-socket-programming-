from socket import *
serverIP = '127.0.0.1'
serverPort = 14000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverIP,serverPort))
    print("Connection is initialized. Type ""Exit"" to terminate.")
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(2048)
    size = clientSocket.recv(2048)
    if (modifiedSentence.decode()=='exit'):
        print ('Disconnected')
        clientSocket.close()
        break
    else:
        print('From Server: Size of the message :', size.decode())
        print('Uppercase :', modifiedSentence.decode())
        clientSocket.close()
print('connection is closed')