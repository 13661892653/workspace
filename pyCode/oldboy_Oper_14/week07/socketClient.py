#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Client
import socket
client=socket.socket()#声明socket类型。同时生成socket链接对象
client.connect(('localhost',9000))
client.send(b"hello world")
data=client.recv(1024)
print('receive',data)
client.close()
