#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika
conn=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=conn.channel()
channel.exchange_declare(exchange='logs',type='fanout')
message='info:hello world!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
channel.basic_publish(
    #指定exchange名称
    exchange='logs',
    #未指定队列
    routing_key='',
    body=message
)
print(message)
conn.close()