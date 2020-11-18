#client

import socket

ip = '127.0.0.1'
port = 9999

client = socket.socket()

client.connect((ip,port))
print(" server connected ------")

#파일전송
f = open("c:/pythonworkspace/1.jpg","rb")
l = f.read(1024)
while(l):
    client.send(l)
    l = f.read(1024)

client.close()


