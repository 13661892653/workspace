#进程池
from multiprocessing import Pool
import os
import time


def worker(msg):
    print("子进程id：%d"%os.getpid())
    startTime = time.time()
    time.sleep(2)
    endTime = time.time()
    print("子进程msg:%s,共花费时间%d"%(msg, endTime - startTime))


#创建进程池
pool = Pool(3)

for x in range(10):
    pool.apply_async(worker, (x, ))

#关闭进程池
pool.close()

#父进程等待进程池结束
pool.join()
print("进程池已结束")