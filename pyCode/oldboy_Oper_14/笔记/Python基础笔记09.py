paramiko模块
ssh 密钥
RSA-非对称密钥验证
	生成公钥和私钥，访问指定服务器任意用户，只需要将公钥拷贝到用户/.ssh目录即可
	rsa ssh-genkey
	ssh-copy-id "-p22 root@192.168.1.102"
	ssh root@192.168.1.102
进程与线程
	线程是操作系统最小的调度单位
	对各种资源管理的集合可以叫进程，比如QQ
	区别：
		启动线程比启动进程快
		线程共享内存空间，进程的内存是独立的
		
线程锁
信号量
	threading.BoundedSemaphore(5)最多允许5个线程同时执行
事件
	event.set()
	event.wait()
	event.clear()
	红绿灯的作业
	__author__ = "Alex Li"
	import time
	import threading
	event = threading.Event()
	def lighter():
		count = 0
		event.set() #先设置绿灯
		while True:
			if count >5 and count < 10: #改成红灯
				event.clear() #把标志位清了
				print("\033[41;1mred light is on....\033[0m")
			elif count >10:
				event.set() #变绿灯
				count = 0
			else:
				print("\033[42;1mgreen light is on....\033[0m")
			time.sleep(1)
			count +=1
	def car(name):
		while True:
			if event.is_set(): #代表绿灯
				print("[%s] running..."% name )
				time.sleep(1)
			else:
				print("[%s] sees red light , waiting...." %name)
				event.wait()
				print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)
	light = threading.Thread(target=lighter,)
	light.start()
	car1 = threading.Thread(target=car,args=("Tesla",))
	car1.start()


Queue队列
	import queue
	q=queue.put("d1")
	q.get()# 
	q.get_nowait()#
class queue.Queue(maxsize=0)
class queue.LifoQueue(maxsize=0)
class queue.PriorityQueue(maxsize=0)

生产者消费者模型
	 __author__ = "Alex Li"
	import threading,time

	import queue
	q = queue.Queue(maxsize=10)
	def Producer(name):
		count = 1
		while True:
			q.put("骨头%s" % count)
			print("生产了骨头",count)
			count +=1
			time.sleep(0.1)
	def  Consumer(name):
		#while q.qsize()>0:
		while True:
			print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
			time.sleep(1)
	p = threading.Thread(target=Producer,args=("Alex",))
	c = threading.Thread(target=Consumer,args=("ChengRonghua",))
	c1 = threading.Thread(target=Consumer,args=("王森",))
	p.start()
	c.start()
	c1.start()















	
	