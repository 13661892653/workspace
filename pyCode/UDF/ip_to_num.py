#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
import struct
import sys,datetime
ipDB='F:\BaiduNetdiskDownload\IP_utf-8.csv'
for line in sys.stdin:
  line = line.strip()
  userid, movieid, rating, unixtime = line.split('\t')
  weekday = datetime.datetime.fromtimestamp(float(unixtime)).isoweekday()
  print('\t'.join([userid, movieid, rating, str(weekday)]))

ip = '103.18.104.0'
num_ip=int(socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0]))
print(num_ip)
f=open(ipDB,'r',encoding="utf-8")
ipDict={}
count = 0
for line in f:
    if count == 9:
        count += 1
        continue
    line=line.split(',')
    if int(line[2])<=num_ip and int(line[3])>=num_ip:
        ipDict['IP'] = ip
        ipDict['国籍']=line[4]
        ipDict['省份'] = line[5]
        ipDict['市'] = line[6]
        ipDict['运营商'] = line[8]
        print('ip详细地址：',ipDict)