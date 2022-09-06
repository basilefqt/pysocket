import socket
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))

        response = client.recv(255)
        if response != "":
                print(response)
                file = open('./stock.txt','a')
                file.write(str(response))
                file.close()
                #os.system('start stock.txt')




print("Close")
client.close()
stock.close()