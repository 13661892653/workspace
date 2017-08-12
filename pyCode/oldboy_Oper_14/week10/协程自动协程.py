#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import gevent
import time
def fun1():
    print('running fun1')
    gevent.sleep(1)
    print('again running fun1')
    gevent.sleep(1)
def fun2():
    print('running fun2')
    gevent.sleep(1)
    print('again running fun2')
    gevent.sleep(1)
def fun3():
    print('running fun3')
    gevent.sleep(1)
    print('again running fun3')
    gevent.sleep(1)
if __name__=='__main__':
    gevent.joinall(
        [
            gevent.spawn(fun1),
            gevent.spawn(fun2),
            gevent.spawn(fun3)
        ]
    )