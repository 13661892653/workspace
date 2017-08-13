#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika
conn=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=conn.channel()
channel.queue_declare(queue='firstQueue',durable=True)

def callback(ch,method,properties,body):
    print("-->",ch,method,properties)
    print("接收到如下消息",str(body).upper())
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    callback,
    queue='firstQueue',
    no_ack=False
)
print('Waiting for messages.')
channel.start_consuming()