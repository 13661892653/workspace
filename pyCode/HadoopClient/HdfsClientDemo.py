#coding=utf-8
from hdfs import *

def main():
    client = Client("http://COLBY-NN-101:50070",timeout=1000)
    #upload(client)
    cat_hdfs_file(client)


def upload(client):
    res_upload=client.upload("/", "F:/BaiduNetdiskDownload/Adobe Acrobat DC Pro v17.009.20058.7z", overwrite=True,n_threads=1)
    res_list =client.list("/")
    print(res_upload,res_list)

def cat_hdfs_file(client):
    f=client.read('/logs/2018-05-27-17/access_log_243d2263-fc00-4255-a562-235469d17ef5.log',encoding='gbk')
    with f as reader:
        print(reader.read())
if __name__ == "__main__":
    main()

