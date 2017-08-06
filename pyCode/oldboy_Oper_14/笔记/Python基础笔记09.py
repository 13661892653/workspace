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
Queue队列
	import queue
	q=queue.put("d1")
	q.get()# 
	q.get_nowait()#
class queue.Queue(maxsize=0)
class queue.LifoQueue(maxsize=0)
class queue.PriorityQueue(maxsize=0)

生产者消费者模型
	  














	
	