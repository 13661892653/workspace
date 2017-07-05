#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
__author__ = "Colby"
import json
info={
    'name':'colby',
    'age':20
}
f=open('info.txt','w')
f.write(json.dumps(info))
f.close()