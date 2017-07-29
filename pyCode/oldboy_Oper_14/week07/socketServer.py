#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Server
import socket
server=socket.socket()
server.bind(('localhost',9000))#绑定监听端口
server.listen(5)#监听5个
print('我要开始等电话了')
conn,addr=server.accept()#等电话打进来
print(conn,addr)
print('电话来啦')
data=conn.recv(1024)
print('recv:',data)
conn.send(data.upper())