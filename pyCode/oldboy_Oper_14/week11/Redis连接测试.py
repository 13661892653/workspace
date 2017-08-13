#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import redis
r=redis.Redis(host='localhost',port=6379)
r.set('guojuan','xifu')
print(r.get('guojuan'))
print(r.get('name'),r.get('age'))