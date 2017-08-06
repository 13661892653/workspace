#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n=n
    def run(self):
        print('%s 线程正在运行' % self.n)
        time.sleep(2)
lst=[]
start_time=time.time()
for i in range(50):
    t=MyThread(i)
    t.start()
    lst.append(t)
for j in lst:
    j.join()
print('cost:',time.time()-start_time)