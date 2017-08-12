#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
from urllib import request
import gevent
import time
from gevent import monkey
monkey.patch_all()

def f(url):
    print('Get %s' %url)
    req=request.urlopen(url)
    data=req.read()
    print(data)

urls=[
    'https://www.baidu.com/',
    'https://www.python.org/',
    'https://www.taobao.com/'
]
time1=time.time()
for i in urls:
    f(i)
print('同步',time.time()-time1)
time2=time.time()
gevent.joinall(
    [
        gevent.spawn(f,'https://www.baidu.com/'),
        gevent.spawn(f,'https://www.python.org/'),
        gevent.spawn(f,'https://www.taobao.com/')
    ]
)
print('异步',time.time()-time2)