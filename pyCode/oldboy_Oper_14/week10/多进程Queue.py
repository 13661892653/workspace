#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import multiprocessing
from multiprocessing import Process,Queue

def run(q):
    q.put('测试数据1')
    q.put('测试数据2')

if __name__=="__main__":
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=run,args=(q,))
    p.start()
    print(q.get())
    print(q.get())
    p.join()