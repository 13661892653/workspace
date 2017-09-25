#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
#num转ip
import socket
import struct
num_ip = 2001459789
ip = socket.inet_ntoa(struct.pack('I',socket.htonl(num_ip)))
print(ip)
#'119.75.218.77'