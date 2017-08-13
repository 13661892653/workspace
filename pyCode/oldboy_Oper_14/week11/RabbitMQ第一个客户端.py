#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika
import time
conn=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=conn.channel()
channel.queue_declare(queue='firstQueue')
def callback(ch,method,properties,body):
    print("-->",ch,method,properties)
    print("接收到如下消息",body)
    time.sleep(30)
channel.basic_consume(
    callback,
    queue='firstQueue',
    no_ack=False
)
print('Waiting for messages.')
channel.start_consuming()