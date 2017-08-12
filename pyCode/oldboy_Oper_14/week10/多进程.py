#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import multiprocessing
import time
def run(name):
    print('进程%s正在执行' % name)
    time.sleep(1)

if __name__ == '__main__':
    for i in range(10):
        p=multiprocessing.Process(target=run,args=('男人%s号'%i,))
        p.start()