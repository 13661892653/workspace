#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import queue
import threading
import time
t=threading.Event()

def lighter():
    count=1
    while True:
        if count<=5:
            t.clear()
            print("\033[42;1m绿灯行%s....\033[0m"%count)
            count += 1
        elif count>5 and count<=10:
            print("\033[41;1m红灯停%s....\033[0m"%(count-5))
            t.set()
            count+=1
        else:
            count = 1
        time.sleep(1)

def car(type):
    while True:
        if t.is_set():
            t.wait()
            print('%s等待....' % type)
            time.sleep(1)
        else:
            print('%s卡车通行....' % type)
            time.sleep(1)

l=threading.Thread(target=lighter)
c1=threading.Thread(target=car,args=('宝马',))
c2=threading.Thread(target=car,args=('迈巴赫',))
c3=threading.Thread(target=car,args=('奔驰',))
c4=threading.Thread(target=car,args=('马萨拉蒂',))
l.start()
c1.start()
c2.start()
c3.start()
c4.start()