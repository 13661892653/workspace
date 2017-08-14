#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
__author__='colby'
import pika
import time
conn = pika.BlockingConnection(pika.ConnectionParameters
                               (host='localhost')
                               )
channel=conn.channel()
channel.queue_declare(queue='rpc_Q')
#斐波拉契函数
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def on_request(ch,method,props,body):
    n=int(body)
    print('fib(%s)' % n)
    response=fib(n)
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request,queue='rpc_Q')
print('等待RPC消息请求...')
channel.start_consuming()
