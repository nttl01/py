# server
import socket

server = socket.socket()
server.bind(('127.0.0.1',9999))
server.listen(5)
print (" server ready -----")


#파일 수신
i = 1

while True:
    client, address = server.accept()
    print("connect ok",address)

    #파일열기
    f = open("c:/pythonworkspace/2.jpg","wb")

    i = i + 1
    print("i = ",i)

    l = 1
    while(l):
        l = client.recv(1024)
        # print("data=",l)

        while(l):
            f.write(l)
            l = client.recv(1024)
        f.close()






client.close()
server.close()



