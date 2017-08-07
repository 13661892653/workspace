#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import queue
import threading
import time
q=queue.Queue(maxsize=10)

def producor(name):
    count=1
    while True:
        if count%10==0:
            q.put('VIP特大包子%s，恭喜哦！' % count)
        q.put('包子%s' %count)
        print('%s生产了包子%s' %(name,count))
        count+=1
        time.sleep(1)

def Consumer(name):
    while True:
        print('{name}取到了{baozi}，并且吃了它' .format(name=name,baozi=q.get()))
        time.sleep(1)
p1=threading.Thread(target=producor,args=("陈伦",))
c1=threading.Thread(target=Consumer,args=("老婆",))
c2=threading.Thread(target=Consumer,args=("儿子",))
p1.start()
c1.start()
c2.start()