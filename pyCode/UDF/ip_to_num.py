#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
import struct
import sys,datetime
ipDB='/opt/data/IP_utf-8.csv'
for line in sys.stdin:
    line = line.strip()
    user_id, reg_ip, reg_ip_geo_map, ds = line.split('\t')
    num_ip = int(socket.ntohl(struct.unpack("I", socket.inet_aton(str(reg_ip)))[0]))
    f = open(ipDB, 'r', encoding="utf-8")
    ipDict = {}
    count = 0
    for line in f:
        if count == 9:
            count += 1
            continue
        line = line.split(',')
        if int(line[2]) <= num_ip and int(line[3]) >= num_ip:
            ipDict['IP'] = reg_ip
            ipDict['nationality'] = line[4]
            ipDict['province'] = line[5]
            ipDict['city'] = line[6]
            ipDict['Corporation'] = line[8]
            reg_ip_geo_map=str(ipDict)[1:-1].replace('\'','').replace(' ','')
            print('\t'.join([user_id, reg_ip, reg_ip_geo_map,ds]))
    f.close()