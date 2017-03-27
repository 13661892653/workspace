#coding=utf-8
'''生产者与消费者，队列的使用'''
from threading import Thread
import queue
import time
class Productor(Thread):
    def __init__(self,name,queue):
        '''
        :param name: 生产者的名字
        :param queue:队列的池子（容器）
        '''
        self.__Name=name
        self.__Queue=queue
        super(Productor,self).__init__()
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('做包子')
                print(time.time(),'%s生产了一个包子'% self.__Name)
                time.sleep(1)
class Consumer(Thread):
    def __init__(self,name,queue):
        '''
        :param name: 生产者的名字
        :param queue:队列的池子（容器）
        '''
        self.__Name=name
        self.__Queue=queue
        super(Consumer,self).__init__()
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                print(time.time(),'''
                %s消费了一个包子:
                %s消费了一个包子:
                %s消费了一个包子:
                ''' % (self.__Name,self.__Name,self.__Name))
                self.__Queue.get()
                time.sleep(1)
'''先进先出，默认取出第一个元素，不需要指定get参数
定义2个生产者
'''
q1=queue.Queue(maxsize=100)
for item1 in range(100):
    name='chenlun%d' % item1
    temp=Productor(name,q1)
    temp.start()
'''定义20个消费者'''
for item2 in range(100):
    name='guojuan%d' % item2
    temp=Consumer(name,q1)
    temp.start()

