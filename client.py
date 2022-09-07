import os

#os.system('python3 serveur.py')


def send(ip,a):
    import socket
    import os
    #os.system('pyhton3 main.py')
    if ip == '':
        ip = '192.168.1.75'
    hote = ip
    port = 15555

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((hote, port))
    print("Connection on {}".format(port))
    obj = bytes(a, 'utf-8')
    socket.send(obj)

    print("Close")
    socket.close()

#send('basile')