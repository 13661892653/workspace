#coding=utf-8
from hdfs import *

def main():
    client = Client("http://BIGDATA:50070",timeout=1000)
    #upload(client)
    cat_hdfs_file(client)

def upload(client):
    #上传文件
    res_upload=client.upload("/", "F:/内部资料/大数据/Hadoop-day02-HDFS工作机制/01.自开发分布式数据采集系统--系统流程设计--采集任务逻辑实现.mp4", overwrite=True,n_threads=1)
    res_list =client.list("/")
    print(res_upload,res_list)

def cat_hdfs_file(client):
    #读取文件
    f=client.read('/logs/2018-05-28-09/access_log_0d9b716f-fa57-4a1c-b7c7-cc713afa5c67.log',encoding='gbk')
    with f as reader:
        print(reader.read())
if __name__ == "__main__":
    main()

