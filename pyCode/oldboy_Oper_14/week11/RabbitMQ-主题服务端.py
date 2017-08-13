#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm 2017.1
import pika,sys
conn=pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel=conn.channel()
channel.exchange_declare(exchange='topic_logs'
                         ,type='topic')
serverity=sys.argv[1] if len(sys.argv)>1 else 'info'
message=' '.join(sys.argv[2:]) or 'hello world'
channel.basic_publish(
    #指定exchange名称
    exchange='topic_logs',
    #未指定队列
    routing_key=serverity,
    body=message
)
print(message)
conn.close()