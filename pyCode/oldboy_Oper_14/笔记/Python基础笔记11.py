RabbitMQ 消息队列
	默认端口 
	Linux启动：rabbitmq-server start
	连接远程mq需要用户和密码
	no_ack=False 服务器确认，如没有被处理完，服务器不会删掉消息
	消费者处理完成后手工确认：
		ch.basic_ack(delivery_tag=method.delivery_tag)
	服务器队列持久化,声明队列时加上参数durable=True-仅持久化队列
		channel.queue_declare(queue='Qname',durable=True)
	客户端：负载均衡，根据客户端处理能力分发消息
		处理完一条服务器端再发一条
		channel.basic_qos(prefetch_count=1)
	广播消息 fanout
	消息分类 directory
	主题划分 消息过滤 topic
		 服务端 主题类型+消息内容
		 客户端 接收主题的类型
Redis
	redis-cli启动命令行
		set name 11
		set age 22
		keys * #获取所有keys
		get name#获取值
	Redis连接池
	2亿用户实时在线统计,知道哪些用户在线
		setbit user 99999 1
		setbit user 88888 1
		bitcount user
		getbit user
	统计在线用户数，不关心那些用户在线
	incr login_users #计数加1
	decr login_users #计数减1
	RPC remote procedure call 远程函数调用
		
Mysql




