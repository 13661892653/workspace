#/bin/python
#coding=utf-8
'''自定义线程类的写法'''
from threading import Thread
import time
class MyThread(Thread):
    def run(self):
        time.sleep(10)
        print('我是儿子线程！')
def Bar():
    print('par')

t1=MyThread(target=Bar)
t1.start()
print('我是父亲线程！')