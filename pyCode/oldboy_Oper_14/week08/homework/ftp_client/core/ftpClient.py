#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
client=socket.socket()
client.connect(('localhost',10002))
while True:
    res=input("发送数据>>")
    if len(res) == 0: continue
    client.send(res.encode('utf-8'))
    print('发送如下数据',res)
    data=client.recv(1024)
    print('接收到服务器端的返回数据',data.decode())
client.close()