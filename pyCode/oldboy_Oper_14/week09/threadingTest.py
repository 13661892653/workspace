#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import threading
import time
def run(n):
    while True:
        print('%s正在运行'%n)
        time.sleep(1)

t1=threading.Thread(target=run,args=('t1',))
t1.start()
t2=threading.Thread(target=run,args=('t2',))
t2.start()