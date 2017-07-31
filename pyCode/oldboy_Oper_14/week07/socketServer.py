#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
server=socket.socket()
server.bind(('localhost',5000))
server.listen(5)

print('我开始等待接受数据了！')
while True:
    conn,addr=server.accept()
    while True:
        data=conn.recv(1024)
        print('收到如下数据',data)
        conn.send(data.upper())
        print('发送如下数据',data.upper())
server.close()

