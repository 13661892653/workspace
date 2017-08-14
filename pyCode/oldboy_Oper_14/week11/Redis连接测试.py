#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import redis
r=redis.Redis(host='localhost',port=6379)
r.set('guojuan','xifu')
r.setbit('user','1000',1)
r.setbit('user','9999',1)
r.setbit('user','8888',1)
r.setbit('user','6666',1)
print('在线同户数%s' % r.bitcount('user'))
