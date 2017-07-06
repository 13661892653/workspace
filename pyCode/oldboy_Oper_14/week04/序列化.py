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
#可以多次dumps
f.write(json.dumps(info)+"\n")
f.write(json.dumps(info)+"\n")
f.write(json.dumps(info)+"\n")
f.write(json.dumps(info))
f.close()
