#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
from multiprocessing import Process,Pool
import os,time
def Foo(i):
    time.sleep(2)
    print('Foo',os.getpid())
def Bar(arg):
    print('Bar',os.getpid())
if __name__=='__main__':
    pool=Pool(processes=1)#允许进程池同时放入5个进程
    print(os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)
    print('结束啦')
    pool.close()
    pool.join()