#coding=utf-8
from hdfs import *

def main():
    client = InsecureClient("http://BIGDATA:50070",user="root")
    client.upload("/", "F:/BaiduNetdiskDownload/eclipse-SDK-4.6-win32-x86_64.zip",n_threads=2)

if __name__ == "__main__":
    main()