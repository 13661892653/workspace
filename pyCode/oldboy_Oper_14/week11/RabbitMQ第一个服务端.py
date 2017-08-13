#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika
conn=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=conn.channel()
channel.queue_declare(queue='Q1')
channel.basic_publish(
    exchange='',
    routing_key='Q1',
    body='Hello world!',
    properties=pika.BasicProperties(
        delivery_mode=2,#消息持久化
    )
)
print("Send hello world!")
conn.close()