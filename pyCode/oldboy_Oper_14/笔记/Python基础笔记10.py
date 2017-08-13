 多进程
	target=run 此处不加括号
进程Queue
	from multiprocessing import Process,Queue 
管道Pipes
	parent,son=Pipe()
	parent.send('')#父亲发送
	son.rece()#儿子接收
进程同步
	lock=Lock()
	lock.acquire()
Managers
	共享list dict Event Queue等等
进程池
	callback=回调
	进程池中一定要先关闭进程池，在join
	pool.close()
	pool.join()
协程Coroutine
	微线程，是一种用户态的轻量级线程
	Greenlet封装好了的协程，自带直接用
	Gevent第三方库
事件驱动与异步IO
	事件驱动一个任务的执行，线程单独处理事件任务
Select\Poll\Epoll异步IO
	Epoll IO多路复用
	

	