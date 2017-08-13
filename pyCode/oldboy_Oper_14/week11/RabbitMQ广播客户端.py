#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika
#声明链接
conn=pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
#声明通道
channel=conn.channel()
#声明exchange类型为fanout
channel.exchange_declare(exchange='logs'
                         ,type='fanout')
#排他
result=channel.queue_declare(exclusive=True)
#获取队列名称
queue_name=result.method.queue
#绑定通道
channel.queue_bind(
    exchange='logs',
    queue=queue_name
)
def callback(ch,method,properties,body):
    print(body)
channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)
print('Waiting for messages.')
#启动
channel.start_consuming()