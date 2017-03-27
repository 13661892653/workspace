#/bin/python
#coding=utf-8
'''线程开发、线程的创建'''
from threading import Thread
import time
def Foo(arg1,arg2):
    for item in range(10):
        print('打印',arg1,arg2)
        time.sleep(1)
print('before')
t1 = Thread(target=Foo,args=(1,2))
#（守护进程）：setDaemon等于True，主线程不等子线程执行完就退出
'''join函数主进程暂停，等待子线程执行完了，主进程再继续执行
，而join里边的超时参数，意思为最多等待多少时间'''
t1.setDaemon(True)
t1.start()
t1.join(2)
print('after')
