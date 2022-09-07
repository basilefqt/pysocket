import socket
import os
from client import send
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15557))


def mat(text):
        text = str(text).strip()
        new = []
        for i in range(2,len(text)-1):
                new.append(text[i])
        return ''.join(new)


        

while True:
        a = ""
        socket.listen(5)
        client, address = socket.accept()
# print("{} connected".format( address ))
        response = client.recv(255)
        if response != "":
                response = mat(response)
                print(response)
                file = open('./stock.txt','a')
                file.write(response)
                file.close()
                while a == "":
                        a = input('votre réponse')
                        send('192.168.1.98',a)
                

                #os.system('start stock.txt')


a = input('votre réponse')
send('192.168.1.92',a)




print("Close")
client.close()
